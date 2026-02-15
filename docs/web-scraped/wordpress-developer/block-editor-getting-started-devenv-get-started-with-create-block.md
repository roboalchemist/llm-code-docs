# Get started with create-block

**Source:** [https://developer.wordpress.org/block-editor/getting-started/devenv/get-started-with-create-block/](https://developer.wordpress.org/block-editor/getting-started/devenv/get-started-with-create-block/)



# Get started with create-block




## In this article


Table of Contents- Quick startInstallationBasic usage
- Alternate implementationsInteractive modeQuick start mode using optionsUsing templates
- Additional resources



↑Back to top


Custom blocks for the Block Editor in WordPress are typically registered using plugins and are defined through a specific set of files. The@wordpress/create-blockpackage is an officially supported tool to scaffold the structure of files needed to create and register a block. It generates all the necessary code to start a project and integrates a modern JavaScript build setup (usingwp-scripts) with no configuration required.


The package is designed to help developers quickly set up a block development environment following WordPress best practices.


## Quick start


### Installation


Start by ensuring you have Node.js andnpminstalled on your computer. Review theNode.js development environmentguide if not.


You can usecreate-blockto scaffold a block just about anywhere and thenusewp-envfrom the inside of the generated plugin folder. This will create a local WordPress development environment with your new block plugin installed and activated.


If you have your ownlocal WordPress development environmentalready set up, navigate to theplugins/folder using the terminal.


Run the following command to scaffold an example block plugin:


```
npx @wordpress/create-block@latest todo-list
cd todo-list

```


Theslugprovided (todo-list) defines the folder name for the scaffolded plugin and the internal block name.


Navigate to the Plugins page of our local WordPress installation and activate the “Todo List” plugin. The example block will then be available in the Editor.


### Basic usage


Thecreate-blockassumes you will use modern JavaScript (ESNext and JSX) to build your block. This requires a build step to compile the code into a format that browsers can understand. Luckily, thewp-scriptspackage handles this process for you. Refer to theGet started with wp-scriptsfor an introduction to this package.


Whencreate-blockscaffolds the block, it installswp-scriptsand adds the most common scripts to the block’spackage.jsonfile. By default, those include:


```
{
    "scripts": {
        "build": "wp-scripts build",
        "format": "wp-scripts format",
        "lint:css": "wp-scripts lint-style",
        "lint:js": "wp-scripts lint-js",
        "packages-update": "wp-scripts packages-update",
        "plugin-zip": "wp-scripts plugin-zip",
        "start": "wp-scripts start"
    }
}

```


These scripts can then be run using the commandnpm run {script name}. The two scripts you will use most often arestartandbuildsince they handle the build step.


When working on your block, use thenpm run startcommand. This will start a development server and automatically rebuild the block whenever any code change is detected.


When you are ready to deploy your block, use thenpm run buildcommand. This optimizes your code and makes it production-ready.


See thewp-scriptspackage documentationfor more details about each available script.


## Alternate implementations


### Interactive mode


For developers who prefer a more guided experience, thecreate-blockpackage provides an interactive mode. Instead of manually specifying all options upfront, like theslugin the above example, this mode will prompt you for inputs step-by-step.


To use this mode, run the command:


```
npx @wordpress/create-block@latest

```


Follow the prompts to configure your block settings interactively.


### Quick start mode using options


If you’re already familiar with thecreate-blockoptionsand want a more streamlined setup, you can use quick start mode. This allows you to pass specific options directly in the command line, eliminating the need for interactive prompts.


For instance, to quickly create a block named “my-block” with a namespace of “my-plugin” that is a Dynamic block, use this command:


```
npx @wordpress/create-block@latest --namespace="my-plugin" --slug="my-block" --variant="dynamic"

```


### Using templates


Thecreate-blockpackage also supports the use of templates, enabling you to create blocks based on predefined configurations and structures. This is especially useful when you have a preferred block structure or when you’re building multiple blocks with similar configurations.


To use a template, specify the--templateoption followed by the template name or path:


```
npx @wordpress/create-block --template="my-custom-template"

```


Templates must be set up in advance so thecreate-blockpackage knows where to find them. Learn more in thecreate-blockdocumentation, and review theExternal Project Templatesguide.


## Additional resources


- Using the create-block tool(Learn WordPress tutorial)
- @wordpress/create-block(Official documentation)
- @wordpress/scripts(Official documentation)





First published


October 17, 2023


Last updated


January 16, 2024


Edit article


Improve it on GitHub: Get started with create-block





[PreviousGet started with wp-envPrevious: Get started with wp-env](https://developer.wordpress.org/block-editor/getting-started/devenv/get-started-with-wp-env/)
[NextGet started with wp-scriptsNext: Get started with wp-scripts](https://developer.wordpress.org/block-editor/getting-started/devenv/get-started-with-wp-scripts/)


