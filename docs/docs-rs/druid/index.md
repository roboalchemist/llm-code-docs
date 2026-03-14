# Crate druid

Source

## Re-exports§

`pub use lens::Lens;``pub use lens::LensExt;``pub use widget::Widget;``pub use widget::WidgetExt;``pub use widget::WidgetId;``pub use shell::image;``image``pub use shell::keyboard_types;`

## Modules§

commandsCommands with special meaning, defined by Druid.debug_stateA data structure for representing widget trees.envAn environment which is passed downward into the widget tree.im`im`Immutable Data Structures for Rustkurbo2D geometry, with a focus on curves.lensImplementations of `Lens`, a way of focusing on subfields of data.menuWindow, application, and context menuspietA piet backend appropriate for the current platform.platform_menusPre-configured, platform appropriate menus and menu items.scroll_componentA component for embedding in another widget to provide consistent and
extendable scrolling behaviortestsNon-WebAssemblyAdditional unit tests that cross file or module boundaries.textEditing and displaying text.themeTheme keys and initial values.widgetCommon widgets.

## Macros§

lensConstruct a lens accessing a type’s fieldwidget_wrapper_bodyA macro to help implementation of WidgetWrapper for a direct wrapper.
Use it in the body of the impl.widget_wrapper_pod_bodyA macro to help implementation of WidgetWrapper for a wrapper of a typed pod.
Use it in the body of the impl.

## Structs§

AffineA 2D affine transform.AppLauncherHandles initial setup of an application, and starts the runloop.ApplicationThe top level application object.BoxConstraintsConstraints for layout.ClipboardA handle to the system clipboard.ClipboardFormatData coupled with a type identifier.CommandAn arbitrary command.CursorDescA platform-independent description of a custom cursor.DelegateCtxA context passed in to `AppDelegate` functions.DruidHandlerThe struct implements the `druid-shell` `WinHandler` trait.EnvAn environment passed down through all widget traversals.EventCtxA mutable context provided to event handling methods of widgets.ExtEventErrorAn error that occurs if an external event cannot be submitted.
This probably means that the application has gone away.ExtEventSinkA thing that can move into other threads and be used to submit commands back
to the running application.FileDialogOptionsOptions for file dialogs.FileInfoInformation about the path to be opened or saved.FileSpecA description of a filetype, for specifying allowed types in a file dialog.HotKeyA description of a keyboard shortcut.ImageBufAn in-memory pixel buffer.InsetsInsets from the edges of a rectangle.KeyA typed `Env` key.KeyEventInformation about a keyboard event.LayoutCtxA context provided to layout-handling methods of widgets.LifeCycleCtxA mutable context provided to the `lifecycle` method on widgets.LinearGradientA description of a linear gradient in the unit rect, which can be resolved
to a fixed gradient.LocalizedStringA string that can be localized based on the current locale.MenuA menu.MenuItemAn item in a menu.ModifiersThe modifiers.MonitorMonitor struct containing data about a monitor on the systemMouseButtonsA set of `MouseButton`s.MouseEventThe state of the mouse for a click, mouse-up, move, or wheel event.NotificationA message passed up the tree from a `Widget` to its ancestors.PaintCtxA context passed to paint methods of widgets.PointA 2D point.RadialGradientA description of a radial gradient in the unit rect, which can be resolved
to a fixed gradient.RectA rectangle.RegionA union of rectangles, useful for describing an area that needs to be repainted.RoundedRectRadiiRadii for each corner of a rounded rectangle.ScaleCoordinate scaling between pixels and display points.ScaledAreaA specific area scaling state.ScreenInformation about the screen and monitorsSelectorAn identifier for a particular command.SingleUseA wrapper type for `Command` payloads that should only be used once.SizeA 2D size.TimerTokenA token that uniquely identifies a running timer.UnitPointA representation of a point relative to a unit rectangle.UpdateCtxA mutable context provided to data update methods of widgets.ValueTypeErrorThe error type for environment access.Vec2A 2D vector.ViewContextInformation about the widget’s surroundings.WidgetPodA container for one widget in the hierarchy.WidgetStateGeneric state for all widgets in the hierarchy.WindowPer-window state not owned by user code.WindowConfigWindow configuration that can be applied to a WindowBuilder, or to an existing WindowHandle.
It does not include anything related to app data.WindowDescA description of a window to be instantiated.WindowHandleA handle to a platform window object.WindowIdA unique identifier for a window.

## Enums§

CodeCode is the physical position of a key.ColorA datatype representing color.CursorMouse cursors.EventAn event, propagated downwards during event flow.HandledAn enum for specifying whether an event was handled.InternalEventInternal events used by Druid inside `WidgetPod`.InternalLifeCycleInternal lifecycle events used by Druid inside `WidgetPod`.KeyOrValueEither a concrete `T` or a `Key<T>` that can be resolved in the `Env`.LifeCycleApplication life cycle events.LocationThe location attribute contains an indication of the logical location
of the key on the device.MouseButtonAn indicator of which mouse button was pressed.PlatformErrorShell errors.RawModsA representation of the active modifier keys.RawWindowHandle`raw-win-handle`A window handle for a particular windowing system.SysModsA platform-agnostic representation of keyboard modifiers, for command handling.TargetThe target of a `Command`.ValueA dynamic type representing all values that can be stored in an environment.WindowLevelLevels in the window system - Z order for display purposes.
Describes the purpose of a window and should be mapped appropriately to match platform
conventions.WindowSizePolicyDefines how a windows size should be determinedWindowStateContains the different states a Window can be in.

## Traits§

AppDelegateA type that provides hooks for handling and modifying top-level events.DataA trait used to represent value types.HasRawWindowHandle`raw-win-handle`Window that wraps around a raw window handle.RenderContextThe main trait for rendering graphics.ScalableThe `Scalable` trait describes how coordinates should be translated
from display points into pixels and vice versa using a `Scale`.ValueTypeValues which can be stored in an environment.

## Type Aliases§

FormatIdA type identifier for the system clipboard.KbKeyThe meaning (mapped value) of a keypress.

## Derive Macros§

DataGenerates implementations of the `Data` trait.LensGenerates lenses to access the fields of a struct.
