lipgloss
# Module size 
Source 
## Functions§
heightHeight returns height of a string in cells. This is done simply by counting
`\n` characters. If your strings use `\r\n` for newlines you should convert
them to `\n` first, or write a separate function for measuring height.sizeSize returns the width and height of the string in cells. ANSI sequences are
ignored and characters wider than one cell (such as Chinese characters and
emojis) are appropriately measured.widthWidth returns the cell width of characters in the string. ANSI sequences are
ignored and characters wider than one cell (such as Chinese characters and
emojis) are appropriately measured.