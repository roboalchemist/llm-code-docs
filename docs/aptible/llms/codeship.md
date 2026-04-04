# Source: https://www.aptible.com/docs/how-to-guides/app-guides/integrate-aptible-with-ci/codeship.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Codeship

You don't need to create a new SSH public key for your robot user when using Codeship. Once you've completed the steps for [CI Integration](/how-to-guides/app-guides/integrate-aptible-with-ci/overview), set up Codeship as follows:

**Step 1:** Copy the public key from your Codeship project's General Settings page, and add it as a [new key](/core-concepts/security-compliance/authentication/ssh-keys) for your robot user.

**Step 2:** Add a Custom Script deployment in Codeship with the following commands:

```bash  theme={null}
git fetch --depth=1000000
git push git@beta.aptible.com:$ENVIRONMENT_HANDLE/$APP_HANDLE.git $CI_COMMIT_ID:master
```

> 📘 In the above example, `git@beta.aptible.com:$ENVIRONMENT_HANDLE/$APP_HANDLE.git` represents your App's Git Remote.

> Also, see [My deploy failed with a git error referencing objects, trees, revisions or commits](/how-to-guides/troubleshooting/common-errors-issues/git-reference-error) to understand why you need `git fetch` here.
