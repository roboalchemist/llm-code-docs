# Source: https://devdocs.io/yarn~classic/configuration

Title: Yarn Classic / 1. Configuration — DevDocs

URL Source: https://devdocs.io/yarn~classic/configuration

Markdown Content:
Yarn Classic / 1. Configuration — DevDocs
===============

You're browsing the Yarn Classic documentation. To browse all docs, go to [devdocs.io](https://devdocs.io/) (or press `esc`).

Clear search
[DevDocs](https://devdocs.io/)
==============================

[Preferences](https://devdocs.io/settings)[Offline Data](https://devdocs.io/offline)[Changelog](https://devdocs.io/news)[Guide](https://devdocs.io/help)[About](https://devdocs.io/about)[Report a bug](https://github.com/freeCodeCamp/devdocs/issues/new/choose)

[1.22.17 Yarn](https://devdocs.io/yarn~classic/ "Yarn Classic")

[3 Getting Started](https://devdocs.io/yarn~classic-getting-started/)[43 CLI Commands](https://devdocs.io/yarn~classic-cli-commands/)[5 Configuration](https://devdocs.io/yarn~classic-configuration/)

[1. Configuration](https://devdocs.io/yarn~classic/configuration)[2. package.json](https://devdocs.io/yarn~classic/package-json)[3. envvars](https://devdocs.io/yarn~classic/envvars)[4. .yarnrc](https://devdocs.io/yarn~classic/yarnrc)[5. yarn.lock](https://devdocs.io/yarn~classic/yarn-lock)

[2 Configuring an Offline Mirror](https://devdocs.io/yarn~classic-configuring-an-offline-mirror/)[2 Creating a Package](https://devdocs.io/yarn~classic-creating-a-package/)[4 Dependencies and versions](https://devdocs.io/yarn~classic-dependencies-and-versions/)[1 Migrating from npm](https://devdocs.io/yarn~classic-migrating-from-npm/)[3 Overview](https://devdocs.io/yarn~classic-overview/)[6 The Yarn Workflow](https://devdocs.io/yarn~classic-the-yarn-workflow/)[1 Workspaces](https://devdocs.io/yarn~classic-workspaces/)

1. Configuration
================

Configuring your package
------------------------

Yarn looks for `package.json` files to identify each package and configure the behavior of yarn while running inside that package.

An example configuration for the `pet-kitten` package, which would be found at `pet-kitten/package.json`:

{
  "name": "pet-kitten",
  "version": "0.1.0",
  "main": "pet.js",
  "dependencies": {
    "hand": "1.0.0"
  }
}
Use `yarn.lock` to pin your dependencies
----------------------------------------

Yarn also uses a `yarn.lock` file in the root of your project to make dependency resolution fast and reliable. You never need to touch this file, yarn owns it and will change it when managing dependencies.

To make sure your app works consistently, **you should always save the `yarn.lock` file in your code repository.**

© 2016–present Yarn Contributors

Licensed under the BSD License.

[https://classic.yarnpkg.com/en/docs/configuration](https://classic.yarnpkg.com/en/docs/configuration)

 Back  Apply Docs Settings

##### Tracking cookies

We would like to gather usage data about how DevDocs is used through Google Analytics and Gauges. We only collect anonymous traffic information. Please confirm if you accept our tracking cookies. You can always change your decision in the settings.

[Accept](https://devdocs.io/yarn~classic/configuration#) or [Decline](https://devdocs.io/yarn~classic/configuration#)Close
