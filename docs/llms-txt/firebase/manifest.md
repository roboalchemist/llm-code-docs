# Source: https://firebase.google.com/docs/extensions/manifest.md.txt

<br />

An*extensions manifest*is a list of extension instances and their configurations. With the manifest, you can:

- Share your extensions configuration with others
- Copy your extensions configuration between different projects (such as from your staging project to your production project)
- Deploy all your extensions at once
- Test how your extensions work with your app using theFirebase Local Emulator Suite
- Commit your extensions configuration to source control
- Include extensions in your CI/CD pipeline

An extensions manifest has two parts:

- The`extensions`section of your`firebase.json`, which is a map of instance ID to extension version reference. For example:

      {
       "extensions": {
         "my-bigquery-extension": "firebase/firestore-bigquery-export@^0.1.18",
         "my-image-resizer": "firebase/storage-resize-images@^0.1.22",
       }
      }

- `.env`files containing the configuration for each of your extension instances, in the`extensions/`subdirectory of your Firebase project directory. For example, an instance of the`storage-resize-images`might have an`.env`file like the following:

  ```
  IMAGE_TYPE=jpeg
  LOCATION=us-central1
  IMG_BUCKET=${param:PROJECT_ID}.firebasestorage.app
  IMG_SIZES=100x100
  DELETE_ORIGINAL_FILE=false
  ```

<br />

| If you don't want to save configuration data for every extension instance, you can edit the`firebase.json`file and remove the unneeded entries from the`extensions`section.

<br />

## Create an extensions manifest

There are three ways to build an extensions manifest:

- Manage your extensions manifest with the Firebase CLI
- Export a project's extensions configuration
- Edit the manifest files manually

The first two methods are explained below.

### Manage your extensions manifest with the Firebase CLI

You can run most of the Firebase CLI's`ext:`commands with the`--local`option to update the extensions manifest without actually changing the project's current configuration.

For example:  

```
firebase ext:install --local firebase/firestore-bigquery-export
```

Running the above command will prompt you to configure the latest version of`firebase/firestore-bigquery-export`extension and save the configuration to the manifest, but it won't deploy the configuration to your project.

Here are some more examples of commands that modify the extensions manifest:  

    # ext:configure changes the params for an extension instance in your extensions manifest
    $ firebase ext:configure my-bigquery-extension --local

    # ext:update --local updates an instance in your extensions manifest
    # to the latest version of that extension
    $ firebase ext:update my-bigquery-extension --local

    # You can also specify a version if you don't want to update to the latest version
    $ firebase ext:update my-bigquery-extension firebase/firestore-bigquery-export@0.1.10 --local 

    # ext:uninstall --local removes an instance from your extensions manifest
    $ firebase ext:uninstall my-bigquery-extension --local

### Export a project's extensions configuration

To save a project's current extensions configuration to the manifest, do the following:

1. If you haven't already done so,[set up the Firebase CLI](https://firebase.google.com/docs/cli#setup_update_cli)
2. From a shell prompt, change to the project directory. (Your project directory contains the file`firebase.json`).
3. Run the`ext:export`command:  

   ```
   firebase ext:export
   ```

The`ext:export`command will add an`extensions`section to the`firebase.json`file. Additionally, the`ext:export`command creates an`extensions`directory containing an`.env`file for each extension instance you've installed. These files contain the configuration parameters for each instance.

## Test an extensions configuration with theFirebase Local Emulator Suite

Once you've added some extension instances to your extensions manifest, you can test them out using theLocal Emulator Suite.

1. [Install and configure theLocal Emulator Suite](https://firebase.google.com/docs/emulator-suite/install_and_configure).

2. [Start theLocal Emulator Suite](https://firebase.google.com/docs/emulator-suite/install_and_configure#startup):

   - To run the Emulator Suite interactively, run:`firebase emulators:start`
   - To run the Emulator Suite and execute a test script, run:`firebase emulators:exec my-test.sh`

Now, if you have extension instances listed in your manifest, theLocal Emulator Suitewill download the source code of those extensions to`~/.cache/firebase/extensions`. Once they have been downloaded, theLocal Emulator Suitewill start and you'll be able to trigger any of the extensions' background triggered functions and connect your app to the Emulator suite to test their integration with your app.

<br />

| Emulated extension instances can potentially make live calls to third party APIs and unemulated Google APIs. Review each extension's post-install instructions before testing to make sure you are aware of any external calls it makes.

<br />

## Deploy an extensions configuration to a project

Once you've added some extension instances to your extension manifest, you can deploy it to a project using the Firebase CLI. When you deploy with an extensions manifest, you install, update, and configure all the extension instances in the manifest into a project at once.

To deploy an extensions manifest:

1. From a shell prompt, change to the directory that contains the saved extensions configuration. (This is the directory that contains`firebase.json`. If you just ran`ext:export`, you're already in the right directory.)
2. Run the`deploy`command. If you want to deploy the extensions to a project other than the current one, also specify`--project=`:  

   ```
   firebase deploy --only extensions â-project=YOUR_PROJECT_ID
   ```

The`deploy`command will validate each instance configuration, ask if you want to delete any extension instances from your destination project that are not listed in`firebase.json`, and then deploy all of your extension instances.

## Project-specific extension configurations

Saved extensions configurations can be used to deploy to multiple different projects: for example, a staging project and a production project. When doing this, some parameter values may need to be different for each project. Project-specific`.env`files make this possible:

- Put parameter values that differ between projects in`extensions/`<var translate="no">EXTENSION_INSTANCE_ID</var>`.env.`<var translate="no">YOUR_PROJECT_ID</var>
- Put shared parameter values in`extensions/`<var translate="no">EXTENSION_INSTANCE_ID</var>`.env`.

Sometimes, you may want to use a different parameter value when emulating your extensions: for example, you may want to provide a test API key instead of a production one. Put these parameters in a`.local`file:

- Put non-secret parameters you want to use during emulation in`extensions/`<var translate="no">EXTENSION_INSTANCE_ID</var>`.env.local`
- Put secret parameter values in`extensions/`<var translate="no">EXTENSION_INSTANCE_ID</var>`.secret.local`