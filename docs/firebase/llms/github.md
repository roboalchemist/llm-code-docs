# Source: https://firebase.google.com/docs/studio/github.md.txt

You can integrateFirebase Studiowith GitHub to ensure that your projects are backed up and can be shared with others.
| **Note:** If you're using theApp Prototyping agent, note that it commits its changes to your local branch on every response.Firebase StudioinCodeview requires you to manually commit changes after you make them. You can do this from the Source Control pane or from the Terminal in[Firebase StudioCodeview](https://firebase.google.com/docs/studio/get-started-workspace).

## Before you begin

- [Create an account on GitHub](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github)

## Add your project to GitHub

To add your project to GitHub:

1. In your open workspace, from the**View** menu, select**Source Control** or press`Ctrl-Shift-G`(`Cmd-Shift-G`in MacOS).

   If you're using theApp Prototyping agentinPrototyperview, first click![Code switch icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg)**Switch to Code** to openCodeview.
2. Review the Source Control graph. If there are any uncommitted changes, use either of the these two methods to commit them locally:

   - From the Source Control pane:

     1. Click**Commit**.

     2. When prompted to stage changes, click**Yes**.

     3. Add a commit message that describes your changes in the`COMMIT_EDITMSG`file that opens.

     4. Save and close the file.

   - From the Terminal:

     1. To view uncommitted files, run:

            git status

     2. Add the files to source control:

        - To add single files, run:

              git add [list of files]

        - To add all uncommitted files, run:

              git add *

     3. Commit your changes:

            git commit -m "Your commit message describing the changes."

   | **Warning:** Inspect the files that you plan to upload to GitHub to ensure you are not uploading any API keys or other secrets. Add any exclusions to the[`.gitignore`file](https://docs.github.com/en/get-started/git-basics/ignoring-files).
3. In the**Source Control** pane, click**Publish Branch.**

4. When prompted to log into Git, click**Allow**and follow the instructions to authenticate.

5. After you've authenticated, return to theFirebase Studiowindow and enter a name for your project in the active field, then select one of the following:

   - **Publish to GitHub private repository**to publish your app privately on GitHub.

   - **Publish to GitHub public repository**to publish your app publicly on GitHub.

| **Tip:** We recommend uploading to a private repository at first. You can set the repository to public on GitHub at any time.

## Next steps

- [Customize yourFirebase Studioworkspace](https://firebase.google.com/docs/studio/customize-workspace).
- [Create a custom template](https://firebase.google.com/docs/studio/custom-templates).