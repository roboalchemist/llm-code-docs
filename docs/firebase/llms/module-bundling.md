# Source: https://firebase.google.com/docs/web/module-bundling.md.txt

<br />

JavaScript module bundlers can do many things, but one of their most useful features is the ability to add and use external libraries in your code base. Module bundlers read import paths in your code and combine (bundle) your application-specific code with your imported library code.

From version 9 and higher, the Firebase JavaScript modular API is optimized to work with the optimization features of module bundlers to reduce the amount of Firebase code included in your final build.  

    import { initializeApp } from 'firebase/app';
    import { getAuth, onAuthStateChanged, getRedirectResult } from 'firebase/auth';

    const firebaseApp = initializeApp({ /* config */ });
    const auth = getAuth(firebaseApp);
    onAuthStateChanged(auth, user => { /* check status */ });

    /**
     * getRedirectResult is unused and should not be included in the code base.
     * In addition, there are many other functions within firebase/auth that are
     * not imported and therefore should not be included as well.
     */

This process of eliminating unused code from a library is known as tree shaking. It would be extremely time consuming and error prone to manually remove this code by hand, but module bundlers can automate this removal.

There are many high quality module bundlers in the JavaScript ecosystem. This guide is focused on covering using Firebase with[webpack](https://webpack.js.org/),[Rollup](https://rollupjs.org/), and[esbuild](https://esbuild.github.io/).

## Get started

This guide requires you to have npm installed in your development environment. npm is used to install and manage dependencies (libraries). To install npm,[install Node.js](https://nodejs.org/en/download/), which includes npm automatically.

Most developers are properly set up once they have installed Node.js. However, there are common problems many developers run into when setting up their environment. If you run into any errors,[make sure your environment has the npm CLI](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)and that you have the proper permissions set up so you[don't have to install packages as an administrator with the sudo command](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally).

### package.json and installing Firebase

Once you have npm installed you will need to create a`package.json`file at the root of your local project. Generate this file with the following npm command:  

    npm init

This will take you through a wizard to supply the needed information. Once the file is created it will look similar to the following:  

    {
      "name": "your-package-name",
      "version": "1.0.0",
      "description": "",
      "main": "index.js",
      "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1"
      },
      "keywords": [],
      "author": "",
      "license": "ISC",
      "dependencies": {

      }
    }

This file is responsible for many different things. This is an important file to familiarize yourself with if you want to learn more about module bundling and building JavaScript code in general. The important piece for this guide is the`"dependencies"`object. This object will hold a key value pair of the library you have installed and the version it is using.

Adding dependencies is done through the`npm install`or`npm i`command.  

    npm i firebase

When you run`npm i firebase`, the installation process will update`package.json`to list Firebase as a dependency:  

      "dependencies": {
        "firebase": "^9.0.0"
      },

The key is the name of the library and the value is the version to use. The version value is flexible and can accept a range of values. This is known as semantic versioning or semver. To learn more about semver,[see npm's guide about semantic versioning](https://docs.npmjs.com/about-semantic-versioning).

### Source vs build folders

The code you write is read and processed by a module bundler and then output as a new file or set of files. It's important to separate these two types of files. The code the module bundlers read and process is known as "source" code. The files they output are known as the built or "dist" (distribution) code.

A common setup in code bases is to store source code in a folder called`src`and the built code in a folder named`dist`.  

    - src
     |_ index.js
     |_ animations.js
     |_ datalist.js


    - dist
     |_ bundle.js

In the example file structure above, consider that`index.js`imports both`animations.js`and`datalist.js`. When a module bundler processes the source code it will produce the`bundle.js`file in the`dist`folder. The`bundle.js`is a combination of the files in the`src`folder and any libraries the import as well.

If you are using source control systems such as Git, it is common to ignore the`dist`folder when storing this code in the main repository.

### Entry points

Module bundlers all have a concept of an entry point. You can think of your application as a tree of files. One file imports code from another and so on and so forth. This means that one file will be the root of the tree. This file is known as the entry point.

Let's revisit the previous file structure example.  

    - src
     |_ index.js
     |_ animations.js
     |_ datalist.js


    - dist
     |_ bundle.js

    // src/index.js
    import { animate } from './animations';
    import { createList } from './datalist';

    // This is not real code, but for example purposes only
    const theList = createList('users/123/tasks');
    theList.addEventListener('loaded', event => {
      animate(theList);
    });

The`src/index.js`file is considered the entry point because it begins the imports of all the needed code for the application. This entry point file is used by module bundlers to begin the bundling process.

## Using Firebase with webpack

There is no specific configuration needed for Firebase apps and webpack. This section[covers a general webpack configuration](https://webpack.js.org/guides/getting-started/).

The first step is to install webpack from npm as a development dependency.  

    npm i webpack webpack-cli -D

Create a file at the root of your local project named`webpack.config.js`and add the following code.  

    const path = require('path');

    module.exports = {
      // The entry point file described above
      entry: './src/index.js',
      // The location of the build folder described above
      output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js'
      },
      // Optional and for development only. This provides the ability to
      // map the built code back to the original source format when debugging.
      devtool: 'eval-source-map',
    };

Then make sure you have Firebase installed as a dependency.  

    npm i firebase

Then initialize Firebase in your code base. The following code imports and initializes Firebase in an entry point file and uses Firestore Lite to load a "city" document.  

    // src/index.js
    import { initializeApp } from 'firebase/app';
    import { getFirestore, doc, getDoc } from 'firebase/firestore/lite';

    const firebaseApp = initializeApp({ /* config */ });
    const db = getFirestore(firebaseApp);

    async function loadCity(name) {
      const cityDoc = doc(db, `cities/${name}`);
      const snapshot = await getDoc(cityDoc);
      return {
        id: snapshot.id,
        ...snapshot.data(),
      };
    }

The next step is to[add an npm script](https://docs.npmjs.com/cli/v7/using-npm/scripts)to run the webpack build. Open the`package.json`file and add the following key value pair to the`"scripts"`object.  

      "scripts": {
        "build": "webpack --mode=development"
      },

To run webpack and generate the build folder run the following command.  

    npm run build

Finally, check the`dist`build folder. It should contain a file named`bundle.js`that contains your bundled application and dependency code.

For more information on optimizing your webpack build for production, see their official documentation on[the "mode" configuration setting](https://webpack.js.org/configuration/mode/).

## Using Firebase with Rollup

There is no specific configuration needed for Firebase apps and Rollup. This section covers a general Rollup configuration.

The first step is to install Rollup and a plugin used to map imports to dependencies installed with npm.  

    npm i rollup @rollup/plugin-node-resolve -D

Create a file at the root of your local project named`rollup.config.js`and add the following code.  

    import { nodeResolve } from '@rollup/plugin-node-resolve';

    export default {
      // the entry point file described above
      input: 'src/index.js',
      // the output for the build folder described above
      output: {
        file: 'dist/bundle.js',
        // Optional and for development only. This provides the ability to
        // map the built code back to the original source format when debugging.
        sourcemap: 'inline',
        // Configure Rollup to convert your module code to a scoped function
        // that "immediate invokes". See the Rollup documentation for more
        // information: https://rollupjs.org/guide/en/#outputformat
        format: 'iife'
      },
      // Add the plugin to map import paths to dependencies
      // installed with npm
      plugins: [nodeResolve()]
    };

Then initialize Firebase in your code base. The following code imports and initializes Firebase in an entry point file and uses Firestore Lite to load a "city" document.  

    // src/index.js
    import { initializeApp } from 'firebase/app';
    import { getFirestore, doc, getDoc } from 'firebase/firestore/lite';

    const firebaseApp = initializeApp({ /* config */ });
    const db = getFirestore(firebaseApp);

    async function loadCity(name) {
      const cityDoc = doc(db, `cities/${name}`);
      const snapshot = await getDoc(cityDoc);
      return {
        id: snapshot.id,
        ...snapshot.data(),
      };
    }

The next step is to[add an npm script](https://docs.npmjs.com/cli/v7/using-npm/scripts)to run the rollup build. Open the`package.json`file and add the following key value pair to the`"scripts"`object.  

      "scripts": {
        "build": "rollup -c rollup.config.js"
      },

To run rollup and generate the build folder, run the following command.  

    npm run build

Finally, check the`dist`build folder. It should contain a file named`bundle.js`that contains your bundled application and dependency code.

For more information on optimizing your Rollup build for production, see their official documentation[on plugins for production builds](https://rollupjs.org/guide/en/#outputplugins).

## Using Firebase with esbuild

There is no specific configuration needed for Firebase apps and esbuild. This section covers a general esbuild configuration.

The first step is to install esbuild as a development dependency.  

    npm i esbuild -D

Create a file at the root of your local project named`esbuild.config.js`and add the following code.  

    require('esbuild').build({
      // the entry point file described above
      entryPoints: ['src/index.js'],
      // the build folder location described above
      outfile: 'dist/bundle.js',
      bundle: true,
      // Replace with the browser versions you need to target
      target: ['chrome60', 'firefox60', 'safari11', 'edge20'],
      // Optional and for development only. This provides the ability to
      // map the built code back to the original source format when debugging.
      sourcemap: 'inline',
    }).catch(() => process.exit(1))

Then initialize Firebase in your code base. The following code imports and initializes Firebase in an entry point file and uses Firestore Lite to load a "city" document.  

    // src/index.js
    import { initializeApp } from 'firebase/app';
    import { getFirestore, doc, getDoc } from 'firebase/firestore/lite';

    const firebaseApp = initializeApp({ /* config */ });
    const db = getFirestore(firebaseApp);

    async function loadCity(name) {
      const cityDoc = doc(db, `cities/${name}`);
      const snapshot = await getDoc(cityDoc);
      return {
        id: snapshot.id,
        ...snapshot.data(),
      };
    }

The next step is to[add an npm script](https://docs.npmjs.com/cli/v7/using-npm/scripts)to run esbuild. Open the`package.json`file and add the following key value pair to the`"scripts"`object.  

      "scripts": {
        "build": "node ./esbuild.config.js"
      },

Finally, check the`dist`build folder. It should contain a file named`bundle.js`that contains your bundled application and dependency code.

For more information on optimizing esbuild for production, see their official documentation[on minification and other optimizations](https://esbuild.github.io/api/#minify).