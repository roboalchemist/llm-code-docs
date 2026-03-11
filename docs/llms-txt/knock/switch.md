# Source: https://docs.knock.app/cli/branch/switch.md

# Switch to a branch

Switches to an existing branch with the given slug.

Switching to the branch will persist until you exit the branch with the `knock branch exit` command by updating the `.knockbranch` file in your directory.

### Flags

- **--force** (boolean): Force switch the branch without confirmation.
- **--create** (boolean): Create the branch if it doesn't exist before switching to it.

```bash title="Switch to a branch"
knock branch switch my-branch
```

```bash title="Switch to a branch and create it if it doesn't exist"
knock branch switch my-branch --create
```
