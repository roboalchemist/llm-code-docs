# Source: https://firebase.google.com/docs/functions/typescript.md.txt

<br />

For developers who prefer to write functions in TypeScript,Cloud Functionsprovides two types of support:

- Create and configure TypeScript projects for automatic transpilation at initialization (`firebase init functions`).
- Transpile existing TypeScript source to JavaScript at deploy time via a[predeploy hook](https://firebase.google.com/docs/cli#hooks).

Following instructions in this guide, you can migrate an existing JavaScript project to TypeScript and continue deploying functions using a predeploy hook to transpile your source code. TypeScript offers many benefits over vanilla JavaScript when writing functions:

- TypeScript supports latest JavaScript features like async/await, simplifying promise management
- ACloud Functionslinter highlights common problems while you're coding
- Type safety helps you avoid runtime errors in deployed functions

If you're new to TypeScript, see[TypeScript in 5 minutes](http://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html).

## Initializing a newCloud Functionsproject with TypeScript

Run`firebase init functions`in a new directory. The tool gives you options to build the project with JavaScript or TypeScript. Choose**TypeScript**to output the following project structure:  

    myproject
     +- functions/     # Directory containing all your functions code
          |
          +- package.json  # npm package file describing your Cloud Functions code
          |
          +- tsconfig.json
          |
          +- .eslintrc.js # Optional file if you enabled ESLint
          +- tsconfig.dev.json # Optional file that references .eslintrc.js
          |
          +- src/     # Directory containing TypeScript source
          |   |
          |   +- index.ts  # main source file for your Cloud Functions code
          |
          +- lib/
              |
              +- index.js  # Built/transpiled JavaScript code
              |
              +- index.js.map # Source map for debugging

Once initialization is complete, uncomment the sample in index.ts and run`npm run serve`to see a "Hello World" function in action.

## Using an existing TypeScript project

If you have an existing TypeScript project, you can add a predeploy hook to make sure your project is transpiled every time you deploy your code toCloud Functions for Firebase. You'll need a properly formed`tsconfig.json`file and a Firebase project, and you'll need to make the following modifications to your Firebase configuration:

1. Edit`package.json`to add a bash script to build your TypeScript project. For example:

        {
          "name": "functions",
          "scripts": {
            "build": "npm run lint && tsc"
          }
        ...

2. Edit`firebase.json`to add a predeploy hook to run the build script. For example:

        {
          "functions": {
            "predeploy": "npm --prefix functions run build",
          }
        }

With this configuration, a`firebase deploy --only functions`command builds your TypeScript code and deploys it as functions.

## Migrating an existing JavaScript project to TypeScript

If you have an existingCloud Functionsproject that you initialized and developed in JavaScript, you can migrate it to TypeScript. You're strongly encouraged to create a git checkpoint or other backup before starting.

**To migrate an existing JavaScriptCloud Functionsproject:**

1. Create a git checkpoint and save copies of your existing JavaScript source files.
2. In the project directory, run`firebase init functions`and select`TypeScript`when prompted for a language for writing functions.
3. When prompted whether to overwrite the existing`package.json`file, select**No**unless you are sure you don't want to keep the existing file.
4. Delete`index.ts`in the directory`functions/src`, replacing it with your existing source code.
5. In the`tsconfig.json`file created at initialization, set the compiler options to allow JavaScript:`"allowJs": true`.
6. Copy your saved`package.json`file into the`functions`directory, and edit it to set`"main"`to`"lib/index.js"`.
7. Also in`package.json`, add a build script for TypeScript like the following:

        {
          "name": "functions",
          "scripts": {
            "build": "npm run lint && tsc"
          }
        ...

8. Add`"typescript"`as a dev dependency by running`npm install --save-dev typescript @typescript-eslint/eslint-plugin @typescript-eslint/parser`.

9. For all dependencies, run`npm install --save @types/<dependency>`.

10. Rewrite source code from .js to .ts as desired.

## Emulating TypeScript functions

To test TypeScript functions locally, you can use the emulation tools described in[Run functions locally](https://firebase.google.com/docs/functions/local-emulator). It's important to compile your code before using these tools, so make sure to run`npm run build`inside your functions directory before running`firebase emulators:start`or`firebase functions:shell`. Alternatively, run`npm run serve`or`npm run shell`as a shortcut; these commands both run the build and serve/start the functions shell.

## Functions logs for TypeScript projects

During`firebase deploy`, your project's`index.ts`is transpiled to`index.js`, meaning that the Cloud Functions log will output line numbers from the`index.js`file and not the code you wrote. To make it easier for you to find the corresponding paths and line numbers in`index.ts`,`firebase deploy`creates`functions/lib/index.js.map`. You can use this source map in your preferred IDE or via a[node module](https://github.com/evanw/node-source-map-support).