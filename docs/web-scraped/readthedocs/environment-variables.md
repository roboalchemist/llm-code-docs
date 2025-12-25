# Source: https://docs.readthedocs.com/platform/latest/environment-variables.html

[]

# Environment variable overview[](#environment-variable-overview "Link to this heading")

Read the Docs allows you to define your own environment variables to be used in the build process. It also defines a set of [[default environment variables]](reference/environment-variables.html) with information about your build. These are useful for different purposes:

-   Custom environment variables are useful for adding build secrets such as API tokens.

-   Default environment variables are useful for varying your build specifically for Read the Docs or specific types of builds on Read the Docs.

Custom environment variables are defined in the [[dashboard]](glossary.html#term-dashboard) interface in [Admin ‣ Environment variables]. Environment variables are defined for a project's entire build process, [[with 2 important exceptions]](#custom-env-var-exceptions).

Aside from storing secrets, there are [[other patterns]](#patterns-of-using-environment-variables) that take advantage of environment variables, like reusing the same *monorepo* configuration in multiple documentation projects. In cases where the environment variable isn't a secret, like a build tool flag, you should also be aware of the [[alternatives to environment variables]](#alternatives-to-environment-variables).

See also

[[How to use custom environment variables]](guides/environment-variables.html)

:   A practical example of adding and accessing custom environment variables.

[[Environment variable reference]](reference/environment-variables.html)

:   Reference to all pre-defined environment variables for your build environments.

[[Public API reference: Environment variables]](api/v3.html#environment-variables)

:   Reference for managing custom environments via Read the Docs' API.

## Environment variables and build process[](#environment-variables-and-build-process "Link to this heading")

When a [[build process]](builds.html) is started, [[pre-defined environment variables]](reference/environment-variables.html) and custom environment variables are added *at each step* of the build process. The two sets of environment variables are merged together during the build process and are exposed to all of the executed commands, with pre-defined variables taking precedence over custom environment variables.

There are two noteworthy exceptions for *custom environment variables*:

Build checkout step

:   Custom environment variables are **not** available during the checkout step of the [[build process]](builds.html)

Pull request builds

:   Custom environment variables that are not marked as [Public] will not be available in [[pull request builds]](pull-requests.html)