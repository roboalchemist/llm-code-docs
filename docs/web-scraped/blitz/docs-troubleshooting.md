# Source: https://blitzjs.com/docs/troubleshooting

Title: Troubleshooting - Blitz.js

URL Source: https://blitzjs.com/docs/troubleshooting

Markdown Content:
This documentation explains how you can debug your Blitz frontend and backend code with full source maps support using either the [VS Code debugger](https://code.visualstudio.com/docs/editor/debugging) or [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools).

Any debugger that can attach to Node.js can also be used to debug a Blitz application. You can find more details in the Node.js [Debugging Guide](https://nodejs.org/en/docs/guides/debugging-getting-started/).

[](https://blitzjs.com/docs/troubleshooting#vscode)Debugging with VS Code
-------------------------------------------------------------------------

Create a file named `.vscode/launch.json` at the root of your project with the following content:

`npm run dev` can be replaced with `yarn dev` if you're using Yarn, or with `blitz dev` if you have Blitz installed globally. If you're [changing the port number](https://blitzjs.com/docs/cli-dev) your application starts on, replace the `3000` in `http://localhost:3000` with the port you're using instead.

Now go to the Debug panel (Ctrl+Shift+D on Windows/Linux, ⇧+⌘+D on macOS), select a launch configuration, then press F5 or select **Debug: Start Debugging** from the Command Palette to start your debugging session.

[](https://blitzjs.com/docs/troubleshooting#chrome-devtools)Debugging with Chrome DevTools
------------------------------------------------------------------------------------------

### [](https://blitzjs.com/docs/troubleshooting#chrome-devtools-client)Client-side code

Start your development server as usual by running `blitz dev`, `npm run dev`, or `yarn dev`. Once the server starts, open `http://localhost:3000` (or your alternate URL) in Chrome. Next, open Chrome's Developer Tools (Ctrl+Shift+J on Windows/Linux, ⌥+⌘+I on macOS), then go to the **Sources** tab

Now, any time your client-side code reaches a [`debugger`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/debugger) statement, code execution will pause and that file will appear in the debug area. You can also press Ctrl+P on Windows/Linux or ⌘+P on macOS to search for a file and set breakpoints manually. Note that when searching here, your source files will have paths starting with `webpack://_N_E/./`.

### [](https://blitzjs.com/docs/troubleshooting#chrome-devtools-server)Server-side code

To debug server-side Blitz code with Chrome DevTools, you need to pass the [`--inspect`](https://nodejs.org/api/cli.html#cli_inspect_host_port) flag to the underlying Node.js process:

If you're using `npm run dev` or `yarn dev` (see [Getting Started](https://blitzjs.com/docs/getting-started)) then you should update the `dev` script on your `package.json`:

Launching the Blitz dev server with the `--inspect` flag will look something like this:

> Be aware that running `NODE_OPTIONS='--inspect' npm run dev` or `NODE_OPTIONS='--inspect' yarn dev` won't work. This would try to start multiple debuggers on the same port: one for the npm/yarn process and one for Blitz. You would then get an error like `Starting inspector on 127.0.0.1:9229 failed: address already in use` in your console.

Once the server starts, open a new tab in Chrome and visit `chrome://inspect`, where you should see your Blitz application inside the **Remote Target** section. Click **inspect** under your application to open a separate DevTools window, then go to the **Sources** tab.

Debugging server-side code here works much like debugging client-side code with Chrome DevTools, except that when you search for files here with

Ctrl+P or ⌘+P, your source files will have paths starting with `webpack://APPLICATION_NAME/./` (where `APPLICATION_NAME` will be replaced with the name of your application according to your `package.json` file).

[](https://blitzjs.com/docs/troubleshooting#debug-logging)Debug logging
-----------------------------------------------------------------------

If you need a more verbose experience on any Blitz module, for debugging purpose, you can enable advanced logging using the DEBUG environment variable.

Blitz internally uses the [debug](https://www.npmjs.com/package/debug) package.

For example, if you want to enable the REPL logging you can run the console like so :

You can also use a wildcard pattern :

Here are the namespace used by Blitz :

* `blitz:approot`
* `blitz:cli`
* `blitz:config`
* `blitz:errorboundary`
* `blitz:generate`
* `blitz:generator`
* `blitz:installer`
* `blitz:manifest`
* `blitz:middleware`
* `blitz:new`
* `blitz:postinstall`
* `blitz:repl`
* `blitz:rpc`
* `blitz:session`
* `blitz:utils`

### [](https://blitzjs.com/docs/troubleshooting#usage-in-the-browser)Usage in the browser

You can also have this kind of logging for the client-side part of Blitz. To do so simply set the local storage variable debug to `blitz:*` or any namespace used by Blitz and then refresh the page.

Please, be sure that the devtools console has the verbose level enabled.

[](https://blitzjs.com/docs/troubleshooting#more-info)More information
----------------------------------------------------------------------

To learn more about how to use a JavaScript debugger, take a look at the following documentation:

* [Node.js debugging in VS Code: Breakpoints](https://code.visualstudio.com/docs/nodejs/nodejs-debugging#_breakpoints)
* [Chrome DevTools: Debug JavaScript](https://developers.google.com/web/tools/chrome-devtools/javascript)
