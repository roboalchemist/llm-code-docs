# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/snowpark-commands/build.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/snowpark/build.md

# Build a Snowpark project

The `snow snowpark build` command builds the Snowpark project as one or more `.zip` archive files that can be used by the `deploy` command. The cp,,amd builds the archives using only the `src` directory specified in the project file.

```snowcli
snow snowpark build
```

```output
Resolving dependencies from requirements.txt
  No external dependencies.
Preparing artifacts for source code
  Creating: app.zip
Build done.
```

Additional options:

* `--allow-shared-libraries`: Allows shared (`.so`/`.dll`) libraries, when using packages installed through `pip`.
* `--ignore-anaconda`: Does not lookup packages on Snowflake Anaconda channel.
* `--index-url`: Specifies the base URL of the Python Package Index to use for package lookup. This URL should point to a repository compliant with PEP 503 (the simple repository API) or a local directory laid out in the same format.
* `--skip-version-check`: Skips comparing versions of dependencies between requirements and Anaconda.
* `--project [-p]`: Specifies the path where the Snowpark project resides. Defaults to the current working directory.
