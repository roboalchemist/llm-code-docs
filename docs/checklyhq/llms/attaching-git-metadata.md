# Source: https://checklyhq.com/docs/cli/attaching-git-metadata.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Attaching Git metadata

The CLI can attach git metadata like `branch`, `commit sha`, `owner` and more when executing the `test --record` and `deploy` commands. This way you can keep track of
your test sessions and deployed resources in the UI and cross-reference them with any updates to your code.

For example, in the screenshot below we ran a **test session** from our CI server after the project was deployed to our
Staging environment with the `npx checkly test --record` command.

<img src="https://mintcdn.com/checkly-422f444a/YgQcQD6j5p9gqjr5/images/docs/images/cli/test_session_git_data.png?fit=max&auto=format&n=YgQcQD6j5p9gqjr5&q=85&s=d813304e1568ae3a0fca03f0c16805c0" alt="test session with git info" width="1970" height="811" data-path="images/docs/images/cli/test_session_git_data.png" />

After the test succeeds, we **deploy** this check so it runs as a monitor with `npx checkly deploy`.

<img src="https://mintcdn.com/checkly-422f444a/YgQcQD6j5p9gqjr5/images/docs/images/cli/browser_check_git_data.png?fit=max&auto=format&n=YgQcQD6j5p9gqjr5&q=85&s=496a12e62e13680d52277bc853949660" alt="browser check with git info" width="2252" height="775" data-path="images/docs/images/cli/browser_check_git_data.png" />

## Environment variables

The CLI will attempt to auto-detect and parse git specific information from your local machine or CI environment, but you
can also set these data items specifically by using environment variables.

| Item               | Auto  | Variable                                               | Description                                 |
| ------------------ | ----- | ------------------------------------------------------ | ------------------------------------------- |
| **Repository**     | false | `repoUrl` in `checkly.config.ts` or `CHECKLY_REPO_URL` | The URL of your repo on GitHub, GitLab etc. |
| **Commit hash**    | true  | `CHECKLY_REPO_SHA`                                     | The SHA of the commit.                      |
| **Branch**         | true  | `CHECKLY_REPO_BRANCH`                                  | The branch name.                            |
| **Commit owner**   | true  | `CHECKLY_REPO_COMMIT_OWNER`                            | The committer's name or email.              |
| **Commit message** | true  | `CHECKLY_REPO_COMMIT_MESSAGE`                          | The commit message.                         |
| **Environment**    | false | `CHECKLY_TEST_ENVIRONMENT`                             | The environment name, e.g. "staging"        |

For example, if you want to specifically set the Environment you invoke:

```bash Terminal theme={null}
CHECKLY_TEST_ENVIRONMENT=Production npx checkly test --record
```

Or, if you want to set repo URL you invoke:

```bash Terminal theme={null}
CHECKLY_REPO_URL="https://my.git.solution/project/" npx checkly test --record
```


Built with [Mintlify](https://mintlify.com).