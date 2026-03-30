# Source: https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0

Title: Tutorial: Get started with ASP.NET Core SignalR using TypeScript and Webpack

URL Source: https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0

Markdown Content:
This tutorial demonstrates using [Webpack](https://webpack.js.org/) in an ASP.NET Core SignalR web app to bundle and build a client written in [TypeScript](https://www.typescriptlang.org/). Webpack enables developers to bundle and build the client-side resources of a web app.

In this tutorial, you learn how to:

*   Create an ASP.NET Core SignalR app
*   Configure the SignalR server
*   Configure a build pipeline using Webpack
*   Configure the SignalR TypeScript client
*   Enable communication between the client and the server

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/signalr-typescript-webpack/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

*   [Node.js](https://nodejs.org/) with [npm](https://www.npmjs.com/)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   [The latest version of Visual Studio](https://visualstudio.microsoft.com/downloads/) with the **ASP.NET and web development** workload.

[![Image 1: VS26 installer workloads](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev-2026.png?view=aspnetcore-10.0)](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev-2026.png?view=aspnetcore-10.0#lightbox)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)

By default, Visual Studio uses the version of npm found in its installation directory. To configure Visual Studio to look for npm in the `PATH` environment variable:

Launch the latest version of Visual Studio. At the start window, select **Continue without code**.

1.   Navigate to **Tools**>**Options**>**Projects and Solutions**>**Web Package Management**>**External Web Tools**.

2.   Select the `$(PATH)` entry from the list. Select the up arrow to move the entry to the second position in the list, and select **OK**:

![Image 2: Visual Studio Configuration.](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack/media/configure-path.png?view=aspnetcore-10.0)

To create a new ASP.NET Core web app:

1.   Use the **File**>**New**>**Project/Solution...** menu option.
2.   In the **Create a new project** dialog, select **ASP.NET Core Empty** template. Then select **Next**.
3.   In the **Configure your new project** dialog, enter `SignalRWebpack` for **Project name**. Select **Next**.
4.   In the **Additional information** dialog, select **.NET 10.0 (Long Term Support)** from the **Framework** drop-down. Select **Create**.

Add the [Microsoft.TypeScript.MSBuild](https://www.nuget.org/packages/Microsoft.TypeScript.MSBuild/) NuGet package to the project:

1.   In **Solution Explorer**, right-click the project node and select **Manage NuGet Packages...**.
2.   In the **Browse** tab, search for `Microsoft.TypeScript.MSBuild` and then select **Install** on the right to install the package.
3.   In the **Preview Changes** dialog, select **Apply**.
4.   In the **License Acceptance** dialog, select **I Accept**.

Visual Studio adds the NuGet package under the **Dependencies** node in **Solution Explorer**, enabling TypeScript compilation in the project.

In this section, you configure the ASP.NET Core web app to send and receive SignalR messages.

1.   In `Program.cs`, call [AddSignalR](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.signalrdependencyinjectionextensions.addsignalr):

```
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddSignalR();
```
2.   Again, in `Program.cs`, call [UseDefaultFiles](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.defaultfilesextensions.usedefaultfiles) and [UseStaticFiles](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.staticfileextensions.usestaticfiles):

```
var app = builder.Build();

app.UseDefaultFiles();
app.UseStaticFiles();
```

The preceding code allows the server to locate and serve the `index.html` file. The file is served whether the user enters its full URL or the root URL of the web app.

3.   Create a new directory named `Hubs` in the project root, `SignalRWebpack/`, for the SignalR hub class.

4.   Create a new file, `Hubs/ChatHub.cs`, with the following code:

```
using Microsoft.AspNetCore.SignalR;

namespace SignalRWebpack.Hubs;

public class ChatHub : Hub
{
    public async Task NewMessage(long username, string message) =>
        await Clients.All.SendAsync("messageReceived", username, message);
}
```

The preceding code broadcasts received messages to all connected users once the server receives them. It's unnecessary to have a generic `on` method to receive all the messages. A method named after the message name is enough.

In this example:

    *   The TypeScript client sends a message identified as `newMessage`.
    *   The C# `NewMessage` method expects the data sent by the client.
    *   A call is made to [SendAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.signalr.clientproxyextensions.sendasync) on [Clients.All](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.signalr.ihubclients-1.all#microsoft-aspnetcore-signalr-ihubclients-1-all).
    *   The received messages are sent to all clients connected to the hub.

5.   Add the following `using` statement at the top of `Program.cs` to resolve the `ChatHub` reference:

```
using SignalRWebpack.Hubs;
```
6.   In `Program.cs`, map the `/hub` route to the `ChatHub` hub. Replace the code that displays `Hello World!` with the following code:

```
app.MapHub<ChatHub>("/hub");
```

In this section, you create a [Node.js](https://nodejs.org/) project to convert TypeScript to JavaScript and bundle client-side resources, including HTML and CSS, using Webpack.

1.   Run the following command in the project root to create a `package.json` file:

```
npm init -y
```
2.   Add the highlighted property to the `package.json` file and save the file changes:

```
{
  "name": "signalrwebpack",
  "version": "1.0.0",
  "private": true,
  "description": "",
  "main": "index.js",
  "scripts": {
    "build": "webpack --mode=development --watch",
    "release": "webpack --mode=production",
    "publish": "npm run release && dotnet publish -c Release"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "type": "commonjs",
  "devDependencies": {
    "clean-webpack-plugin": "4.0.0",
    "css-loader": "7.1.3",
    "html-webpack-plugin": "5.6.6",
    "mini-css-extract-plugin": "2.10.0",
    "ts-loader": "9.5.4",
    "typescript": "5.9.3",
    "webpack": "5.104.1",
    "webpack-cli": "6.0.1"
  },
  "dependencies": {
    "@microsoft/signalr": "^10.0.0",
    "@types/node": "^25.0.10"
  }
}
```

Setting the `private` property to `true` prevents package installation warnings in the next step.

3.   Install the required npm packages. Run the following command from the project root:

```
npm i -D -E clean-webpack-plugin css-loader html-webpack-plugin mini-css-extract-plugin ts-loader typescript webpack webpack-cli
```

The `-E` option disables npm's default behavior of writing [semantic versioning](https://semver.org/) range operators to `package.json`. For example, `"webpack": "5.76.1"` is used instead of `"webpack": "^5.76.1"`. This option prevents unintended upgrades to newer package versions.

For more information, see the [npm-install](https://docs.npmjs.com/cli/install) documentation.

4.   Replace the `scripts` property of `package.json` file with the following code:

```
"scripts": {
  "build": "webpack --mode=development --watch",
  "release": "webpack --mode=production",
  "publish": "npm run release && dotnet publish -c Release"
},
```

The following scripts are defined:

    *   `build`: Bundles the client-side resources in development mode and watches for file changes. The file watcher causes the bundle to regenerate each time a project file changes. The `mode` option disables production optimizations, such as tree shaking and minification. use `build` in development only.
    *   `release`: Bundles the client-side resources in production mode.
    *   `publish`: Runs the `release` script to bundle the client-side resources in production mode. It calls the .NET CLI's [publish](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-publish) command to publish the app.

5.   Create a file named `webpack.config.js` in the project root, with the following code:

```
const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    entry: "./src/index.ts",
    output: {
        path: path.resolve(__dirname, "wwwroot"),
        filename: "[name].[chunkhash].js",
        publicPath: "/",
    },
    resolve: {
        extensions: [".js", ".ts"],
    },
    module: {
        rules: [
            {
                test: /\.ts$/,
                use: "ts-loader",
            },
            {
                test: /\.css$/,
                use: [MiniCssExtractPlugin.loader, "css-loader"],
            },
        ],
    },
    plugins: [
        new CleanWebpackPlugin(),
        new HtmlWebpackPlugin({
            template: "./src/index.html",
        }),
        new MiniCssExtractPlugin({
            filename: "css/[name].[chunkhash].css",
        }),
    ],
};
```

The preceding file configures the Webpack compilation process:

    *   The `output` property overrides the default value of `dist`. The bundle is instead emitted in the `wwwroot` directory.
    *   The `resolve.extensions` array includes `.js` to import the SignalR client JavaScript.

6.   Create a new directory named `src` in the project root, `SignalRWebpack/`, for the client code.

7.   Copy the `src` directory and its contents from the [sample project](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/signalr-typescript-webpack/samples/) into the project root. The `src` directory contains the following files:

    *   `index.html`, which defines the homepage's boilerplate markup:

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>ASP.NET Core SignalR with TypeScript and Webpack</title>
  </head>
  <body>
    <div id="divMessages" class="messages"></div>
    <div class="input-zone">
      <label id="lblMessage" for="tbMessage">Message:</label>
      <input id="tbMessage" class="input-zone-input" type="text" />
      <button id="btnSend">Send</button>
    </div>
  </body>
</html>
```
    *   `css/main.css`, which provides CSS styles for the homepage:

```
*,
*::before,
*::after {
  box-sizing: border-box;
}

html,
body {
  margin: 0;
  padding: 0;
}

.input-zone {
  align-items: center;
  display: flex;
  flex-direction: row;
  margin: 10px;
}

.input-zone-input {
  flex: 1;
  margin-right: 10px;
}

.message-author {
  font-weight: bold;
}

.messages {
  border: 1px solid #000;
  margin: 10px;
  max-height: 300px;
  min-height: 300px;
  overflow-y: auto;
  padding: 5px;
}
```
    *   `tsconfig.json`, which configures the TypeScript compiler to produce [ECMAScript](https://wikipedia.org/wiki/ECMAScript) 5-compatible JavaScript:

```
{
  "compilerOptions": {
    "target": "es5"
  }
}
```
    *   `index.ts`:

```
import * as signalR from "@microsoft/signalr";
import "./css/main.css";

const divMessages: HTMLDivElement = document.querySelector("#divMessages");
const tbMessage: HTMLInputElement = document.querySelector("#tbMessage");
const btnSend: HTMLButtonElement = document.querySelector("#btnSend");
const username = new Date().getTime();

const connection = new signalR.HubConnectionBuilder()
    .withUrl("/hub")
    .build();

connection.on("messageReceived", (username: string, message: string) => {
  const m = document.createElement("div");

  const author = document.createElement("div");
  author.className = "message-author";
  author.textContent = username;

  const content = document.createElement("div");
  content.textContent = message;

  m.append(author, content);

  divMessages.appendChild(m);
  divMessages.scrollTop = divMessages.scrollHeight;
});

connection.start().catch((err) => document.write(err));

tbMessage.addEventListener("keyup", (e: KeyboardEvent) => {
  if (e.key === "Enter") {
    send();
  }
});

btnSend.addEventListener("click", send);

function send() {
  connection.send("newMessage", username, tbMessage.value)
    .then(() => (tbMessage.value = ""));
}
```

The preceding code retrieves references to DOM elements and attaches two event handlers:

        *   `keyup`: Fires when the user types in the `tbMessage` textbox and calls the `send` function when the user presses the **Enter** key.
        *   `click`: Fires when the user selects the **Send** button and calls `send` function is called.

The `HubConnectionBuilder` class creates a new builder for configuring the server connection. The `withUrl` function configures the hub URL.

SignalR enables the exchange of messages between a client and a server. Each message has a specific name. For example, messages with the name `messageReceived` can run the logic responsible for displaying the new message in the messages zone. Listening to a specific message can be done via the `on` function. Any number of message names can be listened to. It's also possible to pass parameters to the message, such as the author's name and the content of the message received. Once the client receives a message, a new `div` element is created with the author's name and message content appended as child elements using `textContent`. It's added to the main `div` element displaying the messages.

Sending a message through the WebSockets connection requires calling the `send` method. The method's first parameter is the message name. The message data inhabits the other parameters. In this example, a message identified as `newMessage` is sent to the server. The message consists of the username and the user input from a text box. If the send works, the text box value is cleared.

8.   Run the following command at the project root:

```
npm i @microsoft/signalr @types/node
```

The preceding command installs:

    *   The [SignalR TypeScript client](https://www.npmjs.com/package/@microsoft/signalr), which allows the client to send messages to the server.
    *   The TypeScript type definitions for Node.js, which enables compile-time checking of Node.js types.

Confirm that the app works with the following steps:

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)

1.   Run Webpack in `release` mode. Using the **Package Manager Console** window, run the following command in the project root.

```
npm run release
```

This command generates the client-side assets to be served when running the app. The assets are placed in the `wwwroot` folder.

Webpack completed the following tasks:

    *   Purged the contents of the `wwwroot` directory.
    *   Converted the TypeScript to JavaScript in a process known as _transpilation_.
    *   Mangled the generated JavaScript to reduce file size in a process known as _minification_.
    *   Copied the processed JavaScript, CSS, and HTML files from `src` to the `wwwroot` directory.
    *   Injected the following elements into the `wwwroot/index.html` file: 
        *   A `<link>` tag, referencing the `wwwroot/main.<hash>.css` file. This tag is placed immediately before the closing `</head>` tag.
        *   A `<script>` tag, referencing the minified `wwwroot/main.<hash>.js` file. This tag is placed immediately after the closing `</title>` tag.

2.   Select **Debug**>**Start without debugging** to launch the app in a browser without attaching the debugger. The `wwwroot/index.html` file is served at `https://localhost:<port>`.

If there are compile errors, try closing and reopening the solution.

3.   Open another browser instance (any browser) and paste the URL in the address bar.

4.   Choose either browser, type something in the **Message** text box, and select the **Send** button. The unique user name and message are displayed on both pages instantly.

![Image 3: Message displayed in both browser windows.](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack/media/browser-message-broadcast.png?view=aspnetcore-10.0)

*   [Strongly typed hubs](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0#strongly-typed-hubs)
*   [Authentication and authorization in ASP.NET Core SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/authn-and-authz?view=aspnetcore-10.0)
*   [MessagePack Hub Protocol in SignalR for ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/signalr/messagepackhubprotocol?view=aspnetcore-10.0)

*   [ASP.NET Core SignalR JavaScript client](https://learn.microsoft.com/en-us/aspnet/core/signalr/javascript-client?view=aspnetcore-10.0)
*   [Use hubs in ASP.NET Core SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0)

This tutorial demonstrates using [Webpack](https://webpack.js.org/) in an ASP.NET Core SignalR web app to bundle and build a client written in [TypeScript](https://www.typescriptlang.org/). Webpack enables developers to bundle and build the client-side resources of a web app.

In this tutorial, you learn how to:

*   Create an ASP.NET Core SignalR app
*   Configure the SignalR server
*   Configure a build pipeline using Webpack
*   Configure the SignalR TypeScript client
*   Enable communication between the client and the server

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs.Samples/tree/main/tutorials/signalr-typescript-webpack/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

*   [Node.js](https://nodejs.org/) with [npm](https://www.npmjs.com/)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) with the **ASP.NET and web development** workload.

![Image 4: VS22 installer workloads](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)

By default, Visual Studio uses the version of npm found in its installation directory. To configure Visual Studio to look for npm in the `PATH` environment variable:

Launch Visual Studio. At the start window, select **Continue without code**.

1.   Navigate to **Tools**>**Options**>**Projects and Solutions**>**Web Package Management**>**External Web Tools**.

2.   Select the `$(PATH)` entry from the list. Select the up arrow to move the entry to the second position in the list, and select **OK**:

![Image 5: Visual Studio Configuration](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack/_static/8.x/signalr-configure-path-visual-studio-v17.8.0.png?view=aspnetcore-10.0).

To create a new ASP.NET Core web app:

1.   Use the **File**>**New**>**Project** menu option and choose the **ASP.NET Core Empty** template. Select **Next**.
2.   Name the project `SignalRWebpack`, and select **Create**.
3.   Select **.NET 8.0 (Long Term Support)** from the **Framework** drop-down. Select **Create**.

Add the [Microsoft.TypeScript.MSBuild](https://www.nuget.org/packages/Microsoft.TypeScript.MSBuild/) NuGet package to the project:

1.   In **Solution Explorer**, right-click the project node and select **Manage NuGet Packages**. In the **Browse** tab, search for `Microsoft.TypeScript.MSBuild` and then select **Install** on the right to install the package.

Visual Studio adds the NuGet package under the **Dependencies** node in **Solution Explorer**, enabling TypeScript compilation in the project.

In this section, you configure the ASP.NET Core web app to send and receive SignalR messages.

1.   In `Program.cs`, call [AddSignalR](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.signalrdependencyinjectionextensions.addsignalr):

```
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddSignalR();
```
2.   Again, in `Program.cs`, call [UseDefaultFiles](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.defaultfilesextensions.usedefaultfiles) and [UseStaticFiles](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.staticfileextensions.usestaticfiles):

```
var app = builder.Build();

app.UseDefaultFiles();
app.UseStaticFiles();
```

The preceding code allows the server to locate and serve the `index.html` file. The file is served whether the user enters its full URL or the root URL of the web app.

3.   Create a new directory named `Hubs` in the project root, `SignalRWebpack/`, for the SignalR hub class.

4.   Create a new file, `Hubs/ChatHub.cs`, with the following code:

```
using Microsoft.AspNetCore.SignalR;

namespace SignalRWebpack.Hubs;

public class ChatHub : Hub
{
    public async Task NewMessage(long username, string message) =>
        await Clients.All.SendAsync("messageReceived", username, message);
}
```

The preceding code broadcasts received messages to all connected users once the server receives them. It's unnecessary to have a generic `on` method to receive all the messages. A method named after the message name is enough.

In this example:

    *   The TypeScript client sends a message identified as `newMessage`.
    *   The C# `NewMessage` method expects the data sent by the client.
    *   A call is made to [SendAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.signalr.clientproxyextensions.sendasync) on [Clients.All](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.signalr.ihubclients-1.all#microsoft-aspnetcore-signalr-ihubclients-1-all).
    *   The received messages are sent to all clients connected to the hub.

5.   Add the following `using` statement at the top of `Program.cs` to resolve the `ChatHub` reference:

```
using SignalRWebpack.Hubs;
```
6.   In `Program.cs`, map the `/hub` route to the `ChatHub` hub. Replace the code that displays `Hello World!` with the following code:

```
app.MapHub<ChatHub>("/hub");
```

In this section, you create a [Node.js](https://nodejs.org/) project to convert TypeScript to JavaScript and bundle client-side resources, including HTML and CSS, using Webpack.

1.   Run the following command in the project root to create a `package.json` file:

```
npm init -y
```
2.   Add the highlighted property to the `package.json` file and save the file changes:

```
{
  "name": "SignalRWebpack",
  "version": "1.0.0",
  "private": true,
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

Setting the `private` property to `true` prevents package installation warnings in the next step.

3.   Install the required npm packages. Run the following command from the project root:

```
npm i -D -E clean-webpack-plugin css-loader html-webpack-plugin mini-css-extract-plugin ts-loader typescript webpack webpack-cli
```

The `-E` option disables npm's default behavior of writing [semantic versioning](https://semver.org/) range operators to `package.json`. For example, `"webpack": "5.76.1"` is used instead of `"webpack": "^5.76.1"`. This option prevents unintended upgrades to newer package versions.

For more information, see the [npm-install](https://docs.npmjs.com/cli/install) documentation.

4.   Replace the `scripts` property of `package.json` file with the following code:

```
"scripts": {
  "build": "webpack --mode=development --watch",
  "release": "webpack --mode=production",
  "publish": "npm run release && dotnet publish -c Release"
},
```

The following scripts are defined:

    *   `build`: Bundles the client-side resources in development mode and watches for file changes. The file watcher causes the bundle to regenerate each time a project file changes. The `mode` option disables production optimizations, such as tree shaking and minification. use `build` in development only.
    *   `release`: Bundles the client-side resources in production mode.
    *   `publish`: Runs the `release` script to bundle the client-side resources in production mode. It calls the .NET CLI's [publish](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-publish) command to publish the app.

5.   Create a file named `webpack.config.js` in the project root, with the following code:

```
const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    entry: "./src/index.ts",
    output: {
        path: path.resolve(__dirname, "wwwroot"),
        filename: "[name].[chunkhash].js",
        publicPath: "/",
    },
    resolve: {
        extensions: [".js", ".ts"],
    },
    module: {
        rules: [
            {
                test: /\.ts$/,
                use: "ts-loader",
            },
            {
                test: /\.css$/,
                use: [MiniCssExtractPlugin.loader, "css-loader"],
            },
        ],
    },
    plugins: [
        new CleanWebpackPlugin(),
        new HtmlWebpackPlugin({
            template: "./src/index.html",
        }),
        new MiniCssExtractPlugin({
            filename: "css/[name].[chunkhash].css",
        }),
    ],
};
```

The preceding file configures the Webpack compilation process:

    *   The `output` property overrides the default value of `dist`. The bundle is instead emitted in the `wwwroot` directory.
    *   The `resolve.extensions` array includes `.js` to import the SignalR client JavaScript.

6.   Create a new directory named `src` in the project root, `SignalRWebpack/`, for the client code.

7.   Copy the `src` directory and its contents from the [sample project](https://github.com/dotnet/AspNetCore.Docs.Samples/tree/main/tutorials/signalr-typescript-webpack/samples/8.x/SignalRWebpack/) into the project root. The `src` directory contains the following files:

    *   `index.html`, which defines the homepage's boilerplate markup:

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>ASP.NET Core SignalR with TypeScript and Webpack</title>
  </head>
  <body>
    <div id="divMessages" class="messages"></div>
    <div class="input-zone">
      <label id="lblMessage" for="tbMessage">Message:</label>
      <input id="tbMessage" class="input-zone-input" type="text" />
      <button id="btnSend">Send</button>
    </div>
  </body>
</html>
```
    *   `css/main.css`, which provides CSS styles for the homepage:

```
*,
*::before,
*::after {
  box-sizing: border-box;
}

html,
body {
  margin: 0;
  padding: 0;
}

.input-zone {
  align-items: center;
  display: flex;
  flex-direction: row;
  margin: 10px;
}

.input-zone-input {
  flex: 1;
  margin-right: 10px;
}

.message-author {
  font-weight: bold;
}

.messages {
  border: 1px solid #000;
  margin: 10px;
  max-height: 300px;
  min-height: 300px;
  overflow-y: auto;
  padding: 5px;
}
```
    *   `tsconfig.json`, which configures the TypeScript compiler to produce [ECMAScript](https://wikipedia.org/wiki/ECMAScript) 5-compatible JavaScript:

```
{
  "compilerOptions": {
    "target": "es5"
  }
}
```
    *   `index.ts`:

```
import * as signalR from "@microsoft/signalr";
import "./css/main.css";

const divMessages: HTMLDivElement = document.querySelector("#divMessages");
const tbMessage: HTMLInputElement = document.querySelector("#tbMessage");
const btnSend: HTMLButtonElement = document.querySelector("#btnSend");
const username = new Date().getTime();

const connection = new signalR.HubConnectionBuilder()
    .withUrl("/hub")
    .build();

connection.on("messageReceived", (username: string, message: string) => {
  const m = document.createElement("div");

  m.innerHTML = `<div class="message-author">${username}</div><div>${message}</div>`;

  divMessages.appendChild(m);
  divMessages.scrollTop = divMessages.scrollHeight;
});

connection.start().catch((err) => document.write(err));

tbMessage.addEventListener("keyup", (e: KeyboardEvent) => {
  if (e.key === "Enter") {
    send();
  }
});

btnSend.addEventListener("click", send);

function send() {
  connection.send("newMessage", username, tbMessage.value)
    .then(() => (tbMessage.value = ""));
}
```

The preceding code retrieves references to DOM elements and attaches two event handlers:

        *   `keyup`: Fires when the user types in the `tbMessage` textbox and calls the `send` function when the user presses the **Enter** key.
        *   `click`: Fires when the user selects the **Send** button and calls `send` function is called.

The `HubConnectionBuilder` class creates a new builder for configuring the server connection. The `withUrl` function configures the hub URL.

SignalR enables the exchange of messages between a client and a server. Each message has a specific name. For example, messages with the name `messageReceived` can run the logic responsible for displaying the new message in the messages zone. Listening to a specific message can be done via the `on` function. Any number of message names can be listened to. It's also possible to pass parameters to the message, such as the author's name and the content of the message received. Once the client receives a message, a new `div` element is created with the author's name and message content appended as child elements using `textContent`. It's added to the main `div` element displaying the messages.

Sending a message through the WebSockets connection requires calling the `send` method. The method's first parameter is the message name. The message data inhabits the other parameters. In this example, a message identified as `newMessage` is sent to the server. The message consists of the username and the user input from a text box. If the send works, the text box value is cleared.

8.   Run the following command at the project root:

```
npm i @microsoft/signalr @types/node
```

The preceding command installs:

    *   The [SignalR TypeScript client](https://www.npmjs.com/package/@microsoft/signalr), which allows the client to send messages to the server.
    *   The TypeScript type definitions for Node.js, which enables compile-time checking of Node.js types.

Confirm that the app works with the following steps:

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)

1.   Run Webpack in `release` mode. Using the **Package Manager Console** window, run the following command in the project root.

```
npm run release
```

This command generates the client-side assets to be served when running the app. The assets are placed in the `wwwroot` folder.

Webpack completed the following tasks:

    *   Purged the contents of the `wwwroot` directory.
    *   Converted the TypeScript to JavaScript in a process known as _transpilation_.
    *   Mangled the generated JavaScript to reduce file size in a process known as _minification_.
    *   Copied the processed JavaScript, CSS, and HTML files from `src` to the `wwwroot` directory.
    *   Injected the following elements into the `wwwroot/index.html` file: 
        *   A `<link>` tag, referencing the `wwwroot/main.<hash>.css` file. This tag is placed immediately before the closing `</head>` tag.
        *   A `<script>` tag, referencing the minified `wwwroot/main.<hash>.js` file. This tag is placed immediately after the closing `</title>` tag.

2.   Select **Debug**>**Start without debugging** to launch the app in a browser without attaching the debugger. The `wwwroot/index.html` file is served at `https://localhost:<port>`.

If there are compile errors, try closing and reopening the solution.

3.   Open another browser instance (any browser) and paste the URL in the address bar.

4.   Choose either browser, type something in the **Message** text box, and select the **Send** button. The unique user name and message are displayed on both pages instantly.

![Image 6: Message displayed in both browser windows](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack/_static/browsers-message-broadcast.png?view=aspnetcore-10.0)

*   [Strongly typed hubs](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0#strongly-typed-hubs)
*   [Authentication and authorization in ASP.NET Core SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/authn-and-authz?view=aspnetcore-10.0)
*   [MessagePack Hub Protocol in SignalR for ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/signalr/messagepackhubprotocol?view=aspnetcore-10.0)

*   [ASP.NET Core SignalR JavaScript client](https://learn.microsoft.com/en-us/aspnet/core/signalr/javascript-client?view=aspnetcore-10.0)
*   [Use hubs in ASP.NET Core SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0)

This tutorial demonstrates using [Webpack](https://webpack.js.org/) in an ASP.NET Core SignalR web app to bundle and build a client written in [TypeScript](https://www.typescriptlang.org/). Webpack enables developers to bundle and build the client-side resources of a web app.

In this tutorial, you learn how to:

*   Create an ASP.NET Core SignalR app
*   Configure the SignalR server
*   Configure a build pipeline using Webpack
*   Configure the SignalR TypeScript client
*   Enable communication between the client and the server

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs.Samples/tree/main/tutorials/signalr-typescript-webpack/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

*   [Node.js](https://nodejs.org/) with [npm](https://www.npmjs.com/)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/vs/#download) with the **ASP.NET and web development** workload.

![Image 7: VS22 installer workloads](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)

By default, Visual Studio uses the version of npm found in its installation directory. To configure Visual Studio to look for npm in the `PATH` environment variable:

Launch Visual Studio. At the start window, select **Continue without code**.

1.   Navigate to **Tools**>**Options**>**Projects and Solutions**>**Web Package Management**>**External Web Tools**.

2.   Select the `$(PATH)` entry from the list. Select the up arrow to move the entry to the second position in the list, and select **OK**:

![Image 8: Visual Studio Configuration](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack/_static/7.x/signalr-configure-path-visual-studio.png?view=aspnetcore-10.0).

To create a new ASP.NET Core web app:

1.   Use the **File**>**New**>**Project** menu option and choose the **ASP.NET Core Empty** template. Select **Next**.
2.   Name the project `SignalRWebpack`, and select **Create**.
3.   Select **.NET 7.0 (Standard Term Support)** from the **Framework** drop-down. Select **Create**.

Add the [Microsoft.TypeScript.MSBuild](https://www.nuget.org/packages/Microsoft.TypeScript.MSBuild/) NuGet package to the project:

1.   In **Solution Explorer**, right-click the project node and select **Manage NuGet Packages**. In the **Browse** tab, search for `Microsoft.TypeScript.MSBuild` and then select **Install** on the right to install the package.

Visual Studio adds the NuGet package under the **Dependencies** node in **Solution Explorer**, enabling TypeScript compilation in the project.

In this section, you configure the ASP.NET Core web app to send and receive SignalR messages.

1.   In `Program.cs`, call [AddSignalR](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.signalrdependencyinjectionextensions.addsignalr):

```
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddSignalR();
```
2.   Again, in `Program.cs`, call [UseDefaultFiles](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.defaultfilesextensions.usedefaultfiles) and [UseStaticFiles](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.staticfileextensions.usestaticfiles):

```
var app = builder.Build();

app.UseDefaultFiles();
app.UseStaticFiles();
```

The preceding code allows the server to locate and serve the `index.html` file. The file is served whether the user enters its full URL or the root URL of the web app.

3.   Create a new directory named `Hubs` in the project root, `SignalRWebpack/`, for the SignalR hub class.

4.   Create a new file, `Hubs/ChatHub.cs`, with the following code:

```
using Microsoft.AspNetCore.SignalR;

namespace SignalRWebpack.Hubs;

public class ChatHub : Hub
{
    public async Task NewMessage(long username, string message) =>
        await Clients.All.SendAsync("messageReceived", username, message);
}
```

The preceding code broadcasts received messages to all connected users once the server receives them. It's unnecessary to have a generic `on` method to receive all the messages. A method named after the message name is enough.

In this example:

    *   The TypeScript client sends a message identified as `newMessage`.
    *   The C# `NewMessage` method expects the data sent by the client.
    *   A call is made to [SendAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.signalr.clientproxyextensions.sendasync) on [Clients.All](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.signalr.ihubclients-1.all#microsoft-aspnetcore-signalr-ihubclients-1-all).
    *   The received messages are sent to all clients connected to the hub.

5.   Add the following `using` statement at the top of `Program.cs` to resolve the `ChatHub` reference:

```
using SignalRWebpack.Hubs;
```
6.   In `Program.cs`, map the `/hub` route to the `ChatHub` hub. Replace the code that displays `Hello World!` with the following code:

```
app.MapHub<ChatHub>("/hub");
```

In this section, you create a [Node.js](https://nodejs.org/) project to convert TypeScript to JavaScript and bundle client-side resources, including HTML and CSS, using Webpack.

1.   Run the following command in the project root to create a `package.json` file:

```
npm init -y
```
2.   Add the highlighted property to the `package.json` file and save the file changes:

```
{
  "name": "SignalRWebpack",
  "version": "1.0.0",
  "private": true,
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

Setting the `private` property to `true` prevents package installation warnings in the next step.

3.   Install the required npm packages. Run the following command from the project root:

```
npm i -D -E clean-webpack-plugin css-loader html-webpack-plugin mini-css-extract-plugin ts-loader typescript webpack webpack-cli
```

The `-E` option disables npm's default behavior of writing [semantic versioning](https://semver.org/) range operators to `package.json`. For example, `"webpack": "5.76.1"` is used instead of `"webpack": "^5.76.1"`. This option prevents unintended upgrades to newer package versions.

For more information, see the [npm-install](https://docs.npmjs.com/cli/install) documentation.

4.   Replace the `scripts` property of `package.json` file with the following code:

```
"scripts": {
  "build": "webpack --mode=development --watch",
  "release": "webpack --mode=production",
  "publish": "npm run release && dotnet publish -c Release"
},
```

The following scripts are defined:

    *   `build`: Bundles the client-side resources in development mode and watches for file changes. The file watcher causes the bundle to regenerate each time a project file changes. The `mode` option disables production optimizations, such as tree shaking and minification. use `build` in development only.
    *   `release`: Bundles the client-side resources in production mode.
    *   `publish`: Runs the `release` script to bundle the client-side resources in production mode. It calls the .NET CLI's [publish](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-publish) command to publish the app.

5.   Create a file named `webpack.config.js` in the project root, with the following code:

```
const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    entry: "./src/index.ts",
    output: {
        path: path.resolve(__dirname, "wwwroot"),
        filename: "[name].[chunkhash].js",
        publicPath: "/",
    },
    resolve: {
        extensions: [".js", ".ts"],
    },
    module: {
        rules: [
            {
                test: /\.ts$/,
                use: "ts-loader",
            },
            {
                test: /\.css$/,
                use: [MiniCssExtractPlugin.loader, "css-loader"],
            },
        ],
    },
    plugins: [
        new CleanWebpackPlugin(),
        new HtmlWebpackPlugin({
            template: "./src/index.html",
        }),
        new MiniCssExtractPlugin({
            filename: "css/[name].[chunkhash].css",
        }),
    ],
};
```

The preceding file configures the Webpack compilation process:

    *   The `output` property overrides the default value of `dist`. The bundle is instead emitted in the `wwwroot` directory.
    *   The `resolve.extensions` array includes `.js` to import the SignalR client JavaScript.

6.   Copy the `src` directory and its contents from the [sample project](https://github.com/dotnet/AspNetCore.Docs.Samples/tree/main/tutorials/signalr-typescript-webpack/samples/7.x/SignalRWebpack/) into the project root. The `src` directory contains the following files:

    *   `index.html`, which defines the homepage's boilerplate markup:

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>ASP.NET Core SignalR with TypeScript and Webpack</title>
  </head>
  <body>
    <div id="divMessages" class="messages"></div>
    <div class="input-zone">
      <label id="lblMessage" for="tbMessage">Message:</label>
      <input id="tbMessage" class="input-zone-input" type="text" />
      <button id="btnSend">Send</button>
    </div>
  </body>
</html>
```
    *   `css/main.css`, which provides CSS styles for the homepage:

```
*,
*::before,
*::after {
  box-sizing: border-box;
}

html,
body {
  margin: 0;
  padding: 0;
}

.input-zone {
  align-items: center;
  display: flex;
  flex-direction: row;
  margin: 10px;
}

.input-zone-input {
  flex: 1;
  margin-right: 10px;
}

.message-author {
  font-weight: bold;
}

.messages {
  border: 1px solid #000;
  margin: 10px;
  max-height: 300px;
  min-height: 300px;
  overflow-y: auto;
  padding: 5px;
}
```
    *   `tsconfig.json`, which configures the TypeScript compiler to produce [ECMAScript](https://wikipedia.org/wiki/ECMAScript) 5-compatible JavaScript:

```
{
  "compilerOptions": {
    "target": "es5"
  }
}
```
    *   `index.ts`:

```
import * as signalR from "@microsoft/signalr";
import "./css/main.css";

const divMessages: HTMLDivElement = document.querySelector("#divMessages");
const tbMessage: HTMLInputElement = document.querySelector("#tbMessage");
const btnSend: HTMLButtonElement = document.querySelector("#btnSend");
const username = new Date().getTime();

const connection = new signalR.HubConnectionBuilder()
    .withUrl("/hub")
    .build();

connection.on("messageReceived", (username: string, message: string) => {
  const m = document.createElement("div");

  m.innerHTML = `<div class="message-author">${username}</div><div>${message}</div>`;

  divMessages.appendChild(m);
  divMessages.scrollTop = divMessages.scrollHeight;
});

connection.start().catch((err) => document.write(err));

tbMessage.addEventListener("keyup", (e: KeyboardEvent) => {
  if (e.key === "Enter") {
    send();
  }
});

btnSend.addEventListener("click", send);

function send() {
  connection.send("newMessage", username, tbMessage.value)
    .then(() => (tbMessage.value = ""));
}
```

The preceding code retrieves references to DOM elements and attaches two event handlers:

        *   `keyup`: Fires when the user types in the `tbMessage` textbox and calls the `send` function when the user presses the **Enter** key.
        *   `click`: Fires when the user selects the **Send** button and calls `send` function is called.

The `HubConnectionBuilder` class creates a new builder for configuring the server connection. The `withUrl` function configures the hub URL.

SignalR enables the exchange of messages between a client and a server. Each message has a specific name. For example, messages with the name `messageReceived` can run the logic responsible for displaying the new message in the messages zone. Listening to a specific message can be done via the `on` function. Any number of message names can be listened to. It's also possible to pass parameters to the message, such as the author's name and the content of the message received. Once the client receives a message, a new `div` element is created with the author's name and message content appended as child elements using `textContent`. It's added to the main `div` element displaying the messages.

Sending a message through the WebSockets connection requires calling the `send` method. The method's first parameter is the message name. The message data inhabits the other parameters. In this example, a message identified as `newMessage` is sent to the server. The message consists of the username and the user input from a text box. If the send works, the text box value is cleared.

7.   Run the following command at the project root:

```
npm i @microsoft/signalr @types/node
```

The preceding command installs:

    *   The [SignalR TypeScript client](https://www.npmjs.com/package/@microsoft/signalr), which allows the client to send messages to the server.
    *   The TypeScript type definitions for Node.js, which enables compile-time checking of Node.js types.

Confirm that the app works with the following steps:

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)

1.   Run Webpack in `release` mode. Using the **Package Manager Console** window, run the following command in the project root.

```
npm run release
```

This command generates the client-side assets to be served when running the app. The assets are placed in the `wwwroot` folder.

Webpack completed the following tasks:

    *   Purged the contents of the `wwwroot` directory.
    *   Converted the TypeScript to JavaScript in a process known as _transpilation_.
    *   Mangled the generated JavaScript to reduce file size in a process known as _minification_.
    *   Copied the processed JavaScript, CSS, and HTML files from `src` to the `wwwroot` directory.
    *   Injected the following elements into the `wwwroot/index.html` file: 
        *   A `<link>` tag, referencing the `wwwroot/main.<hash>.css` file. This tag is placed immediately before the closing `</head>` tag.
        *   A `<script>` tag, referencing the minified `wwwroot/main.<hash>.js` file. This tag is placed immediately after the closing `</title>` tag.

2.   Select **Debug**>**Start without debugging** to launch the app in a browser without attaching the debugger. The `wwwroot/index.html` file is served at `https://localhost:<port>`.

If there are compile errors, try closing and reopening the solution.

3.   Open another browser instance (any browser) and paste the URL in the address bar.

4.   Choose either browser, type something in the **Message** text box, and select the **Send** button. The unique user name and message are displayed on both pages instantly.

![Image 9: Message displayed in both browser windows](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack/_static/browsers-message-broadcast.png?view=aspnetcore-10.0)

*   [Strongly typed hubs](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0#strongly-typed-hubs)
*   [Authentication and authorization in ASP.NET Core SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/authn-and-authz?view=aspnetcore-10.0)
*   [MessagePack Hub Protocol in SignalR for ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/signalr/messagepackhubprotocol?view=aspnetcore-10.0)

*   [ASP.NET Core SignalR JavaScript client](https://learn.microsoft.com/en-us/aspnet/core/signalr/javascript-client?view=aspnetcore-10.0)
*   [Use hubs in ASP.NET Core SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0)

This tutorial demonstrates using [Webpack](https://webpack.js.org/) in an ASP.NET Core SignalR web app to bundle and build a client written in [TypeScript](https://www.typescriptlang.org/). Webpack enables developers to bundle and build the client-side resources of a web app.

In this tutorial, you learn how to:

*   Create an ASP.NET Core SignalR app
*   Configure the SignalR server
*   Configure a build pipeline using Webpack
*   Configure the SignalR TypeScript client
*   Enable communication between the client and the server

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs.Samples/tree/main/tutorials/signalr-typescript-webpack/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

*   [Node.js](https://nodejs.org/) with [npm](https://www.npmjs.com/)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/vs/#download) with the **ASP.NET and web development** workload.
*   [.NET 6 SDK](https://dotnet.microsoft.com/download/dotnet/6.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)

By default, Visual Studio uses the version of npm found in its installation directory. To configure Visual Studio to look for npm in the `PATH` environment variable:

1.   Launch Visual Studio. At the start window, select **Continue without code**.

2.   Navigate to **Tools**>**Options**>**Projects and Solutions**>**Web Package Management**>**External Web Tools**.

3.   Select the `$(PATH)` entry from the list. Select the up arrow to move the entry to the second position in the list, and select **OK**:

![Image 10: Visual Studio Configuration](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack/_static/signalr-configure-path-visual-studio.png?view=aspnetcore-10.0).

To create a new ASP.NET Core web app:

1.   Use the **File**>**New**>**Project** menu option and choose the **ASP.NET Core Empty** template. Select **Next**.
2.   Name the project `SignalRWebpack`, and select **Create**.
3.   Select **.NET 6.0 (Long Term Support)** from the **Framework** drop-down. Select **Create**.

Add the [Microsoft.TypeScript.MSBuild](https://www.nuget.org/packages/Microsoft.TypeScript.MSBuild/) NuGet package to the project:

1.   In **Solution Explorer**, right-click the project node and select **Manage NuGet Packages**. In the **Browse** tab, search for `Microsoft.TypeScript.MSBuild` and then select **Install** on the right to install the package.

Visual Studio adds the NuGet package under the **Dependencies** node in **Solution Explorer**, enabling TypeScript compilation in the project.

In this section, you configure the ASP.NET Core web app to send and receive SignalR messages.

1.   In `Program.cs`, call [AddSignalR](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.signalrdependencyinjectionextensions.addsignalr):

```
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddSignalR();
```
2.   Again, in `Program.cs`, call [UseDefaultFiles](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.defaultfilesextensions.usedefaultfiles) and [UseStaticFiles](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.staticfileextensions.usestaticfiles):

```
var app = builder.Build();

app.UseDefaultFiles();
app.UseStaticFiles();
```

The preceding code allows the server to locate and serve the `index.html` file. The file is served whether the user enters its full URL or the root URL of the web app.

3.   Create a new directory named `Hubs` in the project root, `SignalRWebpack/`, for the SignalR hub class.

4.   Create a new file, `Hubs/ChatHub.cs`, with the following code:

```
using Microsoft.AspNetCore.SignalR;

namespace SignalRWebpack.Hubs;

public class ChatHub : Hub
{
    public async Task NewMessage(long username, string message) =>
        await Clients.All.SendAsync("messageReceived", username, message);
}
```

The preceding code broadcasts received messages to all connected users once the server receives them. It's unnecessary to have a generic `on` method to receive all the messages. A method named after the message name is enough.

In this example, the TypeScript client sends a message identified as `newMessage`. The C# `NewMessage` method expects the data sent by the client. A call is made to [SendAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.signalr.clientproxyextensions.sendasync) on [Clients.All](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.signalr.ihubclients-1.all#microsoft-aspnetcore-signalr-ihubclients-1-all). The received messages are sent to all clients connected to the hub.

5.   Add the following `using` statement at the top of `Program.cs` to resolve the `ChatHub` reference:

```
using SignalRWebpack.Hubs;
```
6.   In `Program.cs`, map the `/hub` route to the `ChatHub` hub. Replace the code that displays `Hello World!` with the following code:

```
app.MapHub<ChatHub>("/hub");
```

In this section, you create a [Node.js](https://nodejs.org/) project to convert TypeScript to JavaScript and bundle client-side resources, including HTML and CSS, using Webpack.

1.   Run the following command in the project root to create a `package.json` file:

```
npm init -y
```
2.   Add the highlighted property to the `package.json` file and save the file changes:

```
{
  "name": "SignalRWebpack",
  "version": "1.0.0",
  "private": true,
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

Setting the `private` property to `true` prevents package installation warnings in the next step.

3.   Install the required npm packages. Run the following command from the project root:

```
npm i -D -E clean-webpack-plugin css-loader html-webpack-plugin mini-css-extract-plugin ts-loader typescript webpack webpack-cli
```

The `-E` option disables npm's default behavior of writing [semantic versioning](https://semver.org/) range operators to `package.json`. For example, `"webpack": "5.70.0"` is used instead of `"webpack": "^5.70.0"`. This option prevents unintended upgrades to newer package versions.

For more information, see the [npm-install](https://docs.npmjs.com/cli/install) documentation.

4.   Replace the `scripts` property of `package.json` file with the following code:

```
"scripts": {
  "build": "webpack --mode=development --watch",
  "release": "webpack --mode=production",
  "publish": "npm run release && dotnet publish -c Release"
},
```

The following scripts are defined:

    *   `build`: Bundles the client-side resources in development mode and watches for file changes. The file watcher causes the bundle to regenerate each time a project file changes. The `mode` option disables production optimizations, such as tree shaking and minification. use `build` in development only.
    *   `release`: Bundles the client-side resources in production mode.
    *   `publish`: Runs the `release` script to bundle the client-side resources in production mode. It calls the .NET CLI's [publish](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-publish) command to publish the app.

5.   Create a file named `webpack.config.js` in the project root, with the following code:

```
const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  entry: "./src/index.ts",
  output: {
    path: path.resolve(__dirname, "wwwroot"),
    filename: "[name].[chunkhash].js",
    publicPath: "/",
  },
  resolve: {
    extensions: [".js", ".ts"],
  },
  module: {
    rules: [
      {
        test: /\.ts$/,
        use: "ts-loader",
      },
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, "css-loader"],
      },
    ],
  },
  plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      template: "./src/index.html",
    }),
    new MiniCssExtractPlugin({
      filename: "css/[name].[chunkhash].css",
    }),
  ],
};
```

The preceding file configures the Webpack compilation process:

    *   The `output` property overrides the default value of `dist`. The bundle is instead emitted in the `wwwroot` directory.
    *   The `resolve.extensions` array includes `.js` to import the SignalR client JavaScript.

6.   Copy the `src` directory and its contents from the [sample project](https://github.com/dotnet/AspNetCore.Docs.Samples/tree/main/tutorials/signalr-typescript-webpack/samples/6.x/SignalRWebpack/) into the project root. The `src` directory contains the following files:

    *   `index.html`, which defines the homepage's boilerplate markup:

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>ASP.NET Core SignalR with TypeScript and Webpack</title>
  </head>
  <body>
    <div id="divMessages" class="messages"></div>
    <div class="input-zone">
      <label id="lblMessage" for="tbMessage">Message:</label>
      <input id="tbMessage" class="input-zone-input" type="text" />
      <button id="btnSend">Send</button>
    </div>
  </body>
</html>
```
    *   `css/main.css`, which provides CSS styles for the homepage:

```
*,
*::before,
*::after {
  box-sizing: border-box;
}

html,
body {
  margin: 0;
  padding: 0;
}

.input-zone {
  align-items: center;
  display: flex;
  flex-direction: row;
  margin: 10px;
}

.input-zone-input {
  flex: 1;
  margin-right: 10px;
}

.message-author {
  font-weight: bold;
}

.messages {
  border: 1px solid #000;
  margin: 10px;
  max-height: 300px;
  min-height: 300px;
  overflow-y: auto;
  padding: 5px;
}
```
    *   `tsconfig.json`, which configures the TypeScript compiler to produce [ECMAScript](https://wikipedia.org/wiki/ECMAScript) 5-compatible JavaScript:

```
{
  "compilerOptions": {
    "target": "es5"
  }
}
```
    *   `index.ts`:

```
import * as signalR from "@microsoft/signalr";
import "./css/main.css";

const divMessages: HTMLDivElement = document.querySelector("#divMessages");
const tbMessage: HTMLInputElement = document.querySelector("#tbMessage");
const btnSend: HTMLButtonElement = document.querySelector("#btnSend");
const username = new Date().getTime();

const connection = new signalR.HubConnectionBuilder()
    .withUrl("/hub")
    .build();

connection.on("messageReceived", (username: string, message: string) => {
  const m = document.createElement("div");

  m.innerHTML = `<div class="message-author">${username}</div><div>${message}</div>`;

  divMessages.appendChild(m);
  divMessages.scrollTop = divMessages.scrollHeight;
});

connection.start().catch((err) => document.write(err));

tbMessage.addEventListener("keyup", (e: KeyboardEvent) => {
  if (e.key === "Enter") {
    send();
  }
});

btnSend.addEventListener("click", send);

function send() {
  connection.send("newMessage", username, tbMessage.value)
    .then(() => (tbMessage.value = ""));
}
```

The preceding code retrieves references to DOM elements and attaches two event handlers:

    *   `keyup`: Fires when the user types in the `tbMessage` textbox and calls the `send` function when the user presses the **Enter** key.
    *   `click`: Fires when the user selects the **Send** button and calls `send` function is called.

The `HubConnectionBuilder` class creates a new builder for configuring the server connection. The `withUrl` function configures the hub URL.

SignalR enables the exchange of messages between a client and a server. Each message has a specific name. For example, messages with the name `messageReceived` can run the logic responsible for displaying the new message in the messages zone. Listening to a specific message can be done via the `on` function. Any number of message names can be listened to. It's also possible to pass parameters to the message, such as the author's name and the content of the message received. Once the client receives a message, a new `div` element is created with the author's name and message content appended as child elements using `textContent`. It's added to the main `div` element displaying the messages.

Sending a message through the WebSockets connection requires calling the `send` method. The method's first parameter is the message name. The message data inhabits the other parameters. In this example, a message identified as `newMessage` is sent to the server. The message consists of the username and the user input from a text box. If the send works, the text box value is cleared.

7.   Run the following command at the project root:

```
npm i @microsoft/signalr @types/node
```

The preceding command installs:

    *   The [SignalR TypeScript client](https://www.npmjs.com/package/@microsoft/signalr), which allows the client to send messages to the server.
    *   The TypeScript type definitions for Node.js, which enables compile-time checking of Node.js types.

Confirm that the app works with the following steps:

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)

1.   Run Webpack in `release` mode. Using the **Package Manager Console** window, run the following command in the project root. If you aren't in the project root, enter `cd SignalRWebpack` before entering the command.

```
npm run release
```

This command generates the client-side assets to be served when running the app. The assets are placed in the `wwwroot` folder.

Webpack completed the following tasks:

    *   Purged the contents of the `wwwroot` directory.
    *   Converted the TypeScript to JavaScript in a process known as _transpilation_.
    *   Mangled the generated JavaScript to reduce file size in a process known as _minification_.
    *   Copied the processed JavaScript, CSS, and HTML files from `src` to the `wwwroot` directory.
    *   Injected the following elements into the `wwwroot/index.html` file: 
        *   A `<link>` tag, referencing the `wwwroot/main.<hash>.css` file. This tag is placed immediately before the closing `</head>` tag.
        *   A `<script>` tag, referencing the minified `wwwroot/main.<hash>.js` file. This tag is placed immediately after the closing `</title>` tag.

2.   Select **Debug**>**Start without debugging** to launch the app in a browser without attaching the debugger. The `wwwroot/index.html` file is served at `https://localhost:<port>`.

If you get compile errors, try closing and reopening the solution.

3.   Open another browser instance (any browser) and paste the URL in the address bar.

4.   Choose either browser, type something in the **Message** text box, and select the **Send** button. The unique user name and message are displayed on both pages instantly.

![Image 11: Message displayed in both browser windows](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack/_static/browsers-message-broadcast.png?view=aspnetcore-10.0)

*   [Strongly typed hubs](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0#strongly-typed-hubs)
*   [Authentication and authorization in ASP.NET Core SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/authn-and-authz?view=aspnetcore-10.0)
*   [MessagePack Hub Protocol in SignalR for ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/signalr/messagepackhubprotocol?view=aspnetcore-10.0)

*   [ASP.NET Core SignalR JavaScript client](https://learn.microsoft.com/en-us/aspnet/core/signalr/javascript-client?view=aspnetcore-10.0)
*   [Use hubs in ASP.NET Core SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0)

This tutorial demonstrates using [Webpack](https://webpack.js.org/) in an ASP.NET Core SignalR web app to bundle and build a client written in [TypeScript](https://www.typescriptlang.org/). Webpack enables developers to bundle and build the client-side resources of a web app.

In this tutorial, you learn how to:

*   Scaffold a starter ASP.NET Core SignalR app
*   Configure the SignalR TypeScript client
*   Configure a build pipeline using Webpack
*   Configure the SignalR server
*   Enable communication between client and server

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/signalr-typescript-webpack/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   [Visual Studio 2019](https://visualstudio.microsoft.com/downloads/?utm_medium=microsoft&utm_source=learn.microsoft.com&utm_campaign=inline+link&utm_content=download+vs2019) with the **ASP.NET and web development** workload
*   [.NET Core SDK 3.0 or later](https://dotnet.microsoft.com/download/dotnet-core)
*   [Node.js](https://nodejs.org/) with [npm](https://www.npmjs.com/)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)

Configure Visual Studio to look for npm in the _PATH_ environment variable. By default, Visual Studio uses the version of npm found in its installation directory. Follow these instructions in Visual Studio:

1.   Launch Visual Studio. At the start window, select **Continue without code**.

2.   Navigate to **Tools**>**Options**>**Projects and Solutions**>**Web Package Management**>**External Web Tools**.

3.   Select the _$(PATH)_ entry from the list. Select the up arrow to move the entry to the second position in the list, and select **OK**.

![Image 12: Visual Studio Configuration](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack/_static/signalr-configure-path-visual-studio.png?view=aspnetcore-10.0).

Visual Studio configuration is complete.

1.   Use the **File**>**New**>**Project** menu option and choose the **ASP.NET Core Web Application** template. Select **Next**.
2.   Name the project *SignalRWebPac``, and select **Create**.
3.   Select _.NET Core_ from the target framework drop-down, and select _ASP.NET Core 3.1_ from the framework selector drop-down. Select the **Empty** template, and select **Create**.

Add the `Microsoft.TypeScript.MSBuild` package to the project:

1.   In **Solution Explorer** (right pane), right-click the project node and select **Manage NuGet Packages**. In the **Browse** tab, search for `Microsoft.TypeScript.MSBuild`, and then click **Install** on the right to install the package.

Visual Studio adds the NuGet package under the **Dependencies** node in **Solution Explorer**, enabling TypeScript compilation in the project.

The following steps configure the conversion of TypeScript to JavaScript and the bundling of client-side resources.

1.   Run the following command in the project root to create a `package.json` file:

```
npm init -y
```
2.   Add the highlighted property to the `package.json` file and save the file changes:

```
{
  "name": "SignalRWebPack",
  "version": "1.0.0",
  "private": true,
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

Setting the `private` property to `true` prevents package installation warnings in the next step.

3.   Install the required npm packages. Run the following command from the project root:

```
npm i -D -E clean-webpack-plugin@3.0.0 css-loader@3.4.2 html-webpack-plugin@3.2.0 mini-css-extract-plugin@0.9.0 ts-loader@6.2.1 typescript@3.7.5 webpack@4.41.5 webpack-cli@3.3.10
```

Some command details to note:

    *   A version number follows the `@` sign for each package name. npm installs those specific package versions.
    *   The `-E` option disables npm's default behavior of writing [semantic versioning](https://semver.org/) range operators to *package`json`. For example, `"webpack": "4.41.5"` is used instead of `"webpack": "^4.41.5"`. This option prevents unintended upgrades to newer package versions.

See the [npm-install](https://docs.npmjs.com/cli/install) docs for more detail.

4.   Replace the `scripts` property of the `package.json` file with the following code:

```
"scripts": {
  "build": "webpack --mode=development --watch",
  "release": "webpack --mode=production",
  "publish": "npm run release && dotnet publish -c Release"
},
```

Some explanation of the scripts:

    *   `build`: Bundles the client-side resources in development mode and watches for file changes. The file watcher causes the bundle to regenerate each time a project file changes. The `mode` option disables production optimizations, such as tree shaking and minification. Only use `build` in development.
    *   `release`: Bundles the client-side resources in production mode.
    *   `publish`: Runs the `release` script to bundle the client-side resources in production mode. It calls the .NET CLI's [publish](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-publish) command to publish the app.

5.   Create a file named `webpack.config.js`, in the project root, with the following code:

```
const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
module.exports = {
    entry: "./src/index.ts",
    output: {
        path: path.resolve(__dirname, "wwwroot"),
        filename: "[name].[chunkhash].js",
        publicPath: "/"
    },
    resolve: {
        extensions: [".js", ".ts"]
    },
    module: {
        rules: [
            {
                test: /\.ts$/,
                use: "ts-loader"
            },
            {
                test: /\.css$/,
                use: [MiniCssExtractPlugin.loader, "css-loader"]
            }
        ]
    },
    plugins: [
        new CleanWebpackPlugin(),
        new HtmlWebpackPlugin({
            template: "./src/index.html"
        }),
        new MiniCssExtractPlugin({
            filename: "css/[name].[chunkhash].css"
        })
    ]
};
```

The preceding file configures the Webpack compilation. Some configuration details to note:

    *   The `output` property overrides the default value of `dist`. The bundle is instead emitted in the `wwwroot` directory.
    *   The `resolve.extensions` array includes `.js` to import the SignalR client JavaScript.

6.   Create a new _src_ directory in the project root to store the project's client-side assets.

7.   Create `src/index.html` with the following markup.

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>ASP.NET Core SignalR</title>
</head>
<body>
    <div id="divMessages" class="messages">
    </div>
    <div class="input-zone">
        <label id="lblMessage" for="tbMessage">Message:</label>
        <input id="tbMessage" class="input-zone-input" type="text" />
        <button id="btnSend">Send</button>
    </div>
</body>
</html>
```

The preceding HTML defines the homepage's boilerplate markup.

8.   Create a new _src/css_ directory. Its purpose is to store the project's `.css` files.

9.   Create `src/css/main.css` with the following CSS:

```
*, *::before, *::after {
    box-sizing: border-box;
}

html, body {
    margin: 0;
    padding: 0;
}

.input-zone {
    align-items: center;
    display: flex;
    flex-direction: row;
    margin: 10px;
}

.input-zone-input {
    flex: 1;
    margin-right: 10px;
}

.message-author {
    font-weight: bold;
}

.messages {
    border: 1px solid #000;
    margin: 10px;
    max-height: 300px;
    min-height: 300px;
    overflow-y: auto;
    padding: 5px;
}
```

The preceding `main.css` file styles the app.

10.   Create `src/tsconfig.json` with the following JSON:

```
{
  "compilerOptions": {
    "target": "es5"
  }
}
```

The preceding code configures the TypeScript compiler to produce [ECMAScript](https://wikipedia.org/wiki/ECMAScript) 5-compatible JavaScript.

11.   Create `src/index.ts` with the following code:

```
import "./css/main.css";

const divMessages: HTMLDivElement = document.querySelector("#divMessages");
const tbMessage: HTMLInputElement = document.querySelector("#tbMessage");
const btnSend: HTMLButtonElement = document.querySelector("#btnSend");
const username = new Date().getTime();

tbMessage.addEventListener("keyup", (e: KeyboardEvent) => {
    if (e.key === "Enter") {
        send();
    }
});

btnSend.addEventListener("click", send);

function send() {
}
```

The preceding TypeScript retrieves references to DOM elements and attaches two event handlers:

    *   `keyup`: This event fires when the user types in the `tbMessage`textbox. The `send` function is called when the user presses the **Enter** key.
    *   `click`: This event fires when the user selects the **Send** button. The `send` function is called.

1.   In `Startup.Configure`, add calls to [UseDefaultFiles(IApplicationBuilder)](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.defaultfilesextensions.usedefaultfiles#microsoft-aspnetcore-builder-defaultfilesextensions-usedefaultfiles(microsoft-aspnetcore-builder-iapplicationbuilder)) and [UseStaticFiles(IApplicationBuilder)](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.staticfileextensions.usestaticfiles#microsoft-aspnetcore-builder-staticfileextensions-usestaticfiles(microsoft-aspnetcore-builder-iapplicationbuilder)).

```
public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
    }
    
    app.UseRouting();
    app.UseDefaultFiles();
    app.UseStaticFiles();
    
    app.UseEndpoints(endpoints =>
    {
        endpoints.MapHub<ChatHub>("/hub");
    });
        
}
```

The preceding code allows the server to locate and serve the `index.html` file. The file is served whether the user enters its full URL or the root URL of the web app.

2.   At the end of `Startup.Configure`, map a _/hub_ route to the `ChatHub` hub. Replace the code that displays _Hello World!_ with the following line:

```
app.UseEndpoints(endpoints =>
{
    endpoints.MapHub<ChatHub>("/hub");
});
```
3.   In `Startup.ConfigureServices`, call [AddSignalR](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.signalrdependencyinjectionextensions.addsignalr).

```
services.AddSignalR();
```
4.   Create a new directory named _Hubs_ in the project root _SignalRWebPack/_ to store the SignalR hub.

5.   Create hub `Hubs/ChatHub.cs` with the following code:

```
using Microsoft.AspNetCore.SignalR;
using System.Threading.Tasks;

namespace SignalRWebPack.Hubs
{
    public class ChatHub : Hub
    {
    }
}
```
6.   Add the following `using` statement at the top of the `Startup.cs` file to resolve the `ChatHub` reference:

```
using SignalRWebPack.Hubs;
```

The app currently displays a basic form to send messages, but isn't yet functional. The server is listening to a specific route but does nothing with sent messages.

1.   Run the following command at the project root:

```
npm i @microsoft/signalr @types/node
```

The preceding command installs:

    *   The [SignalR TypeScript client](https://www.npmjs.com/package/@microsoft/signalr), which allows the client to send messages to the server.
    *   The TypeScript type definitions for Node.js, which enables compile-time checking of Node.js types.

2.   Add the highlighted code to the `src/index.ts` file:

```
import "./css/main.css";
import * as signalR from "@microsoft/signalr";

const divMessages: HTMLDivElement = document.querySelector("#divMessages");
const tbMessage: HTMLInputElement = document.querySelector("#tbMessage");
const btnSend: HTMLButtonElement = document.querySelector("#btnSend");
const username = new Date().getTime();

const connection = new signalR.HubConnectionBuilder()
    .withUrl("/hub")
    .build();

connection.on("messageReceived", (username: string, message: string) => {
    let m = document.createElement("div");

    const author = document.createElement("div");
    author.className = "message-author";
    author.textContent = username;

    const content = document.createElement("div");
    content.textContent = message;

    m.append(author, content);

    divMessages.appendChild(m);
    divMessages.scrollTop = divMessages.scrollHeight;
});

connection.start().catch(err => document.write(err));

tbMessage.addEventListener("keyup", (e: KeyboardEvent) => {
    if (e.key === "Enter") {
        send();
    }
});

btnSend.addEventListener("click", send);

function send() {
}
```

The preceding code supports receiving messages from the server. The `HubConnectionBuilder` class creates a new builder for configuring the server connection. The `withUrl` function configures the hub URL.

SignalR enables the exchange of messages between a client and a server. Each message has a specific name. For example, messages with the name `messageReceived` can run the logic responsible for displaying the new message in the messages zone. Listening to a specific message can be done via the `on` function. Any number of message names can be listened to. It's also possible to pass parameters to the message, such as the author's name and the content of the message received. Once the client receives a message, a new `div` element is created with the author's name and message content appended as child elements using `textContent`. It's added to the main `div` element displaying the messages.

3.   Now that the client can receive a message, configure it to send messages. Add the highlighted code to the `src/index.ts` file:

```
import "./css/main.css";
import * as signalR from "@microsoft/signalr";

const divMessages: HTMLDivElement = document.querySelector("#divMessages");
const tbMessage: HTMLInputElement = document.querySelector("#tbMessage");
const btnSend: HTMLButtonElement = document.querySelector("#btnSend");
const username = new Date().getTime();

const connection = new signalR.HubConnectionBuilder()
    .withUrl("/hub")
    .build();

connection.on("messageReceived", (username: string, message: string) => {
    let messages = document.createElement("div");

    const author = document.createElement("div");
    author.className = "message-author";
    author.textContent = username;

    const content = document.createElement("div");
    content.textContent = message;

    messages.append(author, content);

    divMessages.appendChild(messages);
    divMessages.scrollTop = divMessages.scrollHeight;
});

connection.start().catch(err => document.write(err));

tbMessage.addEventListener("keyup", (e: KeyboardEvent) => {
    if (e.key === "Enter") {
        send();
    }
});

btnSend.addEventListener("click", send);

function send() {
    connection.send("newMessage", username, tbMessage.value)
        .then(() => tbMessage.value = "");
}
```

Sending a message through the WebSockets connection requires calling the `send` method. The method's first parameter is the message name. The message data inhabits the other parameters. In this example, a message identified as `newMessage` is sent to the server. The message consists of the username and the user input from a text box. If the send works, the text box value is cleared.

4.   Add the `NewMessage` method to the `ChatHub` class:

```
using Microsoft.AspNetCore.SignalR;
using System.Threading.Tasks;

namespace SignalRWebPack.Hubs
{
    public class ChatHub : Hub
    {
        public async Task NewMessage(long username, string message)
        {
            await Clients.All.SendAsync("messageReceived", username, message);
        }
    }
}
```

The preceding code broadcasts received messages to all connected users once the server receives them. It's unnecessary to have a generic `on` method to receive all the messages. A method named after the message name suffices.

In this example, the TypeScript client sends a message identified as `newMessage`. The C# `NewMessage` method expects the data sent by the client. A call is made to [SendAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.signalr.clientproxyextensions.sendasync) on [Clients.All](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.signalr.ihubclients-1.all#microsoft-aspnetcore-signalr-ihubclients-1-all). The received messages are sent to all clients connected to the hub.

Confirm that the app works with the following steps.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)

1.   Run Webpack in _release_ mode. Using the **Package Manager Console** window, run the following command in the project root. If you aren't in the project root, enter `cd SignalRWebPack` before entering the command.

```
npm run release
```

This command generates the client-side assets to be served when running the app. The assets are placed in the `wwwroot` folder.

Webpack completed the following tasks:

    *   Purged the contents of the `wwwroot` directory.
    *   Converted the TypeScript to JavaScript in a process known as _transpilation_.
    *   Mangled the generated JavaScript to reduce file size in a process known as _minification_.
    *   Copied the processed JavaScript, CSS, and HTML files from `src` to the `wwwroot` directory.
    *   Injected the following elements into the `wwwroot/index.html` file: 
        *   A `<link>` tag, referencing the `wwwroot/main.<hash>.css` file. This tag is placed immediately before the closing `</head>` tag.
        *   A `<script>` tag, referencing the minified `wwwroot/main.<hash>.js` file. This tag is placed immediately after the closing `</title>` tag.

2.   Select **Debug**>**Start without debugging** to launch the app in a browser without attaching the debugger. The `wwwroot/index.html` file is served at `http://localhost:<port_number>`.

If you get compile errors, try closing and reopening the solution.

3.   Open another browser instance (any browser). Paste the URL in the address bar.

4.   Choose either browser, type something in the **Message** text box, and select the **Send** button. The unique user name and message are displayed on both pages instantly.

![Image 13: Message displayed in both browser windows](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack/_static/browsers-message-broadcast.png?view=aspnetcore-10.0)

*   [ASP.NET Core SignalR JavaScript client](https://learn.microsoft.com/en-us/aspnet/core/signalr/javascript-client?view=aspnetcore-10.0)
*   [Use hubs in ASP.NET Core SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0)

This tutorial demonstrates using [Webpack](https://webpack.js.org/) in an ASP.NET Core SignalR web app to bundle and build a client written in [TypeScript](https://www.typescriptlang.org/). Webpack enables developers to bundle and build the client-side resources of a web app.

In this tutorial, you learn how to:

*   Scaffold a starter ASP.NET Core SignalR app
*   Configure the SignalR TypeScript client
*   Configure a build pipeline using Webpack
*   Configure the SignalR server
*   Enable communication between client and server

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/signalr-typescript-webpack/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_4_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_4_visual-studio-code)

*   [Visual Studio 2019](https://visualstudio.microsoft.com/downloads/?utm_medium=microsoft&utm_source=learn.microsoft.com&utm_campaign=inline+link&utm_content=download+vs2019) with the **ASP.NET and web development** workload
*   [.NET Core SDK 2.2 or later](https://dotnet.microsoft.com/download/dotnet-core)
*   [Node.js](https://nodejs.org/) with [npm](https://www.npmjs.com/)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_5_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_5_visual-studio-code)

Configure Visual Studio to look for npm in the _PATH_ environment variable. By default, Visual Studio uses the version of npm found in its installation directory. Follow these instructions in Visual Studio:

1.   Navigate to **Tools**>**Options**>**Projects and Solutions**>**Web Package Management**>**External Web Tools**.

2.   Select the _$(PATH)_ entry from the list. Select the up arrow to move the entry to the second position in the list.

![Image 14: Visual Studio Configuration](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack/_static/signalr-configure-path-visual-studio.png?view=aspnetcore-10.0)

Visual Studio configuration is completed. It's time to create the project.

1.   Use the **File**>**New**>**Project** menu option and choose the **ASP.NET Core Web Application** template.
2.   Name the project *SignalRWebPack`, and select **Create**.
3.   Select _.NET Core_ from the target framework drop-down, and select _ASP.NET Core 2.2_ from the framework selector drop-down. Select the **Empty** template, and select **Create**.

The following steps configure the conversion of TypeScript to JavaScript and the bundling of client-side resources.

1.   Run the following command in the project root to create a `package.json` file:

```
npm init -y
```
2.   Add the highlighted property to the `package.json` file:

```
{
  "name": "SignalRWebPack",
  "version": "1.0.0",
  "private": true,
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

Setting the `private` property to `true` prevents package installation warnings in the next step.

3.   Install the required npm packages. Run the following command from the project root:

```
npm install -D -E clean-webpack-plugin@1.0.1 css-loader@2.1.0 html-webpack-plugin@4.0.0-beta.5 mini-css-extract-plugin@0.5.0 ts-loader@5.3.3 typescript@3.3.3 webpack@4.29.3 webpack-cli@3.2.3
```

Some command details to note:

    *   A version number follows the `@` sign for each package name. npm installs those specific package versions.
    *   The `-E` option disables npm's default behavior of writing [semantic versioning](https://semver.org/) range operators to *package`json`. For example, `"webpack": "4.29.3"` is used instead of `"webpack": "^4.29.3"`. This option prevents unintended upgrades to newer package versions.

See the [npm-install](https://docs.npmjs.com/cli/install) docs for more detail.

4.   Replace the `scripts` property of the `package.json` file with the following code:

```
"scripts": {
  "build": "webpack --mode=development --watch",
  "release": "webpack --mode=production",
  "publish": "npm run release && dotnet publish -c Release"
},
```

Some explanation of the scripts:

    *   `build`: Bundles the client-side resources in development mode and watches for file changes. The file watcher causes the bundle to regenerate each time a project file changes. The `mode` option disables production optimizations, such as tree shaking and minification. Only use `build` in development.
    *   `release`: Bundles the client-side resources in production mode.
    *   `publish`: Runs the `release` script to bundle the client-side resources in production mode. It calls the .NET CLI's [publish](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-publish) command to publish the app.

5.   Create a file named`*webpack.config.js` in the project root, with the following code:

```
const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const CleanWebpackPlugin = require("clean-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    entry: "./src/index.ts",
    output: {
        path: path.resolve(__dirname, "wwwroot"),
        filename: "[name].[chunkhash].js",
        publicPath: "/"
    },
    resolve: {
        extensions: [".js", ".ts"]
    },
    module: {
        rules: [
            {
                test: /\.ts$/,
                use: "ts-loader"
            },
            {
                test: /\.css$/,
                use: [MiniCssExtractPlugin.loader, "css-loader"]
            }
        ]
    },
    plugins: [
        new CleanWebpackPlugin(["wwwroot/*"]),
        new HtmlWebpackPlugin({
            template: "./src/index.html"
        }),
        new MiniCssExtractPlugin({
            filename: "css/[name].[chunkhash].css"
        })
    ]
};
```

The preceding file configures the Webpack compilation. Some configuration details to note:

    *   The `output` property overrides the default value of `dist`. The bundle is instead emitted in the `wwwroot` directory.
    *   The `resolve.extensions` array includes `.js` to import the SignalR client JavaScript.

6.   Create a new _src_ directory in the project root to store the project's client-side assets.

7.   Create `src/index.html` with the following markup.

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>ASP.NET Core SignalR</title>
</head>
<body>
    <div id="divMessages" class="messages">
    </div>
    <div class="input-zone">
        <label id="lblMessage" for="tbMessage">Message:</label>
        <input id="tbMessage" class="input-zone-input" type="text" />
        <button id="btnSend">Send</button>
    </div>
</body>
</html>
```

The preceding HTML defines the homepage's boilerplate markup.

8.   Create a new _src/css_ directory. Its purpose is to store the project's `.css` files.

9.   Create `src/css/main.css` with the following markup:

```
*, *::before, *::after {
    box-sizing: border-box;
}

html, body {
    margin: 0;
    padding: 0;
}

.input-zone {
    align-items: center;
    display: flex;
    flex-direction: row;
    margin: 10px;
}

.input-zone-input {
    flex: 1;
    margin-right: 10px;
}

.message-author {
    font-weight: bold;
}

.messages {
    border: 1px solid #000;
    margin: 10px;
    max-height: 300px;
    min-height: 300px;
    overflow-y: auto;
    padding: 5px;
}
```

The preceding `main.css` file styles the app.

10.   Create `src/tsconfig.json` with the following JSON:

```
{
  "compilerOptions": {
    "target": "es5"
  }
}
```

The preceding code configures the TypeScript compiler to produce [ECMAScript](https://wikipedia.org/wiki/ECMAScript) 5-compatible JavaScript.

11.   Create `src/index.ts` with the following code:

```
import "./css/main.css";

const divMessages: HTMLDivElement = document.querySelector("#divMessages");
const tbMessage: HTMLInputElement = document.querySelector("#tbMessage");
const btnSend: HTMLButtonElement = document.querySelector("#btnSend");
const username = new Date().getTime();

tbMessage.addEventListener("keyup", (e: KeyboardEvent) => {
    if (e.keyCode === 13) {
        send();
    }
});

btnSend.addEventListener("click", send);

function send() {
}
```

The preceding TypeScript retrieves references to DOM elements and attaches two event handlers:

    *   `keyup`: This event fires when the user types in the `tbMessage` textbox. The `send` function is called when the user presses the **Enter** key.
    *   `click`: This event fires when the user selects the **Send** button. The `send` function is called.

1.   The code provided in the `Startup.Configure` method displays _Hello World!_. Replace the `app.Run` method call with calls to [UseDefaultFiles(IApplicationBuilder)](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.defaultfilesextensions.usedefaultfiles#microsoft-aspnetcore-builder-defaultfilesextensions-usedefaultfiles(microsoft-aspnetcore-builder-iapplicationbuilder)) and [UseStaticFiles(IApplicationBuilder)](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.staticfileextensions.usestaticfiles#microsoft-aspnetcore-builder-staticfileextensions-usestaticfiles(microsoft-aspnetcore-builder-iapplicationbuilder)).

```
app.UseDefaultFiles();
app.UseStaticFiles();
```

The preceding code allows the server to locate and serve the `index.html` file, whether the user enters its full URL or the root URL of the web app.

2.   Call [AddSignalR](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.signalrdependencyinjectionextensions.addsignalr) in `Startup.ConfigureServices`. It adds the SignalR services to the project.

```
services.AddSignalR();
```
3.   Map a _/hub_ route to the `ChatHub` hub. Add the following lines at the end of `Startup.Configure`:

```
app.UseSignalR(options =>
{
    options.MapHub<ChatHub>("/hub");
});
```
4.   Create a new directory, called _Hubs_, in the project root. Its purpose is to store the SignalR hub, which is created in the next step.

5.   Create hub `Hubs/ChatHub.cs` with the following code:

```
using Microsoft.AspNetCore.SignalR;
using System.Threading.Tasks;

namespace SignalRWebPack.Hubs
{
    public class ChatHub : Hub
    {
    }
}
```
6.   Add the following code at the top of the `Startup.cs` file to resolve the `ChatHub` reference:

```
using SignalRWebPack.Hubs;
```

The app currently displays a simple form to send messages. Nothing happens when you try to do so. The server is listening to a specific route but does nothing with sent messages.

1.   Run the following command at the project root:

```
npm install @aspnet/signalr
```

The preceding command installs the [SignalR TypeScript client](https://www.npmjs.com/package/@microsoft/signalr), which allows the client to send messages to the server.

2.   Add the highlighted code to the `src/index.ts` file:

```
import "./css/main.css";
import * as signalR from "@aspnet/signalr";

const divMessages: HTMLDivElement = document.querySelector("#divMessages");
const tbMessage: HTMLInputElement = document.querySelector("#tbMessage");
const btnSend: HTMLButtonElement = document.querySelector("#btnSend");
const username = new Date().getTime();

const connection = new signalR.HubConnectionBuilder()
    .withUrl("/hub")
    .build();

connection.on("messageReceived", (username: string, message: string) => {
    let m = document.createElement("div");

    const author = document.createElement("div");
    author.className = "message-author";
    author.textContent = username;

    const content = document.createElement("div");
    content.textContent = message;

    m.append(author, content);

    divMessages.appendChild(m);
    divMessages.scrollTop = divMessages.scrollHeight;
});

connection.start().catch(err => document.write(err));

tbMessage.addEventListener("keyup", (e: KeyboardEvent) => {
    if (e.keyCode === 13) {
        send();
    }
});

btnSend.addEventListener("click", send);

function send() {
}
```

The preceding code supports receiving messages from the server. The `HubConnectionBuilder` class creates a new builder for configuring the server connection. The `withUrl` function configures the hub URL.

SignalR enables the exchange of messages between a client and a server. Each message has a specific name. For example, messages with the name `messageReceived` can run the logic responsible for displaying the new message in the messages zone. Listening to a specific message can be done via the `on` function. You can listen to any number of message names. It's also possible to pass parameters to the message, such as the author's name and the content of the message received. Once the client receives a message, a new `div` element is created with the author's name and message content appended as child elements using `textContent`. The new message is added to the main `div` element displaying the messages.

3.   Now that the client can receive a message, configure it to send messages. Add the highlighted code to the `src/index.ts` file:

```
import "./css/main.css";
import * as signalR from "@aspnet/signalr";

const divMessages: HTMLDivElement = document.querySelector("#divMessages");
const tbMessage: HTMLInputElement = document.querySelector("#tbMessage");
const btnSend: HTMLButtonElement = document.querySelector("#btnSend");
const username = new Date().getTime();

const connection = new signalR.HubConnectionBuilder()
    .withUrl("/hub")
    .build();

connection.on("messageReceived", (username: string, message: string) => {
    let messageContainer = document.createElement("div");

    const author = document.createElement("div");
    author.className = "message-author";
    author.textContent = username;

    const content = document.createElement("div");
    content.textContent = message;

    messageContainer.append(author, content);

    divMessages.appendChild(messageContainer);
    divMessages.scrollTop = divMessages.scrollHeight;
});

connection.start().catch(err => document.write(err));

tbMessage.addEventListener("keyup", (e: KeyboardEvent) => {
    if (e.keyCode === 13) {
        send();
    }
});

btnSend.addEventListener("click", send);

function send() {
    connection.send("newMessage", username, tbMessage.value)
              .then(() => tbMessage.value = "");
}
```

Sending a message through the WebSockets connection requires calling the `send` method. The method's first parameter is the message name. The message data inhabits the other parameters. In this example, a message identified as `newMessage` is sent to the server. The message consists of the username and the user input from a text box. If the send works, the text box value is cleared.

4.   Add the `NewMessage` method to the `ChatHub` class:

```
using Microsoft.AspNetCore.SignalR;
using System.Threading.Tasks;

namespace SignalRWebPack.Hubs
{
    public class ChatHub : Hub
    {
        public async Task NewMessage(long username, string message)
        {
            await Clients.All.SendAsync("messageReceived", username, message);
        }
    }
}
```

The preceding code broadcasts received messages to all connected users once the server receives them. It's unnecessary to have a generic `on` method to receive all the messages. A method named after the message name suffices.

In this example, the TypeScript client sends a message identified as `newMessage`. The C# `NewMessage` method expects the data sent by the client. A call is made to [SendAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.signalr.clientproxyextensions.sendasync) on [Clients.All](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.signalr.ihubclients-1.all#microsoft-aspnetcore-signalr-ihubclients-1-all). The received messages are sent to all clients connected to the hub.

Confirm that the app works with the following steps.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_6_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack?view=aspnetcore-10.0#tabpanel_6_visual-studio-code)

1.   Run Webpack in _release_ mode. Using the **Package Manager Console** window, run the following command in the project root. If you aren't in the project root, enter `cd SignalRWebPack` before entering the command.

```
npm run release
```

This command generates the client-side assets to be served when running the app. The assets are placed in the `wwwroot` folder.

Webpack completed the following tasks:

    *   Purged the contents of the `wwwroot` directory.
    *   Converted the TypeScript to JavaScript in a process known as _transpilation_.
    *   Mangled the generated JavaScript to reduce file size in a process known as _minification_.
    *   Copied the processed JavaScript, CSS, and HTML files from `src` to the `wwwroot` directory.
    *   Injected the following elements into the `wwwroot/index.html` file: 
        *   A `<link>` tag, referencing the `wwwroot/main.<hash>.css` file. This tag is placed immediately before the closing `</head>` tag.
        *   A `<script>` tag, referencing the minified `wwwroot/main.<hash>.js` file. This tag is placed immediately after the closing `</title>` tag.

2.   Select **Debug**>**Start without debugging** to launch the app in a browser without attaching the debugger. The `wwwroot/index.html` file is served at `http://localhost:<port_number>`.

3.   Open another browser instance (any browser). Paste the URL in the address bar.

4.   Choose either browser, type something in the **Message** text box, and select the **Send** button. The unique user name and message are displayed on both pages instantly.

![Image 15: Message displayed in both browser windows](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr-typescript-webpack/_static/browsers-message-broadcast.png?view=aspnetcore-10.0)

*   [ASP.NET Core SignalR JavaScript client](https://learn.microsoft.com/en-us/aspnet/core/signalr/javascript-client?view=aspnetcore-10.0)
*   [Use hubs in ASP.NET Core SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0)
