# Converting GLSL to Godot shaders in English

# Converting GLSL to Godot shaders
This document explains the differences between Godot's shading language and GLSL
and gives practical advice on how to migrate shaders from other sources, such as
Shadertoy and The Book of Shaders, into Godot shaders.
For detailed information on Godot's shading language, please refer to theShading Languagereference.

## GLSL
Godot uses a shading language based on GLSL with the addition of a few
quality-of-life features. Accordingly, most features available in GLSL are
available in Godot's shading language.

### Shader programs
In GLSL, each shader uses a separate program. You have one program for the
vertex shader and one for the fragment shader. In Godot, you have a single
shader that contains avertexand/or afragmentfunction. If you only
choose to write one, Godot will supply the other.
Godot allows uniform variables and functions to be shared by defining the
fragment and vertex shaders in one file. In GLSL, the vertex and fragment
programs cannot share variables except when varyings are used.

### Vertex attributes
In GLSL, you can pass in per-vertex information using attributes and have the
flexibility to pass in as much or as little as you want. In Godot, you have a
set number of input attributes, includingVERTEX(position),COLOR,UV,UV2,NORMAL. Each shaders' page in the shader reference section
of the documentation comes with a complete list of its vertex attributes.

### gl_Position
gl_Positionreceives the final position of a vertex specified in the vertex
shader. It is specified by the user in clip space. Typically, in GLSL, the model
space vertex position is passed in using a vertex attribute calledpositionand you handle the conversion from model space to clip space manually.
In Godot,VERTEXspecifies the vertex position in model space at the
beginning of thevertexfunction. Godot also handles the final conversion to
clip space after the user-definedvertexfunction is run. If you want to
skip the conversion from model to view space, you can set therender_modetoskip_vertex_transform. If you want to skip all transforms, setrender_modetoskip_vertex_transformand set thePROJECTION_MATRIXtomat4(1.0)in order to nullify the final transform from view space to clip
space.

### Varyings
Varyings are a type of variable that can be passed from the vertex shader to the
fragment shader. In modern GLSL (3.0 and up), varyings are defined with theinandoutkeywords. A variable going out of the vertex shader is
defined withoutin the vertex shader andininside the fragment shader.

### Main
In GLSL, each shader program looks like a self-contained C-style program.
Accordingly, the main entry point ismain. If you are copying a vertex
shader, renamemaintovertexand if you are copying a fragment shader,
renamemaintofragment.

### Macros
TheGodot shader preprocessorsupports the following macros:
- #define/#undef
#define/#undef
- #if,#elif,#else,#endif,defined(),#ifdef,#ifndef
#if,#elif,#else,#endif,defined(),#ifdef,#ifndef
- #include(only.gdshaderincfiles and with a maximum depth of 25)
#include(only.gdshaderincfiles and with a maximum depth of 25)
- #pragmadisable_preprocessor, which disables preprocessing for the rest of the file
#pragmadisable_preprocessor, which disables preprocessing for the rest of the file

### Variables
GLSL has many built-in variables that are hard-coded. These variables are not
uniforms, so they are not editable from the main program.

| Variable | Type | Equivalent | Description |
|---|---|---|---|
| gl_FragColor | out vec4 | COLOR | Output color for each pixel. |
| gl_FragCoord | vec4 | FRAGCOORD | For full screen quads. For smaller quads, use UV. |
| gl_Position | vec4 | VERTEX | Position of Vertex, output from Vertex Shader. |
| gl_PointSize | float | POINT_SIZE | Size of Point primitive. |
| gl_PointCoord | vec2 | POINT_COORD | Position on point when drawing Point primitives. |
| gl_FrontFacing | bool | FRONT_FACING | True if front face of primitive. |

Variable
Type
Equivalent
Description
gl_FragColor
out vec4
COLOR
Output color for each pixel.
gl_FragCoord
vec4
FRAGCOORD
For full screen quads. For smaller quads, use UV.
gl_Position
vec4
VERTEX
Position of Vertex, output from Vertex Shader.
gl_PointSize
float
POINT_SIZE
Size of Point primitive.
gl_PointCoord
vec2
POINT_COORD
Position on point when drawing Point primitives.
gl_FrontFacing
bool
FRONT_FACING
True if front face of primitive.

### Coordinates
gl_FragCoordin GLSL andFRAGCOORDin the Godot shading language use the
same coordinate system. If using UV in Godot, the y-coordinate will be flipped
upside down.

### Precision
In GLSL, you can define the precision of a given type (float or int) at the top
of the shader with theprecisionkeyword. In Godot, you can set the
precision of individual variables as you need by placing precision qualifierslowp,mediump, andhighpbefore the type when defining the variable.
For more information, see theShading Languagereference.

## Shadertoy
Shadertoyis a website that makes it easy to write fragment shaders and
createpure magic.
Shadertoy does not give the user full control over the shader. It handles all
the input and uniforms and only lets the user write the fragment shader.

