# 3D text in English

# 3D text

## Introduction

In a project, there may be times when text needs to be created as part of a 3D
scene and not just in the HUD. Godot provides 2 methods to do this: the
Label3D node and the TextMeshresourcefor a MeshInstance3D node.
Additionally, Godot makes it possible to position Control nodes according to a
3D point's position on the camera. This can be used as an alternative to "true"
3D text in situations where Label3D and TextMesh aren't flexible enough.
See also
You can see 3D text in action using the3D Labels and Texts demo project.
This page doesnotcover how to display a GUI scene within a 3D
environment. For information on how to achieve that, see theGUI in 3Ddemo project.

## Label3D

Label3D behaves like a Label node, but in 3D space. Unlike the Label node, this
Label3D node doesnotinherit properties of a GUI theme. However, its look
remains customizable and uses the same font subresource as Control nodes
(including support forMSDFfont
rendering).

### Advantages

- Label3D is faster to generate than TextMesh. While both use a caching
mechanism to only render new glyphs once, Label3D will still be faster to
(re)generate, especially for long text. This can avoid stuttering during
gameplay on low-end CPUs or mobile.
Label3D is faster to generate than TextMesh. While both use a caching
mechanism to only render new glyphs once, Label3D will still be faster to
(re)generate, especially for long text. This can avoid stuttering during
gameplay on low-end CPUs or mobile.
- Label3D can use bitmap fonts and dynamic fonts (with and withoutMSDFor mipmaps). This makes it
more flexible on that aspect compared to TextMesh, especially for rendering
fonts with self-intersecting outlines or colored fonts (emoji).
Label3D can use bitmap fonts and dynamic fonts (with and withoutMSDFor mipmaps). This makes it
more flexible on that aspect compared to TextMesh, especially for rendering
fonts with self-intersecting outlines or colored fonts (emoji).
See also
SeeUsing Fontsfor guidelines on configuring font imports.

### Limitations

By default, Label3D has limited interaction with a 3D environment. It can be
occluded by geometry and lit by light sources if theShadedflag is enabled.
However, it will not cast shadows even ifCast Shadowis set toOnin
the Label3D's GeometryInstance3D properties. This is because the node internally
generates a quad mesh (one glyph per quad) with transparent textures and has the
same limitations as Sprite3D. Transparency sorting issues can also become apparent
when several Label3Ds overlap, especially if they have outlines.
This can be mitigated by setting the Label3D's transparency mode toAlpha
Cut, at the cost of less smooth text rendering. TheOpaque Pre-Passtransparency mode can preserve text smoothness while allowing the Label3D to
cast shadows, but some transparency sorting issues will remain.
SeeTransparency sortingsection in the 3D rendering limitations page for more information.
Text rendering quality can also suffer when the Label3D is viewed at a distance. To improve
text rendering quality,enable mipmaps on the fontorswitch the font to use MSDF rendering.

## TextMesh

The TextMesh resource has similarities to Label3D. They both display text in a
3D scene, and will use the same font subresource. However, instead of generating
transparent quads, TextMesh generates 3D geometry that represents the glyphs'
contours and has the properties of a mesh. As a result, a TextMesh is shaded by
default and automatically casts shadows onto the environment. A TextMesh can
also have a material applied to it (including custom shaders).
Here is an example of a texture and how it's applied to the mesh. You can use
the texture below as a reference for the generated mesh's UV map:

### Advantages

TextMesh has a few advantages over Label3D:

- TextMesh can use a texture to modify text color on a per-side basis.
TextMesh can use a texture to modify text color on a per-side basis.
- TextMesh geometry can have actual depth to it, giving glyphs a 3D look.
TextMesh geometry can have actual depth to it, giving glyphs a 3D look.
- TextMesh can use custom shaders, unlike Label3D.
TextMesh can use custom shaders, unlike Label3D.

### Limitations

There are some limitations to TextMesh:

