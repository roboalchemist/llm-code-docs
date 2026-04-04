# Source: https://microsoft.github.io/react-native-windows/docs/autolink-windows-cli

Title: react-native autolink-windows · React Native for Windows

URL Source: https://microsoft.github.io/react-native-windows/docs/autolink-windows-cli

Markdown Content:
react-native autolink-windows · React Native for Windows
===============

[![Image 2: React Native for Windows](https://microsoft.github.io/react-native-windows/img/header_logo.svg) React Native for Windows ------------------------](https://microsoft.github.io/react-native-windows/)[### 0.81](https://microsoft.github.io/react-native-windows/versions)

*   [Docs](https://microsoft.github.io/react-native-windows/docs/getting-started)
*   [APIs](https://microsoft.github.io/react-native-windows/docs/flyout-component)
*   [Blog](https://devblogs.microsoft.com/react-native/)
*   [Resources](https://microsoft.github.io/react-native-windows/resources)
*   [Samples](https://github.com/microsoft/react-native-windows-samples/tree/main/samples)
*   [Support](https://microsoft.github.io/react-native-windows/support)

_›_ CLI Commands
----------------

### The Basics

*   [Get Started with Windows](https://microsoft.github.io/react-native-windows/docs/getting-started)
*   [System Requirements](https://microsoft.github.io/react-native-windows/docs/rnw-dependencies)
*   [React Native Windows CLI](https://microsoft.github.io/react-native-windows/docs/react-native-windows-cli)
*   [React Native Windows Components and APIs](https://microsoft.github.io/react-native-windows/docs/parity-status)
*   [React Native Config Schema](https://microsoft.github.io/react-native-windows/docs/config)
*   [Using PlatformColor and Responding to Themes](https://microsoft.github.io/react-native-windows/docs/windowsbrush-and-theme)
*   [Release Strategy](https://microsoft.github.io/react-native-windows/docs/releases)
*   [Platform Detection](https://microsoft.github.io/react-native-windows/docs/platform)
*   [Upgrading App to Latest Version of React Native Windows](https://microsoft.github.io/react-native-windows/docs/upgrade-app)
*   [Migration Guide](https://microsoft.github.io/react-native-windows/docs/migration-guide)
*   [Setup Continuous Integration Pipeline for an RNW App](https://microsoft.github.io/react-native-windows/docs/setup-ci)
*   [Publishing a React Native Windows App to the Microsoft Store](https://microsoft.github.io/react-native-windows/docs/app-publishing)
*   [Supported Community Modules](https://microsoft.github.io/react-native-windows/docs/supported-community-modules)

### CLI Commands

*   [react-native autolink-windows](https://microsoft.github.io/react-native-windows/docs/autolink-windows-cli)
*   [react-native codegen-windows](https://microsoft.github.io/react-native-windows/docs/codegen-windows-cli)
*   [react-native init-windows](https://microsoft.github.io/react-native-windows/docs/init-windows-cli)
*   [react-native run-windows](https://microsoft.github.io/react-native-windows/docs/run-windows-cli)

### Native Development

*   [Overview](https://microsoft.github.io/react-native-windows/docs/native-platform)
*   [Getting Started](https://microsoft.github.io/react-native-windows/docs/native-platform-getting-started)
*   [Native Modules](https://microsoft.github.io/react-native-windows/docs/native-platform-modules)
*   [Native Components (Fabric)](https://microsoft.github.io/react-native-windows/docs/native-platform-components)
*   [Native Components (Paper)](https://microsoft.github.io/react-native-windows/docs/native-platform-components-paper)
*   [Using Native Libraries](https://microsoft.github.io/react-native-windows/docs/native-platform-using)

### Advanced Topics

*   [Developing Windows apps on a non-Windows PC](https://microsoft.github.io/react-native-windows/docs/win10-vm)
*   [Hermes on Windows](https://microsoft.github.io/react-native-windows/docs/hermes)
*   [Using Microsoft.ReactNative NuGet packages](https://microsoft.github.io/react-native-windows/docs/NuGet)

### Troubleshooting

*   [JavaScript Debugging](https://microsoft.github.io/react-native-windows/docs/debugging-javascript)
*   [Metro config for out of tree platforms](https://microsoft.github.io/react-native-windows/docs/metro-config-out-tree-platforms)

### Legacy Docs

#### Native Modules

    *   [Native Modules](https://microsoft.github.io/react-native-windows/docs/native-modules)
    *   [Native UI Components](https://microsoft.github.io/react-native-windows/docs/view-managers)
    *   [Native Module Setup](https://microsoft.github.io/react-native-windows/docs/native-modules-setup)
    *   [Native Modules vs Turbo Modules](https://microsoft.github.io/react-native-windows/docs/native-modules-vs-turbo-modules)
    *   [Using Community Native Modules](https://microsoft.github.io/react-native-windows/docs/native-modules-using)
    *   [Autolinking Native Modules](https://microsoft.github.io/react-native-windows/docs/native-modules-autolinking)
    *   [Native Modules (Advanced)](https://microsoft.github.io/react-native-windows/docs/native-modules-advanced)
    *   [Troubleshooting Native Modules](https://microsoft.github.io/react-native-windows/docs/native-modules-troubleshooting)

#### Native Development

    *   [Working with native code on Windows](https://microsoft.github.io/react-native-windows/docs/native-code)
    *   [Choosing C++ or C# for native code](https://microsoft.github.io/react-native-windows/docs/native-code-language-choice)
    *   [Marshaling Data](https://microsoft.github.io/react-native-windows/docs/native-modules-marshalling-data)
    *   [Using Asynchronous Windows APIs](https://microsoft.github.io/react-native-windows/docs/native-modules-async)
    *   [Using JSValue](https://microsoft.github.io/react-native-windows/docs/native-modules-jsvalue)
    *   [Compile time code generation for C#](https://microsoft.github.io/react-native-windows/docs/native-modules-csharp-codegen)
    *   [Customizing SDK versions](https://microsoft.github.io/react-native-windows/docs/customizing-SDK-versions)
    *   [Managing C++ dependencies](https://microsoft.github.io/react-native-windows/docs/managing-cpp-deps)

[Edit](https://github.com/microsoft/react-native-windows-samples/blob/main/docs/autolink-windows-cli.md)
react-native autolink-windows
=============================

![Image 3: Architecture](https://img.shields.io/badge/architecture-new_&_old-green)

This guide will give you more information on the `autolink-windows` command of the React Native Windows CLI.

[](https://microsoft.github.io/react-native-windows/docs/autolink-windows-cli)[](https://microsoft.github.io/react-native-windows/docs/autolink-windows-cli#autolink-windows)`autolink-windows`
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `autolink-windows` CLI command is used to link the native code and build systems for a React Native for Windows app with any native community modules it uses.

**Note:** Autolinking runs automatically as part of running the [run-windows command](https://microsoft.github.io/react-native-windows/docs/run-windows-cli), unless the `--no-autolink` argument is used.

### [](https://microsoft.github.io/react-native-windows/docs/autolink-windows-cli)[](https://microsoft.github.io/react-native-windows/docs/autolink-windows-cli#usage)Usage

Runs Windows-specific autolinking for your RNW project.

```bat
npx react-native autolink-windows
```

### [](https://microsoft.github.io/react-native-windows/docs/autolink-windows-cli)[](https://microsoft.github.io/react-native-windows/docs/autolink-windows-cli#options)Options

Here are the options that `react-native autolink-windows` takes:

| Option | Input Type | Description |
| --- | --- | --- |
| `--logging` | boolean | Verbose output logging |
| `--check` | boolean | Only check whether any autolinked files need to change |
| `--sln` | string | Override the app solution file determined by 'react-native config', i.e. `windows\myApp.sln` |
| `--proj` | string | Override the app project file determined by 'react-native config', i.e. `windows\myApp\myApp.vcxproj` |
| `--no-telemetry` | boolean | Disables sending telemetry that allows analysis of usage and failures of the react-native-windows CLI |
| `-h`, `--help` | boolean | Display help for command |

[](https://microsoft.github.io/react-native-windows/docs/autolink-windows-cli)[](https://microsoft.github.io/react-native-windows/docs/autolink-windows-cli#telemetry-notice)Telemetry Notice
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This command sends telemetry to Microsoft by default. You can prevent the telemetry from being sent by using the `--no-telemetry` command line option. See below for more details.

The software may collect information about you and your use of the software and send it to Microsoft. Microsoft may use this information to provide services and improve our products and services. You may turn off the telemetry as described in the repository. There are also some features in the software that may enable you and Microsoft to collect data from users of your applications. If you use these features, you must comply with applicable law, including providing appropriate notices to users of your applications together with a copy of Microsoft's privacy statement. Our privacy statement is located at [https://go.microsoft.com/fwlink/?LinkID=824704](https://go.microsoft.com/fwlink/?LinkID=824704). You can learn more about data collection and use in the help documentation and our privacy statement. Your use of the software operates as your consent to these practices.

This data collection notice only applies to the process of running the react-native-windows CLI commands.

_Last updated on 3/3/2026_

[← Supported Community Modules](https://microsoft.github.io/react-native-windows/docs/supported-community-modules)[react-native codegen-windows →](https://microsoft.github.io/react-native-windows/docs/codegen-windows-cli)

*   [`autolink-windows`](https://microsoft.github.io/react-native-windows/docs/autolink-windows-cli#autolink-windows)
    *   [Usage](https://microsoft.github.io/react-native-windows/docs/autolink-windows-cli#usage)
    *   [Options](https://microsoft.github.io/react-native-windows/docs/autolink-windows-cli#options)

*   [Telemetry Notice](https://microsoft.github.io/react-native-windows/docs/autolink-windows-cli#telemetry-notice)

##### React Native Docs

[Getting Started](https://reactnative.dev/docs/getting-started)[Tutorial](https://reactnative.dev/docs/tutorial)[Components and APIs](https://reactnative.dev/docs/components-and-apis)[More Resources](https://reactnative.dev/docs/more-resources)

##### React Native for Windows Docs

[Get Started with Windows](https://microsoft.github.io/react-native-windows/docs/getting-started)

[React Native Windows Components and APIs](https://microsoft.github.io/react-native-windows/docs/parity-status)[Native Modules](https://microsoft.github.io/react-native-windows/docs/native-modules)[Native UI Components](https://microsoft.github.io/react-native-windows/docs/view-managers)

##### Connect With Us On

[Blog](https://devblogs.microsoft.com/react-native/)[Twitter](https://twitter.com/ReactNativeMSFT)[GitHub](https://github.com/microsoft/react-native-windows)[Samples](https://github.com/microsoft/react-native-windows-samples/tree/main/samples)
