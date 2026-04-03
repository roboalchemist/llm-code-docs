# Spatial shaders in English

# Spatial shaders
Spatial shaders are used for shading 3D objects. They are the most complex type of shader Godot offers.
Spatial shaders are highly configurable with different render modes and different rendering options
(e.g. Subsurface Scattering, Transmission, Ambient Occlusion, Rim lighting, etc.). Users can optionally
write vertex, fragment, and light processor functions to affect how objects are drawn.

## Render modes
For visual examples of these render modes, seeStandard Material 3D and ORM Material 3D.

| Render mode | Description |
|---|---|
| blend_mix | Mix blend mode (alpha is transparency), default. |
| blend_add | Additive blend mode. |
| blend_sub | Subtractive blend mode. |
| blend_mul | Multiplicative blend mode. |
| blend_premul_alpha | Premultiplied alpha blend mode (fully transparent = add, fully opaque = mix). |
| depth_draw_opaque | Only draw depth for opaque geometry (not transparent). |
| depth_draw_always | Always draw depth (opaque and transparent). |
| depth_draw_never | Never draw depth. |
| depth_prepass_alpha | Do opaque depth pre-pass for transparent geometry. |
| depth_test_disabled | Disable depth testing. |
| depth_test_default | Depth test will discard the pixel if it is behind other pixels.
In Forward+ only, the pixel is also discarded if it's at the exact same depth as another pixel. |
| depth_test_inverted | Depth test will discard the pixel if it is in front of other pixels. Useful for stencil effects. |
| sss_mode_skin | Subsurface Scattering mode for skin (optimizes visuals for human skin, e.g. boosted red channel). |
| cull_back | Cull back-faces (default). |
| cull_front | Cull front-faces. |
| cull_disabled | Culling disabled (double sided). |
| unshaded | Result is just albedo. No lighting/shading happens in material, making it faster to render. |
| wireframe | Geometry draws using lines (useful for troubleshooting). |
| debug_shadow_splits | Directional shadows are drawn using different colors for each split (useful for troubleshooting). |
| diffuse_burley | Burley (Disney PBS) for diffuse (default). |
| diffuse_lambert | Lambert shading for diffuse. |
| diffuse_lambert_wrap | Lambert-wrap shading (roughness-dependent) for diffuse. |
| diffuse_toon | Toon shading for diffuse. |
| specular_schlick_ggx | Schlick-GGX for direct light specular lobes (default). |
| specular_toon | Toon for direct light specular lobes. |
| specular_disabled | Disable direct light specular lobes. Doesn't affect reflected light (useSPECULAR=0.0instead). |
| skip_vertex_transform | VERTEX,NORMAL,TANGENT, andBITANGENTneed to be transformed manually in thevertex()function. |
| world_vertex_coords | VERTEX,NORMAL,TANGENT, andBITANGENTare modified in world space instead of model space. |
| ensure_correct_normals | Use when non-uniform scale is applied to mesh(note: currently unimplemented). |
| shadows_disabled | Disable computing shadows in shader. The shader will not receive shadows, but can still cast them. |
| ambient_light_disabled | Disable contribution from ambient light and radiance map. |
| shadow_to_opacity | Lighting modifies the alpha so shadowed areas are opaque and
non-shadowed areas are transparent. Useful for overlaying shadows onto
a camera feed in AR. |
| vertex_lighting | Use vertex-based lighting instead of per-pixel lighting. |
| particle_trails | Enables the trails when used on particle geometry. |
| alpha_to_coverage | Alpha antialiasing mode, seeherefor more. |
| alpha_to_coverage_and_one | Alpha antialiasing mode, seeherefor more. |
| fog_disabled | Disable receiving depth-based or volumetric fog. Useful forblend_addmaterials like particles. |

Render mode
Description
blend_mix
Mix blend mode (alpha is transparency), default.
blend_add
Additive blend mode.
blend_sub
Subtractive blend mode.
blend_mul
Multiplicative blend mode.
blend_premul_alpha
Premultiplied alpha blend mode (fully transparent = add, fully opaque = mix).
depth_draw_opaque
Only draw depth for opaque geometry (not transparent).
depth_draw_always
Always draw depth (opaque and transparent).
depth_draw_never
Never draw depth.
depth_prepass_alpha
Do opaque depth pre-pass for transparent geometry.
depth_test_disabled
Disable depth testing.
depth_test_default
Depth test will discard the pixel if it is behind other pixels.
In Forward+ only, the pixel is also discarded if it's at the exact same depth as another pixel.
depth_test_inverted
Depth test will discard the pixel if it is in front of other pixels. Useful for stencil effects.
sss_mode_skin
Subsurface Scattering mode for skin (optimizes visuals for human skin, e.g. boosted red channel).
cull_back
Cull back-faces (default).
cull_front
Cull front-faces.
cull_disabled
Culling disabled (double sided).
unshaded
Result is just albedo. No lighting/shading happens in material, making it faster to render.
wireframe
Geometry draws using lines (useful for troubleshooting).
debug_shadow_splits
Directional shadows are drawn using different colors for each split (useful for troubleshooting).
diffuse_burley
Burley (Disney PBS) for diffuse (default).
diffuse_lambert
Lambert shading for diffuse.
diffuse_lambert_wrap
Lambert-wrap shading (roughness-dependent) for diffuse.
diffuse_toon
Toon shading for diffuse.
specular_schlick_ggx
Schlick-GGX for direct light specular lobes (default).
specular_toon
Toon for direct light specular lobes.
specular_disabled
Disable direct light specular lobes. Doesn't affect reflected light (useSPECULAR=0.0instead).
skip_vertex_transform
VERTEX,NORMAL,TANGENT, andBITANGENTneed to be transformed manually in thevertex()function.
world_vertex_coords
VERTEX,NORMAL,TANGENT, andBITANGENTare modified in world space instead of model space.
ensure_correct_normals
Use when non-uniform scale is applied to mesh(note: currently unimplemented).
shadows_disabled
Disable computing shadows in shader. The shader will not receive shadows, but can still cast them.
ambient_light_disabled
Disable contribution from ambient light and radiance map.
shadow_to_opacity
Lighting modifies the alpha so shadowed areas are opaque and
non-shadowed areas are transparent. Useful for overlaying shadows onto
a camera feed in AR.
vertex_lighting
Use vertex-based lighting instead of per-pixel lighting.
particle_trails
Enables the trails when used on particle geometry.
alpha_to_coverage
Alpha antialiasing mode, seeherefor more.
alpha_to_coverage_and_one
Alpha antialiasing mode, seeherefor more.
fog_disabled
Disable receiving depth-based or volumetric fog. Useful forblend_addmaterials like particles.

