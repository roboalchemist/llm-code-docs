# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/integrate-luciq-on-ios/integrate-swiftui-automatic.md

# Integrate SwiftUI (Automatic)

### Overview

The `LuciqSwiftUIIntegrator` is a powerful command-line tool designed to automatically instrument SwiftUI applications for enhanced user experience monitoring and debugging capabilities. This tool modifies your SwiftUI source code during the build process to add instrumentation code that tracks user interactions and screen navigation.

The instrumentor adds additional code to your project's Swift files `(*.swift)` during the build process to observe UI element states and user interactions. After the build process completes, all changes to your source code are automatically reverted, ensuring your original code remains unchanged.

### Requirements

* **iOS 14+**
* **Luciq SDK** **v18.0.0+**
* **Xcode build environment**

### Features

#### Supported SwiftUI Controls

* **Button** - Tracks button taps
* **Toggle** - Monitors toggle state changes
* **Slider** - Captures slider value changes
* **Stepper** - Tracks stepper increment/decrement actions
* **NavigationLink** - Monitors navigation events
* **TabView** - Tracks tab selection changes

#### Supported Modifiers

The tool also instruments the following SwiftUI modifiers:

* **onTapGesture** - Captures tap gestures on views
* **sheet** - Tracks sheet presentation and dismissal
* **popover** - Monitors popover interactions
* **fullScreenCover** - Captures full screen cover presentations
* **navigationDestination** - Tracks navigation destination changes

#### Instrumentation Capabilities

1. **Screen Name Tracking** - Automatically extracts and tracks screen/view names
2. **User Interaction Monitoring** - Captures user interactions with UI elements
3. **Privacy Masking** - Supports masking sensitive UI components
4. **Automatic Reversion** - Reverts all code changes after build completion

#### Screen Transitions Tracking

The tool automatically observes SwiftUI view transitions and navigation events to capture performance metrics and relevant screenshots. This includes transitions triggered by:

* **.sheet**
* **.popover**
* **.fullScreenCover**
* **NavigationLink**
* **navigationDestination**
* **TabView index changes**

### Installation & Setup

#### Prerequisites

Ensure that the Luciq SDK is already integrated into your project before using the SwiftUI instrumentor.

#### Integration Steps

