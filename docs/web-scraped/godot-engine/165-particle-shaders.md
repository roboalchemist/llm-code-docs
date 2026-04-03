# Particle shaders

# Particle shaders
Particle shaders are a special type of shader that runs before the object is
drawn. They are used for calculating material properties such as color,
position, and rotation. They can be drawn with any regular material for CanvasItem
or Spatial, depending on whether they are 2D or 3D.
Particle shaders are unique because they are not used to draw the object itself;
they are used to calculate particle properties, which are then used by aCanvasItemorSpatialshader. They contain two processor functions:start()andprocess().
Unlike other shader types, particle shaders keep the data that was output the
previous frame. Therefore, particle shaders can be used for complex effects that
take place over multiple frames.
Note
Particle shaders are only available with GPU-based particle nodes
(GPUParticles2DandGPUParticles3D).
CPU-based particle nodes (CPUParticles2DandCPUParticles3D) arerenderedon the GPU (which means they can
use custom CanvasItem or Spatial shaders), but their motion issimulatedon the CPU.

## Render modes

| Render mode | Description |
|---|---|
| keep_data | Do not clear previous data on restart. |
| disable_force | Disable attractor force. |
| disable_velocity | IgnoreVELOCITYvalue. |
| collision_use_scale | Scale the particle's size for collisions. |

Render mode
Description
keep_data
Do not clear previous data on restart.
disable_force
Disable attractor force.
disable_velocity
IgnoreVELOCITYvalue.
collision_use_scale
Scale the particle's size for collisions.

## Built-ins
Values marked asinare read-only. Values marked asoutcan optionally be written to and will
not necessarily contain sensible values. Values marked asinoutprovide a sensible default
value, and can optionally be written to. Samplers cannot be written to so they are not marked.

## Global built-ins
Global built-ins are available everywhere, including custom functions.

| Built-in | Description |
|---|---|
| in floatTIME | Global time since the engine has started, in seconds. It repeats after every3,600seconds (which can be changed with therolloversetting). It's affected bytime_scalebut not by pausing. If you need aTIMEvariable that is not affected by time scale, add your ownglobal shader uniformand update it each
frame. |
| in floatPI | APIconstant (3.141592).
The ratio of a circle's circumference to its diameter and the number of radians in a half turn. |
| in floatTAU | ATAUconstant (6.283185).
Equivalent toPI*2and the number of radians in a full turn. |
| in floatE | AnEconstant (2.718281). Euler's number, the base of the natural logarithm. |

Built-in
Description
in floatTIME
Global time since the engine has started, in seconds. It repeats after every3,600seconds (which can be changed with therolloversetting). It's affected bytime_scalebut not by pausing. If you need aTIMEvariable that is not affected by time scale, add your ownglobal shader uniformand update it each
frame.
in floatPI
APIconstant (3.141592).
The ratio of a circle's circumference to its diameter and the number of radians in a half turn.
in floatTAU
ATAUconstant (6.283185).
Equivalent toPI*2and the number of radians in a full turn.
in floatE
AnEconstant (2.718281). Euler's number, the base of the natural logarithm.

## Start and Process built-ins
These properties can be accessed from both thestart()andprocess()functions.