## Stencil modes
Note
Stencil support is experimental, use at your own risk.
We will try to not break compatibility as much as possible,
but if significant flaws are found in the API, it may change
in the next minor version.
Stencil operations are a set of operations that allow writing to
an efficient buffer in an hardware-accelerated manner.
This is generally used to mask in or out parts of the scene.
Some of the most well-known uses are:
- Outlines: Mask out the inner mesh that is being outlined to avoid inner outlines.
Outlines: Mask out the inner mesh that is being outlined to avoid inner outlines.
- X-Ray: Display a mesh behind other objects.
X-Ray: Display a mesh behind other objects.
- Portals: Draw geometry that is normally "impossible" (non-Euclidian) by masking objects.
Portals: Draw geometry that is normally "impossible" (non-Euclidian) by masking objects.
Note
You can only read from the stencil buffer in the transparent pass.
Any attempt to read in the opaque pass will fail, as it's currently not supported behavior.
Note that for compositor effects, the main renderer's stencil buffer can't be copied
to a custom texture.

| Stencil mode | Description |
|---|---|
| read | Read from the stencil buffer. |
| write | Write reference value to the stencil buffer. |
| write_if_depth_fail | Write reference value to the stencil buffer if the depth test fails. |
| compare_always | Always pass stencil test. |
| compare_equal | Pass stencil test if the reference value is equal to the stencil buffer value. |
| compare_not_equal | Pass stencil test if the reference value is not equal to the stencil buffer value. |
| compare_less | Pass stencil test if the reference value is less than the stencil buffer value. |
| compare_less_or_equal | Pass stencil test if the reference value is less than or equal to the stencil buffer value. |
| compare_greater | Pass stencil test if the reference value is greater than the stencil buffer value. |
| compare_greater_or_equal | Pass stencil test if the reference value is greater than or equal to the stencil buffer value. |

Stencil mode
Description
read
Read from the stencil buffer.
write
Write reference value to the stencil buffer.
write_if_depth_fail
Write reference value to the stencil buffer if the depth test fails.
compare_always
Always pass stencil test.
compare_equal
Pass stencil test if the reference value is equal to the stencil buffer value.
compare_not_equal
Pass stencil test if the reference value is not equal to the stencil buffer value.
compare_less
Pass stencil test if the reference value is less than the stencil buffer value.
compare_less_or_equal
Pass stencil test if the reference value is less than or equal to the stencil buffer value.
compare_greater
Pass stencil test if the reference value is greater than the stencil buffer value.
compare_greater_or_equal
Pass stencil test if the reference value is greater than or equal to the stencil buffer value.

## Built-ins
Values marked asinare read-only. Values marked asoutcan optionally be written to and will
not necessarily contain sensible values. Values marked asinoutprovide a sensible default
value, and can optionally be written to. Samplers cannot be written to so they are not marked.
Not all built-ins are available in all processing functions. To access a vertex
built-in from thefragment()function, you can use avarying.
The same applies for accessing fragment built-ins from thelight()function.

## Global built-ins
Global built-ins are available everywhere, including custom functions.

| Built-in | Description |
|---|---|
| in floatTIME | Global time since the engine has started, in seconds. It repeats after every3,600seconds (which can be changed with therolloversetting). It's affected bytime_scalebut not by pausing.
If you need aTIMEvariable that is not affected by time scale, add your ownglobal shader uniformand update it each
frame. |
| in floatPI | APIconstant (3.141592).
The ratio of a circle's circumference to its diameter and the number of radians in a half turn. |
| in floatTAU | ATAUconstant (6.283185).
Equivalent toPI*2and the number of radians in a full turn. |
| in floatE | AnEconstant (2.718281). Euler's number, the base of the natural logarithm. |
| in boolOUTPUT_IS_SRGB | truewhen output is in sRGB color space (this istruein the Compatibility
renderer,falsein Forward+ and Mobile). |
| in floatCLIP_SPACE_FAR | Clip space farzvalue.
In the Forward+ or Mobile renderers, it's0.0.
In the Compatibility renderer, it's-1.0. |

