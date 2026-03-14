# Crate iced 
Source 
## Re-exports§
`pub use application::Application;``pub use daemon::Daemon;``pub use iced_futures::futures;``pub use iced_highlighter as highlighter;``highlighter``pub use iced_renderer::wgpu::wgpu;``wgpu``pub use Alignment::Center;``pub use Length::Fill;``pub use Length::FillPortion;``pub use Length::Shrink;``pub use alignment::Horizontal::Left;``pub use alignment::Horizontal::Right;``pub use alignment::Vertical::Bottom;``pub use alignment::Vertical::Top;`
## Modules§
advanced`advanced`Leverage advanced concepts like custom widgets.alignmentAlign and position widgets.animationAnimate your applications.applicationCreate and run iced applications step by step.borderDraw lines around containers.clipboardAccess the clipboard.daemonCreate and run daemons that run in the background.debugDebug your applications.eventHandle events of a user interface.executorChoose your preferred executor to power your application.fontLoad and use fonts.gradientColors that transition progressively.keyboardListen and react to keyboard events.messageTraits for the message type of a `Program`.mouseListen and react to mouse events.overlayDisplay interactive elements on top of other widgets.paddingSpace stuff around the perimeter.streamCreate asynchronous streams of data.systemRetrieve system information.taskCreate runtime tasks.themeUse the built-in theme and styles.timeListen and react to time.touchListen and react to touch events.widgetUse the built-in widgets or create your own.windowConfigure the window of your application in native platforms.
## Macros§
colorCreates a `Color` with shorter and cleaner syntax.
## Structs§
AnimationThe animation of some particular state.BorderA border.ColorA color in the `sRGB` color space.DegreesDegreesFontA font.PaddingAn amount of space to pad for each side of a boxPixelsAn amount of logical pixels.PointA 2D point.PresetA specific boot strategy for a `Program`.RadiansRadiansRectangleAn axis-aligned rectangle.SettingsThe settings of an iced program.ShadowA shadow.SizeAn amount of space in 2 dimensions.SubscriptionA request to listen to external events.TaskA set of concurrent actions to be performed by the iced runtime.TransformationA 2D transformation matrix.VectorA 2D vector.
## Enums§
AlignmentAlignment on the axis of a container.BackgroundThe background of some element.ContentFitThe strategy used to fit the contents of a widget to its bounding box.ErrorAn error that occurred while running an application.EventA user interface event.GradientA fill which transitions colors progressively along a direction, either linearly, radially (TBD),
or conically (TBD).LengthThe strategy used to fill space in a specific dimension.NeverThe error type for errors that can never happen.RotationThe strategy used to rotate the content.ThemeA built-in theme.
## Traits§
ExecutorA type that can run futures.FunctionA trait extension for binary functions (`Fn(A, B) -> O`).ProgramAn interactive, native, cross-platform, multi-windowed application.WindowA window managed by iced.
## Functions§
applicationCreates an iced `Application` given its boot, update, and view logic.daemonCreates an iced `Daemon` given its boot, update, and view logic.exitCreates a `Task` that exits the iced runtime.neverA function that can *never* be called.runRuns a basic iced application with default `Settings` given its update
and view logic.
## Type Aliases§
ElementA generic widget.RendererThe default graphics renderer for `iced`.ResultThe result of running an iced program.