# LinkButton in English

# LinkButton
Inherits:BaseButton<Control<CanvasItem<Node<Object
A button that represents a link.

## Description
A button that represents a link. This type of button is primarily used for interactions that cause a context change (like linking to a web page).
See alsoBaseButtonwhich contains common properties and methods associated with this node.

## Properties

| String | ellipsis_char | "…" |
|---|---|---|
| FocusMode | focus_mode | 3(overridesControl) |
| String | language | "" |
| CursorShape | mouse_default_cursor_shape | 2(overridesControl) |
| StructuredTextParser | structured_text_bidi_override | 0 |
| Array | structured_text_bidi_override_options | [] |
| String | text | "" |
| TextDirection | text_direction | 0 |
| OverrunBehavior | text_overrun_behavior | 0 |
| UnderlineMode | underline | 0 |
| String | uri | "" |

String
ellipsis_char
FocusMode
focus_mode
3(overridesControl)
String
language
CursorShape
mouse_default_cursor_shape
2(overridesControl)
StructuredTextParser
structured_text_bidi_override
Array
structured_text_bidi_override_options
String
text
TextDirection
text_direction
OverrunBehavior
text_overrun_behavior
UnderlineMode
underline
String

## Theme Properties

| Color | font_color | Color(0.875,0.875,0.875,1) |
|---|---|---|
| Color | font_disabled_color | Color(0,0,0,1) |
| Color | font_focus_color | Color(0.95,0.95,0.95,1) |
| Color | font_hover_color | Color(0.95,0.95,0.95,1) |
| Color | font_hover_pressed_color | Color(0,0,0,1) |
| Color | font_outline_color | Color(0,0,0,1) |
| Color | font_pressed_color | Color(1,1,1,1) |
| int | outline_size | 0 |
| int | underline_spacing | 2 |
| Font | font |  |
| int | font_size |  |
| StyleBox | focus |  |

Color
font_color
Color(0.875,0.875,0.875,1)
Color
font_disabled_color
Color(0,0,0,1)
Color
font_focus_color
Color(0.95,0.95,0.95,1)
Color
font_hover_color
Color(0.95,0.95,0.95,1)
Color
font_hover_pressed_color
Color(0,0,0,1)
Color
font_outline_color
Color(0,0,0,1)
Color
font_pressed_color
Color(1,1,1,1)
outline_size
underline_spacing
Font
font
font_size
StyleBox
focus

## Enumerations
enumUnderlineMode:🔗
UnderlineModeUNDERLINE_MODE_ALWAYS=0
The LinkButton will always show an underline at the bottom of its text.
UnderlineModeUNDERLINE_MODE_ON_HOVER=1
The LinkButton will show an underline at the bottom of its text when the mouse cursor is over it.
UnderlineModeUNDERLINE_MODE_NEVER=2
The LinkButton will never show an underline at the bottom of its text.

## Property Descriptions
Stringellipsis_char="…"🔗
- voidset_ellipsis_char(value:String)
voidset_ellipsis_char(value:String)
- Stringget_ellipsis_char()
Stringget_ellipsis_char()
Ellipsis character used for text clipping.
Stringlanguage=""🔗
- voidset_language(value:String)
voidset_language(value:String)
- Stringget_language()
Stringget_language()
Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.
StructuredTextParserstructured_text_bidi_override=0🔗
- voidset_structured_text_bidi_override(value:StructuredTextParser)
voidset_structured_text_bidi_override(value:StructuredTextParser)
- StructuredTextParserget_structured_text_bidi_override()
StructuredTextParserget_structured_text_bidi_override()
Set BiDi algorithm override for the structured text.
Arraystructured_text_bidi_override_options=[]🔗
- voidset_structured_text_bidi_override_options(value:Array)
voidset_structured_text_bidi_override_options(value:Array)
- Arrayget_structured_text_bidi_override_options()
Arrayget_structured_text_bidi_override_options()
Set additional options for BiDi override.
Stringtext=""🔗
- voidset_text(value:String)
voidset_text(value:String)
- Stringget_text()
Stringget_text()
The button's text that will be displayed inside the button's area.
TextDirectiontext_direction=0🔗
- voidset_text_direction(value:TextDirection)
voidset_text_direction(value:TextDirection)
- TextDirectionget_text_direction()
TextDirectionget_text_direction()
Base text writing direction.
OverrunBehaviortext_overrun_behavior=0🔗
- voidset_text_overrun_behavior(value:OverrunBehavior)
voidset_text_overrun_behavior(value:OverrunBehavior)
- OverrunBehaviorget_text_overrun_behavior()
OverrunBehaviorget_text_overrun_behavior()
Sets the clipping behavior when the text exceeds the node's bounding rectangle.
UnderlineModeunderline=0🔗
- voidset_underline_mode(value:UnderlineMode)
voidset_underline_mode(value:UnderlineMode)
- UnderlineModeget_underline_mode()
UnderlineModeget_underline_mode()
The underline mode to use for the text.
Stringuri=""🔗
- voidset_uri(value:String)
voidset_uri(value:String)
- Stringget_uri()
Stringget_uri()
TheURIfor thisLinkButton. If set to a valid URI, pressing the button opens the URI using the operating system's default program for the protocol (viaOS.shell_open()). HTTP and HTTPS URLs open the default web browser.
```
uri = "https://godotengine.org"  # Opens the URL in the default web browser.
uri = "C:\SomeFolder"  # Opens the file explorer at the given path.
uri = "C:\SomeImage.png"  # Opens the given image in the default viewing app.
```
```
Uri = "https://godotengine.org"; // Opens the URL in the default web browser.
Uri = "C:\SomeFolder"; // Opens the file explorer at the given path.
Uri = "C:\SomeImage.png"; // Opens the given image in the default viewing app.
```

## Theme Property Descriptions
Colorfont_color=Color(0.875,0.875,0.875,1)🔗
Default textColorof theLinkButton.
Colorfont_disabled_color=Color(0,0,0,1)🔗
TextColorused when theLinkButtonis disabled.
Colorfont_focus_color=Color(0.95,0.95,0.95,1)🔗
TextColorused when theLinkButtonis focused. Only replaces the normal text color of the button. Disabled, hovered, and pressed states take precedence over this color.
Colorfont_hover_color=Color(0.95,0.95,0.95,1)🔗
TextColorused when theLinkButtonis being hovered.
Colorfont_hover_pressed_color=Color(0,0,0,1)🔗
TextColorused when theLinkButtonis being hovered and pressed.
Colorfont_outline_color=Color(0,0,0,1)🔗
The tint of text outline of theLinkButton.
Colorfont_pressed_color=Color(1,1,1,1)🔗
TextColorused when theLinkButtonis being pressed.
intoutline_size=0🔗
The size of the text outline.
Note:If using a font withFontFile.multichannel_signed_distance_fieldenabled, itsFontFile.msdf_pixel_rangemust be set to at leasttwicethe value ofoutline_sizefor outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.
intunderline_spacing=2🔗
The vertical space between the baseline of text and the underline.
Fontfont🔗
Fontof theLinkButton's text.
intfont_size🔗
Font size of theLinkButton's text.
StyleBoxfocus🔗
StyleBoxused when theLinkButtonis focused. ThefocusStyleBoxis displayedoverthe baseStyleBox, so a partially transparentStyleBoxshould be used to ensure the baseStyleBoxremains visible. AStyleBoxthat represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign aStyleBoxEmptyresource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.