1. **Download LuciqSwiftUIIntegrator**\
   You can download the instrumentor file from [here](https://github.com/luciqai/luciq-ios-sdk/releases/download/19.2.0/LuciqSwiftUIIntegrator.zip).
2. **Add the Instrumentor to Your Build Process**\
   Add the LuciqSwiftUIIntegrator as a pre-build phase in your Xcode project:

```
# Pre-build phase
/path/to/LuciqSwiftUIIntegrator instrument --directory "${SRCROOT}"
```

3. **Configure Build Settings**\
   The tool automatically handles build environment detection and will skip simulator builds by default unless explicitly enabled.

### Command Reference

#### Basic Usage

```
LuciqSwiftUIIntegrator [ACTION] [OPTIONS]
```

#### Available Actions

1. `instrument` **(Default)**\
   Performs complete instrumentation of both screen names and user interactions.CMD

   ```
   LuciqSwiftUIIntegrator instrument --directory /path/to/project
   ```

   **Description**: This is the most comprehensive action that instruments your SwiftUI views to extract both screen names and user interaction events.
2. `screen_names`\
   Instruments the project to extract only screen names.

   ```
   LuciqSwiftUIIntegrator screen_names --directory /path/to/project
   ```

   **Description**: Focuses specifically on tracking navigation and screen identification without instrumenting user interactions.
3. `user_interaction`\
   Instruments the project to extract only user interaction events.

   ```
   LuciqSwiftUIIntegrator user_interaction --directory /path/to/project
   ```
4. `revert`\
   Manually reverts all instrumentation changes.

   ```
   LuciqSwiftUIIntegrator revert --directory /path/to/project
   ```

**Description**: Manually cleans up and reverts all changes made by the instrumentor. Normally, this happens automatically after the build.

#### Command Options

**Directory Path**

```
--directory, -d <path>
```

Specifies the project's base directory path. Defaults to current directory (`.`).

**Example:**

```
LuciqSwiftUIIntegrator instrument --directory /Users/developer/MyApp
```

**Blacklist Files**

```
\--black_list, -bl <comma-separated-filenames>
```

Excludes specific files from instrumentation.

**Example:**

```
LuciqSwiftUIIntegrator instrument --black_list TestView.swift,MockView.swift
```

**Masked Types**

```
\--masked-types <comma-separated-types>
```

Specifies SwiftUI view types to be automatically masked for privacy.

**Example:**

```
LuciqSwiftUIIntegrator instrument --masked-types Text,SecureField,TextField
```

**Enable Simulator**

```
\--enable-simulator
```

Enables instrumentation for simulator builds (disabled by default).

**Example:**

```
LuciqSwiftUIIntegrator instrument --enable-simulator
```

**Disable Diff Tracking**

```
\--no-diff
```

Disables keeping track of changes made to source code.

**Example:**

```
LuciqSwiftUIIntegrator instrument --no-diff
```

**Disable Logging**

```
\--no-log
```

Disables internal debug logs of the tool.

**Example:**

```
LuciqSwiftUIIntegrator instrument --no-log
```

**Version**

```
\--version, -v
```

Prints the version of the tool.

**Example:**

```
LuciqSwiftUIIntegrator --version
```

### Configuration Examples

#### Basic Project Instrumentation

```
# Instrument all SwiftUI views and interactions
LuciqSwiftUIIntegrator instrument --directory "$SRCROOT"
```

### Privacy-Focused Configuration

```
# Instrument with privacy masking for sensitive fields
LuciqSwiftUIIntegrator instrument
  --directory "$SRCROOT"  
  --masked-types SecureField,TextField  
  --black_list LoginView.swift,PaymentView.swift
```

### Screen Tracking Only

```
# Track only screen navigation without user interactions
LuciqSwiftUIIntegrator screen_names --directory "$SRCROOT"
```

### Development Build Configuration

```
# Enable simulator builds with verbose logging
LuciqSwiftUIIntegrator instrument  
  --directory "$SRCROOT"  
  --enable-simulator
```

### Integration with Xcode Build Process

#### Pre-Build Script Phase

Add a new "Run Script" phase in your Xcode target's Build Phases:

```
# Run the instrumentor
/path/to/LuciqSwiftUIIntegrator instrument  
    --directory "$SRCROOT"  
    --masked-types SecureField,TextField  
      --black_list TestFiles.swift
  
echo "SwiftUI instrumentation completed"
```

#### Conditionally Skip Instrumentation

After testing out the script, you can add checks to optimize build time in debug builds. The following snippet skips the instrumentation for debug builds, and you can manually disable instrumentation for CI builds by setting `ENABLE_LUCIQ_SWIFTUI` to `NO`.

```
# !/bin/bash
# Check if running in CI or specific conditions

if [ "$CONFIGURATION" = "Release" ] \|\| [ "$ENABLE_LUCIQ_SWIFTUI" = "YES" ]; then  
echo "Running Luciq SwiftUI Instrumentor..."  

    # Run the instrumentor  
    /path/to/LuciqSwiftUIIntegrator instrument  
        --directory "$SRCROOT"  
        --masked-types SecureField,TextField  
          --black_list TestFiles.swift  

    echo "SwiftUI instrumentation completed"  
else  
    echo "Skipping SwiftUI instrumentation for debug builds"  
fi
```

### How It Works

#### Instrumentation Process

1. **File Discovery:** The tool recursively searches for all .swift files in the specified directory
2. **Syntax Analysis**: Each Swift file is parsed to identify SwiftUI views
3. **Code Rewriting**: Supported SwiftUI elements are wrapped with tracking code
4. **Import Injection**: Adds necessary import statements (import LuciqSDK)
5. **Backup Creation**: Creates backup files (.backup extension) of original source
6. **Automatic Reversion**: Monitors build completion and automatically reverts changes

#### Privacy Masking

When a view type is specified in `--masked-types`, the tool wraps those views with privacy masking:

CMD

```
// Original code  
Text("Sensitive Information")  

// After instrumentation (when Text is masked)  
LuciqPrivateView {  
    Text("Sensitive Information")  
}
```

#### User Interaction Tracking

The tool enhances user interaction callbacks with tracking code:

```
// Original code  
Button("Submit") {  
    submitForm()  
}  

// After instrumentation  
Button("Submit") {  
    UserStep(event: .tap, automatic: true)?  
        .setViewTypeName("Button")  
        .setMessage("Tap on Button Submit")  
        .logUserStep()  
    submitForm()  
}
```

### Known Limitations

#### SwiftUI Version Support

* **SwiftUI 2.0+ only:** The instrumentor requires iOS 14+ deployment target
* **Custom SwiftUI controls:** Currently doesn't support instrumentation of custom SwiftUI components

#### Build Performance Impact

* **Increased build time:** The instrumentation process adds overhead to build time
* **File processing:** Each Swift file must be parsed and potentially rewritten

#### Reversion

* **Reversion process is not executed:** This happens if the build process is terminated from Xcode before the build finishes.

#### Simulator Builds

* **Disabled by default:** Simulator instrumentation is disabled by default to optimize development builds
* **Manual enabling:** Use `--enable-simulator` flag to enable for simulator builds

### Troubleshooting

#### Common Issues

**Build Failures**

If the instrumentor causes build failures:

1. Check that all blacklisted files are correctly specified
2. Ensure the Luciq SDK is properly integrated
3. Verify iOS deployment target is 14.0 or higher
4. Please reach out to our support team with the tool’s debug logs file. The file is located at `{PROJECT_DIR}/LuciqInstrumentation/changeLogsFile.log`

**Performance Issues**

If builds are too slow:

1. Use selective actions (`screen_names` or `user_interaction` instead of `instrument`)
2. Disable simulator instrumentation
3. Add frequently changing files to the blacklist

**Privacy Concerns**

For sensitive applications:

1. Use `--masked-types` to automatically mask sensitive view types
2. Blacklist files containing sensitive information
3. Review instrumented code in development builds before release

#### Debug Information

The tool provides comprehensive logging.

* Views being instrumented
* Errors and warnings
* Reversion process

#### Getting Help

```
# Display help information
LuciqSwiftUIIntegrator --help

# Display version information
LuciqSwiftUIIntegrator --version
```

### Best Practices

#### Development Workflow

1. **Test incrementally:** Start with `screen_names` or `user_interaction` before using full `instrument`
2. **Use blacklists:** Exclude test files, mock files, and frequently changing development files
3. **Monitor build times:** Track build performance impact and adjust configuration as needed

#### Production Builds

1. **Release configuration:** Only enable instrumentation for release builds or specific configurations
2. **Privacy masking:** Always configure appropriate masking for sensitive data
3. **Validation:** Test instrumented builds thoroughly before release

#### CI/CD Integration

1. **Conditional execution:** Use environment variables to control when instrumentation runs
2. **Caching:** Consider caching strategies for the instrumentor binary and dependencies
3. **Build logs:** Capture and analyze instrumentation logs for debugging

The LuciqSwiftUIIntegrator provides a powerful way to enhance your SwiftUI applications with comprehensive user experience monitoring while maintaining the flexibility to customize the instrumentation process to your specific needs.