Built-in
Description
in floatTIME
Global time since the engine has started, in seconds. It repeats after every3,600seconds (which can be changed with therolloversetting). It's affected bytime_scalebut not by pausing.
If you need aTIMEvariable that is not affected by time scale, add your ownglobal shader uniformand update it each
frame.
in floatPI
APIconstant (3.141592).
The ratio of a circle's circumference to its diameter and the number of radians in a half turn.
in floatTAU
ATAUconstant (6.283185).
Equivalent toPI*2and the number of radians in a full turn.
in floatE
AnEconstant (2.718281). Euler's number, the base of the natural logarithm.
in boolOUTPUT_IS_SRGB
truewhen output is in sRGB color space (this istruein the Compatibility
renderer,falsein Forward+ and Mobile).
in floatCLIP_SPACE_FAR
Clip space farzvalue.
In the Forward+ or Mobile renderers, it's0.0.
In the Compatibility renderer, it's-1.0.

## Vertex built-ins
Vertex data (VERTEX,NORMAL,TANGENT, andBITANGENT) are presented in model space
(also called local space). If not written to, these values will not be modified and be
passed through as they came, then transformed into view space to be used infragment().
They can optionally be presented in world space by using theworld_vertex_coordsrender mode.
Users can disable the built-in modelview transform (projection will still happen later) and do
it manually with the following code:
```
shader_type spatial;
render_mode skip_vertex_transform;

void vertex() {
    VERTEX = (MODELVIEW_MATRIX * vec4(VERTEX, 1.0)).xyz;
    NORMAL = normalize((MODELVIEW_MATRIX * vec4(NORMAL, 0.0)).xyz);
    BINORMAL = normalize((MODELVIEW_MATRIX * vec4(BINORMAL, 0.0)).xyz);
    TANGENT = normalize((MODELVIEW_MATRIX * vec4(TANGENT, 0.0)).xyz);
}
```
Other built-ins, such asUV,UV2, andCOLOR, are also passed through to thefragment()function if not modified.
Users can override the modelview and projection transforms using thePOSITIONbuilt-in. IfPOSITIONis written
to anywhere in the shader, it will always be used, so the user becomes responsible for ensuring that it always has
an acceptable value. WhenPOSITIONis used, the value fromVERTEXis ignored and projection does not happen.
However, the value passed to the fragment shader still comes fromVERTEX.
For instancing, theINSTANCE_CUSTOMvariable contains the instance custom data. When using particles, this information
is usually:
- x: Rotation angle in radians.
x: Rotation angle in radians.
- y: Phase during lifetime (0.0to1.0).
y: Phase during lifetime (0.0to1.0).
- z: Animation frame.
z: Animation frame.
This allows you to easily adjust the shader to a particle system using default particle material. When writing a custom particle
shader, this value can be used as desired.

| Built-in | Description |
|---|---|
| in vec2VIEWPORT_SIZE | Size of viewport (in pixels). |
| in mat4VIEW_MATRIX | World space to view space transform. |
| in mat4INV_VIEW_MATRIX | View space to world space transform. |
| in mat4MAIN_CAM_INV_VIEW_MATRIX | View space to world space transform of the camera used
to draw the current viewport. |
| in mat4INV_PROJECTION_MATRIX | Clip space to view space transform. |
| in vec3NODE_POSITION_WORLD | Node position, in world space. |
| in vec3NODE_POSITION_VIEW | Node position, in view space. |
| in vec3CAMERA_POSITION_WORLD | Camera position, in world space. Represents the
midpoint of the two eyes when in multiview/stereo
rendering. |
| in vec3CAMERA_DIRECTION_WORLD | Camera direction, in world space. |
| in uintCAMERA_VISIBLE_LAYERS | Cull layers of the camera rendering the current pass. |
| in intINSTANCE_ID | Instance ID for instancing. |
| in vec4INSTANCE_CUSTOM | Instance custom data (for particles, mostly). |
| in intVIEW_INDEX | The view that we are rendering.VIEW_MONO_LEFT(0) for Mono (not multiview) or
left eye,VIEW_RIGHT(1) for right eye. |
| in intVIEW_MONO_LEFT | Constant for Mono or left eye, always0. |
| in intVIEW_RIGHT | Constant for right eye, always1. |
| in vec3EYE_OFFSET | Position offset for the eye being rendered, in view
space. Only applicable for multiview rendering. |
| inout vec3VERTEX | Position of the vertex, in model space.
In world space ifworld_vertex_coordsis used. |
| in intVERTEX_ID | The index of the current vertex in the vertex buffer. |
| inout vec3NORMAL | Normal in model space.
In world space ifworld_vertex_coordsis used. |
| inout vec3TANGENT | Tangent in model space.
In world space ifworld_vertex_coordsis used. |
| inout vec3BINORMAL | Binormal in model space.
In world space ifworld_vertex_coordsis used. |
| out vec4POSITION | If written to, overrides final vertex position in clip
space. |
| inout vec2UV | UV main channel. |
| inout vec2UV2 | UV secondary channel. |
| inout vec4COLOR | Color from vertices. Limited to values between0.0and1.0for each channel and 8 bits per channel
precision (256 possible levels). Alpha channel is
supported. Values outside the allowed range are
clamped, and values may be rounded due to precision
limitations. UseCUSTOM0-CUSTOM3to pass data
with more precision if needed. |
| out floatROUGHNESS | Roughness for vertex lighting. |
| inout floatPOINT_SIZE | Point size for point rendering. |
| inout mat4MODELVIEW_MATRIX | Model/local space to view space transform
(use if possible). |
| inout mat3MODELVIEW_NORMAL_MATRIX |  |
| in mat4MODEL_MATRIX | Model/local space to world space transform. |
| in mat3MODEL_NORMAL_MATRIX |  |
| inout mat4PROJECTION_MATRIX | View space to clip space transform. |
| in uvec4BONE_INDICES |  |
| in vec4BONE_WEIGHTS |  |
| in vec4CUSTOM0 | Custom value from vertex primitive. When using extra
UVs,xyis UV3 andzwis UV4. |
| in vec4CUSTOM1 | Custom value from vertex primitive. When using extra
UVs,xyis UV5 andzwis UV6. |
| in vec4CUSTOM2 | Custom value from vertex primitive. When using extra
UVs,xyis UV7 andzwis UV8. |
| in vec4CUSTOM3 | Custom value from vertex primitive. |
| out floatZ_CLIP_SCALE | If written to, scales the vertex towards the camera to
avoid clipping into things like walls.
Lighting and shadows will continue to work correctly
when this is written to, but screen-space effects like
SSAO and SSR may break with lower scales. Try to keep
this value as close to1.0as possible. |

