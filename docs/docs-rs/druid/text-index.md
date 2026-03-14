druid

# Module text

Source

## Structs§

AttributeSpansA collection of spans of attributes of various kinds.AttributesAdderAdds Attributes to the text.EditSessionEditable text state.EnvUpdateCtxProvides information about keys change for more fine grained invalidationFontDescriptorA collection of attributes that describe a font.FontFamilyA reference to a font family.FontWeightA font weight, represented as a value in the range 1..=1000.LayoutMetricsMetrics describing the layout text.LinkA clickable range of text with an associated `Command`.ParseFormatterA naive `Formatter` for types that implement `FromStr`.RichTextText with optional style spans.RichTextBuilderA builder for creating `RichText` objects.SelectionA range of selected text, or a caret.StringCursorA cursor type that implements EditableTextCursor for StringTextComponentA widget that accepts text input.TextLayoutA component for displaying text on screen.ValidationThe result of a `Formatter` attempting to validate some partial input.ValidationErrorAn error returned by a `Formatter` when it cannot parse input.

## Enums§

AffinityDistinguishes between two visually distinct locations with the same byte
index.AttributeAttributes that can be applied to text.DirectionIndicates a horizontal direction in the text.FontStyleA font style, which may be italic or regular.ImeInvalidationAn event representing an application-initiated change in `InputHandler`
state.MovementIndicates a movement that transforms a particular text position in a
document.TextActionA special text editing command sent from the platform to the application.TextAlignmentThe alignment of text in a `TextLayout`.VerticalMovementIndicates a vertical movement in a text document.WritingDirectionIndicates a horizontal direction for writing text.

## Traits§

EditableTextAn EditableText trait.EditableTextCursorA cursor with convenience functions for moving through EditableText.FormatterA trait for types that create, interpret, and validate textual representations
of values.ImeHandlerRefA trait for input handlers registered by widgets.InputHandlerA lock on a text field that allows the platform to retrieve state and make
edits.TextStorageA type that represents text that can be displayed.

## Functions§

movementCompute the result of a `Movement` on a `Selection`.offset_for_delete_backwardsCalculate resulting offset for a backwards delete.

## Type Aliases§

ArcStrA reference counted string slice.
