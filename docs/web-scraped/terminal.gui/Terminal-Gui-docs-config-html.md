# Source: https://gui-cs.github.io/Terminal.Gui/docs/config.html

Title: Configuration Management Deep Dive | Terminal.Gui v2

URL Source: https://gui-cs.github.io/Terminal.Gui/docs/config.html

Markdown Content:
Terminal.Gui provides a comprehensive configuration system that allows users and developers to customize application behavior and appearance through JSON configuration files. The [ConfigurationManager](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigurationManager.html) enables persistent settings, themes, and application-specific preferences.

Table of Contents[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#table-of-contents)
---------------------------------------------------------------------------------------------

* [Overview](https://gui-cs.github.io/Terminal.Gui/docs/config.html#overview)
* [Getting Started](https://gui-cs.github.io/Terminal.Gui/docs/config.html#getting-started)
* [Configuration Scopes](https://gui-cs.github.io/Terminal.Gui/docs/config.html#configuration-scopes)
* [Configuration Locations and Precedence](https://gui-cs.github.io/Terminal.Gui/docs/config.html#configuration-locations-and-precedence)
* [Themes and Schemes](https://gui-cs.github.io/Terminal.Gui/docs/config.html#themes-and-schemes)
* [Defining Configuration Properties](https://gui-cs.github.io/Terminal.Gui/docs/config.html#defining-configuration-properties)
* [Loading and Applying Configuration](https://gui-cs.github.io/Terminal.Gui/docs/config.html#loading-and-applying-configuration)
* [Events](https://gui-cs.github.io/Terminal.Gui/docs/config.html#events)
* [What Can Be Configured](https://gui-cs.github.io/Terminal.Gui/docs/config.html#what-can-be-configured)
* [Configuration File Format](https://gui-cs.github.io/Terminal.Gui/docs/config.html#configuration-file-format)
* [Best Practices](https://gui-cs.github.io/Terminal.Gui/docs/config.html#best-practices)

* * *

Overview[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#overview)
---------------------------------------------------------------------------

The [ConfigurationManager](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigurationManager.html) provides:

* **Persistent Settings** - User preferences stored in JSON files
* **Theme System** - Named collections of visual settings
* **Scheme Management** - Color and text style definitions
* **Configuration Precedence** - Layered configuration from multiple sources
* **Runtime Configuration** - In-memory configuration without files
* **AOT Compatible** - Works with Native AOT compilation

### Key Features[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#key-features)

* JSON-based configuration with schema validation
* Multiple configuration locations (user home, app directory, resources)
* Process-wide settings using static properties
* Built-in themes (Default, Dark, Light, etc.)
* Custom glyphs and Unicode characters
* Event-driven configuration changes

* * *

Getting Started[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#getting-started)
-----------------------------------------------------------------------------------------

### Enabling Configuration[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#enabling-configuration)

**ConfigurationManager is disabled by default** and must be explicitly enabled:

```
using Terminal.Gui.Configuration;

class Program
{
    static void Main()
    {
        // Enable configuration with all sources
        ConfigurationManager.Enable(ConfigLocations.All);

        using IApplication app = Application.Create();
        app.Init();
        // ... rest of app
    }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### Quick Example[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#quick-example)

```
// Enable configuration
ConfigurationManager.Enable(ConfigLocations.All);

// Listen for configuration changes
ConfigurationManager.Applied += (sender, e) => 
{
    Console.WriteLine("Configuration applied!");
};

// Switch themes
ThemeManager.Theme = "Dark";
ConfigurationManager.Apply();
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

* * *

Configuration Scopes[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#configuration-scopes)
---------------------------------------------------------------------------------------------------

Terminal.Gui uses three configuration scopes, each serving a different purpose:

### 1. Settings Scope[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#1-settingsscope)

System-level settings that affect Terminal.Gui behavior. Only Terminal.Gui library developers can define [SettingsScope](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.SettingsScope.html) properties.

```
[ConfigurationProperty(Scope = typeof(SettingsScope))]
public static bool Force16Colors { get; set; } = false;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")
**Examples:**

* `Application.DefaultKeyBindings` (e.g. `Command.Quit`) - Default keys for application-level commands
* `Application.Force16Colors` - Force 16-color mode
* `Key.Separator` - Character separating keys in key combinations

### 2. Theme Scope[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#2-themescope)

Visual appearance settings that can be themed. Only Terminal.Gui library developers can define [ThemeScope](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ThemeScope.html) properties.

```
[ConfigurationProperty(Scope = typeof(ThemeScope))]
public static LineStyle DefaultBorderStyle { get; set; } = LineStyle.Single;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")
**Examples:**

* `Window.DefaultBorderStyle` - Default border style for windows
* `Dialog.DefaultShadow` - Default shadow style for dialogs
* [Schemes](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.Schemes.html) - Color schemes for the theme

### 3. App Settings Scope (Default)[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#3-appsettingsscope-default)

Application-specific settings. Application developers can define [AppSettingsScope](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.AppSettingsScope.html) properties for their apps.

```
[ConfigurationProperty] // AppSettingsScope is default
public static string MyAppSetting { get; set; } = "default value";
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")
**Important:**

* App developers **cannot** define [Settings Scope](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.SettingsScope.html) or [Theme Scope](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ThemeScope.html) properties
* AppSettings property names must be globally unique (automatically prefixed with class name)

* * *

Configuration Locations and Precedence[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#configuration-locations-and-precedence)
---------------------------------------------------------------------------------------------------------------------------------------

Configuration is loaded from multiple locations with increasing precedence (higher numbers override lower):

### Config Locations Enum[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#configlocations-enum)

[ConfigLocations](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigLocations.html) specifies where configuration can be loaded from:

1. **[ConfigLocations.HardCoded](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigLocations.html)** (Lowest Precedence)

    *   Default values in code (static property initializers)
    *   Always available, even when ConfigurationManager is disabled

2.   **[ConfigLocations.LibraryResources](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigLocations.html)**

    *   Settings in `Terminal.Gui.dll` resources (`Terminal.Gui.Resources.config.json`)
    *   Defines default themes and settings for the library

3.   **[ConfigLocations.AppResources](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigLocations.html)**

    *   App-specific resources (`MyApp.Resources.config.json` or `Resources/config.json`)
    *   Embedded in the application assembly

4.   **[ConfigLocations.GlobalHome](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigLocations.html)**

    *   Global file in user's home directory (`~/.tui/config.json`)

5.   **[ConfigLocations.GlobalCurrent](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigLocations.html)**

    *   Global file in current directory (`./.tui/config.json`)

6.   **[ConfigLocations.AppHome](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigLocations.html)**

    *   App-specific file in user's home directory (`~/.tui/MyApp.config.json`)

7.   **[ConfigLocations.AppCurrent](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigLocations.html)**

    *   App-specific file in current directory (`./.tui/MyApp.config.json`)

8.   **[ConfigLocations.Env](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigLocations.html)**

    *   Settings from the `TUI_CONFIG` environment variable
    *   Useful for container environments and CI/CD pipelines

9.   **[ConfigLocations.Runtime](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigLocations.html)** (Highest Precedence)

    *   Settings in [Configuration Manager](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigurationManager.html)'s `RuntimeConfig` string property
    *   In-memory configuration without files

### Precedence Diagram[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#precedence-diagram)

### File Locations[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#file-locations)

**Global Settings** (`config.json`):

* Windows: `C:\Users\username\.tui\config.json`
* macOS/Linux: `~/.tui/config.json` or `./.tui/config.json`

**App-Specific Settings** (`AppName.config.json`):

* Windows: `C:\Users\username\.tui\UICatalog.config.json`
* macOS/Linux: `~/.tui/UICatalog.config.json` or `./.tui/UICatalog.config.json`

**Environment Variable** (`TUI_CONFIG`):

```
# Linux/macOS
export TUI_CONFIG='{"Application.DefaultKeyBindings": {"Quit": {"All": ["Ctrl+Q"]}}}'

# Windows PowerShell
$env:TUI_CONFIG='{"Application.DefaultKeyBindings": {"Quit": {"All": ["Ctrl+Q"]}}}'
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

* * *

Themes and Schemes[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#themes-and-schemes)
-----------------------------------------------------------------------------------------------

### Theme System[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#theme-system)

A **Theme** is a named collection of visual settings bundled together. Terminal.Gui includes several built-in themes.

#### Built-in Themes[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#built-in-themes)

* **Default** - The default Terminal.Gui theme (matches hard-coded defaults)
* **Dark** - Dark color scheme with heavy borders
* **Light** - Light color scheme
* **TurboPascal 5** - Classic Turbo Pascal IDE colors
* **And more** - See `Terminal.Gui/Resources/config.json` for all built-in themes

#### Using Themes[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#using-themes)

```
// Get current theme
ThemeScope currentTheme = ThemeManager.GetCurrentTheme();

// Get all available themes
Dictionary<string, ThemeScope> themes = ThemeManager.GetThemes();

// Get theme names
ImmutableList<string> themeNames = ThemeManager.GetThemeNames();

// Switch themes
ThemeManager.Theme = "Dark";
ConfigurationManager.Apply();

// Listen for theme changes
ThemeManager.ThemeChanged += (sender, e) => 
{
    // Update UI based on new theme
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### Scheme System[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#scheme-system)

A **Scheme** defines the colors and text styles for a specific UI context (e.g., Dialog, Menu, Runnable).

See the [Scheme Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/scheme.html) for complete details on the scheme system.

#### Built-in Schemes[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#built-in-schemes)

[Schemes](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.Schemes.html) enum defines the standard schemes:

* **Runnable** - Top-level application windows
* **Base** - Default for most views
* **Dialog** - Dialogs and message boxes
* **Menu** - Menus and status bars
* **Error** - Error messages and dialogs

#### Working with Schemes[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#working-with-schemes)

```
// Get all schemes for current theme
Dictionary<string, Scheme> schemes = SchemeManager.GetCurrentSchemes();

// Get specific scheme
Scheme dialogScheme = SchemeManager.GetScheme(Schemes.Dialog);

// Get scheme names
ImmutableList<string> schemeNames = SchemeManager.GetSchemeNames();

// Add custom scheme
SchemeManager.AddScheme("MyScheme", new Scheme
{
    Normal = new Attribute(Color.White, Color.Blue),
    Focus = new Attribute(Color.Black, Color.Cyan)
});

// Listen for scheme changes
SchemeManager.CollectionChanged += (sender, e) => 
{
    // Handle scheme changes
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

#### Scheme Structure[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#scheme-structure)

Each [Scheme](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.Scheme.html) maps [VisualRole](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.VisualRole.html) to [Attribute](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.Attribute.html):

```
{
  "Runnable": {
    "Normal": {
      "Foreground": "BrightGreen",
      "Background": "Black",
      "Style": "None"
    },
    "Focus": {
      "Foreground": "White",
      "Background": "Cyan",
      "Style": "Bold"
    },
    "HotNormal": {
      "Foreground": "Yellow",
      "Background": "Black"
    },
    "HotFocus": {
      "Foreground": "Blue",
      "Background": "Cyan",
      "Style": "Underline"
    },
    "Disabled": {
      "Foreground": "DarkGray",
      "Background": "Black",
      "Style": "Faint"
    }
  }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

* * *

Defining Configuration Properties[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#defining-configuration-properties)
-----------------------------------------------------------------------------------------------------------------------------

### Basic Property Definition[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#basic-property-definition)

Application developers define settings using the [ConfigurationPropertyAttribute](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigurationPropertyAttribute.html):

```
public class MyApp
{
    [ConfigurationProperty]
    public static string MySetting { get; set; } = "Default Value";
    
    [ConfigurationProperty]
    public static int MaxItems { get; set; } = 100;
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")
**Requirements:**

* Must be `public` or `internal`
* Must be `static`
* Must be a property (not a field)
* Must have a default value

### Property Naming[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#property-naming)

AppSettings properties are automatically prefixed with the class name to ensure global uniqueness:

```
// Code
public class MyApp
{
    [ConfigurationProperty]
    public static string MySetting { get; set; } = "value";
}

// JSON
{
  "AppSettings": {
    "MyApp.MySetting": "value"
  }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### Scope Specification[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#scope-specification)

Use the `Scope` parameter to specify non-default scopes (Terminal.Gui library only):

```
// SettingsScope - Library-wide settings
[ConfigurationProperty(Scope = typeof(SettingsScope))]
public static bool Force16Colors { get; set; } = false;

// ThemeScope - Visual settings
[ConfigurationProperty(Scope = typeof(ThemeScope))]
public static LineStyle DefaultBorderStyle { get; set; } = LineStyle.Single;

// AppSettingsScope - Application settings (default)
[ConfigurationProperty] // or explicitly: Scope = typeof(AppSettingsScope)
public static string MyAppSetting { get; set; } = "default";
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### Omit Class Name (Advanced)[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#omit-class-name-advanced)

For library developers only, use `OmitClassName = true` for cleaner JSON:

```
[ConfigurationProperty(Scope = typeof(ThemeScope), OmitClassName = true)]
public static Dictionary<string, Scheme> Schemes { get; set; } = new();
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

* * *

Loading and Applying Configuration[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#loading-and-applying-configuration)
-------------------------------------------------------------------------------------------------------------------------------

### Enable with Load and Apply[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#enable-with-load-and-apply)

The simplest approach - enable and load in one call:

```
ConfigurationManager.Enable(ConfigLocations.All);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")
This:

1. Enables ConfigurationManager
2. Loads configuration from all locations
3. Applies settings to the application

### Granular Control[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#granular-control)

For more control, use [Configuration Manager](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigurationManager.html)'s `Load` and `Apply()` separately:

```
// Enable without loading
ConfigurationManager.Enable(ConfigLocations.None);

// Load from specific locations
ConfigurationManager.Load(ConfigLocations.GlobalHome | ConfigLocations.AppResources);

// Apply settings
ConfigurationManager.Apply();
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### Runtime Configuration[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#runtime-configuration)

Set configuration directly in code without files:

```
ConfigurationManager.RuntimeConfig = @"
{
  ""Application.DefaultKeyBindings.Quit"": ""Ctrl+Q"",
  ""Application.Force16Colors"": true
}";

ConfigurationManager.Enable(ConfigLocations.Runtime);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### Reset to Defaults[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#reset-to-defaults)

Reset all settings to hard-coded defaults:

```
ConfigurationManager.ResetToHardCodedDefaults();
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

* * *

Events[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#events)
-----------------------------------------------------------------------

The ConfigurationManager provides events to track configuration changes:

### Applied Event[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#applied-event)

Raised after configuration is applied to the application:

```
ConfigurationManager.Applied += (sender, e) => 
{
    // Configuration has been applied
    // Update UI or refresh views
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### Theme Changed Event[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#themechanged-event)

Raised when the active theme changes:

```
ThemeManager.ThemeChanged += (sender, e) => 
{
    // Theme has changed
    // Refresh all views to use new theme
    // From within a View, use: App?.Current?.SetNeedsDraw();
    // Or access via IApplication instance: app.Current?.SetNeedsDraw();
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### Collection Changed Event[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#collectionchanged-event)

Raised when schemes collection changes:

```
SchemeManager.CollectionChanged += (sender, e) => 
{
    // Schemes have changed
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

* * *

What Can Be Configured[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#what-can-be-configured)
-------------------------------------------------------------------------------------------------------

### Application Settings[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#application-settings)

System-wide settings from [SettingsScope](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.SettingsScope.html):

```
{
  "Application.DefaultKeyBindings.Quit": "Esc",
  "Application.Force16Colors": false,
  "Application.IsMouseDisabled": false,
  "Application.DefaultKeyBindings.Arrange": "Ctrl+F5",
  "Application.DefaultKeyBindings.NextTabStop": "Tab",
  "Application.DefaultKeyBindings.PreviousTabStop": "Shift+Tab",
  "Application.DefaultKeyBindings.NextTabGroup": "F6",
  "Application.DefaultKeyBindings.PreviousTabGroup": "Shift+F6",
  "Key.Separator": "+"
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### Key Binding Settings[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#key-binding-settings)

Configurable key bindings use the `PlatformKeyBinding` format to support platform-aware defaults. See [Key Binding Overrides](https://gui-cs.github.io/Terminal.Gui/docs/config.html#key-binding-overrides) for the full JSON format.

```
{
  "Application.DefaultKeyBindings": {
    "Quit": { "All": ["Esc"] },
    "Suspend": { "Linux": ["Ctrl+Z"], "Macos": ["Ctrl+Z"] },
    "Arrange": { "All": ["Ctrl+F5"] }
  },
  "View.DefaultKeyBindings": {
    "Copy": { "All": ["Ctrl+C"] },
    "Undo": { "All": ["Ctrl+Z"], "Linux": ["Ctrl+/"], "Macos": ["Ctrl+/"] }
  },
  "View.ViewKeyBindings": {
    "TextField": {
      "CutToEndOfLine": { "All": ["Ctrl+K"] }
    }
  }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### View-Specific Settings[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#view-specific-settings)

Settings for individual View types from [ThemeScope](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ThemeScope.html):

```
{
  "Window.DefaultBorderStyle": "Single",
  "Window.DefaultShadow": "None",
  "Dialog.DefaultBorderStyle": "Heavy",
  "Dialog.DefaultShadow": "Transparent",
  "Dialog.DefaultButtonAlignment": "End",
  "FrameView.DefaultBorderStyle": "Rounded",
  "Button.DefaultShadow": "None",
  "PopoverMenu.DefaultKey": "Shift+F10",
  "FileDialog.MaxSearchResults": 10000
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### Glyphs[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#glyphs)

Customize the Unicode characters used for drawing:

```
{
  "Glyphs.RightArrow": "►",
  "Glyphs.LeftArrow": "U+25C4",
  "Glyphs.DownArrow": "\\u25BC",
  "Glyphs.UpArrow": 965010,
  "Glyphs.LeftBracket": "[",
  "Glyphs.RightBracket": "]",
  "Glyphs.Checked": "☑",
  "Glyphs.UnChecked": "☐",
  "Glyphs.Selected": "◉",
  "Glyphs.UnSelected": "○"
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")
Glyphs can be specified as:

* Unicode character: `"►"`
* U+ format: `"U+25C4"`
* UTF-16 format: `"\\u25BC"`
* Decimal codepoint: `965010`

### Key Binding Overrides[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#key-binding-overrides)

Key bindings for Application-level commands, base View commands, and per-view commands can all be overridden in configuration. See [Keyboard Deep Dive - Configurable Key Bindings](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html#configurable-key-bindings) for the full architecture.

**Override Application-level key bindings** (e.g., change the Quit key):

```
{
  "Application.DefaultKeyBindings": {
    "Quit": { "All": ["Ctrl+Q"] },
    "Suspend": { "Linux": ["Ctrl+Z"], "Macos": ["Ctrl+Z"] }
  }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")
**Override base View key bindings** (affects all views that support those commands):

```
{
  "View.DefaultKeyBindings": {
    "Copy": { "All": ["Ctrl+C", "Ctrl+Insert"] },
    "Paste": { "All": ["Ctrl+V", "Shift+Insert"] },
    "Undo": { "All": ["Ctrl+Z"], "Linux": ["Ctrl+/"], "Macos": ["Ctrl+/"] }
  }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")
**Override per-view key bindings** using `View.ViewKeyBindings` (maps view type name to command overrides):

```
{
  "View.ViewKeyBindings": {
    "TextField": {
      "Undo": { "All": ["Ctrl+Z"] },
      "CutToEndOfLine": { "All": ["Ctrl+K"] }
    },
    "TextView": {
      "Redo": { "All": ["Ctrl+Shift+Z"], "Windows": ["Ctrl+Y"] }
    }
  }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")
Each entry uses the `PlatformKeyBinding` format with optional `All`, `Windows`, `Linux`, and `Macos` string arrays. `All` keys apply on every platform; platform-specific arrays add additional bindings for that OS.

### Discovering Configuration Properties[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#discovering-configuration-properties)

To find all available configuration properties:

```
// Get hard-coded configuration
SettingsScope hardCoded = ConfigurationManager.GetHardCodedConfig();

// Iterate through all properties
foreach (var property in hardCoded)
{
    Console.WriteLine($"{property.Key} = {property.Value}");
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")
Or search the source code for `[ConfigurationProperty]` attributes.

* * *

Themes and Schemes[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#themes-and-schemes-1)
-------------------------------------------------------------------------------------------------

### Theme Structure[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#theme-structure)

A theme is a named collection bundling visual settings and schemes:

```
{
  "Themes": [
    {
      "Dark": {
        "Dialog.DefaultBorderStyle": "Heavy",
        "Dialog.DefaultShadow": "Transparent",
        "Window.DefaultBorderStyle": "Single",
        "Button.DefaultShadow": "Opaque",
        "Schemes": [
          {
            "Runnable": {
              "Normal": { "Foreground": "BrightGreen", "Background": "Black" },
              "Focus": { "Foreground": "White", "Background": "Cyan" }
            },
            "Dialog": {
              "Normal": { "Foreground": "Black", "Background": "Gray" }
            }
          }
        ]
      }
    }
  ]
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### Creating Custom Themes[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#creating-custom-themes)

Custom themes can be defined in configuration files:

```
{
  "Themes": [
    {
      "MyCustomTheme": {
        "Window.DefaultBorderStyle": "Double",
        "Dialog.DefaultShadow": "Opaque",
        "Schemes": [
          {
            "Base": {
              "Normal": {
                "Foreground": "Cyan",
                "Background": "Black",
                "Style": "Bold"
              }
            }
          }
        ]
      }
    }
  ]
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")
Then activate the theme:

```
ThemeManager.Theme = "MyCustomTheme";
ConfigurationManager.Apply();
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### Theme Inheritance[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#theme-inheritance)

Themes only override specified properties. To build on an existing theme:

```
// Start with default theme
ThemeManager.Theme = "Default";
ConfigurationManager.Apply();

// Apply custom theme (overrides only what's specified)
ThemeManager.Theme = "MyCustomTheme";
ConfigurationManager.Apply();
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### Text Style in Schemes[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#textstyle-in-schemes)

Each [Attribute](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.Attribute.html) in a scheme now includes [TextStyle](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Drawing.TextStyle.html):

```
{
  "Normal": {
    "Foreground": "White",
    "Background": "Blue",
    "Style": "Bold, Underline"
  }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")
Available styles (combinable):

* `None`
* `Bold`
* `Faint`
* `Italic`
* `Underline`
* `Blink`
* `Reverse`
* `Strikethrough`

* * *

Configuration File Format[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#configuration-file-format)
-------------------------------------------------------------------------------------------------------------

### Schema[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#schema)

All configuration files must conform to the JSON schema:

**Schema URL:**[https://gui-cs.github.io/Terminal.Gui/schemas/tui-config-schema.json](https://gui-cs.github.io/Terminal.Gui/schemas/tui-config-schema.json)

### Root Structure[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#root-structure)

```
{
  "$schema": "https://gui-cs.github.io/Terminal.Gui/schemas/tui-config-schema.json",
  
  // SettingsScope properties
  "Application.DefaultKeyBindings.Quit": "Esc",
  "Application.Force16Colors": false,
  
  // Current theme name
  "Theme": "Dark",
  
  // Theme definitions
  "Themes": [
    {
      "Dark": {
        // ThemeScope properties
        "Window.DefaultBorderStyle": "Single",
        // Schemes
        "Schemes": [ ... ]
      }
    }
  ],
  
  // AppSettings
  "AppSettings": {
    "MyApp.MySetting": "value"
  }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")
Best Practices[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#best-practices)
---------------------------------------------------------------------------------------

### For Application Developers[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#for-application-developers)

**1. Enable Early**

Enable ConfigurationManager at the start of `Main()`, before creating the application:

```
static void Main()
{
    ConfigurationManager.Enable(ConfigLocations.All);
    using IApplication app = Application.Create();
    app.Init();
    // ...
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")
**2. Use AppSettings for App Configuration**

```
public class MyApp
{
    [ConfigurationProperty]
    public static bool ShowWelcomeMessage { get; set; } = true;
    
    [ConfigurationProperty]
    public static string DefaultDirectory { get; set; } = "";
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")
**3. Ship Default Configuration as Resource**

Include a `Resources/config.json` file in your app:

```
<ItemGroup>
  <EmbeddedResource Include="Resources\config.json" />
</ItemGroup>
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")
**4. Handle Configuration Changes**

```
ConfigurationManager.Applied += (sender, e) => 
{
    // Refresh UI when configuration changes
    RefreshAllViews();
};
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### For Library Developers[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#for-library-developers)

**1. Use Appropriate Scopes**

* [Settings Scope](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.SettingsScope.html) - For system-wide behavior
* [Theme Scope](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ThemeScope.html) - For visual appearance that should be themeable
* Don't use `AppSettingsScope` in library code

**2. Provide Meaningful Defaults**

```
[ConfigurationProperty(Scope = typeof(ThemeScope))]
public static LineStyle DefaultBorderStyle { get; set; } = LineStyle.Single;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")
**3. Document Configuration Properties**

```
/// <summary>
///     Gets or sets the default border style for all Windows.
/// </summary>
[ConfigurationProperty(Scope = typeof(ThemeScope))]
public static LineStyle DefaultBorderStyle { get; set; } = LineStyle.Single;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### Process-Wide Settings[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#process-wide-settings)

##### Important

Configuration settings are applied at the **process level**.

Since configuration properties are static, changes affect all applications in the same process. This is typically not an issue for normal applications, but can affect scenarios with:

* Multiple Terminal.Gui apps in the same process
* Unit tests running in parallel
* Hot reload scenarios

* * *

Advanced Topics[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#advanced-topics)
-----------------------------------------------------------------------------------------

### JSON Error Handling[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#json-error-handling)

Control how JSON parsing errors are handled:

```
{
  "ConfigurationManager.ThrowOnJsonErrors": true
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

* `false` (default) - Silent failures, errors logged
* `true` - Throws exceptions on JSON parsing errors

### Manually Trigger Updates[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#manually-trigger-updates)

Update ConfigurationManager to reflect current static property values:

```
// Change a setting programmatically
Application.DefaultKeyBindings[Command.Quit] = Bind.All (Key.Q.WithCtrl);

// Update ConfigurationManager to reflect the change
ConfigurationManager.UpdateToCurrentValues();

// Save to file (if needed)
string json = ConfigurationManager.Serialize();
File.WriteAllText("my-config.json", json);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### Disable Configuration Manager[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#disable-configurationmanager)

Disable and optionally reset to defaults:

```
// Disable but keep current settings
ConfigurationManager.Disable(resetToHardCodedDefaults: false);

// Disable and reset to hard-coded defaults
ConfigurationManager.Disable(resetToHardCodedDefaults: true);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### File System Watching[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#file-system-watching)

Watch for configuration file changes:

```
var watcher = new FileSystemWatcher(
    Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), ".tui"));
watcher.Filter = "*.json";
watcher.Changed += (s, e) => 
{
    ConfigurationManager.Load(ConfigLocations.GlobalHome);
    ConfigurationManager.Apply();
};
watcher.EnableRaisingEvents = true;
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")
See UICatalog's `ConfigurationEditor` scenario for a complete example.

* * *

Examples[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#examples)
---------------------------------------------------------------------------

### Example 1: Simple Theme Switching[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#example-1-simple-theme-switching)

```
using Terminal.Gui;
using Terminal.Gui.Configuration;

ConfigurationManager.Enable(ConfigLocations.All);
Application.Init();

var themeSelector = new OptionSelector<string>
{
    X = 1,
    Y = 1,
};
themeSelector.SetSource(ThemeManager.GetThemeNames());
themeSelector.SelectedItemChanged += (s, e) =>
{
    ThemeManager.Theme = e.Value.ToString();
    ConfigurationManager.Apply();
};

Application.Run(new Window { Title = "Theme Demo" }).Add(themeSelector);
Application.Shutdown();
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### Example 2: Custom Application Settings[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#example-2-custom-application-settings)

```
public class MyApp
{
    [ConfigurationProperty]
    public static string LastOpenedFile { get; set; } = "";
    
    [ConfigurationProperty]
    public static int WindowWidth { get; set; } = 80;
    
    [ConfigurationProperty]
    public static int WindowHeight { get; set; } = 25;
}

// Enable and use
ConfigurationManager.Enable(ConfigLocations.All);

// Settings are automatically loaded and applied
var window = new Window
{
    Width = MyApp.WindowWidth,
    Height = MyApp.WindowHeight
};

// Later, save updated settings
MyApp.WindowWidth = 100;
ConfigurationManager.UpdateToCurrentValues();
// Could save to file here
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

### Example 3: Runtime Configuration[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#example-3-runtime-configuration)

```
ConfigurationManager.RuntimeConfig = @"
{
  ""Application.DefaultKeyBindings"": {
    ""Quit"": { ""All"": [""Ctrl+Q""] }
  },
  ""Driver.Force16Colors"": true,
  ""Theme"": ""Dark""
}";

ConfigurationManager.Enable(ConfigLocations.Runtime);

// Settings are now applied
// Quit key is Ctrl+Q
// 16-color mode is forced
// Dark theme is active
```

[](https://gui-cs.github.io/Terminal.Gui/docs/config.html# "Copy")

* * *

See Also[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#see-also)
---------------------------------------------------------------------------

* **[Scheme Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/scheme.html)** - Color scheme details
* **[Drawing Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/drawing.html)** - Color and attribute system
* **[View Deep Dive](https://gui-cs.github.io/Terminal.Gui/docs/View.html)** - View configuration properties
* **[Theme Schema](https://gui-cs.github.io/Terminal.Gui/schemas/tui-config-schema.json)** - JSON schema for validation
* **[Default Config](https://raw.githubusercontent.com/gui-cs/Terminal.Gui/v2_develop/Terminal.Gui/Resources/config.json)** - Complete default configuration

### UICatalog Examples[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#uicatalog-examples)

The UICatalog application demonstrates configuration management:

* **Configuration Editor** - Interactive editor for configuration files
* **Themes** - Theme viewer and selector
* **File System Watcher** - Automatic reload on configuration file changes

### API Reference[](https://gui-cs.github.io/Terminal.Gui/docs/config.html#api-reference)

* [ConfigurationManager](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigurationManager.html)
* [ConfigLocations](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigLocations.html)
* [SettingsScope](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.SettingsScope.html)
* [ThemeScope](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ThemeScope.html)
* [AppSettingsScope](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.AppSettingsScope.html)
* [ThemeManager](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ThemeManager.html)
* [SchemeManager](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.SchemeManager.html)
* [ConfigurationPropertyAttribute](https://gui-cs.github.io/Terminal.Gui/api/Terminal.Gui.Configuration.ConfigurationPropertyAttribute.html)
