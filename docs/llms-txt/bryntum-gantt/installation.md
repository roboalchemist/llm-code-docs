# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/npm/repository/installation.md

﻿# Installation and usage

## Installing trial packages

Trial packages require using npm package aliasing to install the `"@bryntum/gantt-trial"` using
the `"@bryntum/gantt"` alias.

<div class="note">

The trial Bryntum Gantt package should be installed first

</div>

Example for Angular framework integration using package manager of your choice:

<div class="docs-tabs" data-name="packagemanager">
<div>
    <a>npm</a>
    <a>yarn</a>
</div>
<div>

```shell
npm install @bryntum/gantt@npm:@bryntum/gantt-trial@7.2.1
npm install @bryntum/gantt-angular@7.2.1
```

<div class="note">

We recommend to use npm <code>--save-exact</code> arguments to install the precise package versions and take upgrades fully under
control.

</div>

</div>
<div>

```shell
yarn add @bryntum/gantt@npm:@bryntum/gantt-trial@7.2.1
yarn add @bryntum/gantt-angular@7.2.1
```

<div class="note">

We recommend using yarn <code>--exact</code> argument to install the specific package versions and keep upgrades fully under
control.

</div>
</div>
</div>

Alternatively, you can directly add entries to the `"dependencies"` section of the `package.json` project file as
follows:

```json
"dependencies": {
  "@bryntum/gantt": "npm:@bryntum/gantt-trial@7.2.1",
  "@bryntum/gantt-angular": "7.2.1"
}
```

<div class="note">

We recommend against prefixing package versions with the caret character (<code>^</code>) to install the precise package versions
and take upgrades fully under control.

</div>

To install Bryntum trial products use the trial product packages `@bryntum/grid-trial`, `@bryntum/gantt-trial`,
`@bryntum/scheduler-trial`, `@bryntum/schedulerpro-trial`, `@bryntum/calendar-trial` or `@bryntum/taskboard-trial`.

<div class="note">

To avoid compatibility issues, please make sure that you use the same version for all installed Bryntum product
packages.

</div>

Packages for other frameworks are listed in the
[Framework wrappers](#Gantt/guides/npm/repository/components.md#frameworks-wrappers) table.

## Trial packages dependencies

Trial packages depend on a corresponding `@bryntum/gantt-lib-trial` package (e.g., `@bryntum/grid-lib-trial`) which
contains the trial license.

The `@bryntum/gantt-lib-trial` packages are different in public (**npmjs.com**) and private Bryntum repositories.
If you switch between repositories, run a project cleanup including npm cache cleaning as described in the
[Project cleanup](#Gantt/guides/npm/repository/troubleshooting.md#project-cleanup) guide.

## Installing licensed packages

All published packages in the private Bryntum npm repository can be installed as any other regular npm packages.

Example: For Angular framework integration it can be done with:

Install using package manager of your choice:

<div class="docs-tabs" data-name="packagemanager">
<div>
    <a>npm</a>
    <a>yarn</a>
</div>
<div>

```shell
npm install @bryntum/gantt@7.2.1
npm install @bryntum/gantt-angular@7.2.1
```

<div class="note">

We recommend to use npm <code>--save-exact</code> arguments to install the specific package versions and keep upgrades fully under
control.

</div>

</div>
<div>

```shell
yarn add @bryntum/gantt@7.2.1
yarn add @bryntum/gantt-angular@7.2.1
```

<div class="note">

We recommend to use yarn <code>--exact</code> arguments to install the specific package versions and keep upgrades fully under
control.

</div>
</div>
</div>

Alternatively, you can directly add entries to the `"dependencies"` section of the `package.json` project file as
follows:

```json
"dependencies": {
  "@bryntum/gantt": "7.2.1",
  "@bryntum/gantt-angular": "7.2.1"
}
```

<div class="note">

We recommend not to prefix package versions with caret character (<code>^</code>) to install the precise package versions and
take upgrades fully under control.

</div>

To install Bryntum products use the product packages `@bryntum/grid`, `@bryntum/gantt`, `@bryntum/scheduler`,
`@bryntum/schedulerpro`, `@bryntum/calendar` or `@bryntum/taskboard`.

<div class="note">

To avoid compatibility issues make sure that you use the same version for all installed Bryntum product packages.

</div>

Packages for other frameworks are listed in the
[Framework wrappers](#Gantt/guides/npm/repository/components.md#frameworks-wrappers) table.

## Weekend nightly builds

Bryntum provides weekend nightly builds of its packages on the Bryntum npm server. Nightly builds are automatically
generated and reflect the latest development state, allowing developers to test upcoming fixes or features before the
official release.

Weekend nightly versions follow the format:

```shell
X.Y.Z-nightly.YYYYMMDD
```

- X.Y.Z - the main version number
- nightly - indicates that this is a nightly build
- YYYYMMDD - the date the package was published

```shell
6.1.8-nightly.20250330
```

This corresponds to version `6.1.8` built on March 30, 2025.

You can view all available versions of a package, including nightly builds, using the following command:

```shell
npm show @bryntum/gantt versions
```

This will output a list of all published versions. Nightly builds can be identified by the -nightly suffix. To install
a specific nightly version of a package, run:

```shell
npm install @bryntum/gantt@6.1.8-nightly.20250330
```

## Migrating from trial to licensed packages

The benefit of using npm package aliasing for trial packages is that we create an alias for the `gantt-trial` package
using the name of the licensed `gantt` package. This means there is no need to change your application code after
purchasing a license. You only need to update the alias in `package.json` to the licensed package version number.

Please follow these steps:

1. Log in to the Bryntum npm repository using your licensed Customer Zone account as described in the
   [Login](#Gantt/guides/npm/repository/private-repository-access.md#login) guide

2. Update the package entries in your `package.json` file

From:

```json
"dependencies": {
  "@bryntum/gantt": "npm:@bryntum/gantt-trial@7.2.1"
}
```

To:

```json
"dependencies": {
  "@bryntum/gantt": "7.2.1"
}
```

1. Perform a project cleanup as described in the [Project cleanup](#Gantt/guides/npm/repository/troubleshooting.md#project-cleanup)
   guide

<div class="note">

<strong>Framework Wrappers</strong> and <strong>Bryntum Demo Resources</strong> packages do not have trial versions.

</div>
