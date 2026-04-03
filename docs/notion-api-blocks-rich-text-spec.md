# Notion API: Blocks & Rich Text Specification

**Last updated**: 2026-04-01  
**Source**: https://developers.notion.com/reference/block, https://developers.notion.com/reference/rich-text

This is a practical API reference for creating and updating content via the Notion API. Focus: exact field names, values, and structures.

---

## Quick Reference: Block Types

| Block Type | API Field | Has Rich Text? | Supports Children? | Notes |
|-----------|-----------|---------------|--------------------|-------|
| Paragraph | `paragraph` | Yes | Yes | Basic text block |
| Heading 1-4 | `heading_1`, `heading_2`, `heading_3`, `heading_4` | Yes | No (toggleable as option) | `is_toggleable` can make them containers |
| Bulleted List Item | `bulleted_list_item` | Yes | Yes | Auto-nests; list structure handled by API |
| Numbered List Item | `numbered_list_item` | Yes | Yes | `list_start_index`, `list_format` on first item |
| To Do | `to_do` | Yes | Yes | `checked` boolean |
| Toggle | `toggle` | Yes | Yes | Collapsible container |
| Quote | `quote` | Yes | Yes | — |
| Callout | `callout` | Yes | No | Requires `icon` object |
| Code | `code` | Yes (in `rich_text`) | No | `language` field, `caption` optional |
| Divider | `divider` | No | No | Empty object `{}` |
| Bookmark | `bookmark` | Yes (in `caption`) | No | `url` required |
| Table | `table` | No | No | `table_width` immutable; contains `table_row` children |
| Table Row | `table_row` | No (cells are rich text arrays) | No | `cells` is `[[richtext], [richtext], ...]` |
| Image | `image` | No | No | Type: `external`, `file`, `file_upload` |
| Audio | `audio` | No | No | Type: `external`, `file`, `file_upload` |
| Video | `video` | No | No | Type: `external`, `file`, `file_upload` |
| File/PDF | `file`, `pdf` | Yes (in `caption`) | No | `caption` optional, type determines source |
| Embed | `embed` | No | No | `url` required |
| Link Preview | `link_preview` | No | No | `url` required; generates preview |
| Equation | `equation` | No | No | `expression` (KaTeX compatible) |
| Column List | `column_list` | No | Yes | Contains `column` blocks only |
| Column | `column` | No | Yes | Has `width_ratio` (0-1) |
| Synced Block | `synced_block` | No | Yes | Original has `synced_from: null`; duplicates reference original |
| Child Page | `child_page` | No | No | `title` string (plain text) |
| Child Database | `child_database` | No | No | `title` string (plain text) |
| Breadcrumb | `breadcrumb` | No | No | Empty object `{}` |
| Table of Contents | `table_of_contents` | No | No | `color` field only |
| Template | `template` | Yes | Yes | `rich_text` for title, `children` duplicated on use |
| Tab | `tab` | No | Yes | Empty object `{}`; metadata via paragraph children |
| Meeting Notes | `meeting_notes` | Yes (in `title`) | Yes | `status`, `calendar_event`, `recording` fields |
| Transcription | `transcription` | No | Yes | Auto-generated from meeting; read-only |
| Unsupported | `unsupported` | No | No | API-unspported block; has `block_type` field |

---

## Rich Text Structure

### Rich Text Object

Every `rich_text` array contains objects with this structure:

```json
{
  "type": "text",
  "text": {
    "content": "Your text here",
    "link": null
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "Your text here",
  "href": null
}
```

### Rich Text Types

#### Text Type

```json
{
  "type": "text",
  "text": {
    "content": "Some words",
    "link": null  // or { "url": "https://example.com" }
  },
  "annotations": { /* see below */ },
  "plain_text": "Some words",
  "href": null  // auto-populated if link present
}
```

#### Mention Type

```json
{
  "type": "mention",
  "mention": {
    "type": "user|date|page|database|link_preview|template_mention",
    // ... type-specific object
  },
  "annotations": { /* see below */ },
  "plain_text": "@...",
  "href": null
}
```

**Mention subtypes:**

