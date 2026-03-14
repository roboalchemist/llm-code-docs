# Source: https://gui-cs.github.io/Terminal.Gui/docs/views.html

Title: Terminal Gui's Built-in Views | Terminal.Gui v2

URL Source: https://gui-cs.github.io/Terminal.Gui/docs/views.html

Markdown Content:
_Terminal.Gui_ provides the following set of built-in views and controls for building terminal user interfaces:

[Attribute Picker](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.AttributePicker.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#attributepicker)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Allows the user to pick an [Attribute](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.Attribute.html) by selecting foreground and background colors, and text styles.

┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊┌┤Foreground├───────────────────────────────────────────────┬┤Style├────────┐ ┊
┊│H:                                                    ▲355 │☒ Bold │ ┊
┊│S:                                   ▲               70 │☐ Faint │ ┊
┊│V:                                               ▲    91 │☒ Italic │ ┊
┊│Name: BrightRed  │☐ Underline │ ┊
┊│Hex:#E74856  ■ │☐ Blink │ ┊
┊├┼Background┼───────────────────────────────────────────────┤☐ Reverse │ ┊
┊│H:                                   ▲                 240 │☐ Strikethrough│ ┊
┊│S:                                      ▲100 │ │ ┊
┊│V:                                      ▲100 │ │ ┊
┊│Name: Blue  │ │ ┊
┊│Hex:#0000FF  ■ │ │ ┊
┊└───────────────────────────────────────────────────────────┴───────────────┘ ┊
┊ Multi-line Sample Text. ┊
┊ This is the second line. ┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[Bar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Bar.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#bar)
-----------------------------------------------------------------------------------------------------------------------------------------

A container for [Shortcut](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Shortcut.html) items that arranges them horizontally or vertically. Serves as the base class for [Menu](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Menu.html), [Menu Bar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.MenuBar.html), and [Status Bar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.StatusBar.html).

┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊ Shortcut Shortcut help F1  Help Help Text F1 ☐ Check Czech F9 ┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[Button](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Button.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#button)
--------------------------------------------------------------------------------------------------------------------------------------------------

Raises the [Accepting](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.Accepting.html) and [Accepted](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.Accepted.html) events when the user presses [Hot Key](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.HotKey.html#Terminal_Gui_ViewBase_View_HotKey), `Enter`, or `Space` or clicks with the mouse.

┌┤Button├┄┄┐
┊⟦ Button ⟧┊
└┄┄┄┄┄┄┄┄┄┄┘

[Char Map](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.CharMap.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#charmap)
------------------------------------------------------------------------------------------------------------------------------------------------------

A scrollable map of the Unicode codepoints.

┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊ 0 1 2 3 4 5 6 7 8 9 a b c d e f ┊
┊U+00000_␀ ␁ ␂ ␃ ␄ ␅ ␆ ␇ ␈ ␉ ␊ ␋ ␌ ␍ ␎ ␏ ▲┊
┊U+00001_ ␐ ␑ ␒ ␓ ␔ ␕ ␖ ␗ ␘ ␙ ␚ ␛ ␜ ␝ ␞ ␟ █┊
┊U+00002_! " # $ % & ' ( ) * + , - . / ░┊
┊U+00003_ 0 1 2 3 4 5 6 7 8 9 : ; < = > ? ░┊
┊U+00004_@ A B C D E F G H I J K L M N O ░┊
┊U+00005_ P Q R S T U V W X Y Z [ \ ] ^ _░┊
┊U+00006_ ` a b c d e f g h i j k l m n o ░┊
┊U+00007_p q r s t u v w x y z { | } ~ ⑿ ░┊
┊U+00008_ ⒀ ⒁ ⒂ ⒃ ⒄ ⒅ ⒆ ⒇ ⒈ ⒉ ⒊ ⒋ ⒌ ⒍ ⒎ ⒏ ░┊
┊U+00009_⒐ ⒑ ⒒ ⒓ ⒔ ⒕ ⒖ ⒗ ⒘ ⒙ ⒚ ⒛ ⒜ ⒝ ⒞ ⒟ ░┊
┊U+0000a_  ¡ ¢ £ ¤ ¥ ¦ § ¨ © ª « ¬ F ® ¯ ░┊
┊U+0000b_° ± ² ³ ´ µ ¶ · ¸ ¹ º » ¼ ½ ¾ ¿ ░┊
┊U+0000c_ À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï ░┊
┊U+0000d_Ð Ñ Ò Ó Ô Õ Ö × Ø Ù Ú Û Ü Ý Þ ß ░┊
┊U+0000e_ à á â ã ä å æ ç è é ê ë ì í î ï ░┊
┊U+0000f_ð ñ ò ó ô õ ö ÷ ø ù ú û ü ý þ ÿ ░┊
┊U+00010_ Ā ā Ă ă Ą ą Ć ć Ĉ ĉ Ċ ċ Č č Ď ď ▼┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[Check Box](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.CheckBox.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#checkbox)
---------------------------------------------------------------------------------------------------------------------------------------------------------

Shows a checkbox that can be cycled between two or three states.

┌┤This is some demo text.├┐
┊☐ This is some demo text.┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[Color Picker](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.ColorPicker.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#colorpicker)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Color Picker supporting RGB, HSL, and HSV color models. Supports choosing colors with sliders and color names from the [IColor Name Resolver](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.IColorNameResolver.html).

┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊H:                         ▲355 ┊
┊S:                  ▲       70 ┊
┊V:                       ▲  91 ┊
┊Hex:#E74856  ■ ┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[Color Picker16](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.ColorPicker16.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#colorpicker16)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A sinple color picker that supports the legacy 16 ANSI colors

┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊┌┄┄┐       ┊
┊└┄┄┘       ┊
┊        ┊
┊        ┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[DateField](xref:Terminal.Gui.Views.DateField)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#datefield)
-----------------------------------------------------------------------------------------------------------------

Provides date editing functionality with specialized cursor behavior for date entry.

[Date Picker](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.DatePicker.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#datepicker)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Lets the user pick a date from a visual calendar.

┌─────────────────────────────┐
│Date: 03/10/2026 │
│┌───┬───┬───┬───┬───┬───┬───┐│
││Sun│Mon│Tue│Wed│Thu│Fri│Sat││
│├───┼───┼───┼───┼───┼───┼───┤│
││1 │2 │3 │4 │5 │6 │7 ││
││8 │9 │10 │11 │12 │13 │14 ││
││15 │16 │17 │18 │19 │20 │21 ││
││22 │23 │24 │25 │26 │27 │28 ││
││29 │30 │31 │- │- │- │- ││
││- │- │- │- │- │- │- ││
│└───┴───┴───┴───┴───┴───┴───┘│
│ ◄◄ ►► │
└─────────────────────────────┘

[Dialog](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Dialog.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#dialog)
--------------------------------------------------------------------------------------------------------------------------------------------------

A modal dialog window with buttons across the bottom. When a button is pressed, [Result](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IRunnable-1.Result.html#Terminal_Gui_App_IRunnable_1_Result) is set to the button's index (0-based).

┏┥Dialog Title┝━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃Example: Type and press ENTER to accept.  ┃
┃                                                  ┃
┃                                                  ┃
┃                               ⟦ Cancel ⟧ ⟦► OK ◄⟧┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

[Dialog<T>](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Dialog-1.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#dialogt)
--------------------------------------------------------------------------------------------------------------------------------------------------------

A generic modal dialog window with buttons across the bottom. Derive from this class to create dialogs that return custom result types.

[Drop Down List](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.DropDownList.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#dropdownlist)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

A dropdown/combo-box control that combines a [Text Field](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.TextField.html) with a popover [List View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.ListView.html) for selecting from a list of items.

┌┄┄┄┄┄┄┄┄┄┄┐
┊Germany ▼┊
└┄┄┄┄┄┄┄┄┄┄┘

[File Dialog](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.FileDialog.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#filedialog)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

The base-class for [Open Dialog](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.OpenDialog.html) and [Save Dialog](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.SaveDialog.html)

┏┥Open┝━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃C:\Users\Tig\s\gui-cs\Terminal.Gui\docfx ┃
┃⟦▲⟧                                                                        ┃
┃┌────────────────────┬──────────┬──────────────────────────────┬───────────┃
┃│Filename (▲)        │Size      │Modified                      │Type       ┃
┃├────────────────────┼──────────┼──────────────────────────────┼───────────┃
┃│.. │ │ │<Directory>┃
┃│\_exported_templates│          │2025-09-12T12:16:14           │<Directory>┃
┃│\_site              │          │2026-03-10T11:03:24           │<Directory>┃
┃│\api                │          │2026-03-10T11:02:45           │<Directory>┃
┃│\apispec            │          │2026-03-09T09:23:54           │<Directory>┃
┃│\docs               │          │2026-03-10T10:40:04           │<Directory>┃
┃│\images             │          │2026-03-04T13:02:07           │<Directory>┃
┃│\includes           │          │2026-03-04T12:44:37           │<Directory>┃
┃│\schemas            │          │2026-01-15T21:25:29           │<Directory>┃
┃│\scripts            │          │2026-03-04T12:44:37           │<Directory>┃
┃│aboutbox.png        │14.06 KB  │2025-09-12T12:16:14           │.png       ┃
┃                                                                           ┃
┃⟦►Tree⟧                                                  ⟦ Cancel ⟧⟦► OK ◄⟧┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

[Flag Selector](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.FlagSelector.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#flagselector)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Provides a user interface for displaying and selecting non-mutually-exclusive flags from a provided dictionary. [FlagSelector<TFlagsEnum>](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.FlagSelector-1.html) provides a type-safe version where a `[Flags]` enum can be provided.

┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊☒ No Style ┊
┊☐ Show None Value Style ┊
┊☐ ShowAllFlag ┊
┊☐ Show Value Editor Style┊
┊☐ All Styles ┊
┊0 ┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[FlagSelector<T>](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.FlagSelector-1.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#flagselectort)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Provides a user interface for displaying and selecting non-mutually-exclusive flags in a type-safe way. [Flag Selector](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.FlagSelector.html) provides a non-type-safe version. `TFlagsEnum` must be a valid enum type with the '[Flags]' attribute.

[Frame View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.FrameView.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#frameview)
------------------------------------------------------------------------------------------------------------------------------------------------------------

A non-overlapped container for other views with a border and optional title.

╭──────────────────────────────────────────────────────────────────────────────╮
│This is some demo text. │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
╰──────────────────────────────────────────────────────────────────────────────╯

[Graph View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.GraphView.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#graphview)
------------------------------------------------------------------------------------------------------------------------------------------------------------

Displays graphs (bar, scatter, etc.) with flexible labels, scaling, and scrolling

┌┤Sine Wave├┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊ │ . ∙ ┊
┊ ┤ ∙ . ┊
┊ │ . .. ┊
┊ │ .. . ┊
┊ 0.20┤. ∙ ┊
┊ ┬────┬────┬────┬────┬────∙────┬────┬────┬────┬────┬────┬────┬────┬────┬────┊
┊ -2.50 -1.50 -0.50 .│ 0.50 1.50 2.50 .3.50 4.50 ┊
┊ . │ . ┊
┊↑ -0.20┤ . ┊
┊Y. . │ ∙ ┊
┊ . ∙ ┤ . ┊
┊ ∙ . │ .. ┊
┊ . .. -0.60┤ . ┊
┊ .. . │ ∙. ┊
┊ . ..∙ ┤ .. ┊
┊ ∙....∙.. -1.00┤ .∙....┊
┊ ┊
┊ X → ┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[Hex View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.HexView.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#hexview)
------------------------------------------------------------------------------------------------------------------------------------------------------

Provides a hex editor with the left side showing the hex values of the bytes in a `Stream` and the right side showing the contents (filtered to printable Unicode glyphs).

┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊00000000 48 65 78 56 ┊ 69 65 77 20 ┊ 64 61 74 61 HexView data ┊
┊0000000c 20 77 69 74 ┊ 68 20 77 69 ┊ 64 65 20 63 with wide c ┊
┊00000018 6f 64 65 70 ┊ 6f 69 6e 74 ┊ 73 3a 20 f0 odepoints: � ┊
┊00000024 9d 94 b9 41 ┊ e2 84 9d f0 ┊ 9d 94 bd 21 ���A�������! ┊
┊00000030 ┊ ┊ ┊
┊0000003c ┊ ┊ ┊
┊00000048 ┊ ┊ ┊
┊00000054 ┊ ┊ ┊
┊00000060 ┊ ┊ ┊
┊0000006c ┊ ┊ ┊
┊00000078 ┊ ┊ ┊
┊00000084 ┊ ┊ ┊
┊00000090 ┊ ┊ ┊
┊0000009c ┊ ┊ ┊
┊000000a8 ┊ ┊ ┊
┊000000b4 ┊ ┊ ┊
┊000000c0 ┊ ┊ ┊
┊000000cc ┊ ┊ ┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[Label](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Label.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#label)
-----------------------------------------------------------------------------------------------------------------------------------------------

Displays text that describes the View next in the [Sub Views](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.SubViews.html#Terminal_Gui_ViewBase_View_SubViews). When the user presses a hotkey that matches the [Hot Key](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.HotKey.html#Terminal_Gui_ViewBase_View_HotKey) of the Label, the next [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) in [Sub Views](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.SubViews.html#Terminal_Gui_ViewBase_View_SubViews) will be activated.

┌┤Lab├┐
┊Label┊
└┄┄┄┄┄┘

[Legend Annotation](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.LegendAnnotation.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#legendannotation)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Used by [Graph View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.GraphView.html) to render symbol definitions in a graph, e.g. colors and their meanings

┌──────────────────────────────────────────────────────────────────────────────┐
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
└──────────────────────────────────────────────────────────────────────────────┘

[Line](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Line.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#line)
--------------------------------------------------------------------------------------------------------------------------------------------

Draws a single line using the [Line Style](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.LineStyle.html) specified by [Style](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Line.Style.html#Terminal_Gui_Views_Line_Style).

┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

[Linear Range](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.LinearRange.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#linearrange)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Provides a linear range control letting the user navigate from a set of typed options in a linear manner using the keyboard or mouse.

┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊ ● ┊
┊This is some demo text.┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[LinearRange<T>](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.LinearRange-1.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#linearranget)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Provides a type-safe linear range control letting the user navigate from a set of typed options in a linear manner using the keyboard or mouse.

[List View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.ListView.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#listview)
---------------------------------------------------------------------------------------------------------------------------------------------------------

Provides a scrollable list of data where each item can be activated to perform an action.

┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊List Item 1 ┊
┊List Item two ┊
┊List Item 3 ┊
┊List Item Quattro ┊
┊Last List Item ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

A vertically-oriented [Bar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Bar.html) that contains [Menu Item](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.MenuItem.html) items, supporting cascading sub-menus, selection tracking, and the [IValue<TValue>](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.IValue-1.html) pattern.

┌────────────────────────────────────┐
│ Format Text formatting options ► ┌
│ View View options ► │
├────────────────────────────────────│
│ About About this demo │
└────────────────────────────────────└

A horizontal [Menu](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Menu.html) that contains [Menu Bar Item](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.MenuBarItem.html) items. Each [Menu Bar Item](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.MenuBarItem.html) owns a [Popover Menu](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.PopoverMenu.html) that is displayed as a drop-down when the item is selected. Typically placed at the top of a window or view.

 File Edit Help

A [Menu Item](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.MenuItem.html)-derived item for use in a [Menu Bar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.MenuBar.html). Each [Menu Bar Item](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.MenuBarItem.html) holds either a [Popover Menu](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.MenuBarItem.PopoverMenu.html#Terminal_Gui_Views_MenuBarItem_PopoverMenu) (modal, default) or an inline [Sub Menu](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.MenuItem.SubMenu.html#Terminal_Gui_Views_MenuItem_SubMenu) (non-modal) that is displayed as a drop-down menu when the item is selected. The behavior is controlled by the [Use Popover Menu](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.MenuBarItem.UsePopoverMenu.html#Terminal_Gui_Views_MenuBarItem_UsePopoverMenu) property.

┌┄┄┐
┊ ┊
└┄┄┘

A [Shortcut](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Shortcut.html)-derived item for use in a [Menu](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Menu.html). Displays a command, help text, and key binding and supports nested [Sub Menu](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.MenuItem.SubMenu.html#Terminal_Gui_Views_MenuItem_SubMenu)s for cascading menu hierarchies.

┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊ Shortcut Shortcut help F1 ┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[Numeric UpDown](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.NumericUpDown.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#numericupdown)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Enables the user to increase or decrease an int by clicking on the up or down buttons.

┌┄┄┄┐
┊▼0▲┊
└┄┄┄┘

[NumericUpDown<T>](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.NumericUpDown-1.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#numericupdownt)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Enables the user to increase or decrease a value with the mouse or keyboard in type-safe way.

[Open Dialog](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.OpenDialog.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#opendialog)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Provides an interactive [Dialog](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Dialog.html) for selecting files or directories for opening

┏┥Open┝━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃C:\Users\Tig\s\gui-cs\Terminal.Gui\docfx ┃
┃⟦▲⟧                                                                        ┃
┃┌────────────────────┬──────────┬──────────────────────────────┬───────────┃
┃│Filename (▲)        │Size      │Modified                      │Type       ┃
┃├────────────────────┼──────────┼──────────────────────────────┼───────────┃
┃│.. │ │ │<Directory>┃
┃│\_exported_templates│          │2025-09-12T12:16:14           │<Directory>┃
┃│\_site              │          │2026-03-10T11:03:24           │<Directory>┃
┃│\api                │          │2026-03-10T11:02:45           │<Directory>┃
┃│\apispec            │          │2026-03-09T09:23:54           │<Directory>┃
┃│\docs               │          │2026-03-10T10:40:04           │<Directory>┃
┃│\images             │          │2026-03-04T13:02:07           │<Directory>┃
┃│\includes           │          │2026-03-04T12:44:37           │<Directory>┃
┃│\schemas            │          │2026-01-15T21:25:29           │<Directory>┃
┃│\scripts            │          │2026-03-04T12:44:37           │<Directory>┃
┃│aboutbox.png        │14.06 KB  │2025-09-12T12:16:14           │.png       ┃
┃                                                                           ┃
┃⟦►Tree⟧                                                  ⟦ Cancel ⟧⟦► OK ◄⟧┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

[Option Selector](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.OptionSelector.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#optionselector)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Provides a user interface for displaying and selecting a single item from a list of options. Each option is represented by a checkbox, but only one can be selected at a time. [OptionSelector<TEnum>](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.OptionSelector-1.html) provides a type-safe version where a enum can be provided.

┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊◉ Option 1 ┊
┊○ Option 2 ┊
┊○ Third Option ┊
┊○ Option Quattro┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[OptionSelector<T>](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.OptionSelector-1.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#optionselectort)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Provides a user interface for displaying and selecting a single item from a list of options in a type-safe way. Each option is represented by a checkbox, but only one can be selected at a time. [Option Selector](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.OptionSelector.html) provides a non-type-safe version.

A [IPopover](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IPopover.html)-derived view that provides a cascading menu. Can be used as a context menu or a drop-down menu as part of [Menu Bar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.MenuBar.html).

[Progress Bar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.ProgressBar.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#progressbar)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

A Progress Bar view that can indicate progress of an activity visually.

┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌ ┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[Prompt<T>](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Prompt-2.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#promptt)
--------------------------------------------------------------------------------------------------------------------------------------------------------

A dialog that wraps any [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) with Ok/Cancel buttons, extracting a typed result when the user accepts.

[Runnable](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Runnable.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#runnable)
--------------------------------------------------------------------------------------------------------------------------------------------------------

Base implementation of [IRunnable](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IRunnable.html) for views that can be run as blocking sessions without returning a result.

┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊This is some demo text.                                                       ┊
┊                                                                              ┊
┊                                                                              ┊
┊                                                                              ┊
┊                                                                              ┊
┊                                                                              ┊
┊                                                                              ┊
┊                                                                              ┊
┊                                                                              ┊
┊                                                                              ┊
┊                                                                              ┊
┊                                                                              ┊
┊                                                                              ┊
┊                                                                              ┊
┊                                                                              ┊
┊                                                                              ┊
┊                                                                              ┊
┊                                                                              ┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[Runnable<T>](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Runnable-1.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#runnablet)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

Base implementation of [IRunnable<TResult>](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IRunnable-1.html) for views that can be run as blocking sessions.

[Save Dialog](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.SaveDialog.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#savedialog)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Provides an interactive [Dialog](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Dialog.html) for selecting files or directories for saving

┏┥Save┝━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃C:\Users\Tig\s\gui-cs\Terminal.Gui\docfx ┃
┃⟦▲⟧                                                                        ┃
┃┌────────────────────┬──────────┬──────────────────────────────┬───────────┃
┃│Filename (▲)        │Size      │Modified                      │Type       ┃
┃├────────────────────┼──────────┼──────────────────────────────┼───────────┃
┃│.. │ │ │<Directory>┃
┃│\_exported_templates│          │2025-09-12T12:16:14           │<Directory>┃
┃│\_site              │          │2026-03-10T11:03:24           │<Directory>┃
┃│\api                │          │2026-03-10T11:02:45           │<Directory>┃
┃│\apispec            │          │2026-03-09T09:23:54           │<Directory>┃
┃│\docs               │          │2026-03-10T10:40:04           │<Directory>┃
┃│\images             │          │2026-03-04T13:02:07           │<Directory>┃
┃│\includes           │          │2026-03-04T12:44:37           │<Directory>┃
┃│\schemas            │          │2026-01-15T21:25:29           │<Directory>┃
┃│\scripts            │          │2026-03-04T12:44:37           │<Directory>┃
┃│aboutbox.png        │14.06 KB  │2025-09-12T12:16:14           │.png       ┃
┃                                                                           ┃
┃⟦►Tree⟧                                                ⟦ Cancel ⟧⟦► Save ◄⟧┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

Indicates the size of scrollable content and controls the position of the visible content, either vertically or horizontally. Two [Button](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Button.html)s are provided, one to scroll up or left and one to scroll down or right. Between the buttons is a [Scroll Slider](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.ScrollSlider.html) that can be dragged to control the position of the visible content. The ScrollSlier is sized to show the proportion of the scrollable content to the size of the [Viewport](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.Viewport.html#Terminal_Gui_ViewBase_View_Viewport).

┊
┊
┊
┊
┊
┊
┊
┊
┊
┊
┊
┊
┊
┊
┊
┊
┊
┊
┊
┊

Represents the proportion of the visible content to the Viewport in a [Scroll Bar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.ScrollBar.html). Can be dragged with the mouse, constrained by the size of the Viewport of it's superview. Can be oriented either vertically or horizontally.

┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊██████████████████████████████████████████████████████████████████████████████┊
┊██████████████████████████████████████████████████████████████████████████████┊
┊██████████████████████████████████████████████████████████████████████████████┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[Selector Base](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.SelectorBase.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#selectorbase)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

The abstract base class for [OptionSelector<TEnum>](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.OptionSelector-1.html) and [FlagSelector<TFlagsEnum>](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.FlagSelector-1.html).

[Shortcut](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Shortcut.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#shortcut)
--------------------------------------------------------------------------------------------------------------------------------------------------------

Displays a command, help text, and a key binding. Serves as the foundational building block for [Bar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Bar.html), [Menu](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Menu.html), [Menu Bar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.MenuBar.html), and [Status Bar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.StatusBar.html).

┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊ Shortcut Shortcut help F1 ┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[Spinner View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.SpinnerView.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#spinnerview)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Displays a spinning glyph or combinations of glyphs to indicate progress or activity

┌┄┐
┊●┊
└┄┘

[Status Bar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.StatusBar.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#statusbar)
------------------------------------------------------------------------------------------------------------------------------------------------------------

A status bar is a [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) that snaps to the bottom of the Viewport displaying set of [Shortcut](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Shortcut.html)s. The [Status Bar](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.StatusBar.html) should be context-sensitive. This means, if the main menu and an open text editor are visible, the items probably shown will be ~F1~ Help ~F2~ Save ~F3~ Load. While a dialog to ask a file to load is executed, the remaining commands will probably be ~F1~ Help. So for each context must be a new instance of a status bar.

 Ctrl+Z Quit Quit │ F1 Help Text Help │ F10 ☐ Show/Hide │⟦ I'll Hide ⟧│Focu

[Tab](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Tab.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#tab)
-----------------------------------------------------------------------------------------------------------------------------------------

A single tab in a [Tab View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.TabView.html).

╭──────────────────────────────────────────────────────────────────────────────╮
│This is some demo text. │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
│ │
╰──────────────────────────────────────────────────────────────────────────────╯

[Table View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.TableView.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#tableview)
------------------------------------------------------------------------------------------------------------------------------------------------------------

Displays and enables infinite scrolling through tabular data based on a [ITable Source](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.ITableSource.html). See the TableView Deep Dive for more.

┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊┌──────────────────┬──────────────────────┬──────┬───────────────────┬────────┊
┊│StrCol │DateCol │IntCol│DoubleCol │NullsCol┊
┊├──────────────────┼──────────────────────┼──────┼───────────────────┼────────┊
┊│Demo text in row 0│12/25/2000 12:00:00 AM│0 │-0.5 │- ┊
┊│Demo text in row 1│12/25/2001 12:00:00 AM│0 │0.40245424998107093│- ┊
┊│Demo text in row 2│12/25/2002 12:00:00 AM│0 │1.3973309257520972 │- ┊
┊│Demo text in row 3│12/25/2003 12:00:00 AM│2 │1.3318544644079424 │- ┊
┊│Demo text in row 4│12/25/2004 12:00:00 AM│1 │0.09525688765349649│- ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[Tab View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.TabView.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#tabview)
------------------------------------------------------------------------------------------------------------------------------------------------------

Control that hosts multiple sub views, presenting a single one at once.

┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊ ┊
┊ ┊
┊ ┊
┊│ │┊
┊│ │┊
┊│ │┊
┊│ │┊
┊│ │┊
┊│ │┊
┊│ │┊
┊│ │┊
┊│ │┊
┊│ │┊
┊│ │┊
┊│ │┊
┊│ │┊
┊│ │┊
┊└────────────────────────────────────────────────────────────────────────────┘┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[Text Field](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.TextField.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#textfield)
------------------------------------------------------------------------------------------------------------------------------------------------------------

Single-line text editor.

┌┤Caption├┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊This is a test. ┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[Text Validate Field](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.TextValidateField.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#textvalidatefield)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Masked text editor that validates input through a [IText Validate Provider](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.ITextValidateProvider.html)

┌┤^([0-9]?[0-9]?[0-9]|1000)$├──────────────────────────────────────────────────┐
│999 │
└──────────────────────────────────────────────────────────────────────────────┘

[Text View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.TextView.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#textview)
---------------------------------------------------------------------------------------------------------------------------------------------------------

Fully featured multi-line text editor

┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊TextView provides a fully featured multi-line text editor. ┊
┊It supports word wrap and history for undo. ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[TimeField](xref:Terminal.Gui.Views.TimeField)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#timefield)
-----------------------------------------------------------------------------------------------------------------

Provides time editing functionality with specialized cursor behavior for time entry.

[Tree View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.TreeView.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#treeview)
---------------------------------------------------------------------------------------------------------------------------------------------------------

Convenience implementation of generic [TreeView<T>](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.TreeView-1.html) for any tree were all nodes implement [ITree Node](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.ITreeNode.html). See TreeView Deep Dive for more information.

┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊├-Root1 ┊
┊│ ├─Child1.1 ┊
┊│ └─Child1.2 ┊
┊└-Root2 ┊
┊ ├─Child2.1 ┊
┊ └─Child2.2 ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
┊ ┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[TreeView<T>](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.TreeView-1.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#treeviewt)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

Hierarchical tree view with expandable branches. Branch objects are dynamically determined when expanded using a user defined [ITreeBuilder<T>](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.ITreeBuilder-1.html). See TreeView Deep Dive for more information.

[Window](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Window.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#window)
--------------------------------------------------------------------------------------------------------------------------------------------------

An overlapped container for other views with a border and optional title.

┌──────────────────────────────────────────────────────────────────────────────┐
│This is some demo text.                                                       │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘

[Wizard](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Wizard.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#wizard)
--------------------------------------------------------------------------------------------------------------------------------------------------

A multi-step dialog for collecting related data across sequential steps.

┌┤Wizard Title - Example Step├┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊Enter Text:                    This is some help text ┊
┊                                                  for the WizardStep. ┊
┊    A List: ┌╌╌╌╌╌╌╌╌┐                            You can provide ┊
┊            ┆Item 1 ┆                            instructions or ┊
┊            ┆Item 2  ┆                            information to guide the┊
┊            ┆Item 3  ┆                            user through this step ┊
┊            ┆Item 4  ┆                            of the wizard. ┊
┊            ┆Item 5  ┆                             ┊
┊            └╌╌╌╌╌╌╌╌┘                             ┊
┊                                                   ┊
┊                                                   ┊
┊                                                                          ┊
┊                                                             ⟦► Next... ◄⟧┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘

[Wizard Step](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.WizardStep.html)[](https://gui-cs.github.io/Terminal.Gui/docs/views.html#wizardstep)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

A single step in a [Wizard](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Views.Wizard.html). Can contain arbitrary [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html)s and display help text in the right [Padding](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.Padding.html).

┌┤Example Step├┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┊Enter Text:   This is some help text ┊
┊ for the WizardStep. ┊
┊ A List: ┌╌╌╌╌╌╌╌╌┐ You can provide ┊
┊ ┆Item 1 ┆ instructions or ┊
┊ ┆Item 2 ┆ information to guide the┊
┊ ┆Item 3 ┆ user through this step ┊
┊ ┆Item 4 ┆ of the wizard. ┊
┊ ┆Item 5 ┆  ┊
┊ └╌╌╌╌╌╌╌╌┘  ┊
┊  ┊
┊  ┊
┊  ┊
┊  ┊
┊  ┊
┊  ┊
┊  ┊
┊  ┊
┊  ┊
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘
