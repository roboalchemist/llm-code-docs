# Source: https://firebase.google.com/docs/extensions/publishers/upload-and-publish.md.txt

<br />

This page explains how you can publish an extension on Extensions Hub.

## Before you begin

To publish an extension, first you need to[register as an extensions publisher](https://firebase.google.com/docs/extensions/publishers/register).

## Verifiable sources

All extensions published on Extensions Hub must have a publicly-verifiable source. Rather than upload your extension source code directly to Extensions Hub, you instead specify the source location and Extension Hub will download it and build it from there.

Currently, this means making your extension source code available on a public GitHub repository.

Uploading from a verifiable source has several benefits:

- Users can inspect the source code of the specific revision of the extension that will be installed.
- You can ensure you upload only what you intend to upload, and not, for example, work in progress, or stray files remaining from development.

| **Note:** You can upload pre-release versions of an extension from local source. These releases will not be listed on Extensions Hub.

## Recommended development cycle

The Firebase Extensions development tools support uploading pre-release versions of your extensions, which makes it easy for you to test your extensions and the extension installation process in the same environment in which they will eventually be released.

This capability makes possible a development cycle like the following:

1. Develop and rapidly iterate on your extension using the[Firebase Emulator Suite](https://firebase.google.com/docs/emulator-suite/use_extensions).

2. Test your extension in a real project by installing it from local source:

       firebase ext:install <var translate="no">/path/to/extension</var>
       firebase deploy --only extensions

3. Upload a pre-release version to Extensions Hub (see below). Distribute the installation link for wider testing, and iterate by uploading more pre-release versions as necessary.

4. Upload the final, stable, version to Extensions Hub (see below) and submit it for review. If the extension passes review, it will be published on Extension Hub.

5. Increment the version number in`extension.yaml`and repeat this cycle for the next version of your extension.

## Upload a new extension

To upload an extension for the first time:

1. **Optional**: Commit your code to a public GitHub repository.

2. Run the Firebase CLI's`ext:dev:upload`command:

   ### GitHub

       firebase ext:dev:upload <var translate="no">your_publisher_id</var>/<var translate="no">your_extension_id</var>

   ### Local source

       cd <var translate="no">/path/to/extension</var>
       firebase ext:dev:upload <var translate="no">your_publisher_id</var>/<var translate="no">your_extension_id</var> --local

   In your command invocation, you specify the following:
   - The publisher ID you[registered](https://firebase.google.com/docs/extensions/publishers/register).

   - An ID string that will identify the extension. Name your extensions with the following format:<var translate="no">firebase-product</var>`-`<var translate="no">description-of-tasks-performed</var>. For example:`firestore-bigquery-export`

   The command will prompt you for additional information:
   - If you're uploading from GitHub:

     - The URL to the extension's repository in GitHub. Note that a repository can contain multiple extensions as long as each extension has a unique root.

       When you upload a new extension for the first time, the repository will be registered as the canonical source for your extension.
     - The directory in the repository that contains your extension.

     - The Git reference of the commit you want to build your extension version source from. This can be a commit hash, tag, or branch name.

   - The release stage of the version you're uploading.

     The`alpha`,`beta`, and`rc`(release candidate) stages are for uploading pre-release versions for testers to install. Use one of these stages for the initial upload of a new extension.

     The`stable`stage is used for public releases to be published on Extensions Hub. Uploading a`stable`release will automatically initiate a review, and, if it passes, will publish the extension.

   Notice you don't specify a version number---this value comes from the`extension.yaml`file. When you upload a pre-release extension version, the stage and upload number is appended to the version. For example, if`extension.yaml`specifies version 1.0.1 and you upload a release candidate, it would result in the version`1.0.1-rc.0`; uploading another release candidate of the same version would automatically increment the count, resulting in`1.0.1-rc.1`, and so on.

Now that you've uploaded a pre-release version of the extension, you can share it with others for testing. Users can install your extension in either of two ways:

- **With the console**: Users can can install the extension by clicking a link with the following format:

  ```
  https://console.firebase.google.com/project/_/extensions/install?ref=your_publisher_id/your_extension_id@version
  ```

  You can share the direct link with your testers.
- **With the CLI** : Users can can install the extension by passing the extension ID string to the`ext:install`command:

  ```
  firebase ext:install your_publisher_id/your_extension_id@version \
      --project=destination_project_id
  ```

## Upload an updated version

After you've uploaded the first version of an extension, you can upload updates to fix issues, add features, or advance the release stage. When you upload a new version, users who have an older version of your extension installed will be prompted in theFirebaseconsole to upgrade.

To upload an update:

1. **Optional**: Commit your code to a public Git repository.

2. Run the Firebase CLI's`ext:dev:upload`command:

   ### GitHub

       firebase ext:dev:upload <var translate="no">your_publisher_id</var>/<var translate="no">your_extension_id</var>

   This time you won't be prompted to specify the GitHub repository or the extension root directory since they have already been configured for your extension. If you have since refactored your repository structure or migrated to a new repository, you can change them with the command arguments`--root`and`--repo`.

   ### Local source

       cd <var translate="no">/path/to/extension</var>
       firebase ext:dev:upload <var translate="no">your_publisher_id</var>/<var translate="no">your_extension_id</var> --local

## Submit an extension for publication

When you're ready to publicly release your extension:

1. Commit your code to a public Git repository. (Required for public releases.)

2. Run the Firebase CLI's`ext:dev:upload`command, specifying`stable`as the release stage:

       firebase ext:dev:upload <var translate="no">your_publisher_id</var>/<var translate="no">your_extension_id</var>

3. If you've previously published a version of your extension, uploading a new stable release will automatically submit the extension for review.

   If you uploaded the extension's first stable release, find the extension on your[publisher dashboard](https://console.firebase.google.com/project/_/publisher/dashboard), and click**Publish to Extensions Hub**.

Once submitted, review can take a few days. If accepted, the extension will be published to Extensions Hub. If rejected, you'll get a message explaining the reason; you can then address the reported issues and resubmit for review.

To expedite the review and increase your chances of passing on the first try, before submitting, double-check the following:

- You have thoroughly tested your extension and the installation process.
- Your documentation is complete and correct, and renders well in the Firebase console.
- Your publisher name and branding clearly and accurately identify you as the publisher.
- Your extension's name, description, and icon clearly and accurately represent your extension's purpose.
- You have applied helpful and accurate tags.
- You have declared in`extension.yaml`all Google and non-Google APIs you use, and all event types your extension emits.
- You are requesting access to only the roles necessary for the extension to function, and you have clearly explained to users why you need such access.
- Your source files are clearly licensed under the terms of`Apache-2.0`.

## Manage uploaded and published extensions

### List your uploaded extensions

To list the extensions you've uploaded under your publisher ID, do one of the following:

#### Publisher dashboard

View them on the[publisher dashboard](https://console.firebase.google.com/project/_/publisher/dashboard).

#### Firebase CLI

Run the`ext:dev:list`command:  

    firebase ext:dev:list <var translate="no">your_publisher_id</var>

### View usage of your uploaded extensions

To view the usage of the extensions you've uploaded under your publisher ID, do one of the following:

#### Publisher dashboard

The[publisher dashboard](https://console.firebase.google.com/project/_/publisher/dashboard)has cumulative usage metrics for all your extensions and individual metrics for each extension.

#### Firebase CLI

Run the`ext:dev:usage`command:  

    firebase ext:dev:usage <var translate="no">your_publisher_id</var>

### Deprecate a version of an extension

At some point, you might want to deprecate an old version of your extension. For example, if you release a new version that fixes a critical bug or updates a dependency with an important security update, it's important to prevent new users from installing an old version and to encourage existing users to upgrade.

To deprecate a version of an extension, do one of the following:

#### Publisher dashboard

1. On the[publisher dashboard](https://console.firebase.google.com/project/_/publisher/dashboard), click the extension to open its details view.
2. Select the version you want to deprecate.
3. Click**Deprecate version**.

#### Firebase CLI

Run the`ext:dev:deprecate`command:  

    firebase ext:dev:deprecate <var translate="no">your_publisher_id</var>/<var translate="no">your_extension_id</var> <var translate="no">versions</var> \
        [--message "<var translate="no">deprecation_message</var>"]

You can specify a single version or range of versions. Examples:

- `1.0.2`
- `1.1.0-1.1.7`
- `<1.2.0`
- `1.1.*`

Deprecated versions of an extension are not listed on Extensions Hub and cannot be installed. Users whose projects have a deprecated version installed will see a message encouraging them to upgrade; they can still use and re-configure the extension in the meantime.

If every version of an extension is deprecated, the extension is considered deprecated and it will be delisted from Extensions Hub. Uploading a new version of a deprecated extension will automatically initiate a review and upon acceptance, publish it on Extensions Hub once again.

To reverse a deprecation, use the publisher dashboard, or run the Firebase CLI's`ext:dev:undeprecate`command:  

```
firebase ext:dev:undeprecate your_publisher_id/your_extension_id versions
```

## Appendix: Troubleshooting build errors

When you upload your extension, the backend first builds your source code using the following process:

1. Clones your GitHub repository and checks out the source ref specified.

2. Installs NPM dependencies by running`npm clean-install`in every function source directory specified in`extension.yaml`(see`sourceDirectory`in[Cloud Function resources](https://firebase.google.com/docs/extensions/reference/extension-yaml#resources)).

   Note the following:
   - Each`package.json`file must have a corresponding`package-lock.json`file. For more information, see[npm-ci](https://docs.npmjs.com/cli/v9/commands/npm-ci#example).

   - Post-install scripts will not be run during dependency installation. If your source code build relies on post-install scripts, refactor it before uploading.

3. Builds your code by running`npm run build`in every function source directory specified in`extension.yaml`.

Only the root directory of your extension will be saved in the final extension package that will be shared.

If you get build errors while uploading your extension, replicate the build steps above locally in a fresh directory until there are no errors, then try uploading again.