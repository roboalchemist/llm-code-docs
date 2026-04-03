# StatusIndicator

# StatusIndicator
Inherits:Node<Object
Application status indicator (aka notification area icon).
Note:Status indicator is implemented on macOS and Windows.

## Properties

| Texture2D | icon |  |
|---|---|---|
| NodePath | menu | NodePath("") |
| String | tooltip | "" |
| bool | visible | true |

Texture2D
icon
NodePath
menu
NodePath("")
String
tooltip
bool
visible
true

## Methods

| Rect2 | get_rect()const |

Rect2
get_rect()const

## Signals
pressed(mouse_button:int, mouse_position:Vector2i)🔗
Emitted when the status indicator is pressed.

## Property Descriptions
Texture2Dicon🔗
- voidset_icon(value:Texture2D)
voidset_icon(value:Texture2D)
- Texture2Dget_icon()
Texture2Dget_icon()
Status indicator icon.
NodePathmenu=NodePath("")🔗
- voidset_menu(value:NodePath)
voidset_menu(value:NodePath)
- NodePathget_menu()
NodePathget_menu()
Status indicator native popup menu. If this is set, thepressedsignal is not emitted.
Note:Native popup is only supported ifNativeMenusupportsNativeMenu.FEATURE_POPUP_MENUfeature.
Stringtooltip=""🔗
- voidset_tooltip(value:String)
voidset_tooltip(value:String)
- Stringget_tooltip()
Stringget_tooltip()
Status indicator tooltip.
boolvisible=true🔗
- voidset_visible(value:bool)
voidset_visible(value:bool)
- boolis_visible()
boolis_visible()
Iftrue, the status indicator is visible.

## Method Descriptions
Rect2get_rect()const🔗
Returns the status indicator rectangle in screen coordinates. If this status indicator is not visible, returns an emptyRect2.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.