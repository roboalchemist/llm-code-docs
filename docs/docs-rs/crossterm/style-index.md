crossterm
# Module style 
Source 
## Structs§
Attributesa bitset for all possible attributesColorsRepresents, optionally, a foreground and/or a background color.ContentStyleThe style that can be put on content.PrintA command that prints the given displayable type.PrintStyledContentA command that prints styled content.ResetColorA command that resets the colors back to default.SetAttributeA command that sets an attribute.SetAttributesA command that sets several attributes.SetBackgroundColorA command that sets the the background color.SetColorsA command that optionally sets the foreground and/or background color.SetForegroundColorA command that sets the the foreground color.SetStyleA command that sets a style (colors and attributes).SetUnderlineColorA command that sets the the underline color.StyledContentThe style with the content to be styled.
## Enums§
AttributeRepresents an attribute.ColorRepresents a color.ColoredRepresents a foreground or background color.
## Traits§
StylizeProvides a set of methods to set attributes and colors.
## Functions§
available_color_countReturns available color count.force_color_outputForces colored output on or off globally, overriding NO_COLOR.styleCreates a `StyledContent`.