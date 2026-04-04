# Source: https://render.com/docs/deploy-svelte.md

# Deploy a Svelte Static Site

Using this guide you can deploy a [Svelte](https://svelte.dev) static site on Render in just a few clicks. If you'd like to deploy a [SvelteKit](https://kit.svelte.dev) Node app instead, check out our [SvelteKit guide](/deploy-sveltekit).

1. [Create your own repo from Render's Svelte template repo](https://github.com/new?template_name=svelte&template_owner=render-examples) on GitHub.
   - Alternatively, you can [clone the repo](https://github.com/render-examples/svelte/) and push your clone to GitLab or Bitbucket.
2. Create a [new Static Site](https://dashboard.render.com/select-repo?type=static) on Render, and give Render permission to access your new repo.
3. Use the following values during creation:

   |                       |                                |
   | --------------------- | ------------------------------ |
   | *Build Command*     | `npm install && npm run build` |
   | *Publish Directory* | `public`                       |

That's it! Your static site will be live on your Render URL as soon as the build finishes.