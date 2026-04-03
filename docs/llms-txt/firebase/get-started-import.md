# Source: https://firebase.google.com/docs/studio/get-started-import.md.txt

Firebase Studiooffers a streamlined way to import existing web app projects into aFirebase Studioworkspace, letting you continue to work on your existing projects withFirebase Studio's AI-powered assistance and streamlined development, deployment, and monitoring capabilities.

You can import projects from a source repository (GitHub, GitLab, or Bitbucket), from Figma with the[Builder.io Figma plugin](https://www.builder.io/c/docs/builder-figma-plugin), or from a local archive file.Firebase Studiosupports importing gzipped tar files and zip files under 100 MiB.

You can also duplicate an existing project to create a copy of it.

## Get started

Import from source controlUpload projectImport from Figma with Builder.io pluginDuplicate an existing project

### Step 1: Import your project

1. Log into your Google Account and open[Firebase Studio](http://studio.firebase.google.com/).

2. Click**Import a project** . The**Import project**dialog appears.

3. In the**Repo URL**field, enter your GitHub, GitLab, or Bitbucket repository URL.

4. Enter a name for your project.

5. If you're importing a Flutter project, enable**This is a Flutter app**. If not, leave the checkbox unchecked.

6. Click**Import**.

7. If the repository is private, you'll be prompted to authenticate to the respective provider:

   - For GitHub, follow the prompts to copy an access token.
   - For GitLab, you can use your account password or create a[personal account token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)
   - For Bitbucket, use your username (not email) and an[app password](https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/)to authenticate.

### Step 2: Install dependencies

By default,Firebase Studiodoesn't install dependencies when you import a project, so you'll need to do this manually after your first import.

For example, if you import a Flutter app, you should run`flutter pub get`in the terminal, or`npm install`for Javascript or TypeScript apps.

You can change this for all future users of your template and for future imports by adding an[`onCreate`hook to your`dev.nix`file](https://firebase.google.com/docs/studio/devnix-reference#idxworkspaceoncreate)in your project repository. You can configure`onCreate`to run the build command appropriate for your project (for example,`npm install`or`flutter pub
get`).

After this is configured, dependencies are installed automatically whenever users import your repository intoFirebase Studio.

## Next steps

- [Learn more aboutFirebase Studioworkspaces](https://firebase.google.com/docs/studio/get-started-workspace).
- [Customize yourFirebase Studioworkspace](https://firebase.google.com/docs/studio/customize-workspace).
- [Discover how Gemini inFirebasecan assist and accelerate your app development](https://firebase.google.com/docs/studio/ai-assistance)with its ability to help answer questions, generate and edit code, fix bugs, and run tools.
- [Turn your project into a custom template](https://firebase.google.com/docs/studio/custom-templates).