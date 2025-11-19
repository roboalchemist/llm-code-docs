# Source: https://www.aptible.com/docs/how-to-guides/app-guides/integrate-aptible-with-ci/circle-cl.md

# Circle CI

Once you've completed the steps for [CI Integration](/how-to-guides/app-guides/integrate-aptible-with-ci/overview), set up Circle CI as follows:

**Step 1:** Add the private key you created for the robot user to your Circle CI project through the **Project Settings > SSH keys** page on Circle CI.

**Step 2:** Add a custom deploy step that pushes to Aptible following Circle's [deployment instructions](https://circleci.com/docs/configuration#deployment). It should look something like this (adjust branch names as needed):

```ruby  theme={null}
deployment:
  production:
    branch: production
    commands:
      - git fetch --depth=1000000
      - git push git@beta.aptible.com:$ENVIRONMENT_HANDLE/$APP_HANDLE.git $CIRCLE_SHA1:master
```

> 📘 In the above example, `git@beta.aptible.com:$ENVIRONMENT_HANDLE/$APP_HANDLE.git` represents your App's Git Remote.

> Also, see [My deploy failed with a git error referencing objects, trees, revisions or commits](/how-to-guides/troubleshooting/common-errors-issues/git-reference-error) to understand why you need `git fetch` here.
