# Using Viewports in English

# Using Viewports

## Introduction
Think of aViewportas a screen onto which the game is projected. In order
to see the game, we need to have a surface on which to draw it. That surface is
the Root Viewport.
SubViewportsare a kind of Viewport that can be added to the scene so that there
are multiple surfaces to draw on. When we are drawing to a SubViewport, we call it a render target. We can access the contents
of a render target by accessing its correspondingtexture.
By using a SubViewport as render target, we can either render multiple scenes simultaneously or we can render to
aViewportTexturewhich is applied to an object in the scene, for example a dynamic
skybox.
SubViewportshave a variety of use cases, including:
- Rendering 3D objects within a 2D game
Rendering 3D objects within a 2D game
- Rendering 2D elements in a 3D game
Rendering 2D elements in a 3D game
- Rendering dynamic textures
Rendering dynamic textures
- Generating procedural textures at runtime
Generating procedural textures at runtime
- Rendering multiple cameras in the same scene
Rendering multiple cameras in the same scene
What all these use cases have in common is that you are given the ability to
draw objects to a texture as if it were another screen and can then choose
what to do with the resulting texture.
Another kind of Viewports in Godot areWindows. They allow their content to be projected onto a window. While the Root Viewport is a Window, they are less
flexible. If you want to use the texture of a Viewport, you'll be working withSubViewportsmost of the time.

## Input
Viewportsare also responsible for delivering properly adjusted and
scaled input events to their children nodes. By defaultSubViewportsdon't
automatically receive input, unless they receive it from their directSubViewportContainerparent node. In this case, input can be
disabled with theDisable Inputproperty.
For more information on how Godot handles input, please read theInput Event Tutorial.

## Listener
Godot supports 3D sound (in both 2D and 3D nodes). More on this can be
found in theAudio Streams Tutorial. For this type of sound to be
audible, theViewportneeds to be enabled as a listener (for 2D or 3D).
If you are using aSubViewportto display yourWorld3DorWorld2D, don't forget to enable this!

## Cameras (2D & 3D)
When using aCamera3DorCamera2D, it will always display on the
closest parentViewport(going towards the root). For example, in the
following hierarchy:
CameraAwill display on the RootViewportand it will drawMeshA.CameraBwill be captured by theSubViewportalong withMeshB. Even thoughMeshBis in the scene
hierarchy, it will still not be drawn to the Root Viewport. Similarly,MeshAwill not
be visible from the SubViewport because SubViewports only
capture nodes below them in the hierarchy.
There can only be one active camera perViewport, so if there is more
than one, make sure that the desired one has thecurrentproperty set,
or make it the current camera by calling:
```
camera.make_current()
```
```
camera.MakeCurrent();
```
By default, cameras will render all objects in their world. In 3D, cameras can use theircull_maskproperty combined with theVisualInstance3D'slayerproperty to restrict which objects are rendered.

## Scale & stretching
SubViewportshave asizeproperty, which represents the size of the SubViewport
in pixels. For SubViewports which are children ofSubViewportContainers,
these values are overridden, but for all others, this sets their resolution.
It is also possible to scale the 2D content and make theSubViewportresolution
different from the one specified in size, by calling:
```
sub_viewport.set_size_2d_override(Vector2i(width, height)) # Custom size for 2D.
sub_viewport.set_size_2d_override_stretch(true) # Enable stretch for custom size.
```
```
subViewport.Size2DOverride = new Vector2I(width, height); // Custom size for 2D.
subViewport.Size2DOverrideStretch = true; // Enable stretch for custom size.
```
For information on scaling and stretching with the Root Viewport visit theMultiple Resolutions Tutorial

## Worlds
For 3D, aViewportwill contain aWorld3D. This
is basically the universe that links physics and rendering together.
Node3D-based nodes will register using the World3D of the closest Viewport.
By default, newly created Viewports do not contain a World3D but
use the same as their parent Viewport. The Root Viewport always contains a
World3D, which is the one objects are rendered to by default.
AWorld3Dcan
be set in aViewportusing theWorld 3Dproperty, that will separate
all children nodes of thisViewportand will prevent them from interacting with the parent
Viewport's World3D. This is especially useful in scenarios where, for
example, you might want to show a separate character in 3D imposed over
the game (like in StarCraft).
As a helper for situations where you want to createViewportsthat
display single objects and don't want to create aWorld3D, Viewport has
the option to use itsOwn World3D. This is useful when you want to
instance 3D characters or objects inWorld2D.
For 2D, eachViewportalways contains its ownWorld2D.
This suffices in most cases, but in case sharing them may be desired, it
is possible to do so by settingworld_2don the Viewport through code.
For an example of how this works, see the demo projects3D in 2Dand2D in 3Drespectively.