Built-in
Description
in vec2VIEWPORT_SIZE
Size of viewport (in pixels).
in mat4VIEW_MATRIX
World space to view space transform.
in mat4INV_VIEW_MATRIX
View space to world space transform.
in mat4MAIN_CAM_INV_VIEW_MATRIX
View space to world space transform of the camera used
to draw the current viewport.
in mat4INV_PROJECTION_MATRIX
Clip space to view space transform.
in vec3NODE_POSITION_WORLD
Node position, in world space.
in vec3NODE_POSITION_VIEW
Node position, in view space.
in vec3CAMERA_POSITION_WORLD
Camera position, in world space. Represents the
midpoint of the two eyes when in multiview/stereo
rendering.
in vec3CAMERA_DIRECTION_WORLD
Camera direction, in world space.
in uintCAMERA_VISIBLE_LAYERS
Cull layers of the camera rendering the current pass.
in intINSTANCE_ID
Instance ID for instancing.
in vec4INSTANCE_CUSTOM
Instance custom data (for particles, mostly).
in intVIEW_INDEX
The view that we are rendering.VIEW_MONO_LEFT(0) for Mono (not multiview) or
left eye,VIEW_RIGHT(1) for right eye.
in intVIEW_MONO_LEFT
Constant for Mono or left eye, always0.
in intVIEW_RIGHT
Constant for right eye, always1.
in vec3EYE_OFFSET
Position offset for the eye being rendered, in view
space. Only applicable for multiview rendering.
inout vec3VERTEX
Position of the vertex, in model space.
In world space ifworld_vertex_coordsis used.
in intVERTEX_ID
The index of the current vertex in the vertex buffer.
inout vec3NORMAL
Normal in model space.
In world space ifworld_vertex_coordsis used.
inout vec3TANGENT
Tangent in model space.
In world space ifworld_vertex_coordsis used.
inout vec3BINORMAL
Binormal in model space.
In world space ifworld_vertex_coordsis used.
out vec4POSITION
If written to, overrides final vertex position in clip
space.
inout vec2UV
UV main channel.
inout vec2UV2
UV secondary channel.
inout vec4COLOR
Color from vertices. Limited to values between0.0and1.0for each channel and 8 bits per channel
precision (256 possible levels). Alpha channel is
supported. Values outside the allowed range are
clamped, and values may be rounded due to precision
limitations. UseCUSTOM0-CUSTOM3to pass data
with more precision if needed.
out floatROUGHNESS
Roughness for vertex lighting.
inout floatPOINT_SIZE
Point size for point rendering.
inout mat4MODELVIEW_MATRIX
Model/local space to view space transform
(use if possible).
inout mat3MODELVIEW_NORMAL_MATRIX
in mat4MODEL_MATRIX
Model/local space to world space transform.
in mat3MODEL_NORMAL_MATRIX
inout mat4PROJECTION_MATRIX
View space to clip space transform.
in uvec4BONE_INDICES
in vec4BONE_WEIGHTS
in vec4CUSTOM0
Custom value from vertex primitive. When using extra
UVs,xyis UV3 andzwis UV4.
in vec4CUSTOM1
Custom value from vertex primitive. When using extra
UVs,xyis UV5 andzwis UV6.
in vec4CUSTOM2
Custom value from vertex primitive. When using extra
UVs,xyis UV7 andzwis UV8.
in vec4CUSTOM3
Custom value from vertex primitive.
out floatZ_CLIP_SCALE
If written to, scales the vertex towards the camera to
avoid clipping into things like walls.
Lighting and shadows will continue to work correctly
when this is written to, but screen-space effects like
SSAO and SSR may break with lower scales. Try to keep
this value as close to1.0as possible.
Note
MODELVIEW_MATRIXcombines both theMODEL_MATRIXandVIEW_MATRIXand is better suited when floating point issues may arise. For example, if the object is very far away from the world origin, you may run into floating point issues when using the separatedMODEL_MATRIXandVIEW_MATRIX.
Note
INV_VIEW_MATRIXis the matrix used for rendering the object in that pass, unlikeMAIN_CAM_INV_VIEW_MATRIX, which is the matrix of the camera in the scene. In the shadow pass,INV_VIEW_MATRIX's view is based on the camera that is located at the position of the light.

