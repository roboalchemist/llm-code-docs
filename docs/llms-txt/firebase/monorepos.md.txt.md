# Source: https://firebase.google.com/docs/app-hosting/monorepos.md.txt

With monorepos, you can organize and manage multiple projects in a single
directory. This guide describes how to get started deploying Turborepo or
Nx-based apps with App Hosting.

## Deploy monorepos with the Firebase console

Monorepo support is built into the graphical backend setup flow in the Firebase
console. When prompted for a "Root directory" under "Deployment settings,"
specify the path to the application you want to deploy inside the monorepo:

![Screen shot of the console backend creation view](https://firebase.google.com/static/docs/app-hosting/images/app-hosting-configure-monorepo-console-example.png)

## Deploy monorepos with the Firebase CLI

Monorepo support is built into the backend setup flow invoked by the Firebase
CLI command `apphosting:backends:create`. After you enter this flow and specify
your chosen GitHub repository, you are prompted to specify your app's root
directory relative to your repository; at this prompt, pass the path to the
application you want to deploy inside the monorepo:

    $ firebase apphosting:backends:create --project [project-name]
    i  === Import a GitHub repository
    ✔  Connected with GitHub successfully

    ? Which GitHub repo do you want to deploy? gh-username/nx-monorepo
    ? Specify your app's root directory relative to your repository path/to/app

For example, here are the assets that would be deployed given the following
project structure and "target-app" as the application you want to build and
deploy:

### Nx

    .
        ├── libs
        ├── apps
        │   └── target-app
        │       ├── project.json
        │       └── src
        │           └── ...
        ├── nx.json
        ├── package-lock.json
        └── package.json

### Turborepo

    .
        ├── packages
        ├── apps
        │   └── target-app
        │       ├── package.json
        │       └── src
        │           └── ...
        ├── turbo.json
        ├── package.json
        └── package-lock.json

The app's root directory relative to your repository is `apps/target-app`.

## Troubleshooting monorepo deployment

- If you do not specify the "root directory" field for Nx, then the build will fail and display a message that App Hosting cannot find a project to target inside the Nx monorepo. Similarly, Turborepo users must specify a target app directory because there is no concept of a default project in Turborepo.
- For Nx + Angular applications, you must use the [Angular application
  builder](https://angular.io/guide/esbuild) to build the application. The Angular application builder is specified in `project.json`