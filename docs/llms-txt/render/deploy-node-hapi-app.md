# Source: https://render.com/docs/deploy-node-hapi-app.md

# Deploy a Node hapi App

You can deploy a Node [hapi](https://hapijs.com) application on Render in just a few clicks.

A sample app for this quick start is deployed at https://hapijs.onrender.com

1. Fork [hapi-quick-start](https://github.com/render-examples/hapi-quick-start) on GitHub.
2. Create a new *Web Service* on Render, and give Render permission to access your new repo.
3. Use the following values during creation:

   |                   |                  |
   | ----------------- | ---------------- |
   | *Language*      | `Node`           |
   | *Build Command* | `npm install`    |
   | *Start Command* | `node server.js` |

That's it! Your web service will be live on your Render URL as soon as the build finishes.

See [Specifying a Node Version](node-version) if you need to customize the version of Node.js used for your app.