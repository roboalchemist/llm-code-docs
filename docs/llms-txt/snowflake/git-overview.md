# Source: https://docs.snowflake.com/en/developer-guide/git/git-overview.md

# Using a Git repository in Snowflake

You can integrate your remote Git repository with Snowflake so that files from the remote repository are synchronized to a local clone of the
repository in Snowflake. The Git repository clone in Snowflake acts as a local Git repository with a full clone of the remote
repository, including branches, tags, and commits.

With a Git repository clone in Snowflake, you can do the following:

* Perform common Git tasks, including the following:

  * Fetch the latest version.

    For more information, see [Fetch from the remote Git repository](git-operations.md).
  * Select branches or tags.
  * Browse folders and search for files by name.

    For more information, see [View a list of repository branches or tags](git-operations.md) and [View a list of repository files](git-operations.md).
  * Copy the full path to any selected file for referencing it in Snowflake code (such as handler code for functions, tasks, or procedures).
  * [Execute immediate from](../../sql-reference/sql/execute-immediate-from.md) `.sql` files (with a code preview).

    For an example, see [Use a Git repository clone file to configure new accounts](git-examples.md).
* Commit and push changes to the remote repository.

  Writing to the remote repository is supported only from the following Snowflake features:

  * [Workspaces](../../user-guide/ui-snowsight/workspaces-git.md)
  * [Streamlit apps](../streamlit/features/git-integration.md)
  * [Snowflake notebooks](../../user-guide/ui-snowsight/notebooks-snowgit.md)
* In Snowflake, use files from any branch or tag.
* From a Git repository clone synchronized from your remote repository, import files into code you execute in Snowflake.

  For example, you can write procedures and user-defined functions (UDFs) whose handler code is held by the Git repository clone synchronized
  from the repository.

## How Snowflake works with a remote Git repository

With a remote Git repository integrated with your Snowflake account, you synchronize files from the remote repository to a
Git repository clone in Snowflake. To access a file in Snowflake, you refer to it in the Git repository clone. For more information about
using repository files, see [Use a Git repository file as a stored procedure handler](git-examples.md).

### Snowflake Git repository clone

A Git repository clone in Snowflake is a full clone with all branches, tags, and commits from the remote repository.

After remote repository contents are in the Git repository clone, you can reference files there as you would a file on a stage.

You can perform operations similar to those you perform with Git commands in a local repository, including:

* [Fetching the remote repository](git-operations.md) to refresh the Git repository clone as the remote
  repository changes.
* [Viewing repository branches or tags](git-operations.md) contained by the Git repository clone.
* Pushing to the repository from Workspaces ([supported only from Workspaces](../../user-guide/ui-snowsight/workspaces-git.md)).

### Git repository and development tools

After you integrate your remote repository with Snowflake, you can continue using your development tools and local repository as before.
Through the Git repository clone, Snowflake becomes another client of your repository separate from your local repository.

## Supported platforms

You can currently integrate Git repositories that use the following Git platforms. This includes repositories based on these platforms, but
available at custom URLs. For example, a repository based on GitHub does not need to be at github.com.

* GitHub
* GitLab
* BitBucket
* Azure DevOps
* AWS CodeCommit

## References

* [CREATE GIT REPOSITORY](../../sql-reference/sql/create-git-repository.md)
* [ALTER GIT REPOSITORY](../../sql-reference/sql/alter-git-repository.md)
* [DESCRIBE GIT REPOSITORY](../../sql-reference/sql/desc-git-repository.md)
* [DROP GIT REPOSITORY](../../sql-reference/sql/drop-git-repository.md)
* [SHOW GIT REPOSITORIES](../../sql-reference/sql/show-git-repositories.md)
* [SHOW GIT BRANCHES](../../sql-reference/sql/show-git-branches.md)
* [SHOW GIT TAGS](../../sql-reference/sql/show-git-tags.md)
