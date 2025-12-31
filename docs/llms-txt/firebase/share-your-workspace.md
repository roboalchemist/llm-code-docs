# Source: https://firebase.google.com/docs/studio/share-your-workspace.md.txt

| **Note:** This feature is highly experimental. Use it with caution.

To facilitate code collaborations like pair programming and testing,Firebase Studiolets you share your workspace with anyone who has a Google Account.
| **Caution:** Users added to your workspace have complete access to the VM's entire file system, which may contain sensitive files like private keys and access tokens. Share your workspace only with people you trust. While this approach helps other users view the exact state of your workspace, it means that they see everything on your workspace.

Note that when multiple users edit the same file in a shared workspace, changes might be overwritten. There is no merge conflict notification or support at this time.

To share your workspace, follow these instructions:

1. Open[Firebase Studio](https://studio.firebase.google.com/).

2. Open a workspace.

3. Press`Cmd+Shift+P`. The command selector appears.

4. Enter**Firebase Studio** in the command selector and select**Share Workspace** from the list of commands. The**Workspace sharing and collaboration window**appears.

5. Enter the email addresses of the users you want to add to your workspace.

6. Click**Share**.

7. Copy the new workspace URL and share it with the person you added to your workspace. Users can view a list of workspaces shared with them by opening the**Shared with you** tab in theFirebase Studiodashboard. Collaborators don't receive email notifications for newly-shared workspaces at this time.

## Share your preview for feedback

If you're only trying to share your work-in-progress app with others to get their feedback, you can[temporarily make your preview publicly accessible](https://firebase.google.com/docs/studio/preview-apps#share), and send them a direct link to the preview.

## Next steps

- Learn how to[publish your app to Firebase orGoogle CloudfromFirebase Studio](https://firebase.google.com/docs/studio/deploy-app).