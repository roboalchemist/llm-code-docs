# Source: https://docs.readthedocs.com/platform/latest/reference/environment-variables.html

# Environment variable reference[](#environment-variable-reference "Link to this heading")

All [[build processes]](../builds.html) have the following environment variables automatically defined and available for each build step:

[[READTHEDOCS]][](#envvar-READTHEDOCS "Link to this definition")

:   Whether the build is running inside Read the Docs.

    Default[:]

    :   [`True`]

```
<!-- -->
```

[[READTHEDOCS_PRODUCTION_DOMAIN]][](#envvar-READTHEDOCS_PRODUCTION_DOMAIN "Link to this definition")

:   Domain where Read the Docs application/dashboard and API are running.

    Example[:]

    :   [`readthedocs.org`]

    Example[:]

    :   [`readthedocs.com`]

    Example[:]

    :   [`app.readthedocs.org`]

    Example[:]

    :   [`app.readthedocs.com`]

    Example[:]

    :   [`devthedocs.org`]

    Example[:]

    :   [`devthedocs.com`]

```
<!-- -->
```

[[READTHEDOCS_PROJECT]][](#envvar-READTHEDOCS_PROJECT "Link to this definition")

:   The [[slug]](../glossary.html#term-slug) of the project being built. For example, [`my-example-project`].

```
<!-- -->
```

[[READTHEDOCS_LANGUAGE]][](#envvar-READTHEDOCS_LANGUAGE "Link to this definition")

:   The locale name, or the identifier for the locale, for the project being built. This value comes from the project's configured language code, which is in lowercase and uses a dash as a separator.

    Example[:]

    :   [`en`]

    Example[:]

    :   [`it`]

    Example[:]

    :   [`de-at`]

    Example[:]

    :   [`es`]

    Example[:]

    :   [`pt-br`]

```
<!-- -->
```

[[READTHEDOCS_VERSION]][](#envvar-READTHEDOCS_VERSION "Link to this definition")

:   The [[slug]](../glossary.html#term-slug) of the version being built, such as [`latest`], [`stable`], or a branch name like [`feature-1234`]. For [[pull request builds]](../pull-requests.html), the value will be the pull request number.

```
<!-- -->
```

[[READTHEDOCS_VERSION_NAME]][](#envvar-READTHEDOCS_VERSION_NAME "Link to this definition")

:   The verbose name of the version being built, such as [`latest`], [`stable`], or a branch name like [`feature/1234`].

```
<!-- -->
```

[[READTHEDOCS_VERSION_TYPE]][](#envvar-READTHEDOCS_VERSION_TYPE "Link to this definition")

:   The type of the version being built.

    Example[:]

    :   [`branch`]

    Example[:]

    :   [`tag`]

    Example[:]

    :   [`external`] (for [[pull request builds]](../pull-requests.html))

    Example[:]

    :   [`unknown`]

```
<!-- -->
```

[[READTHEDOCS_VIRTUALENV_PATH]][](#envvar-READTHEDOCS_VIRTUALENV_PATH "Link to this definition")

:   Path for the [[virtualenv that was created for this build]](../builds.html). Only exists for builds using Virtualenv and not Conda.

    Example[:]

    :   [`/home/docs/checkouts/readthedocs.org/user_builds/project/envs/version`]

```
<!-- -->
```

[[READTHEDOCS_OUTPUT]][](#envvar-READTHEDOCS_OUTPUT "Link to this definition")

:   Base path for well-known output directories. Files in these directories will automatically be found, uploaded, and published.

    You need to concatenate an output format to this variable. Currently valid formats are [`html`], [`pdf`], [`htmlzip`], and [`epub`]. (e.g. [`$READTHEDOCS_OUTPUT/html/`] or [`$READTHEDOCS_OUTPUT/pdf/`]) You also need to create the directory before moving outputs into the destination. You can create it with the following command [`mkdir`]` `[`-p`]` `[`$READTHEDOCS_OUTPUT/html/`]. Note that only [`html`] supports multiple files, the other formats should have one and only one file to be uploaded.

    ::: 
    See also

    [[Where to put files]](../build-customization.html#where-to-put-files)

    :   Information about using custom commands to generate output that will automatically be published once your build succeeds.
    :::

```
<!-- -->
```

[[READTHEDOCS_CANONICAL_URL]][](#envvar-READTHEDOCS_CANONICAL_URL "Link to this definition")

:   Canonical base URL for the version that is built. If the project has configured a [[custom domain]](../custom-domains.html) (e.g. [`docs.example.com`]) it will be used in the resulting canonical URL. Otherwise, your project's [[default subdomain]](../custom-domains.html#default-subdomain) will be used.

    The path for the language and version is appended to the domain, so the final canonical base URLs can look like the following examples:

    Example[:]

    :   [`https://docs.example.com/en/latest/`]

    Example[:]

    :   [`https://docs.readthedocs.io/ja/stable/`]

    Example[:]

    :   [`https://example--17.org.readthedocs.build/fr/17/`]

```
<!-- -->
```

[[READTHEDOCS_REPOSITORY_PATH]][](#envvar-READTHEDOCS_REPOSITORY_PATH "Link to this definition")

:   Path where the repository was cloned.

    Example[:]

    :   [`/home/docs/checkouts/readthedocs.org/user_builds/test-builds/checkouts/latest`]

```
<!-- -->
```

[[READTHEDOCS_GIT_CLONE_URL]][](#envvar-READTHEDOCS_GIT_CLONE_URL "Link to this definition")

:   URL for the remote source repository, from which the documentation is cloned. It could be HTTPS, SSH or any other URL scheme supported by Git. This is the same URL defined in your Project's [[dashboard]](../glossary.html#term-dashboard) in [Admin ‣ Settings ‣ Repository URL].

    Example[:]

    :   [`https://github.com/readthedocs/readthedocs.org`]

    Example[:]

    :   [`git@github.com:readthedocs/readthedocs.org.git`]

```
<!-- -->
```

[[READTHEDOCS_GIT_IDENTIFIER]][](#envvar-READTHEDOCS_GIT_IDENTIFIER "Link to this definition")

:   Contains the Git identifier that was *checked out* from the remote repository URL. Possible values are either a branch or tag name.

    Example[:]

    :   [`v1.x`]

    Example[:]

    :   [`bugfix/docs-typo`]

    Example[:]

    :   [`feature/signup`]

    Example[:]

    :   [`update-readme`]

    ::: 
    Note

    When building pull requests, this variable contains the numeric ID of the pull request, as we don't have access to the branch name.
    :::

```
<!-- -->
```

[[READTHEDOCS_GIT_COMMIT_HASH]][](#envvar-READTHEDOCS_GIT_COMMIT_HASH "Link to this definition")

:   Git commit hash identifier checked out from the repository URL.

    Example[:]

    :   [`1f94e04b7f596c309b7efab4e7630ed78e85a1f1`]

See also

[[Environment variable overview]](../environment-variables.html)

:   General information about how environment variables are used in the build process.

[[How to use custom environment variables]](../guides/environment-variables.html)

:   Learn how to define your own custom environment variables, in addition to the pre-defined ones.