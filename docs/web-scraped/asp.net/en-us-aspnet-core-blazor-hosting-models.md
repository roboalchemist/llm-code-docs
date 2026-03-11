# Source: https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0

Title: ASP.NET Core Blazor hosting models

URL Source: https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0

Markdown Content:
This article explains Blazor hosting models, primarily focused on Blazor Server and Blazor WebAssembly apps in versions of .NET earlier than .NET 8. The guidance in this article is relevant under all .NET releases for Blazor Hybrid apps that run on native mobile and desktop platforms. Blazor Web Apps in .NET 8 or later are better conceptualized by how Razor components are rendered, which is described as their _render mode_. Render modes are briefly touched on in the _Fundamentals_ overview article and covered in detail in [ASP.NET Core Blazor render modes](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/render-modes?view=aspnetcore-10.0) of the _Components_ node.

This article explains Blazor hosting models and how to choose which one to use.

Blazor is a web framework for building web UI components ([Razor components](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/?view=aspnetcore-10.0)) that can be hosted in different ways. Razor components can run server-side in ASP.NET Core (_Blazor Server_) versus client-side in the browser on a [WebAssembly](https://webassembly.org/)-based .NET runtime (_Blazor WebAssembly_, _Blazor Wasm_). You can also host Razor components in native mobile and desktop apps that render to an embedded Web View control (_Blazor Hybrid_). Regardless of the hosting model, the way you build Razor components _is the same_. The same Razor components can be used with any of the hosting models unchanged.

Blazor is a web framework for building web UI components ([Razor components](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/?view=aspnetcore-10.0)) that can be hosted in different ways. Razor components can run server-side in ASP.NET Core (_Blazor Server_) versus client-side in the browser on a [WebAssembly](https://webassembly.org/)-based .NET runtime (_Blazor WebAssembly_, _Blazor Wasm_). Regardless of the hosting model, the way you build Razor components _is the same_. The same Razor components can be used with any of the hosting models unchanged.

With the Blazor Server hosting model, components are executed on the server from within an ASP.NET Core app. UI updates, event handling, and JavaScript calls are handled over a [SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/introduction?view=aspnetcore-10.0) connection using the [WebSockets protocol](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/websockets?view=aspnetcore-10.0). The state on the server associated with each connected client is called a _circuit_. Circuits aren't tied to a specific network connection and can tolerate temporary network interruptions and attempts by the client to reconnect to the server when the connection is lost.

In a traditional server-rendered app, opening the same app in multiple browser screens (tabs or `iframes`) typically doesn't translate into additional resource demands on the server. For the Blazor Server hosting model, each browser screen requires a separate circuit and separate instances of server-managed component state. Blazor considers closing a browser tab or navigating to an external URL a _graceful_ termination. In the event of a graceful termination, the circuit and associated resources are immediately released. A client may also disconnect non-gracefully, for instance due to a network interruption. Blazor Server stores disconnected circuits for a configurable interval to allow the client to reconnect.

![Image 1: The browser interacts with Blazor (hosted inside of an ASP.NET Core app) on the server over a SignalR connection.](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models/_static/blazor-server.png?view=aspnetcore-10.0)

On the client, the Blazor script establishes the SignalR connection with the server. The script is served as a static web asset with automatic compression and [fingerprinting](https://developer.mozilla.org/docs/Glossary/Fingerprinting).

On the client, the Blazor script establishes the SignalR connection with the server. The script is served from an embedded resource in the ASP.NET Core shared framework.

The Blazor Server hosting model offers several benefits:

*   Download size is significantly smaller than when the Blazor WebAssembly hosting model is used, and the app loads much faster.
*   The app takes full advantage of server capabilities, including the use of .NET APIs.
*   .NET on the server is used to run the app, so existing .NET tooling, such as debugging, works as expected.
*   Thin clients are supported. For example, Blazor Server works with browsers that don't support WebAssembly and on resource-constrained devices.
*   The app's .NET/C# code base, including the app's component code, isn't served to clients.

The Blazor Server hosting model has the following limitations:

*   Higher latency usually exists. Every user interaction involves a network hop.
*   There's no offline support. If the client connection fails, interactivity fails.
*   Scaling apps with many users requires server resources to handle multiple client connections and client state.
*   An ASP.NET Core server is required to serve the app. Serverless deployment scenarios aren't possible, such as serving the app from a Content Delivery Network (CDN).

We recommend using the [Azure SignalR Service](https://learn.microsoft.com/en-us/azure/azure-signalr) for apps that adopt the Blazor Server hosting model. The service allows for scaling up a Blazor Server app to a large number of concurrent SignalR connections.

The Blazor WebAssembly hosting model runs components client-side in the browser on a WebAssembly-based .NET runtime. Razor components, their dependencies, and the .NET runtime are downloaded to the browser. Components are executed directly on the browser UI thread. UI updates and event handling occur within the same process. Assets are deployed as static files to a web server or service capable of serving static content to clients.

![Image 2: Blazor WebAssembly: Blazor runs on a UI thread inside the browser.](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models/_static/blazor-webassembly.png?view=aspnetcore-10.0)

Blazor Web Apps can use the Blazor WebAssembly hosting model to enable client-side interactivity. When an app is created that exclusively runs on the Blazor WebAssembly hosting model without server-side rendering and interactivity, the app is called a _standalone_ Blazor WebAssembly app.

When the Blazor WebAssembly app is created for deployment without a backend ASP.NET Core app to serve its files, the app is called a _standalone_ Blazor WebAssembly app.

When a standalone Blazor WebAssembly app uses a backend ASP.NET Core app to serve its files, the app is called a _hosted_ Blazor WebAssembly app. Using hosted Blazor WebAssembly, you get a full-stack web development experience with .NET, including the ability to share code between the client and server apps, support for prerendering, and integration with MVC and Razor Pages. A hosted client app can interact with its backend server app over the network using a variety of messaging frameworks and protocols, such as [web API](https://learn.microsoft.com/en-us/aspnet/core/web-api/?view=aspnetcore-10.0), [gRPC-web](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0), and [SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/introduction?view=aspnetcore-10.0) ([Use ASP.NET Core SignalR with Blazor](https://learn.microsoft.com/en-us/aspnet/core/blazor/tutorials/signalr-blazor?view=aspnetcore-10.0)).

A Blazor WebAssembly app built as a [Progressive Web App (PWA)](https://learn.microsoft.com/en-us/aspnet/core/blazor/progressive-web-app/?view=aspnetcore-10.0) uses modern browser APIs to enable many of the capabilities of a native client app, such as working offline, running in its own app window, launching from the host's operating system, receiving push notifications, and automatically updating in the background.

The Blazor script handles:

*   Downloading the .NET runtime, Razor components, and dependencies.
*   Runtime initialization.

The size of the published app, its _payload size_, is a critical performance factor for an app's usability. A large app takes a relatively long time to download to a browser, which diminishes the user experience. Blazor WebAssembly optimizes payload size to reduce download times:

*   Unused code is stripped out of the app when it's published by the [Intermediate Language (IL) Trimmer](https://learn.microsoft.com/en-us/aspnet/core/blazor/host-and-deploy/configure-trimmer?view=aspnetcore-10.0).
*   HTTP responses are compressed.
*   The .NET runtime and assemblies are cached in the browser.

The Blazor WebAssembly hosting model offers several benefits:

*   For standalone Blazor WebAssembly apps, there's no .NET server-side dependency after the app is downloaded from the server, so the app remains functional if the server goes offline.
*   Client resources and capabilities are fully leveraged.
*   Work is offloaded from the server to the client.
*   For standalone Blazor WebAssembly apps, an ASP.NET Core web server isn't required to host the app. Serverless deployment scenarios are possible, such as serving the app from a Content Delivery Network (CDN).

The Blazor WebAssembly hosting model has the following limitations:

*   Razor components are restricted to the capabilities of the browser.
*   Capable client hardware and software (for example, WebAssembly support) is required.
*   Download size is larger, and components take longer to load.
*   Code sent to the client can't be protected from inspection and tampering by users.

The .NET [Intermediate Language (IL)](https://learn.microsoft.com/en-us/dotnet/standard/glossary#il) interpreter includes partial [just-in-time (JIT)](https://learn.microsoft.com/en-us/dotnet/standard/glossary#jit) runtime support to achieve improved runtime performance. The JIT interpreter optimizes execution of interpreter bytecodes by replacing them with tiny blobs of WebAssembly code. The JIT interpreter is automatically enabled for Blazor WebAssembly apps except when debugging.

Blazor can also be used to build native client apps using a hybrid approach. Hybrid apps are native apps that leverage web technologies for their functionality. In a Blazor Hybrid app, Razor components run directly in the native app (not on WebAssembly) along with any other .NET code and render web UI based on HTML and CSS to an embedded Web View control through a local interop channel.

![Image 3: Hybrid apps with .NET and Blazor render UI in a Web View control, where the HTML DOM interacts with Blazor and .NET of the native desktop or mobile app.](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models/_static/hybrid-apps-1.png?view=aspnetcore-10.0)

Blazor Hybrid apps can be built using different .NET native app frameworks, including .NET MAUI, WPF, and Windows Forms. Blazor provides `BlazorWebView` controls for adding Razor components to apps built with these frameworks. Using Blazor with .NET MAUI offers a convenient way to build cross-platform Blazor Hybrid apps for mobile and desktop, while Blazor integration with WPF and Windows Forms can be a great way to modernize existing apps.

Because Blazor Hybrid apps are native apps, they can support functionality that isn't available with only the web platform. Blazor Hybrid apps have full access to native platform capabilities through normal .NET APIs. Blazor Hybrid apps can also share and reuse components with existing Blazor Server or Blazor WebAssembly apps. Blazor Hybrid apps combine the benefits of the web, native apps, and the .NET platform.

The Blazor Hybrid hosting model offers several benefits:

*   Reuse existing components that can be shared across mobile, desktop, and web.
*   Leverage web development skills, experience, and resources.
*   Apps have full access to the native capabilities of the device.

The Blazor Hybrid hosting model has the following limitations:

*   Separate native client apps must be built, deployed, and maintained for each target platform.
*   Native client apps usually take longer to find, download, and install over accessing a web app in a browser.

For more information, see [ASP.NET Core Blazor Hybrid](https://learn.microsoft.com/en-us/aspnet/core/blazor/hybrid/?view=aspnetcore-10.0).

For more information on Microsoft native client frameworks, see the following resources:

*   [.NET Multi-platform App UI (.NET MAUI)](https://learn.microsoft.com/en-us/dotnet/maui/what-is-maui)
*   [Windows Presentation Foundation (WPF)](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/overview/)
*   [Windows Forms](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/overview/)

A component's hosting model is set by its _render mode_, either at compile time or runtime, which is described with examples in [ASP.NET Core Blazor render modes](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/render-modes?view=aspnetcore-10.0). The following table shows the primary considerations for setting the render mode to determine a component's hosting model. For standalone Blazor WebAssembly apps, all of the app's components are rendered on the client with the Blazor WebAssembly hosting model.

Select the Blazor hosting model based on the app's feature requirements. The following table shows the primary considerations for selecting the hosting model.

Blazor Hybrid apps include .NET MAUI, WPF, and Windows Forms framework apps.

| Feature | Blazor Server | Blazor WebAssembly (Wasm) | Blazor Hybrid |
| --- | --- | --- | --- |
| [Complete .NET API compatibility](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#complete-net-api-compatibility) | Supported | Not supported | Supported |
| [Direct access to server and network resources](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#direct-access-to-server-and-network-resources) | Supported | Not supported† | Not supported† |
| [Small payload size with fast initial load time](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#small-payload-size-with-fast-initial-load-time) | Supported | Not supported | Not supported |
| [Near native execution speed](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#near-native-execution-speed) | Supported | Supported‡ | Supported |
| [App code secure and private on the server](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#app-code-secure-and-private-on-the-server) | Supported | Not supported† | Not supported† |
| [Run apps offline once downloaded](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#run-apps-offline-once-downloaded) | Not supported | Supported | Supported |
| [Static site hosting](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#static-site-hosting) | Not supported | Supported | Not supported |
| [Offloads processing to clients](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#offloads-processing-to-clients) | Not supported | Supported | Supported |
| [Full access to native client capabilities](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#full-access-to-native-client-capabilities) | Not supported | Not supported | Supported |
| [Web-based deployment](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#web-based-deployment) | Supported | Supported | Not supported |

†Blazor WebAssembly and Blazor Hybrid apps can use server-based APIs to access server/network resources and access private and secure app code.

 ‡Blazor WebAssembly only reaches near-native performance with [ahead-of-time (AOT) compilation](https://learn.microsoft.com/en-us/aspnet/core/blazor/webassembly-build-tools-and-aot?view=aspnetcore-10.0#ahead-of-time-aot-compilation).

| Feature | Blazor Server | Blazor WebAssembly (Wasm) |
| --- | --- | --- |
| [Complete .NET API compatibility](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#complete-net-api-compatibility) | Supported | Not supported |
| [Direct access to server and network resources](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#direct-access-to-server-and-network-resources) | Supported | Not supported† |
| [Small payload size with fast initial load time](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#small-payload-size-with-fast-initial-load-time) | Supported | Not supported |
| [App code secure and private on the server](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#app-code-secure-and-private-on-the-server) | Supported | Not supported† |
| [Run apps offline once downloaded](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#run-apps-offline-once-downloaded) | Not supported | Supported |
| [Static site hosting](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#static-site-hosting) | Not supported | Supported |
| [Offloads processing to clients](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#offloads-processing-to-clients) | Not supported | Supported |

†Blazor WebAssembly apps can use server-based APIs to access server/network resources and access private and secure app code.

After you choose the app's hosting model, you can generate a Blazor Server or Blazor WebAssembly app from a Blazor project template. For more information, see [Tooling for ASP.NET Core Blazor](https://learn.microsoft.com/en-us/aspnet/core/blazor/tooling?view=aspnetcore-10.0#blazor-template-options).

Components rendered for the Blazor Server hosting model and Blazor Hybrid apps have complete .NET API compatibility, while components rendered for Blazor WebAssembly are limited to a [subset of .NET APIs](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/?view=aspnetcore-10.0#subset-of-net-apis-for-blazor-webassembly-apps). When an app's specification requires one or more .NET APIs that are unavailable to WebAssembly-rendered components, then choose to render components for Blazor Server or use Blazor Hybrid.

Blazor Server and Blazor Hybrid apps have complete .NET API compatibility, while Blazor WebAssembly apps are limited to a subset of .NET APIs. When an app's specification requires one or more .NET APIs that are unavailable to Blazor WebAssembly apps, then choose Blazor Server or Blazor Hybrid.

Blazor Server apps have complete .NET API compatibility, while Blazor WebAssembly apps are limited to a subset of .NET APIs. When an app's specification requires one or more .NET APIs that are unavailable to Blazor WebAssembly apps, then choose Blazor Server.

Components rendered for the Blazor Server hosting model have direct access to server and network resources where the app is executing. Because components hosted using Blazor WebAssembly or Blazor Hybrid execute on a client, they don't have direct access to server and network resources. Components can access server and network resources _indirectly_ via protected server-based APIs. Server-based APIs might be available via third-party libraries, packages, and services. Take into account the following considerations:

*   Third-party libraries, packages, and services might be costly to implement and maintain, weakly supported, or introduce security risks.
*   If one or more server-based APIs are developed internally by your organization, additional resources are required to build and maintain them.

Use the Blazor Server hosting model to avoid the need to expose APIs from the server environment.

Blazor Server apps have direct access to server and network resources where the app is executing. Because Blazor WebAssembly and Blazor Hybrid apps execute on a client, they don't have direct access to server and network resources. Blazor WebAssembly and Blazor Hybrid apps can access server and network resources _indirectly_ via protected server-based APIs. Server-based APIs might be available via third-party libraries, packages, and services. Take into account the following considerations:

*   Third-party libraries, packages, and services might be costly to implement and maintain, weakly supported, or introduce security risks.
*   If one or more server-based APIs are developed internally by your organization, additional resources are required to build and maintain them.

To avoid server-based APIs for Blazor WebAssembly or Blazor Hybrid apps, adopt Blazor Server, which can access server and network resources directly.

Blazor Server apps have direct access to server and network resources where the app is executing. Because Blazor WebAssembly apps execute on a client, they don't have direct access to server and network resources. Blazor WebAssembly apps can access server and network resources _indirectly_ via protected server-based APIs. Server-based APIs might be available via third-party libraries, packages, and services. Take into account the following considerations:

*   Third-party libraries, packages, and services might be costly to implement and maintain, weakly supported, or introduce security risks.
*   If one or more server-based APIs are developed internally by your organization, additional resources are required to build and maintain them.

To avoid server-based APIs for Blazor WebAssembly apps, adopt Blazor Server, which can access server and network resources directly.

Rendering components from the server reduces the app payload size and improves initial load times. When a fast initial load time is desired, use the Blazor Server hosting model or consider static server-side rendering.

Blazor Server apps have relatively small payload sizes with faster initial load times. When a fast initial load time is desired, adopt Blazor Server.

Blazor Hybrid apps run using the .NET runtime natively on the target platform, which offers the best possible speed.

Components rendered for the Blazor WebAssembly hosting model, including Progressive Web Apps (PWAs), and standalone Blazor WebAssembly apps run using the .NET runtime for WebAssembly, which is slower than running directly on the platform. Consider using [ahead-of-time (AOT) compiled](https://learn.microsoft.com/en-us/aspnet/core/blazor/webassembly-build-tools-and-aot?view=aspnetcore-10.0#ahead-of-time-aot-compilation) to improve runtime performance when using Blazor WebAssembly.

Blazor Hybrid apps run using the .NET runtime natively on the target platform, which offers the best possible speed.

Blazor WebAssembly, including Progressive Web Apps (PWAs), apps run using the .NET runtime for WebAssembly, which is slower than running directly on the platform, even for apps that are [ahead-of-time (AOT) compiled](https://learn.microsoft.com/en-us/aspnet/core/blazor/webassembly-build-tools-and-aot?view=aspnetcore-10.0#ahead-of-time-aot-compilation) for WebAssembly in the browser.

Blazor Server apps generally execute on the server quickly.

Blazor WebAssembly apps run using the .NET runtime for WebAssembly, which is slower than running directly on the platform.

Maintaining app code securely and privately on the server is a built-in feature of components rendered for the Blazor Server hosting model. Components rendered using the Blazor WebAssembly or Blazor Hybrid hosting models can use server-based APIs to access functionality that must be kept private and secure. The considerations for developing and maintaining server-based APIs described in the [Direct access to server and network resources](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#direct-access-to-server-and-network-resources) section apply. If the development and maintenance of server-based APIs isn't desirable for maintaining secure and private app code, render components for the Blazor Server hosting model.

Maintaining app code securely and privately on the server is a built-in feature of Blazor Server. Blazor WebAssembly and Blazor Hybrid apps can use server-based APIs to access functionality that must be kept private and secure. The considerations for developing and maintaining server-based APIs described in the [Direct access to server and network resources](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#direct-access-to-server-and-network-resources) section apply. If the development and maintenance of server-based APIs isn't desirable for maintaining secure and private app code, adopt the Blazor Server hosting model.

Maintaining app code securely and privately on the server is a built-in feature of Blazor Server. Blazor WebAssembly apps can use server-based APIs to access functionality that must be kept private and secure. The considerations for developing and maintaining server-based APIs described in the [Direct access to server and network resources](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0#direct-access-to-server-and-network-resources) section apply. If the development and maintenance of server-based APIs isn't desirable for maintaining secure and private app code, adopt the Blazor Server hosting model.

Standalone Blazor WebAssembly apps built as Progressive Web Apps (PWAs) and Blazor Hybrid apps can run offline, which is particularly useful when clients aren't able to connect to the Internet. Components rendered for the Blazor Server hosting model fail to run when the connection to the server is lost. If an app must run offline, standalone Blazor WebAssembly and Blazor Hybrid are the best choices.

Blazor WebAssembly apps built as Progressive Web Apps (PWAs) and Blazor Hybrid apps can run offline, which is particularly useful when clients aren't able to connect to the Internet. Blazor Server apps fail to run when the connection to the server is lost. If an app must run offline, Blazor WebAssembly and Blazor Hybrid are the best choices.

Blazor WebAssembly apps can run offline, which is particularly useful when clients aren't able to connect to the Internet. Blazor Server apps fail to run when the connection to the server is lost. If an app must run offline, Blazor WebAssembly is the best choice.

Static site hosting is possible with standalone Blazor WebAssembly apps because they're downloaded to clients as a set of static files. Standalone Blazor WebAssembly apps don't require a server to execute server-side code in order to download and run and can be delivered via a [Content Delivery Network (CDN)](https://developer.mozilla.org/docs/Glossary/CDN) (for example, [Azure CDN](https://azure.microsoft.com/services/cdn/)).

Although Blazor Hybrid apps are compiled into one or more self-contained deployment assets, the assets are usually provided to clients through a third-party app store. If static hosting is an app requirement, select standalone Blazor WebAssembly.

Components rendered using the Blazor WebAssembly or Blazor Hybrid hosting models execute on clients and thus offload processing to clients. Components rendered for the Blazor Server hosting model execute on a server, so server resource demand typically increases with the number of users and the amount of processing required per user. When it's possible to offload most or all of an app's processing to clients and the app processes a significant amount of data, Blazor WebAssembly or Blazor Hybrid is the best choice.

Blazor WebAssembly and Blazor Hybrid apps execute on clients and thus offload processing to clients. Blazor Server apps execute on a server, so server resource demand typically increases with the number of users and the amount of processing required per user. When it's possible to offload most or all of an app's processing to clients and the app processes a significant amount of data, Blazor WebAssembly or Blazor Hybrid is the best choice.

Blazor WebAssembly apps execute on clients and thus offload processing to clients. Blazor Server apps execute on a server, so server resource demand typically increases with the number of users and the amount of processing required per user. When it's possible to offload most or all of an app's processing to clients and the app processes a significant amount of data, Blazor WebAssembly is the best choice.

Blazor Hybrid apps have full access to native client API capabilities via .NET native app frameworks. In Blazor Hybrid apps, Razor components run directly in the native app, not on [WebAssembly](https://developer.mozilla.org/docs/WebAssembly). When full client capabilities are a requirement, Blazor Hybrid is the best choice.

Blazor Web Apps are updated on the next app refresh from the browser.

Blazor Hybrid apps are native client apps that typically require an installer and platform-specific deployment mechanism.

To set a component's hosting model to Blazor Server or Blazor WebAssembly at compile-time or dynamically at runtime, you set its _render mode_. Render modes are fully explained and demonstrated in the [ASP.NET Core Blazor render modes](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/render-modes?view=aspnetcore-10.0) article. We don't recommend that you jump from this article directly to the _Render modes_ article without reading the content in the articles between these two articles. For example, render modes are more easily understood by looking at Razor component examples, but basic Razor component structure and function isn't covered until the [ASP.NET Core Blazor fundamentals](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/?view=aspnetcore-10.0) article is reached. It's also helpful to learn about Blazor's project templates and tooling before working with the component examples in the _Render modes_ article.
