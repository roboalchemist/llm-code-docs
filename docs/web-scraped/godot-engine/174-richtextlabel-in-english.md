# RichTextLabel in English

# RichTextLabel
Inherits:Control<CanvasItem<Node<Object
A control for displaying text that can contain different font styles, images, and basic formatting.

## Description
A control for displaying text that can contain custom fonts, images, and basic formatting.RichTextLabelmanages these as an internal tag stack. It also adapts itself to given width/heights.
Note:newline(),push_paragraph(),"\n","\r\n",ptag, and alignment tags start a new paragraph. Each paragraph is processed independently, in its own BiDi context. If you want to force line wrapping within paragraph, any other line breaking character can be used, for example, Form Feed (U+000C), Next Line (U+0085), Line Separator (U+2028).
Note:Assignments totextclear the tag stack and reconstruct it from the property's contents. Any edits made totextwill erase previous edits made from other manual sources such asappend_text()and thepush_*/pop()methods.
Note:RichTextLabel doesn't support entangled BBCode tags. For example, instead of using[b]bold[i]bolditalic[/b]italic[/i], use[b]bold[i]bolditalic[/i][/b][i]italic[/i].
Note:push_*/pop_*functions won't affect BBCode.
Note:Whilebbcode_enabledis enabled, alignment tags such as[center]will take priority over thehorizontal_alignmentsetting which determines the default text alignment.

## Tutorials
- BBCode in RichTextLabel
BBCode in RichTextLabel
- Rich Text Label with BBCode Demo
Rich Text Label with BBCode Demo
- Operating System Testing Demo
Operating System Testing Demo

## Properties

| AutowrapMode | autowrap_mode | 3 |
|---|---|---|
| BitField[LineBreakFlag] | autowrap_trim_flags | 192 |
| bool | bbcode_enabled | false |
| bool | clip_contents | true(overridesControl) |
| bool | context_menu_enabled | false |
| Array | custom_effects | [] |
| bool | deselect_on_focus_loss_enabled | true |
| bool | drag_and_drop_selection_enabled | true |
| bool | fit_content | false |
| FocusMode | focus_mode | 3(overridesControl) |
| bool | hint_underlined | true |
| HorizontalAlignment | horizontal_alignment | 0 |
| BitField[JustificationFlag] | justification_flags | 163 |
| String | language | "" |
| bool | meta_underlined | true |
| int | progress_bar_delay | 1000 |
| bool | scroll_active | true |
| bool | scroll_following | false |
| bool | scroll_following_visible_characters | false |
| bool | selection_enabled | false |
| bool | shortcut_keys_enabled | true |
| StructuredTextParser | structured_text_bidi_override | 0 |
| Array | structured_text_bidi_override_options | [] |
| int | tab_size | 4 |
| PackedFloat32Array | tab_stops | PackedFloat32Array() |
| String | text | "" |
| TextDirection | text_direction | 0 |
| bool | threaded | false |
| VerticalAlignment | vertical_alignment | 0 |
| int | visible_characters | -1 |
| VisibleCharactersBehavior | visible_characters_behavior | 0 |
| float | visible_ratio | 1.0 |

AutowrapMode
autowrap_mode
BitField[LineBreakFlag]
autowrap_trim_flags
bool
bbcode_enabled
false
bool
clip_contents
true(overridesControl)
bool
context_menu_enabled
false
Array
custom_effects
bool
deselect_on_focus_loss_enabled
true
bool
drag_and_drop_selection_enabled
true
bool
fit_content
false
FocusMode
focus_mode
3(overridesControl)
bool
hint_underlined
true
HorizontalAlignment
horizontal_alignment
BitField[JustificationFlag]
justification_flags
String
language
bool
meta_underlined
true
progress_bar_delay
1000
bool
scroll_active
true
bool
scroll_following
false
bool
scroll_following_visible_characters
false
bool
selection_enabled
false
bool
shortcut_keys_enabled
true
StructuredTextParser
structured_text_bidi_override
Array
structured_text_bidi_override_options
tab_size
PackedFloat32Array
tab_stops
PackedFloat32Array()
String
text
TextDirection
text_direction
bool
threaded
false
VerticalAlignment
vertical_alignment
visible_characters
VisibleCharactersBehavior
visible_characters_behavior
float
visible_ratio

## Methods

