# Upgrading from Godot 3 to Godot 4 in English

# Upgrading from Godot 3 to Godot 4

## Should I upgrade to Godot 4?
Before beginning the upgrade process, it's worth thinking about the advantages
and disadvantages that upgrading would bring to your project.

### Advantages of upgrading
Along with thenew features present in 4.0,
upgrading gives the following advantages:
- Many bugs are fixed in 4.0, but cannot be resolved in 3.x for various reasons
(such as graphics API differences or backwards compatibility).
Many bugs are fixed in 4.0, but cannot be resolved in 3.x for various reasons
(such as graphics API differences or backwards compatibility).
- 4.x will enjoy a longersupport period. Godot 3.x
will continue to be supported for some time after 4.0 is released, but it will
eventually stop receiving support.
4.x will enjoy a longersupport period. Godot 3.x
will continue to be supported for some time after 4.0 is released, but it will
eventually stop receiving support.
SeeDocumentation changelogfor a list of pages documenting new features in
Godot 4.0, andList of featuresfor a list of all features in Godot.

### Disadvantages of upgrading
If you don'tneedany features present in Godot 4.x, you may want to stay on
Godot 3.x for the following reasons:
- Godot 4's baseline hardware requirements (such as memory usage) are slightly
higher, both for the editor and exported projects. This was required for the
implementation of some core optimizations.
Godot 4's baseline hardware requirements (such as memory usage) are slightly
higher, both for the editor and exported projects. This was required for the
implementation of some core optimizations.
- Since Godot 4 includes more features than Godot 3, Godot 4's binary size for
exported projects is larger. While this can be mitigated byoptimizing a build for size, a 4.0 build with
a given set of enabled modules will remain larger compared to a 3.x build with
the same modules. This can be an issue forexporting to the Web, as binary size directly
influences how fast the engine can initialize (regardless of download speed).
Since Godot 4 includes more features than Godot 3, Godot 4's binary size for
exported projects is larger. While this can be mitigated byoptimizing a build for size, a 4.0 build with
a given set of enabled modules will remain larger compared to a 3.x build with
the same modules. This can be an issue forexporting to the Web, as binary size directly
influences how fast the engine can initialize (regardless of download speed).
- Godot 4 does not and will not have support for GLES2 rendering.
(There is still support for GLES3 rendering using the new Compatibility renderer,
which means that devices without Vulkan support can still run Godot 4.)If you are targetingveryold hardware such as Intel Sandy Bridge (2nd
generation) integrated graphics, this will prevent the project from running
on such hardware after upgrading.Software OpenGL implementationscan be used to bypass this limitation, but they're too slow for gaming.
Godot 4 does not and will not have support for GLES2 rendering.
(There is still support for GLES3 rendering using the new Compatibility renderer,
which means that devices without Vulkan support can still run Godot 4.)
- If you are targetingveryold hardware such as Intel Sandy Bridge (2nd
generation) integrated graphics, this will prevent the project from running
on such hardware after upgrading.Software OpenGL implementationscan be used to bypass this limitation, but they're too slow for gaming.
If you are targetingveryold hardware such as Intel Sandy Bridge (2nd
generation) integrated graphics, this will prevent the project from running
on such hardware after upgrading.Software OpenGL implementationscan be used to bypass this limitation, but they're too slow for gaming.

### Caveats of upgrading
Since Godot 4 is a complete rewrite in many aspects, some features have
unfortunately been lost in the process.Some of these features may be restored
in future Godot releases:
- Bullet physics was removed in favor of GodotPhysics. This only affects 3D
projects that used the default physics engine (which was Bullet) and didn't
manually change it to GodotPhysics. There are no plans to re-add Bullet physics
in core, but a third-party add-on could be created for it thanks to
GDExtension.
Bullet physics was removed in favor of GodotPhysics. This only affects 3D
projects that used the default physics engine (which was Bullet) and didn't
manually change it to GodotPhysics. There are no plans to re-add Bullet physics
in core, but a third-party add-on could be created for it thanks to
GDExtension.
- By default, rendering in 2D is no longer performed in HDR, which means
"overbright" modulate values have no visible effect. Since Godot 4.2, you can
enable the project settingHDR 2Dto perform 2D rendering in HDR. See alsoUsing glow in 2D.
By default, rendering in 2D is no longer performed in HDR, which means
"overbright" modulate values have no visible effect. Since Godot 4.2, you can
enable the project settingHDR 2Dto perform 2D rendering in HDR. See alsoUsing glow in 2D.
- While rendering still happens in HDR in 3D when using the Forward+ or Mobile
renderers, Viewports cannot return HDR data anymore. This is planned to be
restored at some point in the future.
While rendering still happens in HDR in 3D when using the Forward+ or Mobile
renderers, Viewports cannot return HDR data anymore. This is planned to be
restored at some point in the future.
- Mono was replaced by .NET 6. This means exporting C# projects to Android, iOS
and HTML5 is no longer supported for now. Exporting C# projects to desktop
platforms is still supported, and as of 4.2 there's experimental support for
exporting to mobile platforms. Support for exporting C# projects to more
platforms will be restored in future 4.x releases as upstream support
improves.
Mono was replaced by .NET 6. This means exporting C# projects to Android, iOS
and HTML5 is no longer supported for now. Exporting C# projects to desktop
platforms is still supported, and as of 4.2 there's experimental support for
exporting to mobile platforms. Support for exporting C# projects to more
platforms will be restored in future 4.x releases as upstream support
improves.
You can find a more complete list of functional regressions by searching forissues labeled "regression" but not "bug" on GitHub.

## Preparing before the upgrade (optional)
If you want to be ready to upgrade to Godot 4 in the future, consider usingTweenerand theTimesingleton in your project. These
classes are both available in Godot 3.5 and later.
This way, you won't be relying on the deprecated Tween node and OS time
functions, both of which are removed in Godot 4.0.
It's also a good idea to rename external shaders so that their extension is.gdshaderinstead of.shader. Godot 3.x supports both extensions, but
only.gdshaderis supported in Godot 4.0.

## Running the project upgrade tool
Danger
Make a full backup of your projectbefore upgrading! The project upgrade
tool willnotperform any backups of the project that is being upgraded.
You can backup a project by using version control, or by copying the project
folder to another location.