- **`user`**: `"mention": { "type": "user", "user": { "object": "user", "id": "uuid" } }`
- **`date`**: `"mention": { "type": "date", "date": { "start": "2024-01-15", "end": null, "time_zone": null } }`
- **`page`**: `"mention": { "type": "page", "page": { "id": "uuid" } }`
- **`database`**: `"mention": { "type": "database", "database": { "id": "uuid" } }`
- **`link_preview`**: `"mention": { "type": "link_preview", "link_preview": { "url": "https://..." } }`
- **`template_mention`** (date): `"mention": { "type": "template_mention", "template_mention": { "type": "template_mention_date", "template_mention_date": "today|now" } }`
- **`template_mention`** (user): `"mention": { "type": "template_mention", "template_mention": { "type": "template_mention_user", "template_mention_user": "me" } }`

#### Equation Type

```json
{
  "type": "equation",
  "equation": {
    "expression": "E = mc^2"  // KaTeX compatible
  },
  "annotations": { /* see below */ },
  "plain_text": "E = mc^2",
  "href": null
}
```

### Annotations Object

**All booleans:**

```json
{
  "bold": false,
  "italic": false,
  "strikethrough": false,
  "underline": false,
  "code": false,
  "color": "default"
}
```

**Color values** (for `color` field):
- Text colors: `"default"`, `"gray"`, `"brown"`, `"orange"`, `"yellow"`, `"green"`, `"blue"`, `"purple"`, `"pink"`, `"red"`
- Background colors: same as above with `_background` suffix (e.g., `"gray_background"`, `"blue_background"`)

---

## Block Type Structures

### Text Blocks (Paragraph, Headings, Lists, Callout, Quote, etc.)

```json
{
  "type": "paragraph",
  "paragraph": {
    "rich_text": [
      {
        "type": "text",
        "text": {
          "content": "Your content",
          "link": null
        },
        "annotations": { /* annotation object */ },
        "plain_text": "Your content",
        "href": null
      }
    ],
    "color": "default",
    "children": [ /* optional child blocks */ ]
  }
}
```

**Color values for block-level (same for headings, lists, quotes, callouts, to_do, toggle):**
- `"default"`, `"gray"`, `"brown"`, `"orange"`, `"yellow"`, `"green"`, `"blue"`, `"purple"`, `"pink"`, `"red"`
- Plus background versions: `"gray_background"`, `"blue_background"`, etc.

### Headings

```json
{
  "type": "heading_1",  // or heading_2, heading_3, heading_4
  "heading_1": {
    "rich_text": [ /* rich text array */ ],
    "color": "default",
    "is_toggleable": false  // set true to make heading a collapsible container
  }
}
```

### Bulleted & Numbered List Items

```json
{
  "type": "bulleted_list_item",
  "bulleted_list_item": {
    "rich_text": [ /* rich text array */ ],
    "color": "default",
    "children": [ /* optional nested items */ ]
  }
}
```

**Numbered list** (same structure, additional fields on first item):

```json
{
  "type": "numbered_list_item",
  "numbered_list_item": {
    "rich_text": [ /* rich text array */ ],
    "color": "default",
    "list_start_index": 1,  // only on first item, defaults to 1
    "list_format": "numbers",  // "numbers", "letters", or "roman"
    "children": [ /* optional nested items */ ]
  }
}
```

### To Do

```json
{
  "type": "to_do",
  "to_do": {
    "rich_text": [ /* rich text array */ ],
    "checked": false,  // boolean
    "color": "default",
    "children": [ /* optional */ ]
  }
}
```

### Toggle

```json
{
  "type": "toggle",
  "toggle": {
    "rich_text": [ /* rich text array */ ],
    "color": "default",
    "children": [ /* nested blocks */ ]
  }
}
```

### Quote

```json
{
  "type": "quote",
  "quote": {
    "rich_text": [ /* rich text array */ ],
    "color": "default",
    "children": [ /* optional */ ]
  }
}
```

### Callout

```json
{
  "type": "callout",
  "callout": {
    "rich_text": [ /* rich text array */ ],
    "icon": {
      "type": "emoji",
      "emoji": "🎉"  // any unicode emoji
      // OR
      // "type": "file",
      // "file": { "url": "https://..." }
    },
    "color": "default"
  }
}
```

### Code Block

```json
{
  "type": "code",
  "code": {
    "rich_text": [ /* rich text array */ ],
    "language": "python",  // see language list below
    "caption": [ /* optional rich text for caption */ ]
  }
}
```

