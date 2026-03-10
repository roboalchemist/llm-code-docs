# Source: https://render.com/docs/deploy-docusaurus.md

# Deploy a Docusaurus Static Site

[Docusaurus](https://docusaurus.io) is a great way to build documentation websites for your projects, and you can deploy a Docusaurus site on Render in under a minute.

Your site is served over a *lightning-fast global CDN*, comes with *fully managed TLS* certificates, and supports *custom domains* out of the box.

1. Create a new *Static Site* on Render, and give Render permission to access your Docusaurus repo.

2. Use the following values during creation:

   |                       |                            |
   | --------------------- | -------------------------- |
   | *Build Command*     | `yarn install; yarn build` |
   | *Publish Directory* | `./build`                  |

> `projectName` above is the value you defined in `docusaurus.config.js` as shown below.

   ```javascript{7}
   const siteConfig = {
     title: 'Docusaurus Example', // Title for your website.
     tagline: 'Fast and easy deployment on Render',
     url: 'https://docusaurus.onrender.com', // Your website URL
     baseUrl: '/', // Base URL for your project */
     // Used for publishing and more
     projectName: 'your-project-name',
     // ...
   ```

That's it! Your app will be live on your Render URL as soon as the build finishes.

See [Specifying a Node Version](node-version) if you need to customize the version of Node.js used for your site.