### Using the Project Manager
To use the project upgrade tool:
- Open the Godot 4 Project Manager.
Open the Godot 4 Project Manager.
- Import the Godot 3.x project using theImportbutton, or use theScanbutton to find the project within a folder.
Import the Godot 3.x project using theImportbutton, or use theScanbutton to find the project within a folder.
- Double-click the imported project (or select the project then chooseEdit).
Double-click the imported project (or select the project then chooseEdit).
- You will see a dialog appearing with two options:Convert project.godot
OnlyandConvert Full Project. After ensuring your project is backed up
(see the above warning), chooseConvert Full Project.Convert
project.godot Onlyis intended to be used for advanced use casesonly, in
case the conversion tool fails.
You will see a dialog appearing with two options:Convert project.godot
OnlyandConvert Full Project. After ensuring your project is backed up
(see the above warning), chooseConvert Full Project.Convert
project.godot Onlyis intended to be used for advanced use casesonly, in
case the conversion tool fails.
- Wait until the project conversion process finishes. This can take up to a few
minutes for large projects with lots of scenes.
Wait until the project conversion process finishes. This can take up to a few
minutes for large projects with lots of scenes.
- When the Project Manager interface becomes available again, double-click the
project (or select the project then chooseEdit) to open it in the
editor.
When the Project Manager interface becomes available again, double-click the
project (or select the project then chooseEdit) to open it in the
editor.
If you hit conversion issues due to some project files being too large or long,
you can use the command line to upgrade the project (see below). This will allow
you to override the converter's size limits.

### Using the command line
To use the project upgrade tool from thecommand line,
it's recommended to validate the project conversion by running the Godot editor binary with the following arguments:
```
# [<max_file_kb>] [<max_line_size>] are optional arguments.
# Remove them if you aren't changing their values.
path/to/godot.binary --path /path/to/project/folder --validate-conversion-3to4 [<max_file_kb>] [<max_line_size>]
```
If the list of planned upgrades looks good to you, run the following command on
the Godot editor binary to upgrade project files:
```
# [<max_file_kb>] [<max_line_size>] are optional arguments.
# Remove them if you aren't changing their values.
path/to/godot.binary --path /path/to/project/folder --convert-3to4 [<max_file_kb>] [<max_line_size>]
```
[<max_file_kb>]and[<max_line_size>]areoptionalarguments to specify
the maximum size of files to be converted (in kilobytes and lines). The default
limits are 4 MB and 100,000 lines respectively. If a file hits either of those
limits, it will not be upgraded by the project converter. This is useful to
prevent large resources from slowing down the upgrade to a crawl.
If you still want large files to be converted by the project upgrade tool,
increase the size limits when running the project upgrade tool. For example,
running the Godot editor binary with those arguments increases both limits by a
10× factor:
```
path/to/godot.binary --path /path/to/project/folder --convert-3to4 40000 1000000
```
Note
Only Godot 3.0 and later projects can be upgraded using the project
conversion tool found in the Godot 4 editor.
It's recommended to ensure that your project is up-to-date with the latest
3.x stable release before running the project upgrade tool.

## Fixing the project after running the project upgrade tool
After upgrading the project, you may notice that certain things don't look as
they should. Scripts will likely contain various errors as well (possibly
hundreds in large projects). This is because the project upgrade tool cannot
cater to all situations. Therefore, a large part of the upgrade process remains
manual.

### Automatically renamed nodes and resources
The list below refers to nodes which were simply renamed for consistency or
clarity in Godot 4.0. The project upgrade tool renames them automatically in
your scripts.
One noteworthy set of renames is 3D nodes, which all got a3Dsuffix added for
consistency with their 2D counterparts. For example,Areais nowArea3D.
For ease of searching, this table lists all nodes and resources that were renamed
and are automatically converted, excluding the ones which only involved adding
a3Dsuffix to the old name:

| Old name (Godot 3.x) | New name (Godot 4) |
|---|---|
| AnimatedSprite | AnimatedSprite2D |
| ARVRCamera | XRCamera3D |
| ARVRController | XRController3D |
| ARVRAnchor | XRAnchor3D |
| ARVRInterface | XRInterface |
| ARVROrigin | XROrigin3D |
| ARVRPositionalTracker | XRPositionalTracker |
| ARVRServer | XRServer |
| BoxShape | BoxShape3D |
| CapsuleShape | CapsuleShape3D |
| CubeMesh | BoxMesh |
| EditorSpatialGizmo | EditorNode3DGizmo |
| EditorSpatialGizmoPlugin | EditorNode3DGizmoPlugin |
| GIProbe | VoxelGI |
| GIProbeData | VoxelGIData |
| GradientTexture | GradientTexture1D |
| KinematicBody | CharacterBody3D |
| KinematicBody2D | CharacterBody2D |
| Light2D | PointLight2D |
| LineShape2D | WorldBoundaryShape2D |
| Listener | AudioListener3D |
| NavigationMeshInstance | NavigationRegion3D |
| NavigationPolygonInstance | NavigationRegion2D |
| Navigation2DServer | NavigationServer2D |
| PanoramaSky | Sky |
| Particles | GPUParticles3D |
| Particles2D | GPUParticles2D |
| ParticlesMaterial | ParticleProcessMaterial |
| Physics2DDirectBodyState | PhysicsDirectBodyState2D |
| Physics2DDirectSpaceState | PhysicsDirectSpaceState2D |
| Physics2DServer | PhysicsServer2D |
| Physics2DShapeQueryParameters | PhysicsShapeQueryParameters2D |
| Physics2DTestMotionResult | PhysicsTestMotionResult2D |
| PlaneShape | WorldBoundaryShape3D |
| Position2D | Marker2D |
| Position3D | Marker3D |
| ProceduralSky | Sky |
| RayShape | SeparationRayShape3D |
| RayShape2D | SeparationRayShape2D |
| ShortCut | Shortcut |
| Spatial | Node3D |
| SpatialGizmo | Node3DGizmo |
| SpatialMaterial | StandardMaterial3D |
| Sprite | Sprite2D |
| StreamTexture | CompressedTexture2D |
| TextureProgress | TextureProgressBar |
| VideoPlayer | VideoStreamPlayer |
| ViewportContainer | SubViewportContainer |
| Viewport | SubViewport |
| VisibilityEnabler | VisibleOnScreenEnabler3D |
| VisibilityNotifier | VisibleOnScreenNotifier3D |
| VisibilityNotifier2D | VisibleOnScreenNotifier2D |
| VisibilityNotifier3D | VisibleOnScreenNotifier3D |
| VisualServer | RenderingServer |
| VisualShaderNodeScalarConstant | VisualShaderNodeFloatConstant |
| VisualShaderNodeScalarFunc | VisualShaderNodeFloatFunc |
| VisualShaderNodeScalarOp | VisualShaderNodeFloatOp |
| VisualShaderNodeScalarClamp | VisualShaderNodeClamp |
| VisualShaderNodeVectorClamp | VisualShaderNodeClamp |
| VisualShaderNodeScalarInterp | VisualShaderNodeMix |
| VisualShaderNodeVectorInterp | VisualShaderNodeMix |
| VisualShaderNodeVectorScalarMix | VisualShaderNodeMix |
| VisualShaderNodeScalarSmoothStep | VisualShaderNodeSmoothStep |
| VisualShaderNodeVectorSmoothStep | VisualShaderNodeSmoothStep |
| VisualShaderNodeVectorScalarSmoothStep | VisualShaderNodeSmoothStep |
| VisualShaderNodeVectorScalarStep | VisualShaderNodeStep |
| VisualShaderNodeScalarSwitch | VisualShaderNodeSwitch |
| VisualShaderNodeScalarTransformMult | VisualShaderNodeTransformOp |
| VisualShaderNodeScalarDerivativeFunc | VisualShaderNodeDerivativeFunc |
| VisualShaderNodeVectorDerivativeFunc | VisualShaderNodeDerivativeFunc |
| VisualShaderNodeBooleanUniform | VisualShaderNodeBooleanParameter |
| VisualShaderNodeColorUniform | VisualShaderNodeColorParameter |
| VisualShaderNodeScalarUniform | VisualShaderNodeFloatParameter |
| VisualShaderNodeCubeMapUniform | VisualShaderNodeCubeMapParameter |
| VisualShaderNodeTextureUniform | VisualShaderNodeTexture2DParameter |
| VisualShaderNodeTextureUniformTriplanar | VisualShaderNodeTextureParameterTriplanar |
| VisualShaderNodeTransformUniform | VisualShaderNodeTransformParameter |
| VisualShaderNodeVec3Uniform | VisualShaderNodeVec3Parameter |
| VisualShaderNodeUniform | VisualShaderNodeParameter |
| VisualShaderNodeUniformRef | VisualShaderNodeParameterRef |

