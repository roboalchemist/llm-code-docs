# Source: https://render.com/docs/deploy-node-express-app.md

# Deploy a Node Express App on Render

You can deploy a Node.js [Express](https://expressjs.com) application on Render in just a few clicks.

This quickstart uses a simple example app. You're welcome to use your own Express app instead.

1. Fork the [express-hello-world](https://github.com/render-examples/express-hello-world) repo on GitHub.

> A demo instance of this app is hosted at [express.onrender.com](https://express.onrender.com).

2. In the [Render Dashboard](https://dashboard.render.com), click *New > Web Service* and connect your new repo.

3. Provide the following values during creation:

   |                   |               |
   | ----------------- | ------------- |
   | *Language*      | `Node`        |
   | *Build Command* | `yarn`        |
   | *Start Command* | `node app.js` |

> *Using your own app?* Instead provide whatever commands you use to build and start it, such as `npm install`/`npm start` or `bun install`/`bun start`.

That's it! Your web service will be live at its `onrender.com` URL as soon as the deploy finishes.

Going forward, every push to your linked branch automatically builds and deploys your app. If a build fails, Render cancels the deploy, and your app's existing version continues running until the next successful deploy. [Learn more about deploys.](/deploys)

If you need to use a specific version of Node.js for your app, see [Setting Your Node.js Version](node-version).