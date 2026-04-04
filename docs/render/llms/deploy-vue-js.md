# Source: https://render.com/docs/deploy-vue-js.md

# Deploy a Vue.js App

You can deploy a [Vue.js](https://vuejs.org/) app on Render in under a minute. Your site is served over a *lightning-fast global CDN*, comes with *fully managed TLS* certificates, and supports *custom domains* out of the box.

The sample app for this quick start is deployed at https://vue.onrender.com.

1. Use your existing Vue.js repository, or fork our sample Vue.js repo on [GitHub](https://github.com/render-examples/vue-hello-world) or [GitLab](https://gitlab.com/render-examples/vue-hello-world).
2. Create a new *Static Site* on Render, and give Render permission to access your new repo.
3. Use the following values during creation:

   |                       |                    |
   | --------------------- | ------------------ |
   | *Build Command*     | `yarn; yarn build` |
   | *Publish Directory* | `dist`             |

That's it! Your app will be live on your Render URL as soon as the build finishes.

## Using Client-Side Routing

If you use [Vue Router](https://github.com/vuejs/vue-router) for [client-side routing](https://vuejs.org/v2/guide/routing.html), you will need to direct all routing requests to `index.html` so they can be handled by your routing library.

You can do this easily by defining a *Rewrite Rule* for your static site. Go to the *Redirects/Rewrites* tab for your service and add a rule with the following values:

|                  |               |
| ---------------- | ------------- |
| Source Path      | `/*`          |
| Destination Path | `/index.html` |
| Action           | `Rewrite`     |

The result should look like this:

[image: Vue Router Rewrite]

See [Specifying a Node Version](node-version) if you need to customize the version of Node.js used for your app.