Old name (Godot 3.x)
New name (Godot 4)
AnimatedSprite
AnimatedSprite2D
ARVRCamera
XRCamera3D
ARVRController
XRController3D
ARVRAnchor
XRAnchor3D
ARVRInterface
XRInterface
ARVROrigin
XROrigin3D
ARVRPositionalTracker
XRPositionalTracker
ARVRServer
XRServer
BoxShape
BoxShape3D
CapsuleShape
CapsuleShape3D
CubeMesh
BoxMesh
EditorSpatialGizmo
EditorNode3DGizmo
EditorSpatialGizmoPlugin
EditorNode3DGizmoPlugin
GIProbe
VoxelGI
GIProbeData
VoxelGIData
GradientTexture
GradientTexture1D
KinematicBody
CharacterBody3D
KinematicBody2D
CharacterBody2D
Light2D
PointLight2D
LineShape2D
WorldBoundaryShape2D
Listener
AudioListener3D
NavigationMeshInstance
NavigationRegion3D
NavigationPolygonInstance
NavigationRegion2D
Navigation2DServer
NavigationServer2D
PanoramaSky
Particles
GPUParticles3D
Particles2D
GPUParticles2D
ParticlesMaterial
ParticleProcessMaterial
Physics2DDirectBodyState
PhysicsDirectBodyState2D
Physics2DDirectSpaceState
PhysicsDirectSpaceState2D
Physics2DServer
PhysicsServer2D
Physics2DShapeQueryParameters
PhysicsShapeQueryParameters2D
Physics2DTestMotionResult
PhysicsTestMotionResult2D
PlaneShape
WorldBoundaryShape3D
Position2D
Marker2D
Position3D
Marker3D
ProceduralSky
RayShape
SeparationRayShape3D
RayShape2D
SeparationRayShape2D
ShortCut
Shortcut
Spatial
Node3D
SpatialGizmo
Node3DGizmo
SpatialMaterial
StandardMaterial3D
Sprite
Sprite2D
StreamTexture
CompressedTexture2D
TextureProgress
TextureProgressBar
VideoPlayer
VideoStreamPlayer
ViewportContainer
SubViewportContainer
Viewport
SubViewport
VisibilityEnabler
VisibleOnScreenEnabler3D
VisibilityNotifier
VisibleOnScreenNotifier3D
VisibilityNotifier2D
VisibleOnScreenNotifier2D
VisibilityNotifier3D
VisibleOnScreenNotifier3D
VisualServer
RenderingServer
VisualShaderNodeScalarConstant
VisualShaderNodeFloatConstant
VisualShaderNodeScalarFunc
VisualShaderNodeFloatFunc
VisualShaderNodeScalarOp
VisualShaderNodeFloatOp
VisualShaderNodeScalarClamp
VisualShaderNodeClamp
VisualShaderNodeVectorClamp
VisualShaderNodeClamp
VisualShaderNodeScalarInterp
VisualShaderNodeMix
VisualShaderNodeVectorInterp
VisualShaderNodeMix
VisualShaderNodeVectorScalarMix
VisualShaderNodeMix
VisualShaderNodeScalarSmoothStep
VisualShaderNodeSmoothStep
VisualShaderNodeVectorSmoothStep
VisualShaderNodeSmoothStep
VisualShaderNodeVectorScalarSmoothStep
VisualShaderNodeSmoothStep
VisualShaderNodeVectorScalarStep
VisualShaderNodeStep
VisualShaderNodeScalarSwitch
VisualShaderNodeSwitch
VisualShaderNodeScalarTransformMult
VisualShaderNodeTransformOp
VisualShaderNodeScalarDerivativeFunc
VisualShaderNodeDerivativeFunc
VisualShaderNodeVectorDerivativeFunc
VisualShaderNodeDerivativeFunc
VisualShaderNodeBooleanUniform
VisualShaderNodeBooleanParameter
VisualShaderNodeColorUniform
VisualShaderNodeColorParameter
VisualShaderNodeScalarUniform
VisualShaderNodeFloatParameter
VisualShaderNodeCubeMapUniform
VisualShaderNodeCubeMapParameter
VisualShaderNodeTextureUniform
VisualShaderNodeTexture2DParameter
VisualShaderNodeTextureUniformTriplanar
VisualShaderNodeTextureParameterTriplanar
VisualShaderNodeTransformUniform
VisualShaderNodeTransformParameter
VisualShaderNodeVec3Uniform
VisualShaderNodeVec3Parameter
VisualShaderNodeUniform
VisualShaderNodeParameter
VisualShaderNodeUniformRef
VisualShaderNodeParameterRef