## Fragment built-ins
The default use of a Godot fragment processor function is to set up the material properties of your object
and to let the built-in renderer handle the final shading. However, you are not required to use all
these properties, and if you don't write to them, Godot will optimize away the corresponding functionality.

| Built-in | Description |
|---|---|
| in vec2VIEWPORT_SIZE | Size of viewport (in pixels). |
| in vec4FRAGCOORD | Coordinate of pixel center in screen space.xyspecifies position in window. Origin is upper
left.zspecifies fragment depth. It is also used as the output value for the fragment depth
unlessDEPTHis written to. |
| in boolFRONT_FACING | trueif current face is front facing,falseotherwise. |
| in vec3VIEW | Normalized vector from fragment position to camera (in view space). This is the same for both
perspective and orthogonal cameras. |
| in vec2UV | UV that comes from thevertex()function. |
| in vec2UV2 | UV2 that comes from thevertex()function. |
| in vec4COLOR | COLOR that comes from thevertex()function. |
| in vec2POINT_COORD | Point coordinate for drawing points withPOINT_SIZE. |
| in mat4MODEL_MATRIX | Model/local space to world space transform. |
| in mat3MODEL_NORMAL_MATRIX | Model/local space to world space transform for normals. This is the same asMODEL_MATRIXby default unless the object is scaled non-uniformly, in which case this is set totranspose(inverse(mat3(MODEL_MATRIX))). |
| in mat4VIEW_MATRIX | World space to view space transform. |
| in mat4INV_VIEW_MATRIX | View space to world space transform. |
| in mat4PROJECTION_MATRIX | View space to clip space transform. |
| in mat4INV_PROJECTION_MATRIX | Clip space to view space transform. |
| in vec3NODE_POSITION_WORLD | Node position, in world space. |
| in vec3NODE_POSITION_VIEW | Node position, in view space. |
| in vec3CAMERA_POSITION_WORLD | Camera position, in world space. Represents the midpoint of the two eyes when in
multiview/stereo rendering. |
| in vec3CAMERA_DIRECTION_WORLD | Camera direction, in world space. |
| in uintCAMERA_VISIBLE_LAYERS | Cull layers of the camera rendering the current pass. |
| in vec3VERTEX | Position of the fragment (pixel), in view space. It is theVERTEXvalue fromvertex()interpolated between the face's vertices and transformed into view space.
Ifskip_vertex_transformis enabled, it may not be in view space. |
| inout vec3LIGHT_VERTEX | A writable version ofVERTEXthat can be used to alter light and shadows. Writing to this
will not change the position of the fragment. |
| in intVIEW_INDEX | The view that we are rendering. Used to distinguish between views in multiview/stereo rendering.VIEW_MONO_LEFT(0) for Mono (not multiview) or
left eye,VIEW_RIGHT(1) for right eye. |
| in intVIEW_MONO_LEFT | Constant for Mono or left eye, always0. |
| in intVIEW_RIGHT | Constant for right eye, always1. |
| in vec3EYE_OFFSET | Position offset for the eye being rendered, in view space. Only applicable for multiview
rendering. |
| sampler2DSCREEN_TEXTURE | Removed in Godot 4. Use asampler2Dwithhint_screen_textureinstead. |
| in vec2SCREEN_UV | Screen UV coordinate for the current pixel. |
| sampler2DDEPTH_TEXTURE | Removed in Godot 4. Use asampler2Dwithhint_depth_textureinstead. |
| out floatDEPTH | Custom depth value (range[0.0,1.0]). IfDEPTHis written to in any shader branch,
then you are responsible for settingDEPTHforallother branches.
Otherwise, the graphics API will leave them uninitialized. |
| inout vec3NORMAL | Normal that comes from thevertex()function, in view space.
Ifskip_vertex_transformis enabled, it may not be in view space. |
| inout vec3TANGENT | Tangent that comes from thevertex()function, in view space.
Ifskip_vertex_transformis enabled, it may not be in view space. |
| inout vec3BINORMAL | Binormal that comes from thevertex()function, in view space.
Ifskip_vertex_transformis enabled, it may not be in view space. |
| out vec3NORMAL_MAP | Set normal here if reading normal from a texture instead ofNORMAL. |
| out floatNORMAL_MAP_DEPTH | Depth fromNORMAL_MAP. Defaults to1.0. |
| out vec3ALBEDO | Albedo (default white). Base color. |
| out floatALPHA | Alpha (range[0.0,1.0]). If read from or written to, the material will go to the
transparent pipeline. |
| out floatALPHA_SCISSOR_THRESHOLD | If written to, values below a certain amount of alpha are discarded. |
| out floatALPHA_HASH_SCALE | Alpha hash scale when using the alpha hash transparency mode. Defaults to1.0.
Higher values result in more visible pixels in the dithering pattern. |
| out floatALPHA_ANTIALIASING_EDGE | The threshold below which alpha to coverage antialiasing should be used. Defaults to0.0.
Requires thealpha_to_coveragerender mode. Should be set to a value lower thanALPHA_SCISSOR_THRESHOLDto be effective. |
| out vec2ALPHA_TEXTURE_COORDINATE | The texture coordinate to use for alpha-to-coverge antialiasing. Requires thealpha_to_coveragerender mode. Typically set toUV*vec2(albedo_texture_size)wherealbedo_texture_sizeis the size of the albedo texture in pixels. |
| out floatPREMUL_ALPHA_FACTOR | Premultiplied alpha factor. Only effective ifrender_modeblend_premul_alpha;is used.
This should be written to when using ashadedmaterial with premultiplied alpha blending for
interaction with lighting. This is not required for unshaded materials. |
| out floatMETALLIC | Metallic (range[0.0,1.0]). |
| out floatSPECULAR | Specular (not physically accurate to change). Defaults to0.5.0.0disables reflections. |
| out floatROUGHNESS | Roughness (range[0.0,1.0]). |
| out floatRIM | Rim (range[0.0,1.0]). If used, Godot calculates rim lighting.
Rim size depends onROUGHNESS. |
| out floatRIM_TINT | Rim Tint, range from0.0(white) to1.0(albedo). If used, Godot calculates rim lighting. |
| out floatCLEARCOAT | Small specular blob added on top of the existing one. If used, Godot calculates clearcoat. |
| out floatCLEARCOAT_GLOSS | Gloss of clearcoat. If used, Godot calculates clearcoat. |
| out floatANISOTROPY | For distorting the specular blob according to tangent space. |
| out vec2ANISOTROPY_FLOW | Distortion direction, use with flowmaps. |
| out floatSSS_STRENGTH | Strength of subsurface scattering. If used, subsurface scattering will be applied to the object. |
| out vec4SSS_TRANSMITTANCE_COLOR | Color of subsurface scattering transmittance. If used, subsurface scattering transmittance
will be applied to the object. |
| out floatSSS_TRANSMITTANCE_DEPTH | Depth of subsurface scattering transmittance. Higher values allow the effect to reach deeper
into the object. |
| out floatSSS_TRANSMITTANCE_BOOST | Boosts the subsurface scattering transmittance if set above0.0. This makes the effect
show up even on directly lit surfaces |
| inout vec3BACKLIGHT | Color of backlighting (works like direct light, but it's received even if the normal
is slightly facing away from the light). If used, backlighting will be applied to the object.
Can be used as a cheaper approximation of subsurface scattering. |
| out floatAO | Strength of ambient occlusion. For use with pre-baked AO. |
| out floatAO_LIGHT_AFFECT | How much ambient occlusion affects direct light (range[0.0,1.0], default0.0). |
| out vec3EMISSION | Emission color (can go over(1.0,1.0,1.0)for HDR). |
| out vec4FOG | If written to, blends final pixel color withFOG.rgbbased onFOG.a. |
| out vec4RADIANCE | If written to, blends environment map radiance withRADIANCE.rgbbased onRADIANCE.a. |
| out vec4IRRADIANCE | If written to, blends environment map irradiance withIRRADIANCE.rgbbased onIRRADIANCE.a. |

