# Source: https://graphite-58cc94ce.mintlify.dev/docs/initialize-in-a-repo.md

# Initialize Graphite In A Repository

> Learn how to initialize the Graphite CLI in your git repository.

To use the Graphite CLI in a Git repository, we need to know your trunk branch (typically `main` or `master`). This helps us know where to merge pull requests, and how to synchronize changes from your upstream `origin`.

To initialize your repository, run `gt init`:

```bash Terminal theme={null}
cd ~/my-project
gt init
```

The CLI will prompt you to select a trunk branch for your development flow. Follow the prompt to choose a trunk branch, and press **Enter** to confirm.

This configuration is stored at `.git/.graphite_repo_config` inside each repository you initialize.

<Note>
  If you forget to run `gt init` in your repository, don't worry! All `gt` commands check for initialization first, and will auto-prompt you to choose a trunk branch at the time of running any command.
</Note>