### Manually renaming methods, properties, signals and constants
Due to how the project upgrade tool works, not allAPIrenames can be performed automatically.
The list below contains all renames that must be performed manually using the script editor.
If you cannot find a node or resource in the list below, refer to the above
table to find its new name.
You can use theReplace in Filesdialog to speed up replacement by pressingCtrl+Shift+Rwhile the script editor is open. However, be careful
as the Replace in Files dialog doesn't offer any way to undo a replacement.
Use version control to commit your upgrade work regularly.
Command line tools such assdcan also be used
if you need something more flexible than the editor's Replace in Files dialog.
If using C#, remember to search for outdated API usage with PascalCase
notation in the project (and perform the replacement with PascalCase
notation).
Methods
- File and Directory classes were replaced byFileAccessandDirAccess, which have an entirely different API. Several methods
are now static, which means you can call them directly on FileAccess or
DirAccess without having to create an instance of that class.
File and Directory classes were replaced byFileAccessandDirAccess, which have an entirely different API. Several methods
are now static, which means you can call them directly on FileAccess or
DirAccess without having to create an instance of that class.
- Screen and window-related methods from theOSsingleton (such asOS.get_screen_size()) were moved to theDisplayServersingleton.
Method naming was also changed to use theDisplayServer.<object>_<get/set>_property()form instead. For example,OS.get_screen_size()becomesDisplayServer.screen_get_size().
Screen and window-related methods from theOSsingleton (such asOS.get_screen_size()) were moved to theDisplayServersingleton.
Method naming was also changed to use theDisplayServer.<object>_<get/set>_property()form instead. For example,OS.get_screen_size()becomesDisplayServer.screen_get_size().
- Time and date methods from theOSsingleton were moved to theTimesingleton.
(The Time singleton is also available in Godot 3.5 and later.)
Time and date methods from theOSsingleton were moved to theTimesingleton.
(The Time singleton is also available in Godot 3.5 and later.)
- You may have to replace someinstance()calls withinstantiate(). The
convertershouldhandle this automatically, but this relies on custom code that
may not work in 100% of situations.
You may have to replace someinstance()calls withinstantiate(). The
convertershouldhandle this automatically, but this relies on custom code that
may not work in 100% of situations.
- AcceptDialog'sset_autowrap()is nowset_autowrap_mode().
AcceptDialog'sset_autowrap()is nowset_autowrap_mode().
- AnimationNode'sprocess()is now_process()(note the leading underscore, which denotes a virtual method).
AnimationNode'sprocess()is now_process()(note the leading underscore, which denotes a virtual method).
- AnimationPlayer'sadd_animation()is nowadd_animation_library()and now uses anAnimationLibrary.
AnimationPlayer'sadd_animation()is nowadd_animation_library()and now uses anAnimationLibrary.
- AnimationTree'sset_process_mode()is nowset_process_callback().
AnimationTree'sset_process_mode()is nowset_process_callback().
- Array'sempty()is nowis_empty().
Array'sempty()is nowis_empty().
- Array'sinvert()is nowreverse().
Array'sinvert()is nowreverse().
- Array'sremove()is nowremove_at().
Array'sremove()is nowremove_at().
- AStar2D and AStar3D'sget_points()is nowget_points_id().
AStar2D and AStar3D'sget_points()is nowget_points_id().
- BaseButton'sset_event()is nowset_shortcut().
BaseButton'sset_event()is nowset_shortcut().
- Camera2D'sget_h_offset()is nowget_drag_horizontal_offset().
Camera2D'sget_h_offset()is nowget_drag_horizontal_offset().
- Camera2D'sget_v_offset()is nowget_drag_vertical_offset().
Camera2D'sget_v_offset()is nowget_drag_vertical_offset().
- Camera2D'sset_h_offset()is nowset_drag_horizontal_offset().
Camera2D'sset_h_offset()is nowset_drag_horizontal_offset().
- Camera2D'sset_v_offset()is nowset_drag_vertical_offset().
Camera2D'sset_v_offset()is nowset_drag_vertical_offset().
- CanvasItem'sraise()is nowmove_to_front().
CanvasItem'sraise()is nowmove_to_front().
- CanvasItem'supdate()is nowqueue_redraw().
CanvasItem'supdate()is nowqueue_redraw().
- Control'sget_stylebox()is nowget_theme_stylebox().
Control'sget_stylebox()is nowget_theme_stylebox().
- Control'sset_tooltip()is nowset_tooltip_text().
Control'sset_tooltip()is nowset_tooltip_text().
- EditorNode3DGizmoPlugin'screate_gizmo()is now_create_gizmo()(note the leading underscore, which denotes a virtual method).
EditorNode3DGizmoPlugin'screate_gizmo()is now_create_gizmo()(note the leading underscore, which denotes a virtual method).
- ENetMultiplayerPeer'sget_peer_port()is nowget_peer().
ENetMultiplayerPeer'sget_peer_port()is nowget_peer().
- FileDialog'sget_mode()is nowget_file_mode().
FileDialog'sget_mode()is nowget_file_mode().
- FileDialog'sset_mode()is nowset_file_mode().
FileDialog'sset_mode()is nowset_file_mode().
- GraphNode'sget_offset()is nowget_position_offset().
GraphNode'sget_offset()is nowget_position_offset().
- GridMap'smap_to_world()is nowmap_to_local().
GridMap'smap_to_world()is nowmap_to_local().
- GridMap'sworld_to_map()is nowlocal_to_map().
GridMap'sworld_to_map()is nowlocal_to_map().
- Image'sget_rect()is nowget_region().
Image'sget_rect()is nowget_region().
- ImmediateGeometry'sset_normal()is nowsurface_set_normal().
ImmediateGeometry'sset_normal()is nowsurface_set_normal().
- ImmediateMesh'sset_color()is nowsurface_set_color().
ImmediateMesh'sset_color()is nowsurface_set_color().
- ImmediateMesh'sset_uv()is nowsurface_set_uv().
ImmediateMesh'sset_uv()is nowsurface_set_uv().
- ItemList'sget_v_scroll()is nowget_v_scroll_bar().
ItemList'sget_v_scroll()is nowget_v_scroll_bar().
- MultiPlayerAPI'sget_network_connected_peers()is nowget_peers().
MultiPlayerAPI'sget_network_connected_peers()is nowget_peers().
- MultiPlayerAPI'sget_network_peer()is nowget_peer().
MultiPlayerAPI'sget_network_peer()is nowget_peer().
- MultiPlayerAPI'sget_network_unique_id()is nowget_unique_id().
MultiPlayerAPI'sget_network_unique_id()is nowget_unique_id().
- MultiPlayerAPI'shas_network_peer()is nowhas_multiplayer_peer().
MultiPlayerAPI'shas_network_peer()is nowhas_multiplayer_peer().
- MultiplayerAPI'sis_refusing_new_network_connections()is nowis_refusing_new_connections().
MultiplayerAPI'sis_refusing_new_network_connections()is nowis_refusing_new_connections().
- PacketPeerUDP'sis_listening()is nowis_bound().
PacketPeerUDP'sis_listening()is nowis_bound().
- PacketPeerUDP'slisten()is nowbind().
PacketPeerUDP'slisten()is nowbind().
- ParticleProcessMaterial'sset_flag()is nowset_particle_flag().
ParticleProcessMaterial'sset_flag()is nowset_particle_flag().
- PhysicsTestMotionResult2D'sget_motion()is nowget_travel().
PhysicsTestMotionResult2D'sget_motion()is nowget_travel().
- RenderingServer'sget_render_info()is nowget_rendering_info().
RenderingServer'sget_render_info()is nowget_rendering_info().
- ResourceFormatLoader'sget_dependencies()is now_get_dependencies()(note the leading underscore, which denotes a virtual method).
ResourceFormatLoader'sget_dependencies()is now_get_dependencies()(note the leading underscore, which denotes a virtual method).
- ResourceFormatLoader'sload()is now_load().
ResourceFormatLoader'sload()is now_load().
- SceneTree'schange_scene()is nowchange_scene_to_file().
SceneTree'schange_scene()is nowchange_scene_to_file().
- Shortcut'sis_valid()is nowhas_valid_event().
Shortcut'sis_valid()is nowhas_valid_event().
- TileMap'smap_to_world()is nowmap_to_local().
TileMap'smap_to_world()is nowmap_to_local().
- TileMap'sworld_to_map()is nowlocal_to_map().
TileMap'sworld_to_map()is nowlocal_to_map().
- Transform2D'sxform()ismat*vecandxform_inv()isvec*mat.
Transform2D'sxform()ismat*vecandxform_inv()isvec*mat.
- XRPositionalTracker'sget_name()is nowget_tracker_name().
XRPositionalTracker'sget_name()is nowget_tracker_name().
- XRPositionalTracker'sget_type()is nowget_tracker_type().
XRPositionalTracker'sget_type()is nowget_tracker_type().
- XRPositionalTracker's_set_name()is nowget_tracker_name().
XRPositionalTracker's_set_name()is nowget_tracker_name().
Properties
Note
If a property is listed here, its associated getter and setter methods must
also be renamed manually if used in the project. For example, PathFollow2D
and PathFollow3D'sset_offset()andget_offset()must be renamed toset_progress()andget_progress()respectively.
- AudioServer'sdeviceis nowoutput_device.
AudioServer'sdeviceis nowoutput_device.
- BaseButton'sgroupis nowbutton_group.
BaseButton'sgroupis nowbutton_group.
- Camera3D'szfaris nowfar.
Camera3D'szfaris nowfar.
- Camera3D'sznearis nownear
Camera3D'sznearis nownear
- Control'smarginis nowoffset.
Control'smarginis nowoffset.
- InputEventMouseButton'sdoubleclickis nowdouble_click.
InputEventMouseButton'sdoubleclickis nowdouble_click.
- InputEventWithModifiers'saltis nowalt_pressed.
InputEventWithModifiers'saltis nowalt_pressed.
- InputEventWithModifiers'scommandis nowcommand_pressed.
InputEventWithModifiers'scommandis nowcommand_pressed.
- InputEventWithModifiers'scontrolis nowctrl_pressed.
InputEventWithModifiers'scontrolis nowctrl_pressed.
- InputEventWithModifiers'smetais nowmeta_pressed.
InputEventWithModifiers'smetais nowmeta_pressed.
- InputEventWithModifiers'sshiftis nowshift_pressed.
InputEventWithModifiers'sshiftis nowshift_pressed.
- Label'spercent_visibleis nowvisible_ratio.
Label'spercent_visibleis nowvisible_ratio.
- MultiPlayerAPI'srefuse_new_network_connectionsis nowrefuse_new_connections.
MultiPlayerAPI'srefuse_new_network_connectionsis nowrefuse_new_connections.
- Node'sfilenameis nowscene_file_path.
Node'sfilenameis nowscene_file_path.
- PathFollow2D'srotateis nowrotates.
PathFollow2D'srotateis nowrotates.
- PathFollow2D and PathFollow3D'soffsetis nowprogress.
PathFollow2D and PathFollow3D'soffsetis nowprogress.
- RectangleShape2D'sextentsis nowsize
RectangleShape2D'sextentsis nowsize
- TextureProgressBar'spercent_visibleis nowshow_percentage.
TextureProgressBar'spercent_visibleis nowshow_percentage.
- Theme'soffis nowunchecked.
Theme'soffis nowunchecked.
- Theme'sofsis nowoffset.
Theme'sofsis nowoffset.
- Theme'sonis nowchecked.
Theme'sonis nowchecked.
- Window'swindow_titleis nowtitle.
Window'swindow_titleis nowtitle.
- WorldMarginShape2D'sdis nowdistance.
WorldMarginShape2D'sdis nowdistance.
- Theextentsproperty on CSG nodes and VoxelGI will have to be replaced
withsize, with the set value halved (as they're no longer half-extents).
This also affects its setter/getter methodsset_extents()andget_extents().
Theextentsproperty on CSG nodes and VoxelGI will have to be replaced
withsize, with the set value halved (as they're no longer half-extents).
This also affects its setter/getter methodsset_extents()andget_extents().
- TheEngine.editor_hintproperty was removed in favor of theEngine.is_editor_hint()method. This is because it's read-only, and
properties in Godot are not used for read-only values.
TheEngine.editor_hintproperty was removed in favor of theEngine.is_editor_hint()method. This is because it's read-only, and
properties in Godot are not used for read-only values.
Enums
- CPUParticles2D'sFLAG_MAXis nowPARTICLE_FLAG_MAX.
CPUParticles2D'sFLAG_MAXis nowPARTICLE_FLAG_MAX.
Signals
- FileSystemDock'sinstantiateis nowinstance.
FileSystemDock'sinstantiateis nowinstance.
- CanvasItem'shideis nowhidden. This rename doesnotapply to thehide()method, only the signal.
CanvasItem'shideis nowhidden. This rename doesnotapply to thehide()method, only the signal.
- Tween'stween_all_completedis nowloop_finished.
Tween'stween_all_completedis nowloop_finished.
- EditorSettings'changedis nowsettings_changed.
EditorSettings'changedis nowsettings_changed.
Constants
- Color names are now uppercase and use underscores between words.
For example,Color.palegreenis nowColor.PALE_GREEN.
Color names are now uppercase and use underscores between words.
For example,Color.palegreenis nowColor.PALE_GREEN.
- MainLoop'sNOTIFICATION_constants were duplicated toNodewhich means
you can remove theMainLoop.prefix when referencing them.
MainLoop'sNOTIFICATION_constants were duplicated toNodewhich means
you can remove theMainLoop.prefix when referencing them.
- MainLoop'sNOTIFICATION_WM_QUIT_REQUESTis nowNOTIFICATION_WM_CLOSE_REQUEST.
MainLoop'sNOTIFICATION_WM_QUIT_REQUESTis nowNOTIFICATION_WM_CLOSE_REQUEST.

### Checking project settings
Several project settings were renamed, and some of them had their enums changed
in incompatible ways (such as shadow filter quality). This means you may need to
set some project settings' values again. Make sure theAdvancedtoggle is
enabled in the project settings dialog so you can see all project settings.

### Checking Environment settings
Graphics quality settings were moved from Environment properties to project
settings. This was done to make runtime quality adjustments easier, without
having to access the currently active Environment resource then modify its
properties.
As a result, you will have to configure Environment quality settings in the
project settings as old Environment quality settings aren't converted
automatically to project settings.
If you have a graphics settings menu that changed environment properties in
Godot 3.x, you will have to change its code to callRenderingServermethods that affect environment effects' quality. Only the "base" toggle of each
environment effect and its visual knobs remain within the Environment resource.

### Updating shaders
There have been some changes to shaders that aren't covered by the upgrade tool.
You will need to make some manual changes, especially if your shader uses coordinate
space transformations or a customlight()function.
The.shaderfile extension is no longer supported, which means you must
rename.shaderfiles to.gdshaderand update references accordingly in
scene/resource files using an external text editor.
Some notable changes you will need to perform in shaders are:
- Texture filter and repeat modes are now set on individual uniforms, rather
than the texture files themselves.
Texture filter and repeat modes are now set on individual uniforms, rather
than the texture files themselves.
- hint_albedois nowsource_color.
hint_albedois nowsource_color.
- hint_coloris nowsource_color.
hint_coloris nowsource_color.
- Built in matrix variables were renamed.
Built in matrix variables were renamed.
- Particles shaders no longer use thevertex()processor function. Instead
they usestart()andprocess().
Particles shaders no longer use thevertex()processor function. Instead
they usestart()andprocess().
- In the Forward+ and Mobile renderers, normalized device coordinates now have a Z-range of[0.0,1.0]instead of[-1.0,1.0]. When reconstructing NDC fromSCREEN_UVand depth, usevec3ndc=vec3(SCREEN_UV*2.0-1.0,depth);instead ofvec3ndc=vec3(SCREEN_UV,depth)*2.0-1.0;. The Compatibility renderer is unchanged,
using the same NDC Z-range as 3.x.
In the Forward+ and Mobile renderers, normalized device coordinates now have a Z-range of[0.0,1.0]instead of[-1.0,1.0]. When reconstructing NDC fromSCREEN_UVand depth, usevec3ndc=vec3(SCREEN_UV*2.0-1.0,depth);instead ofvec3ndc=vec3(SCREEN_UV,depth)*2.0-1.0;. The Compatibility renderer is unchanged,
using the same NDC Z-range as 3.x.
- The lighting model changed. If your shader has a customlight()function,
you may need to make changes to get the same visual result.
The lighting model changed. If your shader has a customlight()function,
you may need to make changes to get the same visual result.
- In 4.3 and up, the reverse Z depth buffer technique is now implemented, which
may break advanced shaders. SeeIntroducing Reverse Z (AKA I'm sorry for breaking your shader).
In 4.3 and up, the reverse Z depth buffer technique is now implemented, which
may break advanced shaders. SeeIntroducing Reverse Z (AKA I'm sorry for breaking your shader).
SeeShading languagefor more information.
This list is not exhaustive. If you made all the changes mentioned here and your
shader still doesn't work, try asking for help in one of thecommunity channels.

### Updating scripts to take backwards-incompatible changes into account
Some changes performed between Godot 3.x and 4 are not renames, but they still
break backwards compatibility due to different default behavior.
The most notable examples of this are:
- Lifecycle functions such as_ready()and_process()no longer
implicitly call parent classes' functions that have the same name. Instead,
you must usesuper()at the top of a lifecycle function in the child class
so that the parent class function is called first.
Lifecycle functions such as_ready()and_process()no longer
implicitly call parent classes' functions that have the same name. Instead,
you must usesuper()at the top of a lifecycle function in the child class
so that the parent class function is called first.
- BothStringandStringNameare now exposed to
GDScript. This allows for greater optimization, as StringName is specifically
designed to be used for "constant" strings that are created once and reused
many times. These types are not strictly equivalent to each other, which meansis_same("example",&"example")returnsfalse. Although in most cases
they are interchangeable ("example"==&"example"returnstrue),
sometimes you may have to replace"example"with&"example".
BothStringandStringNameare now exposed to
GDScript. This allows for greater optimization, as StringName is specifically
designed to be used for "constant" strings that are created once and reused
many times. These types are not strictly equivalent to each other, which meansis_same("example",&"example")returnsfalse. Although in most cases
they are interchangeable ("example"==&"example"returnstrue),
sometimes you may have to replace"example"with&"example".
- GDScript setter and getter syntaxwas changed, but it's only partially converted by the conversion tool. In most
cases, manual changes are required to make setters and getters working again.
GDScript setter and getter syntaxwas changed, but it's only partially converted by the conversion tool. In most
cases, manual changes are required to make setters and getters working again.
- GDScript signal connection syntaxwas changed.
The conversion tool will use the string-based syntax which is still present in
Godot 4, but it's recommended to switch to theSignal-based syntax
described on the linked page. This way, strings are no longer involved,
which avoids issues with signal name errors that can only be discovered at runtime.
GDScript signal connection syntaxwas changed.
The conversion tool will use the string-based syntax which is still present in
Godot 4, but it's recommended to switch to theSignal-based syntax
described on the linked page. This way, strings are no longer involved,
which avoids issues with signal name errors that can only be discovered at runtime.
- Built-in scripts that aretool scriptsdo not get thetoolkeyword converted to the@toolannotation.
Built-in scripts that aretool scriptsdo not get thetoolkeyword converted to the@toolannotation.
- The Tween node was removed in favor of Tweeners, which are also available in
Godot 3.5 and later. See theoriginal pull requestfor details.
The Tween node was removed in favor of Tweeners, which are also available in
Godot 3.5 and later. See theoriginal pull requestfor details.
- randomize()is now automatically called on project load, so deterministic
randomness with the global RandomNumberGenerate instance requires manually
setting a seed in a script's_ready()function.
randomize()is now automatically called on project load, so deterministic
randomness with the global RandomNumberGenerate instance requires manually
setting a seed in a script's_ready()function.
- call_group(),set_group()andnotify_group()are now immediate by
default. If calling an expensive function, this may result in stuttering when
used on a group containing a large number of nodes. To use deferred calls like
before, replacecall_group(...)withcall_group_flags(SceneTree.GROUP_CALL_DEFERRED,...)(and do the same withset_group()andnotify_group()respectively).
call_group(),set_group()andnotify_group()are now immediate by
default. If calling an expensive function, this may result in stuttering when
used on a group containing a large number of nodes. To use deferred calls like
before, replacecall_group(...)withcall_group_flags(SceneTree.GROUP_CALL_DEFERRED,...)(and do the same withset_group()andnotify_group()respectively).
- Instead ofrotation_degrees, therotationproperty is exposed to the
editor, which is automatically displayed as degrees in the Inspector
dock. This may break animations, as the conversion is not handled automatically by the
conversion tool.
Instead ofrotation_degrees, therotationproperty is exposed to the
editor, which is automatically displayed as degrees in the Inspector
dock. This may break animations, as the conversion is not handled automatically by the
conversion tool.
- AABB'shas_no_surface()was inverted and renamed tohas_surface().
AABB'shas_no_surface()was inverted and renamed tohas_surface().
- AABBandRect2'shas_no_area()was inverted and
renamed tohas_area().
AABBandRect2'shas_no_area()was inverted and
renamed tohas_area().
- AnimatedTexture'sfpsproperty was replaced byspeed_scale,
which works the same as AnimationPlayer'splayback_speedproperty.
AnimatedTexture'sfpsproperty was replaced byspeed_scale,
which works the same as AnimationPlayer'splayback_speedproperty.
- AnimatedSprite2DandAnimatedSprite3Dnow allow
negativespeed_scalevalues. This may break animations if you relied onspeed_scalebeing internally clamped to0.0.
AnimatedSprite2DandAnimatedSprite3Dnow allow
negativespeed_scalevalues. This may break animations if you relied onspeed_scalebeing internally clamped to0.0.
- AnimatedSprite2DandAnimatedSprite3D'splayingproperty was removed. Useplay()/stop()method instead OR configureautoplayanimation via the SpriteFrames bottom panel (but not both at once).
AnimatedSprite2DandAnimatedSprite3D'splayingproperty was removed. Useplay()/stop()method instead OR configureautoplayanimation via the SpriteFrames bottom panel (but not both at once).
- Array'sslice()second parameter (end) is nowexclusive,
instead of being inclusive. For example, this means that[1,2,3].slice(0,1)now returns[1]instead of[1,2].
Array'sslice()second parameter (end) is nowexclusive,
instead of being inclusive. For example, this means that[1,2,3].slice(0,1)now returns[1]instead of[1,2].
- BaseButton's signals are nowbutton_upandbutton_down.
Thepressedproperty is nowbutton_pressed.
BaseButton's signals are nowbutton_upandbutton_down.
Thepressedproperty is nowbutton_pressed.
- Camera2D'srotatingproperty was replaced byignore_rotation, which has inverted behavior.
Camera2D'srotatingproperty was replaced byignore_rotation, which has inverted behavior.
- Camera2D'szoomproperty was inverted: higher values are now more zoomed
in, instead of less.
Camera2D'szoomproperty was inverted: higher values are now more zoomed
in, instead of less.
- Node'sremove_and_skip()method was removed.
If you need to reimplement it in a script, you can use theold C++ implementationas a reference.
Node'sremove_and_skip()method was removed.
If you need to reimplement it in a script, you can use theold C++ implementationas a reference.
- OS.get_system_time_secs()should be converted toTime.get_time_dict_from_system()["second"].
OS.get_system_time_secs()should be converted toTime.get_time_dict_from_system()["second"].
- ResourceSaver'ssave()method now has its arguments swapped around
(resource:Resource,path:String). This also applies toResourceFormatSaver's_save()method.
ResourceSaver'ssave()method now has its arguments swapped around
(resource:Resource,path:String). This also applies toResourceFormatSaver's_save()method.
- AStreamPeerTCPmust havepoll()called on it to update its
state, instead of relying onget_status()automatically polling:GH-59582
AStreamPeerTCPmust havepoll()called on it to update its
state, instead of relying onget_status()automatically polling:GH-59582
- String'sright()methodhas changed behavior:
it now returns a number of characters from the right of the string, rather than
the right side of the string from a given position. If you need the old behavior,
you can usesubstr()instead.
String'sright()methodhas changed behavior:
it now returns a number of characters from the right of the string, rather than
the right side of the string from a given position. If you need the old behavior,
you can usesubstr()instead.
- is_connected_to_host()was removed from StreamPeerTCP and PacketPeerUDP as
perGH-59582.get_status()can be used in StreamPeerTCP instead.is_socket_connected()can be used inPacketPeerUDPinstead.
is_connected_to_host()was removed from StreamPeerTCP and PacketPeerUDP as
perGH-59582.get_status()can be used in StreamPeerTCP instead.is_socket_connected()can be used inPacketPeerUDPinstead.
- In_get_property_list(), theor_lesserproperty hint string is nowor_less.
In_get_property_list(), theor_lesserproperty hint string is nowor_less.
- In_get_property_list(), thenosliderproperty hint string is nowno_slider.
In_get_property_list(), thenosliderproperty hint string is nowno_slider.
- VisualShaderNodeVec4Parameter now takes aVector4as parameter
instead of aQuaternion.
VisualShaderNodeVec4Parameter now takes aVector4as parameter
instead of aQuaternion.
Removed or replaced nodes/resources
This lists all nodes that were replaced by another node requiring different
configuration. The setup must be done from scratch again, as the project
converter doesn't support updating existing setups:

| Removed node | Closest approximation | Comment |
|---|---|---|
| AnimationTreePlayer | AnimationTree | AnimationTreePlayer was deprecated since Godot 3.1. |
| BakedLightmap | LightmapGI | SeeUsing Lightmap global illumination. |
| BakedLightmapData | LightmapGIData |
| BitmapFont | FontFile | SeeUsing Fonts. |
| DynamicFont | FontFile |
| DynamicFontData | FontFile |
| ClippedCamera | Camera2D or Camera3D | Camera's pyramid shape was moved to :ref:'class_Camera3D'. |
| InterpolatedCamera | Camera2D or Camera3D |
| Navigation2D | Node2D | Replaced byother 2D Navigation nodes. |
| Navigation3D | Node3D | Replaced byother 3D Navigation nodes. |
| OpenSimplexNoise | FastNoiseLite | Has different parameters and more noise types such as cellular. No
support for 4D noise as it's absent from the FastNoiseLite library. |
| ToolButton | Button | ToolButton was Button with theFlatproperty enabled by default. |
| YSort | Node2D or Control | CanvasItem has a newY Sort Enabledproperty in 4.0. |
| ProximityGroup | Node3D | VisibleOnScreenNotifier3Dcan act as a replacement. |
| Portal | Node3D | Portal and room occlusion culling was replaced by rasterocclusion culling(OccluderInstance3D node), which requires a different setup process. |
| Room | Node3D |
| RoomManager | Node3D |
| RoomGroup | Node3D |
| Occluder | Node3D | Geometry occlusion culling was replaced by rasterocclusion culling(OccluderInstance3D node), which requires a different setup process. |
| OccluderShapeSphere | Resource |

Removed node
Closest approximation
Comment
AnimationTreePlayer
AnimationTree
AnimationTreePlayer was deprecated since Godot 3.1.
BakedLightmap
LightmapGI
SeeUsing Lightmap global illumination.
BakedLightmapData
LightmapGIData
BitmapFont
FontFile
SeeUsing Fonts.
DynamicFont
FontFile
DynamicFontData
FontFile
ClippedCamera
Camera2D or Camera3D
Camera's pyramid shape was moved to :ref:'class_Camera3D'.
InterpolatedCamera
Camera2D or Camera3D
Navigation2D
Node2D
Replaced byother 2D Navigation nodes.
Navigation3D
Node3D
Replaced byother 3D Navigation nodes.
OpenSimplexNoise
FastNoiseLite
Has different parameters and more noise types such as cellular. No
support for 4D noise as it's absent from the FastNoiseLite library.
ToolButton
Button
ToolButton was Button with theFlatproperty enabled by default.
YSort
Node2D or Control
CanvasItem has a newY Sort Enabledproperty in 4.0.
ProximityGroup
Node3D
VisibleOnScreenNotifier3Dcan act as a replacement.
Portal
Node3D
Portal and room occlusion culling was replaced by rasterocclusion culling(OccluderInstance3D node), which requires a different setup process.
Room
Node3D
RoomManager
Node3D
RoomGroup
Node3D
Occluder
Node3D
Geometry occlusion culling was replaced by rasterocclusion culling(OccluderInstance3D node), which requires a different setup process.
OccluderShapeSphere
Resource
If loading an old project, the node will be replaced with itsClosest approximationautomatically (even if not using the project upgrade tool).
Threading changes
ThreadingAPIs have changed in 4.0. For
example, the following code snippet in Godot 3.x must be modified to work in 4.0:
```
# 3.x
var start_success = new_thread.start(self, "__threaded_background_loader",
    [resource_path, thread_num]
)

# 4.0
var start_success = new_thread.start(__threaded_background_loader.bind(resource_path, thread_num))
```
Thread.is_active()is no longer used and should be converted toThread.is_alive().
See also
See thechangelogfor a full list of changes between Godot 3.x and 4.

### ArrayMesh resource compatibility breakage
If you've saved an ArrayMesh resource to a.resor.tresfile, the
format used in 4.0 is not compatible with the one used in 3.x. You will need to
go through the process of importing the source mesh file and saving it as an
ArrayMesh resource again.

## List of automatically renamed methods, properties, signals and constants
Theeditor/renames_map_3_to_4.cppsource file lists all automatic renames performed by the project upgrade tool.
Lines that are commented out refer to API renames thatcannot be performed automatically.

## Porting editor settings
Godot 3.x and 4.0 use different editor settings files. This means their settings
can be changed independently from each other.
If you wish to port over your Godot 3.x settings to Godot 4, open theeditor settings folderand copyeditor_settings-3.trestoeditor_settings-4.treswhile the Godot 4
editor is closed.
Note
Many settings' names and categories have changed since Godot 3.x. Editor settings
whose name or category has changed won't carry over to Godot 4.0; you will
have to set their values again.

## Updating version control settings
Godot 3.x and 4.x have entirely different lists of files and folders that should
be ignored by yourversion control system.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.