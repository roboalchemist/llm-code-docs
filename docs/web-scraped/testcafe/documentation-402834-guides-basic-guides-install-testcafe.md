# Source: https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe

Title: Install TestCafe | Basic Guides | Guides

URL Source: https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe

Markdown Content:
Note

Use the [TestCafe Setup Wizard](https://testcafe.io/documentation/404259/guides/best-practices/create-testcafe) to quickly bootstrap your TestCafe project. You can always adjust your setup afterwards.

[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#article-summary)Article Summary[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#article-summary)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The easiest way to install TestCafe is to use the node package manager. The following command creates a global installation of TestCafe, accessible anywhere on your machine:

```
npm i -g testcafe
```

Omit the `-g` flag to create a local installation. Use the `--save-dev` flag to add testcafe to the dependencies list.

Yarn users can install TestCafe with [yarn](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#install-testcafe-with-yarn). If you want to contribute to the development of the framework, you can [build TestCafe from source](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#install-testcafe-from-source).

[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#table-of-contents)Table of Contents[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#table-of-contents)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Prerequisites](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#prerequisites)
*   [Installation methods overview](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#installation-methods-overview)
*   [Install TestCafe from NPM](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#install-testcafe-from-npm)
*   [Install TestCafe with Yarn](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#install-testcafe-with-yarn)
*   [Install TestCafe from source](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#install-testcafe-from-source)
*   [Ad Hoc installation](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#ad-hoc-installation)
*   [Installation conflicts](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#installation-priority-and-conflicts)
*   [macOS permissions](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#macos-permissions)

[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#prerequisites)Prerequisites[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#prerequisites)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#nodejs)Node.js[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#nodejs)

The TestCafe framework requires an up-to-date version of the [Node.js](https://nodejs.org/en) runtime. Execute the following shell command to confirm that you run a [recent version](https://github.com/nodejs/release#release-schedule) of Node.js:

```
node --version
```

[Install Node.js](https://nodejs.org/en/download) if necessary.

### [](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#npm)NPM[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#npm)

You need the `npm` command-line utility to [install TestCafe from the NPM repository](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#install-testcafe-from-npm) or [run an ad hoc](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#ad-hoc-installation) installation of TestCafe.

Most Node.js installers include the `npm` command-line utility out of the box. Make sure that your setup includes an [up-to-date version](https://www.npmjs.com/package/npm) of `npm`:

```
npm --version
```

Update `npm` if it is out of date:

```
npm install -g npm@latest
```

Install `npm` if it is absent:

```
curl -qL https://www.npmjs.com/install.sh | sh
```

### [](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#screenshot-prerequisites)Screenshot prerequisites[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#screenshot-prerequisites)

You may need to install extra software to [take screenshots](https://testcafe.io/documentation/402840/guides/intermediate-guides/screenshots-and-videos).

If you run **Windows**, [install .NET 4.0](https://dotnet.microsoft.com/en-us/download) or newer.

If you run **Linux**, make sure that your environment contains an [ICCCM/EWMH-compliant window manager](https://en.wikipedia.org/wiki/Comparison_of_X_window_managers).

**macOS** users can take screenshots out of the box.

### [](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#video-prerequisites)Video prerequisites[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#video-prerequisites)

TestCafe uses [ffmpeg](https://ffmpeg.org/) to record videos.

The easiest way to install `ffmpeg` is to run the [@ffmpeg-installer/ffmpeg](https://www.npmjs.com/package/@ffmpeg-installer/ffmpeg) utility:

```
npm install --save @ffmpeg-installer/ffmpeg
```

Consult the official website for [alternative installation instructions](https://ffmpeg.org/download.html).

#### [](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#ffmpeg-troubleshooting)FFmpeg troubleshooting[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#ffmpeg-troubleshooting)

Perform the following actions if TestCafe cannot detect the `ffmpeg` binary:

*   Specify the path to the FFMpeg folder in the `PATH` environment variable.
*   Specify the path to the FFmpeg executable in the `FFMPEG_PATH` environment variable.
*   Reinstall the `ffmpeg` binary with the [@ffmpeg-installer/ffmpeg](https://www.npmjs.com/package/@ffmpeg-installer/ffmpeg) utility.

[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#installation-methods-overview)Installation methods overview[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#installation-methods-overview)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#npm-1)NPM[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#npm-1)

The easiest way to install TestCafe is to [use the npm package management utility](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#install-testcafe-from-npm). NPM is the most popular [package repository](https://www.npmjs.com/) for the Node.js ecosystem. The TestCafe team uploads ready-to-use builds of the framework to this repository. You can use the `npm` command-line tool to install and manage Node.js packages, including TestCafe.

NPM can create a [system-wide installation](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#system-wide-installation) or [add TestCafe as a project dependency](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#local-installation).

If you’re unsure which option to pick, use [system-wide installation](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#system-wide-installation). Global installation allows you to use a single version of TestCafe for all your projects.

A [local installation](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#local-installation) is a great fit for continuous integration systems and Node.js applications. It allows you to install the entirety of your project dependencies, including TestCafe, with a single `npm install` command. You can use different _local_ versions of TestCafe in different projects.

### [](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#yarn)Yarn[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#yarn)

[Yarn](https://yarnpkg.com/) is an alternative Node.js package manager. If you already use `yarn`, you can [use it](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#install-testcafe-with-yarn) to install `testcafe`.

### [](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#source-code)Source Code[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#source-code)

If you want to test the development version of TestCafe, or contribute code to the project, [install the framework from source](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#install-testcafe-from-source).

### [](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#ad-hoc)Ad Hoc[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#ad-hoc)

If you cannot create a permanent installation of TestCafe, use the `npx` command to run TestCafe tests [on the fly](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#ad-hoc-installation).

[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#install-testcafe-from-npm)Install TestCafe from npm[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#install-testcafe-from-npm)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#system-wide-installation)System-wide installation[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#system-wide-installation)

Run the following command to install the `testcafe` package system-wide:

```
npm install -g testcafe
```

### [](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#local-installation)Local Installation[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#local-installation)

Run the following command to install TestCafe into your current working directory and save it to the dependencies list.

```
npm install --save-dev testcafe
```

[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#install-testcafe-with-yarn)Install TestCafe with yarn[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#install-testcafe-with-yarn)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.   If your setup does not contain `yarn`, follow the [official installation guide](https://yarnpkg.com/getting-started/install).
2.   Navigate to a directory with an initialized yarn project, or initialize a new project:

```
yarn init
```
3.   Add `testcafe` to your project dependencies:

```
yarn add -D testcafe
```

[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#install-testcafe-from-source)Install TestCafe from source[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#install-testcafe-from-source)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The installation process consists of two steps:

1.   [Build TestCafe](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#build-testcafe)
2.   [Install the build](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#install-the-build)

### [](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#build-testcafe)Build TestCafe[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#build-testcafe)

Note

The TestCafe team stores the framework’s source code in a [public git repository](https://github.com/devexpress/testcafe). Install and configure [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to work with the TestCafe repository.

1.   [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the [TestCafe repository](https://github.com/DevExpress/testcafe):

```
git clone git@github.com:DevExpress/testcafe.git
```
2.   Navigate to the root directory of the repository. Install project dependencies with the following shell command:

```
npm install
```
3.   Build the project with the following shell command:

```
npx gulp build
```

### [](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#install-the-build)Install the build[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#install-the-build)

Install the build in one of the following two ways:

#### [](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#npm-link)npm link[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#npm-link)

The `npm link` method suits most testers and contributors. It allows you to use TestCafe while you make changes to the framework’s code.

The `npm link` command creates a [symbolic link](https://en.wikipedia.org/wiki/Symbolic_link) between the TestCafe directory and your project.

1.   Navigate to the root directory of the repository and run the following shell command:

```
npm link
```
2.   Navigate to the directory that contains your test files and run the following shell command:

```
npm link testcafe
```

#### [](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#npm-pack)npm pack[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#npm-pack)

1.   Run the following shell command to [package](https://docs.npmjs.com/cli/v7/commands/npm-pack/) the framework:

```
npm pack
```

This command creates a `name-version.tgz` package in the `testcafe` folder.

2.   Run the following shell command to install the package system-wide. Replace the `path/to/package.tgz` section with the actual path to the package.

```
npm install -g path/to/package.tgz
```

Note

The `/lib` directory stores build artifacts. Build tasks remove this folder before they run. To remove this directory manually, run the following command:

```
gulp clean
```

[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#ad-hoc-installation)Ad Hoc Installation[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#ad-hoc-installation)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Ad hoc installation tools allow you to run rarely used packages without adding them to your project dependencies. Most TestCafe users should only resort to this measure if no other installation method is feasible.

Use the [npx](https://www.npmjs.com/package/npx) utility to run TestCafe without a permanent installation.

```
npx testcafe chrome test.js
```

The `npx` command creates a temporary installation of TestCafe and all its dependencies. When you end the `testcafe` process, the installation disappears. The next time you run `npx`, it downloads and installs the TestCafe package all over again.

[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#installation-priority-and-conflicts)Installation priority and conflicts[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#installation-priority-and-conflicts)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you installed the `testcafe` package [globally](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#system-wide-installation), but your current working directory contains a [local TestCafe installation](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#local-installation), the `testcafe` command launches the local version of the framework.

If in doubt, double-check the version of the framework and the installation type with the following command:

```
testcafe -v
```

![Image 1: Install TestCafe](https://testcafe.io/images/version-check.png)

[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#macos-permissions)macOS Permissions[](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe#macos-permissions)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Main article: [Grant or Fix TestCafe Permissions on macOS](https://testcafe.io/documentation/404111/recipes/debugging/macos-permissions)

In macOS v10.15 and up, the operating system imposes new restrictions on applications that automate browsers and perform screen capture. For TestCafe to work, you need to explicitly grant permissions to the framework.

When you launch TestCafe for the first time, macOS asks you to grant _TestCafe Browser Tools_ screen recording permission. Click the **Open System Preferences** button and check the **TestCafe Browser Tools** box to grant this permission.

![Image 2: Screen Recording Permissions](https://testcafe.io/images/recording-permissions.png)

When you update TestCafe, macOS may reset its security permissions. If that happens, the system repeats the permission prompt the next time you launch TestCafe.

When the **Security and Privacy** dialog opens, uncheck the **TestCafe Browser Tools** check box and check it again.

![Image 3: Screen Recording Permissions](https://testcafe.io/images/recording-permission-system-settings.png)
