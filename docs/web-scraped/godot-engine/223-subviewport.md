# SubViewport

# SubViewport
Inherits:Viewport<Node<Object
An interface to a game world that doesn't create a window or draw to the screen directly.

## Description
SubViewportIsolates a rectangular region of a scene to be displayed independently. This can be used, for example, to display UI in 3D space.
Note:SubViewportis aViewportthat isn't aWindow, i.e. it doesn't draw anything by itself. To display anything,SubViewportmust have a non-zero size and be either put inside aSubViewportContaineror assigned to aViewportTexture.
Note:InputEvents are not passed to a standaloneSubViewportby default. To ensureInputEventpropagation, aSubViewportcan be placed inside of aSubViewportContainer.

## Tutorials
- Using Viewports
Using Viewports
- Viewport and canvas transforms
Viewport and canvas transforms
- GUI in 3D Viewport Demo
GUI in 3D Viewport Demo
- 3D in 2D Viewport Demo
3D in 2D Viewport Demo
- 2D in 3D Viewport Demo
2D in 3D Viewport Demo
- Screen Capture Demo
Screen Capture Demo
- Dynamic Split Screen Demo
Dynamic Split Screen Demo
- 3D Resolution Scaling Demo
3D Resolution Scaling Demo

## Properties

| ClearMode | render_target_clear_mode | 0 |
|---|---|---|
| UpdateMode | render_target_update_mode | 2 |
| Vector2i | size | Vector2i(512,512) |
| Vector2i | size_2d_override | Vector2i(0,0) |
| bool | size_2d_override_stretch | false |

ClearMode
render_target_clear_mode
UpdateMode
render_target_update_mode
Vector2i
size
Vector2i(512,512)
Vector2i
size_2d_override
Vector2i(0,0)
bool
size_2d_override_stretch
false

## Enumerations
enumClearMode:🔗
ClearModeCLEAR_MODE_ALWAYS=0
Always clear the render target before drawing.
ClearModeCLEAR_MODE_NEVER=1
Never clear the render target.
ClearModeCLEAR_MODE_ONCE=2
Clear the render target on the next frame, then switch toCLEAR_MODE_NEVER.
enumUpdateMode:🔗
UpdateModeUPDATE_DISABLED=0
Do not update the render target.
UpdateModeUPDATE_ONCE=1
Update the render target once, then switch toUPDATE_DISABLED.
UpdateModeUPDATE_WHEN_VISIBLE=2
Update the render target only when it is visible. This is the default value.
UpdateModeUPDATE_WHEN_PARENT_VISIBLE=3
Update the render target only when its parent is visible.
UpdateModeUPDATE_ALWAYS=4
Always update the render target.

## Property Descriptions
ClearModerender_target_clear_mode=0🔗
- voidset_clear_mode(value:ClearMode)
voidset_clear_mode(value:ClearMode)
- ClearModeget_clear_mode()
ClearModeget_clear_mode()
The clear mode when the sub-viewport is used as a render target.
Note:This property is intended for 2D usage.
UpdateModerender_target_update_mode=2🔗
- voidset_update_mode(value:UpdateMode)
voidset_update_mode(value:UpdateMode)
- UpdateModeget_update_mode()
UpdateModeget_update_mode()
The update mode when the sub-viewport is used as a render target.
Vector2isize=Vector2i(512,512)🔗
- voidset_size(value:Vector2i)
voidset_size(value:Vector2i)
- Vector2iget_size()
Vector2iget_size()
The width and height of the sub-viewport. Must be set to a value greater than or equal to 2 pixels on both dimensions. Otherwise, nothing will be displayed.
Note:If the parent node is aSubViewportContainerand itsSubViewportContainer.stretchistrue, the viewport size cannot be changed manually.
Vector2isize_2d_override=Vector2i(0,0)🔗
- voidset_size_2d_override(value:Vector2i)
voidset_size_2d_override(value:Vector2i)
- Vector2iget_size_2d_override()
Vector2iget_size_2d_override()
The 2D size override of the sub-viewport. If either the width or height is0, the override is disabled.
boolsize_2d_override_stretch=false🔗
- voidset_size_2d_override_stretch(value:bool)
voidset_size_2d_override_stretch(value:bool)
- boolis_size_2d_override_stretch_enabled()
boolis_size_2d_override_stretch_enabled()
Iftrue, the 2D size override affects stretch as well.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.