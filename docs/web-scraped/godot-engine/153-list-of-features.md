# List of features

# List of features
This page aims to listallfeatures currently supported by Godot.
Note
This page lists features supported by the current stable version of
Godot. Some of these features are not available in the3.x release series.

## Platforms
See also
SeeSystem requirementsfor hardware and software version requirements.
Note
For information about console support, see theGodot website.
Can run both the editor and exported projects:
- Windows (x86 and ARM, 64-bit and 32-bit).
Windows (x86 and ARM, 64-bit and 32-bit).
- macOS (x86 and ARM, 64-bit only).
macOS (x86 and ARM, 64-bit only).
- Linux (x86 and ARM, 64-bit and 32-bit).Binaries are statically linked and can run on any distribution if compiled
on an old enough base distribution.Official binaries are compiled using theGodot Engine buildroot,
allowing for binaries that work across common Linux distributions.
Linux (x86 and ARM, 64-bit and 32-bit).
> Binaries are statically linked and can run on any distribution if compiled
on an old enough base distribution.Official binaries are compiled using theGodot Engine buildroot,
allowing for binaries that work across common Linux distributions.
- Binaries are statically linked and can run on any distribution if compiled
on an old enough base distribution.
Binaries are statically linked and can run on any distribution if compiled
on an old enough base distribution.
- Official binaries are compiled using theGodot Engine buildroot,
allowing for binaries that work across common Linux distributions.
Official binaries are compiled using theGodot Engine buildroot,
allowing for binaries that work across common Linux distributions.
- Android (editor support is experimental).
Android (editor support is experimental).
- Web browsers. Experimental in 4.0,
using Godot 3.x is recommended instead when targeting HTML5.
Web browsers. Experimental in 4.0,
using Godot 3.x is recommended instead when targeting HTML5.
Note
Linux supports rv64 (RISC-V), ppc64 & ppc32 (PowerPC), and loongarch64. However
you must compile the editor for that platform (as well as export templates)
yourself, no official downloads are currently provided. RISC-V compiling
instructions can be found on theCompiling for Linux, *BSDpage.
Runs exported projects:
- iOS.
iOS.
Godot aims to be as platform-independent as possible and can beported to new platformswith relative ease.
Note
Projects written in C# using Godot 4 currently cannot be exported to the
web platform. To use C# on that platform, consider Godot 3 instead.
Android and iOS platform support is available as of Godot 4.2, but is
experimental andsome limitations apply.

## Editor
Features:
- Scene tree editor.
Scene tree editor.
- Built-in script editor.
Built-in script editor.
- Support forexternal script editorssuch as
Visual Studio Code or Vim.
Support forexternal script editorssuch as
Visual Studio Code or Vim.
- GDScriptdebugger.Support for debugging in threads is available since 4.2.
GDScriptdebugger.
> Support for debugging in threads is available since 4.2.
- Support for debugging in threads is available since 4.2.
Support for debugging in threads is available since 4.2.
- Visual profiler with CPU and GPU time indications for each step of the
rendering pipeline.
Visual profiler with CPU and GPU time indications for each step of the
rendering pipeline.
- Performance monitoring tools, includingcustom performance monitors.
Performance monitoring tools, includingcustom performance monitors.
- Live script reloading.
Live script reloading.
- Live scene editing.Changes will reflect in the editor and will be kept after closing the running project.
Live scene editing.
> Changes will reflect in the editor and will be kept after closing the running project.
- Changes will reflect in the editor and will be kept after closing the running project.
Changes will reflect in the editor and will be kept after closing the running project.
- Remote inspector.Changes won't reflect in the editor and won't be kept after closing the running project.
Remote inspector.
> Changes won't reflect in the editor and won't be kept after closing the running project.
- Changes won't reflect in the editor and won't be kept after closing the running project.
Changes won't reflect in the editor and won't be kept after closing the running project.
- Live camera replication.Move the in-editor camera and see the result in the running project.
Live camera replication.
> Move the in-editor camera and see the result in the running project.
- Move the in-editor camera and see the result in the running project.
Move the in-editor camera and see the result in the running project.
- Built-in offline class reference documentation.
Built-in offline class reference documentation.
- Use the editor in dozens of languages contributed by the community.
Use the editor in dozens of languages contributed by the community.
Plugins:
- Editor plugins can be downloaded from theasset libraryto extend editor functionality.
Editor plugins can be downloaded from theasset libraryto extend editor functionality.
- Create your own pluginsusing GDScript to add new
features or speed up your workflow.
Create your own pluginsusing GDScript to add new
features or speed up your workflow.
- Download projects from the asset libraryin the Project Manager and import them directly.
Download projects from the asset libraryin the Project Manager and import them directly.

## Rendering
Godot 4 includes three renderers:
- Forward+. The most advanced renderer, suited for desktop platforms only.
Used by default on desktop platforms. This renderer usesVulkan,Direct3D 12,
orMetalas the rendering driver, and it uses theRenderingDevicebackend.
Forward+. The most advanced renderer, suited for desktop platforms only.
Used by default on desktop platforms. This renderer usesVulkan,Direct3D 12,
orMetalas the rendering driver, and it uses theRenderingDevicebackend.
- Mobile. Fewer features, but renders simple scenes faster. Suited for mobile
and desktop platforms. Used by default on mobile platforms. This renderer usesVulkan,Direct3D 12, orMetalas the rendering driver, and it uses
theRenderingDevicebackend.
Mobile. Fewer features, but renders simple scenes faster. Suited for mobile
and desktop platforms. Used by default on mobile platforms. This renderer usesVulkan,Direct3D 12, orMetalas the rendering driver, and it uses
theRenderingDevicebackend.
- Compatibility, sometimes calledGL Compatibility. The least advanced
renderer, suited for low-end desktop and mobile platforms. Used by default on
the web platform. This renderer usesOpenGLas the rendering driver.
Compatibility, sometimes calledGL Compatibility. The least advanced
renderer, suited for low-end desktop and mobile platforms. Used by default on
the web platform. This renderer usesOpenGLas the rendering driver.
SeeOverview of renderersfor a detailed comparison of the rendering methods.

