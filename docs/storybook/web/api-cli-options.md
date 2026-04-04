# Storybook Documentation
# Source: https://storybook.js.org/docs/api/cli-options
# Page: /docs/api/cli-options

# CLI options

The Storybook command line interface (CLI) is the main tool you use to build and develop Storybook.

ℹ️

Storybook collects completely anonymous data to help us improve user experience. Participation is optional, and you may [opt-out](../configure/telemetry#how-to-opt-out) if you'd not like to share any information.

## 

CLI commands

All of the following documentation is available in the CLI by running `storybook --help`.

💡

Passing options to these commands works slightly differently if you're using npm instead of Yarn. You must prefix all of your options with `--`. For example, `npm run storybook build -- -o ./path/to/build --quiet`.

### 

`dev`

Compiles and serves a development build of your Storybook that reflects your source code changes in the browser in real-time. It should be run from the root of your project.
    
    
    storybook dev [options]

Options include:

Option| Description  
---|---  
`--help`| Output usage information.  
`storybook dev --help`  
`-V`, `--version`| Output the version number.  
`storybook dev -V`  
`-p`, `--port [number]`| Port to run Storybook.  
`storybook dev -p 9009`  
`--exact-port`| Attempts to run Storybook on the exact port number specified.  
If the port is already in use, Storybook will exit with an error message.  
`storybook dev -p 9009 --exact-port`  
`-h`, `--host [string]`| Host to run Storybook.  
`storybook dev -h my-host.com`  
`-c`, `--config-dir [dir-name]`| Storybook configuration directory.  
`storybook dev -c .storybook`  
`--loglevel [level]`| Controls level of logging during build.  
Available options: `silly`, `verbose`, `info` (default), `warn`, `error`, `silent`  
`storybook dev --loglevel warn`  
`--https`| Serve Storybook over HTTPS. Note: You must provide your own certificate information.  
`storybook dev --https`  
`--ssl-ca`| Provide an SSL certificate authority. (Optional with --https, required if using a self-signed certificate)  
`storybook dev --ssl-ca my-certificate`  
`--ssl-cert`| Provide an SSL certificate. (Required with --https)  
`storybook dev --ssl-cert my-ssl-certificate`  
`--ssl-key`| Provide an SSL key. (Required with --https)  
`storybook dev --ssl-key my-ssl-key`  
`--smoke-test`| Exit after successful start.  
`storybook dev --smoke-test`  
`--ci`| CI mode (skip interactive prompts, don't open browser).  
`storybook dev --ci`  
`--no-open`| Do not open Storybook automatically in the browser.  
`storybook dev --no-open`  
`--quiet`| Suppress verbose build output.  
`storybook dev --quiet`  
`--debug`| Outputs more logs in the CLI to assist debugging.  
`storybook dev --debug`  
`--debug-webpack`| Display final webpack configurations for debugging purposes.  
`storybook dev --debug-webpack`  
`--stats-json [dir-name]`| Write stats JSON to disk.  
Requires Webpack  
`storybook dev --stats-json /tmp/stats`  
`--no-version-updates`| Skips Storybook's update check.  
`storybook dev --no-version-updates`  
`--docs`| Starts Storybook in documentation mode. Learn more about it in [here](../writing-docs/build-documentation#preview-storybooks-documentation).  
`storybook dev --docs`  
`--initial-path [path]`| Configures the URL Storybook should open when it opens the browser for the first time.  
`storybook dev --initial-path=/docs/getting-started--docs`  
`--preview-url [path]`| Overrides the default Storybook preview with a custom built preview URL.  
`storybook dev --preview-url=http://localhost:1337/external-iframe.html`  
`--force-build-preview`| Forcefully builds Storybook's preview iframe.  
Useful if you're experiencing issues, or combined with `--preview-url` to ensure the preview is up-to-date.  
`storybook dev --force-build-preview`  
`--disable-telemetry`| Disables Storybook's telemetry. Learn more about it [here](../configure/telemetry#how-to-opt-out).  
`storybook dev --disable-telemetry`  
`--enable-crash-reports`| Enables sending crash reports to Storybook's telemetry. Learn more about it [here](../configure/telemetry#crash-reports-disabled-by-default).  
`storybook dev --enable-crash-reports`  
`--preview-only`| Skips Storybook's manager from building and opens the app in "preview only" mode, which is designed to be used in [unsupported browsers](../sharing/publish-storybook#build-storybook-for-older-browsers).   
`storybook dev --preview-only`  
  
⚠️

With the release of Storybook 8, the `-s` CLI flag was removed. We recommend using the [static directory](../configure/integration/images-and-assets#serving-static-files-via-storybook) instead if you need to serve static files.

### 

`build`

Compiles your Storybook instance so it can be [deployed](../sharing/publish-storybook). It should be run from the root of your project.
    
    
    storybook build [options]

Options include:

Option| Description  
---|---  
`-h`, `--help`| Output usage information.  
`storybook build --help`  
`-V`, `--version`| Output the version number.  
`storybook build -V`  
`-o`, `--output-dir [dir-name]`| Directory where to store built files.  
`storybook build -o /my-deployed-storybook`  
`-c`, `--config-dir [dir-name]`| Storybook configuration directory.  
`storybook build -c .storybook`  
`--loglevel [level]`| Controls level of logging during build.  
Available options: `silly`, `verbose`, `info` (default), `warn`, `error`, `silent`.  
`storybook build --loglevel warn`  
`--quiet`| Suppress verbose build output.  
`storybook build --quiet`  
`--debug`| Outputs more logs in the CLI to assist debugging.  
`storybook build --debug`  
`--debug-webpack`| Display final webpack configurations for debugging purposes.  
`storybook build --debug-webpack`  
`--stats-json [dir-name]`| Write stats JSON to disk.  
Requires Webpack  
`storybook build --stats-json /tmp/stats`  
`--docs`| Builds Storybook in documentation mode. Learn more about it in [here](../writing-docs/build-documentation#publish-storybooks-documentation).  
`storybook build --docs`  
`--test`| Optimize Storybook's production build for performance and tests by removing unnecessary features with the `test` option. Learn more [here](../api/main-config/main-config-build).  
`storybook build --test`  
`--preview-url [path]`| Overrides the default Storybook preview with a custom built preview URL.  
`storybook build --preview-url=http://localhost:1337/external-iframe.html`  
`--force-build-preview`| Forcefully builds Storybook's preview iframe.  
Useful if you're experiencing issues, or combined with `--preview-url` to ensure the preview is up-to-date.  
`storybook build --force-build-preview`  
`--disable-telemetry`| Disables Storybook's telemetry. Learn more about it [here](../configure/telemetry#how-to-opt-out).  
`storybook build --disable-telemetry`  
`--enable-crash-reports`| Enables sending crash reports to Storybook's telemetry. Learn more about it [here](../configure/telemetry#crash-reports-disabled-by-default).  
`storybook build --enable-crash-reports`  
`--preview-only`| Skips Storybook's manager from building and produces a "preview only" app, which is designed to be used in [unsupported browsers](../sharing/publish-storybook#build-storybook-for-older-browsers).   
`storybook build --preview-only`  
  
### 

`init`

ℹ️

We recommend `create-storybook` for new projects. The `init` command will remain available for backwards compatibility.

Installs and initializes the specified version (e.g., `@latest`, `@8`, `@next`) of Storybook into your project. If no version is specified, the latest version is installed. Read more in the [installation guide](../get-started/install).
    
    
    storybook[@version] init [options]

For example, `storybook@8.4 init` will install Storybook 8.4 into your project.

Options include:

Option| Description  
---|---  
`-h`, `--help`| Output usage information.  
`storybook init --help`  
`-b`, `--builder`| Defines the [builder](../builders) to use for your Storybook instance.  
`storybook init --builder webpack5`  
`-f`, `--force`| Forcefully installs Storybook into your project, prompting you to overwrite existing files.  
`storybook init --force`  
`-s`, `--skip-install`| Skips the dependency installation step. Used only when you need to configure Storybook manually.  
`storybook init --skip-install`  
`-t`, `--type`| Defines the [framework](../configure/integration/frameworks) to use for your Storybook instance.  
`storybook init --type solid`  
`-y`, `--yes`| Skips interactive prompts and automatically installs Storybook per specified version, including all features.  
`storybook init --yes`  
`--features [...values]`| Use these features when installing, skipping the prompt. Supported values are `docs`, `test`, and `a11y`, space separated.  
`storybook init --features docs test a11y`  
`--package-manager`| Sets the package manager to use when installing Storybook.  
Available package managers include `npm`, `yarn`, and `pnpm`.  
`storybook init --package-manager pnpm`  
`--use-pnp`| Enables [Plug'n'Play](https://yarnpkg.com/features/pnp) support for Yarn. This option is only available when using Yarn as your package manager.  
`storybook init --use-pnp`  
`-p`, `--parser`| Sets the [jscodeshift parser](https://github.com/facebook/jscodeshift#parser).  
Available parsers include `babel`, `babylon`, `flow`, `ts`, and `tsx`.  
`storybook init --parser tsx`  
`--debug`| Outputs more logs in the CLI to assist debugging.  
`storybook init --debug`  
`--disable-telemetry`| Disables Storybook's telemetry. Learn more about it [here](../configure/telemetry#how-to-opt-out).  
`storybook init --disable-telemetry`  
`--enable-crash-reports`| Enables sending crash reports to Storybook's telemetry. Learn more about it [here](../configure/telemetry#crash-reports-disabled-by-default).  
`storybook init --enable-crash-reports`  
`--loglevel <level>`| Controls level of logging during initialization.  
Available options: `trace`, `debug`, `info` (default), `warn`, `error`, `silent`  
`storybook init --loglevel debug`  
`--logfile [path]`| Write all debug logs to the specified file at the end of the run. Defaults to debug-storybook.log when [path] is not provided.  
`storybook init --logfile /tmp/debug-storybook.log`  
`--no-dev`| Complete the initialization of Storybook without running the Storybook dev server.  
`storybook init --no-dev`  
  
### 

`add`

Installs a Storybook addon and configures your project for it. Read more in the [addon installation guide](../addons/install-addons).
    
    
    storybook add [addon] [options]

Options include:

Option| Description  
---|---  
`-h`, `--help`| Output usage information.  
`storybook add --help`  
`-c`, `--config-dir`| Storybook configuration directory.  
`storybook migrate --config-dir .storybook`  
`--package-manager`| Sets the package manager to use when installing the addon.  
Available package managers include `npm`, `yarn`, and `pnpm`.  
`storybook add [addon] --package-manager pnpm`  
`-s`, `--skip-postinstall`| Skips post-install configuration. Used only when you need to configure the addon yourself.  
`storybook add [addon] --skip-postinstall`  
`--debug`| Outputs more logs in the CLI to assist debugging.  
`storybook add --debug`  
`--loglevel <level>`| Controls level of logging during addon installation.  
Available options: `trace`, `debug`, `info` (default), `warn`, `error`, `silent`  
`storybook add [addon] --loglevel debug`  
`--logfile [path]`| Write all debug logs to the specified file at the end of the run. Defaults to debug-storybook.log when [path] is not provided.  
`storybook add [addon] --logfile /tmp/debug-storybook.log`  
  
### 

`remove`

Deletes a Storybook addon from your project. Read more in the [addon installation guide](../addons/install-addons#removing-addons).
    
    
    storybook remove [addon] [options]

Options include:

Option| Description  
---|---  
`-h`, `--help`| Output usage information.  
`storybook remove --help`  
`--package-manager`| Sets the package manager to use when removing the addon.  
Available package managers include `npm`, `yarn`, and `pnpm`.  
`storybook remove [addon]--package-manager pnpm`  
`--debug`| Outputs more logs in the CLI to assist debugging.  
`storybook remove --debug`  
`--disable-telemetry`| Disables Storybook's telemetry. Learn more about it [here](../configure/telemetry#how-to-opt-out).  
`storybook remove --disable-telemetry`  
`--enable-crash-reports`| Enables sending crash reports to Storybook's telemetry. Learn more about it [here](../configure/telemetry#crash-reports-disabled-by-default).  
`storybook remove --enable-crash-reports`  
  
### 

`upgrade`

Upgrades your Storybook instance to the specified version (e.g., `@latest`, `@8`, `@next`). Read more in the [upgrade guide](../releases/upgrading).
    
    
    storybook[@version] upgrade [options]

For example, `storybook@latest upgrade --dry-run` will perform a dry run (no actual changes) of upgrading your project to the latest version of Storybook.

Options include:

Option| Description  
---|---  
`-h`, `--help`| Output usage information.  
`storybook upgrade --help`  
`-c, --config-dir <dir-name...>`| Directory or directories to find Storybook configurations  
`storybook upgrade --config-dir .storybook`  
`-n`, `--dry-run`| Checks for version upgrades without installing them.  
`storybook upgrade --dry-run`  
`-s`, `--skip-check`| Skips the migration check step during the upgrade process.  
`storybook upgrade --skip-check`  
`-y`, `--yes`| Skips interactive prompts and automatically upgrades Storybook to the latest version.  
`storybook upgrade --yes`  
`-f`,`--force`| Force the upgrade, skipping autoblockers check.  
`storybook upgrade --force`  
`--package-manager`| Sets the package manager to use when upgrading Storybook.  
Available package managers include `npm`, `yarn`, and `pnpm`.  
`storybook upgrade --package-manager pnpm`  
`--debug`| Outputs more logs in the CLI to assist debugging.  
`storybook upgrade --debug`  
`--disable-telemetry`| Disables Storybook's telemetry. Learn more about it [here](../configure/telemetry#how-to-opt-out).  
`storybook upgrade --disable-telemetry`  
`--enable-crash-reports`| Enables sending crash reports to Storybook's telemetry. Learn more about it [here](../configure/telemetry#crash-reports-disabled-by-default).  
`storybook upgrade --enable-crash-reports`  
`-logfile [path]`| Write all debug logs to the specified file at the end of the run. Defaults to debug-storybook.log when [path] is not provided.  
`storybook upgrade --logfile /tmp/debug-storybook.log`  
`--loglevel <level>`| Define log level: `debug`, `error`, `info`, `silent`, `trace`, or `warn` (default: `info`).  
`storybook upgrade --loglevel debug`  
  
### 

`migrate`

Runs the provided codemod to ensure your Storybook project is compatible with the specified version. Read more in the [migration guide](../releases/upgrading).
    
    
    storybook[@version] migrate [codemod] [options]

ℹ️

The command requires the codemod name (e.g., `csf-2-to-3`) as an argument to apply the necessary changes to your project. You can find the list of available codemods by running `storybook migrate --list`.

For example, `storybook@latest migrate csf-2-to-3 --dry-run`, checks your project to verify if the codemod can be applied without making any changes, providing you with a report of which files would be affected.

Options include:

Option| Description  
---|---  
`-h`, `--help`| Output usage information.  
`storybook migrate --help`  
`-c`, `--config-dir`| Storybook configuration directory.  
`storybook migrate --config-dir .storybook`  
`-n`, `--dry-run`| Verify the migration exists and show the files to which it will be applied.  
`storybook migrate --dry-run`  
`-l`, `--list`| Shows a list of available codemods.  
`storybook migrate --list`  
`-g`, `--glob`| Glob for files upon which to apply the codemods.  
`storybook migrate --glob src/**/*.stories.tsx`  
`-p`, `--parser`| Sets the [jscodeshift parser](https://github.com/facebook/jscodeshift#parser).  
Available parsers include `babel`, `babylon`, `flow`, `ts`, and `tsx`.  
`storybook migrate --parser tsx`  
`-r`, `--rename [from-to]`| Renames the files affected by the codemod to include the provided suffix.  
`storybook migrate --rename ".js:.ts"`  
`--debug`| Outputs more logs in the CLI to assist debugging.  
`storybook migrate --debug`  
  
### 

`automigrate`

Perform standard configuration checks to determine if your Storybook project can be automatically migrated to the specified version. Read more in the [migration guide](../releases/upgrading#automigrate-script).
    
    
    storybook[@version] automigrate [fixId] [options]

For example, `storybook@latest automigrate --dry-run` scans your project for potential migrations that can be applied automatically without making any changes.

Options include:

Option| Description  
---|---  
`-h`, `--help`| Output usage information.  
`storybook automigrate --help`  
`-c`, `--config-dir`| Storybook configuration directory.  
`storybook automigrate --config-dir .storybook`  
`-n`, `--dry-run`| Checks for available migrations without applying them.  
`storybook automigrate --dry-run`  
`-s`, `--skip-install`| Skip installing dependencies whenever applicable.  
`storybook automigrate --skip-install`  
`-y`, `--yes`| Applies available migrations automatically without prompting for confirmation.  
`storybook automigrate --yes`  
`-l`, `--list`| Shows a list of available automigrations.  
`storybook automigrate --list`  
`--package-manager`| Sets the package manager to use when running the auto migration.  
Available package managers include `npm`, `yarn`, and `pnpm`.  
`storybook automigrate --package-manager pnpm`  
`--renderer`| Specifies Storybook's renderer to use when running the automigration.  
Useful for monorepo environments where multiple Storybook instances can exist in the same project.  
`storybook automigrate --renderer vue`  
`--debug`| Outputs more logs in the CLI to assist debugging.  
`storybook automigrate --debug`  
`--disable-telemetry`| Disables Storybook's telemetry. Learn more about it [here](../configure/telemetry#how-to-opt-out).  
`storybook automigrate --disable-telemetry`  
`--enable-crash-reports`| Enables sending crash reports to Storybook's telemetry. Learn more about it [here](../configure/telemetry#crash-reports-disabled-by-default).  
`storybook automigrate --enable-crash-reports`  
  
### 

`doctor`

Performs a health check on your Storybook project for common issues (e.g., duplicate dependencies, incompatible addons or mismatched versions) and provides suggestions on how to fix them. Applicable when [upgrading](../releases/upgrading#verifying-the-upgrade) Storybook versions.
    
    
    storybook doctor [options]

Options include:

Option| Description  
---|---  
`-h`, `--help`| Output usage information.  
`storybook doctor --help`  
`-c`, `--config-dir`| Storybook configuration directory.  
`storybook doctor --config-dir .storybook`  
`--package-manager`| Sets the package manager to use when running the health check.  
Available package managers include `npm`, `yarn`, and `pnpm`.  
`storybook doctor --package-manager pnpm`  
`--debug`| Outputs more logs in the CLI to assist debugging.  
`storybook doctor --debug`  
  
### 

`info`

Reports useful debugging information about your environment. Helpful in providing information when opening an issue or a discussion.
    
    
    storybook info

Example output:
    
    
    Storybook Environment Info:
     
      System:
        OS: macOS 14.2
        CPU: (8) arm64 Apple M3
        Shell: 5.9 - /bin/zsh
      Binaries:
        Node: 18.19.0 - ~/.nvm/versions/node/v18.19.0/bin/node
        npm: 10.2.3 - ~/.nvm/versions/node/v18.19.0/bin/npm <----- active
      Browsers:
        Chrome: 120.0.6099.199
      npmPackages:
        @storybook/addon-onboarding: ^1.0.10 => 1.0.10
        @storybook/react: ^7.6.6 => 7.6.6
        @storybook/react-vite: ^7.6.6 => 7.6.6
        storybook: ^7.6.6 => 7.6.6
      npmGlobalPackages:
        chromatic: ^10.2.0 => 10.2.0

### 

`index`

Build an `index.json` that lists all stories and docs entries in your Storybook.
    
    
    storybook index [options]

Options include:

Option| Description  
---|---  
`-o`, `--output-file <file-name>`| JSON file to output index  
`-c`, `--config-dir <dir-name>`| Storybook configuration directory  
`--quiet`| Suppress verbose build output  
`--loglevel <level>`| Control level of logging during build  
`--disable-telemetry`| Disables Storybook's telemetry  
`--debug`| Outputs more logs in the CLI to assist debugging.  
`--enable-crash-reports`| Enables sending crash reports to Storybook's telemetry  
  
### 

`sandbox`

Generates a local sandbox project using the specified version (e.g., `@latest`, `@8`, `@next`) for testing Storybook features based on the list of supported [frameworks](../configure/integration/frameworks). Useful for reproducing bugs when opening an issue or a discussion.
    
    
    storybook[@version] sandbox [framework-filter] [options]

For example, `storybook@next sandbox` will generated sandboxes using the newest pre-release version of Storybook.

The `framework-filter` argument is optional and can filter the list of available frameworks. For example, `storybook@next sandbox react` will only offer to generate React-based sandboxes.

Options include:

Option| Description  
---|---  
`-h`, `--help`| Output usage information.  
`storybook sandbox --help`  
`-o`, `--output [dir-name]`| Configures the location of the sandbox project.  
`storybook sandbox --output /my-sandbox-project`  
`--no-init`| Generates a sandbox project without initializing Storybook.  
`storybook sandbox --no-init`  
`--debug`| Outputs more logs in the CLI to assist debugging.  
`storybook sandbox --debug`  
`--disable-telemetry`| Disables Storybook's telemetry. Learn more about it [here](../configure/telemetry#how-to-opt-out).  
`storybook sandbox --disable-telemetry`  
`--enable-crash-reports`| Enables sending crash reports to Storybook's telemetry. Learn more about it [here](../configure/telemetry#crash-reports-disabled-by-default).  
`storybook sandbox --enable-crash-reports`  
  
ℹ️

If you're looking for a hosted version of the available sandboxes, see [storybook.new](https://storybook.new).

## 

`create-storybook`

To streamline the process of creating a new Storybook project, a separate CLI called `create-storybook` is provided. Package managers such as npm, pnpm, and Yarn will execute this command when running `create storybook`. You can specify a version (e.g., `@latest`, `@8`, `@next`) or it will default to the latest version. Read more in the [installation guide](../get-started/install).
    
    
    create storybook[@version] [options]

For example, `create storybook@8.6` will install Storybook 8.6 into your project.

Options include:

Option| Description  
---|---  
`-h`, `--help`| Output usage information.  
`create storybook --help`  
`-b`, `--builder`| Defines the [builder](../builders) to use for your Storybook instance.  
`create storybook --builder webpack5`  
`-f`, `--force`| Forcefully installs Storybook into your project, prompting you to overwrite existing files.  
`create storybook --force`  
`-s`, `--skip-install`| Skips the dependency installation step. Used only when you need to configure Storybook manually.  
`create storybook --skip-install`  
`-t`, `--type`| Defines the [framework](../configure/integration/frameworks) to use for your Storybook instance.  
`create storybook --type solid`  
`-y`, `--yes`| Skips interactive prompts and automatically installs Storybook per specified version, including all features.  
`create storybook --yes`  
`--features [...values]`| Use these features when installing, skipping the prompt. Supported values are `docs`, `test`, and `a11y`, space separated.  
`create storybook --features docs test a11y`  
`--package-manager`| Sets the package manager to use when installing Storybook.  
Available package managers include `npm`, `yarn`, and `pnpm`.  
`create storybook --package-manager pnpm`  
`--use-pnp`| Enables [Plug'n'Play](https://yarnpkg.com/features/pnp) support for Yarn. This option is only available when using Yarn as your package manager.  
`create storybook --use-pnp`  
`-p`, `--parser`| Sets the [jscodeshift parser](https://github.com/facebook/jscodeshift#parser).  
Available parsers include `babel`, `babylon`, `flow`, `ts`, and `tsx`.  
`create storybook --parser tsx`  
`--debug`| Outputs more logs in the CLI to assist debugging.  
`create storybook --debug`  
`--disable-telemetry`| Disables Storybook's telemetry. Learn more about it [here](../configure/telemetry#how-to-opt-out).  
`create storybook --disable-telemetry`  
`--enable-crash-reports`| Enables sending crash reports to Storybook's telemetry. Learn more about it [here](../configure/telemetry#crash-reports-disabled-by-default).  
`create storybook --enable-crash-reports`  
`--loglevel <level>`| Controls level of logging during initialization.  
Available options: `trace`, `debug`, `info` (default), `warn`, `error`, `silent`  
`storybook init --loglevel debug`  
`--logfile [path]`| Write all debug logs to the specified file at the end of the run. Defaults to debug-storybook.log when [path] is not provided.  
`storybook init --logfile /tmp/debug-storybook.log`  
`--no-dev`| Complete the initialization of Storybook without running the Storybook dev server.  
`create storybook --no-dev`  
  
Was this page useful?

👍👎

[✍️ Edit on Github](https://github.com/storybookjs/storybook/tree/next/docs/api/cli-options.mdx)