| void | add_hr(width:int= 90, height:int= 2, color:Color= Color(1, 1, 1, 1), alignment:HorizontalAlignment= 1, width_in_percent:bool= true, height_in_percent:bool= false) |
|---|---|
| void | add_image(image:Texture2D, width:int= 0, height:int= 0, color:Color= Color(1, 1, 1, 1), inline_align:InlineAlignment= 5, region:Rect2= Rect2(0, 0, 0, 0), key:Variant= null, pad:bool= false, tooltip:String= "", width_in_percent:bool= false, height_in_percent:bool= false, alt_text:String= "") |
| void | add_text(text:String) |
| void | append_text(bbcode:String) |
| void | clear() |
| void | deselect() |
| int | get_character_line(character:int) |
| int | get_character_paragraph(character:int) |
| int | get_content_height()const |
| int | get_content_width()const |
| int | get_line_count()const |
| int | get_line_height(line:int)const |
| float | get_line_offset(line:int) |
| Vector2i | get_line_range(line:int) |
| int | get_line_width(line:int)const |
| PopupMenu | get_menu()const |
| int | get_paragraph_count()const |
| float | get_paragraph_offset(paragraph:int) |
| String | get_parsed_text()const |
| String | get_selected_text()const |
| int | get_selection_from()const |
| float | get_selection_line_offset()const |
| int | get_selection_to()const |
| int | get_total_character_count()const |
| VScrollBar | get_v_scroll_bar() |
| Rect2i | get_visible_content_rect()const |
| int | get_visible_line_count()const |
| int | get_visible_paragraph_count()const |
| void | install_effect(effect:Variant) |
| bool | invalidate_paragraph(paragraph:int) |
| bool | is_finished()const |
| bool | is_menu_visible()const |
| bool | is_ready()const |
| void | menu_option(option:int) |
| void | newline() |
| void | parse_bbcode(bbcode:String) |
| Dictionary | parse_expressions_for_values(expressions:PackedStringArray) |
| void | pop() |
| void | pop_all() |
| void | pop_context() |
| void | push_bgcolor(bgcolor:Color) |
| void | push_bold() |
| void | push_bold_italics() |
| void | push_cell() |
| void | push_color(color:Color) |
| void | push_context() |
| void | push_customfx(effect:RichTextEffect, env:Dictionary) |
| void | push_dropcap(string:String, font:Font, size:int, dropcap_margins:Rect2= Rect2(0, 0, 0, 0), color:Color= Color(1, 1, 1, 1), outline_size:int= 0, outline_color:Color= Color(0, 0, 0, 0)) |
| void | push_fgcolor(fgcolor:Color) |
| void | push_font(font:Font, font_size:int= 0) |
| void | push_font_size(font_size:int) |
| void | push_hint(description:String) |
| void | push_indent(level:int) |
| void | push_italics() |
| void | push_language(language:String) |
| void | push_list(level:int, type:ListType, capitalize:bool, bullet:String= "•") |
| void | push_meta(data:Variant, underline_mode:MetaUnderline= 1, tooltip:String= "") |
| void | push_mono() |
| void | push_normal() |
| void | push_outline_color(color:Color) |
| void | push_outline_size(outline_size:int) |
| void | push_paragraph(alignment:HorizontalAlignment, base_direction:TextDirection= 0, language:String= "", st_parser:StructuredTextParser= 0, justification_flags:BitField[JustificationFlag] = 163, tab_stops:PackedFloat32Array= PackedFloat32Array()) |
| void | push_strikethrough(color:Color= Color(0, 0, 0, 0)) |
| void | push_table(columns:int, inline_align:InlineAlignment= 0, align_to_row:int= -1, name:String= "") |
| void | push_underline(color:Color= Color(0, 0, 0, 0)) |
| void | reload_effects() |
| bool | remove_paragraph(paragraph:int, no_invalidate:bool= false) |
| void | scroll_to_line(line:int) |
| void | scroll_to_paragraph(paragraph:int) |
| void | scroll_to_selection() |
| void | select_all() |
| void | set_cell_border_color(color:Color) |
| void | set_cell_padding(padding:Rect2) |
| void | set_cell_row_background_color(odd_row_bg:Color, even_row_bg:Color) |
| void | set_cell_size_override(min_size:Vector2, max_size:Vector2) |
| void | set_table_column_expand(column:int, expand:bool, ratio:int= 1, shrink:bool= true) |
| void | set_table_column_name(column:int, name:String) |
| void | update_image(key:Variant, mask:BitField[ImageUpdateMask], image:Texture2D, width:int= 0, height:int= 0, color:Color= Color(1, 1, 1, 1), inline_align:InlineAlignment= 5, region:Rect2= Rect2(0, 0, 0, 0), pad:bool= false, tooltip:String= "", width_in_percent:bool= false, height_in_percent:bool= false) |

void
add_hr(width:int= 90, height:int= 2, color:Color= Color(1, 1, 1, 1), alignment:HorizontalAlignment= 1, width_in_percent:bool= true, height_in_percent:bool= false)
void
add_image(image:Texture2D, width:int= 0, height:int= 0, color:Color= Color(1, 1, 1, 1), inline_align:InlineAlignment= 5, region:Rect2= Rect2(0, 0, 0, 0), key:Variant= null, pad:bool= false, tooltip:String= "", width_in_percent:bool= false, height_in_percent:bool= false, alt_text:String= "")
void
add_text(text:String)
void
append_text(bbcode:String)
void
clear()
void
deselect()
get_character_line(character:int)
get_character_paragraph(character:int)
get_content_height()const
get_content_width()const
get_line_count()const
get_line_height(line:int)const
float
get_line_offset(line:int)
Vector2i
get_line_range(line:int)
get_line_width(line:int)const
PopupMenu
get_menu()const
get_paragraph_count()const
float
get_paragraph_offset(paragraph:int)
String
get_parsed_text()const
String
get_selected_text()const
get_selection_from()const
float
get_selection_line_offset()const
get_selection_to()const
get_total_character_count()const
VScrollBar
get_v_scroll_bar()
Rect2i
get_visible_content_rect()const
get_visible_line_count()const
get_visible_paragraph_count()const
void
install_effect(effect:Variant)
bool
invalidate_paragraph(paragraph:int)
bool
is_finished()const
bool
is_menu_visible()const
bool
is_ready()const
void
menu_option(option:int)
void
newline()
void
parse_bbcode(bbcode:String)
Dictionary
parse_expressions_for_values(expressions:PackedStringArray)
void
pop()
void
pop_all()
void
pop_context()
void
push_bgcolor(bgcolor:Color)
void
push_bold()
void
push_bold_italics()
void
push_cell()
void
push_color(color:Color)
void
push_context()
void
push_customfx(effect:RichTextEffect, env:Dictionary)
void
push_dropcap(string:String, font:Font, size:int, dropcap_margins:Rect2= Rect2(0, 0, 0, 0), color:Color= Color(1, 1, 1, 1), outline_size:int= 0, outline_color:Color= Color(0, 0, 0, 0))
void
push_fgcolor(fgcolor:Color)
void
push_font(font:Font, font_size:int= 0)
void
push_font_size(font_size:int)
void
push_hint(description:String)
void
push_indent(level:int)
void
push_italics()
void
push_language(language:String)
void
push_list(level:int, type:ListType, capitalize:bool, bullet:String= "•")
void
push_meta(data:Variant, underline_mode:MetaUnderline= 1, tooltip:String= "")
void
push_mono()
void
push_normal()
void
push_outline_color(color:Color)
void
push_outline_size(outline_size:int)
void
push_paragraph(alignment:HorizontalAlignment, base_direction:TextDirection= 0, language:String= "", st_parser:StructuredTextParser= 0, justification_flags:BitField[JustificationFlag] = 163, tab_stops:PackedFloat32Array= PackedFloat32Array())
void
push_strikethrough(color:Color= Color(0, 0, 0, 0))
void
push_table(columns:int, inline_align:InlineAlignment= 0, align_to_row:int= -1, name:String= "")
void
push_underline(color:Color= Color(0, 0, 0, 0))
void
reload_effects()
bool
remove_paragraph(paragraph:int, no_invalidate:bool= false)
void
scroll_to_line(line:int)
void
scroll_to_paragraph(paragraph:int)
void
scroll_to_selection()
void
select_all()
void
set_cell_border_color(color:Color)
void
set_cell_padding(padding:Rect2)
void
set_cell_row_background_color(odd_row_bg:Color, even_row_bg:Color)
void
set_cell_size_override(min_size:Vector2, max_size:Vector2)
void
set_table_column_expand(column:int, expand:bool, ratio:int= 1, shrink:bool= true)
void
set_table_column_name(column:int, name:String)
void
update_image(key:Variant, mask:BitField[ImageUpdateMask], image:Texture2D, width:int= 0, height:int= 0, color:Color= Color(1, 1, 1, 1), inline_align:InlineAlignment= 5, region:Rect2= Rect2(0, 0, 0, 0), pad:bool= false, tooltip:String= "", width_in_percent:bool= false, height_in_percent:bool= false)

