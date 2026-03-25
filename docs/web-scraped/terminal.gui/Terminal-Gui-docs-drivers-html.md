# Source: https://gui-cs.github.io/Terminal.Gui/docs/drivers.html

Title: Cross-Platform Driver Model | Terminal.Gui v2

URL Source: https://gui-cs.github.io/Terminal.Gui/docs/drivers.html

Markdown Content:
Overview[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#overview)
----------------------------------------------------------------------------

The driver model is the mechanism by which Terminal.Gui supports multiple platforms. Windows, Mac, Linux, and unit test environments are all supported through a modular, component-based architecture.

Terminal.Gui v2 uses a sophisticated driver architecture that separates concerns and enables platform-specific optimizations while maintaining a consistent API. The architecture is based on the **Component Factory** pattern and uses **multi-threading** to ensure responsive input handling.

**Important:**[View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html) subclasses should not access [Application](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.html)'s `Driver`. Use the View APIs instead:

* [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html)'s `Move(col, row)` for positioning
* [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html)'s `AddRune()` and `AddStr()` for drawing
* [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html)'s `App.Screen` for screen dimensions

Available Drivers[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#available-drivers)
----------------------------------------------------------------------------------------------

Terminal.Gui provides three console driver implementations:

|  | **ansi** | **dotnet** | **windows** |
| --- | --- | --- | --- |
| **Theme** | Default driver for Unix/macOS and a showcase driver for all platforms. Pure ANSI implementation. Ideal for testing/CI. Deterministic behavior with virtual time support. | Cross-platform managed .NET driver. Simplest implementation using `System.Console` API. Works with .NET BCL only. | High-performance Windows-only driver. Native Win32 Console API. Direct access to Windows-specific features. |
| **Input Model** | Reads raw ANSI sequences, parses to Terminal.Gui events | Reads `ConsoleKeyInfo` from `System.Console`, converts to Terminal.Gui events | Reads `INPUT_RECORD` structures directly, converts to Terminal.Gui events |
| **Unix Read APIs** | `poll(STDIN_FILENO, ...)`, `read(STDIN_FILENO, buffer, len)`, `tcgetattr()`/`tcsetattr()` for raw mode via `UnixRawModeHelper` | N/A (uses .NET `Console.ReadKey()` which internally delegates to platform APIs) reads `char` | N/A (Windows-only) |
| **Windows Read APIs** | P/Invokes `ReadFile()` reads `char` | N/A (uses .NET `Console.ReadKey()` which internally delegates to platform APIs) | P/Invokes `ReadConsoleInputW()` reads `INPUT_RECORD`, `GetConsoleMode()`/`SetConsoleMode()` enables mouse input and raw mode |
| **Output Model** | Pure ANSI escape sequences | Managed .NET + ANSI sequences (when VT mode enabled) | Direct character output via Win32 API with double buffering |
| **Unix Write APIs** | `write()` syscall to stdout (fd 1) | N/A (uses .NET `Console.Write()` which internally delegates to platform APIs) | N/A (Windows-only) |
| **Windows Write APIs** | P/Invokes `WriteFile()` | N/A (uses .NET `Console.Write()` which internally delegates to platform APIs) | P/Invokes `WriteConsoleW()`, `CreateConsoleScreenBuffer()`/`SetConsoleActiveScreenBuffer()` for double buffering, `SetConsoleTextAttribute()` |
| **Screen Model** | Configurable via `Driver.SizeDetection`. Default (`AnsiQuery`): ANSI `CSI 18t` query, throttled to 500 ms. `Polling`: `ioctl(TIOCGWINSZ)` on Unix, Console API on Windows. | Polling-based re-size: `Console.WindowWidth`/`Console.WindowHeight` queried periodically. Falls back to 80x25 on `IOException`. | Event-based re-size: `WINDOW_BUFFER_SIZE_EVENT` received in input stream via `ReadConsoleInputW()`. Immediate resize notification. `GetConsoleScreenBufferInfoEx()` queries dimensions. |
| **Cursor Handling** | ANSI sequences: DECTCEM (`CSI ? 25 h/l`) for show/hide, DECSCUSR (`CSI Ps SP q`) for style. Full `CursorStyle` support. | ANSI sequences (same as ansi driver). Falls back to `Console.SetCursorPosition()` on Windows. | • Legacy mode: Win32 `CONSOLE_CURSOR_INFO` (size percentage only, no blinking control). • Modern VT mode: ANSI sequences (same as ansi driver). Full `CursorStyle` support. |
| **Advantages** | • Cross-platform (all platforms) • Pure, clean implementation • Perfect for testing/CI • Virtual time support • Deterministic behavior • Configurable size detection | • Cross-platform (all platforms) • Maximum compatibility • Simple implementation • No P/Invoke; Works with .NET BCL | • Highest performance on Windows • Immediate resize detection |
| **Disadvantages** | • Requires proper ANSI support | • Lower performance (managed overhead) • Limited feature set • `System.ReadKey` has bugs on Windows • Polling-based resize | • Windows-only • More complex P/Invoke code |

### Automatic Driver Selection[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#automatic-driver-selection)

The appropriate driver is automatically selected based on the platform when [Application](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.html)'s `Init()` is called:

* **Windows** (Win32NT, Win32S, Win32Windows) → `WindowsDriver`
* **Unix/Linux/macOS** → `AnsiDriver`

### Explicit Driver Selection[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#explicit-driver-selection)

Explicitly specify a driver in several ways:

Method 1: Set ForceDriver using Configuration Manager

```
{
  "Application.ForceDriver": "ansi"
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html# "Copy")
Method 2: Pass driver name to Init

```
// Use type-safe constants from DriverRegistry.Names
Application.Init(driverName: DriverRegistry.Names.ANSI);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html# "Copy")
Method 3: Set ForceDriver on instance

```
using Terminal.Gui.Drivers;
using (IApplication app = Application.Create())
{
    app.ForceDriver = DriverRegistry.Names.ANSI;
    app.Init();
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html# "Copy")

### Force Driver as Configuration Property[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#forcedriver-as-configuration-property)

The `ForceDriver` property is a configuration property marked with `[ConfigurationProperty]`, which means:

* It can be set through the configuration system (e.g., `config.json`)
* Changes raise the `ForceDriverChanged` event
* It persists across application instances when using the static [Application](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.html) class

```
// Subscribe to driver changes
Application.ForceDriverChanged += (_, e) =>
{
    Logging.Information($"Driver changed: {e.OldValue} → {e.NewValue}");
};

// Change driver
Application.ForceDriver = DriverRegistry.Names.ANSI;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html# "Copy")

### Discovering Available Drivers[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#discovering-available-drivers)

Terminal.Gui provides several methods to discover available drivers at runtime through the **Driver Registry**:

```
// Get driver names (AOT-friendly, no reflection)
IEnumerable<string> driverNames = Application.GetRegisteredDriverNames();

Logging.Information("Available drivers:");
foreach (string name in driverNames)
{
    Logging.Information($"  - {name}");
}

// Output:
// Available drivers:
//   - dotnet
//   - windows
//   - ansi
```

[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html# "Copy")
For more detailed information about each driver:

```
// Get driver metadata
foreach (DriverRegistry.DriverDescriptor descriptor in Application.GetRegisteredDrivers())
{
    Logging.Information($"{descriptor.DisplayName}");
    Logging.Information($"  Name: {descriptor.Name}");
    Logging.Information($"  Description: {descriptor.Description}");
    Logging.Information($"  Platforms: {string.Join(", ", descriptor.SupportedPlatforms)}");
    Logging.Information("");
}

// Output:
// Windows Console Driver
//   Name: windows
//   Description: Optimized Windows Console API driver with native input handling
//   Platforms: Win32NT, Win32S, Win32Windows
//
// .NET Cross-Platform Driver
//   Name: dotnet
//   Description: Cross-platform driver using System.Console API
//   Platforms: Win32NT, Unix, MacOSX
// ...
```

[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html# "Copy")
Validate driver names (useful for CLI argument validation):

```
string userInput = args[0];

if (Application.IsDriverNameValid(userInput))
{
    Application.Init(driverName: userInput);
}
else
{
    Logging.Information($"Invalid driver: {userInput}");
    Logging.Information($"Valid options: {string.Join(", ", Application.GetRegisteredDriverNames())}");
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html# "Copy")
Use type-safe constants in code:

```
using Terminal.Gui.Drivers;

// Type-safe driver names from DriverRegistry.Names
string driverName = DriverRegistry.Names.ANSI;  // "ansi"
app.Init(driverName);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html# "Copy")
**Note**: The legacy `GetDriverTypes()` method is now obsolete. Use `GetRegisteredDriverNames()` or `GetRegisteredDrivers()` instead for AOT-friendly, reflection-free driver discovery.

Architecture[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#architecture)
------------------------------------------------------------------------------------

### Driver Registry[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#driver-registry)

Terminal.Gui v2 uses a **Driver Registry** pattern for managing available drivers without reflection. The registry provides:

* **Type-safe driver names** via `DriverRegistry.Names` constants
* **Driver metadata** including display names, descriptions, and supported platforms
* **AOT compatibility** - no reflection, fully ahead-of-time compilation friendly
* **Extensibility** - custom drivers can be registered via `DriverRegistry.Register()`

```
// Access well-known driver name constants
string windowsDriver = DriverRegistry.Names.WINDOWS;  // "windows"
string dotnetDriver = DriverRegistry.Names.DOTNET;    // "dotnet"
string ansiDriver = DriverRegistry.Names.ANSI;        // "ansi"

// Get detailed driver information
if (DriverRegistry.TryGetDriver(DriverRegistry.Names.WINDOWS, out DriverRegistry.DriverDescriptor descriptor))
{
    Logging.Information($"Found: {descriptor.DisplayName}");
    Logging.Information($"Description: {descriptor.Description}");
    
    // Check if supported on current platform
    bool isSupported = descriptor.SupportedPlatforms.Contains(Environment.OSVersion.Platform);
}

// Get drivers supported on current platform
foreach (DriverRegistry.DriverDescriptor driver in DriverRegistry.GetSupportedDrivers())
{
    Logging.Information($"{driver.Name} - {driver.DisplayName}");
}

// Get the default driver for current platform
DriverRegistry.DriverDescriptor defaultDriver = DriverRegistry.GetDefaultDriver();
Logging.Information($"Default driver: {defaultDriver.Name}");
```

[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html# "Copy")

### Component Factory Pattern[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#component-factory-pattern)

The v2 driver architecture uses the **Component Factory** pattern to create platform-specific components. Each driver has a corresponding factory that implements `IComponentFactory<T>`:

* `NetComponentFactory` - Creates components for DotNetDriver
* `WindowsComponentFactory` - Creates components for WindowsDriver
* `AnsiComponentFactory` - Creates components for AnsiDriver (all platforms)

Each factory is responsible for:

* Creating driver-specific components (`IInput<T>`, `IOutput`, `IInputProcessor`, etc.)
* Providing the driver name via `GetDriverName()` (single source of truth for driver identity)
* Being registered in the `DriverRegistry` with metadata

The factory pattern ensures proper component creation and initialization while maintaining clean separation of concerns.

### Core Components[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#core-components)

Each driver is composed of specialized components, each with a single responsibility:

#### IInput<T>[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#iinputt)

Reads raw console input events from the terminal on a dedicated input thread. The generic type `T` represents the platform-specific input record type:

* `ConsoleKeyInfo` for DotNetDriver (from `Console.ReadKey()`)
* `WindowsConsole.InputRecord` for WindowsDriver (from `ReadConsoleInputW()`)
* `char` for AnsiDriver (raw bytes from `read()` syscall or `ReadFile()`)

Input runs on a separate thread managed by `MainLoopCoordinator`, continuously reading from the console and queueing events into a thread-safe `ConcurrentQueue<T>` to avoid blocking the UI thread.

#### IOutput[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#ioutput)

Renders the output buffer to the terminal. Platform-specific implementations:

* **NetOutput**: Uses `Console.Write()` with ANSI sequences (VT mode on Windows)
* **AnsiOutput**: Pure ANSI escape sequences via `WriteFile()` (Windows) or `write()` (Unix)

Responsibilities include:

* Writing characters, strings, and ANSI escape sequences
* Cursor positioning and visibility control
* Querying terminal window size
* Managing the active screen buffer

#### IInput Processor[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#iinputprocessor)

Translates raw console input into Terminal.Gui events:

* Converts raw input to [Key](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.Key.html) events (handles keyboard input)
* Parses ANSI escape sequences (mouse events, special keys)
* Generates `MouseEventArgs` for mouse input
* Handles platform-specific key mappings
* Uses `IKeyConverter<T>` to translate `TInputRecord` to [Key](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Input.Key.html):
* `AnsiKeyConverter` - For `char` input (AnsiDriver)
* `NetKeyConverter` - For `ConsoleKeyInfo` input (DotNetDriver)
* `WindowsKeyConverter` - For `WindowsConsole.InputRecord` input (WindowsDriver)

#### IOutput Buffer[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#ioutputbuffer)

Manages the screen buffer and drawing operations:

* Maintains the `Contents` array (what should be displayed)
* Provides methods like `AddRune()`, `AddStr()`, `Move()`, `FillRect()`
* Handles clipping regions
* Tracks dirty regions for efficient rendering

#### IWindow Size Monitor[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#iwindowsizemonitor)

Detects terminal size changes and raises `SizeChanged` events when the terminal is resized.

#### DriverFacade<T>[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#driverfacadet)

A unified facade that implements `IDriver` and coordinates all the components. This is what gets assigned to [Application](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.html)'s `Driver`.

### Threading Model[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#threading-model)

The driver architecture employs a **multi-threaded design** for optimal responsiveness:

```
┌─────────────────────────────────────────────┐
│         IApplication.Init()              │
│  Creates MainLoopCoordinator<T> with        │
│  ComponentFactory<T>                        │
└────────────────┬────────────────────────────┘
                 │
                 ├──────────────────┬───────────────────┐
                 │                  │                   │
        ┌────────▼────────┐ ┌──────▼─────────┐ ┌──────▼──────────┐
        │  Input Thread   │ │  Main UI Thread│ │ Driver          │
        │                 │ │                 │ │   Facade        │
        │ IInput   │ │ ApplicationMain│ │                 │
        │ reads console   │ │ Loop processes │ │ Coordinates all │
        │ input async     │ │ events, layout,│ │ components      │
        │ into queue      │ │ and rendering  │ │                 │
        └─────────────────┘ └────────────────┘ └─────────────────┘
```

[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html# "Copy")

* **Input Thread**: Started by `MainLoopCoordinator`, runs `IInput.Run()` which continuously reads console input and queues it into a thread-safe `ConcurrentQueue<T>`.

* **Main UI Thread**: Runs `ApplicationMainLoop.Iteration()` which:

    1. Processes input from the queue via `IInputProcessor`
    2. Executes timeout callbacks
    3. Checks for UI changes (layout/drawing)
    4. Renders updates via `IOutput`

This separation ensures that input is never lost and the UI remains responsive during intensive operations.

### Initialization Flow[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#initialization-flow)

When [Application](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.html)'s `Init()` is called:

1. **IApplication.Init()** is invoked
2. Creates a `MainLoopCoordinator<T>` with the appropriate `ComponentFactory<T>`
3. **MainLoopCoordinator.StartAsync()** begins:
    *Starts the input thread which creates `IInput<T>`
    *   Initializes the main UI loop which creates `IOutput`
    *Creates `DriverFacade<T>` and assigns to [IApplication](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.html)'s `Driver`
    *   Waits for both threads to be ready

4. Returns control to the application

### Shutdown Flow[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#shutdown-flow)

When [IApplication](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.IApplication.html)'s `Shutdown()` is called:

1. Cancellation token is triggered
2. Input thread exits its read loop
3. `IOutput` is disposed
4. Main thread waits for input thread to complete
5. All resources are cleaned up

Component Interfaces[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#component-interfaces)
----------------------------------------------------------------------------------------------------

### IDriver[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#idriver)

The main driver interface that the framework uses internally. `IDriver` is organized into logical regions:

#### Driver Lifecycle[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#driver-lifecycle)

* `Init()`, `Refresh()`, `End()` - Core lifecycle methods
* `GetName()`, `GetVersionInfo()` - Driver identification
* `Suspend()` - Platform-specific suspend support

#### Driver Components[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#driver-components)

* `InputProcessor` - Processes input into Terminal.Gui events
* `OutputBuffer` - Manages screen buffer state
* `SizeMonitor` - Detects terminal size changes
* `Clipboard` - OS clipboard integration

#### Screen and Display[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#screen-and-display)

* `Screen`, `Cols`, `Rows`, `Left`, `Top` - Screen dimensions
* `SetScreenSize()`, `SizeChanged` - Size management

#### Color Support[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#color-support)

* `SupportsTrueColor` - 24-bit color capability
* `Force16Colors` - Force 16-color mode
* `DefaultAttribute` - The terminal's actual default foreground/background colors, detected at startup via OSC 10/11 queries. Used by [Scheme](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.Scheme.html) to resolve [Color](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.Color.html)'s `None` during role derivation. `null` if the terminal didn't respond (e.g., legacy console).
* `ColorCapabilities` - The terminal's color capability level (`NoColor`, `Colors16`, `Colors256`, `TrueColor`), detected from `$TERM`, `$COLORTERM`, and other environment variables

#### Size Detection (ANSI Driver)[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#size-detection-ansi-driver)

The ANSI driver's terminal-size detection strategy is controlled by `Driver.SizeDetection` (a `[ConfigurationProperty]`):

| Mode | Mechanism | When to use |
| --- | --- | --- |
| `AnsiQuery` (default) | Sends `CSI 18t`, parses `ESC[8;h;wt` response. Async, ~500 ms throttle. | Most terminals. Works everywhere ANSI is supported. |
| `Polling` | `ioctl(TIOCGWINSZ)` on Unix, `Console.WindowWidth/Height` on Windows. Synchronous. | When the ANSI response does not reflect the actual terminal size (e.g., some SSH configurations). |

Set via JSON configuration:

```
{ "Driver.SizeDetection": "Polling" }
```

[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html# "Copy")
Or programmatically before `Init()`:

```
Driver.SizeDetection = SizeDetectionMode.Polling;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html# "Copy")

#### Content Buffer[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#content-buffer)

* `Contents` - Screen buffer array
* `Clip` - Clipping region
* `ClearContents()`, `ClearedContents` - Buffer management

#### Drawing and Rendering[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#drawing-and-rendering)

* `Col`, `Row`, `CurrentAttribute` - Drawing state
* `Move()`, `AddRune()`, `AddStr()`, `FillRect()` - Drawing operations
* `SetAttribute()`, `GetAttribute()` - Attribute management
* `WriteRaw()`, `GetSixels()` - Raw output and graphics
* `Refresh()`, `ToString()`, `ToAnsi()` - Output rendering

#### Cursor[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#cursor)

Drivers implement cursor control through `IDriver` which delegates to `IOutput`:

* `SetCursor(Cursor cursor)` - Set cursor position and style atomically
* `GetCursor()` - Get current cursor state
* `SetCursorNeedsUpdate(bool)` / `GetCursorNeedsUpdate()` - Optimization flag for cursor updates

##### Note

The cursor system is managed by `ApplicationNavigation`. Drivers implement the low-level cursor control; views use the [View](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.ViewBase.View.html)'s `Cursor` property. See [Cursor Management](https://gui-cs.github.io/Terminal.Gui/docs/cursor.html) for complete details.

#### Input Events[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#input-events)

* `KeyDown` - Raised for key press and repeat events
* `KeyUp` - Raised for key release events (only when the driver supports it — currently the ANSI driver with kitty keyboard protocol)
* `MouseEvent` - Raised for mouse input events

##### Note

For testing, use the input injection API. See [Input Injection](https://gui-cs.github.io/Terminal.Gui/docs/input-injection.html) for details.

#### Kitty Keyboard Protocol[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#kitty-keyboard-protocol)

The ANSI driver detects and enables the [kitty keyboard protocol](https://sw.kovidgoyal.net/kitty/keyboard-protocol/) at startup when the terminal supports it. This provides:

* **Disambiguated escape codes** (flag 1) — eliminates ambiguity in legacy ANSI key sequences
* **Event type reporting** (flag 2) — press, repeat, and release events via `Key.EventType`
* **Standalone modifier key events** — pressing Shift, Ctrl, Alt alone generates events with `Key.IsModifierOnly == true` and `Key.ModifierKey` identifying the specific modifier (e.g. `ModifierKey.LeftShift`)

Detection uses the `KittyKeyboardProtocolDetector` which queries the terminal via CSI `?u`. If supported, the protocol is enabled with flags 1+2. On shutdown, the protocol is disabled to restore normal terminal behavior.

Three ANSI parser patterns handle kitty event types: `KittyKeyboardPattern` (CSI `u`), `CsiKeyPattern` (CSI `~`), and `CsiCursorPattern` (CSI cursor letters). Release events route to `KeyUp`; press and repeat route to `KeyDown`.

#### ANSI Escape Sequences[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#ansi-escape-sequences)

* `QueueAnsiRequest()` - ANSI request handling

**Note:** The driver is internal to Terminal.Gui. View classes should not access `Driver` directly. Instead:

* Use [Application](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.App.Application.html)'s `Screen` to get screen dimensions
* Use `Move()` for positioning (with viewport-relative coordinates)
* Use `AddRune()` and `AddStr()` for drawing
* ViewBase infrastructure classes (in `Terminal.Gui/ViewBase/`) can access Driver when needed for framework implementation

### Driver Creation and Selection[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#driver-creation-and-selection)

The driver selection logic in `ApplicationImpl.Driver.cs` uses the **Driver Registry** to select and instantiate drivers:

**Selection Priority Order:**

1. **Provided Component Factory**: If an `IComponentFactory` is explicitly provided to `ApplicationImpl`, it determines the driver via `factory.GetDriverName()`
2. **Driver Name Parameter**: The `driverName` parameter passed to `Init()` is looked up in the registry
3. **Application.ForceDriver Configuration**: The `Application.ForceDriver` property is checked and looked up in the registry
4. **Platform Default**: `DriverRegistry.GetDefaultDriver()` selects based on current platform:
    *Windows (Win32NT, Win32S, Win32Windows) → `WindowsDriver`
    *   Unix/Linux/macOS → `AnsiDriver`
    *   Other platforms → `DotNetDriver` (fallback)

**Driver Creation Process:**

```
// Example of how driver creation works internally
DriverRegistry.DriverDescriptor descriptor;

if (DriverRegistry.TryGetDriver(driverName, out descriptor))
{
    // Create factory using descriptor's factory function
    IComponentFactory factory = descriptor.CreateFactory();
    
    // Factory creates all driver components
    MainLoopCoordinator<TInputRecord> coordinator = new (
        timedEvents,
        inputQueue,
        mainLoop,
        factory  // Factory knows its driver name via GetDriverName()
    );
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html# "Copy")
This architecture provides:

* **Deterministic behavior** - clear priority order for driver selection
* **Flexibility** - multiple ways to specify a driver
* **Type safety** - use `DriverRegistry.Names` constants instead of strings
* **Extensibility** - custom drivers can register themselves
* **AOT compatibility** - no reflection required

Testing and Input Injection[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html#testing-and-input-injection)
------------------------------------------------------------------------------------------------------------------

For comprehensive documentation on testing Terminal.Gui applications with input injection, virtual time control, and deterministic testing, see [Input Injection](https://gui-cs.github.io/Terminal.Gui/docs/input-injection.html).

**Quick Summary:**

* Use the **ANSI driver** for testing - it's cross-platform and deterministic
* Use **Virtual Time** (`VirtualTimeProvider`) for timing control
* The default **Direct Mode** is fastest for most tests
* Use **Pipeline Mode** only when testing ANSI encoding/parsing

**Example:**

```
VirtualTimeProvider time = new ();
using IApplication app = Application.Create(time);
app.Init(DriverRegistry.Names.ANSI);

// Inject input
app.InjectKey(Key.Enter);
app.InjectMouse(new () { Flags = MouseFlags.LeftButtonPressed, ScreenPosition = new (5, 5) });

// Verify behavior
Assert.True(eventFired);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html# "Copy")
See [Input Injection](https://gui-cs.github.io/Terminal.Gui/docs/input-injection.html) for:

* Complete API documentation
* Testing patterns and best practices
* Virtual time control details
* Injection modes (Direct vs Pipeline)
* Troubleshooting guide
