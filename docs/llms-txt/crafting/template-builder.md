# Source: https://docs.sandboxes.cloud/docs/template-builder.md

## Template builder wizard

This page talks about how to use the template builder provided by Crafting to quickly setup ground work for a template.

To start a new template, click the `New Template` button on the `Templates` page

<Image align="center" className="border" border={true} src="https://files.readme.io/61e2b1d-admin-new-template.jpg" />

<Image align="center" className="border" border={true} src="https://files.readme.io/c248944-image.png" />

In this page, there lists a few ways to start building a template:

* **Using samples**: It's best fit for starting with some simple demo codebases with one frontend and one backend + database. It supports several common technologies to let you create a working template very quickly.
* **Template builder wizard**: It has a quick wizard to walk you through some basic steps. We will mainly talk about that in the rest of this section.
* **From scratch**: This option lets you directly get into the template builder with an empty template. You can directly change the yaml file based on the reference in [Sandbox Definition](https://docs.sandboxes.cloud/docs/sandbox-definition)

## Select source code repositories

<Image align="center" className="border" border={true} src="https://files.readme.io/feb6ea0-image.png" />

First step in the template builder wizard is to select source repos that you want to work on. With GitHub app integration, you can select the repos here directly. Without it, you can input the repo manually here and optionally select a default branch, like shown above.

Crafting can test whether the [Git Access](https://docs.sandboxes.cloud/docs/git-access) is set properly for the repos listed here. We recommend test the repo access before continue to next step.

## Select dependencies

<Image align="center" className="border" border={true} src="https://files.readme.io/8aa2d4e-image.png" />

After selecting source code repos, you can select what dependency services needed in your development environment. Crafting supports a number of commonly used services as built-in dependencies. For a complete built-in dependency list, please see the `Resources -> Dependencies` page.

If you are not able to find the dependency service you need, you can always added as a custom container later in the process. Please see [Setup containers and dependencies](https://docs.sandboxes.cloud/docs/containers-dependencies-setup) for more details.

## Select tool packages

<Image align="center" className="border" border={true} src="https://files.readme.io/744212b-image.png" />

The next step in the wizard is to select what tool packages such as (nodejs, jdk, etc.) to install on the workspaces. Installing them will override the system default. For your convenience, Crafting also has built-in support for a range of tool packages as listed in the page `Resources -> Packages`

If your code depends on other tool packages to setup and build, you have `sudo` permission on your workspace and you can always install them later via `sudo apt install` as needed and persist the setup. See [Setup workspaces](https://docs.sandboxes.cloud/docs/workspaces-setup) for more information.

Here you are asked to specify a name for the `Template Builder Sandbox` that is going to be created next to assist you building the template.

## Template builder sandbox

![Template Builder Sandbox](https://files.readme.io/3471945-image.png)

After clicking next from the last step of the wizard, Crafting system will create a `Template Builder Sandbox` (also known as `Standalone Sandbox`) for you, which should include all the settings you have input in the wizard, i.e., it will checkout the code, setup the dependencies, and install the tool packages. Please continue at [Standalone sandbox](https://docs.sandboxes.cloud/docs/standalone-sandbox) and [Setup workspaces](https://docs.sandboxes.cloud/docs/workspaces-setup) for instructions on next steps.