| Function | Description |
|---|---|
| in floatLIFETIME | Particle lifetime. |
| in floatDELTA | Delta process time. |
| in uintNUMBER | Unique number since emission start. |
| in uintINDEX | Particle index (from total particles). |
| in mat4EMISSION_TRANSFORM | Emitter transform (used for non-local systems). |
| in uintRANDOM_SEED | Random seed used as base for random. |
| inout boolACTIVE | truewhen the particle is active, can be set tofalse. |
| inout vec4COLOR | Particle color, can be written to and accessed in the mesh's vertex function. |
| inout vec3VELOCITY | Particle velocity, can be modified. |
| inout mat4TRANSFORM | Particle transform. |
| inout vec4CUSTOM | Custom particle data. Accessible from the mesh's shader asINSTANCE_CUSTOM. |
| inout floatMASS | Particle mass, intended to be used with attractors.1.0by default. |
| in vec4USERDATAX | Vector that enables the integration of supplementary user-defined data into the particle process shader.USERDATAXare six built-ins identified by number,Xcan be numbers between 1 and 6, for exampleUSERDATA3. |
| in uintFLAG_EMIT_POSITION | A flag for the last argument of theemit_subparticle()function to assign a position to a new particle's transform. |
| in uintFLAG_EMIT_ROT_SCALE | A flag for the last argument of theemit_subparticle()function to assign a rotation and scale to a new particle's transform. |
| in uintFLAG_EMIT_VELOCITY | A flag for the last argument of theemit_subparticle()function to assign a velocity to a new particle. |
| in uintFLAG_EMIT_COLOR | A flag for the last argument of theemit_subparticle()function to assign a color to a new particle. |
| in uintFLAG_EMIT_CUSTOM | A flag for the last argument of theemit_subparticle()function to assign a custom data vector to a new particle. |
| in vec3EMITTER_VELOCITY | Velocity of theParticles2D(3D) node. |
| in floatINTERPOLATE_TO_END | Value of theinterp_to_end(3D) property of the Particles node. |
| in uintAMOUNT_RATIO | Value of theamount_ratio(3D) property of the Particles node. |

Function
Description
in floatLIFETIME
Particle lifetime.
in floatDELTA
Delta process time.
in uintNUMBER
Unique number since emission start.
in uintINDEX
Particle index (from total particles).
in mat4EMISSION_TRANSFORM
Emitter transform (used for non-local systems).
in uintRANDOM_SEED
Random seed used as base for random.
inout boolACTIVE
truewhen the particle is active, can be set tofalse.
inout vec4COLOR
Particle color, can be written to and accessed in the mesh's vertex function.
inout vec3VELOCITY
Particle velocity, can be modified.
inout mat4TRANSFORM
Particle transform.
inout vec4CUSTOM
Custom particle data. Accessible from the mesh's shader asINSTANCE_CUSTOM.
inout floatMASS
Particle mass, intended to be used with attractors.1.0by default.
in vec4USERDATAX
Vector that enables the integration of supplementary user-defined data into the particle process shader.USERDATAXare six built-ins identified by number,Xcan be numbers between 1 and 6, for exampleUSERDATA3.
in uintFLAG_EMIT_POSITION
A flag for the last argument of theemit_subparticle()function to assign a position to a new particle's transform.
in uintFLAG_EMIT_ROT_SCALE
A flag for the last argument of theemit_subparticle()function to assign a rotation and scale to a new particle's transform.
in uintFLAG_EMIT_VELOCITY
A flag for the last argument of theemit_subparticle()function to assign a velocity to a new particle.
in uintFLAG_EMIT_COLOR
A flag for the last argument of theemit_subparticle()function to assign a color to a new particle.
in uintFLAG_EMIT_CUSTOM
A flag for the last argument of theemit_subparticle()function to assign a custom data vector to a new particle.
in vec3EMITTER_VELOCITY
Velocity of theParticles2D(3D) node.
in floatINTERPOLATE_TO_END
Value of theinterp_to_end(3D) property of the Particles node.
in uintAMOUNT_RATIO
Value of theamount_ratio(3D) property of the Particles node.
Note
In order to use theCOLORvariable in a StandardMaterial3D, setvertex_color_use_as_albedototrue. In a ShaderMaterial, access it with theCOLORvariable.

## Start built-ins

