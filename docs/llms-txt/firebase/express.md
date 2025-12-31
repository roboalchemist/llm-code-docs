# Source: https://firebase.google.com/docs/hosting/frameworks/express.md.txt

<br />

With some additional configuration, you can build on the basic framework-aware CLI functionality to extend integration support to frameworks other than Angular and Next.js.
| **Note:** Framework-awareHostingis an early public preview. This means that the functionality might change in backward-incompatible ways. A preview release is not subject to any SLA or deprecation policy and may receive limited or no support.

## Before you begin

Before you get started deploying your app to Firebase, review the following requirements and options:

- FirebaseCLI version 12.1.0 or later. Make sure to[install the CLI](https://firebase.google.com/docs/cli#install_the_firebase_cli)using your preferred method.
- Optional: Billing enabled on your Firebase project (required if you plan to use SSR)

## Initialize Firebase

To get started, initialize Firebase for your framework project. Use theFirebaseCLI for a new project, or modify`firebase.json`for an existing project.

### Initialize a new project

1. In theFirebaseCLI, enable the web frameworks preview:  

   ```
   firebase experiments:enable webframeworks
   ```
2. Run the initialization command from the CLI and then follow the prompts:

   ```
   firebase init hosting
   ```

   <br />

3. Answer yes to "Do you want to use a web framework? (experimental)"

4. Choose your hosting source directory; this could be an existing web app.

5. If prompted, choose Express.js / custom

### Initialize an existing project

Change your hosting config in`firebase.json`to have a`source`option, rather than a`public`option. For example:  

    {
      "hosting": {
        "source": "./path-to-your-express-directory"
      }
    }

## Serve static content

Before deploying static content, you'll need to configure your application.

### Configure

In order to know how to deploy your application, theFirebaseCLI needs to be able to both build your app and know where your tooling places the assets destined forHosting. This is accomplished with the npm build script and CJS directories directive in`package.json`.

Given the following package.json:  

    {
        "name": "express-app",
        "version": "0.0.0",
        "scripts": {
            "build": "spack",
            "static": "cp static/* dist",
            "prerender": "ts-node prerender.ts"
        },
        ...
    }

TheFirebaseCLI only calls your build script, so you'll need to ensure that your build script is exhaustive.
**Tip:** you can add additional steps using`&&`. If you have a lot of steps, consider a shell script or tooling like[npm-run-all](https://www.npmjs.com/package/npm-run-all)or[wireit](https://www.npmjs.com/package/wireit).  

    {
        "name": "express-app",
        "version": "0.0.0",
        "scripts": {
            "build": "spack && npm run static && npm run prerender",
            "static": "cp static/* dist",
            "prerender": "ts-node prerender.ts"
        },
        ...
    }

If your framework doesn't support pre-rendering out of the box, consider using a tool like[Rendertron](https://github.com/GoogleChrome/rendertron). Rendertron will allow you to make headless Chrome requests against a local instance of your app, so you can save the resulting HTML to be served onHosting.

Finally, different frameworks and build tools store their artifacts in different places. Use`directories.serve`to tell the CLI where your build script is outputting the resulting artifacts:  

    {
        "name": "express-app",
        "version": "0.0.0",
        "scripts": {
            "build": "spack && npm run static && npm run prerender",
            "static": "cp static/* dist",
            "prerender": "ts-node prerender.ts"
        },
        "directories": {
            "serve": "dist"
        },
        ...
    }

### Deploy

After configuring your app, you can serve static content with the standard deployment command:  

    firebase deploy

## Serve Dynamic Content

To serve your Express app onCloud Functions for Firebase, ensure that your Express app (or express-style URL handler) is exported in such a way that Firebase can find it after your library has been npm packed.

To accomplish this, ensure that your`files`directive includes everything needed for the server, and that your main entry point is set up correctly in`package.json`:  

    {
        "name": "express-app",
        "version": "0.0.0",
        "scripts": {
            "build": "spack && npm run static && npm run prerender",
            "static": "cp static/* dist",
            "prerender": "ts-node tools/prerender.ts"
        },
        "directories": {
            "serve": "dist"
        },
        "files": ["dist", "server.js"],
        "main": "server.js",
        ...
    }

Export your express app from a function named`app`:  

    // server.js
    export function app() {
      const server = express();
       ...
       return server;
    }

Or if you'd rather export an express-style URL handler, name it`handle`:  

    export function handle(req, res) {
       res.send('hello world');
    }

### Deploy

    firebase deploy

This deploys your static content toFirebase Hostingand allows Firebase to fall back to your Express app hosted onCloud Functions for Firebase.

## Optional: integrate with Firebase Authentication

The web framework-aware Firebase deploy tooling will automatically keep client and server state in sync using cookies. To access the authentication context, the Express`res.locals`object optionally contains an authenticated Firebase App instance (`firebaseApp`) and the currently signed in User (`currentUser`).