**Language values** (complete list):
`"abap"`, `"arduino"`, `"bash"`, `"basic"`, `"c"`, `"clojure"`, `"coffeescript"`, `"c++"`, `"c#"`, `"css"`, `"dart"`, `"diff"`, `"docker"`, `"elixir"`, `"elm"`, `"erlang"`, `"flow"`, `"fortran"`, `"f#"`, `"gherkin"`, `"glsl"`, `"go"`, `"graphql"`, `"groovy"`, `"haskell"`, `"html"`, `"java"`, `"javascript"`, `"json"`, `"julia"`, `"kotlin"`, `"latex"`, `"less"`, `"lisp"`, `"livescript"`, `"lua"`, `"makefile"`, `"markdown"`, `"markup"`, `"matlab"`, `"mermaid"`, `"nix"`, `"objective-c"`, `"ocaml"`, `"pascal"`, `"perl"`, `"php"`, `"plain text"`, `"powershell"`, `"prolog"`, `"protobuf"`, `"python"`, `"r"`, `"reason"`, `"ruby"`, `"rust"`, `"sass"`, `"scala"`, `"scheme"`, `"scss"`, `"shell"`, `"sql"`, `"swift"`, `"typescript"`, `"vb.net"`, `"verilog"`, `"vhdl"`, `"visual basic"`, `"webassembly"`, `"xml"`, `"yaml"`, `"java/c/c++/c#"`

### Divider

```json
{
  "type": "divider",
  "divider": {}
}
```

### Breadcrumb

```json
{
  "type": "breadcrumb",
  "breadcrumb": {}
}
```

### Table of Contents

```json
{
  "type": "table_of_contents",
  "table_of_contents": {
    "color": "default"
  }
}
```

### Bookmark

```json
{
  "type": "bookmark",
  "bookmark": {
    "url": "https://example.com",
    "caption": [ /* optional rich text */ ]
  }
}
```

### Image / Audio / Video

```json
{
  "type": "image",
  "image": {
    "type": "external",  // or "file", "file_upload"
    "external": {
      "url": "https://example.com/image.png"
    }
    // OR for file uploads:
    // "file_upload": { "id": "upload_id" }
  }
}
```

**Image types** (external): `.bmp`, `.gif`, `.heic`, `.jpeg`, `.jpg`, `.png`, `.svg`, `.tif`, `.tiff`

**Audio types** (external): `.mp3`, `.wav`, `.ogg`, `.oga`, `.m4a`

**Video types** (external): `.amv`, `.asf`, `.avi`, `.f4v`, `.flv`, `.gifv`, `.mkv`, `.mov`, `.mpg`, `.mpeg`, `.mpv`, `.mp4`, `.m4v`, `.qt`, `.wmv`

**Embed URLs**:
- YouTube: `https://www.youtube.com/watch?v=[id]` or `https://www.youtube.com/embed/[id]`

### File / PDF

```json
{
  "type": "file",
  "file": {
    "type": "external",  // or "file", "file_upload"
    "external": {
      "url": "https://example.com/document.pdf"
    },
    "caption": [ /* optional */ ],
    "name": "document.pdf"  // optional; auto-appended if omitted
  }
}
```

### Embed

```json
{
  "type": "embed",
  "embed": {
    "url": "https://example.com"
  }
}
```

### Link Preview

```json
{
  "type": "link_preview",
  "link_preview": {
    "url": "https://github.com/example/repo/pull/1234"
  }
}
```

### Equation

```json
{
  "type": "equation",
  "equation": {
    "expression": "e=mc^2"  // KaTeX compatible
  }
}
```

### Table

```json
{
  "type": "table",
  "table": {
    "table_width": 3,  // immutable after creation
    "has_column_header": true,
    "has_row_header": false
  }
}
```

**Then add children as `table_row` blocks.**

### Table Row

```json
{
  "type": "table_row",
  "table_row": {
    "cells": [
      [ /* rich text array for cell 1 */ ],
      [ /* rich text array for cell 2 */ ],
      [ /* rich text array for cell 3 */ ]
    ]
  }
}
```

**Note**: Cell count must match `table_width` from parent table.

### Column List & Column

```json
{
  "type": "column_list",
  "column_list": {}
}
```

**Children are `column` blocks:**

```json
{
  "type": "column",
  "column": {
    "width_ratio": 0.5  // 0-1 float; proportional width
  }
}
```

### Synced Block

**Original synced block:**

```json
{
  "type": "synced_block",
  "synced_block": {
    "synced_from": null,  // signals this is original
    "children": [ /* blocks to sync */ ]
  }
}
```