- No built-in outline support, unlike Label3D. This can be simulated using custom
shaders though.
No built-in outline support, unlike Label3D. This can be simulated using custom
shaders though.
- Only dynamic fonts are supported (.ttf,.otf,.woff,.woff2).
Bitmap fonts in the.fntor.fontformats arenotsupported.
Only dynamic fonts are supported (.ttf,.otf,.woff,.woff2).
Bitmap fonts in the.fntor.fontformats arenotsupported.
- Fonts with self-intersecting outlines will not render correctly.
If you notice rendering issues on fonts downloaded from websites such as
Google Fonts, try downloading the font from the font author's official
website instead.
Fonts with self-intersecting outlines will not render correctly.
If you notice rendering issues on fonts downloaded from websites such as
Google Fonts, try downloading the font from the font author's official
website instead.
- Antialiasing the text rendering requires a full-scene antialiasing method to
be enabled such as MSAA, FXAA and temporal antialiasing (TAA). If no
antialiasing method is enabled, text will appear grainy, especially at a
distance. See3D antialiasingfor more information.
Antialiasing the text rendering requires a full-scene antialiasing method to
be enabled such as MSAA, FXAA and temporal antialiasing (TAA). If no
antialiasing method is enabled, text will appear grainy, especially at a
distance. See3D antialiasingfor more information.

## Projected Label node (or any other Control)

There is a last solution that is more complex to set up, but provides the most
flexibility: projecting a 2D node onto 3D space. This can be achieved using the
return value ofunproject_positionmethod on a Camera3D node in a script's_process()function. This return value
should then be used to set thepositionproperty of a Control node.
See the3D waypointsdemo for an example of this.

### Advantages

- Any Control node can be used, including Label, RichTextLabel or even nodes such
as Button. This allows for powerful formatting and GUI interaction.
Any Control node can be used, including Label, RichTextLabel or even nodes such
as Button. This allows for powerful formatting and GUI interaction.
- The script-based approach allows for complete freedom in positioning.
For example, this makes it considerably easier to pin Controls to the screen's
edges when they go off-screen (for in-game 3D markers).
The script-based approach allows for complete freedom in positioning.
For example, this makes it considerably easier to pin Controls to the screen's
edges when they go off-screen (for in-game 3D markers).
- Control theming is obeyed. This allows for easier customization that globally
applies to the project.
Control theming is obeyed. This allows for easier customization that globally
applies to the project.

### Limitations

- Projected Controls cannot be occluded by 3D geometry in any way. You can use a
RayCast to fully hide the control if its target position is occluded by a
collider, but this doesn't allow for partially hiding the control behind a
wall.
Projected Controls cannot be occluded by 3D geometry in any way. You can use a
RayCast to fully hide the control if its target position is occluded by a
collider, but this doesn't allow for partially hiding the control behind a
wall.
- Changing text size depending on distance by adjusting the Control'sscaleproperty is possible, but it needs to be done manually. Label3D and TextMesh
automatically take care of this, at the cost of less flexibility (can't set a
minimum/maximum text size in pixels).
Changing text size depending on distance by adjusting the Control'sscaleproperty is possible, but it needs to be done manually. Label3D and TextMesh
automatically take care of this, at the cost of less flexibility (can't set a
minimum/maximum text size in pixels).
- Handling resolution and aspect ratio changes must be taken into account in the
script, which can be challenging.
Handling resolution and aspect ratio changes must be taken into account in the
script, which can be challenging.

## Should I use Label3D, TextMesh or a projected Control?

In most scenarios, Label3D is recommended as it's easier to set up and provides
higher rendering quality (especially if 3D antialiasing is disabled).
For advanced use cases, TextMesh is more flexible as it allows styling the text
with custom shaders. Custom shaders allow for modifying the final geometry, such
as curving the text along a surface. Since the text is actual 3D geometry, the
text can optionally have depth to it and can also contribute to global
illumination.
If you need features such as BBCode or Control theming support, then using a projected
RichTextLabel node is the only way to go.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
