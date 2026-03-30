bat::config
# Struct Config 
Source 

```
pub struct Config<'a> {}
```

## Fields§
§`language: Option<&'a str>`

The explicitly configured language, if any
§`show_nonprintable: bool`

Whether or not to show/replace non-printable characters like space, tab and newline.
§`nonprintable_notation: NonprintableNotation`

The configured notation for non-printable characters
§`binary: BinaryBehavior`

How to treat binary content
§`term_width: usize`

The character width of the terminal
§`tab_width: usize`

The width of tab characters.
Currently, a value of 0 will cause tabs to be passed through without expanding them.
§`loop_through: bool`

Whether or not to simply loop through all input (`cat` mode)
§`colored_output: bool`

Whether or not the output should be colorized
§`true_color: bool`

Whether or not the output terminal supports true color
§`style_components: StyleComponents`

Style elements (grid, line numbers, …)
§`wrapping_mode: WrappingMode`

If and how text should be wrapped
§`paging_mode: PagingMode`

Pager or STDOUT
§`visible_lines: VisibleLines`

Specifies which lines should be printed
§`theme: String`

The syntax highlighting theme
§`syntax_mapping: SyntaxMapping<'a>`

File extension/name mappings
§`pager: Option<&'a str>`

Command to start the pager
§`use_italic_text: bool`

Whether or not to use ANSI italics
§`highlighted_lines: HighlightedLineRanges`

Ranges of lines which should be highlighted with a special background color
§`use_custom_assets: bool`

Whether or not to allow custom assets. If this is false or if custom assets (a.k.a.
cached assets) are not available, assets from the binary will be used instead.
§`set_terminal_title: bool`§`squeeze_lines: Option<usize>`

The maximum number of consecutive empty lines to display
§`strip_ansi: StripAnsiMode`
## Trait Implementations§