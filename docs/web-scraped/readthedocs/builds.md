# Source: https://docs.readthedocs.com/platform/latest/builds.html

# Build process overview[](#build-process-overview "Link to this heading")

Once a project has been added and a build is triggered, Read the Docs executes a set of [[pre-defined jobs]](glossary.html#term-pre-defined-build-jobs) to build and upload documentation. This page explains in detail what happens behind the scenes, and includes an overview of how you can change this process.

## Understanding the build process[](#understanding-the-build-process "Link to this heading")

Understanding how your content is built helps with debugging any problems you might hit. It also gives you the knowledge to customize the build process.

Note

All the steps are run inside a Docker container, using the image defined in [[build.os]](config-file/v2.html#build-os). The build has access to all [[pre-defined environment variables]](reference/environment-variables.html) and [[custom environment variables]](environment-variables.html).

The build process includes the following jobs:

checkout[:]

:   Checks out a project's code from the Git repository. On Read the Docs for Business, this environment includes the SSH deploy key that gives access to the repository.

system_dependencies[:]

:   Installs operating system and runtime dependencies. This includes specific versions of a language (e.g. Python, Node.js, Go, Rust) and also [`apt`] packages.

    [[build.tools]](config-file/v2.html#build-tools) can be used to define a language version, and [[build.apt_packages]](config-file/v2.html#build-apt-packages) to define [`apt`] packages.

create_environment[:]

:   Creates a Python environment to install all the dependencies in an isolated and reproducible way. Depending on what's defined by the project, a [[virtualenv]](glossary.html#term-virtualenv) or a [[conda environment]](config-file/v2.html#conda) will be used.

    ::: 
    Note

    This step is only executed if the [[sphinx]](config-file/v2.html#sphinx) or [[mkdocs]](config-file/v2.html#mkdocs) keys are defined.
    :::

install[:]

:   Installs [[default and project dependencies]](build-default-versions.html). This includes any requirements you have configured in [[Requirements file]](config-file/v2.html#requirements-file).

    If the project has extra Python requirements, [[python.install]](config-file/v2.html#python-install) can be used to specify them.

    ::: 
    Tip

    We strongly recommend [[pinning all the versions]](guides/reproducible-builds.html) required to build the documentation to avoid unexpected build errors.
    :::

    ::: 
    Note

    This step is only executed if the [[sphinx]](config-file/v2.html#sphinx) or [[mkdocs]](config-file/v2.html#mkdocs) keys are defined.
    :::

build[:]

:   Runs the main command to build the documentation for each of the formats declared ([[formats]](config-file/v2.html#formats)). It will use Sphinx ([[sphinx]](config-file/v2.html#sphinx)) or MkDocs ([[mkdocs]](config-file/v2.html#mkdocs)) depending on the project.

upload[:]

:   Once the build process finishes successfully, the resulting artifacts (HTML, PDF, etc.) are uploaded to our servers. Our [[CDN]](reference/cdn.html) is then purged so your docs are *always up to date*.

See also

If you require additional build steps or customization, it's possible to run user-defined commands and [[customize the build process]](build-customization.html).