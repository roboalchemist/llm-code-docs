# Source: https://docs.expo.dev/eas/workflows/get-started

---
modificationDate: February 26, 2026
title: Get started with EAS Workflows
description: Learn how to use EAS Workflows to automate your React Native CI/CD development and release processes.
---

# Get started with EAS Workflows

Learn how to use EAS Workflows to automate your React Native CI/CD development and release processes.

This page walks you through the process of creating your first EAS Workflow for building and submitting your app to the app stores.

## Get started

Prerequisites

4 requirements

1.

Sign up for an Expo account

You'll need to [sign up](https://expo.dev/signup) for an Expo account.

2.

Create a project

You'll need to create a project with the following command:

```sh
npx create-expo-app@latest --template default@sdk-55
```

3.

Sync the project with EAS

You'll need to sync the project with EAS with the following command. This will create an EAS project and link it to your local project:

```sh
npx eas-cli@latest init
```

4.

Add eas.json

You'll need to add an `eas.json` file to the root of your project if it doesn't already exist:

```sh
touch eas.json && echo "{}" > eas.json
```

Create a directory named **.eas/workflows** at the root of your project with a YAML file inside of it. For example: **.eas/workflows/create-production-builds.yml**.

`my-app`

 `.eas`

  `workflows`

   `create-production-builds.yml`

 `eas.json`

Add the following YAML to the `create-production-builds.yml` file:

```yaml
name: Create Production Builds

jobs:
  build_android:
    type: build # This job type creates a production build for Android
    params:
      platform: android
  build_ios:
    type: build # This job type creates a production build for iOS
    params:
      platform: ios
```

The workflow above will create a production build for Android and iOS in parallel. To run this workflow successfully, you'll need to [set up and build your project using EAS CLI](/build/setup) first.

Finally, run the workflow with the following command:

```sh
npx eas-cli@latest workflow:run create-production-builds.yml
```

Once you do, you can see your workflow running on your project's [workflows page](https://expo.dev/accounts/%5Baccount%5D/projects/%5BprojectName%5D/workflows).

## More

### Automate workflows with GitHub events

You can trigger a workflow by pushing a commit to your GitHub repository. You can link a GitHub repo to your EAS project with the following steps:

-   Navigate to your project's [GitHub settings](https://expo.dev/accounts/%5Baccount%5D/projects/%5BprojectName%5D/github).
-   Follow the UI to install the GitHub app.
-   Select the GitHub repository that matches the Expo project and connect it.

Then, add the [`on` trigger](/eas/workflows/syntax#on) to your workflow file. For example, if you want to trigger the workflow when a commit is pushed to the `main` branch, you can add the following:

```yaml
name: Create Production Builds

on:
  push:
    branches: ['main']

  jobs:
    build_android:
      type: build
      params:
        platform: android
    build_ios:
      type: build
```

### VS Code extension

Download the [Expo Tools VS Code extension](https://marketplace.visualstudio.com/items?itemName=expo.vscode-expo-tools) to get descriptions and autocompletions for your workflow files.

> Got feedback or feature requests? Send us an email at [workflows@expo.dev](mailto:workflows@expo.dev).
