# Block Development Environment

**Source:** [https://developer.wordpress.org/block-editor/getting-started/devenv/](https://developer.wordpress.org/block-editor/getting-started/devenv/)

## In this article

Table of Contents- Code editor

- Node.js development tools
- Local WordPress environment

↑Back to top

This guide will help you set up the right development environment to create blocks and other plugins that extend and modify the Block Editor in WordPress.

A block development environment includes the tools you need on your computer to successfully develop for the Block Editor. The three essential requirements are:

- Block Development EnvironmentCode editorNode.js development toolsLocal WordPress environment

```text
To contribute to the Gutenberg project itself, refer to the additional documentation in the [code contribution guide](https://developer.wordpress.org/block-editor/contributors/code/getting-started-with-code-contribution).

```

## Code editor

A code editor is used to write code. You can use whichever editor you’re most comfortable with. The key is having a way to open, edit, and save text files.

If you do not already have a preferred code editor,Visual Studio Code(VS Code) is a popular choice for JavaScript development among Core contributors. It works well across the three major platforms (Windows, Linux, and Mac), is open-source, and is actively maintained by Microsoft. VS Code also has a vibrant community providing plugins and extensions, including many for WordPress development.

## Node.js development tools

Node.js (node) is an open-source runtime environment that allows you to execute JavaScript outside of the web browser. While Node.js is not required for all WordPress JavaScript development, it’s essential when working with modern JavaScript tools and developing for the Block Editor.

Node.js and its accompanying development tools allow you to:

- Install and run WordPress packages needed for Block Editor development, such aswp-scripts
- Set up local WordPress environments withwp-envand@wp-playground/cli
- Use the latest ECMAScript features and write code in ESNext
- Lint, format, and test JavaScript code
- Scaffold custom blocks with thecreate-blockpackage

The list goes on. While modern JavaScript development can be challenging, WordPress provides several tools, likewp-scriptsandcreate-block, that streamline the process and are made possible by Node.js development tools.

The recommended Node.js version for block development isActive LTS(Long Term Support). However, there are times when you need to use different versions. A Node.js version manager tool likenvmis strongly recommended and allows you to change yournodeversion when required. You will also need Node Package Manager (npm) and the Node Package eXecute (npx) to work with some WordPress packages. Both are installed automatically with Node.js.

To be able to use the Node.js tools andpackages provided by WordPressfor block development, you’ll need to set a proper Node.js runtime environment on your machine. To learn more about how to do this, refer to the links below.

- Install Node.js for Mac and Linux
- Install Node.js for Windows

## Local WordPress environment

A local WordPress environment (site) provides a controlled, efficient, and secure space for development, allowing you to build and test your code before deploying it to a production site. The samerequirementsfor WordPress apply to local sites.

In the broader WordPress community, many tools are available for setting up a local WordPress environment on your computer. The Block Editor Handbook coverswp-env, which is open-source and maintained by the WordPress project itself. It’s also the recommended tool for Gutenberg development.

Refer to theGet started withwp-envguide for setup instructions.

```text

Throughout the Handbook, you may also see references to `@wp-playground/cli`. This is a lightweight tool powered by [WordPress Playground](https://developer.wordpress.org/playground/) that streamlines setting up a simple local WordPress environment. While still experimental, this tool is great for quickly testing WordPress releases, plugins, and themes.

```python

This list is not exhaustive, but here are several additional options to choose from if you prefer not to usewp-env:

- WordPress Studio
- Local
- XAMPP
- MAMP
- Varying Vagrant Vagrants(VVV)

First published

March 9, 2021

Last updated

August 6, 2025

Edit article

Improve it on GitHub: Block Development Environment

[PreviousGetting StartedPrevious: Getting Started](https://developer.wordpress.org/block-editor/getting-started/)
[NextNode.js development environmentNext: Node.js development environment](https://developer.wordpress.org/block-editor/getting-started/devenv/nodejs-development-environment/)