## 2D graphics
- Sprite, polygon and line rendering.High-level tools to draw lines and polygons such asPolygon2DandLine2D, with support for texturing.
Sprite, polygon and line rendering.
> High-level tools to draw lines and polygons such asPolygon2DandLine2D, with support for texturing.
- High-level tools to draw lines and polygons such asPolygon2DandLine2D, with support for texturing.
High-level tools to draw lines and polygons such asPolygon2DandLine2D, with support for texturing.
- AnimatedSprite2D as a helper for creating animated sprites.
AnimatedSprite2D as a helper for creating animated sprites.
- Parallax layers.Pseudo-3D support including preview in the editor.
Parallax layers.
> Pseudo-3D support including preview in the editor.
- Pseudo-3D support including preview in the editor.
Pseudo-3D support including preview in the editor.
- 2D lightingwith normal maps and specular maps.Point (omni/spot) and directional 2D lights.Hard or soft shadows (adjustable on a per-light basis).Custom shaders can access a real-timeSDFrepresentation of the 2D scene based onLightOccluder2Dnodes,
which can be used for improved 2D lighting effects including 2D global illumination.
2D lightingwith normal maps and specular maps.
> Point (omni/spot) and directional 2D lights.Hard or soft shadows (adjustable on a per-light basis).Custom shaders can access a real-timeSDFrepresentation of the 2D scene based onLightOccluder2Dnodes,
which can be used for improved 2D lighting effects including 2D global illumination.
- Point (omni/spot) and directional 2D lights.
Point (omni/spot) and directional 2D lights.
- Hard or soft shadows (adjustable on a per-light basis).
Hard or soft shadows (adjustable on a per-light basis).
- Custom shaders can access a real-timeSDFrepresentation of the 2D scene based onLightOccluder2Dnodes,
which can be used for improved 2D lighting effects including 2D global illumination.
Custom shaders can access a real-timeSDFrepresentation of the 2D scene based onLightOccluder2Dnodes,
which can be used for improved 2D lighting effects including 2D global illumination.
- Font renderingusing bitmaps, rasterization using FreeType
or multi-channel signed distance fields (MSDF).Bitmap fonts can be exported using tools like BMFont, or imported from images
(for fixed-width fonts only).Dynamic fonts support monochrome fonts as well as colored fonts (e.g. for emoji).
Supported formats are TTF, OTF, WOFF1 and WOFF2.Dynamic fonts support optional font outlines with adjustable width and color.Dynamic fonts support variable fonts and OpenType features including ligatures.Dynamic fonts support simulated bold and italic when the font file lacks
those styles.Dynamic fonts support oversampling to keep fonts sharp at higher resolutions.Dynamic fonts support subpixel positioning to make fonts crisper at low sizes.Dynamic fonts support LCD subpixel optimizations to make fonts even crisper at low sizes.Signed distance field fonts can be scaled at any resolution without
requiring re-rasterization. Multi-channel usage makes SDF fonts scale down
to lower sizes better compared to monochrome SDF fonts.
Font renderingusing bitmaps, rasterization using FreeType
or multi-channel signed distance fields (MSDF).
> Bitmap fonts can be exported using tools like BMFont, or imported from images
(for fixed-width fonts only).Dynamic fonts support monochrome fonts as well as colored fonts (e.g. for emoji).
Supported formats are TTF, OTF, WOFF1 and WOFF2.Dynamic fonts support optional font outlines with adjustable width and color.Dynamic fonts support variable fonts and OpenType features including ligatures.Dynamic fonts support simulated bold and italic when the font file lacks
those styles.Dynamic fonts support oversampling to keep fonts sharp at higher resolutions.Dynamic fonts support subpixel positioning to make fonts crisper at low sizes.Dynamic fonts support LCD subpixel optimizations to make fonts even crisper at low sizes.Signed distance field fonts can be scaled at any resolution without
requiring re-rasterization. Multi-channel usage makes SDF fonts scale down
to lower sizes better compared to monochrome SDF fonts.
- Bitmap fonts can be exported using tools like BMFont, or imported from images
(for fixed-width fonts only).
Bitmap fonts can be exported using tools like BMFont, or imported from images
(for fixed-width fonts only).
- Dynamic fonts support monochrome fonts as well as colored fonts (e.g. for emoji).
Supported formats are TTF, OTF, WOFF1 and WOFF2.
Dynamic fonts support monochrome fonts as well as colored fonts (e.g. for emoji).
Supported formats are TTF, OTF, WOFF1 and WOFF2.
- Dynamic fonts support optional font outlines with adjustable width and color.
Dynamic fonts support optional font outlines with adjustable width and color.
- Dynamic fonts support variable fonts and OpenType features including ligatures.
Dynamic fonts support variable fonts and OpenType features including ligatures.
- Dynamic fonts support simulated bold and italic when the font file lacks
those styles.
Dynamic fonts support simulated bold and italic when the font file lacks
those styles.
- Dynamic fonts support oversampling to keep fonts sharp at higher resolutions.
Dynamic fonts support oversampling to keep fonts sharp at higher resolutions.
- Dynamic fonts support subpixel positioning to make fonts crisper at low sizes.
Dynamic fonts support subpixel positioning to make fonts crisper at low sizes.
- Dynamic fonts support LCD subpixel optimizations to make fonts even crisper at low sizes.
Dynamic fonts support LCD subpixel optimizations to make fonts even crisper at low sizes.
- Signed distance field fonts can be scaled at any resolution without
requiring re-rasterization. Multi-channel usage makes SDF fonts scale down
to lower sizes better compared to monochrome SDF fonts.
Signed distance field fonts can be scaled at any resolution without
requiring re-rasterization. Multi-channel usage makes SDF fonts scale down
to lower sizes better compared to monochrome SDF fonts.
- GPU-basedparticleswith support forcustom particle shaders.
GPU-basedparticleswith support forcustom particle shaders.
- CPU-based particles.
CPU-based particles.
- Optional2D HDR renderingfor better glow capabilities.
Optional2D HDR renderingfor better glow capabilities.

## 2D tools
- TileMapsfor 2D tile-based level design.
TileMapsfor 2D tile-based level design.
- 2D camera with built-in smoothing and drag margins.
2D camera with built-in smoothing and drag margins.
- Path2D node to represent a path in 2D space.Can be drawn in the editor or generated procedurally.PathFollow2D node to make nodes follow a Path2D.
Path2D node to represent a path in 2D space.
> Can be drawn in the editor or generated procedurally.PathFollow2D node to make nodes follow a Path2D.
- Can be drawn in the editor or generated procedurally.
Can be drawn in the editor or generated procedurally.
- PathFollow2D node to make nodes follow a Path2D.
PathFollow2D node to make nodes follow a Path2D.
- 2D geometry helper class.
2D geometry helper class.

## 2D physics
Physics bodies:
- Static bodies.
Static bodies.
- Animatable bodies (for objects moving only by script or animation, such as doors and platforms).
Animatable bodies (for objects moving only by script or animation, such as doors and platforms).
- Rigid bodies.
Rigid bodies.
- Character bodies.
Character bodies.
- Joints.
Joints.
- Areas to detect bodies entering or leaving it.
Areas to detect bodies entering or leaving it.
Collision detection:
- Built-in shapes: line, box, circle, capsule, world boundary (infinite plane).
Built-in shapes: line, box, circle, capsule, world boundary (infinite plane).
- Collision polygons (can be drawn manually or generated from a sprite in the editor).
Collision polygons (can be drawn manually or generated from a sprite in the editor).

