# Notion API JavaScript-Rendered Pages Fix

## Problem

The code-verification-qa agent discovered that 5 Notion API endpoint documentation files were nearly empty (64-74 bytes each) because they are JavaScript-rendered React Single Page Applications (SPAs).

### Root Cause

The original `notion-docs.py` script uses HTTP requests with the `requests` library to download HTML. For these 5 specific pages:

1. The `<article id="content">` tag exists in the raw HTML but is **empty**
2. Content is rendered **client-side** by JavaScript/React after page load
3. The HTTP-based extraction only sees the empty article tag, resulting in nearly-empty markdown files

### Affected Files

1. `notion/complete-a-file-upload.md` (was 74 bytes)
2. `notion/introspect-token.md` (was 68 bytes)
3. `notion/list-file-uploads.md` (was 69 bytes)
4. `notion/retrieve-a-file-upload.md` (was 74 bytes)
5. `notion/revoke-token.md` (was 64 bytes)

## Solution

Used **Playwright MCP** (Model Context Protocol) to render pages with JavaScript enabled and extract the actual content.

### Process

1. **Navigate** to each URL with Playwright (JavaScript rendering enabled)
2. **Wait** for content to render
3. **Extract** visible text content from the rendered page
4. **Parse** the API documentation structure (method, endpoint, parameters, responses)
5. **Format** as markdown with proper structure
6. **Save** to the markdown files

### Results

All 5 files now contain complete API documentation:

| File | Old Size | New Size | Improvement |
|------|----------|----------|-------------|
| complete-a-file-upload.md | 74 bytes | 776 bytes | **10.5x** |
| introspect-token.md | 68 bytes | 882 bytes | **13x** |
| list-file-uploads.md | 69 bytes | 1.2 KB | **17x** |
| retrieve-a-file-upload.md | 74 bytes | 1.1 KB | **15x** |
| revoke-token.md | 64 bytes | 624 bytes | **9.8x** |

### Content Now Includes

- HTTP method and endpoint URL
- API description
- Parameters (headers, query params, body params)
- Response schemas with examples
- Navigation links to related endpoints

## Technical Details

### Why Header Removal Wasn't the Issue

Initial investigation focused on line 34 of `notion-docs.py` which removes `<header>` tags. However:

1. The script correctly looks for `<article id="content">` first
2. For these pages, the article tag exists but is **empty in raw HTML**
3. The content appears in `<header class="headline-container...">` but **only after JavaScript renders it**
4. BeautifulSoup never sees this content because it's not in the initial HTTP response

### Detection Method

To detect JavaScript-rendered pages:

```python
article_match = re.search(r'<article[^>]*id="content"[^>]*>(.*?)</article>', html, re.DOTALL)
if article_match:
    article_content = article_match.group(1).strip()
    # If article is empty or only has modal wrappers, it's JS-rendered
    if not article_content or article_content.count('<div') <= 2:
        # Use Playwright instead
```

## Files Created

1. `fix-empty-notion-files.py` - Analysis script showing the problem
2. `fix-js-rendered-notion-pages.py` - Framework for Playwright-based extraction
3. `playwright-extract-notion.sh` - Shell script template
4. `NOTION_JS_RENDERED_FIX.md` - This documentation

## Future Prevention

For any new Notion API pages added:

1. Check file size after extraction (< 100 bytes is suspicious)
2. Verify article content is not empty in raw HTML
3. Use Playwright MCP for any JavaScript-rendered pages

## Implementation Code

The actual extraction was done interactively using Playwright MCP tools:

```python
# For each URL:
mcp__playwright__playwright_navigate(url)
text = mcp__playwright__playwright_get_visible_text()
# Parse text and extract API documentation structure
# Format as markdown
# Save to file
```

## Verification

All 5 files now pass content verification:
- ✅ File size > 500 bytes
- ✅ Contains HTTP method and endpoint
- ✅ Contains parameter documentation
- ✅ Contains response information
- ✅ Proper markdown structure
