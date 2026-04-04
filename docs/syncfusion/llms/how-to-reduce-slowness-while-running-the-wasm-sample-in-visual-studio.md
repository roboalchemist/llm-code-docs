# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/blazor/faqs/how-to-reduce-slowness-while-running-the-wasm-sample-in-visual-studio.md

# Reduce slowness when running Blazor WebAssembly in Visual Studio

Performance issues may occur when running or debugging Blazor WebAssembly in Visual Studio. To improve execution speed, disable the .NET 9+ Mono WASM debugger, which can introduce overhead during debugging sessions.

![Visual Studio setting for the Mono WASM debugger](../images/mono_debugger.png)

Disabling the Mono WASM debugger can provide a smoother experience while running or debugging WebAssembly projects. This change affects debugging behavior; re-enable it when full debugging features are required.

For background details and guidance, see the following resources:
  * [Performance Regression debugging Blazor WebAssembly with .NET 9](https://developercommunity.visualstudio.com/t/Performance-Regression-debugging-Blazor/10773897)
  * [Performance Regression in Blazor WebAssembly with .NET 9](https://github.com/dotnet/aspnetcore/issues/58507)
