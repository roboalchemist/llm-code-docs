# Source: https://render.com/docs/deploy-sveltekit.md

# Deploy a SvelteKit App

[SvelteKit](https://kit.svelte.dev) is an exciting new development from the folks who created [Svelte](https://svelte.dev). While Svelte is great for static site creation, SvelteKit is a framework for building high-performance web applications. It includes routing, code-splitting, offline support, and server-rendered views with client-side hydration. Each page of a SvelteKit app is actually a Svelte component!

You can choose to deploy it as a [Node Server](#deploy-as-a-node-server) or [Static Site](#deploy-as-a-static-site).

The key difference is that the app deployed as a Node server is built using the [SvelteKit Node.js adapter](https://github.com/sveltejs/kit/tree/master/packages/adapter-node). The static site uses the [SvelteKit static adapter](https://github.com/sveltejs/kit/tree/master/packages/adapter-static) to generate static HTML for all pages.

## Deploy as a Node Server

A sample app is deployed at https://sveltekit-app.onrender.com. Follow the steps below to start building your own SvelteKit app.

### One-Click Deploy

Click Deploy to Render below and follow the prompts to deploy SvelteKit to Render.

<deploy-to-render repo="https://github.com/render-examples/sveltekit">
</deploy-to-render>

### Manual Deploy

1. [Create your own repo from Render's SvelteKit template repo](https://github.com/new?template_name=sveltekit&template_owner=render-examples) on GitHub (you may need to log in first).
   - Alternatively, you can [clone the repo](https://github.com/render-examples/sveltekit/) and push your clone to GitLab or Bitbucket.
2. Create a [new *Web Service*](https://dashboard.render.com/select-repo?type=web) on Render, and give Render permission to access the repo.
3. Use the following values during creation:

   |                   |                                |
   | ----------------- | ------------------------------ |
   | *Language*      | `Node`                         |
   | *Build Command* | `npm install && npm run build` |
   | *Start Command* | `node build/index.js`          |

That's it! Your SvelteKit app will be live on your Render URL as soon as the build finishes and the service starts.

## Deploy as a Static Site

A sample static site is deployed at https://sveltekit-static.onrender.com. Follow the steps below to start building your own site.

### One-Click Deploy

Click Deploy to Render below and follow the prompts to deploy SvelteKit to Render as a Static Site.

<deploy-to-render repo="https://github.com/render-examples/sveltekit-static">
</deploy-to-render>

### Manual Deploy

1. [Create your own repo from Render's SvelteKit Static template repo](https://github.com/render-examples/sveltekit-static/generate) on GitHub (you may need to log in first).
2. Create a [new *Static Site*](https://dashboard.render.com/select-repo?type=static) on Render, and give Render permission to access the repo.
3. Use the following values during creation:

   |                       |                                |
   | --------------------- | ------------------------------ |
   | *Build Command*     | `npm install && npm run build` |
   | *Publish Directory* | `build`                        |

That's it! Your static site will be live on your Render URL as soon as the build finishes.