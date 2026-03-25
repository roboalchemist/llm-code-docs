# Source: https://redocly.com/docs/realm/reunite/project/remote-content/edit-remote-content-folder.md

# Edit remote content settings

You can edit settings for remote content folders and files after creation.

## Editable settings

The following remote content settings can be updated:

- **Git provider**: Change to a different provider (GitHub, GitLab, Azure DevOps, Bitbucket)
- **Repository and branch**: Switch to a different repository or branch
- **Content path**: Change the folder or file being synced from the source repository
- **Auto-sync**: Enable or disable automatic synchronization
- **Auto-merge**: Enable or disable automatic merging of sync pull requests
- **URL and interval** (for URL sources): Update the source URL or sync frequency


Update these settings in Reunite either in the file tree of the editor, or on the **Remote content** page.

## Non-editable settings

You cannot update the following settings:

- **Mount path**: The destination folder or file location in your project


To change the mount path, add a new remote content entry with the desired path, then delete the previous one.

## Edit remote content

Edit settings on existing remote content from either the file tree of the editor or the Remote content page in Reunite.

To edit remote content settings:

1. From the file tree of the editor, right-click the remote content (folders and files with remote content have a cloud icon), then select **Edit**.
Alternatively, from the Remote content page, select the options menu on the far right side of the table row, then select **Edit**.

2. Modify the settings as needed. The available settings depend on your content source type:
  - **Git sources**: Change provider, repository, branch, folder/file path, auto-sync, or auto-merge settings.
  - **URL sources**: Change the source URL, sync interval, auto-sync, or auto-merge settings.
  - **CI/CD sources**: Change auto-merge settings.
3. Select **Save** or **Next** to apply changes.
Reunite creates a pull request with your changes.
4. Review and merge the pull request to apply the updated settings.


## Resources

- **[Remote content concepts](/docs/realm/reunite/project/remote-content/remote-content)** - Understand the remote content feature including supported source types, sync mechanisms, and auto-merge capabilities
- **[Add remote files with one-way sync](/docs/realm/reunite/project/remote-content)** - Guides for setting up remote content from Git providers, URLs, or CI/CD pipelines
- **[Manually sync remote content](/docs/realm/reunite/project/remote-content/manually-sync-remote-content)** - Trigger remote content synchronization manually when auto-sync is disabled