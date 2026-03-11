# Source: https://www.fastly.com/documentation/guides/compute/developer-guides/frameworks/

Title: Front-end frameworks on the Compute platform | Fastly Documentation

URL Source: https://www.fastly.com/documentation/guides/compute/developer-guides/frameworks/

Markdown Content:

1. [Home](https://www.fastly.com/documentation/)
2. [Guides](https://www.fastly.com/documentation/guides/)
3. [Compute](https://www.fastly.com/documentation/guides/compute/)
4. [Developer guides](https://www.fastly.com/documentation/guides/compute/developer-guides/)

Many full stack and static site frameworks can be used with the Compute platform. Frameworks often give developers the ability to write frontend components using a library like [React](https://react.dev/), offer useful abstractions for server routes and request handlers, and a convenient and intuitive way to set up some of the best features you need for production: hybrid static & server rendering, smart bundling, route prefetching, and more, with very little configuration needed.

Fastly aims to provide compatibility with frameworks, and at least, avoid getting in their way - but for some, we have official libraries to help you get the most out of the framework when you use it with Fastly.

[](https://www.fastly.com/documentation/guides/compute/developer-guides/frameworks/#nextjs)Next.js
--------------------------------------------------------------------------------------------------

[Next.js](https://nextjs.org/) is an open source full stack web framework created by [Vercel](https://vercel.com/). It uses React for front end component management and has server-side rendering and dynamic server-side components for API routes.

We maintain [`next-compute-js`](https://github.com/fastly/next-compute-js)[](https://www.fastly.com/documentation/developers/labs) to provide a combination of project-scaffolding and a Next.js runtime for our Compute platform. It operates on the exact same built artifacts from the next build command, and aims to provide all of the features of the Next.js runtime (except for the bits that are dependent on the [Vercel Edge runtime](https://vercel.com/blog/introducing-the-edge-runtime) — which currently requires a full Node.js environment).

To use it, run a standard Next.js build using npx next build, then:

`$ npx @fastly/next-compute-js$ cd compute-js$ fastly compute publish`

For more information:

* See [`next-compute-js` on GitHub](https://github.com/fastly/next-compute-js) for usage instructions
* Read the [announcement blog post](https://www.fastly.com/blog/run-your-next-js-app-on-fastly)

[](https://www.fastly.com/documentation/guides/compute/developer-guides/frameworks/#remix)Remix
-----------------------------------------------------------------------------------------------

[Remix](https://remix.run/) is a JavaScript-based full stack web framework that focuses on UI and web standards. We maintain [remix-compute-js](https://github.com/fastly/remix-compute-js/)[](https://www.fastly.com/documentation/developers/labs) as a template that can be used by the official Remix command line tool:

`$ npm create remix@latest ./my-app --template https://github.com/fastly/remix-compute-js/tree/main/packages/remix-template`

This will create a project in the `my-app` directory that is both a Remix app and also a valid Compute program. Remix will be configured to use Fastly's [local development server](https://www.fastly.com/documentation/guides/compute/developer-guides/testing/#running-a-local-testing-server), and commands such as npm run dev, npm run build, and npm run deploy will work as expected, with deploys going to your Fastly account.

For more information:

* See [`remix-compute-js` on GitHub](https://github.com/fastly/remix-compute-js/) for usage instructions
* Read the [announcement blog post](https://www.fastly.com/blog/host-your-remix-app-on-fastly-compute-edge)

[](https://www.fastly.com/documentation/guides/compute/developer-guides/frameworks/#static-site--jamstack)Static site & JAMStack
--------------------------------------------------------------------------------------------------------------------------------

Static site generators produce a directory of files that can be served by any properly configured web server. Our [`compute-js-static-publish`](https://github.com/fastly/compute-js-static-publish)[](https://www.fastly.com/documentation/developers/labs) tool is designed to make it as easy as possible to get those files onto Fastly.

For example, for a [Gatsby](https://www.gatsbyjs.com/) site:

`$ npm run build$ npx @fastly/compute-js-static-publish --preset=gatsby$ cd ./compute-js$ fastly compute publish`

We have preset support for a variety of frameworks, including [create-react-app](https://create-react-app.dev/), [Vite](https://vitejs.dev/), [SvelteKit](https://kit.svelte.dev/), [Vue](https://vuejs.org/), [Next.js](https://nextjs.org/), [Astro](https://astro.build/), [Gatsby](https://www.gatsbyjs.com/) and [Docusaurus](https://docusaurus.io/).

For more information:

* See [`compute-js-static-publish` on GitHub](https://github.com/fastly/compute-js-static-publish) for complete documentation
* Read the [announcement blog post](https://www.fastly.com/blog/no-origin-static-websites-at-the-edge)

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/frameworks/#adding-dynamic-routes)Adding dynamic routes

Once the static publisher has created your Fastly app, you have an `index.js` file which you can edit to add whatever additional routes you would like to handle. [Learn more about running your own code alongside static routes](https://github.com/fastly/compute-js-static-publish?_fsi=kXZve2xi#running-custom-code-alongside-publisher-server).
