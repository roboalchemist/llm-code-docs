# Source: https://render.com/docs/deploy-nextjs-app.md

# Deploy a Next.js App

You can deploy a [Next.js](https://nextjs.org/) application on Render in just a few clicks.

A sample app for this quick start is deployed at https://next-js.onrender.com.

You can choose to deploy it as a [Node Server](#deploy-as-a-node-server) or [Static Site](#deploy-as-a-static-site).

## Deploy as a Node Server

1. Fork [nextjs-hello-world](https://github.com/render-examples/nextjs-hello-world/tree/master) on GitHub.
2. Create a new *Web Service* on Render, and give Render permission to access your new repo.
3. Use the following values during creation:

   |                   |                    |
   | ----------------- | ------------------ |
   | *Language*      | `Node`             |
   | *Build Command* | `yarn; yarn build` |
   | *Start Command* | `yarn start`       |

That's it! Your web service will be live on your Render URL as soon as the build finishes.

See [Specifying a Node Version](node-version) if you need to customize the version of Node.js used for your app.

## Deploy as a Static Site

1. Fork [nextjs-hello-world](https://github.com/render-examples/nextjs-hello-world/tree/master) on GitHub.
1. Modify the code according to the instructions in the [nextjs-hello-world README](https://github.com/render-examples/nextjs-hello-world/blob/master/README.md).
1. Create a new *Static Site* on Render, and give Render permission to access your new repo.
1. Use the following values during creation:

   |                       |                    |
   | --------------------- | ------------------ |
   | *Build Command*     | `yarn; yarn build` |
   | *Publish Directory* | `out`              |

That's it! Your static site will be live on your Render URL as soon as the build finishes.