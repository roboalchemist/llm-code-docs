# Source: https://docs.zapier.com/platform/news/2025/labeled-versions.md

# Source: https://docs.zapier.com/platform/manage/labeled-versions.md

# Source: https://docs.zapier.com/platform/news/2025/labeled-versions.md

# Source: https://docs.zapier.com/platform/manage/labeled-versions.md

# Work with labeled versions

> Use labeled versions to iterate on integration changes without committing to a semantic version number.

Labeled versions let you develop and test changes without committing to a [semantic version number](/platform/manage/versions#version-numbering) until you're ready to ship.

<Note>
  Labeled versions are only available in Platform CLI as of version 17.7.2.
</Note>

## What are labeled versions?

A **labeled version** uses the format `MAJOR.MINOR.PATCH-LABEL`, where:

* `MAJOR.MINOR.PATCH` can be either the next expected semantic version number for [pre-releases](https://semver.org/#spec-item-9), or `0.0.0` for snapshots<sup>\*</sup>.
* `label` is your custom identifier (e.g., `JIRA-1234`, `new-trigger`, `oauth-v2`)

A special variant of labeled versions is the **snapshot version**. This is a labeled version where `MAJOR.MINOR.PATCH` is `0.0.0`, making no assumption about the nature of the change and thus what the next expected semantic version number might be.

This gives you flexibility to:

* Iterate on changes without version number commitments
* Test thoroughly before deciding semantic versioning impact
* Work on multiple features in parallel with different labels
* Focus on building rather than version planning

When you're ready to release, you update to the appropriate semantic version (like `1.0.1` or `1.1.0`), push that version, and promote it.

## When to use labeled versions

Here are our recommendations for using labeled versions:

**Use labeled versions** for all development work. This approach gives you maximum flexibility to defer versioning decisions until you're ready to ship.

Specifically, **use snapshot versions** (`0.0.0-my-feature`) as the default, to test local changes and e.g. in a CI/CD workflow that runs on merge/pull requests.

Alternately, **use labeled pre-release versions** (`2.0.0-beta`) if you already know the version number, e.g. you are working towards a new major version that you would like other maintainers to thoroughly test.

Finally, **use semantic versions** (`1.2.3`) only when you're ready to promote changes to users. Semantic versions are what your users will see and interact with in the Zap Editor or other Zapier products.

## Creating a labeled version

You can create a labeled version in two ways:

**Option 1: Use the `--snapshot` flag** (recommended for quick iteration)

```bash  theme={null}
zapier-platform push --snapshot JIRA-1234
```

<Note>
  When using `--snapshot`, you must include the flag each time you push updates
  to the same labeled version.
</Note>

**Option 2: Set version in `package.json`** (recommended for CI/CD workflows)

```json  theme={null}
{
  "version": "0.0.0-JIRA-1234"
}
```

Then use `zapier-platform push` without the flag. This approach is useful when you want the version controlled in your repository or when automating deployments.

You can use any label that describes your work, such as:

* `0.0.0-webhooks`
* `0.0.0-new-trigger`
* `0.0.0-oauth-v2`
* `0.0.0-refactor`

<Note>Labels must be 12 characters or fewer.</Note>

## Working with labeled versions

Once you've created a labeled version, you can:

* Make changes to triggers, actions, and authentication
* Test with your team (admins and collaborators)
* Iterate as much as needed by pushing updates
* Push different labeled versions for parallel work

<Warning>
  **Limitations:** Labeled versions are for development by your integration team
  only. You cannot promote labeled versions to public status, migrate users
  to/from them, or share them with invited users outside your integration team.
  When you're ready to release changes to users, update to a semantic version
  (like `1.0.1` or `1.1.0`) and promote that version.
</Warning>

## Moving from labeled to semantic versions

When your changes are ready to ship:

1. Decide the appropriate [semantic version](/platform/manage/versions#version-numbering) based on your changes:
   * **Patch** (`1.0.0` → `1.0.1`): Bug fixes, help text updates, backward-compatible changes
   * **Minor** (`1.0.0` → `1.1.0`): New features, no breaking changes
   * **Major** (`1.0.0` → `2.0.0`): Breaking changes requiring user intervention

2. Update the version in your `package.json` to remove the label:

```json  theme={null}
{
  "version": "1.0.1"
}
```

3. Push the new version:

```bash  theme={null}
zapier-platform push
```

4. [Promote the new version](/platform/manage/promote) to make it available to users

## Recommended workflow

Here's the recommended development workflow:

1. **Start with a snapshot**: Create a labeled version with the `zapier-platform push --snapshot` command or by setting the version in `package.json`.

2. **Develop and iterate**: Make your changes and push repeatedly. You can keep pushing to the same snapshot as you iterate

3. **Test with your team**: Admins and collaborators can test the snapshot in their Zaps

4. **Update to semantic version**: When ready to ship, change the version in `package.json` to the appropriate semantic version (e.g., `1.0.1`) and push

5. **Promote**: Run validation checks and promote the new version

6. **Clean up** (optional): Delete the snapshot version if you no longer need it

This workflow keeps development flexible while ensuring only properly versioned integrations reach your users.

## FAQ

### Can I have multiple labeled versions at the same time?

Yes! You can create multiple labeled versions for different features or experiments. For example:

* `0.0.0-trigger-abc`
* `0.0.0-oauth-v2`
* `0.0.0-perf-fixes`
* `0.0.0-feature-a`
* `0.0.0-feature-b`

This lets you work on multiple features in parallel without interfering with each other.

### How do I incorporate changes from other engineers into my labeled version?

When multiple engineers are working on the same integration using many labeled versions, use Git to keep your labeled version up to date:

1. **Rebase from main**: Pull the latest changes from your main branch to get the current promoted version
2. **Test your changes**: Ensure your feature still works with the latest code
3. **Update to semantic version**: Update your `package.json` to the appropriate semantic version
4. **Push and promote**: Push and promote the new version

For example:

```bash  theme={null}
# Rebase from main to get latest code
git rebase main

# Test your changes locally
# (Optional) Push snapshot again if you need to test with your team:
# zapier-platform push --snapshot my-feature

# When ready, update package.json version to 1.0.1
# Then push and promote
zapier-platform push
zapier-platform promote 1.0.1
```

This ensures your changes incorporate the latest code before releasing. If there are multiple features ready to ship, coordinate with your team to promote them together.

### What happens to my labeled version when I push a semantic version?

The labeled version remains as a separate version. You can:

* Keep the labeled version for future development
* Continue pushing to it for ongoing work
* Push a new labeled version with a different label for other features
* Delete the labeled version if you no longer need it

### Can I migrate users from a semantic version to a labeled version?

No. Labeled versions are for development only and cannot be used as migration targets. This protects your users from accidentally being moved to unstable development versions.

### Can I promote a labeled version directly?

No. You must first push a semantic version (without the label suffix), then promote that semantic version. This ensures that only promotion-ready code with proper version numbers reaches your users.

### How do labeled versions affect my user count and limits?

Labeled versions follow the same rules as other private versions:

* You can edit versions with fewer than 5 active users
* Versions with 5+ users cannot be edited directly
* Sharing limits work the same way as regular private versions

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
