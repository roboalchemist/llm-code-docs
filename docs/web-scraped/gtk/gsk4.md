# Source: https://docs.gtk.org/gsk4/

Title: Gsk-4.0

URL Source: https://docs.gtk.org/gsk4/

Markdown Content:
### Namespace

The GTK toolkit

*   [Paths](https://docs.gtk.org/gsk4/paths.html)
*   [The Node file format](https://docs.gtk.org/gsk4/node-format.html)
*   [Classes Hierarchy](https://docs.gtk.org/gsk4/classes_hierarchy.html)

[BlendNode](https://docs.gtk.org/gsk4/class.BlendNode.html "BlendNode")A render node applying a blending function between its two child nodes.
[BlurNode](https://docs.gtk.org/gsk4/class.BlurNode.html "BlurNode")A render node applying a blur effect to its single child.
[BorderNode](https://docs.gtk.org/gsk4/class.BorderNode.html "BorderNode")A render node for a border.
[CairoNode](https://docs.gtk.org/gsk4/class.CairoNode.html "CairoNode")A render node for a Cairo surface.
[CairoRenderer](https://docs.gtk.org/gsk4/class.CairoRenderer.html "CairoRenderer")Renders a GSK rendernode tree with cairo.
[ClipNode](https://docs.gtk.org/gsk4/class.ClipNode.html "ClipNode")A render node applying a rectangular clip to its single child node.
[ColorMatrixNode](https://docs.gtk.org/gsk4/class.ColorMatrixNode.html "ColorMatrixNode")A render node controlling the color matrix of its single child node.
[ColorNode](https://docs.gtk.org/gsk4/class.ColorNode.html "ColorNode")A render node for a solid color.
[ComponentTransferNode](https://docs.gtk.org/gsk4/class.ComponentTransferNode.html "ComponentTransferNode")A render node for applying a `GskComponentTransfer` for each color component of the child node.

since: 4.20
[CompositeNode](https://docs.gtk.org/gsk4/class.CompositeNode.html "CompositeNode")A render node that uses Porter/Duff compositing operators to combine its child with the background.

since: 4.22
[ConicGradientNode](https://docs.gtk.org/gsk4/class.ConicGradientNode.html "ConicGradientNode")A render node for a conic gradient.
[ContainerNode](https://docs.gtk.org/gsk4/class.ContainerNode.html "ContainerNode")A render node that can contain other render nodes.
[CopyNode](https://docs.gtk.org/gsk4/class.CopyNode.html "CopyNode")A render node that copies the current state of the rendering canvas so a `GskPasteNode` can draw it.

since: 4.22
[CrossFadeNode](https://docs.gtk.org/gsk4/class.CrossFadeNode.html "CrossFadeNode")A render node cross fading between two child nodes.
[DebugNode](https://docs.gtk.org/gsk4/class.DebugNode.html "DebugNode")A render node that emits a debugging message when drawing its child node.
[FillNode](https://docs.gtk.org/gsk4/class.FillNode.html "FillNode")A render node filling the area given by `GskPath` and `GskFillRule` with the child node.

since: 4.14
[GLRenderer](https://docs.gtk.org/gsk4/class.GLRenderer.html "GLRenderer")Renders a GSK rendernode tree with OpenGL.

since: 4.2
[GLShader](https://docs.gtk.org/gsk4/class.GLShader.html "GLShader")Implements a fragment shader using GLSL.

deprecated: 4.16
[GLShaderNode](https://docs.gtk.org/gsk4/class.GLShaderNode.html "GLShaderNode")A render node using a GL shader when drawing its children nodes.
[InsetShadowNode](https://docs.gtk.org/gsk4/class.InsetShadowNode.html "InsetShadowNode")A render node for an inset shadow.
[IsolationNode](https://docs.gtk.org/gsk4/class.IsolationNode.html "IsolationNode")A render node that isolates its child from surrounding rendernodes.

since: 4.22
[LinearGradientNode](https://docs.gtk.org/gsk4/class.LinearGradientNode.html "LinearGradientNode")A render node for a linear gradient.
[MaskNode](https://docs.gtk.org/gsk4/class.MaskNode.html "MaskNode")A render node masking one child node with another.

since: 4.10
[NglRenderer](https://docs.gtk.org/gsk4/class.NglRenderer.html "NglRenderer")A GL based renderer.
[OpacityNode](https://docs.gtk.org/gsk4/class.OpacityNode.html "OpacityNode")A render node controlling the opacity of its single child node.
[OutsetShadowNode](https://docs.gtk.org/gsk4/class.OutsetShadowNode.html "OutsetShadowNode")A render node for an outset shadow.
[PasteNode](https://docs.gtk.org/gsk4/class.PasteNode.html "PasteNode")A render node for a paste.

since: 4.22
[RadialGradientNode](https://docs.gtk.org/gsk4/class.RadialGradientNode.html "RadialGradientNode")A render node for a radial gradient.
[Renderer](https://docs.gtk.org/gsk4/class.Renderer.html "Renderer")Renders a scene graph defined via a tree of `GskRenderNode` instances.
[RenderNode](https://docs.gtk.org/gsk4/class.RenderNode.html "RenderNode")The basic block in a scene graph to be rendered using `GskRenderer`.
[RepeatingLinearGradientNode](https://docs.gtk.org/gsk4/class.RepeatingLinearGradientNode.html "RepeatingLinearGradientNode")A render node for a repeating linear gradient.
[RepeatingRadialGradientNode](https://docs.gtk.org/gsk4/class.RepeatingRadialGradientNode.html "RepeatingRadialGradientNode")A render node for a repeating radial gradient.
[RepeatNode](https://docs.gtk.org/gsk4/class.RepeatNode.html "RepeatNode")A render node repeating its single child node.
[RoundedClipNode](https://docs.gtk.org/gsk4/class.RoundedClipNode.html "RoundedClipNode")A render node applying a rounded rectangle clip to its single child.
[ShadowNode](https://docs.gtk.org/gsk4/class.ShadowNode.html "ShadowNode")A render node drawing one or more shadows behind its single child node.
[StrokeNode](https://docs.gtk.org/gsk4/class.StrokeNode.html "StrokeNode")A render node that will fill the area determined by stroking the the given `GskPath` using the `GskStroke` attributes.

since: 4.14
[SubsurfaceNode](https://docs.gtk.org/gsk4/class.SubsurfaceNode.html "SubsurfaceNode")A render node that potentially diverts a part of the scene graph to a subsurface.

since: 4.14
[TextNode](https://docs.gtk.org/gsk4/class.TextNode.html "TextNode")A render node drawing a set of glyphs.
[TextureNode](https://docs.gtk.org/gsk4/class.TextureNode.html "TextureNode")A render node for a `GdkTexture`.
[TextureScaleNode](https://docs.gtk.org/gsk4/class.TextureScaleNode.html "TextureScaleNode")A render node for a `GdkTexture`, with control over scaling.

since: 4.10
[TransformNode](https://docs.gtk.org/gsk4/class.TransformNode.html "TransformNode")A render node applying a `GskTransform` to its single child node.
[VulkanRenderer](https://docs.gtk.org/gsk4/class.VulkanRenderer.html "VulkanRenderer")Renders a GSK rendernode tree with Vulkan.

[ColorStop](https://docs.gtk.org/gsk4/struct.ColorStop.html "ColorStop")A color stop in a gradient node.
[ComponentTransfer](https://docs.gtk.org/gsk4/struct.ComponentTransfer.html "ComponentTransfer")Specifies a transfer function for a color component to be applied while rendering.

since: 4.20
[ParseLocation](https://docs.gtk.org/gsk4/struct.ParseLocation.html "ParseLocation")A location in a parse buffer.
[Path](https://docs.gtk.org/gsk4/struct.Path.html "Path")Describes lines and curves that are more complex than simple rectangles.

since: 4.14
[PathBuilder](https://docs.gtk.org/gsk4/struct.PathBuilder.html "PathBuilder")Constructs `GskPath` objects.

since: 4.14
[PathMeasure](https://docs.gtk.org/gsk4/struct.PathMeasure.html "PathMeasure")Performs measurements on paths such as determining the length of the path.

since: 4.14
[PathPoint](https://docs.gtk.org/gsk4/struct.PathPoint.html "PathPoint")Represents a point on a path.

since: 4.14
[RenderReplay](https://docs.gtk.org/gsk4/struct.RenderReplay.html "RenderReplay")A facility to replay a `GskRenderNode` and its children, potentially modifying them.

since: 4.22
[RoundedRect](https://docs.gtk.org/gsk4/struct.RoundedRect.html "RoundedRect")A rectangular region with rounded corners.
[ShaderArgsBuilder](https://docs.gtk.org/gsk4/struct.ShaderArgsBuilder.html "ShaderArgsBuilder")Builds the uniforms data for a `GskGLShader`.

deprecated: 4.16
[Shadow](https://docs.gtk.org/gsk4/struct.Shadow.html "Shadow")The shadow parameters in a shadow node.
[Stroke](https://docs.gtk.org/gsk4/struct.Stroke.html "Stroke")Collects the parameters that are needed when stroking a path.

since: 4.14
[Transform](https://docs.gtk.org/gsk4/struct.Transform.html "Transform")Describes a 3D transform.

[BlendMode](https://docs.gtk.org/gsk4/enum.BlendMode.html "BlendMode")The blend modes available for render nodes.
[Corner](https://docs.gtk.org/gsk4/enum.Corner.html "Corner")The corner indices used by `GskRoundedRect`.
[FillRule](https://docs.gtk.org/gsk4/enum.FillRule.html "FillRule")Specifies how paths are filled.

since: 4.14
[GLUniformType](https://docs.gtk.org/gsk4/enum.GLUniformType.html "GLUniformType")Defines the types of the uniforms that `GskGLShaders` declare.

deprecated: 4.16
[LineCap](https://docs.gtk.org/gsk4/enum.LineCap.html "LineCap")Specifies how to render the start and end points of contours or dashes when stroking.

since: 4.14
[LineJoin](https://docs.gtk.org/gsk4/enum.LineJoin.html "LineJoin")Specifies how to render the junction of two lines when stroking.

since: 4.14
[MaskMode](https://docs.gtk.org/gsk4/enum.MaskMode.html "MaskMode")The mask modes available for mask nodes.

since: 4.10
[PathDirection](https://docs.gtk.org/gsk4/enum.PathDirection.html "PathDirection")Used to pick one of the four tangents at a given point on the path.

since: 4.14
[PathIntersection](https://docs.gtk.org/gsk4/enum.PathIntersection.html "PathIntersection")The values of this enumeration classify intersections between paths.

since: 4.20
[PathOperation](https://docs.gtk.org/gsk4/enum.PathOperation.html "PathOperation")Describes the segments of a `GskPath`.

since: 4.14
[PorterDuff](https://docs.gtk.org/gsk4/enum.PorterDuff.html "PorterDuff")The 12 compositing modes defined by the seminal paper by Thomas Porter and Tom Duff.

since: 4.22
[RenderNodeType](https://docs.gtk.org/gsk4/enum.RenderNodeType.html "RenderNodeType")The type of a node determines what the node is rendering.
[ScalingFilter](https://docs.gtk.org/gsk4/enum.ScalingFilter.html "ScalingFilter")The filters used when scaling texture data.
[TransformCategory](https://docs.gtk.org/gsk4/enum.TransformCategory.html "TransformCategory")The categories of matrices relevant for GSK and GTK.

[Isolation](https://docs.gtk.org/gsk4/flags.Isolation.html "Isolation")These flags describe the types of isolations possible with a `GskIsolationNode`.

since: 4.22
[PathForeachFlags](https://docs.gtk.org/gsk4/flags.PathForeachFlags.html "PathForeachFlags")Flags that can be passed to `gsk_path_foreach()` to influence what kinds of operations the path is decomposed into.

since: 4.14

[ParseErrorFunc](https://docs.gtk.org/gsk4/callback.ParseErrorFunc.html "ParseErrorFunc")Type of callback that is called when an error occurs during node deserialization.
[PathForeachFunc](https://docs.gtk.org/gsk4/callback.PathForeachFunc.html "PathForeachFunc")Type of the callback to iterate through the operations of a path.
[PathIntersectionFunc](https://docs.gtk.org/gsk4/callback.PathIntersectionFunc.html "PathIntersectionFunc")Prototype of the callback to iterate through the intersections of two paths.

since: 4.20
[RenderReplayFontFilter](https://docs.gtk.org/gsk4/callback.RenderReplayFontFilter.html "RenderReplayFontFilter")A function that filters fonts.

since: 4.22
[RenderReplayNodeFilter](https://docs.gtk.org/gsk4/callback.RenderReplayNodeFilter.html "RenderReplayNodeFilter")A function to replay a node.

since: 4.22
[RenderReplayTextureFilter](https://docs.gtk.org/gsk4/callback.RenderReplayTextureFilter.html "RenderReplayTextureFilter")A function that filters textures.

since: 4.22