## 3D graphics
- HDR rendering with sRGB.
HDR rendering with sRGB.
- Perspective, orthographic and frustum-offset cameras.
Perspective, orthographic and frustum-offset cameras.
- When using the Forward+ renderer, a depth prepass is used to improve
performance in complex scenes by reducing the cost of overdraw.
When using the Forward+ renderer, a depth prepass is used to improve
performance in complex scenes by reducing the cost of overdraw.
- Variable rate shadingon supported GPUs in Forward+ and Mobile.
Variable rate shadingon supported GPUs in Forward+ and Mobile.
Physically-based rendering (built-in material features):
- Follows the Disney PBR model.
Follows the Disney PBR model.
- Supports Burley, Lambert, Lambert Wrap (half-Lambert) and Toon diffuse shading modes.
Supports Burley, Lambert, Lambert Wrap (half-Lambert) and Toon diffuse shading modes.
- Supports Schlick-GGX, Toon and Disabled specular shading modes.
Supports Schlick-GGX, Toon and Disabled specular shading modes.
- Uses a roughness-metallic workflow with support for ORM textures.
Uses a roughness-metallic workflow with support for ORM textures.
- Uses horizon specular occlusion (Filament model) to improve material appearance.
Uses horizon specular occlusion (Filament model) to improve material appearance.
- Normal mapping.
Normal mapping.
- Parallax/relief mapping with automatic level of detail based on distance.
Parallax/relief mapping with automatic level of detail based on distance.
- Detail mapping for the albedo and normal maps.
Detail mapping for the albedo and normal maps.
- Sub-surface scattering and transmittance.
Sub-surface scattering and transmittance.
- Screen-space refraction with support for material roughness (resulting in blurry refraction).
Screen-space refraction with support for material roughness (resulting in blurry refraction).
- Proximity fade (soft particles) and distance fade.
Proximity fade (soft particles) and distance fade.
- Distance fade can use alpha blending or dithering to avoid going through
the transparent pipeline.
Distance fade can use alpha blending or dithering to avoid going through
the transparent pipeline.
- Dithering can be determined on a per-pixel or per-object basis.
Dithering can be determined on a per-pixel or per-object basis.
Real-time lighting:
- Directional lights (sun/moon). Up to 4 per scene.
Directional lights (sun/moon). Up to 4 per scene.
- Omnidirectional lights.
Omnidirectional lights.
- Spot lights with adjustable cone angle and attenuation.
Spot lights with adjustable cone angle and attenuation.
- Specular, indirect light, and volumetric fog energy can be adjusted on a per-light basis.
Specular, indirect light, and volumetric fog energy can be adjusted on a per-light basis.
- Adjustable light "size" for fake area lights (will also make shadows blurrier).
Adjustable light "size" for fake area lights (will also make shadows blurrier).
- Optional distance fade system to fade distant lights and their shadows, improving performance.
Optional distance fade system to fade distant lights and their shadows, improving performance.
- When using the Forward+ renderer (default on desktop), lights are
rendered with clustered forward optimizations to decrease their individual cost.
Clustered rendering also lifts any limits on the number of lights that can be used on a mesh.
When using the Forward+ renderer (default on desktop), lights are
rendered with clustered forward optimizations to decrease their individual cost.
Clustered rendering also lifts any limits on the number of lights that can be used on a mesh.
- When using the Mobile renderer, up to 8 omni lights and 8 spot lights can
be displayed per mesh resource. Baked lighting can be used to overcome this limit
if needed.
When using the Mobile renderer, up to 8 omni lights and 8 spot lights can
be displayed per mesh resource. Baked lighting can be used to overcome this limit
if needed.
Shadow mapping:
- DirectionalLight:Orthogonal (fastest), PSSM 2-split and 4-split.
Supports blending between splits.
DirectionalLight:Orthogonal (fastest), PSSM 2-split and 4-split.
Supports blending between splits.
- OmniLight:Dual paraboloid (fast) or cubemap (slower but more accurate).
Supports colored projector textures in the form of panoramas.
OmniLight:Dual paraboloid (fast) or cubemap (slower but more accurate).
Supports colored projector textures in the form of panoramas.
- SpotLight:Single texture. Supports colored projector textures.
SpotLight:Single texture. Supports colored projector textures.
- Shadow normal offset bias and shadow pancaking to decrease the amount of
visible shadow acne and peter-panning.
Shadow normal offset bias and shadow pancaking to decrease the amount of
visible shadow acne and peter-panning.
- PCSS-like shadow blur based on the
light size and distance from the surface the shadow is cast on.
PCSS-like shadow blur based on the
light size and distance from the surface the shadow is cast on.
- Adjustable shadow blur on a per-light basis.
Adjustable shadow blur on a per-light basis.
Global illumination with indirect lighting:
- Baked lightmaps(fast, but can't be updated at runtime).Supports baking indirect light only or baking both direct and indirect lighting.
The bake mode can be adjusted on a per-light basis to allow for hybrid light
baking setups.Supports lighting dynamic objects using automatic and manually placed probes.Optionally supports directional lighting and rough reflections based on spherical
harmonics.Lightmaps are baked on the GPU using compute shaders (much faster compared
to CPU lightmapping). Baking can only be performed from the editor,
not in exported projects.Supports GPU-baseddenoisingwith JNLM, or CPU/GPU-based denoising with OIDN.
Baked lightmaps(fast, but can't be updated at runtime).
> Supports baking indirect light only or baking both direct and indirect lighting.
The bake mode can be adjusted on a per-light basis to allow for hybrid light
baking setups.Supports lighting dynamic objects using automatic and manually placed probes.Optionally supports directional lighting and rough reflections based on spherical
harmonics.Lightmaps are baked on the GPU using compute shaders (much faster compared
to CPU lightmapping). Baking can only be performed from the editor,
not in exported projects.Supports GPU-baseddenoisingwith JNLM, or CPU/GPU-based denoising with OIDN.
- Supports baking indirect light only or baking both direct and indirect lighting.
The bake mode can be adjusted on a per-light basis to allow for hybrid light
baking setups.
Supports baking indirect light only or baking both direct and indirect lighting.
The bake mode can be adjusted on a per-light basis to allow for hybrid light
baking setups.
- Supports lighting dynamic objects using automatic and manually placed probes.
Supports lighting dynamic objects using automatic and manually placed probes.
- Optionally supports directional lighting and rough reflections based on spherical
harmonics.
Optionally supports directional lighting and rough reflections based on spherical
harmonics.
- Lightmaps are baked on the GPU using compute shaders (much faster compared
to CPU lightmapping). Baking can only be performed from the editor,
not in exported projects.
Lightmaps are baked on the GPU using compute shaders (much faster compared
to CPU lightmapping). Baking can only be performed from the editor,
not in exported projects.
- Supports GPU-baseddenoisingwith JNLM, or CPU/GPU-based denoising with OIDN.
Supports GPU-baseddenoisingwith JNLM, or CPU/GPU-based denoising with OIDN.
- Voxel-based GI probes. Supports
dynamic lightsanddynamic occluders, while also supporting reflections.
Requires a fast baking step which can be performed in the editor or at
runtime (including from an exported project).
Voxel-based GI probes. Supports
dynamic lightsanddynamic occluders, while also supporting reflections.
Requires a fast baking step which can be performed in the editor or at
runtime (including from an exported project).
- Signed-distance field GIdesigned for large open worlds.
Supports dynamic lights, but not dynamic occluders. Supports reflections.
No baking required.
Signed-distance field GIdesigned for large open worlds.
Supports dynamic lights, but not dynamic occluders. Supports reflections.
No baking required.
- Screen-space indirect lighting (SSIL)at half or full resolution. Fully real-time and supports any kind of emissive
light source (including decals).
Screen-space indirect lighting (SSIL)at half or full resolution. Fully real-time and supports any kind of emissive
light source (including decals).
- VoxelGI and SDFGI use a deferred pass to allow for rendering GI at half
resolution to improve performance (while still having functional MSAA support).
VoxelGI and SDFGI use a deferred pass to allow for rendering GI at half
resolution to improve performance (while still having functional MSAA support).
Reflections:
- Voxel-based reflections (when using GI probes) and SDF-based reflections
(when using signed distance field GI). Voxel-based reflections are visible
on transparent surfaces, while rough SDF-based reflections are visible
on transparent surfaces.
Voxel-based reflections (when using GI probes) and SDF-based reflections
(when using signed distance field GI). Voxel-based reflections are visible
on transparent surfaces, while rough SDF-based reflections are visible
on transparent surfaces.
- Fast baked reflections or slow real-time reflections using ReflectionProbe.
Parallax box correction can optionally be enabled.
Fast baked reflections or slow real-time reflections using ReflectionProbe.
Parallax box correction can optionally be enabled.
- Screen-space reflections with support for material roughness.
Screen-space reflections with support for material roughness.
- Reflection techniques can be mixed together for greater accuracy or scalability.
Reflection techniques can be mixed together for greater accuracy or scalability.
- When using the Forward+ renderer (default on desktop), reflection probes are
rendered with clustered forward optimizations to decrease their individual cost.
Clustered rendering also lifts any limits on the number of reflection probes that can be used on a mesh.
When using the Forward+ renderer (default on desktop), reflection probes are
rendered with clustered forward optimizations to decrease their individual cost.
Clustered rendering also lifts any limits on the number of reflection probes that can be used on a mesh.
- When using the Mobile renderer, up to 8 reflection probes can be displayed per mesh
resource. When using the Compatibility renderer, up to 2 reflection probes can
be displayed per mesh resource.
When using the Mobile renderer, up to 8 reflection probes can be displayed per mesh
resource. When using the Compatibility renderer, up to 2 reflection probes can
be displayed per mesh resource.
Decals:
- Supports albedo, emissive,ORM,
and normal mapping.
Supports albedo, emissive,ORM,
and normal mapping.
- Texture channels are smoothly overlaid on top of the underlying material,
with support for normal/ORM-only decals.
Texture channels are smoothly overlaid on top of the underlying material,
with support for normal/ORM-only decals.
- Support for normal fade to fade the decal depending on its incidence angle.
Support for normal fade to fade the decal depending on its incidence angle.
- Does not rely on runtime mesh generation. This means decals can be used on
complex skinned meshes with no performance penalty, even if the decal moves every frame.
Does not rely on runtime mesh generation. This means decals can be used on
complex skinned meshes with no performance penalty, even if the decal moves every frame.
- Support for nearest, bilinear, trilinear or anisotropic texture filtering (configured globally).
Support for nearest, bilinear, trilinear or anisotropic texture filtering (configured globally).
- Optional distance fade system to fade distant decals, improving performance.
Optional distance fade system to fade distant decals, improving performance.
- When using the Forward+ renderer (default on desktop), decals are
rendered with clustered forward optimizations to decrease their individual cost.
Clustered rendering also lifts any limits on the number of decals that can be used on a mesh.
When using the Forward+ renderer (default on desktop), decals are
rendered with clustered forward optimizations to decrease their individual cost.
Clustered rendering also lifts any limits on the number of decals that can be used on a mesh.
- When using the Mobile renderer, up to 8 decals can be displayed per mesh
resource.
When using the Mobile renderer, up to 8 decals can be displayed per mesh
resource.
Sky:
- Panorama sky (using an HDRI).
Panorama sky (using an HDRI).
- Procedural sky and Physically-based sky that respond to the DirectionalLights in the scene.
Procedural sky and Physically-based sky that respond to the DirectionalLights in the scene.
- Support forcustom sky shaders, which can be animated.
Support forcustom sky shaders, which can be animated.
- The radiance map used for ambient and specular light can be updated in
real-time depending on the quality settings chosen.
The radiance map used for ambient and specular light can be updated in
real-time depending on the quality settings chosen.
Fog:
- Exponential depth fog.
Exponential depth fog.
- Exponential height fog.
Exponential height fog.
- Support for automatic fog color depending on the sky color (aerial perspective).
Support for automatic fog color depending on the sky color (aerial perspective).
- Support for sun scattering in the fog.
Support for sun scattering in the fog.
- Support for controlling how much fog rendering should affect the sky, with
separate controls for traditional and volumetric fog.
Support for controlling how much fog rendering should affect the sky, with
separate controls for traditional and volumetric fog.
- Support for making specific materials ignore fog.
Support for making specific materials ignore fog.
Volumetric fog:
- Globalvolumetric fogthat reacts to lights and shadows.
Globalvolumetric fogthat reacts to lights and shadows.
- Volumetric fog can take indirect light into account when using VoxelGI or SDFGI.
Volumetric fog can take indirect light into account when using VoxelGI or SDFGI.
- Fog volume nodes that can be placed to add fog to specific areas (or remove fog from specific areas).
Supported shapes include box, ellipse, cone, cylinder, and 3D texture-based density maps.
Fog volume nodes that can be placed to add fog to specific areas (or remove fog from specific areas).
Supported shapes include box, ellipse, cone, cylinder, and 3D texture-based density maps.
- Each fog volume can have its own custom shader.
Each fog volume can have its own custom shader.
- Can be used together with traditional fog.
Can be used together with traditional fog.
Particles:
- GPU-based particles with support for subemitters (2D + 3D), trails (2D + 3D),
attractors (3D only) and collision (2D + 3D).3D particle attractor shapes supported: box, sphere and 3D vector fields.3D particle collision shapes supported: box, sphere, baked signed distance field
and real-time heightmap (suited for open world weather effects).2D particle collision is handled using a signed distance field generated in real-time
based onLightOccluder2Dnodes in the scene.Trails can use the built-in ribbon trail and tube trail meshes, or custom
meshes with skeletons.Support for custom particle shaders with manual emission.
GPU-based particles with support for subemitters (2D + 3D), trails (2D + 3D),
attractors (3D only) and collision (2D + 3D).
- 3D particle attractor shapes supported: box, sphere and 3D vector fields.
3D particle attractor shapes supported: box, sphere and 3D vector fields.
- 3D particle collision shapes supported: box, sphere, baked signed distance field
and real-time heightmap (suited for open world weather effects).
3D particle collision shapes supported: box, sphere, baked signed distance field
and real-time heightmap (suited for open world weather effects).
- 2D particle collision is handled using a signed distance field generated in real-time
based onLightOccluder2Dnodes in the scene.
2D particle collision is handled using a signed distance field generated in real-time
based onLightOccluder2Dnodes in the scene.
- Trails can use the built-in ribbon trail and tube trail meshes, or custom
meshes with skeletons.
Trails can use the built-in ribbon trail and tube trail meshes, or custom
meshes with skeletons.
- Support for custom particle shaders with manual emission.
Support for custom particle shaders with manual emission.
- CPU-based particles.
CPU-based particles.
Post-processing:
- Tonemapping (Linear, Reinhard, Filmic, ACES, AgX).
Tonemapping (Linear, Reinhard, Filmic, ACES, AgX).
- Automatic exposure adjustments based on viewport brightness (and manual exposure override).
Automatic exposure adjustments based on viewport brightness (and manual exposure override).
- Near and far depth of field with adjustable bokeh simulation (box, hexagon, circle).
Near and far depth of field with adjustable bokeh simulation (box, hexagon, circle).
- Screen-space ambient occlusion (SSAO) at half or full resolution.
Screen-space ambient occlusion (SSAO) at half or full resolution.
- Glow/bloom with optional bicubic upscaling and several blend modes available:
Screen, Soft Light, Add, Replace, Mix.
Glow/bloom with optional bicubic upscaling and several blend modes available:
Screen, Soft Light, Add, Replace, Mix.
- Glow can have a colored dirt map texture, acting as a lens dirt effect.
Glow can have a colored dirt map texture, acting as a lens dirt effect.
- Glow can beused as a screen-space blur effect.
Glow can beused as a screen-space blur effect.
- Color correction using a one-dimensional ramp or a 3D LUT texture.
Color correction using a one-dimensional ramp or a 3D LUT texture.
- Roughness limiter to reduce the impact of specular aliasing.
Roughness limiter to reduce the impact of specular aliasing.
- Brightness, contrast and saturation adjustments.
Brightness, contrast and saturation adjustments.
Texture filtering:
- Nearest, bilinear, trilinear or anisotropic filtering.
Nearest, bilinear, trilinear or anisotropic filtering.
- Filtering options are defined on a per-use basis, not a per-texture basis.
Filtering options are defined on a per-use basis, not a per-texture basis.
Texture compression:
- Basis Universal (slow, but results in smaller files).
Basis Universal (slow, but results in smaller files).
- BPTC for high-quality compression (not supported on macOS).
BPTC for high-quality compression (not supported on macOS).
- ETC2 (not supported on macOS).
ETC2 (not supported on macOS).
- S3TC (not supported on mobile/Web platforms).
S3TC (not supported on mobile/Web platforms).
Antialiasing:
- Temporalantialiasing(TAA).
Temporalantialiasing(TAA).
- AMD FidelityFX Super Resolution 2.2antialiasing(FSR2),
which can be used at native resolution as a form of high-quality temporal antialiasing.
AMD FidelityFX Super Resolution 2.2antialiasing(FSR2),
which can be used at native resolution as a form of high-quality temporal antialiasing.
- Multi-sample antialiasing (MSAA), for both2D antialiasingand3D antialiasing.
Multi-sample antialiasing (MSAA), for both2D antialiasingand3D antialiasing.
- Fast approximate antialiasing (FXAA).
Fast approximate antialiasing (FXAA).
- Super-sample antialiasing (SSAA) using bilinear 3D scaling and a 3D resolution scale above 1.0.
Super-sample antialiasing (SSAA) using bilinear 3D scaling and a 3D resolution scale above 1.0.
- Alpha antialiasing, MSAA alpha to coverage and alpha hashing on a per-material basis.
Alpha antialiasing, MSAA alpha to coverage and alpha hashing on a per-material basis.
Resolution scaling:
- Support forrendering 3D at a lower resolutionwhile keeping 2D rendering at the original scale. This can be used to improve
performance on low-end systems or improve visuals on high-end systems.
Support forrendering 3D at a lower resolutionwhile keeping 2D rendering at the original scale. This can be used to improve
performance on low-end systems or improve visuals on high-end systems.
- Resolution scaling uses bilinear filtering, AMD FidelityFX Super Resolution
1.0 (FSR1) or AMD FidelityFX Super Resolution 2.2 (FSR2).
Resolution scaling uses bilinear filtering, AMD FidelityFX Super Resolution
1.0 (FSR1) or AMD FidelityFX Super Resolution 2.2 (FSR2).
- Texture mipmap LOD bias is adjusted automatically to improve quality at lower
resolution scales. It can also be modified with a manual offset.
Texture mipmap LOD bias is adjusted automatically to improve quality at lower
resolution scales. It can also be modified with a manual offset.
Most effects listed above can be adjusted for better performance or to further
improve quality. This can be helpful whenusing Godot for offline rendering.

## 3D tools
- Built-in meshes: cube, cylinder/cone, (hemi)sphere, prism, plane, quad, torus, ribbon, tube.
Built-in meshes: cube, cylinder/cone, (hemi)sphere, prism, plane, quad, torus, ribbon, tube.
- GridMapsfor 3D tile-based level design.
GridMapsfor 3D tile-based level design.
- Constructive solid geometry(intended for prototyping).
Constructive solid geometry(intended for prototyping).
- Tools forprocedural geometry generation.
Tools forprocedural geometry generation.
- Path3D node to represent a path in 3D space.Can be drawn in the editor or generated procedurally.PathFollow3D node to make nodes follow a Path3D.
Path3D node to represent a path in 3D space.
> Can be drawn in the editor or generated procedurally.PathFollow3D node to make nodes follow a Path3D.
- Can be drawn in the editor or generated procedurally.
Can be drawn in the editor or generated procedurally.
- PathFollow3D node to make nodes follow a Path3D.
PathFollow3D node to make nodes follow a Path3D.
- 3D geometry helper class.
3D geometry helper class.
- Support for exporting the current scene as a glTF 2.0 file, both from the editor
and at runtime from an exported project.
Support for exporting the current scene as a glTF 2.0 file, both from the editor
and at runtime from an exported project.

## 3D physics
Physics bodies:
- Static bodies.
Static bodies.
- Animatable bodies (for objects moving only by script or animation, such as doors and platforms).
Animatable bodies (for objects moving only by script or animation, such as doors and platforms).
- Rigid bodies.
Rigid bodies.
- Character bodies.
Character bodies.
- Vehicle bodies (intended for arcade physics, not simulation).
Vehicle bodies (intended for arcade physics, not simulation).
- Joints.
Joints.
- Soft bodies.
Soft bodies.
- Ragdolls.
Ragdolls.
- Areas to detect bodies entering or leaving it.
Areas to detect bodies entering or leaving it.
Collision detection:
- Built-in shapes: cuboid, sphere, capsule, cylinder, world boundary (infinite plane).
Built-in shapes: cuboid, sphere, capsule, cylinder, world boundary (infinite plane).
- Generate triangle collision shapes for any mesh from the editor.
Generate triangle collision shapes for any mesh from the editor.
- Generate one or several convex collision shapes for any mesh from the editor.
Generate one or several convex collision shapes for any mesh from the editor.

## Shaders
- 2D:Custom vertex, fragment, and light shaders.
2D:Custom vertex, fragment, and light shaders.
- 3D:Custom vertex, fragment, light, and sky shaders.
3D:Custom vertex, fragment, light, and sky shaders.
- Text-based shaders using ashader language inspired by GLSL.
Text-based shaders using ashader language inspired by GLSL.
- Visual shader editor.Support forvisual shader plugins.
Visual shader editor.
> Support forvisual shader plugins.
- Support forvisual shader plugins.
Support forvisual shader plugins.

## Scripting
General:
- Object-oriented design pattern with scripts extending nodes.
Object-oriented design pattern with scripts extending nodes.
- Signals and groups for communicating between scripts.
Signals and groups for communicating between scripts.
- Support forcross-language scripting.
Support forcross-language scripting.
- Many 2D, 3D and 4D linear algebra data types such as vectors and transforms.
Many 2D, 3D and 4D linear algebra data types such as vectors and transforms.
GDScript:
- High-level interpreted languagewithoptional static typing.
High-level interpreted languagewithoptional static typing.
- Syntax inspired by Python. However, GDScript isnotbased on Python.
Syntax inspired by Python. However, GDScript isnotbased on Python.
- Syntax highlighting is provided on GitHub.
Syntax highlighting is provided on GitHub.
- Use threadsto perform asynchronous actions
or make use of multiple processor cores.
Use threadsto perform asynchronous actions
or make use of multiple processor cores.
- Packaged in a separate binary to keep file sizes and dependencies down.
Packaged in a separate binary to keep file sizes and dependencies down.
- Supports .NET 8 and higher.Full support for the C# 12.0 syntax and features.
Supports .NET 8 and higher.
> Full support for the C# 12.0 syntax and features.
- Full support for the C# 12.0 syntax and features.
Full support for the C# 12.0 syntax and features.
- Supports Windows, Linux, and macOS. Since Godot 4.2, experimental support for Android and iOS is also available.On the iOS platform only some architectures are supported:arm64.The web platform is currently unsupported. To use C# on that platform,
consider Godot 3 instead.
Supports Windows, Linux, and macOS. Since Godot 4.2, experimental support for Android and iOS is also available.
> On the iOS platform only some architectures are supported:arm64.The web platform is currently unsupported. To use C# on that platform,
consider Godot 3 instead.
- On the iOS platform only some architectures are supported:arm64.
On the iOS platform only some architectures are supported:arm64.
- The web platform is currently unsupported. To use C# on that platform,
consider Godot 3 instead.
The web platform is currently unsupported. To use C# on that platform,
consider Godot 3 instead.
- Using an external editor is recommended to benefit from IDE functionality.
Using an external editor is recommended to benefit from IDE functionality.
GDExtension (C, C++, Rust, D, ...):
- When you need it, link to native libraries for higher performance and third-party integrations.For scripting game logic, GDScript or C# are recommended if their
performance is suitable.
When you need it, link to native libraries for higher performance and third-party integrations.
> For scripting game logic, GDScript or C# are recommended if their
performance is suitable.
- For scripting game logic, GDScript or C# are recommended if their
performance is suitable.
For scripting game logic, GDScript or C# are recommended if their
performance is suitable.
- Official GDExtension bindings forCandC++.Use any build system and language features you wish.
Official GDExtension bindings forCandC++.
> Use any build system and language features you wish.
- Use any build system and language features you wish.
Use any build system and language features you wish.
- Actively developed GDExtension bindings forD,Swift, andRustbindings provided by the community. (Some of these bindings may be experimental and not production-ready).
Actively developed GDExtension bindings forD,Swift, andRustbindings provided by the community. (Some of these bindings may be experimental and not production-ready).

## Audio
Features:
- Mono, stereo, 5.1 and 7.1 output.
Mono, stereo, 5.1 and 7.1 output.
- Non-positional and positional playback in 2D and 3D.Optional Doppler effect in 2D and 3D.
Non-positional and positional playback in 2D and 3D.
> Optional Doppler effect in 2D and 3D.
- Optional Doppler effect in 2D and 3D.
Optional Doppler effect in 2D and 3D.
- Support for re-routableaudio busesand effects
with dozens of effects included.
Support for re-routableaudio busesand effects
with dozens of effects included.
- Support for polyphony (playing several sounds from a single AudioStreamPlayer node).
Support for polyphony (playing several sounds from a single AudioStreamPlayer node).
- Support for random volume and pitch.
Support for random volume and pitch.
- Support for real-time pitch scaling.
Support for real-time pitch scaling.
- Support for sequential/random sample selection, including repetition prevention
when using random sample selection.
Support for sequential/random sample selection, including repetition prevention
when using random sample selection.
- Listener2D and Listener3D nodes to listen from a position different than the camera.
Listener2D and Listener3D nodes to listen from a position different than the camera.
- Support forprocedural audio generation.
Support forprocedural audio generation.
- Audio input to record microphones.
Audio input to record microphones.
- Text to speechusing platform-provided TTS engines.
Text to speechusing platform-provided TTS engines.
- MIDI input.No support for MIDI output yet.
MIDI input.
> No support for MIDI output yet.
- No support for MIDI output yet.
No support for MIDI output yet.
APIs used:
- Windows:WASAPI.
Windows:WASAPI.
- macOS:CoreAudio.
macOS:CoreAudio.
- Linux:PulseAudio or ALSA.
Linux:PulseAudio or ALSA.

## Import
- Support forcustom import plugins.
Support forcustom import plugins.
Formats:
- Images:SeeImporting images.
Images:SeeImporting images.
- Audio:WAV with optional IMA-ADPCM compression.Ogg Vorbis.MP3.
Audio:
> WAV with optional IMA-ADPCM compression.Ogg Vorbis.MP3.
- WAV with optional IMA-ADPCM compression.
WAV with optional IMA-ADPCM compression.
- Ogg Vorbis.
Ogg Vorbis.
- MP3.
MP3.
- 3D scenes:SeeImporting 3D scenes.glTF 2.0(recommended)..blend(by calling Blender's glTF export functionality transparently).FBX (by callingFBX2glTFtransparently).Collada (.dae).Wavefront OBJ (static scenes only, can be loaded directly as a mesh or imported as a 3D scene).
3D scenes:SeeImporting 3D scenes.
> glTF 2.0(recommended)..blend(by calling Blender's glTF export functionality transparently).FBX (by callingFBX2glTFtransparently).Collada (.dae).Wavefront OBJ (static scenes only, can be loaded directly as a mesh or imported as a 3D scene).
- glTF 2.0(recommended).
glTF 2.0(recommended).
- .blend(by calling Blender's glTF export functionality transparently).
.blend(by calling Blender's glTF export functionality transparently).
- FBX (by callingFBX2glTFtransparently).
FBX (by callingFBX2glTFtransparently).
- Collada (.dae).
Collada (.dae).
- Wavefront OBJ (static scenes only, can be loaded directly as a mesh or imported as a 3D scene).
Wavefront OBJ (static scenes only, can be loaded directly as a mesh or imported as a 3D scene).
- Support for loading glTF 2.0 scenes at runtime, including from an exported project.
Support for loading glTF 2.0 scenes at runtime, including from an exported project.
- 3D meshes useMikktspaceto generate tangents
on import, which ensures consistency with other 3D applications such as Blender.
3D meshes useMikktspaceto generate tangents
on import, which ensures consistency with other 3D applications such as Blender.

## Input
- Input mapping systemusing hardcoded input events
or remappable input actions.Axis values can be mapped to two different actions with a configurable deadzone.Use the same code to support both keyboards and gamepads.
Input mapping systemusing hardcoded input events
or remappable input actions.
> Axis values can be mapped to two different actions with a configurable deadzone.Use the same code to support both keyboards and gamepads.
- Axis values can be mapped to two different actions with a configurable deadzone.
Axis values can be mapped to two different actions with a configurable deadzone.
- Use the same code to support both keyboards and gamepads.
Use the same code to support both keyboards and gamepads.
- Keyboard input.Keys can be mapped in "physical" mode to be independent of the keyboard layout.
Keyboard input.
> Keys can be mapped in "physical" mode to be independent of the keyboard layout.
- Keys can be mapped in "physical" mode to be independent of the keyboard layout.
Keys can be mapped in "physical" mode to be independent of the keyboard layout.
- Mouse input.The mouse cursor can be visible, hidden, captured or confined within the window.When captured, raw input will be used on Windows and Linux to
sidestep the OS' mouse acceleration settings.
Mouse input.
> The mouse cursor can be visible, hidden, captured or confined within the window.When captured, raw input will be used on Windows and Linux to
sidestep the OS' mouse acceleration settings.
- The mouse cursor can be visible, hidden, captured or confined within the window.
The mouse cursor can be visible, hidden, captured or confined within the window.
- When captured, raw input will be used on Windows and Linux to
sidestep the OS' mouse acceleration settings.
When captured, raw input will be used on Windows and Linux to
sidestep the OS' mouse acceleration settings.
- Gamepad input (up to 8 simultaneous controllers).
Gamepad input (up to 8 simultaneous controllers).
- Pen/tablet input with pressure support.
Pen/tablet input with pressure support.

## Navigation
- A* algorithm in2Dand3D.
A* algorithm in2Dand3D.
- Navigation meshes with dynamic obstacle avoidance in2Dand3D.
Navigation meshes with dynamic obstacle avoidance in2Dand3D.
- Generate navigation meshes from the editor or at runtime (including from an exported project).
Generate navigation meshes from the editor or at runtime (including from an exported project).

## Networking
- Low-level TCP networking usingStreamPeerandTCPServer.
Low-level TCP networking usingStreamPeerandTCPServer.
- Low-level UDP networking usingPacketPeerandUDPServer.
Low-level UDP networking usingPacketPeerandUDPServer.
- Low-level HTTP requests usingHTTPClient.
Low-level HTTP requests usingHTTPClient.
- High-level HTTP requests usingHTTPRequest.Supports HTTPS out of the box using bundled certificates.
High-level HTTP requests usingHTTPRequest.
> Supports HTTPS out of the box using bundled certificates.
- Supports HTTPS out of the box using bundled certificates.
Supports HTTPS out of the box using bundled certificates.
- High-level multiplayerAPI using UDP and ENet.Automatic replication using remote procedure calls (RPCs).Supports unreliable, reliable and ordered transfers.
High-level multiplayerAPI using UDP and ENet.
> Automatic replication using remote procedure calls (RPCs).Supports unreliable, reliable and ordered transfers.
- Automatic replication using remote procedure calls (RPCs).
Automatic replication using remote procedure calls (RPCs).
- Supports unreliable, reliable and ordered transfers.
Supports unreliable, reliable and ordered transfers.
- WebSocketclient and server, available on all platforms.
WebSocketclient and server, available on all platforms.
- WebRTCclient and server, available on all platforms.
WebRTCclient and server, available on all platforms.
- Support forUPnPto sidestep the requirement to forward ports
when hosting a server behind a NAT.
Support forUPnPto sidestep the requirement to forward ports
when hosting a server behind a NAT.

## Internationalization
- Full support for Unicode including emoji.
Full support for Unicode including emoji.
- Support for loading system fonts on Windows, macOS, and Linux.By default, system fonts are used as a fallback to display unsupported
characters. This allows proper display of multilingual text without
having to bundle large font files with a project.
Support for loading system fonts on Windows, macOS, and Linux.
- By default, system fonts are used as a fallback to display unsupported
characters. This allows proper display of multilingual text without
having to bundle large font files with a project.
By default, system fonts are used as a fallback to display unsupported
characters. This allows proper display of multilingual text without
having to bundle large font files with a project.
- Store localization strings usingCSVorgettext.Support for generating gettext POT and PO files from the editor.
Store localization strings usingCSVorgettext.
- Support for generating gettext POT and PO files from the editor.
Support for generating gettext POT and PO files from the editor.
- Use localized strings in your project automatically in GUI elements or by
using thetr()function.
Use localized strings in your project automatically in GUI elements or by
using thetr()function.
- Support for pluralization and translation contexts.
Support for pluralization and translation contexts.
- Support forbidirectional typesetting,
text shaping and OpenType localized forms.
Support forbidirectional typesetting,
text shaping and OpenType localized forms.
- Automatic UI mirroring for right-to-left locales.
Automatic UI mirroring for right-to-left locales.
- Support for pseudolocalization to test your project for i18n-friendliness.
Support for pseudolocalization to test your project for i18n-friendliness.

## Windowing and OS integration
- Spawn multiple independent windows within a single process.
Spawn multiple independent windows within a single process.
- Move, resize, minimize, and maximize windows spawned by the project.
Move, resize, minimize, and maximize windows spawned by the project.
- Change the window title and icon.
Change the window title and icon.
- Create transparent windows to use as overlays, with polygon-based
mouse passthrough support.
Create transparent windows to use as overlays, with polygon-based
mouse passthrough support.
- Request attention (will cause the title bar to blink on most platforms).
Request attention (will cause the title bar to blink on most platforms).
- Fullscreen mode.Uses borderless fullscreen by default on Windows for fast alt-tabbing,
but can optionally use exclusive fullscreen to reduce input lag.
Fullscreen mode.
> Uses borderless fullscreen by default on Windows for fast alt-tabbing,
but can optionally use exclusive fullscreen to reduce input lag.
- Uses borderless fullscreen by default on Windows for fast alt-tabbing,
but can optionally use exclusive fullscreen to reduce input lag.
Uses borderless fullscreen by default on Windows for fast alt-tabbing,
but can optionally use exclusive fullscreen to reduce input lag.
- Borderless windows (fullscreen or non-fullscreen).
Borderless windows (fullscreen or non-fullscreen).
- Keep a window always on top.
Keep a window always on top.
- Make a window ignore focus (useful for overlays).
Make a window ignore focus (useful for overlays).
- Declare a window as a popup (hidden from task switcher)
or exclusive (prevents interacting with other windows from the same process).
Declare a window as a popup (hidden from task switcher)
or exclusive (prevents interacting with other windows from the same process).
- Native file dialog support on Windows, macOS, Linux, and Android.
Native file dialog support on Windows, macOS, Linux, and Android.
- Tray icon support on Windows and macOS.
Tray icon support on Windows and macOS.
- Global menu integration on macOS.
Global menu integration on macOS.
- Client-side decorations on macOS.
Client-side decorations on macOS.
- Execute commands in a blocking or non-blocking manner (including running
multiple instances of the same project).
Execute commands in a blocking or non-blocking manner (including running
multiple instances of the same project).
- Open file paths and URLs using default or custom protocol handlers (if registered on the system).
Open file paths and URLs using default or custom protocol handlers (if registered on the system).
- Parse custom command line arguments.
Parse custom command line arguments.
- Support for screen readers on Windows, macOS, and Linux.
Support for screen readers on Windows, macOS, and Linux.
- Any Godot binary (editor or exported project) can beused as a headless serverby starting it with the--headlesscommand line argument.
This allows running the engine without a GPU or display server.
Any Godot binary (editor or exported project) can beused as a headless serverby starting it with the--headlesscommand line argument.
This allows running the engine without a GPU or display server.
See also
SeeCreating applicationsfor details on using these features.

## Mobile
- In-app purchases onAndroidandiOS.
In-app purchases onAndroidandiOS.
- Support for advertisements using third-party modules.
Support for advertisements using third-party modules.

## XR support (AR and VR)
- Out of the boxsupport for OpenXR.Including support for popular desktop headsets like the Valve Index, WMR headsets, and Quest over Link.
Out of the boxsupport for OpenXR.
> Including support for popular desktop headsets like the Valve Index, WMR headsets, and Quest over Link.
- Including support for popular desktop headsets like the Valve Index, WMR headsets, and Quest over Link.
Including support for popular desktop headsets like the Valve Index, WMR headsets, and Quest over Link.
- Support forAndroid-based headsetsusing OpenXR through a plugin.Including support for popular stand alone headsets like the Meta Quest 1/2/3 and Pro, Pico 4, Magic Leap 2, and Lynx R1.
Support forAndroid-based headsetsusing OpenXR through a plugin.
- Including support for popular stand alone headsets like the Meta Quest 1/2/3 and Pro, Pico 4, Magic Leap 2, and Lynx R1.
Including support for popular stand alone headsets like the Meta Quest 1/2/3 and Pro, Pico 4, Magic Leap 2, and Lynx R1.
- Out of the box limited support for visionOS Apple headsets.Currently only exporting an application for use on a flat plane within the
headset is supported. Immersive experiences are not supported.
Out of the box limited support for visionOS Apple headsets.
- Currently only exporting an application for use on a flat plane within the
headset is supported. Immersive experiences are not supported.
Currently only exporting an application for use on a flat plane within the
headset is supported. Immersive experiences are not supported.
- Other devices supported through an XR plugin structure.
Other devices supported through an XR plugin structure.
- Various advanced toolkits are available that implement common features required by XR applications.
Various advanced toolkits are available that implement common features required by XR applications.

## GUI system
Godot's GUI is built using the same Control nodes used to make games in Godot.
The editor UI can easily be extended in many ways using add-ons.
Nodes:
- Buttons.
Buttons.
- Checkboxes, check buttons, radio buttons.
Checkboxes, check buttons, radio buttons.
- Text entry usingLineEdit(single line) andTextEdit(multiple lines).
TextEdit also supports code editing features such as displaying line numbers
and syntax highlighting.
Text entry usingLineEdit(single line) andTextEdit(multiple lines).
TextEdit also supports code editing features such as displaying line numbers
and syntax highlighting.
- Dropdown menus usingPopupMenuandOptionButton.
Dropdown menus usingPopupMenuandOptionButton.
- Scrollbars.
Scrollbars.
- Labels.
Labels.
- RichTextLabel fortext formatted using BBCode,
with support for animated custom effects.
RichTextLabel fortext formatted using BBCode,
with support for animated custom effects.
- Trees (can also be used to represent tables).
Trees (can also be used to represent tables).
- Color picker with RGB and HSV modes.
Color picker with RGB and HSV modes.
- Controls can be rotated and scaled.
Controls can be rotated and scaled.
Sizing:
- Anchors to keep GUI elements in a specific corner, edge or centered.
Anchors to keep GUI elements in a specific corner, edge or centered.
- Containers to place GUI elements automatically following certain rules.Stacklayouts.Gridlayouts.Flowlayouts (similar to autowrapping text).Margin,centeredandaspect ratiolayouts.Draggable splitterlayouts.
Containers to place GUI elements automatically following certain rules.
> Stacklayouts.Gridlayouts.Flowlayouts (similar to autowrapping text).Margin,centeredandaspect ratiolayouts.Draggable splitterlayouts.
- Stacklayouts.
Stacklayouts.
- Gridlayouts.
Gridlayouts.
- Flowlayouts (similar to autowrapping text).
Flowlayouts (similar to autowrapping text).
- Margin,centeredandaspect ratiolayouts.
Margin,centeredandaspect ratiolayouts.
- Draggable splitterlayouts.
Draggable splitterlayouts.
- Scale tomultiple resolutionsusing thecanvas_itemsorviewportstretch modes.
Scale tomultiple resolutionsusing thecanvas_itemsorviewportstretch modes.
- Support any aspect ratio using anchors and theexpandstretch aspect.
Support any aspect ratio using anchors and theexpandstretch aspect.
Theming:
- Built-in theme editor.Generate a theme based on the current editor theme settings.
Built-in theme editor.
> Generate a theme based on the current editor theme settings.
- Generate a theme based on the current editor theme settings.
Generate a theme based on the current editor theme settings.
- Procedural vector-based theming usingStyleBoxFlat.Supports rounded/beveled corners, drop shadows, per-border widths and antialiasing.
Procedural vector-based theming usingStyleBoxFlat.
> Supports rounded/beveled corners, drop shadows, per-border widths and antialiasing.
- Supports rounded/beveled corners, drop shadows, per-border widths and antialiasing.
Supports rounded/beveled corners, drop shadows, per-border widths and antialiasing.
- Texture-based theming usingStyleBoxTexture.
Texture-based theming usingStyleBoxTexture.
Godot's small distribution size can make it a suitable alternative to frameworks
like Electron or Qt.

## Animation
- Direct kinematics and inverse kinematics.
Direct kinematics and inverse kinematics.
- Support for animating any property with customizable interpolation.
Support for animating any property with customizable interpolation.
- Support for calling methods in animation tracks.
Support for calling methods in animation tracks.
- Support for playing sounds in animation tracks.
Support for playing sounds in animation tracks.
- Support for Bézier curves in animation.
Support for Bézier curves in animation.

## File formats
- Scenes and resources can be saved intext-basedor binary formats.Text-based formats are human-readable and more friendly to version control.Binary formats are faster to save/load for large scenes/resources.
Scenes and resources can be saved intext-basedor binary formats.
> Text-based formats are human-readable and more friendly to version control.Binary formats are faster to save/load for large scenes/resources.
- Text-based formats are human-readable and more friendly to version control.
Text-based formats are human-readable and more friendly to version control.
- Binary formats are faster to save/load for large scenes/resources.
Binary formats are faster to save/load for large scenes/resources.
- Read and write text or binary files usingFileAccess.Can optionally be compressed or encrypted.
Read and write text or binary files usingFileAccess.
> Can optionally be compressed or encrypted.
- Can optionally be compressed or encrypted.
Can optionally be compressed or encrypted.
- Read and writeJSONfiles.
Read and writeJSONfiles.
- Read and write INI-style configuration files usingConfigFile.Can (de)serialize any Godot datatype, including Vector2/3, Color, ...
Read and write INI-style configuration files usingConfigFile.
> Can (de)serialize any Godot datatype, including Vector2/3, Color, ...
- Can (de)serialize any Godot datatype, including Vector2/3, Color, ...
Can (de)serialize any Godot datatype, including Vector2/3, Color, ...
- Read XML files usingXMLParser.
Read XML files usingXMLParser.
- Load and save images, audio/video, fonts and ZIP archivesin an exported project without having to go through Godot's import system.
Load and save images, audio/video, fonts and ZIP archivesin an exported project without having to go through Godot's import system.
- Pack game data into a PCK file (custom format optimized for fast seeking),
into a ZIP archive, or directly into the executable for single-file distribution.
Pack game data into a PCK file (custom format optimized for fast seeking),
into a ZIP archive, or directly into the executable for single-file distribution.
- Export additional PCK filesthat can be read
by the engine to support mods and DLCs.
Export additional PCK filesthat can be read
by the engine to support mods and DLCs.

## Miscellaneous
- Video playbackwith built-in support for Ogg Theora.
Video playbackwith built-in support for Ogg Theora.
- Movie Maker modeto record videos from a running
project with synchronized audio and perfect frame pacing.
Movie Maker modeto record videos from a running
project with synchronized audio and perfect frame pacing.
- Low-level access to serverswhich allows bypassing
the scene tree's overhead when needed.
Low-level access to serverswhich allows bypassing
the scene tree's overhead when needed.
- Command line interfacefor automation.Export and deploy projects using continuous integration platforms.Shell completion scriptsare available for Bash, zsh and fish.Print colored text to standard output on all platforms usingprint_rich.
Command line interfacefor automation.
> Export and deploy projects using continuous integration platforms.Shell completion scriptsare available for Bash, zsh and fish.Print colored text to standard output on all platforms usingprint_rich.
- Export and deploy projects using continuous integration platforms.
Export and deploy projects using continuous integration platforms.
- Shell completion scriptsare available for Bash, zsh and fish.
Shell completion scriptsare available for Bash, zsh and fish.
- Print colored text to standard output on all platforms usingprint_rich.
Print colored text to standard output on all platforms usingprint_rich.
- The editor candetect features used in a project and create a compilation profile,
which can be used to create smaller export template binaries
with unneeded features disabled.
The editor candetect features used in a project and create a compilation profile,
which can be used to create smaller export template binaries
with unneeded features disabled.
- Support forC++ modulesstatically linked
into the engine binary.Most built-in modules can be disabled at compile-time to reduce binary size
in custom builds. SeeOptimizing a build for sizefor details.
Support forC++ modulesstatically linked
into the engine binary.
- Most built-in modules can be disabled at compile-time to reduce binary size
in custom builds. SeeOptimizing a build for sizefor details.
Most built-in modules can be disabled at compile-time to reduce binary size
in custom builds. SeeOptimizing a build for sizefor details.
- Engine and editor written in C++17.Can becompiledusing GCC,
Clang and MSVC. MinGW is also supported.Friendly towards packagers. In most cases, system libraries can be used
instead of the ones provided by Godot. The build system doesn't download anything.
Builds can be fully reproducible.
Engine and editor written in C++17.
> Can becompiledusing GCC,
Clang and MSVC. MinGW is also supported.Friendly towards packagers. In most cases, system libraries can be used
instead of the ones provided by Godot. The build system doesn't download anything.
Builds can be fully reproducible.
- Can becompiledusing GCC,
Clang and MSVC. MinGW is also supported.
Can becompiledusing GCC,
Clang and MSVC. MinGW is also supported.
- Friendly towards packagers. In most cases, system libraries can be used
instead of the ones provided by Godot. The build system doesn't download anything.
Builds can be fully reproducible.
Friendly towards packagers. In most cases, system libraries can be used
instead of the ones provided by Godot. The build system doesn't download anything.
Builds can be fully reproducible.
- Licensed under the permissive MIT license.Open development process withcontributions welcome.
Licensed under the permissive MIT license.
> Open development process withcontributions welcome.
- Open development process withcontributions welcome.
Open development process withcontributions welcome.
See also
TheGodot proposals repositorylists features that have been requested by the community and may be implemented
in future Godot releases.