## Theme Properties

| Color | default_color | Color(1,1,1,1) |
|---|---|---|
| Color | font_outline_color | Color(0,0,0,1) |
| Color | font_selected_color | Color(0,0,0,0) |
| Color | font_shadow_color | Color(0,0,0,0) |
| Color | selection_color | Color(0.1,0.1,1,0.8) |
| Color | table_border | Color(0,0,0,0) |
| Color | table_even_row_bg | Color(0,0,0,0) |
| Color | table_odd_row_bg | Color(0,0,0,0) |
| int | line_separation | 0 |
| int | outline_size | 0 |
| int | paragraph_separation | 0 |
| int | shadow_offset_x | 1 |
| int | shadow_offset_y | 1 |
| int | shadow_outline_size | 1 |
| int | strikethrough_alpha | 50 |
| int | table_h_separation | 3 |
| int | table_v_separation | 3 |
| int | text_highlight_h_padding | 3 |
| int | text_highlight_v_padding | 3 |
| int | underline_alpha | 50 |
| Font | bold_font |  |
| Font | bold_italics_font |  |
| Font | italics_font |  |
| Font | mono_font |  |
| Font | normal_font |  |
| int | bold_font_size |  |
| int | bold_italics_font_size |  |
| int | italics_font_size |  |
| int | mono_font_size |  |
| int | normal_font_size |  |
| Texture2D | horizontal_rule |  |
| StyleBox | focus |  |
| StyleBox | normal |  |

Color
default_color
Color(1,1,1,1)
Color
font_outline_color
Color(0,0,0,1)
Color
font_selected_color
Color(0,0,0,0)
Color
font_shadow_color
Color(0,0,0,0)
Color
selection_color
Color(0.1,0.1,1,0.8)
Color
table_border
Color(0,0,0,0)
Color
table_even_row_bg
Color(0,0,0,0)
Color
table_odd_row_bg
Color(0,0,0,0)
line_separation
outline_size
paragraph_separation
shadow_offset_x
shadow_offset_y
shadow_outline_size
strikethrough_alpha
table_h_separation
table_v_separation
text_highlight_h_padding
text_highlight_v_padding
underline_alpha
Font
bold_font
Font
bold_italics_font
Font
italics_font
Font
mono_font
Font
normal_font
bold_font_size
bold_italics_font_size
italics_font_size
mono_font_size
normal_font_size
Texture2D
horizontal_rule
StyleBox
focus
StyleBox
normal

## Signals
finished()🔗
Triggered when the document is fully loaded.
Note:This can happen before the text is processed for drawing. Scrolling values may not be valid until the document is drawn for the first time after this signal.
meta_clicked(meta:Variant)🔗
Triggered when the user clicks on content between meta (URL) tags. If the meta is defined in BBCode, e.g.[url={"key":"value"}]Text[/url], then the parameter for this signal will always be aStringtype. If a particular type or an object is desired, thepush_meta()method must be used to manually insert the data into the tag stack. Alternatively, you can convert theStringinput to the desired type based on its contents (such as callingJSON.parse()on it).
For example, the following method can be connected tometa_clickedto open clicked URLs using the user's default web browser:
```
# This assumes RichTextLabel's `meta_clicked` signal was connected to
# the function below using the signal connection dialog.
func _richtextlabel_on_meta_clicked(meta):
    # `meta` is of Variant type, so convert it to a String to avoid script errors at run-time.
    OS.shell_open(str(meta))
```
meta_hover_ended(meta:Variant)🔗
Triggers when the mouse exits a meta tag.
meta_hover_started(meta:Variant)🔗
Triggers when the mouse enters a meta tag.

## Enumerations
enumListType:🔗
ListTypeLIST_NUMBERS=0
Each list item has a number marker.
ListTypeLIST_LETTERS=1
Each list item has a letter marker.
ListTypeLIST_ROMAN=2
Each list item has a roman number marker.
ListTypeLIST_DOTS=3
Each list item has a filled circle marker.
enumMenuItems:🔗
MenuItemsMENU_COPY=0
Copies the selected text.
MenuItemsMENU_SELECT_ALL=1
Selects the wholeRichTextLabeltext.
MenuItemsMENU_MAX=2
Represents the size of theMenuItemsenum.
enumMetaUnderline:🔗
MetaUnderlineMETA_UNDERLINE_NEVER=0
Meta tag does not display an underline, even ifmeta_underlinedistrue.
MetaUnderlineMETA_UNDERLINE_ALWAYS=1
Ifmeta_underlinedistrue, meta tag always display an underline.
MetaUnderlineMETA_UNDERLINE_ON_HOVER=2
Ifmeta_underlinedistrue, meta tag display an underline when the mouse cursor is over it.
flagsImageUpdateMask:🔗
ImageUpdateMaskUPDATE_TEXTURE=1
If this bit is set,update_image()changes image texture.
ImageUpdateMaskUPDATE_SIZE=2
If this bit is set,update_image()changes image size.
ImageUpdateMaskUPDATE_COLOR=4
If this bit is set,update_image()changes image color.
ImageUpdateMaskUPDATE_ALIGNMENT=8
If this bit is set,update_image()changes image inline alignment.
ImageUpdateMaskUPDATE_REGION=16
If this bit is set,update_image()changes image texture region.
ImageUpdateMaskUPDATE_PAD=32
If this bit is set,update_image()changes image padding.
ImageUpdateMaskUPDATE_TOOLTIP=64
If this bit is set,update_image()changes image tooltip.
ImageUpdateMaskUPDATE_WIDTH_IN_PERCENT=128
If this bit is set,update_image()changes image width from/to percents.

