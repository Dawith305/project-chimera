# Tooling Strategy — Project Chimera

**Version:** 1.0  
**Date:** February 5, 2026  
**Traceability:** Task 2.3 Sub-Task A, specs/_meta.md §2.2

---

## 1. Overview

This document defines the **Developer Tools (MCP)** strategy for Project Chimera. These MCP servers help *you* (the developer) build, test, and govern the agentic infrastructure — they are distinct from **Runtime Skills**, which empower the Chimera agents at execution time.

| Category | Purpose | Consumer |
|----------|---------|----------|
| **Developer Tools (MCP)** | Version control, file editing, testing, governance | Human developer + IDE agent |
| **Runtime Skills** | Content generation, trend fetching, social publishing | Chimera Planner/Worker/Judge agents |

---

## 2. Developer MCP Servers (Recommended)

### 2.1 Tenx MCP Sense (Required)

| Attribute | Value |
|-----------|-------|
| **Purpose** | Traceability and "Black Box" flight recorder |
| **Status** | Already configured (see `.cursor/mcp.json`) |
| **Why** | Challenge requirement; captures development telemetry for assessment |

**Configuration:** `tenxfeedbackanalytics` proxy at `https://mcppulse.10academy.org/proxy`

---

### 2.2 Git MCP Server

| Attribute | Value |
|-----------|-------|
| **Purpose** | Version control operations from the IDE agent |
| **Package** | `mcp-server-git` (or equivalent) |
| **Tools** | `git_status`, `git_diff`, `git_log`, `git_add`, `git_commit`, `git_checkout`, `git_create_branch`, `git_reset`, `git_show` |

**Use cases:**
- Inspect repo state without leaving the chat
- Compare branches, view diffs
- Create branches, stage files (commit still run by user from external terminal per project rules)

**Installation (example):**
```bash
# Via uv
uv add mcp-server-git

# Or npm
npx -y @modelcontextprotocol/server-git
```

**Note:** Per `.cursor/rules/git-commits.mdc`, the AI must not run `git commit` or `git commit --amend` from Cursor's terminal. The Git MCP can still support `git_status`, `git_diff`, `git_log`, and `git_add`.

---

### 2.3 Filesystem MCP Server

| Attribute | Value |
|-----------|-------|
| **Purpose** | File read/write, directory listing, search |
| **Package** | `@modelcontextprotocol/server-filesystem` (or equivalent) |
| **Tools** | `read_file`, `read_multiple_files`, `write_file`, `edit_file`, `list_directory`, `create_directory`, `search_files`, `move_file` |

**Use cases:**
- Read specs, configs, and code across the repo
- Create or edit files with structured diffs
- Search for patterns (e.g. "find all references to task_id")
- Restricted to allowed directories for security

**Installation (example):**
```bash
npx -y @modelcontextprotocol/server-filesystem /path/to/project-chimera
```

**Security:** Configure `allowedDirectories` to scope access to the project root only.

---

### 2.4 Database MCP (Optional, for later phases)

| Attribute | Value |
|-----------|-------|
| **Purpose** | Query Postgres, Redis, or Weaviate during development |
| **Package** | `mcp-server-postgres`, `mcp-server-sqlite`, or similar |
| **Use cases** | Validate schema, inspect test data, debug queries |

**Status:** Defer until Task 3 (TDD, Docker) when database services are containerized.

---

### 2.5 Browser MCP (Optional)

| Attribute | Value |
|-----------|-------|
| **Purpose** | Navigate, snapshot, and interact with web UIs |
| **Package** | `@modelcontextprotocol/server-puppeteer` or similar |
| **Use cases** | Test dashboard, HITL interface, OpenClaw integration flows |

**Status:** Defer until UI components exist.

---

## 3. MCP Configuration Layout

Recommended `.cursor/mcp.json` structure (extend existing):

```json
{
  "mcpServers": {
    "tenxfeedbackanalytics": {
      "name": "tenxanalysismcp",
      "url": "https://mcppulse.10academy.org/proxy",
      "headers": {
        "X-Device": "mac",
        "X-Coding-Tool": "cursor"
      }
    },
    "git": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-git", "/path/to/project-chimera"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/project-chimera"]
    }
  }
}
```

Replace `/path/to/project-chimera` with the actual project root.

---

## 4. Separation of Concerns

| Tool Type | Example | Used By |
|-----------|---------|---------|
| **Developer MCP** | git-mcp, filesystem-mcp, Tenx Sense | You + IDE co-pilot |
| **Runtime MCP** | mcp-server-twitter, mcp-server-weaviate, mcp-server-ideogram | Chimera agents (Planner, Worker, Judge) |
| **Runtime Skill** | skill_fetch_trends, skill_transcribe_audio | Chimera agents (via internal functions) |

Runtime MCPs and Skills are documented in `specs/technical.md` and `skills/README.md`.

---

## 5. Next Steps

1. Add `git` and `filesystem` MCP servers to `.cursor/mcp.json` when ready.
2. Verify Tenx MCP Sense remains connected.
3. Document any Runtime MCP servers in `specs/technical.md` as they are adopted.
4. Implement Skills per `skills/README.md` contracts.
