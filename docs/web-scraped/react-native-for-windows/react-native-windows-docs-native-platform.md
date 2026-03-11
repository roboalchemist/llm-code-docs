# Source: https://microsoft.github.io/react-native-windows/docs/native-platform

Title: Native Platform: Overview · React Native for Windows

URL Source: https://microsoft.github.io/react-native-windows/docs/native-platform

Markdown Content:
Native Platform: Overview · React Native for Windows
===============

[![Image 2: React Native for Windows](https://microsoft.github.io/react-native-windows/img/header_logo.svg) React Native for Windows ------------------------](https://microsoft.github.io/react-native-windows/)[### 0.81](https://microsoft.github.io/react-native-windows/versions)

*   [Docs](https://microsoft.github.io/react-native-windows/docs/getting-started)
*   [APIs](https://microsoft.github.io/react-native-windows/docs/flyout-component)
*   [Blog](https://devblogs.microsoft.com/react-native/)
*   [Resources](https://microsoft.github.io/react-native-windows/resources)
*   [Samples](https://github.com/microsoft/react-native-windows-samples/tree/main/samples)
*   [Support](https://microsoft.github.io/react-native-windows/support)

_›_ Native Development
----------------------

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

[Edit](https://github.com/microsoft/react-native-windows-samples/blob/main/docs/native-platform.md)
Native Platform: Overview
=========================

![Image 3: Architecture](https://img.shields.io/badge/architecture-new_&_old-green)

Sometimes a React Native app needs to access native functionality that isn't already exposed via `react-native` or an existing community library. Whether it's to access a platform API or some other custom native code, React Native was designed to be extensible, making it possible for anyone to write native code and expose that functionality to their app's JavaScript.

The [reactnative.dev Native Platform guide](https://reactnative.dev/docs/native-platform) defines _Native Modules_ as native libraries for accessing non-UI native code, and _Native Components_ for accessing native platform views. That guide includes steps for implementing new Native Modules (and/or Components) for both the Android and iOS platforms. This guide will cover how to implement new Native Modules (and/or Components) for the Windows platform.

> **Architecture Note:** The React Native guide recommends creating _Turbo Native Modules_ and/or _Fabric Native Components_ to support React Native's New Architecture, rather than using the legacy APIs made for the Old Architecture. This guide will detail how to create a single library which supports both architectures on Windows. For more information on React Native architectures in React Native for Windows, see [New vs. Old Architecture](https://microsoft.github.io/react-native-windows/docs/new-architecture).

[](https://microsoft.github.io/react-native-windows/docs/native-platform)[](https://microsoft.github.io/react-native-windows/docs/native-platform#getting-started)Getting Started
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Your first step to implement a new Native Module (and/or Component) is to create a new base native library and initialize React Native for Windows support. See [Native Platform: Getting Started](https://microsoft.github.io/react-native-windows/docs/native-platform-getting-started).

[](https://microsoft.github.io/react-native-windows/docs/native-platform)[](https://microsoft.github.io/react-native-windows/docs/native-platform#implementing-windows-support)Implementing Windows Support
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

After you've initialized a new project to support Windows, your next step is to implement that Windows support in native code.

If you're implementing a Native Module (i.e. exposing non-UI native code), continue with [Native Platform: Native Modules](https://microsoft.github.io/react-native-windows/docs/native-platform-modules).

If you're implementing a Native Component (i.e. exposing native Windows UI), continue with [Native Platform: Native Components](https://microsoft.github.io/react-native-windows/docs/native-platform-components).

[](https://microsoft.github.io/react-native-windows/docs/native-platform)[](https://microsoft.github.io/react-native-windows/docs/native-platform#using-native-libraries-on-windows)Using Native Libraries on Windows
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

After you've implemented your native library, the final step is to consume it in your React Native for Windows app. Continue with [Native Platform: Using Native Libraries](https://microsoft.github.io/react-native-windows/docs/native-platform-using).

[](https://microsoft.github.io/react-native-windows/docs/native-platform)[](https://microsoft.github.io/react-native-windows/docs/native-platform#native-module-sample)Native Module Sample
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [Native Module Sample](https://github.com/microsoft/react-native-windows-samples/tree/main/samples/NativeModuleSample/cpp-lib) project is a complete React Native for Windows library that contains:

*   Several Native Modules examples
*   A Native Component example with implementations for both Paper and Fabric
*   Both New and Old Architecture example apps

_Last updated on 3/3/2026_

[← react-native run-windows](https://microsoft.github.io/react-native-windows/docs/run-windows-cli)[Getting Started →](https://microsoft.github.io/react-native-windows/docs/native-platform-getting-started)

*   [Getting Started](https://microsoft.github.io/react-native-windows/docs/native-platform#getting-started)
*   [Implementing Windows Support](https://microsoft.github.io/react-native-windows/docs/native-platform#implementing-windows-support)
*   [Using Native Libraries on Windows](https://microsoft.github.io/react-native-windows/docs/native-platform#using-native-libraries-on-windows)
*   [Native Module Sample](https://microsoft.github.io/react-native-windows/docs/native-platform#native-module-sample)

##### React Native Docs

[Getting Started](https://reactnative.dev/docs/getting-started)[Tutorial](https://reactnative.dev/docs/tutorial)[Components and APIs](https://reactnative.dev/docs/components-and-apis)[More Resources](https://reactnative.dev/docs/more-resources)

##### React Native for Windows Docs

[Get Started with Windows](https://microsoft.github.io/react-native-windows/docs/getting-started)

[React Native Windows Components and APIs](https://microsoft.github.io/react-native-windows/docs/parity-status)[Native Modules](https://microsoft.github.io/react-native-windows/docs/native-modules)[Native UI Components](https://microsoft.github.io/react-native-windows/docs/view-managers)

##### Connect With Us On

[Blog](https://devblogs.microsoft.com/react-native/)[Twitter](https://twitter.com/ReactNativeMSFT)[GitHub](https://github.com/microsoft/react-native-windows)[Samples](https://github.com/microsoft/react-native-windows-samples/tree/main/samples)
