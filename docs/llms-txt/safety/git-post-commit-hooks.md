# Source: https://docs.safetycli.com/safety-docs/installation/securing-git-repositories/git-post-commit-hooks.md

# Git Post-Commit Hooks

## Scanning your development environments

It's a best practice run your security scans as soon as possible in the development life-cycle - this is called shift left security.

Running PyUp security scans in your development environments is as simple as adding Safety's CLI scan to your git pre-commit hook files. This is a file that is executed before a git commit is run, and a failing command in this process will halt the commit itself, and warn the developer of the issue.

## Adding Safety CLI to your git pre-commit hooks

To add Safety scans to your git pre-commit hooks, first find your git pre-commit hook file, located at `.git/hooks/pre-commit`.

If you haven't already set up a pre-commit hook it may still be named `pre-commit.sample`. In that case, rename it to `pre-commit` and that file will start running before your git commits.

Once you've got the file ready, add the following to the bottom of the file:

Shell

```shell
# Add Safety Scan
exec safety scan
```

And that's it. Now Safety will scan your development machine before any code is pushed to central source control systems.
