# Source: https://www.aptible.com/docs/how-to-guides/app-guides/integrate-aptible-with-ci/travis-cl.md

# Travis CI

Once you've completed the steps for [CI Integration](/how-to-guides/app-guides/integrate-aptible-with-ci/overview), set up Travis CI as follows:

**Step 1:** Encrypt the private key you created for the robot user and store it in the repo. To do so, follow Travis CI's [instructions on encrypting files](http://docs.travis-ci.com/user/encrypting-files/). We recommend using the "Automated Encryption" method.

**Step 2:** Add an `after_success` deploy step. Here again, follow Travis CI's [instructions on custom deployment](http://docs.travis-ci.com/user/deployment/custom/). The `after_success` in your `.travis.yml` file should look like this:

```ruby  theme={null}
after_success:
  - git fetch --depth=1000000
  - chmod 600 .travis/deploy.pem
  - ssh-add .travis/deploy.pem
  - git remote add aptible git@beta.aptible.com:$ENVIRONMENT_HANDLE/$APP_HANDLE.git
  - git push aptible master
```

<Tip> 📘 In the above example, `git@beta.aptible.com:$ENVIRONMENT_HANDLE/$APP_HANDLE.git` represents your App's Git Remote. </Tip>

> Also, see [My deploy failed with a git error referencing objects, trees, revisions or commits](/how-to-guides/troubleshooting/common-errors-issues/git-reference-error) to understand why you need `git fetch` here.
