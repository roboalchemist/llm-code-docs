# Source: https://docs.upsun.com/languages/nodejs/debug.md

# Debugging


p:last-child]:mb-0 [&>h3]:mt-0 rounded-lg" >

### Note
You can now use composable image (BETA) to install runtimes and tools in your application container. To find out more, see the [dedicated documentation page](https://docs.upsun.com/create-apps/app-reference/composable-image.md).

Effectively debugging web apps takes effort,
especially when an HTTP request goes through multiple layers before reaching your web app.
Follow the steps below to debug a specific app.

You can choose to debug in an environment deployed to Upsun
or with your app running locally but connected to deployed services.
In either case, make sure to debug in a preview environment.

For more general information, see how to [troubleshoot development](https://docs.upsun.com/development/troubleshoot.md).

## 1. Create a new environment

Start by creating a new environment completely isolated from production but with the same data for debugging:

```bash
upsun branch debug-branch
```

## 2. Get access

To access deployed apps and services, open tunnels to everything your app has relationships with:

```bash {}
upsun tunnel:open
```

In the same terminal, set the relevant environment variables:

```bash {}
export PLATFORM_RELATIONSHIPS="$(upsun tunnel:info --encode)"
export PORT=8888
```

## 3. Run your app in inspect mode

In the same terminal as the previous step, run the following command:

```bash {}
node --inspect <START_FILE>
```

Replace `<START_FILE>` with the file defined for [your app's `start` command](https://docs.upsun.com/languages/nodejs.md#4-start-your-app).

You get output something like this:

```bash
Debugger listening on ws://127.0.0.1:9229/10701e5d-d627-4180-a967-d47a924c93c0
For help, see: https://nodejs.org/en/docs/inspector
Listening on port 8888
```

## 4. (If debugging remotely) Forward the debugger port locally

In another terminal, create an SSH tunnel that forwards to the 9229 port:

```bash
ssh -N -L 9229:localhost:9229 $(upsun ssh --pipe)
```

## 5. Connect the debugger

You can now connect the debugger as if you were debugging a local application.
See examples with some common tools:

Use the ``Node.js: Attach`` debugger option.
If you haven’t created the option:

 - On the **Run and Debug** tab, click ``create a launch.json file``.
 - Select ``Node.js`` as the environment.
 - In the ``configurations`` array, start IntelliSense (usually ctrl+space).
 - Select ``Node.js: Attach``.
 - Make sure the port is the same as in [step 4 above](#4-if-debugging-remotely-forward-the-debugger-port-locally).

Once you have the option:
In the **Run and Debug** tab, select ``Attach`` from the menu and click **Start Debugging** (the green arrow).
See more on [Node.js debugging in Visual Studio Code](https://code.visualstudio.com/docs/nodejs/nodejs-debugging).

Now when you load the site at your deployed URL (if debugging remote) or localhost (if debugging locally),
the local debugger you've attached is called.

Set breakpoints:

Directly in your source files.

## Other issues

### pm2 process manager blocks other processes

If you're using the [`pm2` process manager](https://github.com/unitech/pm2) to start your app from a script,
you might find it daemonizes itself and blocks other processes (such as backups) by constantly respawning.
This may happen even if you use the `--no-daemon` flag.

Instead of using a script, call `pm2 start` directly in your [`start` command](https://docs.upsun.com/languages/nodejs.md#4-start-your-app).