Built-in
Description
in vec2VIEWPORT_SIZE
Size of viewport (in pixels).
in vec4FRAGCOORD
Coordinate of pixel center in screen space.xyspecifies position in window. Origin is upper
left.zspecifies fragment depth. It is also used as the output value for the fragment depth
unlessDEPTHis written to.
in boolFRONT_FACING
trueif current face is front facing,falseotherwise.
in vec3VIEW
Normalized vector from fragment position to camera (in view space). This is the same for both
perspective and orthogonal cameras.
in vec2UV
UV that comes from thevertex()function.
in vec2UV2
UV2 that comes from thevertex()function.
in vec4COLOR
COLOR that comes from thevertex()function.
in vec2POINT_COORD
Point coordinate for drawing points withPOINT_SIZE.
in mat4MODEL_MATRIX
Model/local space to world space transform.
in mat3MODEL_NORMAL_MATRIX
Model/local space to world space transform for normals. This is the same asMODEL_MATRIXby default unless the object is scaled non-uniformly, in which case this is set totranspose(inverse(mat3(MODEL_MATRIX))).
in mat4VIEW_MATRIX
World space to view space transform.
in mat4INV_VIEW_MATRIX
View space to world space transform.
in mat4PROJECTION_MATRIX
View space to clip space transform.
in mat4INV_PROJECTION_MATRIX
Clip space to view space transform.
in vec3NODE_POSITION_WORLD
Node position, in world space.
in vec3NODE_POSITION_VIEW
Node position, in view space.
in vec3CAMERA_POSITION_WORLD
Camera position, in world space. Represents the midpoint of the two eyes when in
multiview/stereo rendering.
in vec3CAMERA_DIRECTION_WORLD
Camera direction, in world space.
in uintCAMERA_VISIBLE_LAYERS
Cull layers of the camera rendering the current pass.
in vec3VERTEX
Position of the fragment (pixel), in view space. It is theVERTEXvalue fromvertex()interpolated between the face's vertices and transformed into view space.
Ifskip_vertex_transformis enabled, it may not be in view space.
inout vec3LIGHT_VERTEX
A writable version ofVERTEXthat can be used to alter light and shadows. Writing to this
will not change the position of the fragment.
in intVIEW_INDEX
The view that we are rendering. Used to distinguish between views in multiview/stereo rendering.VIEW_MONO_LEFT(0) for Mono (not multiview) or
left eye,VIEW_RIGHT(1) for right eye.
in intVIEW_MONO_LEFT
Constant for Mono or left eye, always0.
in intVIEW_RIGHT
Constant for right eye, always1.
in vec3EYE_OFFSET
Position offset for the eye being rendered, in view space. Only applicable for multiview
rendering.
sampler2DSCREEN_TEXTURE
Removed in Godot 4. Use asampler2Dwithhint_screen_textureinstead.
in vec2SCREEN_UV
Screen UV coordinate for the current pixel.
sampler2DDEPTH_TEXTURE
Removed in Godot 4. Use asampler2Dwithhint_depth_textureinstead.
out floatDEPTH
Custom depth value (range[0.0,1.0]). IfDEPTHis written to in any shader branch,
then you are responsible for settingDEPTHforallother branches.
Otherwise, the graphics API will leave them uninitialized.
inout vec3NORMAL
Normal that comes from thevertex()function, in view space.
Ifskip_vertex_transformis enabled, it may not be in view space.
inout vec3TANGENT
Tangent that comes from thevertex()function, in view space.
Ifskip_vertex_transformis enabled, it may not be in view space.
inout vec3BINORMAL
Binormal that comes from thevertex()function, in view space.
Ifskip_vertex_transformis enabled, it may not be in view space.
out vec3NORMAL_MAP
Set normal here if reading normal from a texture instead ofNORMAL.
out floatNORMAL_MAP_DEPTH
Depth fromNORMAL_MAP. Defaults to1.0.
out vec3ALBEDO
Albedo (default white). Base color.
out floatALPHA
Alpha (range[0.0,1.0]). If read from or written to, the material will go to the
transparent pipeline.
out floatALPHA_SCISSOR_THRESHOLD
If written to, values below a certain amount of alpha are discarded.
out floatALPHA_HASH_SCALE
Alpha hash scale when using the alpha hash transparency mode. Defaults to1.0.
Higher values result in more visible pixels in the dithering pattern.
out floatALPHA_ANTIALIASING_EDGE
The threshold below which alpha to coverage antialiasing should be used. Defaults to0.0.
Requires thealpha_to_coveragerender mode. Should be set to a value lower thanALPHA_SCISSOR_THRESHOLDto be effective.
out vec2ALPHA_TEXTURE_COORDINATE
The texture coordinate to use for alpha-to-coverge antialiasing. Requires thealpha_to_coveragerender mode. Typically set toUV*vec2(albedo_texture_size)wherealbedo_texture_sizeis the size of the albedo texture in pixels.
out floatPREMUL_ALPHA_FACTOR
Premultiplied alpha factor. Only effective ifrender_modeblend_premul_alpha;is used.
This should be written to when using ashadedmaterial with premultiplied alpha blending for
interaction with lighting. This is not required for unshaded materials.
out floatMETALLIC
Metallic (range[0.0,1.0]).
out floatSPECULAR
Specular (not physically accurate to change). Defaults to0.5.0.0disables reflections.
out floatROUGHNESS
Roughness (range[0.0,1.0]).
out floatRIM
Rim (range[0.0,1.0]). If used, Godot calculates rim lighting.
Rim size depends onROUGHNESS.
out floatRIM_TINT
Rim Tint, range from0.0(white) to1.0(albedo). If used, Godot calculates rim lighting.
out floatCLEARCOAT
Small specular blob added on top of the existing one. If used, Godot calculates clearcoat.
out floatCLEARCOAT_GLOSS
Gloss of clearcoat. If used, Godot calculates clearcoat.
out floatANISOTROPY
For distorting the specular blob according to tangent space.
out vec2ANISOTROPY_FLOW
Distortion direction, use with flowmaps.
out floatSSS_STRENGTH
Strength of subsurface scattering. If used, subsurface scattering will be applied to the object.
out vec4SSS_TRANSMITTANCE_COLOR
Color of subsurface scattering transmittance. If used, subsurface scattering transmittance
will be applied to the object.
out floatSSS_TRANSMITTANCE_DEPTH
Depth of subsurface scattering transmittance. Higher values allow the effect to reach deeper
into the object.
out floatSSS_TRANSMITTANCE_BOOST
Boosts the subsurface scattering transmittance if set above0.0. This makes the effect
show up even on directly lit surfaces
inout vec3BACKLIGHT
Color of backlighting (works like direct light, but it's received even if the normal
is slightly facing away from the light). If used, backlighting will be applied to the object.
Can be used as a cheaper approximation of subsurface scattering.
out floatAO
Strength of ambient occlusion. For use with pre-baked AO.
out floatAO_LIGHT_AFFECT
How much ambient occlusion affects direct light (range[0.0,1.0], default0.0).
out vec3EMISSION
Emission color (can go over(1.0,1.0,1.0)for HDR).
out vec4FOG
If written to, blends final pixel color withFOG.rgbbased onFOG.a.
out vec4RADIANCE
If written to, blends environment map radiance withRADIANCE.rgbbased onRADIANCE.a.
out vec4IRRADIANCE
If written to, blends environment map irradiance withIRRADIANCE.rgbbased onIRRADIANCE.a.
Note
Shaders going through the transparent pipeline whenALPHAis written to
may exhibit transparency sorting issues. Read thetransparency sorting section in the 3D rendering limitations pagefor more information and ways to avoid issues.

