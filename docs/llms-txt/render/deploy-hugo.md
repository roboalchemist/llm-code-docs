# Source: https://render.com/docs/deploy-hugo.md

# Deploy a Hugo Static Site

You can deploy a [Hugo](https://gohugo.io/) static site on Render in under a minute. Your site is served over a *lightning-fast global CDN*, comes with *fully managed TLS* certificates, and supports *custom domains* out of the box. Best of all, it's free!

The sample app in this guide is based on Hugo's official [quick start](https://gohugo.io/getting-started/quick-start/).

1. Use your existing Hugo repository, or fork our sample Hugo repo on [GitHub](https://github.com/render-examples/hugo-quick-start) or [GitLab](https://gitlab.com/render-examples/hugo).
2. Create a new *Static Site* on Render, and give Render permission to access your new repo.
3. Use the following values during creation:

   |                       |                      |
   | --------------------- | -------------------- |
   | *Build Command*     | `hugo --gc --minify` |
   | *Publish Directory* | `public`             |

That's it! Your app will be live on your Render URL as soon as the build finishes.