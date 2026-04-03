# Your first 3D shader

# Your first 3D shader

You have decided to start writing your own custom Spatial shader. Maybe you saw
a cool trick online that was done with shaders, or you have found that theStandardMaterial3Disn't quite meeting your
needs. Either way, you have decided to write your own and now you need to figure
out where to start.
This tutorial will explain how to write a Spatial shader and will cover more
topics than theCanvasItemtutorial.
Spatial shaders have more built-in functionality than CanvasItem shaders. The
expectation with spatial shaders is that Godot has already provided the
functionality for common use cases and all the user needs to do in the shader is
set the proper parameters. This is especially true for a PBR (physically based
rendering) workflow.
This is a two-part tutorial. In this first part we will create terrain using
vertex displacement from a heightmap in the
vertex function. In thesecond partwe
will take the concepts from this tutorial and set up
custom materials in a fragment shader by writing an ocean water shader.
Note
This tutorial assumes some basic shader knowledge such as types
(vec2,float,sampler2D), and functions. If you are
uncomfortable with these concepts it is best to get a gentle
introduction fromThe Book of Shadersbefore completing this tutorial.

## Where to assign my material

In 3D, objects are drawn usingMeshes. Meshes are a resource
type that store geometry (the shape of your object) and materials (the color and
how the object reacts to light) in units called "surfaces". A Mesh can have
multiple surfaces, or just one. Typically, you would import a mesh from another
program (e.g. Blender). But Godot also has a fewPrimitiveMeshesthat allow you to add basic geometry to a scene without
importing Meshes.
There are multiple node types that you can use to draw a mesh. The main one isMeshInstance3D, but you can also useGPUParticles3D,MultiMeshes(with aMultiMeshInstance3D), or others.
Typically, a material is associated with a given surface in a mesh, but some
nodes, like MeshInstance3D, allow you to override the material for a specific
surface, or for all surfaces.
If you set a material on the surface or mesh itself, then all MeshInstance3Ds that
share that mesh will share that material. However, if you want to reuse the same
mesh across multiple mesh instances, but have different materials for each
instance then you should set the material on the MeshInstance3D.
For this tutorial we will set our material on the mesh itself rather than taking
advantage of the MeshInstance3D's ability to override materials.

## Setting up

Add a newMeshInstance3Dnode to your scene.
In the inspector tab, set the MeshInstance3D'sMeshproperty to a newPlaneMeshresource, by clicking on<empty>and
choosingNew PlaneMesh. Then expand the resource by clicking on the image of
a plane that appears.
This adds a plane to our scene.
Then, in the viewport, click in the upper left corner on thePerspectivebutton.
In the menu that appears, selectDisplay Wireframe.
This will allow you to see the triangles making up the plane.
Now setSubdivide WidthandSubdivide Depthof thePlaneMeshto32.
You can see that there are now many more triangles in theMeshInstance3D. This will give us more vertices to work with
and thus allow us to add more detail.
PrimitiveMeshes, like PlaneMesh, only have one
surface, so instead of an array of materials there is only one. Set theMaterialto a new ShaderMaterial, then expand the material by clicking on
the sphere that appears.
Note
Materials that inherit from theMaterialresource, such asStandardMaterial3DandParticleProcessMaterial, can be converted to aShaderMaterialand their existing properties will be converted to an accompanying text shader.
To do so, right-click on the material in the FileSystem dock and chooseConvert to ShaderMaterial. You can also do so by right-clicking on any
property holding a reference to the material in the inspector.
Now set the material'sShaderto a new Shader by clicking<empty>and
selectNew Shader.... Leave the default settings, give your shader a name,
and clickCreate.
Click on the shader in the inspector, and the shader editor should now pop up. You
are ready to begin writing your first Spatial shader!

## Shader magic

The new shader is already generated with ashader_typevariable, thevertex()function, and thefragment()function. The first thing Godot
shaders need is a declaration of what type of shader they are. In this case theshader_typeis set tospatialbecause this is a spatial shader.

```
shader_type spatial;
```

Thevertex()function determines where the vertices of yourMeshInstance3Dappear in the final scene. We will be using it to offset the height of each vertex
and make our flat plane appear like a little terrain.
With nothing in thevertex()function, Godot will use its default vertex
shader. We can start to make changes by adding a single line:

```
void vertex() {
  VERTEX.y += cos(VERTEX.x) * sin(VERTEX.z);
}
```

Adding this line, you should get an image like the one below.
Okay, let's unpack this. Theyvalue of theVERTEXis being increased.
And we are passing thexandzcomponents of theVERTEXas arguments
tocos()andsin(); that gives
us a wave-like appearance across thexandzaxes.
What we want to achieve is the look of little hills; after all.cos()andsin()already look kind of like hills. We do so by scaling the inputs to thecos()andsin()functions.

```
void vertex() {
  VERTEX.y += cos(VERTEX.x * 4.0) * sin(VERTEX.z * 4.0);
}
```

This looks better, but it is still too spiky and repetitive, let's make it a
little more interesting.

## Noise heightmap

Noise is a very popular tool for faking the look of terrain. Think of it as
similar to the cosine function where you have repeating hills except, with
noise, each hill has a different height.
Godot provides theNoiseTexture2Dresource for
generating a noise texture that can be accessed from a shader.
To access a texture in a shader add the following code near the top of your
shader, outside thevertex()function.

```
uniform sampler2D noise;
```

This will allow you to send a noise texture to the shader. Now look in the
inspector under your material. You should see a section calledShader Parameters.
If you open it up, you'll see a parameter called "Noise".
Set thisNoiseparameter to a newNoiseTexture2D.
Then in your NoiseTexture2D, set itsNoiseproperty to a newFastNoiseLite. The FastNoiseLite class is used by
the NoiseTexture2D to generate a heightmap.
Once you set it up and should look like this.
Now, access the noise texture using thetexture()function:

