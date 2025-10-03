# LLM Code Documentation Repository - Project Context

## Project Overview
This is a centralized repository for AI-readable documentation extracted from various codebases and frameworks. The repository provides automated tools to keep documentation current and comprehensive.

## Current Status
- ✅ CircuitPython documentation extraction (complete)
- ✅ Claude Code SDK documentation extraction (complete)
- 🔄 Notion API documentation extraction (in progress - migrating to Crawl4AI)
- ⏳ Perplexity documentation extraction (planned)
- ⏳ OpenRouter models API extraction (planned)

## Architecture

### Documentation Sets
- `/circuitpython/` - MicroPython for microcontrollers documentation
- `/claude-code-sdk/` - Claude Code development tools documentation
- `/notion/` - Notion API reference documentation (71 pages)
- `/textual/` - Textual TUI framework documentation
- Future: `/perplexity/`, `/openrouter/`

### Update Scripts (`/update-scripts/`)
- `extract_docs.py` - Git repository documentation extractor (CircuitPython)
- `claude-code-sdk-docs.py` - Claude Code SDK downloader with live sidebar extraction
- `notion-docs-crawl4ai.py` - Crawl4AI-based Notion API extractor (NEW - handles JS-rendered content)
- `notion-docs.py` - DEPRECATED - Old HTTP-based extractor with incompleteness issues
- `notion-docs-playwright.py` - DEPRECATED - Playwright attempt with incomplete extraction
- `update.sh` - Master update script for all documentation

### Configuration
- `repo_config.yaml` - Git repository extraction configuration
- `notion-api-links.txt` - Cached list of 71 Notion API URLs

## Task Management

### todo.txt Structure
The project uses a comprehensive `todo.txt` file with 21 tasks organized in 3 phases:
1. **Phase 0** (Task 0): Current state validation
2. **Phase 1** (Tasks 1-8): Complete Notion API extraction with Crawl4AI
3. **Phase 2** (Tasks 9-15): Perplexity documentation extraction
4. **Phase 3** (Tasks 16-20): OpenRouter models API extraction

### Task Execution Guidelines
- Tasks are designed for independent agents to execute serially
- Each task is self-contained with complete context and instructions
- Testing is integrated into each task (not separate)
- Tasks include detailed verification steps and success criteria
- Use `[ ]` for pending, `[-]` for in progress, `[x]` for complete

## Critical Context: Notion Extraction Evolution

### Problem History
1. **First attempt**: `notion-docs.py` using requests + BeautifulSoup + pandoc
   - Issue: Missed collapsible sections, JavaScript-rendered content
   - Result: Incomplete files (block.md only 40KB, 0 example matches)

2. **Second attempt**: `notion-docs-playwright.py` using Playwright browser automation
   - Issue: Still incomplete extraction, missing expanded sections
   - Result: Partial improvement but not complete

3. **Current solution**: `notion-docs-crawl4ai.py` using Crawl4AI framework
   - Fully renders JavaScript content
   - Expands all collapsible sections
   - Expected: Complete content capture (block.md >100KB, multiple examples)

### Key Files to Monitor
- `notion/block.md` - Critical test file (should be >100KB with examples)
- `notion/page.md` - Should be >15KB
- `notion/database.md` - Should be >15KB
- Files previously problematic: create-a-data-source.md, create-a-file-upload.md, revoke-token.md, introspect-token.md

## Development Workflow

### When Working on Extraction Scripts
1. **Always test on 3 sample pages first** (block, page, intro)
2. **Verify completeness** before full extraction:
   - File size significantly larger
   - Code examples present (grep for "example", "```")
   - Visual inspection of markdown quality
3. **Back up before major changes**: Use `git stash push -m 'description' path/`
4. **Full extraction only after sample validation**
5. **Comprehensive QA on all files** after full extraction

### Quality Assurance Checklist
- [ ] File sizes appropriate (>2KB minimum, critical files >15KB)
- [ ] Source headers present (`# Source: URL`)
- [ ] Code examples present (grep for ``` markers)
- [ ] No extraction artifacts (javascript:, void(0), CSS classes)
- [ ] Markdown formatting correct (headers, lists, tables)
- [ ] Content completeness (compare with live pages)

### Testing Sub-Agents
When delegating to sub-agents:
- **task-research-analyst**: Research approaches, analyze patterns
- **task-executor**: Implement scripts, run extractions
- **code-verification-qa**: Verify quality, test functionality
- **git-cleanup-agent**: Clean up obsolete files before commits

## Dependencies

### Required Python Packages
- `beautifulsoup4` - HTML parsing
- `requests` - HTTP requests
- `pyyaml` - Configuration parsing
- `crawl4ai` - Modern web crawling with JS rendering (for Notion)
- `playwright` - Browser automation (optional, for complex pages)

### System Requirements
- `pandoc` - HTML to Markdown conversion
- `git` - Version control and repository cloning
- Python 3.8+

## API Keys and Configuration

### Environment Variables
- `OPENROUTER_API_KEY` - Required for OpenRouter models extraction
- May be in: `~/.bashrc`, `~/.zshrc`, `~/.config/openrouter/config`

### MCP Tools Available
- Playwright MCP tools for browser automation
- Perplexity MCP for research and documentation queries
- Joplin MCP for note-taking (optional)

## Common Commands

### Run Specific Extraction
```bash
# Update CircuitPython docs
python3 update-scripts/extract_docs.py

# Update Claude Code SDK docs
python3 update-scripts/claude-code-sdk-docs.py

# Update Notion docs (new Crawl4AI approach)
python3 update-scripts/notion-docs-crawl4ai.py

# Update all documentation
./update-scripts/update.sh
```

### Verify Documentation Quality
```bash
# Check file sizes
ls -lh notion/*.md | awk '{print $5, $9}' | sort -h

# Count files
ls -1 notion/*.md | wc -l

# Check for examples
grep -l "example" -i notion/*.md | wc -l

# Check for code blocks
grep -l '```' notion/*.md | wc -l
```

### Backup and Restore
```bash
# Backup before major changes
git stash push -m 'Pre-extraction backup' notion/

# Restore if needed
git stash pop
```

## Project Goals
1. Provide comprehensive, AI-readable documentation for multiple frameworks
2. Automate documentation updates to stay current with source projects
3. Ensure complete content capture (no missing sections or examples)
4. Maintain high quality markdown formatting
5. Enable easy addition of new documentation sources

## Success Criteria
- All extraction scripts run without errors
- Documentation files are complete with examples and schemas
- File sizes indicate comprehensive content capture
- Markdown is clean, readable, and well-formatted
- Automated updates work reliably
- Documentation stays synchronized with upstream sources

---

**Last Updated**: 2025-10-02
**Current Focus**: Completing Notion API extraction with Crawl4AI, then adding Perplexity and OpenRouter documentation
