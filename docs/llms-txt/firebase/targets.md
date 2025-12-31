# Source: https://firebase.google.com/docs/cli/targets.md.txt

***Deploy targets*** are short-name identifiers (that you define yourself) for Firebase resources in your Firebase project, like aHostingsite with unique static assets or a group ofRealtime Databaseinstances that share the same security rules.

Deploy targets are useful when you have[multipleHostingsites](https://firebase.google.com/docs/hosting/multisites), multipleCloud Storagebuckets, or[multipleRealtime Databaseinstances](https://firebase.google.com/docs/database/usage/sharding#edit_and_deploy_for_each_instance). With deploy targets, theFirebaseCLI can deploy settings to a*specific*Firebase resource or group of resources in your project, such as:

- The hosting configuration for each of yourHostingsites
- Static assets from your project directory for each of yourHostingsites
- Security rules shared by multipleRealtime Databaseinstances or multipleCloud Storagebuckets

To set up a deploy target:

1. [Apply a`TARGET_NAME`](https://firebase.google.com/docs/cli/targets#set-up_deploy_targets)to the targeted Firebase resource or group of Firebase resources.
2. In your`firebase.json`file,[reference the associated`TARGET_NAME`](https://firebase.google.com/docs/cli/targets#configure_firebasejson_to_use_deploy_targets)when you're configuring the settings for each resource or group of resources.

When you run[FirebaseCLI commands](https://firebase.google.com/docs/cli/targets#deploy-target-commands)(like`firebase deploy`), theFirebaseCLI pairs each`TARGET_NAME`with its associated Firebase resources. The CLI then communicates to your Firebase project the settings for each resource.
| **Note:** TheFirebaseCLI applies deploy targets to the Firebase resources in the**currently active Firebase project in the CLI** . So, if you're[managing multiple Firebase projects](https://firebase.google.com/docs/cli#project_aliases)with the CLI, configure the deploy targets for each Firebase project.

## Set up deploy targets for your Firebase resources

Using theFirebaseCLI, apply a`TARGET_NAME`(short-name identifier that you define yourself) to a Firebase resource or group of Firebase resources. Firebase supports deploy targets for:

- [Firebase Hostingsites](https://firebase.google.com/docs/cli/targets#set-up-deploy-target-hosting)
- [Cloud Storage for Firebasestorage buckets](https://firebase.google.com/docs/cli/targets#set-up-deploy-target-storage-database)
- [Firebase Realtime Databaseinstances](https://firebase.google.com/docs/cli/targets#set-up-deploy-target-storage-database)

| **Note:** Run allFirebaseCLI commands for deploy targets from the root of your project directory.

The settings for deploy targets are stored in the`.firebaserc`file in your project directory, so you only need to set up deploy targets one time per project.

### Set up deploy targets forHosting

To create a deploy target and apply a`TARGET_NAME`to aHostingsite, run the following CLI command:

<br />

```
firebase target:apply TYPE TARGET_NAME RESOURCE_IDENTIFIER
```

<br />

Where the parameters are:

- <var translate="no">TYPE</var>--- the relevant Firebase resource type

  - ForFirebase Hostingsites, use`hosting`.
- <var translate="no">TARGET_NAME</var>--- a unique name for theHostingsite that you're deploying to

- <var translate="no">RESOURCE_IDENTIFIER</var>--- the`SITE_ID`for theHostingsite***as listed in your Firebase project***

For example, if you've[created two sites](https://firebase.google.com/docs/hosting/multisites)(`myapp-blog`and`myapp-app`) in your Firebase project, you could apply a unique`TARGET_NAME`(`blog`and`app`, respectively) to each site by running the following commands:  

```
firebase target:apply hosting blog myapp-blog
```  

```
firebase target:apply hosting app myapp-app
```

### Set up deploy targets forCloud StorageorRealtime Database

To create a deploy target and apply a`TARGET_NAME`to a set ofCloud StorageorRealtime Databaseresources, run the following CLI command:  

```
firebase target:apply TYPE TARGET_NAME RESOURCE-1_IDENTIFIER RESOURCE-2_IDENTIFIER ...
```

Where the parameters are:

- <var translate="no">TYPE</var>--- the relevant Firebase resource type

  - ForCloud Storagebuckets, use`storage`.
  - ForRealtime Databaseinstances, use`database`.
- <var translate="no">TARGET_NAME</var>--- a unique name for the resource or group of resources that share security rules

- <var translate="no">RESOURCE_IDENTIFIER</var>--- the identifiers for the resources***as listed in your Firebase project***(like storage bucket names or database instance IDs) that all share the same security rules

For example, you could apply the`TARGET_NAME`of`main`to a group of three regionalCloud Storagebuckets (that all share the same security rules) by running the following command:  

```
firebase target:apply storage main myproject.firebasestorage.app myproject-eu myproject-ja
```

Note that`myproject.firebasestorage.app`is the identifier for the default bucket, while`myproject-eu`and`myproject-ja`are two additional buckets created in the Firebase project.

## Configure your firebase.json file to use deploy targets

After you've set up deploy targets for your Firebase resources, reference each applied`TARGET_NAME`in your[`firebase.json`](https://firebase.google.com/docs/cli#the_firebasejson_file)configuration file:

1. Create an array of configuration objects for each Firebase resource`TYPE`(`hosting`,`storage`, or`database`).
2. In the arrays, specify the`target`(using the`TARGET_NAME`) and define your settings for the associated Firebase resource or group of resources.

Continuing the examples from above, where your Firebase project has twoHostingsites and threeCloud Storagebuckets (that share the same security rules), your`firebase.json`file would look like this:  

```scdoc
{
  "hosting": [ {
      "target": "blog",  // "blog" is the applied TARGET_NAME for the Hosting site "myapp-blog"
      "public": "blog/dist",  // contents of this folder are deployed to the site "myapp-blog"

      // ...
    },
    {
      "target": "app",  // "app" is the applied TARGET_NAME for the Hosting site "myapp-app"
      "public": "app/dist",  // contents of this folder are deployed to the site "myapp-app"

      // ...

      "rewrites": [...]  // You can define specific Hosting configurations for each site
    }
  ]
}

{
  "storage": [ {
      "target": "main",  // "main" is the applied TARGET_NAME for the group of Cloud Storage buckets
      "rules": "storage.main.rules"  // the file that contains the shared security rules
    }
  ]
}
```

If you have multiple configurations for your resources, you can create multiple deploy targets and specify each one in the`firebase.json`file. All associated resources will be deployed together when you run`firebase deploy`.

## Manage deploy targets

The settings for deploy targets are stored in the`.firebaserc`file in your project directory. You can manage your project's deploy targets by running any of the following commands from the root of your project directory.

|                                                  Command                                                  |                            Description                            |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| `firebase target`                                                                                         | Lists the deploy targets for your current project directory       |
| `firebase target:remove \` <var translate="no">TYPE</var>` `<var translate="no">RESOURCE_IDENTIFIER</var> | Removes a resource from the target to which it's been assigned    |
| `firebase target:clear \` <var translate="no">TYPE</var>` `<var translate="no">TARGET_NAME</var>          | Removes all the resources orHostingsite from the specified target |

The`target:remove`and`target:clear`commands automatically update the deploy target settings in the`.firebaserc`file in your project directory.

## Test locally before deploying

Run any of the following commands from the root of your project directory.

|                                       Command                                        |                                  Description                                  |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| `firebase emulators:start`                                                           | Emulates*all*the configured resources in your project directory               |
| `firebase emulators:start \` `--only hosting:`<var translate="no">TARGET_NAME</var>  | Emulates only theHostingcontent and configuration of the specifiedHostingsite |
| `firebase emulators:start \` `--only storage:`<var translate="no">TARGET_NAME</var>  | Emulates only the rules file for the specifiedCloud Storagetarget             |
| `firebase emulators:start \` `--only database:`<var translate="no">TARGET_NAME</var> | Emulates only the rules file for the specifiedRealtime Databasetarget         |

Learn more about configuring and using the[Firebase Local Emulator Suite](https://firebase.google.com/docs/emulator-suite).

## Deploy specific Firebase resources

Run any of the following commands from the root of your project directory.

|                                                          Command                                                          |                                                                                    Description                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `firebase deploy`                                                                                                         | Creates a release of*all*deployable resources in your project directory                                                                                                           |
| `firebase deploy \` `--only hosting:`<var translate="no">TARGET_NAME</var>                                                | Deploys only theHostingcontent and configuration of the specifiedHostingsite to the live channel for the site                                                                     |
| `firebase hosting:channel:deploy `<var translate="no">CHANNEL_ID</var>` \` `--only `<var translate="no">TARGET_NAME</var> | Deploys only theHostingcontent and configuration of the specifiedHostingsite to a[preview channel](https://firebase.google.com/docs/hosting/manage-hosting-resources)for the site |
| `firebase deploy \` `--only storage:`<var translate="no">TARGET_NAME</var>                                                | Deploys only the rules file for the specifiedCloud Storagetarget                                                                                                                  |
| `firebase deploy \` `--only database:`<var translate="no">TARGET_NAME</var>                                               | Deploys only the rules file for the specifiedRealtime Databasetarget                                                                                                              |