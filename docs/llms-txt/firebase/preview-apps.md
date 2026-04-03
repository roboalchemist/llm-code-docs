# Source: https://firebase.google.com/docs/studio/preview-apps.md.txt

Firebase Studiooffers several ways to preview and test your application during development. This includes using theApp Prototyping agentand leveraging the built-in web previewer, and the web and Android previewers available within Firebase Studio workspaces.

## Enable and configure your preview environment

If you use a[template](https://firebase.google.com/docs/studio/get-started-template)or generate your app using theApp Prototyping agent, previews are often already configured for you. If previews aren't already set up in your template, you can configure them in the project's Nix configuration file.

1. From your workspace, open`.idx/dev.nix`.

   Firebase Studioautomatically generates this file when you create a new workspace and includes any applicable preview environments based on the template you select. If the file isn't in yourFirebase Studiocode repository, create it and then set the`idx.previews`attribute to`true`. Then, add configuration attributes, as the following example shows:  

       { pkgs, ... }: {

         # NOTE: This is an excerpt of a complete Nix configuration example.
         # For more information about the dev.nix file in Firebase Studio, see
         # https://firebase.google.com/docs/studio/customize-workspace

         # Enable previews and customize configuration
         idx.previews = {
           enable = true;
           previews = {
             # The following object sets web previews
             web = {
               command = [
                 "npm"
                 "run"
                 "start"
                 "--"
                 "--port"
                 "$PORT"
                 "--host"
                 "0.0.0.0"
                 "--disable-host-check"
               ];
               manager = "web";
               # Optionally, specify a directory that contains your web app
               # cwd = "app/client";
             };
             # The following object sets Android previews
             # Note that this is supported only on Flutter workspaces
             android = {
               manager = "flutter";
             };
           };
         };
       }

   For a full list of Nix attributes inFirebase Studio, see[Nix +Firebase Studio](https://firebase.google.com/docs/studio/customize-workspace#nix+fs).
2. Rebuild your environment:

   - From the command palette (`Cmd+Shift+P`/`Ctrl+Shift+P`), run the**Firebase Studio: Hard restart**command.
   - From the**Environment config updated** notification, click**Rebuild environment**.

   When you rebuild the environment after modifying your`dev.nix`file, the preview panel appears in your workspace showing either or both of**Android** and**Web**tabs, depending on what you've enabled.

| **Key Point:** You can preview your app in a separate browser tab by clicking the**Open in new window** icon in the preview window toolbar. This pop-out link is also useful for demoing your work in progress to a friend or colleague through[workspace sharing](https://firebase.google.com/docs/studio/share-your-workspace). If you close a preview and want to re-open it, open the command palette and search for the appropriate preview command.

## Use app previews

Firebase Studiooffers web previews on Chrome and Android emulators in Flutter workspaces that install your app on the preview environment. This lets you test your app fully, from end to end, directly from your workspace.

### Refresh previews for web and Android

Firebase Studiohooks into the hot reload functionalities of the underlying frameworks (like`npm run start`and`flutter hot-reload`) to give you a streamlined inner development loop.Firebase Studioprovides the following types of reloads:

- **Automatic Hot Reload** : Hot reloads are automatically performed when you save a file. Sometimes known as*Hot Module Replacement*(or HMR), a hot reload updates your app without reloading the page (for web apps) or without restarting or reinstalling the app (for emulators). This approach is useful for preserving your app's live state but might not always work as intended.

- **Manual Full Reload**: This option is equivalent to a page refresh (for web apps) or an app restart (for emulators). We recommend using a full reload to capture significant changes to your source code, such as when refactoring large chunks of code.

- **Manual Hard Restart** : This option performs a complete restart ofFirebase Studio's preview system, which includes stopping and restarting your app's web server.

All reload options are available using either the preview toolbar or the command palette (`Cmd+Shift+P`on Mac or`Ctrl+Shift+P`on ChromeOS, Windows, or Linux), under the**Firebase Studio**category.

To use the preview toolbar, follow these steps:

1. Click the**Reload**icon to refresh the page. This forces a full reload. For a different type of refresh, click the arrow next to the reload icon to expand the menu.

2. Select the refresh option you want from the menu:**Hot Reload** ,**Full Reload** , or**Hard Restart**.

## Share your web preview with others

You can share your app's web preview with others for feedback by enabling access and then sharing the direct link to the preview:

1. In the web preview toolbar, click the![image of a link icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-link.svg)**Share Preview Link**icon, to the right of the address bar to open the sharing menu.

2. Allow others to access your workspace, using one of these options:

   - **Make preview public** : Make your workspace preview publicly accessible. This lets anyone on the Internet reach the preview server running on your workspace*while your workspace is active*, and until you turn off public access.

   - **Manage workspace access**. Share your workspace with just the people to which you want to give access.

     | **Warning:** Sharing your workspace lets other users make changes to your code and access other private information like authentication tokens saved on the workspace, so only share with those you trust. Learn more at[Share your workspace](https://firebase.google.com/docs/studio/share-your-workspace).
3. Select**Copy preview URL**to copy a direct link to the workspace preview, which you can then send to those you'd like to get feedback from. You can also use the QR code that appears to open your preview on your mobile device.

## Configure autosave and hot reload

By default,Firebase Studioautosaves your work one second after you stop typing, triggering automatic hot reloads. If you wantFirebase Studioto save your work at a different interval, change the autosave setting. You can also turn off autosave.  

#### Configure autosave

1. Open[Firebase Studio](https://studio.firebase.google.com/).
2. Click the**Settings**icon.
3. Search for**Files: Auto Save**and verify that the field is set to \`afterDelay\`.
4. Search for**Files: Auto Save Delay**.
5. Enter a new autosave delay interval, expressed in milliseconds. Changes to your work are now automatically saved based on the new autosave delay setting.  

#### Turn off autosave

1. Open[Firebase Studio](https://firebase.google.com/docs/studio/https/studio.firebase.google.com).
2. Click the**Settings**icon.
3. Search for**Files: Auto Save**.
4. Click the drop-down and select**off**.

## Preview backend disconnected

You can safely disregard the "Preview backend disconnected" message.

## Next steps

- [Publish with Firebase](https://firebase.google.com/docs/studio/deploy-app).
- [Monitor your app](https://firebase.google.com/docs/studio/monitor).