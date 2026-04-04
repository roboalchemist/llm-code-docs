# Source: https://render.com/docs/deploy-puppeteer-node.md

# Deploy Puppeteer with Node

You can deploy a sample [Puppeteer](https://developers.google.com/web/tools/puppeteer/) service on Render in just a few clicks. Puppeteer helps you generate screenshots and PDFs of pages, crawl Single Page Apps (SPAs) to prerender them for SEO, and test your frontend code automatically.

For this example, we're using a minimally modified version of [Rendertron](https://github.com/GoogleChrome/rendertron), a Node project created by Google to demo Puppeteer features.

1. Fork [render-examples/rendertron](https://github.com/render-examples/rendertron) on GitHub.
2. Create a new *Web Service* on Render, and give Render permission to access your new repo.
3. Use the following values during creation:

   |                   |                                |
   | ----------------- | ------------------------------ |
   | *Language*      | `Node`                         |
   | *Build Command* | `npm install && npm run build` |
   | *Start Command* | `npm run start`                |

That's it! Your personal Rendertron will be live on your Render URL as soon as the build finishes.

See [Specifying a Node Version](node-version) if you need to customize the version of Node.js used for your app.