**Duplicate synced block:**

```json
{
  "type": "synced_block",
  "synced_block": {
    "synced_from": {
      "type": "block_id",
      "block_id": "uuid-of-original-block"
    }
  }
}
```

### Child Page

```json
{
  "type": "child_page",
  "child_page": {
    "title": "Page Title"  // plain text string, not rich text
  }
}
```

### Child Database

```json
{
  "type": "child_database",
  "child_database": {
    "title": "Database Title"  // plain text string
  }
}
```

### Template

```json
{
  "type": "template",
  "template": {
    "rich_text": [ /* rich text array */ ],
    "children": [ /* blocks duplicated on template use */ ]
  }
}
```

### Tab

```json
{
  "type": "tab",
  "tab": {}
}
```

**Metadata via paragraph children** with `icon` field:

```json
{
  "type": "paragraph",
  "paragraph": {
    "icon": { "type": "emoji", "emoji": "📌" },
    "rich_text": [ /* tab title */ ],
    "children": [ /* tab content */ ]
  }
}
```

### Meeting Notes

```json
{
  "type": "meeting_notes",
  "meeting_notes": {
    "title": [ /* rich text array */ ],
    "status": "notes_ready",  // "transcription_not_started", "transcription_paused", "transcription_in_progress", "summary_in_progress", "notes_ready"
    "children": { /* pointers to related blocks */ },
    "calendar_event": {
      "start_time": "2024-01-15T10:00:00.000Z",
      "end_time": "2024-01-15T10:45:00.000Z",
      "attendees": [ /* optional array of user IDs */ ]
    },
    "recording": {
      "start_time": "2024-01-15T10:00:00.000Z",
      "end_time": "2024-01-15T10:45:00.000Z"
    }
  }
}
```

### Unsupported

```json
{
  "type": "unsupported",
  "unsupported": {
    "block_type": "form"  // or "button", "drive", etc.
  }
}
```

---

## Callout Icons

Callout `icon` field accepts:

```json
{
  "type": "emoji",
  "emoji": "🎉"  // any valid unicode emoji
}
```

Or external file:

```json
{
  "type": "file",
  "file": { "url": "https://example.com/icon.png" }
}
```

---

## Color Reference

### Exact Strings for Colors

**Text foreground & block colors** (same values):
- Neutral: `"default"`, `"gray"`
- Warm: `"brown"`, `"orange"`, `"yellow"`
- Cool: `"green"`, `"blue"`, `"purple"`, `"pink"`, `"red"`
- Backgrounds (append `_background`): `"gray_background"`, `"brown_background"`, `"orange_background"`, `"yellow_background"`, `"green_background"`, `"blue_background"`, `"purple_background"`, `"pink_background"`, `"red_background"`

**No custom hex colors via API** — use the enum values above.

---

## Nesting & Children

### Block Types That Support Children

- `paragraph`
- `bulleted_list_item`
- `numbered_list_item`
- `to_do`
- `toggle`
- `quote`
- `heading_1`, `heading_2`, `heading_3`, `heading_4` (when `is_toggleable: true`)
- `column_list` (contains `column` blocks)
- `column` (can contain any block)
- `synced_block`
- `template`
- `tab` (content via paragraph children with icon)
- `meeting_notes`

### How to Add Children

When creating a block, include `children` array:

```json
{
  "type": "paragraph",
  "paragraph": {
    "rich_text": [ /* ... */ ],
    "children": [
      {
        "type": "paragraph",
        "paragraph": {
          "rich_text": [ /* ... */ ]
        }
      }
    ]
  }
}
```

**Note**: Nesting depth supported by API is unlimited, but UI may have practical limits.

---

## Markdown-like Syntax vs. Structured Objects

### What the API Requires Structured Objects For

- **Lists**: Must use `bulleted_list_item` / `numbered_list_item` blocks (not nested text with markdown-style `- ` prefix)
- **Headings**: Must use `heading_1`, `heading_2`, etc. blocks (not `# ` prefix in text)
- **Code blocks**: Must use `code` block type with `language` field (not triple backticks)
- **Links**: Must be in rich text `text` object's `link` field (not `[text](url)` syntax)
- **Callouts**: Must be `callout` block type (not `> ` blockquote syntax)
- **Bold, italic, etc.**: Must be in `annotations` object (not `**text**` or `_text_`)
- **Dividers**: Must be `divider` block type (not `---`)
- **Tables**: Must be `table` block with `table_row` children (not ASCII tables)

