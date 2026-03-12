# Source: https://docs.snowflake.com/en/developer-guide/git/git-limitations.md

# Git in Snowflake limitations

This topic describes limitations for using Git repositories from within Snowflake.

* Currently, only the following Snowflake features can write to the repository:

  * [Workspaces](../../user-guide/ui-snowsight/workspaces-git.md)
  * [Streamlit applications](../streamlit/features/git-integration.md)
  * [Notebooks](../../user-guide/ui-snowsight/notebooks-snowgit.md)

  For other Snowflake code, access to the repository is read-only.
* When you connect to a Git repository using a workspace, the following limitation applies:

  * The Git repository can’t be empty. It must have at least one commit.
* [Preview Feature](../../release-notes/preview-features.md) — Open

  OAuth support is generally available only when the repository is hosted at [github.com](https://github.com/).

  OAuth support is in preview for repository providers other than github.com.

  Creating a local Git repository in Snowflake is supported only when using the Workspaces user interface to create it. It isn’t
  supported when you create the repository by using [CREATE GIT REPOSITORY](../../sql-reference/sql/create-git-repository.md) in a workspace. This is because
  when using the SQL command, the flow does not include presenting a user interface with which to sign in.
* Sharing Snowflake Git repository clones is not supported through data sharing or apps built on the Snowflake Native App Framework.
* Creating Snowflake Git repository clones inside application packages is not supported and might be blocked in the future.
* Creating Snowflake Git repository clones inside native applications on the consumer side is not supported.
* Snowflake doesn’t currently support submodules, so you won’t be able to see submodule files. Snowflake won’t download those files
  from the remote repository nor upload them to the remote repository.
* Git repositories larger than 2GB aren’t supported.
* Setting up an API integration on Snowflake is required to set up a Git repository object in Snowflake. For more information, see
  [Setting up Snowflake to use Git](git-setting-up.md).