## Light built-ins
Writing light processor functions is completely optional. You can skip thelight()function by using
theunshadedrender mode. If no light function is written, Godot will use the material properties
written to in thefragment()function to calculate the lighting for you (subject to the render mode).
Thelight()function is called for every light in every pixel. It is called within a loop for each light type.
Below is an example of a customlight()function using a Lambertian lighting model:
```
void light() {
    DIFFUSE_LIGHT += clamp(dot(NORMAL, LIGHT), 0.0, 1.0) * ATTENUATION * LIGHT_COLOR / PI;
}
```
If you want the lights to add together, add the light contribution toDIFFUSE_LIGHTusing+=, rather than overwriting it.
Warning
Thelight()function won't be run if thevertex_lightingrender mode is enabled, or ifRendering > Quality > Shading > Force Vertex Shadingis enabled in the Project Settings. (It's enabled by default on mobile platforms.)

| Built-in | Description |
|---|---|
| in vec2VIEWPORT_SIZE | Size of viewport (in pixels). |
| in vec4FRAGCOORD | Coordinate of pixel center in screen space.xyspecifies position in window,zspecifies fragment depth ifDEPTHis not used.
Origin is lower-left. |
| in mat4MODEL_MATRIX | Model/local space to world space transform. |
| in mat4INV_VIEW_MATRIX | View space to world space transform. |
| in mat4VIEW_MATRIX | World space to view space transform. |
| in mat4PROJECTION_MATRIX | View space to clip space transform. |
| in mat4INV_PROJECTION_MATRIX | Clip space to view space transform. |
| in vec3NORMAL | Normal vector, in view space. |
| in vec2SCREEN_UV | Screen UV coordinate for the current pixel. |
| in vec2UV | UV that comes from thevertex()function. |
| in vec2UV2 | UV2 that comes from thevertex()function. |
| in vec3VIEW | View vector, in view space. |
| in vec3LIGHT | Light vector, in view space. |
| in vec3LIGHT_COLOR | Light colormultiplied bylight energymultiplied byPI. ThePImultiplication is present because
physically-based lighting models include a division byPI. |
| in floatSPECULAR_AMOUNT | ForOmniLight3DandSpotLight3D,2.0multiplied bylight_specular.
ForDirectionalLight3D,1.0. |
| in boolLIGHT_IS_DIRECTIONAL | trueif this pass is aDirectionalLight3D. |
| in floatATTENUATION | Attenuation based on distance or shadow. |
| in vec3ALBEDO | Base albedo. |
| in vec3BACKLIGHT |  |
| in floatMETALLIC | Metallic. |
| in floatROUGHNESS | Roughness. |
| out vec3DIFFUSE_LIGHT | Diffuse light result. |
| out vec3SPECULAR_LIGHT | Specular light result. |
| out floatALPHA | Alpha (range[0.0,1.0]). If written to, the material will go to
the transparent pipeline. |