## Capture
It is possible to query a capture of theViewportcontents. For the Root
Viewport, this is effectively a screen capture. This is done with the
following code:
```
# Retrieve the captured Image using get_image().
var img = get_viewport().get_texture().get_image()
# Convert Image to ImageTexture.
var tex = ImageTexture.create_from_image(img)
# Set sprite texture.
sprite.texture = tex
```
```
// Retrieve the captured Image using get_image().
var img = GetViewport().GetTexture().GetImage();
// Convert Image to ImageTexture.
var tex = ImageTexture.CreateFromImage(img);
// Set sprite texture.
sprite.Texture = tex;
```
But if you use this in_ready()or from the first frame of theViewport'sinitialization,
you will get an empty texture because there is nothing to get as texture. You can deal with
it using (for example):
```
# Wait until the frame has finished before getting the texture.
await RenderingServer.frame_post_draw
# You can get the image after this.
```
```
// Wait until the frame has finished before getting the texture.
await ToSignal(RenderingServer.Singleton, RenderingServer.SignalName.FramePostDraw);
// You can get the image after this.
```

## Viewport Container
If theSubViewportis a child of aSubViewportContainer, it will become active and display anything it has inside. The layout looks like this:
TheSubViewportwill cover the area of its parentSubViewportContainercompletely
ifStretchis set totruein the SubViewportContainer.
Note
The size of theSubViewportContainercannot be smaller than the size of theSubViewport.

## Rendering
Due to the fact that theViewportis an entryway into another rendering surface, it exposes a few
rendering properties that can be different from the project settings. You can
choose to use a different level ofMSAAfor each Viewport. The default behavior isDisabled.
If you know that theViewportis only going to be used for 2D, you canDisable 3D. Godot will then
restrict how the Viewport is drawn.
Disabling 3D is slightly faster and uses less memory compared to enabled 3D. It's a good idea to disable 3D if your viewport doesn't render anything in 3D.
Note
If you need to render 3D shadows in the viewport, make sure to set the viewport'spositional_shadow_atlas_sizeproperty to a value higher than0.
Otherwise, shadows won't be rendered. By default, the equivalent project setting is set to4096on desktop platforms and2048on mobile platforms.
Godot also provides a way of customizing how everything is drawn insideViewportsusingDebug Draw.
Debug Draw allows you to specify a mode which determines how the Viewport will display things drawn
inside it. Debug Draw isDisabledby default. Some other options areUnshaded,Overdraw, andWireframe. For a full list, refer to theViewport Documentation.
- Debug Draw = Disabled(default): The scene is drawn normally.
Debug Draw = Disabled(default): The scene is drawn normally.
- Debug Draw = Unshaded: Unshaded draws the scene without using lighting information so all the objects appear flatly colored in their albedo color.
Debug Draw = Unshaded: Unshaded draws the scene without using lighting information so all the objects appear flatly colored in their albedo color.
- Debug Draw = Overdraw: Overdraw draws the meshes semi-transparent with an additive blend so you can see how the meshes overlap.
Debug Draw = Overdraw: Overdraw draws the meshes semi-transparent with an additive blend so you can see how the meshes overlap.
- Debug Draw = Wireframe: Wireframe draws the scene using only the edges of triangles in the meshes.
Debug Draw = Wireframe: Wireframe draws the scene using only the edges of triangles in the meshes.
Note
Debug Draw modes are currentlynotsupported when using the
Compatibility rendering method. They will appear as regular draw modes.

## Render target
When rendering to aSubViewport, whatever is inside will not be
visible in the scene editor. To display the contents, you have to draw the SubViewport'sViewportTexturesomewhere.
This can be requested via code using (for example):
```
# This gives us the ViewportTexture.
var tex = viewport.get_texture()
sprite.texture = tex
```
```
// This gives us the ViewportTexture.
var tex = viewport.GetTexture();
sprite.Texture = tex;
```
Or it can be assigned in the editor by selecting "New ViewportTexture"
and then selecting theViewportyou want to use.
Every frame, theViewport'stexture is cleared away with the default clear color (or a transparent
color ifTransparent BGis set totrue). This can be changed by settingClear ModetoNeverorNextFrame.
As the name implies, Never means the texture will never be cleared, while next frame will
clear the texture on the next frame and then set itself to Never.
By default, re-rendering of theSubViewporthappens when
itsViewportTexturehas been drawn in a frame. If visible, it will be
rendered, otherwise, it will not. This behavior can be changed by settingUpdate ModetoNever,Once,Always, orWhenParentVisible.
Never and Always will never or always re-render respectively. Once will re-render the next frame and change to Never afterwards. This can be used to manually update the Viewport.
This flexibility allows users to render an image once and then use the texture without incurring the cost of rendering every frame.
Note
Make sure to check the Viewport demos. They are available in the
viewport folder of the demos archive, or athttps://github.com/godotengine/godot-demo-projects/tree/master/viewport.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.