## Property Descriptions
AutowrapModeautowrap_mode=3🔗
- voidset_autowrap_mode(value:AutowrapMode)
voidset_autowrap_mode(value:AutowrapMode)
- AutowrapModeget_autowrap_mode()
AutowrapModeget_autowrap_mode()
If set to something other thanTextServer.AUTOWRAP_OFF, the text gets wrapped inside the node's bounding rectangle.
BitField[LineBreakFlag]autowrap_trim_flags=192🔗
- voidset_autowrap_trim_flags(value:BitField[LineBreakFlag])
voidset_autowrap_trim_flags(value:BitField[LineBreakFlag])
- BitField[LineBreakFlag]get_autowrap_trim_flags()
BitField[LineBreakFlag]get_autowrap_trim_flags()
Autowrap space trimming flags. SeeTextServer.BREAK_TRIM_START_EDGE_SPACESandTextServer.BREAK_TRIM_END_EDGE_SPACESfor more info.
boolbbcode_enabled=false🔗
- voidset_use_bbcode(value:bool)
voidset_use_bbcode(value:bool)
- boolis_using_bbcode()
boolis_using_bbcode()
Iftrue, the label uses BBCode formatting.
Note:This only affects the contents oftext, not the tag stack.
boolcontext_menu_enabled=false🔗
- voidset_context_menu_enabled(value:bool)
voidset_context_menu_enabled(value:bool)
- boolis_context_menu_enabled()
boolis_context_menu_enabled()
Iftrue, a right-click displays the context menu.
Arraycustom_effects=[]🔗
- voidset_effects(value:Array)
voidset_effects(value:Array)
- Arrayget_effects()
Arrayget_effects()
The currently installed custom effects. This is an array ofRichTextEffects.
To add a custom effect, it's more convenient to useinstall_effect().
booldeselect_on_focus_loss_enabled=true🔗
- voidset_deselect_on_focus_loss_enabled(value:bool)
voidset_deselect_on_focus_loss_enabled(value:bool)
- boolis_deselect_on_focus_loss_enabled()
boolis_deselect_on_focus_loss_enabled()
Iftrue, the selected text will be deselected when focus is lost.
booldrag_and_drop_selection_enabled=true🔗
- voidset_drag_and_drop_selection_enabled(value:bool)
voidset_drag_and_drop_selection_enabled(value:bool)
- boolis_drag_and_drop_selection_enabled()
boolis_drag_and_drop_selection_enabled()
Iftrue, allow drag and drop of selected text.
boolfit_content=false🔗
- voidset_fit_content(value:bool)
voidset_fit_content(value:bool)
- boolis_fit_content_enabled()
boolis_fit_content_enabled()
Iftrue, the label's minimum size will be automatically updated to fit its content, matching the behavior ofLabel.
boolhint_underlined=true🔗
- voidset_hint_underline(value:bool)
voidset_hint_underline(value:bool)
- boolis_hint_underlined()
boolis_hint_underlined()
Iftrue, the label underlines hint tags such as[hint=description]{text}[/hint].
HorizontalAlignmenthorizontal_alignment=0🔗
- voidset_horizontal_alignment(value:HorizontalAlignment)
voidset_horizontal_alignment(value:HorizontalAlignment)
- HorizontalAlignmentget_horizontal_alignment()
HorizontalAlignmentget_horizontal_alignment()
Controls the text's horizontal alignment. Supports left, center, right, and fill (also known as justify).
BitField[JustificationFlag]justification_flags=163🔗
- voidset_justification_flags(value:BitField[JustificationFlag])
voidset_justification_flags(value:BitField[JustificationFlag])
- BitField[JustificationFlag]get_justification_flags()
BitField[JustificationFlag]get_justification_flags()
Line fill alignment rules.
Stringlanguage=""🔗
- voidset_language(value:String)
voidset_language(value:String)
- Stringget_language()
Stringget_language()
Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.
boolmeta_underlined=true🔗
- voidset_meta_underline(value:bool)
voidset_meta_underline(value:bool)
- boolis_meta_underlined()
boolis_meta_underlined()
Iftrue, the label underlines meta tags such as[url]{text}[/url]. These tags can call a function when clicked ifmeta_clickedis connected to a function.
intprogress_bar_delay=1000🔗
- voidset_progress_bar_delay(value:int)
voidset_progress_bar_delay(value:int)
- intget_progress_bar_delay()
intget_progress_bar_delay()
The delay after which the loading progress bar is displayed, in milliseconds. Set to-1to disable progress bar entirely.
Note:Progress bar is displayed only ifthreadedis enabled.
boolscroll_active=true🔗
- voidset_scroll_active(value:bool)
voidset_scroll_active(value:bool)
- boolis_scroll_active()
boolis_scroll_active()
Iftrue, the scrollbar is visible. Setting this tofalsedoes not block scrolling completely. Seescroll_to_line().
boolscroll_following=false🔗
- voidset_scroll_follow(value:bool)
voidset_scroll_follow(value:bool)
- boolis_scroll_following()
boolis_scroll_following()
Iftrue, the window scrolls down to display new content automatically.
boolscroll_following_visible_characters=false🔗
- voidset_scroll_follow_visible_characters(value:bool)
voidset_scroll_follow_visible_characters(value:bool)
- boolis_scroll_following_visible_characters()
boolis_scroll_following_visible_characters()
Iftrue, the window scrolls to display the last visible line whenvisible_charactersorvisible_ratiois changed.
boolselection_enabled=false🔗
- voidset_selection_enabled(value:bool)
voidset_selection_enabled(value:bool)
- boolis_selection_enabled()
boolis_selection_enabled()
Iftrue, the label allows text selection.
boolshortcut_keys_enabled=true🔗
- voidset_shortcut_keys_enabled(value:bool)
voidset_shortcut_keys_enabled(value:bool)
- boolis_shortcut_keys_enabled()
boolis_shortcut_keys_enabled()
Iftrue, shortcut keys for context menu items are enabled, even if the context menu is disabled.
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
inttab_size=4🔗
- voidset_tab_size(value:int)
voidset_tab_size(value:int)
- intget_tab_size()
intget_tab_size()
The number of spaces associated with a single tab length. Does not affect\tin text tags, only indent tags.
PackedFloat32Arraytab_stops=PackedFloat32Array()🔗
- voidset_tab_stops(value:PackedFloat32Array)
voidset_tab_stops(value:PackedFloat32Array)
- PackedFloat32Arrayget_tab_stops()
PackedFloat32Arrayget_tab_stops()
Aligns text to the given tab-stops.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedFloat32Arrayfor more details.
Stringtext=""🔗
- voidset_text(value:String)
voidset_text(value:String)
- Stringget_text()
Stringget_text()
The label's text in BBCode format. Is not representative of manual modifications to the internal tag stack. Erases changes made by other methods when edited.
Note:Ifbbcode_enabledistrue, it is unadvised to use the+=operator withtext(e.g.text+="somestring") as it replaces the whole text and can cause slowdowns. It will also erase all BBCode that was added to stack usingpush_*methods. Useappend_text()for adding text instead, unless you absolutely need to close a tag that was opened in an earlier method call.
TextDirectiontext_direction=0🔗
- voidset_text_direction(value:TextDirection)
voidset_text_direction(value:TextDirection)
- TextDirectionget_text_direction()
TextDirectionget_text_direction()
Base text writing direction.
boolthreaded=false🔗
- voidset_threaded(value:bool)
voidset_threaded(value:bool)
- boolis_threaded()
boolis_threaded()
Iftrue, text processing is done in a background thread.
VerticalAlignmentvertical_alignment=0🔗
- voidset_vertical_alignment(value:VerticalAlignment)
voidset_vertical_alignment(value:VerticalAlignment)
- VerticalAlignmentget_vertical_alignment()
VerticalAlignmentget_vertical_alignment()
Controls the text's vertical alignment. Supports top, center, bottom, and fill.
intvisible_characters=-1🔗
- voidset_visible_characters(value:int)
voidset_visible_characters(value:int)
- intget_visible_characters()
intget_visible_characters()
The number of characters to display. If set to-1, all characters are displayed. This can be useful when animating the text appearing in a dialog box.
Note:Setting this property updatesvisible_ratioaccordingly.
Note:Characters are counted as Unicode codepoints. A single visible grapheme may contain multiple codepoints (e.g. certain emoji use three codepoints). A single codepoint may contain two UTF-16 characters, which are used in C# strings.
VisibleCharactersBehaviorvisible_characters_behavior=0🔗
- voidset_visible_characters_behavior(value:VisibleCharactersBehavior)
voidset_visible_characters_behavior(value:VisibleCharactersBehavior)
- VisibleCharactersBehaviorget_visible_characters_behavior()
VisibleCharactersBehaviorget_visible_characters_behavior()
The clipping behavior whenvisible_charactersorvisible_ratiois set.
floatvisible_ratio=1.0🔗
- voidset_visible_ratio(value:float)
voidset_visible_ratio(value:float)
- floatget_visible_ratio()
floatget_visible_ratio()
The fraction of characters to display, relative to the total number of characters (seeget_total_character_count()). If set to1.0, all characters are displayed. If set to0.5, only half of the characters will be displayed. This can be useful when animating the text appearing in a dialog box.
Note:Setting this property updatesvisible_charactersaccordingly.