Built-in
Description
in vec2VIEWPORT_SIZE
Size of viewport (in pixels).
in vec4FRAGCOORD
Coordinate of pixel center in screen space.xyspecifies position in window,zspecifies fragment depth ifDEPTHis not used.
Origin is lower-left.
in mat4MODEL_MATRIX
Model/local space to world space transform.
in mat4INV_VIEW_MATRIX
View space to world space transform.
in mat4VIEW_MATRIX
World space to view space transform.
in mat4PROJECTION_MATRIX
View space to clip space transform.
in mat4INV_PROJECTION_MATRIX
Clip space to view space transform.
in vec3NORMAL
Normal vector, in view space.
in vec2SCREEN_UV
Screen UV coordinate for the current pixel.
in vec2UV
UV that comes from thevertex()function.
in vec2UV2
UV2 that comes from thevertex()function.
in vec3VIEW
View vector, in view space.
in vec3LIGHT
Light vector, in view space.
in vec3LIGHT_COLOR
Light colormultiplied bylight energymultiplied byPI. ThePImultiplication is present because
physically-based lighting models include a division byPI.
in floatSPECULAR_AMOUNT
ForOmniLight3DandSpotLight3D,2.0multiplied bylight_specular.
ForDirectionalLight3D,1.0.
in boolLIGHT_IS_DIRECTIONAL
trueif this pass is aDirectionalLight3D.
in floatATTENUATION
Attenuation based on distance or shadow.
in vec3ALBEDO
Base albedo.
in vec3BACKLIGHT
in floatMETALLIC
Metallic.
in floatROUGHNESS
Roughness.
out vec3DIFFUSE_LIGHT
Diffuse light result.
out vec3SPECULAR_LIGHT
Specular light result.
out floatALPHA
Alpha (range[0.0,1.0]). If written to, the material will go to
the transparent pipeline.
Note
Shaders going through the transparent pipeline whenALPHAis written to
may exhibit transparency sorting issues. Read thetransparency sorting section in the 3D rendering limitations pagefor more information and ways to avoid issues.
Transparent materials also cannot cast shadows or appear inhint_screen_textureandhint_depth_textureuniforms. This in turn prevents those
materials from appearing in screen-space reflections or refraction.SDFGIsharp reflections are not visible on transparent
materials (only rough reflections are visible on transparent materials).

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.