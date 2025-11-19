# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/git-reference-error.md

# git Reference Error

You may encounter the following error messages when running a `git push` from a CI platform, such as Circle CI, Travis CI, Jenkins and others:

```bash  theme={null}
error: Could not read COMMIT_HASH
fatal: revision walk setup failed
fatal: reference is not a tree: COMMIT_HASH
! [remote rejected] master -> master (missing necessary objects)
! [remote rejected] master -> master (shallow update not allowed)
```

(Where `COMMIT_HASH` is a long hexadecimal number)

## Cause

These errors are all caused by pushing from a [shallow clone](https://www.perforce.com/blog/141218/git-beyond-basics-using-shallow-clones).

Shallow clones are often used by CI platforms to make builds faster, but you can't push from a shallow clone to another git repository, which is why this fails when you try pushing to Aptible.

## Resolution

To solve this problem, update your build script to run this command before pushing to Aptible:

```bash  theme={null}
git fetch --unshallow || true
```

If your CI platform uses an old version of git, `--unshallow` may not be available. In that case, you can try fetching a number of commits large enough to fetch all commits through to the repository root, thus unshallowing your repository:

```bash  theme={null}
git fetch --depth=1000000
```
