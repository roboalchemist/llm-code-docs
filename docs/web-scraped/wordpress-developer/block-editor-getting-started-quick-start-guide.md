# Quick Start Guide

**Source:** [https://developer.wordpress.org/block-editor/getting-started/quick-start-guide/](https://developer.wordpress.org/block-editor/getting-started/quick-start-guide/)



# Quick Start Guide




## In this article


Table of Contents- Scaffold the block plugin
- Basic usage
- View the block in action
- Additional resources



↑Back to top


This guide is designed to demonstrate the basic principles of block development in WordPress using a hands-on approach. Following the steps below, you will create a custom block plugin that uses modern JavaScript (ESNext and JSX) in a matter of minutes. The example block displays the copyright symbol (©) and the current year, the perfect addition to any website’s footer. You can see these steps in action through this short video demonstration.



## Scaffold the block plugin


Start by ensuring you have Node.js andnpminstalled on your computer. Review theNode.js development environmentguide if not.


Next, use the@wordpress/create-blockpackage and the@wordpress/create-block-tutorial-templatetemplate to scaffold the complete “Copyright Date Block” plugin.



    You can use `create-block` to scaffold a block just about anywhere and then use [wp-env](https://developer.wordpress.org/block-editor/getting-started/devenv/get-started-with-wp-env/) inside the generated plugin folder. This will create a local WordPress development environment with your new block plugin installed and activated.

    If you already have your own [local WordPress development environment](https://developer.wordpress.org/block-editor/getting-started/devenv/#local-wordpress-environment), navigate to the `plugins/` folder using the terminal.

Choose the folder where you want to create the plugin, and then execute the following command in the terminal from within that folder:


```
npx @wordpress/create-block copyright-date-block --template @wordpress/create-block-tutorial-template

```


Theslugprovided (copyright-date-block) defines the folder name for the scaffolded plugin and the internal block name.


Navigate to the Plugins page of your local WordPress installation and activate the “Copyright Date Block” plugin. The example block will then be available in the Editor.


## Basic usage


With the plugin activated, you can explore how the block works. Use the following command to move into the newly created plugin folder and start the development process.


```
cd copyright-date-block && npm start

```


Whencreate-blockscaffolds the block, it installswp-scriptsand adds the most common scripts to the block’spackage.jsonfile. Refer to theGet started with wp-scriptsarticle for an introduction to this package.


Thenpm startcommand will start a development server and watch for changes in the block’s code, rebuilding the block whenever modifications are made.


When you are finished making changes, run thenpm run buildcommand. This optimizes the block code and makes it production-ready.


## View the block in action


You can use any local WordPress development environment to test your new block, but the scaffolded plugin includes configuration forwp-env. You must haveDockeralready installed and running on your machine, but if you do, run thenpx wp-env startcommand.


Once the script finishes running, you can access the local environment at:http://localhost:8888. Log into the WordPress dashboard using usernameadminand passwordpassword. The plugin will already be installed and activated. Open the Editor or Site Editor, and insert the Copyright Date Block as you would any other block.


Visit theGetting startedguide to learn more aboutwp-env.


## Additional resources


- Get started with create-block
- Get started with wp-scripts
- Get started with wp-env





First published


November 13, 2023


Last updated


April 29, 2024


Edit article


Improve it on GitHub: Quick Start Guide





[PreviousGet started with wp-scriptsPrevious: Get started with wp-scripts](https://developer.wordpress.org/block-editor/getting-started/devenv/get-started-with-wp-scripts/)
[NextTutorial: Build your first blockNext: Tutorial: Build your first block](https://developer.wordpress.org/block-editor/getting-started/tutorial/)


