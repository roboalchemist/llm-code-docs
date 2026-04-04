# Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/

Title: Graphics and Multimedia - WPF

URL Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/

Markdown Content:
[](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/) Windows Presentation Foundation (WPF) provides support for multimedia, vector graphics, animation, and content composition, making it easy for developers to build interesting user interfaces and content. Using Visual Studio, you can create vector graphics or complex animations and integrate media into your applications.

This topic introduces the graphics, animation, and media features of WPF, which enable you to add graphics, transition effects, sound, and video to your applications.

Note

Using WPF types in a Windows service is strongly discouraged. If you attempt to use WPF types in a Windows service, the service may not work as expected.

Several changes have been made related to graphics and animations.

*   Layout Rounding

When an object edge falls in the middle of a pixel device, the DPI-independent graphics system can create rendering artifacts, such as blurry or semi-transparent edges. Previous versions of WPF included pixel snapping to help handle this case. Silverlight 2 introduced layout rounding, which is another way to move elements so that edges fall on whole pixel boundaries. WPF now supports layout rounding with the [UseLayoutRounding](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement.uselayoutrounding) attached property on [FrameworkElement](https://learn.microsoft.com/en-us/dotnet/api/system.windows.frameworkelement).

*   Cached Composition

By using the new [BitmapCache](https://learn.microsoft.com/en-us/dotnet/api/system.windows.media.bitmapcache) and [BitmapCacheBrush](https://learn.microsoft.com/en-us/dotnet/api/system.windows.media.bitmapcachebrush) classes, you can cache a complex part of the visual tree as a bitmap and greatly improve rendering time. The bitmap remains responsive to user input, such as mouse clicks, and you can paint it onto other elements just like any brush.

*   Pixel Shader 3 Support

WPF 4 builds on top of the [ShaderEffect](https://learn.microsoft.com/en-us/dotnet/api/system.windows.media.effects.shadereffect) support introduced in WPF 3.5 SP1 by allowing applications to write effects by using Pixel Shader (PS) version 3.0. The PS 3.0 shader model is more sophisticated than PS 2.0, which allows for even more effects on supported hardware.

*   Easing Functions

You can enhance animations with easing functions, which give you additional control over the behavior of animations. For example, you can apply an [ElasticEase](https://learn.microsoft.com/en-us/dotnet/api/system.windows.media.animation.elasticease) to an animation to give the animation a springy behavior. For more information, see the easing types in the [System.Windows.Media.Animation](https://learn.microsoft.com/en-us/dotnet/api/system.windows.media.animation) namespace.

WPF includes support for high quality 2D graphics. The functionality includes brushes, geometries, images, shapes and transformations. For more information, see [Graphics](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/graphics). The rendering of graphical elements is based on the [Visual](https://learn.microsoft.com/en-us/dotnet/api/system.windows.media.visual) class. The structure of visual objects on the screen is described by the visual tree. For more information, see [WPF Graphics Rendering Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/wpf-graphics-rendering-overview).

WPF provides a library of commonly used, vector-drawn 2D shapes, such as rectangles and ellipses, which the following illustration shows.

![Image 1: Diagram showing ellipses and rectangles.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/media/index/two-deminsional-shapes-ellipses-rectangles.png)

These intrinsic WPF shapes are not just shapes: they are programmable elements that implement many of the features that you expect from most common controls, which include keyboard and mouse input. The following example shows how to handle the [MouseUp](https://learn.microsoft.com/en-us/dotnet/api/system.windows.uielement.mouseup#system-windows-uielement-mouseup) event raised by clicking an [Ellipse](https://learn.microsoft.com/en-us/dotnet/api/system.windows.shapes.ellipse) element.

```
<Window
  xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
  xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
  x:Class="Window1" >
  <Ellipse Fill="LightBlue" MouseUp="ellipseButton_MouseUp" />
</Window>
```

```
public partial class Window1  : Window
{
    void ellipseButton_MouseUp(object sender, MouseButtonEventArgs e)
    {
        MessageBox.Show("You clicked the ellipse!");
    }
}
```

The following illustration shows the output for the preceding XAML markup and code-behind.

![Image 2: A message box saying "You clicked the ellipse!"](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/media/index/messagebox-text-output.png)

For more information, see [Shapes and Basic Drawing in WPF Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/shapes-and-basic-drawing-in-wpf-overview). For an introductory sample, see [Shape Elements Sample](https://github.com/Microsoft/WPF-Samples/tree/master/Graphics/ShapeElements).

When the 2D shapes that WPF provides are not sufficient, you can use WPF support for geometries and paths to create your own. The following illustration shows how you can use geometries to create shapes, as a drawing brush, and to clip other WPF elements.

![Image 3: Screenshot showing how you can use geometries to create shapes.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/media/index/use-geometries-create-shapes.png)

For more information, see [Geometry Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/geometry-overview). For an introductory sample, see [Geometries Sample](https://github.com/Microsoft/WPF-Samples/tree/master/Graphics/Geometry).

WPF provides a library of 2D classes that you can use to create a variety of effects. The 2D rendering capability of WPF provides the ability to paint UI elements that have gradients, bitmaps, drawings, and videos; and to manipulate them by using rotation, scaling, and skewing. The following illustration gives an example of the many effects you can achieve by using WPF brushes.

![Image 4: Illustration showing the different WPF brushes and paint elements.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/media/index/brushes-paint-elements.png)

For more information, see [WPF Brushes Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/wpf-brushes-overview). For an introductory sample, see [Brushes Sample](https://github.com/Microsoft/WPF-Samples/tree/master/Graphics/Brushes).

WPF provides a set of 3D rendering capabilities that integrate with 2D graphics support in WPF in order for you to create more exciting layout, UI, and data visualization. At one end of the spectrum, WPF enables you to render 2D images onto the surfaces of 3D shapes, which the following illustration demonstrates.

![Image 5: Screenshot of a sample showing 3D shapes with different textures.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/media/index/visual-three-dimensional-shape.png)

For more information, see [3D Graphics Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/3-d-graphics-overview). For an introductory sample, see [3D Solids Sample](https://github.com/microsoft/WPF-Samples/tree/master/Animation/AnimationExamples).

Use animation to make controls and elements grow, shake, spin, and fade; and to create interesting page transitions, and more. Because WPF enables you to animate most properties, not only can you animate most WPF objects, you can also use WPF to animate custom objects that you create.

![Image 6: Screenshot of an animated cube.](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/media/index/animate-custom-objects.png)

For more information, see [Animation Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/animation-overview). For an introductory sample, see [Animation Example Gallery](https://github.com/Microsoft/WPF-Samples/tree/master/Animation/AnimationExamples).

Images, video, and audio are media-rich ways of conveying information and user experiences.

Images, which include icons, backgrounds, and even parts of animations, are a core part of most applications. Because you frequently need to use images, WPF exposes the ability to work with them in a variety of ways. The following illustration shows just one of those ways.

![Image 7: Styling sample screenshot](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/controls/media/stylingintro-eventtriggers.png)

For more information, see [Imaging Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/imaging-overview).

A core feature of the graphics capabilities of WPF is to provide native support for working with multimedia, which includes video and audio. The following example shows how to insert a media player into an application.

```
<MediaElement Source="media\numbers.wmv" Width="450" Height="250" />
```

[MediaElement](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.mediaelement) is capable of playing both video and audio, and is extensible enough to allow the easy creation of custom UIs.

For more information, see the [Multimedia Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/multimedia-overview).

*   [System.Windows.Media](https://learn.microsoft.com/en-us/dotnet/api/system.windows.media)
*   [System.Windows.Media.Animation](https://learn.microsoft.com/en-us/dotnet/api/system.windows.media.animation)
*   [System.Windows.Media.Media3D](https://learn.microsoft.com/en-us/dotnet/api/system.windows.media.media3d)
*   [2D Graphics and Imaging](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/optimizing-performance-2d-graphics-and-imaging)
*   [Shapes and Basic Drawing in WPF Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/shapes-and-basic-drawing-in-wpf-overview)
*   [Painting with Solid Colors and Gradients Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/painting-with-solid-colors-and-gradients-overview)
*   [Painting with Images, Drawings, and Visuals](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/painting-with-images-drawings-and-visuals)
*   [Animation and Timing How-to Topics](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/animation-and-timing-how-to-topics)
*   [3D Graphics Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/3-d-graphics-overview)
*   [Multimedia Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/graphics-multimedia/multimedia-overview)
