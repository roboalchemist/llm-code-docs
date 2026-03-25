lipgloss
# Module utils 
Source 
## Structs§
RangeRepresents a character range with an associated style for selective text styling.
## Functions§
NewRangeGo-style alias for `new_range`.StyleRangesGo-style alias for `style_ranges`.StyleRunesGo-style alias for `style_runes`.get_linesSplits text into lines and returns the maximum content width.get_lines_visibleSplits text into lines, strips ANSI codes, and returns the maximum visible width.heightReturns the number of lines in a string.new_rangeCreates a new `Range` (convenience function).strip_ansiStrips ANSI escape sequences from a string, returning clean text.style_rangesApplies styles to specific character ranges within a string.style_runesApplies different styles to specific character indices versus the rest of the text.which_sides_boolHelper for CSS-style shorthand boolean values (border sides).which_sides_colorHelper for CSS-style shorthand color values (border colors).which_sides_intHelper for CSS-style shorthand integer values (padding, margin).widthReturns the display width of a string in terminal cells.width_visibleReturns the visible display width of a string, ignoring ANSI escape sequences.