| Built-in | Description |
|---|---|
| in boolRESTART_POSITION | trueif particle is restarted, or emitted without a custom position (i.e. this particle was created byemit_subparticle()without theFLAG_EMIT_POSITIONflag). |
| in boolRESTART_ROT_SCALE | trueif particle is restarted, or emitted without a custom rotation or scale (i.e. this particle was created byemit_subparticle()without theFLAG_EMIT_ROT_SCALEflag). |
| in boolRESTART_VELOCITY | trueif particle is restarted, or emitted without a custom velocity (i.e. this particle was created byemit_subparticle()without theFLAG_EMIT_VELOCITYflag). |
| in boolRESTART_COLOR | trueif particle is restarted, or emitted without a custom color (i.e. this particle was created byemit_subparticle()without theFLAG_EMIT_COLORflag). |
| in boolRESTART_CUSTOM | trueif particle is restarted, or emitted without a custom property (i.e. this particle was created byemit_subparticle()without theFLAG_EMIT_CUSTOMflag). |

Built-in
Description
in boolRESTART_POSITION
trueif particle is restarted, or emitted without a custom position (i.e. this particle was created byemit_subparticle()without theFLAG_EMIT_POSITIONflag).
in boolRESTART_ROT_SCALE
trueif particle is restarted, or emitted without a custom rotation or scale (i.e. this particle was created byemit_subparticle()without theFLAG_EMIT_ROT_SCALEflag).
in boolRESTART_VELOCITY
trueif particle is restarted, or emitted without a custom velocity (i.e. this particle was created byemit_subparticle()without theFLAG_EMIT_VELOCITYflag).
in boolRESTART_COLOR
trueif particle is restarted, or emitted without a custom color (i.e. this particle was created byemit_subparticle()without theFLAG_EMIT_COLORflag).
in boolRESTART_CUSTOM
trueif particle is restarted, or emitted without a custom property (i.e. this particle was created byemit_subparticle()without theFLAG_EMIT_CUSTOMflag).

## Process built-ins

| Built-in | Description |
|---|---|
| in boolRESTART | trueif the current process frame is the first for the particle. |
| in boolCOLLIDED | truewhen the particle has collided with a particle collider. |
| in vec3COLLISION_NORMAL | A normal of the last collision. If there is no collision detected it is equal to(0.0,0.0,0.0). |
| in floatCOLLISION_DEPTH | A length of the normal of the last collision. If there is no collision detected it is equal to0.0. |
| in vec3ATTRACTOR_FORCE | A combined force of the attractors at the moment on that particle. |

Built-in
Description
in boolRESTART
trueif the current process frame is the first for the particle.
in boolCOLLIDED
truewhen the particle has collided with a particle collider.
in vec3COLLISION_NORMAL
A normal of the last collision. If there is no collision detected it is equal to(0.0,0.0,0.0).
in floatCOLLISION_DEPTH
A length of the normal of the last collision. If there is no collision detected it is equal to0.0.
in vec3ATTRACTOR_FORCE
A combined force of the attractors at the moment on that particle.

## Process functions
emit_subparticle()is currently the only custom function supported by
particle shaders. It allows users to add a new particle with specified
parameters from a sub-emitter. The newly created particle will only use the
properties that match theflagsparameter. For example, the
following code will emit a particle with a specified position, velocity, and
color, but unspecified rotation, scale, and custom value:
```
mat4 custom_transform = mat4(1.0);
custom_transform[3].xyz = vec3(10.5, 0.0, 4.0);
emit_subparticle(custom_transform, vec3(1.0, 0.5, 1.0), vec4(1.0, 0.0, 0.0, 1.0), vec4(1.0), FLAG_EMIT_POSITION | FLAG_EMIT_VELOCITY | FLAG_EMIT_COLOR);
```

| Function | Description |
|---|---|
| boolemit_subparticle(mat4 xform, vec3 velocity, vec4 color, vec4 custom, uint flags) | Emits a particle from a sub-emitter. |

Function
Description
boolemit_subparticle(mat4 xform, vec3 velocity, vec4 color, vec4 custom, uint flags)
Emits a particle from a sub-emitter.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.