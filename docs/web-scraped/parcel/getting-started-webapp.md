# Source: https://parceljs.org/getting-started/webapp/

Title: Building a web app with Parcel

URL Source: https://parceljs.org/getting-started/webapp/

Markdown Content:
Quick start
-----------

[#](https://parceljs.org/getting-started/webapp/#quick-start)
To quickly scaffold a new web app with Parcel, run the following commands. This will create a new Git repository, install dependencies, and setup a few source files you can modify.

`npm create parcel vanilla my-parcel-appcd my-parcel-appnpm start`
Replace `npm` with `yarn` or `pnpm` to use your preferred package manager. The following templates are supported:

*   `vanilla` – a Vanilla JS + HTML app (shown above)
*   `react-client` – a TypeScript + React client only app. See [Parcel's React docs](https://parceljs.org/recipes/react/).
*   `react-server` – a TypeScript + React Server Components app. See [Parcel's React Server Components docs](https://parceljs.org/recipes/rsc/).
*   `react-static` – a TypeScript + React static site generator. See [Parcel's React Server Components docs](https://parceljs.org/recipes/rsc/).

See below for a deep dive.

Installation
------------

[#](https://parceljs.org/getting-started/webapp/#installation)
Before we get started, you'll need to install Node and Yarn or npm, and create a directory for your project. Then, install Parcel into your app using Yarn:

`yarn add --dev parcel`
Or when using npm run:

`npm install --save-dev parcel`
Project setup
-------------

[#](https://parceljs.org/getting-started/webapp/#project-setup)
Now that Parcel is installed, let’s create some source files for our app. Parcel accepts any type of file as an entry point, but an HTML file is a good place to start. Parcel will follow all of your dependencies from there to build your app.

_src/index.html:_

`<!doctype html><html lang="en">  <head>    <meta charset="utf-8"/>    <title>My First Parcel App</title>  </head>  <body>    <h1>Hello, World!</h1>  </body></html>`

Parcel has a development server built in, which will automatically rebuild your app as you make changes. To start it, run the `parcel` CLI pointing to your entry file:

`yarn parcel src/index.html`
Or when using npm run:

`npx parcel src/index.html`
Now open [http://localhost:1234/](http://localhost:1234/) in your browser to see the HTML file you created above.

Next, you can start adding dependencies to your HTML file, such as a JavaScript or CSS file. For example, you could create a `styles.css` file and reference it from your `index.html` file with a `<link>` tag, and an `app.js` file referenced with a `<script>` tag.

_src/styles.css:_

`h1 {  color: hotpink;  font-family: cursive;}`

_src/app.js:_

`console.log('Hello world!');`

_src/index.html:_

`<!doctype html><html lang="en">  <head>    <meta charset="utf-8"/>    <title>My First Parcel App</title>    <link rel="stylesheet" href="styles.css" />    <script type="module" src="app.js"></script>  </head>  <body>    <h1>Hello, World!</h1>  </body></html>`

As you make changes, you should see your app automatically update in the browser without even refreshing the page!

In this example, we’ve shown how to use vanilla HTML, CSS, and JavaScript, but Parcel also works with many common web frameworks and languages like [React](https://parceljs.org/recipes/react/) and [TypeScript](https://parceljs.org/languages/typescript/) out of the box. Check out the Recipes and Languages sections of the docs to learn more.

Package scripts
---------------

[#](https://parceljs.org/getting-started/webapp/#package-scripts)
So far, we’ve been running the `parcel` CLI directly, but it can be useful to create some scripts in your `package.json` file to make this easier. We'll also setup a script to build your app for [production](https://parceljs.org/features/production/) using the `parcel build` command. Finally, you can also declare your [entries](https://parceljs.org/features/targets/#entries) in a single place using the `source` field so you don't need to duplicate them in each `parcel` command.

_package.json:_

`{  "name": "my-project",  "source": "src/index.html",  "scripts": {    "start": "parcel",    "build": "parcel build"  },  "devDependencies": {    "parcel": "latest"  }}`

Now you can run `yarn build` to build your project for production and `yarn start` to start the development server.

Declaring browser targets
-------------------------

[#](https://parceljs.org/getting-started/webapp/#declaring-browser-targets)
By default Parcel does not perform any code transpilation. This means that if you write your code using modern language features, that’s what Parcel will output. You can declare your app’s supported browsers using the `browserslist` field. When this field is declared, Parcel will transpile your code accordingly to ensure compatibility with your supported browsers.

_package.json:_

`{  "name": "my-project",  "source": "src/index.html",  "browserslist": "> 0.5%, last 2 versions, not dead",  "scripts": {    "start": "parcel",    "build": "parcel build"  },  "devDependencies": {    "parcel": "latest"  }}`

You can learn more about targets, as well as Parcel’s automatic support for differential bundling on the [Targets](https://parceljs.org/features/targets/) page.

Next steps
----------

[#](https://parceljs.org/getting-started/webapp/#next-steps)
Now that you’ve set up your project, you're ready to learn about some more advanced features of Parcel. Check out the documentation about [development](https://parceljs.org/features/development/) and [production](https://parceljs.org/features/production/), and see the Recipes and Languages sections for more in-depth guides using popular web frameworks and tools.