## Method Descriptions
voidadd_hr(width:int= 90, height:int= 2, color:Color= Color(1, 1, 1, 1), alignment:HorizontalAlignment= 1, width_in_percent:bool= true, height_in_percent:bool= false)🔗
Adds a horizontal rule that can be used to separate content.
Ifwidth_in_percentis set,widthvalues are percentages of the control width instead of pixels.
Ifheight_in_percentis set,heightvalues are percentages of the control width instead of pixels.
voidadd_image(image:Texture2D, width:int= 0, height:int= 0, color:Color= Color(1, 1, 1, 1), inline_align:InlineAlignment= 5, region:Rect2= Rect2(0, 0, 0, 0), key:Variant= null, pad:bool= false, tooltip:String= "", width_in_percent:bool= false, height_in_percent:bool= false, alt_text:String= "")🔗
Adds an image's opening and closing tags to the tag stack, optionally providing awidthandheightto resize the image, acolorto tint the image and aregionto only use parts of the image.
Ifwidthorheightis set to 0, the image size will be adjusted in order to keep the original aspect ratio.
Ifwidthandheightare not set, butregionis, the region's rect will be used.
keyis an optional identifier, that can be used to modify the image viaupdate_image().
Ifpadis set, and the image is smaller than the size specified bywidthandheight, the image padding is added to match the size instead of upscaling.
Ifwidth_in_percentis set,widthvalues are percentages of the control width instead of pixels.
Ifheight_in_percentis set,heightvalues are percentages of the control width instead of pixels.
alt_textis used as the image description for assistive apps.
voidadd_text(text:String)🔗
Adds raw non-BBCode-parsed text to the tag stack.
voidappend_text(bbcode:String)🔗
Parsesbbcodeand adds tags to the tag stack as needed.
Note:Using this method, you can't close a tag that was opened in a previousappend_text()call. This is done to improve performance, especially when updating large RichTextLabels since rebuilding the whole BBCode every time would be slower. If you absolutely need to close a tag in a future method call, append thetextinstead of usingappend_text().
voidclear()🔗
Clears the tag stack, causing the label to display nothing.
Note:This method does not affecttext, and its contents will show again if the label is redrawn. However, settingtextto an emptyStringalso clears the stack.
voiddeselect()🔗
Clears the current selection.
intget_character_line(character:int)🔗
Returns the line number of the character position provided. Line and character numbers are both zero-indexed.
Note:Ifthreadedis enabled, this method returns a value for the loaded part of the document. Useis_finished()orfinishedto determine whether document is fully loaded.
intget_character_paragraph(character:int)🔗
Returns the paragraph number of the character position provided. Paragraph and character numbers are both zero-indexed.
Note:Ifthreadedis enabled, this method returns a value for the loaded part of the document. Useis_finished()orfinishedto determine whether document is fully loaded.
intget_content_height()const🔗
Returns the height of the content.
Note:This method always returns the full content size, and is not affected byvisible_ratioandvisible_characters. To get the visible content size, useget_visible_content_rect().
Note:Ifthreadedis enabled, this method returns a value for the loaded part of the document. Useis_finished()orfinishedto determine whether document is fully loaded.
intget_content_width()const🔗
Returns the width of the content.
Note:This method always returns the full content size, and is not affected byvisible_ratioandvisible_characters. To get the visible content size, useget_visible_content_rect().
Note:Ifthreadedis enabled, this method returns a value for the loaded part of the document. Useis_finished()orfinishedto determine whether document is fully loaded.
intget_line_count()const🔗
Returns the total number of lines in the text. Wrapped text is counted as multiple lines.
Note:Ifthreadedis enabled, this method returns a value for the loaded part of the document. Useis_finished()orfinishedto determine whether document is fully loaded.
intget_line_height(line:int)const🔗
Returns the height of the line found at the provided index.
Note:Ifthreadedis enabled, this method returns a value for the loaded part of the document. Useis_finished()orfinishedto determine whether the document is fully loaded.
floatget_line_offset(line:int)🔗
Returns the vertical offset of the line found at the provided index.
Note:Ifthreadedis enabled, this method returns a value for the loaded part of the document. Useis_finished()orfinishedto determine whether document is fully loaded.
Vector2iget_line_range(line:int)🔗
Returns the indexes of the first and last visible characters for the givenline, as aVector2i.
Note:Ifvisible_characters_behavioris set toTextServer.VC_CHARS_BEFORE_SHAPINGonly visible wrapped lines are counted.
Note:Ifthreadedis enabled, this method returns a value for the loaded part of the document. Useis_finished()orfinishedto determine whether document is fully loaded.
intget_line_width(line:int)const🔗
Returns the width of the line found at the provided index.
Note:Ifthreadedis enabled, this method returns a value for the loaded part of the document. Useis_finished()orfinishedto determine whether the document is fully loaded.
PopupMenuget_menu()const🔗
Returns thePopupMenuof thisRichTextLabel. By default, this menu is displayed when right-clicking on theRichTextLabel.
You can add custom menu items or remove standard ones. Make sure your IDs don't conflict with the standard ones (seeMenuItems). For example:
```
func _ready():
    var menu = get_menu()
    # Remove "Select All" item.
    menu.remove_item(MENU_SELECT_ALL)
    # Add custom items.
    menu.add_separator()
    menu.add_item("Duplicate Text", MENU_MAX + 1)
    # Connect callback.
    menu.id_pressed.connect(_on_item_pressed)

func _on_item_pressed(id):
    if id == MENU_MAX + 1:
        add_text("\n" + get_parsed_text())
```
```
public override void _Ready()
{
    var menu = GetMenu();
    // Remove "Select All" item.
    menu.RemoveItem(RichTextLabel.MenuItems.SelectAll);
    // Add custom items.
    menu.AddSeparator();
    menu.AddItem("Duplicate Text", RichTextLabel.MenuItems.Max + 1);
    // Add event handler.
    menu.IdPressed += OnItemPressed;
}

public void OnItemPressed(int id)
{
    if (id == TextEdit.MenuItems.Max + 1)
    {
        AddText("\n" + GetParsedText());
    }
}
```
Warning:This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use theirWindow.visibleproperty.
intget_paragraph_count()const🔗
Returns the total number of paragraphs (newlines orptags in the tag stack's text tags). Considers wrapped text as one paragraph.
floatget_paragraph_offset(paragraph:int)🔗
Returns the vertical offset of the paragraph found at the provided index.
Note:Ifthreadedis enabled, this method returns a value for the loaded part of the document. Useis_finished()orfinishedto determine whether document is fully loaded.
Stringget_parsed_text()const🔗
Returns the text without BBCode mark-up.
Stringget_selected_text()const🔗
Returns the current selection text. Does not include BBCodes.
intget_selection_from()const🔗
Returns the current selection first character index if a selection is active,-1otherwise. Does not include BBCodes.
floatget_selection_line_offset()const🔗
Returns the current selection vertical line offset if a selection is active,-1.0otherwise.
intget_selection_to()const🔗
Returns the current selection last character index if a selection is active,-1otherwise. Does not include BBCodes.
intget_total_character_count()const🔗
Returns the total number of characters from text tags. Does not include BBCodes.
VScrollBarget_v_scroll_bar()🔗
Returns the vertical scrollbar.
Warning:This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use theirCanvasItem.visibleproperty.
Rect2iget_visible_content_rect()const🔗
Returns the bounding rectangle of the visible content.
Note:This method returns a correct value only after the label has been drawn.
```
extends RichTextLabel

@export var background_panel: Panel

func _ready():
    await draw
    background_panel.position = get_visible_content_rect().position
    background_panel.size = get_visible_content_rect().size
```
```
public partial class TestLabel : RichTextLabel
{
    [Export]
    public Panel BackgroundPanel { get; set; }

    public override async void _Ready()
    {
        await ToSignal(this, Control.SignalName.Draw);
        BackgroundGPanel.Position = GetVisibleContentRect().Position;
        BackgroundPanel.Size = GetVisibleContentRect().Size;
    }
}
```
intget_visible_line_count()const🔗
Returns the number of visible lines.
Note:This method returns a correct value only after the label has been drawn.
Note:Ifthreadedis enabled, this method returns a value for the loaded part of the document. Useis_finished()orfinishedto determine whether document is fully loaded.
intget_visible_paragraph_count()const🔗
Returns the number of visible paragraphs. A paragraph is considered visible if at least one of its lines is visible.
Note:This method returns a correct value only after the label has been drawn.
Note:Ifthreadedis enabled, this method returns a value for the loaded part of the document. Useis_finished()orfinishedto determine whether document is fully loaded.
voidinstall_effect(effect:Variant)🔗
Installs a custom effect. This can also be done in the Inspector through thecustom_effectsproperty.effectshould be a validRichTextEffect.
Example:With the following script extending fromRichTextEffect:
```
# effect.gd
class_name MyCustomEffect
extends RichTextEffect

var bbcode = "my_custom_effect"

# ...
```
The above effect can be installed inRichTextLabelfrom a script:
```
# rich_text_label.gd
extends RichTextLabel

func _ready():
    install_effect(MyCustomEffect.new())

    # Alternatively, if not using `class_name` in the script that extends RichTextEffect:
    install_effect(preload("res://effect.gd").new())
```
boolinvalidate_paragraph(paragraph:int)🔗
Invalidatesparagraphand all subsequent paragraphs cache.
boolis_finished()const🔗
Ifthreadedis enabled, returnstrueif the background thread has finished text processing, otherwise always returntrue.
boolis_menu_visible()const🔗
Returns whether the menu is visible. Use this instead ofget_menu().visibleto improve performance (so the creation of the menu is avoided).
boolis_ready()const🔗
Deprecated:Useis_finished()instead.
Ifthreadedis enabled, returnstrueif the background thread has finished text processing, otherwise always returntrue.
voidmenu_option(option:int)🔗
Executes a given action as defined in theMenuItemsenum.
voidnewline()🔗
Adds a newline tag to the tag stack.
voidparse_bbcode(bbcode:String)🔗
The assignment version ofappend_text(). Clears the tag stack and inserts the new content.
Dictionaryparse_expressions_for_values(expressions:PackedStringArray)🔗
Parses BBCode parameterexpressionsinto a dictionary.
voidpop()🔗
Terminates the current tag. Use afterpush_*methods to close BBCodes manually. Does not need to followadd_*methods.
voidpop_all()🔗
Terminates all tags opened bypush_*methods.
voidpop_context()🔗
Terminates tags opened after the lastpush_context()call (including context marker), or all tags if there's no context marker on the stack.
voidpush_bgcolor(bgcolor:Color)🔗
Adds a[bgcolor]tag to the tag stack.
Note:The background color has padding applied by default, which is controlled usingtext_highlight_h_paddingandtext_highlight_v_padding. This can lead to overlapping highlights if background colors are placed on neighboring lines/columns, so consider setting those theme items to0if you want to avoid this.
voidpush_bold()🔗
Adds a[font]tag with a bold font to the tag stack. This is the same as adding a[b]tag if not currently in a[i]tag.
voidpush_bold_italics()🔗
Adds a[font]tag with a bold italics font to the tag stack.
voidpush_cell()🔗
Adds a[cell]tag to the tag stack. Must be inside a[table]tag. Seepush_table()for details. Useset_table_column_expand()to set column expansion ratio,set_cell_border_color()to set cell border,set_cell_row_background_color()to set cell background,set_cell_size_override()to override cell size, andset_cell_padding()to set padding.
voidpush_color(color:Color)🔗
Adds a[color]tag to the tag stack.
voidpush_context()🔗
Adds a context marker to the tag stack. Seepop_context().
voidpush_customfx(effect:RichTextEffect, env:Dictionary)🔗
Adds a custom effect tag to the tag stack. The effect does not need to be incustom_effects. The environment is directly passed to the effect.
voidpush_dropcap(string:String, font:Font, size:int, dropcap_margins:Rect2= Rect2(0, 0, 0, 0), color:Color= Color(1, 1, 1, 1), outline_size:int= 0, outline_color:Color= Color(0, 0, 0, 0))🔗
Adds a[dropcap]tag to the tag stack. Drop cap (dropped capital) is a decorative element at the beginning of a paragraph that is larger than the rest of the text.
voidpush_fgcolor(fgcolor:Color)🔗
Adds a[fgcolor]tag to the tag stack.
Note:The foreground color has padding applied by default, which is controlled usingtext_highlight_h_paddingandtext_highlight_v_padding. This can lead to overlapping highlights if foreground colors are placed on neighboring lines/columns, so consider setting those theme items to0if you want to avoid this.
voidpush_font(font:Font, font_size:int= 0)🔗
Adds a[font]tag to the tag stack. Overrides default fonts for its duration.
Passing0tofont_sizewill use the existing default font size.
voidpush_font_size(font_size:int)🔗
Adds a[font_size]tag to the tag stack. Overrides default font size for its duration.
voidpush_hint(description:String)🔗
Adds a[hint]tag to the tag stack. Same as BBCode[hint=something]{text}[/hint].
voidpush_indent(level:int)🔗
Adds an[indent]tag to the tag stack. Multiplieslevelby currenttab_sizeto determine new margin length.
voidpush_italics()🔗
Adds a[font]tag with an italics font to the tag stack. This is the same as adding an[i]tag if not currently in a[b]tag.
voidpush_language(language:String)🔗
Adds language code used for text shaping algorithm and Open-Type font features.
voidpush_list(level:int, type:ListType, capitalize:bool, bullet:String= "•")🔗
Adds[ol]or[ul]tag to the tag stack. Multiplieslevelby currenttab_sizeto determine new margin length.
voidpush_meta(data:Variant, underline_mode:MetaUnderline= 1, tooltip:String= "")🔗
Adds a meta tag to the tag stack. Similar to the BBCode[url=something]{text}[/url], but supports non-Stringmetadata types.
Ifmeta_underlinedistrue, meta tags display an underline. This behavior can be customized withunderline_mode.
Note:Meta tags do nothing by default when clicked. To assign behavior when clicked, connectmeta_clickedto a function that is called when the meta tag is clicked.
voidpush_mono()🔗
Adds a[font]tag with a monospace font to the tag stack.
voidpush_normal()🔗
Adds a[font]tag with a normal font to the tag stack.
voidpush_outline_color(color:Color)🔗
Adds a[outline_color]tag to the tag stack. Adds text outline for its duration.
voidpush_outline_size(outline_size:int)🔗
Adds a[outline_size]tag to the tag stack. Overrides default text outline size for its duration.
voidpush_paragraph(alignment:HorizontalAlignment, base_direction:TextDirection= 0, language:String= "", st_parser:StructuredTextParser= 0, justification_flags:BitField[JustificationFlag] = 163, tab_stops:PackedFloat32Array= PackedFloat32Array())🔗
Adds a[p]tag to the tag stack.
voidpush_strikethrough(color:Color= Color(0, 0, 0, 0))🔗
Adds a[s]tag to the tag stack. Ifcolor's alpha value is0.0, the current font's color with its alpha multiplied bystrikethrough_alphais used.
voidpush_table(columns:int, inline_align:InlineAlignment= 0, align_to_row:int= -1, name:String= "")🔗
Adds a[table=columns,inline_align]tag to the tag stack. Useset_table_column_expand()to set column expansion ratio. Usepush_cell()to add cells.nameis used as the table name for assistive apps.
voidpush_underline(color:Color= Color(0, 0, 0, 0))🔗
Adds a[u]tag to the tag stack. Ifcolor's alpha value is0.0, the current font's color with its alpha multiplied byunderline_alphais used.
voidreload_effects()🔗
Reloads custom effects. Useful whencustom_effectsis modified manually.
boolremove_paragraph(paragraph:int, no_invalidate:bool= false)🔗
Removes a paragraph of content from the label. Returnstrueif the paragraph exists.
Theparagraphargument is the index of the paragraph to remove, it can take values in the interval[0,get_paragraph_count()-1].
Ifno_invalidateis set totrue, cache for the subsequent paragraphs is not invalidated. Use it for faster updates if deleted paragraph is fully self-contained (have no unclosed tags), or this call is part of the complex edit operation andinvalidate_paragraph()will be called at the end of operation.
voidscroll_to_line(line:int)🔗
Scrolls the window's top line to matchline.
voidscroll_to_paragraph(paragraph:int)🔗
Scrolls the window's top line to match first line of theparagraph.
voidscroll_to_selection()🔗
Scrolls to the beginning of the current selection.
voidselect_all()🔗
Select all the text.
Ifselection_enabledisfalse, no selection will occur.
voidset_cell_border_color(color:Color)🔗
Sets color of a table cell border.
voidset_cell_padding(padding:Rect2)🔗
Sets inner padding of a table cell.
voidset_cell_row_background_color(odd_row_bg:Color, even_row_bg:Color)🔗
Sets color of a table cell. Separate colors for alternating rows can be specified.
voidset_cell_size_override(min_size:Vector2, max_size:Vector2)🔗
Sets minimum and maximum size overrides for a table cell.
voidset_table_column_expand(column:int, expand:bool, ratio:int= 1, shrink:bool= true)🔗
Edits the selected column's expansion options. Ifexpandistrue, the column expands in proportion to its expansion ratio versus the other columns' ratios.
For example, 2 columns with ratios 3 and 4 plus 70 pixels in available width would expand 30 and 40 pixels, respectively.
Ifexpandisfalse, the column will not contribute to the total ratio.
voidset_table_column_name(column:int, name:String)🔗
Sets table column name for assistive apps.
voidupdate_image(key:Variant, mask:BitField[ImageUpdateMask], image:Texture2D, width:int= 0, height:int= 0, color:Color= Color(1, 1, 1, 1), inline_align:InlineAlignment= 5, region:Rect2= Rect2(0, 0, 0, 0), pad:bool= false, tooltip:String= "", width_in_percent:bool= false, height_in_percent:bool= false)🔗
Updates the existing images with the keykey. Only properties specified bymaskbits are updated. Seeadd_image().

## Theme Property Descriptions
Colordefault_color=Color(1,1,1,1)🔗
The default text color.
Colorfont_outline_color=Color(0,0,0,1)🔗
The default tint of text outline.
Colorfont_selected_color=Color(0,0,0,0)🔗
The color of selected text, used whenselection_enabledistrue. If equal toColor(0,0,0,0), it will be ignored.
Colorfont_shadow_color=Color(0,0,0,0)🔗
The color of the font's shadow.
Colorselection_color=Color(0.1,0.1,1,0.8)🔗
The color of the selection box.
Colortable_border=Color(0,0,0,0)🔗
The default cell border color.
Colortable_even_row_bg=Color(0,0,0,0)🔗
The default background color for even rows.
Colortable_odd_row_bg=Color(0,0,0,0)🔗
The default background color for odd rows.
intline_separation=0🔗
Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.
intoutline_size=0🔗
The size of the text outline.
Note:If using a font withFontFile.multichannel_signed_distance_fieldenabled, itsFontFile.msdf_pixel_rangemust be set to at leasttwicethe value ofoutline_sizefor outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.
intparagraph_separation=0🔗
Additional vertical spacing between paragraphs (in pixels). Spacing is added after the last line. This value can be negative.
intshadow_offset_x=1🔗
The horizontal offset of the font's shadow.
intshadow_offset_y=1🔗
The vertical offset of the font's shadow.
intshadow_outline_size=1🔗
The size of the shadow outline.
intstrikethrough_alpha=50🔗
The default strikethrough color transparency (percent). For strikethroughs with a custom color, this theme item is only used if the custom color's alpha is0.0(fully transparent).
inttable_h_separation=3🔗
The horizontal separation of elements in a table.
inttable_v_separation=3🔗
The vertical separation of elements in a table.
inttext_highlight_h_padding=3🔗
The horizontal padding around boxes drawn by the[fgcolor]and[bgcolor]tags. This does not affect the appearance of text selection. To avoid any risk of neighboring highlights overlapping each other, set this to0to disable padding.
inttext_highlight_v_padding=3🔗
The vertical padding around boxes drawn by the[fgcolor]and[bgcolor]tags. This does not affect the appearance of text selection. To avoid any risk of neighboring highlights overlapping each other, set this to0to disable padding.
intunderline_alpha=50🔗
The default underline color transparency (percent). For underlines with a custom color, this theme item is only used if the custom color's alpha is0.0(fully transparent).
Fontbold_font🔗
The font used for bold text.
Fontbold_italics_font🔗
The font used for bold italics text.
Fontitalics_font🔗
The font used for italics text.
Fontmono_font🔗
The font used for monospace text.
Fontnormal_font🔗
The default text font.
intbold_font_size🔗
The font size used for bold text.
intbold_italics_font_size🔗
The font size used for bold italics text.
intitalics_font_size🔗
The font size used for italics text.
intmono_font_size🔗
The font size used for monospace text.
intnormal_font_size🔗
The default text font size.
Texture2Dhorizontal_rule🔗
The horizontal rule texture.
StyleBoxfocus🔗
The background used when theRichTextLabelis focused. ThefocusStyleBoxis displayedoverthe baseStyleBox, so a partially transparentStyleBoxshould be used to ensure the baseStyleBoxremains visible. AStyleBoxthat represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign aStyleBoxEmptyresource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.
StyleBoxnormal🔗
The normal background for theRichTextLabel.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.