```
void vertex() {
  float height = texture(noise, VERTEX.xz / 2.0 + 0.5).x;
  VERTEX.y += height;
}
```

texture()takes a texture as the first argument and
avec2for the position on the texture as the second argument. We use thexandzchannels ofVERTEXto determine where on the texture to look
up.
Since the PlaneMesh coordinates are within the[-1.0,1.0]range (for a size
of2.0), while the texture coordinates are within[0.0,1.0], to remap
the coordinates we divide by the size of the PlaneMesh by2.0and add0.5.
texture()returns avec4of ther,g,b,achannels at the position.
Since the noise texture is grayscale, all of the values are the same, so we can
use any one of the channels as the height. In this case we'll use ther, orxchannel.
Note
xyzwis the same asrgbain GLSL, so instead oftexture().xabove, we could usetexture().r. See theOpenGL documentationfor more
details.
Using this code you can see the texture creates random looking hills.
Right now it is too spiky, we want to soften the hills a bit. To do that, we
will use a uniform. You already used a uniform above to pass in the noise
texture, now let's learn how they work.

## Uniforms

Uniform variablesallow you to pass data
from the game into the shader. They are
very useful for controlling shader effects. Uniforms can be almost any datatype
that can be used in the shader. To use a uniform, you declare it in yourShaderusing the keyworduniform.
Let's make a uniform that changes the height of the terrain.

```
uniform float height_scale = 0.5;
```

Godot lets you initialize a uniform with a value; here,height_scaleis set
to0.5. You can set uniforms from GDScript by calling the functionset_shader_parameter()on the material corresponding to the shader. The value passed from GDScript
takes precedence over the value used to initialize it in the shader.

```
# called from the MeshInstance3D
mesh.material.set_shader_parameter("height_scale", 0.5)
```

Note
Changing uniforms in Spatial-based nodes is different from
CanvasItem-based nodes. Here, we set the material inside the PlaneMesh
resource. In other mesh resources you may need to first access the
material by callingsurface_get_material(). While in the
MeshInstance3D you would access the material usingget_surface_material()ormaterial_override.
Remember that the string passed intoset_shader_parameter()must match the name
of the uniform variable in the shader. You can use the
uniform variable anywhere inside your shader. Here, we will
use it to set the height value instead of arbitrarily multiplying by0.5.

```
VERTEX.y += height * height_scale;
```

Now it looks much better.
Using uniforms, we can even change the value every frame to animate the height
of the terrain. Combined withTweens, this can be
especially useful for animations.

## Interacting with light

First, turn wireframe off. To do so, open thePerspectivemenu in the
upper-left of the viewport again, and selectDisplay Normal. Additionally in
the 3D scene toolbar, turn off preview sunlight.
Note how the mesh color goes flat. This is because the lighting on it is flat.
Let's add a light!
First, we will add anOmniLight3Dto the scene, and
drag it up so it is above the terrain.
You can see the light affecting the terrain, but it looks odd. The problem is
the light is affecting the terrain as if it were a flat plane. This is because
the light shader uses the normals from theMeshto calculate
light.
The normals are stored in the Mesh, but we are changing the shape of the Mesh in
the shader, so the normals are no longer correct. To fix this, we can
recalculate the normals in the shader or use a normal texture that corresponds
to our noise. Godot makes both easy for us.
You can calculate the new normal manually in the vertex function and then just
setNORMAL. WithNORMALset, Godot will do all the difficult lighting
calculations for us. We will cover this method in the next part of this
tutorial, for now we will read normals from a texture.
Instead we will rely on the NoiseTexture again to calculate normals for us. We
do that by passing in a second noise texture.

```
uniform sampler2D normalmap;
```

Set this second uniform texture to anotherNoiseTexture2Dwith anotherFastNoiseLite. But this time, checkAs Normal Map.
When we have normals that correspond to a specific vertex we setNORMAL, but
if you have a normalmap that comes from a texture, set the normal usingNORMAL_MAPin thefragment()function. This way Godot will handle
wrapping the texture around the mesh automatically.
Lastly, in order to ensure that we are reading from the same places on the noise
texture and the normalmap texture, we are going to pass theVERTEX.xzposition from thevertex()function to thefragment()function. We do
that using avarying.
Above thevertex()define avaryingvec2calledtex_position. And
inside thevertex()function assignVERTEX.xztotex_position.

```
varying vec2 tex_position;

void vertex() {
  tex_position = VERTEX.xz / 2.0 + 0.5;
  float height = texture(noise, tex_position).x;
  VERTEX.y += height * height_scale;
}
```

And now we can accesstex_positionfrom thefragment()function.

```
void fragment() {
  NORMAL_MAP = texture(normalmap, tex_position).xyz;
}
```

With the normals in place the light now reacts to the height of the mesh
dynamically.
We can even drag the light around and the lighting will update automatically.

## Full code

Here is the full code for this tutorial. You can see it is not very long as
Godot handles most of the difficult stuff for you.

```
shader_type spatial;

uniform float height_scale = 0.5;
uniform sampler2D noise;
uniform sampler2D normalmap;

varying vec2 tex_position;

void vertex() {
  tex_position = VERTEX.xz / 2.0 + 0.5;
  float height = texture(noise, tex_position).x;
  VERTEX.y += height * height_scale;
}

void fragment() {
  NORMAL_MAP = texture(normalmap, tex_position).xyz;
}
```

That is everything for this part. Hopefully, you now understand the basics of
vertex shaders in Godot. In the next part of this tutorial we will write a
fragment function to accompany this vertex function and we will cover a more
advanced technique to turn this terrain into an ocean of moving waves.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
