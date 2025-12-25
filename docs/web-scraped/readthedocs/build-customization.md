# Source: https://docs.readthedocs.com/platform/latest/build-customization.html

# Build process customization[](#build-process-customization "Link to this heading")

Read the Docs has a [[well-defined build process]](builds.html) that works for many projects. We also allow customization of builds in two ways:

Customize our standard build process

:   Keep using the default commands for MkDocs or Sphinx, but extend or override the ones you need.

Define a build process from scratch

:   This option gives you *full control* over your build. Read the Docs supports any tool that generates HTML.

## Extend or override the build process[](#extend-or-override-the-build-process "Link to this heading")

In the normal build process, the pre-defined jobs [`checkout`], [`system_dependencies`], and [`upload`] are executed. If you define a [[sphinx]](config-file/v2.html#sphinx) or [[mkdocs]](config-file/v2.html#mkdocs) configuration, the [`create_environment`], [`install`], and [`build`] jobs will use the default commands for the selected tool. If no tool configuration is specified, these jobs won't execute anything by default.

The jobs where users can customize our default build process are:

+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Step                | Customizable jobs                                                                                                                                                                                    |
+=====================+======================================================================================================================================================================================================+
| Checkout            | [`post_checkout`]                                                                                                                                             |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| System dependencies | [`pre_system_dependencies`], [`post_system_dependencies`]                                                              |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Create environment  | [`pre_create_environment`], [`create_environment`], [`post_create_environment`] |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Install             | [`pre_install`], [`install`], [`post_install`]                                  |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Build               | [`pre_build`], [`build`], [`post_build`]                                        |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Upload              | No customizable jobs currently                                                                                                                                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Note

Any other pre-defined jobs ([`checkout`], [`system_dependencies`], [`upload`]) cannot be overridden or skipped.

These jobs are defined using the [[configuration file]](config-file/v2.html) with the [[build.jobs]](config-file/v2.html#build-jobs) key. This example configuration defines commands to be executed *before* installing and *after* the build has finished, and also overrides the default build command for the [`htmlzip`] format, while keeping the default commands for the [`html`] and [`pdf`] formats:

[.readthedocs.yaml][](#id1 "Link to this code")

    version: 2
    formats: [htmlzip, pdf]
    sphinx:
       configuration: docs/conf.py
    python:
       install:
         - requirements: docs/requirements.txt
    build:
      os: "ubuntu-22.04"
      tools:
        python: "3.10"
      jobs:
        pre_install:
          - bash ./scripts/pre_install.sh
        build:
          # The default commands for generating the HTML and pdf formats will still run.
          htmlzip:
            - echo "Override default build command for htmlzip format"
            - mkdir -p $READTHEDOCS_OUTPUT/htmlzip/
            - echo "Hello, world!" > $READTHEDOCS_OUTPUT/htmlzip/index.zip
        post_build:
          - curl -X POST \
            -F "project=$" \
            -F "version=$" https://example.com/webhooks/readthedocs/

### Features and limitations[](#features-and-limitations "Link to this heading")

-   The current working directory is at the root of your project's cloned repository.

-   Environment variables are expanded for each individual command (see [[Environment variable reference]](reference/environment-variables.html)).

-   Each command is executed in a new shell process, so modifications done to the shell environment do not persist between commands.

-   Any command returning non-zero exit code will cause the build to fail immediately (note there is a special exit code to [cancel the build](cancel-build-based-on-a-condition)).

-   [`build.os`] and [`build.tools`] are required when using [`build.jobs`].

-   If the [[sphinx]](config-file/v2.html#sphinx) or [[mkdocs]](config-file/v2.html#mkdocs) configuration is defined, the [`create_environment`], [`install`], and [`build`] jobs will use the default commands for the selected tool.

-   If neither of the [[sphinx]](config-file/v2.html#sphinx) or [[mkdocs]](config-file/v2.html#mkdocs) configurations are defined, the [`create_environment`], [`install`], and [`build`] jobs will default to run nothing, giving you full control over the build process.