### Types
Shadertoy uses the webgl spec, so it runs a slightly different version of GLSL.
However, it still has the regular types, including constants and macros.

### mainImage
The main point of entry to a Shadertoy shader is themainImagefunction.mainImagehas two parameters,fragColorandfragCoord, which
correspond toCOLORandFRAGCOORDin Godot, respectively. These
parameters are handled automatically in Godot, so you do not need to include
them as parameters yourself. Anything in themainImagefunction should be
copied into thefragmentfunction when porting to Godot.

### Variables
In order to make writing fragment shaders straightforward and easy, Shadertoy
handles passing a lot of helpful information from the main program into the
fragment shader for you. A few of these have no equivalents in Godot because
Godot has chosen not to make them available by default. This is okay because
Godot gives you the ability to make your own uniforms. For variables whose
equivalents are listed as "Provide with Uniform", users are responsible for
creating that uniform themselves. The description gives the reader a hint about
what they can pass in as a substitute.

| Variable | Type | Equivalent | Description |
|---|---|---|---|
| fragColor | out vec4 | COLOR | Output color for each pixel. |
| fragCoord | vec2 | FRAGCOORD.xy | For full screen quads. For smaller quads, use UV. |
| iResolution | vec3 | 1.0 / SCREEN_PIXEL_SIZE | Can also pass in manually. |
| iTime | float | TIME | Time since shader started. |
| iTimeDelta | float | Provide with Uniform | Time to render previous frame. |
| iFrame | float | Provide with Uniform | Frame number. |
| iChannelTime[4] | float | Provide with Uniform | Time since that particular texture started. |
| iMouse | vec4 | Provide with Uniform | Mouse position in pixel coordinates. |
| iDate | vec4 | Provide with Uniform | Current date, expressed in seconds. |
| iChannelResolution[4] | vec3 | 1.0 / TEXTURE_PIXEL_SIZE | Resolution of particular texture. |
| iChanneli | Sampler2D | TEXTURE | Godot provides only one built-in; user can make more. |

Variable
Type
Equivalent
Description
fragColor
out vec4
COLOR
Output color for each pixel.
fragCoord
vec2
FRAGCOORD.xy
For full screen quads. For smaller quads, use UV.
iResolution
vec3
1.0 / SCREEN_PIXEL_SIZE
Can also pass in manually.
iTime
float
TIME
Time since shader started.
iTimeDelta
float
Provide with Uniform
Time to render previous frame.
iFrame
float
Provide with Uniform
Frame number.
iChannelTime[4]
float
Provide with Uniform
Time since that particular texture started.
iMouse
vec4
Provide with Uniform
Mouse position in pixel coordinates.
iDate
vec4
Provide with Uniform
Current date, expressed in seconds.
iChannelResolution[4]
vec3
1.0 / TEXTURE_PIXEL_SIZE
Resolution of particular texture.
iChanneli
Sampler2D
TEXTURE
Godot provides only one built-in; user can make more.

### Coordinates
fragCoordbehaves the same asgl_FragCoordinGLSLandFRAGCOORDin Godot.

## The Book of Shaders
Similar to Shadertoy,The Book of Shadersprovides access to a fragment shader in the web browser, with which the user may
interact. The user is restricted to writing fragment shader code with a set list
of uniforms passed in and with no ability to add additional uniforms.
For further help on porting shaders to various frameworks generally, The Book of
Shaders provides apageon running shaders
in various frameworks.

### Types
The Book of Shaders uses the webgl spec, so it runs a slightly different version
of GLSL. However, it still has the regular types, including constants and
macros.

### Main
The entry point for a Book of Shaders fragment shader ismain, just like in
GLSL. Everything written in a Book of Shadersmainfunction should be copied
into Godot'sfragmentfunction.

### Variables
The Book of Shaders sticks closer to plain GLSL than Shadertoy does. It also
implements fewer uniforms than Shadertoy.

| Variable | Type | Equivalent | Description |
|---|---|---|---|
| gl_FragColor | out vec4 | COLOR | Output color for each pixel. |
| gl_FragCoord | vec4 | FRAGCOORD | For full screen quads. For smaller quads, use UV. |
| u_resolution | vec2 | 1.0 / SCREEN_PIXEL_SIZE | Can also pass in manually. |
| u_time | float | TIME | Time since shader started. |
| u_mouse | vec2 | Provide with Uniform | Mouse position in pixel coordinates. |

Variable
Type
Equivalent
Description
gl_FragColor
out vec4
COLOR
Output color for each pixel.
gl_FragCoord
vec4
FRAGCOORD
For full screen quads. For smaller quads, use UV.
u_resolution
vec2
1.0 / SCREEN_PIXEL_SIZE
Can also pass in manually.
u_time
float
TIME
Time since shader started.
u_mouse
vec2
Provide with Uniform
Mouse position in pixel coordinates.

### Coordinates
The Book of Shaders uses the same coordinate system asGLSL.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.