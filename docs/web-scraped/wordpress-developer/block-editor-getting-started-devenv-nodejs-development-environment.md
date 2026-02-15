# Node.js development environment

**Source:** [https://developer.wordpress.org/block-editor/getting-started/devenv/nodejs-development-environment/](https://developer.wordpress.org/block-editor/getting-started/devenv/nodejs-development-environment/)



# Node.js development environment




## In this article


Table of Contents- Node.js installation on Mac and Linux (with nvm)
- Node.js installation on Windows and others
- Troubleshooting
- Additional resources



↑Back to top


When developing for the Block Editor, you will needNode.jsdevelopment tools along with a code editor and a local WordPress environment (seeBlock Development Environment). Node.js (node) is an open-source runtime environment that allows you to execute JavaScript code from the terminal (also known as a command-line interface, CLI, or shell)


Installingnodewill automatically include the Node Package Manager (npm) and the Node Package eXecute (npx), two tools you will frequently use in block and plugin development.


Node Package Manager (npm) serves multiple purposes, including dependency management and script execution. It’s the recommended package manager and is extensively featured in all documentation.


The Node Package eXecute (npx) tool is used to run commands from packages without installing them globally and is commonly used when scaffolding blocks with thecreate-blockpackage.


## Node.js installation on Mac and Linux (with nvm)


It’s recommended that you useNode Version Manager(nvm) to install Node.js. This allows you to install and manage specific versions ofnode, which are installed locally in your home directory, avoiding any global permission issues.


Here are the quick instructions for installingnodeusingnvmand setting the recommended Node.js version for block development. See thecomplete installation guidefor more details.


1. Open the terminal and run the following to installnvm. On macOS, the required developer tools are not installed by default. Install them if prompted.


```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash

```


1. Quit and restart the terminal.
1. Runnvm install --ltsin the terminal to install the latestLTS(Long Term Support) version of Node.js.
1. Runnode -vandnpm -vin the terminal to verify the installednodeandnpmversions.


If needed, you can also install specific versions ofnode. For example, install version 18 by runningnvm install 18, and switch between different versions by runningnvm use [version-number]. See thenvmusage guidefor more details.


Some projects, like Gutenberg, include an.nvmrcfile which specifies the version ofnodethat should be used. In this case, runningnvm usewill automatically select the correct version. If the version is not yet installed, you will get an error that tells you what version needs to be added. Runnvm install [version-number]followed bynvm use.


## Node.js installation on Windows and others


You candownload a Node.js installerdirectly from the main Node.js website. The latest version is recommended. Installers are available for Windows and Mac, and binaries are available for Linux.


Microsoft also provides adetailed guideon how to installnvmand Node.js on Windows and WSL.


## Troubleshooting


If you encounter the errorzsh: command not found: nvmwhen attempting to installnode, you might need to create the default profile file.


The default shell iszshon macOS, so create the profile file by runningtouch ~/.zshrcin the terminal. It’s fine to run if the file already exists. The default profile isbashfor Ubuntu, including WSL, so usetouch ~/.bashrcinstead. Then repeat steps 2-4.


The latestnodeversion should work for most development projects, but be aware that some packages and tools have specific requirements. If you encounter issues, you might need to install and use a previousnodeversion. Also, make sure to check if the project has an.nvmrcand use thenodeversion indicated.


## Additional resources


- Node.js(Official documentation)
- Node Version Manager(Official documentation)
- Installing Node.js and npm for local WordPress development(Learn WordPress tutorial)





First published


September 18, 2023


Last updated


January 16, 2024


Edit article


Improve it on GitHub: Node.js development environment





[PreviousBlock Development EnvironmentPrevious: Block Development Environment](https://developer.wordpress.org/block-editor/getting-started/devenv/)
[NextGet started with wp-envNext: Get started with wp-env](https://developer.wordpress.org/block-editor/getting-started/devenv/get-started-with-wp-env/)