### Plain Markdown You Can Put in Text Content

The `content` field in rich text can include:
- Regular text
- Newlines (though usually blocks represent structure instead)
- Unicode emoji

**But formatting must be done via `annotations` and `link` fields, not markdown syntax.**

---

## Limits & Constraints

### Known Limits

| Item | Limit | Notes |
|------|-------|-------|
| Rich text array | Depends on request size | No documented hard limit; test responsiveness |
| Blocks per request | No documented limit | Practical: test with 100+ |
| Nesting depth | Unlimited (API-side) | UI may have practical limits |
| Text content length | No documented limit | Test with very large content |
| Table width | Immutable after creation | Set at creation time; cannot change `table_width` |
| Table rows | No documented limit | Test with large datasets |
| Code language values | ~60 supported | See language list above |
| Color values | 16 + 8 backgrounds | Only enum values; no hex or custom colors |

### Pagination & Retrieval

- When retrieving blocks with children, use pagination to fetch large child arrays
- `start_cursor` and `end_cursor` in responses for pagination

---

## Common Patterns

### Creating a Rich Text Array

```python
# Python example
def create_rich_text(content, bold=False, link=None):
    return {
        "type": "text",
        "text": {
            "content": content,
            "link": {"url": link} if link else None
        },
        "annotations": {
            "bold": bold,
            "italic": False,
            "strikethrough": False,
            "underline": False,
            "code": False,
            "color": "default"
        }
    }
```

### Creating a Paragraph with Color

```json
{
  "type": "paragraph",
  "paragraph": {
    "rich_text": [
      {
        "type": "text",
        "text": {
          "content": "Red text paragraph",
          "link": null
        },
        "annotations": {
          "bold": false,
          "italic": false,
          "strikethrough": false,
          "underline": false,
          "code": false,
          "color": "red"
        }
      }
    ],
    "color": "default"  // block background, not text color
  }
}
```

### Creating a Numbered List

```json
[
  {
    "type": "numbered_list_item",
    "numbered_list_item": {
      "rich_text": [{"type": "text", "text": {"content": "First", "link": null}}],
      "color": "default",
      "list_start_index": 1,
      "list_format": "numbers"
    }
  },
  {
    "type": "numbered_list_item",
    "numbered_list_item": {
      "rich_text": [{"type": "text", "text": {"content": "Second", "link": null}}],
      "color": "default"
    }
  }
]
```

### Creating a Table

```json
[
  {
    "type": "table",
    "table": {
      "table_width": 2,
      "has_column_header": true,
      "has_row_header": false
    }
  },
  {
    "type": "table_row",
    "table_row": {
      "cells": [
        [{"type": "text", "text": {"content": "Header 1", "link": null}}],
        [{"type": "text", "text": {"content": "Header 2", "link": null}}]
      ]
    }
  },
  {
    "type": "table_row",
    "table_row": {
      "cells": [
        [{"type": "text", "text": {"content": "Cell 1", "link": null}}],
        [{"type": "text", "text": {"content": "Cell 2", "link": null}}]
      ]
    }
  }
]
```

---

## Icon & Emoji Support

### Where Icons Appear

- **Callout**: `callout.icon`
- **Paragraph** (inside tabs): `paragraph.icon`

### Icon Structure

**Emoji:**
```json
{
  "type": "emoji",
  "emoji": "🎉"
}
```

**File/External:**
```json
{
  "type": "file",
  "file": {
    "url": "https://example.com/icon.png"
  }
}
```

---

## Response Behavior

When you create/update a block, the API response includes:

- `id`: UUIDv4 of the block
- `type`: Block type
- `{type}`: Block type object (same structure you sent)
- `created_time`, `last_edited_time`: ISO 8601 timestamps
- `created_by`, `last_edited_by`: User objects
- `parent`: Parent reference (page, block, database, etc.)
- `has_children`: Boolean
- `in_trash`: Boolean

**For file uploads**, the response changes `file_upload` to `file` with a temporary `url` and `expiry_time`.

---

## Further Reference

- **Official Blocks Docs**: https://developers.notion.com/reference/block
- **Official Rich Text Docs**: https://developers.notion.com/reference/rich-text
- **Create Page with Blocks**: https://developers.notion.com/reference/create-a-page
- **Update Block**: https://developers.notion.com/reference/update-a-block
