# Source: https://docs.warp.dev/support-and-billing/updating-warp.md

# Updating Warp

Warp automatically checks for updates on startup. A notification will appear in the top right corner of the Warp window when a new update is available.

![Update Available](https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-976978f8711aaeb81d33778ed5c3a9d0a5820831%2Fupdate-available.png?alt=media\&token=61b8a26b-ed1b-4cc9-87ee-337fa765f106)

To check for updates, search for "update" in the [Command Palette](https://docs.warp.dev/terminal/command-palette) or go to `Settings > Accounts` and click "Check for Update".

![Check for Update manually](https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-99ab35e6148db2f437666654403f1e91bcb92151%2Fcheck-for-update.gif?alt=media)

If nothing happens, it means you already have the latest stable build.

## Auto-Update Issues

Warp cannot auto-update if it does not have the correct permissions to replace the running version of Warp If this is the case, a banner will prompt you to manually update Warp.

![Update Available](https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-5b32279175fc86324225ee14a9eb1b38db1f8489%2Fupdate-available-bar.png?alt=media)

There are 2 main causes of this:

1. You opened Warp directly from the mounted volume instead of dragging it into your Applications directory. If this is the case, the easiest fix is to quit Warp, drag the application into /Applications, and restart Warp.
2. You are a non-Admin user. This can happen if you use a computer with multiple profiles. If you have admin access on the computer, opening the app with the admin user should fix the auto-update issues.

{% hint style="info" %}
(Oct 2022): There is a known issue with [auto-update on MacOS Ventura](https://docs.warp.dev/known-issues#auto-update-on-macos-ventura).
{% endhint %}
