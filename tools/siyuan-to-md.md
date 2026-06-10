# siyuan-to-md

Converts SiYuan `.sy` JSON files to clean Markdown.

SiYuan stores documents in a JSON-based block format. This tool extracts the content and converts it to standard Markdown for use with LLMs and other tools.

## Usage

```bash
# Convert a single file
python siyuan_to_md.py input.sy output.md

# Convert a directory recursively
python siyuan_to_md.py input_dir/ output_dir/
```

## Supported Node Types

- `NodeDocument` - Document root with title
- `NodeHeading` - Headings (H1-H6)
- `NodeParagraph` - Paragraphs
- `NodeText` - Plain text
- `NodeCodeSpan` - Inline code
- `NodeCodeBlock` - Code blocks
- `NodeKbd` - Keyboard shortcuts
- `NodeList` - Ordered and unordered lists
- `NodeListItem` - List items
- `NodeBlockquote` - Block quotes
- `NodeLink` - Links
- `NodeImage` - Images
- `NodeEmphasis` - Italic text
- `NodeStrong` - Bold text
- `NodeStrikethrough` - Strikethrough text
- `NodeMark` - Highlighted text
- `NodeTable` - Tables

## License

MIT
