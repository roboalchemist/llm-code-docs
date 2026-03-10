# Source: https://render.com/docs/deploy-node-fastify-app.md

# Deploy a Node Fastify App

[Fastify](https://www.fastify.io/) is fast and low overhead web framework, for Node.js.

> *Note:* Fastify's `.listen` method default binding uses `localhost` (`127.0.0.1`), whereas Render requires `0.0.0.0`. See our [example repo](https://github.com/render-examples/fastify-hello-world) for a setup that works with Render.

## One-Click Deploy

<deploy-to-render repo="https://github.com/render-examples/fastify-hello-world">
</deploy-to-render>

## Manual Deploy

1. Fork [fastify-hello-world](https://github.com/render-examples/fastify-hello-world) on GitHub.
2. Create a new *Web Service* on Render, and give Render permission to access your new repo.
3. Use the following values during creation:

   |                   |               |
   | ----------------- | ------------- |
   | *Language*      | `Node`        |
   | *Build Command* | `npm install` |
   | *Start Command* | `node app.js` |

That's it! Your web service will be live on your Render URL as soon as the build finishes.

This quickstart is also deployed at https://fastify.onrender.com.

See [Specifying a Node Version](node-version) if you need to customize the version of Node.js used for your app.