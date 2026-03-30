# Source: https://render.com/docs/deploy-nuxtjs.md

# Deploy a Nuxt.js App

[NuxtJS](https://nuxtjs.org) is a Vue.js framework that you can deploy on Render in just a few clicks.

A sample app for this quick start is deployed at https://hello-nuxt.onrender.com.

You can choose to deploy it as a [Node Server](#deploy-as-a-node-server) or [Static Site](#deploy-as-a-static-site).

## Deploy as a Node Server

1. Fork [nuxtjs-hello-world](https://github.com/render-examples/nuxtjs-hello-world/tree/master) on GitHub.
2. Create a new *Web Service* on Render, and give Render permission to access your new repo.
3. Use the following values during creation:

   |                   |                    |
   | ----------------- | ------------------ |
   | *Language*      | `Node`             |
   | *Build Command* | `yarn; yarn build` |
   | *Start Command* | `yarn start`       |

4. Add the following environment variable to your web service:

   | Key    | Value     |
   | ------ | --------- |
   | `HOST` | `0.0.0.0` |

That's it! Your web service will be live on your Render URL as soon as the build finishes.

See [Specifying a Node Version](node-version) if you need to customize the version of Node.js used for your app.

## Deploy as a Static Site

1. Fork [nuxtjs-hello-world](https://github.com/render-examples/nuxtjs-hello-world/tree/master) on GitHub.
2. Create a new *Static Site* on Render, and give Render permission to access your new repo.
3. Use the following values during creation:

   |                       |                       |
   | --------------------- | --------------------- |
   | *Branch*            | `static`              |
   | *Build Command*     | `yarn; yarn generate` |
   | *Publish Directory* | `dist`                |

That's it! Your static site will be live on your Render URL as soon as the build finishes.

## Infrastructure as Code

You can version control these deployment configurations using Render's [Infrastructure as Code](infrastructure-as-code) functionality. Sample `render.yaml` files for this process are provided in both the main and static branches of the [nuxtjs-hello-world](https://github.com/render-examples/nuxtjs-hello-world) example repo.