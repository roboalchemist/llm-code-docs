# Source: https://firebase.google.com/docs/app-hosting/monorepos.md.txt

<br />

With monorepos, you can organize and manage multiple projects in a single directory. This guide describes how to get started deploying Turborepo or Nx-based apps withApp Hosting.

## Deploy monorepos with the Firebase console

Monorepo support is built into the graphical backend setup flow in the Firebase console. When prompted for a "Root directory" under "Deployment settings," specify the path to the application you want to deploy inside the monorepo:

![Screen shot of the console backend creation view](https://firebase.google.com/static/docs/app-hosting/images/app-hosting-configure-monorepo-console-example.png)

## Deploy monorepos with the Firebase CLI

Monorepo support is built into the backend setup flow invoked by the Firebase CLI command`apphosting:backends:create`. After you enter this flow and specify your chosen GitHub repository, you are prompted to specify your app's root directory relative to your repository; at this prompt, pass the path to the application you want to deploy inside the monorepo:  

    $ firebase apphosting:backends:create --project [project-name]
    i  === Import a GitHub repository
    â  Connected with GitHub successfully

    ? Which GitHub repo do you want to deploy? gh-username/nx-monorepo
    ? Specify your app's root directory relative to your repository path/to/app

For example, here are the assets that would be deployed given the following project structure and "target-app" as the application you want to build and deploy:  

### Nx

    .
        âââ libs
        âââ apps
        â   âââ target-app
        â       âââ project.json
        â       âââ src
        â           âââ ...
        âââ nx.json
        âââ package-lock.json
        âââ package.json

### Turborepo

    .
        âââ packages
        âââ apps
        â   âââ target-app
        â       âââ package.json
        â       âââ src
        â           âââ ...
        âââ turbo.json
        âââ package.json
        âââ package-lock.json

The app's root directory relative to your repository is`apps/target-app`.

## Troubleshooting monorepo deployment

- If you do not specify the "root directory" field for Nx, then the build will fail and display a message thatApp Hostingcannot find a project to target inside the Nx monorepo. Similarly, Turborepo users must specify a target app directory because there is no concept of a default project in Turborepo.
- For Nx + Angular applications, you must use the[Angular application builder](https://angular.io/guide/esbuild)to build the application. The Angular application builder is specified in`project.json`