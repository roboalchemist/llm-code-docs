# Source: https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0

Title: Get started with ASP.NET Core SignalR

URL Source: https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0

Markdown Content:
This tutorial teaches the basics of building a real-time app using SignalR. You learn how to:

*   Create a web project.
*   Add the SignalR client library.
*   Create a SignalR hub.
*   Configure the project to use SignalR.
*   Add code that sends messages from any client to all connected clients.

At the end, you'll have a working chat app:

![Image 1: Completed SignalR sample app.](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/media/signalr-chat-app.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   [The latest version of Visual Studio](https://visualstudio.microsoft.com/downloads/) with the **ASP.NET and web development** workload.

[![Image 2: VS26 installer workloads](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev-2026.png?view=aspnetcore-10.0)](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev-2026.png?view=aspnetcore-10.0#lightbox)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)

Start the latest version of Visual Studio and select **Create a new project**.

![Image 3: Create a new project from the start window.](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/media/start-window-create-new-project.png?view=aspnetcore-10.0)

In the **Create a new project** dialog, select **ASP.NET Core Web App (Razor Pages)**, and then select **Next**.

![Image 4: Create an ASP.NET Core Web App.](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/media/new-aspnet-core-web-app.png?view=aspnetcore-10.0)

In the **Configure your new project** dialog, enter `SignalRChat` for **Project name**. It's important to name the project `SignalRChat`, including matching the capitalization, so the namespaces match the code in the tutorial.

Select **Next**.

In the **Additional information** dialog, select **.NET 10.0 (Long Term Support)** and then select **Create**.

![Image 5: Additional information.](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/media/additional-information.png?view=aspnetcore-10.0)

The SignalR server library is included in the ASP.NET Core shared framework. The JavaScript client library isn't automatically included in the project. For this tutorial, use Library Manager (LibMan) to get the client library from [unpkg](https://unpkg.com/). `unpkg`is a fast, global content delivery network for everything on [npm](https://www.npmjs.com/).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)

In **Solution Explorer**, right-click the project, and select **Add**>**Client-Side Library**.

In the **Add Client-Side Library** dialog:

*   Select **unpkg** for **Provider**
*   Enter `@microsoft/signalr@latest` for **Library**.
*   Select **Choose specific files**, expand the _dist/browser_ folder, and select `signalr.js` and `signalr.min.js`.
*   Set **Target Location** to `wwwroot/js/signalr/`.
*   Select **Install**.

![Image 6: Add Client-Side Library dialog - select library.](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/media/add-client-side-library.png?view=aspnetcore-10.0)

LibMan creates a `wwwroot/js/signalr` folder and copies the selected files to it. A `libman.json` file is created with the following code:

```
{
  "version": "3.0",
  "defaultProvider": "unpkg",
  "libraries": [
    {
      "library": "@microsoft/signalr@latest",
      "destination": "wwwroot/lib/microsoft/signalr/",
      "files": [
        "dist/browser/signalr.js",
        "dist/browser/signalr.min.js"
      ]
    }
  ]
}
```

A _hub_ is a class that serves as a high-level pipeline that handles client-server communication.

In the SignalRChat project folder, create a `Hubs` folder.

In the `Hubs` folder, create the `ChatHub` class with the following code:

```
using Microsoft.AspNetCore.SignalR;

namespace SignalRChat.Hubs
{
    public class ChatHub : Hub
    {
        public async Task SendMessage(string user, string message)
        {
            await Clients.All.SendAsync("ReceiveMessage", user, message);
        }
    }
}
```

The `ChatHub` class inherits from the SignalR [Hub](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.signalr.hub) class. The `Hub` class manages connections, groups, and messaging.

The `SendMessage` method can be called by a connected client to send a message to all clients. JavaScript client code that calls the method is shown later in the tutorial. SignalR code is asynchronous to provide maximum scalability.

The SignalR server must be configured to pass SignalR requests to SignalR. Add the following highlighted code to the `Program.cs` file.

```
using SignalRChat.Hubs;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorPages();
builder.Services.AddSignalR();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();

app.UseRouting();

app.UseAuthorization();

app.MapStaticAssets();
app.MapHub<ChatHub>("/chatHub");
app.MapRazorPages()
   .WithStaticAssets();

app.Run();
```

The preceding highlighted code adds SignalR to the ASP.NET Core dependency injection and routing systems.

Replace the content in `Pages/Index.cshtml` with the following code:

```
@page
<div class="container">
    <div class="row p-1">
        <div class="col-1">User</div>
        <div class="col-5"><input type="text" id="userInput" /></div>
    </div>
    <div class="row p-1">
        <div class="col-1">Message</div>
        <div class="col-5"><input type="text" class="w-100" id="messageInput" /></div>
    </div>
    <div class="row p-1">
        <div class="col-6 text-end">
            <input type="button" id="sendButton" value="Send Message" />
        </div>
    </div>
    <div class="row p-1">
        <div class="col-6">
            <hr />
        </div>
    </div>
    <div class="row p-1">
        <div class="col-6">
            <ul id="messagesList"></ul>
        </div>
    </div>
</div>
<script src="~/lib/microsoft/signalr/dist/browser/signalr.js"></script>
<script src="~/js/chat.js"></script>
```

The preceding markup:

*   Creates text boxes and a submit button.
*   Creates a list with `id="messagesList"` for displaying messages that are received from the SignalR hub.
*   Includes script references to SignalR and the `chat.js` app code is created in the next step.

In the `wwwroot/js` folder, create a `chat.js` file with the following code:

```
"use strict";

var connection = new signalR.HubConnectionBuilder().withUrl("/chatHub").build();

//Disable the send button until connection is established.
document.getElementById("sendButton").disabled = true;

connection.on("ReceiveMessage", function (user, message) {
    var li = document.createElement("li");
    document.getElementById("messagesList").appendChild(li);
    // We can assign user-supplied strings to an element's textContent because it
    // is not interpreted as markup. If you're assigning in any other way, you 
    // should be aware of possible script injection concerns.
    li.textContent = `${user} says ${message}`;
});

connection.start().then(function () {
    document.getElementById("sendButton").disabled = false;
}).catch(function (err) {
    return console.error(err.toString());
});

document.getElementById("sendButton").addEventListener("click", function (event) {
    var user = document.getElementById("userInput").value;
    var message = document.getElementById("messageInput").value;
    connection.invoke("SendMessage", user, message).catch(function (err) {
        return console.error(err.toString());
    });
    event.preventDefault();
});
```

The preceding JavaScript:

*   Creates and starts a connection.
*   Adds to the submit button a handler that sends messages to the hub.
*   Adds to the connection object a handler that receives messages from the hub and adds them to the list.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_4_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_4_visual-studio-code)

Select Ctrl+F5 to run the app without debugging.

Copy the URL from the address bar, open another browser instance or tab, and paste the URL in the address bar.

Choose either browser, enter a name and message, and select the **Send Message** button.

The name and message are displayed on both pages instantly.

![Image 7: Completed SignalR sample app.](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/media/signalr-chat-app.png?view=aspnetcore-10.0)

Tip

If the app doesn't work, open the browser developer tools (F12) and go to the console. Look for possible errors related to HTML and JavaScript code. For example, if `signalr.js` was put in a different folder than directed, the reference to that file won't work resulting in a 404 error in the console. ![Image 8: signalr.js not found error](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/7.x/f12-console.png?view=aspnetcore-10.0) If an `ERR_SPDY_INADEQUATE_TRANSPORT_SECURITY` error has occurred in Chrome, run the following commands to update the development certificate:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

For information on deploying to Azure, see [Quickstart: Deploy an ASP.NET web app](https://learn.microsoft.com/en-us/azure/app-service/quickstart-dotnetcore). For more information on Azure SignalR Service, see [What is Azure SignalR Service?](https://learn.microsoft.com/en-us/azure/azure-signalr/signalr-overview).

*   [Use hubs](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0)
*   [Strongly typed hubs](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0#strongly-typed-hubs)
*   [Authentication and authorization in ASP.NET Core SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/authn-and-authz?view=aspnetcore-10.0)
*   [View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/signalr/javascript-client/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

This tutorial teaches the basics of building a real-time app using SignalR. You learn how to:

*   Create a web project.
*   Add the SignalR client library.
*   Create a SignalR hub.
*   Configure the project to use SignalR.
*   Add code that sends messages from any client to all connected clients.

At the end, you'll have a working chat app:

![Image 9: Completed SignalR sample app](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/7.x/signalr-get-started-finished.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) with the **ASP.NET and web development** workload.

![Image 10: VS22 installer workloads](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)

Start Visual Studio 2022 and select **Create a new project**.

![Image 11: Create a new project from the start window](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/8.x/start-window-create-new-project-vs17.8.0.png?view=aspnetcore-10.0)

In the **Create a new project** dialog, select **ASP.NET Core Web App (Razor Pages)**, and then select **Next**.

![Image 12: Create an ASP.NET Core Web App](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/8.x/new-project-select-vs17.9.0.png?view=aspnetcore-10.0)

In the **Configure your new project** dialog, enter `SignalRChat` for **Project name**. It's important to name the project `SignalRChat`, including matching the capitalization, so the namespaces match the code in the tutorial.

Select **Next**.

In the **Additional information** dialog, select **.NET 8.0 (Long Term Support)** and then select **Create**.

![Image 13: Additional information](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/8.x/additional-info-vs17.9.0.png?view=aspnetcore-10.0)

The SignalR server library is included in the ASP.NET Core shared framework. The JavaScript client library isn't automatically included in the project. For this tutorial, use Library Manager (LibMan) to get the client library from [unpkg](https://unpkg.com/). `unpkg`is a fast, global content delivery network for everything on [npm](https://www.npmjs.com/).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)

In **Solution Explorer**, right-click the project, and select **Add**>**Client-Side Library**.

In the **Add Client-Side Library** dialog:

*   Select **unpkg** for **Provider**
*   Enter `@microsoft/signalr@latest` for **Library**.
*   Select **Choose specific files**, expand the _dist/browser_ folder, and select `signalr.js` and `signalr.min.js`.
*   Set **Target Location** to `wwwroot/js/signalr/`.
*   Select **Install**.

![Image 14: Add Client-Side Library dialog - select library](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/8.x/find-signalr-client-libs-select-files-vs17.8.0.png?view=aspnetcore-10.0)

LibMan creates a `wwwroot/js/signalr` folder and copies the selected files to it.

A _hub_ is a class that serves as a high-level pipeline that handles client-server communication.

In the SignalRChat project folder, create a `Hubs` folder.

In the `Hubs` folder, create the `ChatHub` class with the following code:

```
using Microsoft.AspNetCore.SignalR;

namespace SignalRChat.Hubs
{
    public class ChatHub : Hub
    {
        public async Task SendMessage(string user, string message)
        {
            await Clients.All.SendAsync("ReceiveMessage", user, message);
        }
    }
}
```

The `ChatHub` class inherits from the SignalR [Hub](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.signalr.hub) class. The `Hub` class manages connections, groups, and messaging.

The `SendMessage` method can be called by a connected client to send a message to all clients. JavaScript client code that calls the method is shown later in the tutorial. SignalR code is asynchronous to provide maximum scalability.

The SignalR server must be configured to pass SignalR requests to SignalR. Add the following highlighted code to the `Program.cs` file.

```
using SignalRChat.Hubs;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorPages();
builder.Services.AddSignalR();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();
app.MapHub<ChatHub>("/chatHub");

app.Run();
```

The preceding highlighted code adds SignalR to the ASP.NET Core dependency injection and routing systems.

Replace the content in `Pages/Index.cshtml` with the following code:

```
@page
<div class="container">
    <div class="row p-1">
        <div class="col-1">User</div>
        <div class="col-5"><input type="text" id="userInput" /></div>
    </div>
    <div class="row p-1">
        <div class="col-1">Message</div>
        <div class="col-5"><input type="text" class="w-100" id="messageInput" /></div>
    </div>
    <div class="row p-1">
        <div class="col-6 text-end">
            <input type="button" id="sendButton" value="Send Message" />
        </div>
    </div>
    <div class="row p-1">
        <div class="col-6">
            <hr />
        </div>
    </div>
    <div class="row p-1">
        <div class="col-6">
            <ul id="messagesList"></ul>
        </div>
    </div>
</div>
<script src="~/js/signalr/dist/browser/signalr.js"></script>
<script src="~/js/chat.js"></script>
```

The preceding markup:

*   Creates text boxes and a submit button.
*   Creates a list with `id="messagesList"` for displaying messages that are received from the SignalR hub.
*   Includes script references to SignalR and the `chat.js` app code is created in the next step.

In the `wwwroot/js` folder, create a `chat.js` file with the following code:

```
"use strict";

var connection = new signalR.HubConnectionBuilder().withUrl("/chatHub").build();

//Disable the send button until connection is established.
document.getElementById("sendButton").disabled = true;

connection.on("ReceiveMessage", function (user, message) {
    var li = document.createElement("li");
    document.getElementById("messagesList").appendChild(li);
    // We can assign user-supplied strings to an element's textContent because it
    // is not interpreted as markup. If you're assigning in any other way, you 
    // should be aware of possible script injection concerns.
    li.textContent = `${user} says ${message}`;
});

connection.start().then(function () {
    document.getElementById("sendButton").disabled = false;
}).catch(function (err) {
    return console.error(err.toString());
});

document.getElementById("sendButton").addEventListener("click", function (event) {
    var user = document.getElementById("userInput").value;
    var message = document.getElementById("messageInput").value;
    connection.invoke("SendMessage", user, message).catch(function (err) {
        return console.error(err.toString());
    });
    event.preventDefault();
});
```

The preceding JavaScript:

*   Creates and starts a connection.
*   Adds to the submit button a handler that sends messages to the hub.
*   Adds to the connection object a handler that receives messages from the hub and adds them to the list.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_4_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_4_visual-studio-code)

Select Ctrl+F5 to run the app without debugging.

Copy the URL from the address bar, open another browser instance or tab, and paste the URL in the address bar.

Choose either browser, enter a name and message, and select the **Send Message** button.

The name and message are displayed on both pages instantly.

![Image 15: Completed SignalR sample app](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/7.x/signalr-get-started-finished.png?view=aspnetcore-10.0)

Tip

If the app doesn't work, open the browser developer tools (F12) and go to the console. Look for possible errors related to HTML and JavaScript code. For example, if `signalr.js` was put in a different folder than directed, the reference to that file won't work resulting in a 404 error in the console. ![Image 16: signalr.js not found error](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/7.x/f12-console.png?view=aspnetcore-10.0) If an `ERR_SPDY_INADEQUATE_TRANSPORT_SECURITY` error has occurred in Chrome, run the following commands to update the development certificate:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

For information on deploying to Azure, see [Quickstart: Deploy an ASP.NET web app](https://learn.microsoft.com/en-us/azure/app-service/quickstart-dotnetcore). For more information on Azure SignalR Service, see [What is Azure SignalR Service?](https://learn.microsoft.com/en-us/azure/azure-signalr/signalr-overview).

*   [Use hubs](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0)
*   [Strongly typed hubs](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0#strongly-typed-hubs)
*   [Authentication and authorization in ASP.NET Core SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/authn-and-authz?view=aspnetcore-10.0)
*   [View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/signalr/javascript-client/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

This tutorial teaches the basics of building a real-time app using SignalR. You learn how to:

*   Create a web project.
*   Add the SignalR client library.
*   Create a SignalR hub.
*   Configure the project to use SignalR.
*   Add code that sends messages from any client to all connected clients.

At the end, you'll have a working chat app:

![Image 17: Completed SignalR sample app](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/7.x/signalr-get-started-finished.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/vs/#download) with the **ASP.NET and web development** workload.

![Image 18: VS22 installer workloads](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_2_visual-studio-mac)

Start Visual Studio 2022 and select **Create a new project**.

![Image 19: Create a new project from the start window](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/7.x/start-window-create-new-project.png?view=aspnetcore-10.0)

In the **Create a new project** dialog, select **ASP.NET Core Web App**, and then select **Next**.

![Image 20: Create an ASP.NET Core Web App](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/7.x/np.png?view=aspnetcore-10.0)

In the **Configure your new project** dialog, enter `SignalRChat` for **Project name**. It's important to name the project `SignalRChat`, including matching the capitalization, so the namespaces match the code in the tutorial.

Select **Next**.

In the **Additional information** dialog, select **.NET 7.0 (Standard Term Support)** and then select **Create**.

![Image 21: Additional information](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/7.x/additional_info.png?view=aspnetcore-10.0)

The SignalR server library is included in the ASP.NET Core shared framework. The JavaScript client library isn't automatically included in the project. For this tutorial, use Library Manager (LibMan) to get the client library from [unpkg](https://unpkg.com/). `unpkg`is a fast, global content delivery network for everything on [npm](https://www.npmjs.com/).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_3_visual-studio-mac)

In **Solution Explorer**, right-click the project, and select **Add**>**Client-Side Library**.

In the **Add Client-Side Library** dialog:

*   Select **unpkg** for **Provider**
*   Enter `@microsoft/signalr@latest` for **Library**.
*   Select **Choose specific files**, expand the _dist/browser_ folder, and select `signalr.js` and `signalr.min.js`.
*   Set **Target Location** to `wwwroot/js/signalr/`.
*   Select **Install**.

![Image 22: Add Client-Side Library dialog - select library](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/7.x/find-signalr-client-libs-select-files.png?view=aspnetcore-10.0)

LibMan creates a `wwwroot/js/signalr` folder and copies the selected files to it.

A _hub_ is a class that serves as a high-level pipeline that handles client-server communication.

In the SignalRChat project folder, create a `Hubs` folder.

In the `Hubs` folder, create the `ChatHub` class with the following code:

```
using Microsoft.AspNetCore.SignalR;

namespace SignalRChat.Hubs
{
    public class ChatHub : Hub
    {
        public async Task SendMessage(string user, string message)
        {
            await Clients.All.SendAsync("ReceiveMessage", user, message);
        }
    }
}
```

The `ChatHub` class inherits from the SignalR [Hub](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.signalr.hub) class. The `Hub` class manages connections, groups, and messaging.

The `SendMessage` method can be called by a connected client to send a message to all clients. JavaScript client code that calls the method is shown later in the tutorial. SignalR code is asynchronous to provide maximum scalability.

The SignalR server must be configured to pass SignalR requests to SignalR. Add the following highlighted code to the `Program.cs` file.

```
using SignalRChat.Hubs;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorPages();
builder.Services.AddSignalR();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();
app.MapHub<ChatHub>("/chatHub");

app.Run();
```

The preceding highlighted code adds SignalR to the ASP.NET Core dependency injection and routing systems.

Replace the content in `Pages/Index.cshtml` with the following code:

```
@page
<div class="container">
    <div class="row p-1">
        <div class="col-1">User</div>
        <div class="col-5"><input type="text" id="userInput" /></div>
    </div>
    <div class="row p-1">
        <div class="col-1">Message</div>
        <div class="col-5"><input type="text" class="w-100" id="messageInput" /></div>
    </div>
    <div class="row p-1">
        <div class="col-6 text-end">
            <input type="button" id="sendButton" value="Send Message" />
        </div>
    </div>
    <div class="row p-1">
        <div class="col-6">
            <hr />
        </div>
    </div>
    <div class="row p-1">
        <div class="col-6">
            <ul id="messagesList"></ul>
        </div>
    </div>
</div>
<script src="~/js/signalr/dist/browser/signalr.js"></script>
<script src="~/js/chat.js"></script>
```

The preceding markup:

*   Creates text boxes and a submit button.
*   Creates a list with `id="messagesList"` for displaying messages that are received from the SignalR hub.
*   Includes script references to SignalR and the `chat.js` app code is created in the next step.

In the `wwwroot/js` folder, create a `chat.js` file with the following code:

```
"use strict";

var connection = new signalR.HubConnectionBuilder().withUrl("/chatHub").build();

//Disable the send button until connection is established.
document.getElementById("sendButton").disabled = true;

connection.on("ReceiveMessage", function (user, message) {
    var li = document.createElement("li");
    document.getElementById("messagesList").appendChild(li);
    // We can assign user-supplied strings to an element's textContent because it
    // is not interpreted as markup. If you're assigning in any other way, you 
    // should be aware of possible script injection concerns.
    li.textContent = `${user} says ${message}`;
});

connection.start().then(function () {
    document.getElementById("sendButton").disabled = false;
}).catch(function (err) {
    return console.error(err.toString());
});

document.getElementById("sendButton").addEventListener("click", function (event) {
    var user = document.getElementById("userInput").value;
    var message = document.getElementById("messageInput").value;
    connection.invoke("SendMessage", user, message).catch(function (err) {
        return console.error(err.toString());
    });
    event.preventDefault();
});
```

The preceding JavaScript:

*   Creates and starts a connection.
*   Adds to the submit button a handler that sends messages to the hub.
*   Adds to the connection object a handler that receives messages from the hub and adds them to the list.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_4_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_4_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_4_visual-studio-mac)

Select Ctrl+F5 to run the app without debugging.

Copy the URL from the address bar, open another browser instance or tab, and paste the URL in the address bar.

Choose either browser, enter a name and message, and select the **Send Message** button.

The name and message are displayed on both pages instantly.

![Image 23: Completed SignalR sample app](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/7.x/signalr-get-started-finished.png?view=aspnetcore-10.0)

Tip

If the app doesn't work, open the browser developer tools (F12) and go to the console. Look for possible errors related to HTML and JavaScript code. For example, if `signalr.js` was put in a different folder than directed, the reference to that file won't work resulting in a 404 error in the console. ![Image 24: signalr.js not found error](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/7.x/f12-console.png?view=aspnetcore-10.0) If an `ERR_SPDY_INADEQUATE_TRANSPORT_SECURITY` error has occurred in Chrome, run the following commands to update the development certificate:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

For information on deploying to Azure, see [Quickstart: Deploy an ASP.NET web app](https://learn.microsoft.com/en-us/azure/app-service/quickstart-dotnetcore). For more information on Azure SignalR Service, see [What is Azure SignalR Service?](https://learn.microsoft.com/en-us/azure/azure-signalr/signalr-overview).

*   [Use hubs](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0)
*   [Strongly typed hubs](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0#strongly-typed-hubs)
*   [Authentication and authorization in ASP.NET Core SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/authn-and-authz?view=aspnetcore-10.0)
*   [View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/signalr/javascript-client/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

This tutorial teaches the basics of building a real-time app using SignalR. You learn how to:

*   Create a web project.
*   Add the SignalR client library.
*   Create a SignalR hub.
*   Configure the project to use SignalR.
*   Add code that sends messages from any client to all connected clients.

At the end, you'll have a working chat app:

![Image 25: SignalR sample app](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/3.x/signalr-get-started-finished.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/vs/#download) with the **ASP.NET and web development** workload.
*   [.NET 6 SDK](https://dotnet.microsoft.com/download/dotnet/6.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_2_visual-studio-mac)

Start Visual Studio 2022 and select **Create a new project**.

![Image 26: Create a new project from the start window](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/6.x/start-window-create-new-project.png?view=aspnetcore-10.0)

In the **Create a new project** dialog, select **ASP.NET Core Web App**, and then select **Next**.

![Image 27: Create an ASP.NET Core Web App](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/6.x/np.png?view=aspnetcore-10.0)

In the **Configure your new project** dialog, enter `SignalRChat` for **Project name**. It's important to name the project `SignalRChat`, including matching the capitalization, so the namespaces match the code in the tutorial.

Select **Next**.

In the **Additional information** dialog, select **.NET 6.0 (Long-term support)** and then select **Create**.

![Image 28: Additional information](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/6.x/additional-info.png?view=aspnetcore-10.0)

The SignalR server library is included in the ASP.NET Core shared framework. The JavaScript client library isn't automatically included in the project. For this tutorial, use Library Manager (LibMan) to get the client library from [unpkg](https://unpkg.com/). `unpkg`is a fast, global content delivery network for everything on [npm](https://www.npmjs.com/).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_3_visual-studio-mac)

In **Solution Explorer**, right-click the project, and select **Add**>**Client-Side Library**.

In the **Add Client-Side Library** dialog:

*   Select **unpkg** for **Provider**
*   Enter `@microsoft/signalr@latest` for **Library**.
*   Select **Choose specific files**, expand the _dist/browser_ folder, and select `signalr.js` and `signalr.min.js`.
*   Set **Target Location** to `wwwroot/js/signalr/`.
*   Select **Install**.

![Image 29: Add Client-Side Library dialog - select library](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/3.x/find-signalr-client-libs-select-files.png?view=aspnetcore-10.0)

LibMan creates a `wwwroot/js/signalr` folder and copies the selected files to it.

A _hub_ is a class that serves as a high-level pipeline that handles client-server communication.

In the SignalRChat project folder, create a `Hubs` folder.

In the `Hubs` folder, create the `ChatHub` class with the following code:

```
using Microsoft.AspNetCore.SignalR;

namespace SignalRChat.Hubs
{
    public class ChatHub : Hub
    {
        public async Task SendMessage(string user, string message)
        {
            await Clients.All.SendAsync("ReceiveMessage", user, message);
        }
    }
}
```

The `ChatHub` class inherits from the SignalR [Hub](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.signalr.hub) class. The `Hub` class manages connections, groups, and messaging.

The `SendMessage` method can be called by a connected client to send a message to all clients. JavaScript client code that calls the method is shown later in the tutorial. SignalR code is asynchronous to provide maximum scalability.

The SignalR server must be configured to pass SignalR requests to SignalR. Add the following highlighted code to the `Program.cs` file.

```
using SignalRChat.Hubs;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();
builder.Services.AddSignalR();

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();
app.MapHub<ChatHub>("/chatHub");

app.Run();
```

The preceding highlighted code adds SignalR to the ASP.NET Core dependency injection and routing systems.

Replace the content in `Pages/Index.cshtml` with the following code:

```
@page
    <div class="container">
        <div class="row p-1">
            <div class="col-1">User</div>
            <div class="col-5"><input type="text" id="userInput" /></div>
        </div>
        <div class="row p-1">
            <div class="col-1">Message</div>
            <div class="col-5"><input type="text" class="w-100" id="messageInput" /></div>
        </div>
        <div class="row p-1">
            <div class="col-6 text-end">
                <input type="button" id="sendButton" value="Send Message" />
            </div>
        </div>
        <div class="row p-1">
            <div class="col-6">
                <hr />
            </div>
        </div>
        <div class="row p-1">
            <div class="col-6">
                <ul id="messagesList"></ul>
            </div>
        </div>
    </div>
<script src="~/js/signalr/dist/browser/signalr.js"></script>
<script src="~/js/chat.js"></script>
```

The preceding markup:

*   Creates text boxes and a submit button.
*   Creates a list with `id="messagesList"` for displaying messages that are received from the SignalR hub.
*   Includes script references to SignalR and the `chat.js` app code is created in the next step.

In the `wwwroot/js` folder, create a `chat.js` file with the following code:

```
"use strict";

var connection = new signalR.HubConnectionBuilder().withUrl("/chatHub").build();

//Disable the send button until connection is established.
document.getElementById("sendButton").disabled = true;

connection.on("ReceiveMessage", function (user, message) {
    var li = document.createElement("li");
    document.getElementById("messagesList").appendChild(li);
    // We can assign user-supplied strings to an element's textContent because it
    // is not interpreted as markup. If you're assigning in any other way, you 
    // should be aware of possible script injection concerns.
    li.textContent = `${user} says ${message}`;
});

connection.start().then(function () {
    document.getElementById("sendButton").disabled = false;
}).catch(function (err) {
    return console.error(err.toString());
});

document.getElementById("sendButton").addEventListener("click", function (event) {
    var user = document.getElementById("userInput").value;
    var message = document.getElementById("messageInput").value;
    connection.invoke("SendMessage", user, message).catch(function (err) {
        return console.error(err.toString());
    });
    event.preventDefault();
});
```

The preceding JavaScript:

*   Creates and starts a connection.
*   Adds to the submit button a handler that sends messages to the hub.
*   Adds to the connection object a handler that receives messages from the hub and adds them to the list.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_4_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_4_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_4_visual-studio-mac)

Press CTRL+F5 to run the app without debugging.

Copy the URL from the address bar, open another browser instance or tab, and paste the URL in the address bar.

Choose either browser, enter a name and message, and select the **Send Message** button.

The name and message are displayed on both pages instantly.

![Image 30: SignalR sample app](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/3.x/signalr-get-started-finished.png?view=aspnetcore-10.0)

Tip

If the app doesn't work, open the browser developer tools (F12) and go to the console. Look for possible errors related to HTML and JavaScript code. For example, if `signalr.js` was put in a different folder than directed, the reference to that file won't work resulting in a 404 error in the console. ![Image 31: signalr.js not found error](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/3.x/f12-console.png?view=aspnetcore-10.0) If an `ERR_SPDY_INADEQUATE_TRANSPORT_SECURITY` error has occurred in Chrome, run the following commands to update the development certificate:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

For information on deploying to Azure, see [Quickstart: Deploy an ASP.NET web app](https://learn.microsoft.com/en-us/azure/app-service/quickstart-dotnetcore). For more information on Azure SignalR Service, see [What is Azure SignalR Service?](https://learn.microsoft.com/en-us/azure/azure-signalr/signalr-overview).

*   [Use hubs](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0)
*   [Strongly typed hubs](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0#strongly-typed-hubs)
*   [Authentication and authorization in ASP.NET Core SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/authn-and-authz?view=aspnetcore-10.0)
*   [View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/signalr/javascript-client/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

This tutorial teaches the basics of building a real-time app using SignalR. You learn how to:

*   Create a web project.
*   Add the SignalR client library.
*   Create a SignalR hub.
*   Configure the project to use SignalR.
*   Add code that sends messages from any client to all connected clients.

At the end, you'll have a working chat app:

![Image 32: SignalR sample app](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/3.x/signalr-get-started-finished.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Visual Studio 2019 16.4 or later](https://visualstudio.microsoft.com/downloads/?utm_medium=microsoft&utm_source=learn.microsoft.com&utm_campaign=inline+link&utm_content=download+vs2019) with the **ASP.NET and web development** workload
*   [.NET Core 3.1 SDK](https://dotnet.microsoft.com/download/dotnet-core/3.1)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_2_visual-studio-mac)

*   From the menu, select **File > New Project**.
*   In the **Create a new project** dialog, select **ASP.NET Core Web Application**, and then select **Next**.
*   In the **Configure your new project** dialog, name the project _SignalRChat_, and then select **Create**.
*   In the **Create a new ASP.NET Core web Application** dialog, select **.NET Core** and **ASP.NET Core 3.1**.
*   Select **Web Application** to create a project that uses Razor Pages, and then select **Create**.

![Image 33: New Project dialog in Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/3.x/signalr-new-project-dialog.png?view=aspnetcore-10.0)

The SignalR server library is included in the ASP.NET Core 3.1 shared framework. The JavaScript client library isn't automatically included in the project. For this tutorial, you use Library Manager (LibMan) to get the client library from _unpkg_. unpkg is a content delivery network (CDN) that can deliver anything found in npm, the Node.js package manager.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_3_visual-studio-mac)

*   In **Solution Explorer**, right-click the project, and select **Add**>**Client-Side Library**.
*   In the **Add Client-Side Library** dialog, for **Provider** select **unpkg**.
*   For **Library**, enter `@microsoft/signalr@latest`.
*   Select **Choose specific files**, expand the _dist/browser_ folder, and select `signalr.js` and `signalr.min.js`.
*   Set **Target Location** to _wwwroot/js/signalr/_
*   Select **Install**

![Image 34: Add Client-Side Library dialog - select library](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/3.x/find-signalr-client-libs-select-files.png?view=aspnetcore-10.0)

LibMan creates a _wwwroot/js/signalr_ folder and copies the selected files to it.

A _hub_ is a class that serves as a high-level pipeline that handles client-server communication.

*   In the SignalRChat project folder, create a _Hubs_ folder.
*   In the _Hubs_ folder, create a `ChatHub.cs` file with the following code:

```
using Microsoft.AspNetCore.SignalR;
using System.Threading.Tasks;

namespace SignalRChat.Hubs
{
    public class ChatHub : Hub
    {
        public async Task SendMessage(string user, string message)
        {
            await Clients.All.SendAsync("ReceiveMessage", user, message);
        }
    }
}
```

The `ChatHub` class inherits from the SignalR `Hub` class. The `Hub` class manages connections, groups, and messaging.

The `SendMessage` method can be called by a connected client to send a message to all clients. JavaScript client code that calls the method is shown later in the tutorial. SignalR code is asynchronous to provide maximum scalability.

The SignalR server must be configured to pass SignalR requests to SignalR.

*   Add the following highlighted code to the `Startup.cs` file.

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.HttpsPolicy;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using SignalRChat.Hubs;

namespace SignalRChat
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // This method gets called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddRazorPages();
            services.AddSignalR();
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }
            else
            {
                app.UseExceptionHandler("/Error");
                // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
                app.UseHsts();
            }

            app.UseHttpsRedirection();
            app.UseStaticFiles();

            app.UseRouting();

            app.UseAuthorization();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapRazorPages();
                endpoints.MapHub<ChatHub>("/chatHub");
            });
        }
    }
}
```

These changes add SignalR to the ASP.NET Core dependency injection and routing systems.

*   Replace the content in `Pages/Index.cshtml` with the following code:

```
@page
    <div class="container">
        <div class="row p-1">
            <div class="col-1">User</div>
            <div class="col-5"><input type="text" id="userInput" /></div>
        </div>
        <div class="row p-1">
            <div class="col-1">Message</div>
            <div class="col-5"><input type="text" class="w-100" id="messageInput" /></div>
        </div>
        <div class="row p-1">
            <div class="col-6 text-end">
                <input type="button" id="sendButton" value="Send Message" />
            </div>
        </div>
        <div class="row p-1">
            <div class="col-6">
                <hr />
            </div>
        </div>
        <div class="row p-1">
            <div class="col-6">
                <ul id="messagesList"></ul>
            </div>
        </div>
    </div>
<script src="~/js/signalr/dist/browser/signalr.js"></script>
<script src="~/js/chat.js"></script>
```

The preceding code:

    *   Creates text boxes for name and message text, and a submit button.
    *   Creates a list with `id="messagesList"` for displaying messages that are received from the SignalR hub.
    *   Includes script references to SignalR and the `chat.js` application code that you create in the next step.

*   In the _wwwroot/js_ folder, create a `chat.js` file with the following code:

```
"use strict";

var connection = new signalR.HubConnectionBuilder().withUrl("/chatHub").build();

//Disable send button until connection is established
document.getElementById("sendButton").disabled = true;

connection.on("ReceiveMessage", function (user, message) {
    var li = document.createElement("li");
    document.getElementById("messagesList").appendChild(li);
    // We can assign user-supplied strings to an element's textContent because it
    // is not interpreted as markup. If you're assigning in any other way, you 
    // should be aware of possible script injection concerns.
    li.textContent = `${user} says ${message}`;
});

connection.start().then(function () {
    document.getElementById("sendButton").disabled = false;
}).catch(function (err) {
    return console.error(err.toString());
});

document.getElementById("sendButton").addEventListener("click", function (event) {
    var user = document.getElementById("userInput").value;
    var message = document.getElementById("messageInput").value;
    connection.invoke("SendMessage", user, message).catch(function (err) {
        return console.error(err.toString());
    });
    event.preventDefault();
});
```

The preceding code:

    *   Creates and starts a connection.
    *   Adds to the submit button a handler that sends messages to the hub.
    *   Adds to the connection object a handler that receives messages from the hub and adds them to the list.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_4_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_4_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr?view=aspnetcore-10.0#tabpanel_4_visual-studio-mac)

*   Press **CTRL+F5** to run the app without debugging.

*   Copy the URL from the address bar, open another browser instance or tab, and paste the URL in the address bar.
*   Choose either browser, enter a name and message, and select the **Send Message** button. The name and message are displayed on both pages instantly.

![Image 35: SignalR sample app](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/3.x/signalr-get-started-finished.png?view=aspnetcore-10.0)

Tip

*   If the app doesn't work, open your browser developer tools (F12) and go to the console. You might see errors related to your HTML and JavaScript code. For example, suppose you put `signalr.js` in a different folder than directed. In that case the reference to that file won't work and you'll see a 404 error in the console. ![Image 36: signalr.js not found error](https://learn.microsoft.com/en-us/aspnet/core/tutorials/signalr/_static/3.x/f12-console.png?view=aspnetcore-10.0)

*   If you get the error ERR_SPDY_INADEQUATE_TRANSPORT_SECURITY in Chrome, run these commands to update your development certificate:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

For information on deploying to Azure, see [Quickstart: Deploy an ASP.NET web app](https://learn.microsoft.com/en-us/azure/app-service/quickstart-dotnetcore).

*   [Use hubs](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0)
*   [Strongly typed hubs](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-10.0#strongly-typed-hubs)
*   [Authentication and authorization in ASP.NET Core SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/authn-and-authz?view=aspnetcore-10.0)
*   [View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/signalr/javascript-client/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))
