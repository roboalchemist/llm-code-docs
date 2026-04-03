# Source: https://firebase.google.com/docs/hosting/multisites.md.txt

<br />

You can set up one or moreFirebase Hostingsites in a single Firebase project. Since the sites are all in the same Firebase project, all the sites can access the other Firebase resources of the project.

- Each site has its own[hosting configuration](https://firebase.google.com/docs/hosting/full-config).
- Each site hosts its own collection of content.
- Each site can have one or more[associated domains](https://firebase.google.com/docs/hosting/custom-domain).

By setting up multipleHostingsites within the same Firebase project, you can more easily share Firebase resources between related sites and apps. For example, if you set up your blog, admin panel, and public app as individual sites in the same Firebase project, they can all share the sameFirebase Authenticationuser database, while also having their own unique domains or content.
| **Important:** To mirror your workflow environments (for example, Dev, Q1, Q2, Prod), we recommend that you create a separate Firebase project for each environment rather than creating multiple sites in a single Firebase project. Generally, you don't want to use production-environment Firebase resources (like customer data in aRealtime Database) in a development environment. Consider using[automatic SDK configuration](https://firebase.google.com/docs/hosting/reserved-urls#sdk_auto-configuration)to mirror multiple environments using a single codebase.
| The multisite feature supports a maximum of 36 sites per Firebase project.

## **Step 1** : Update yourFirebaseCLI version

Access the most currentFirebase Hostingfeatures by[updating to the latest version of theFirebaseCLI](https://firebase.google.com/docs/cli#update-cli).

## **Step 2**: Add additional sites

Add additional sites to a Firebase project using one of the following methods:

- Use the workflow in the[Hostingpage](https://console.firebase.google.com/project/_/hosting/sites)of theFirebaseconsole

- Use theFirebaseCLI command:`firebase hosting:sites:create `<var translate="no">SITE_ID</var>

- Use theHostingREST API:[`projects.sites.create`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites/create)

For each of these methods, you'll specify a`SITE_ID`which is used to construct the Firebase-provisioned default subdomains for the site:

- <var translate="no">SITE_ID</var>`.web.app`
- <var translate="no">SITE_ID</var>`.firebaseapp.com`

Because the`SITE_ID`is used for these URLs, the site ID has the following requirements:

- Must be a valid hostname label, meaning it cannot contain`.`,`_`, etc.
- Must be 30 characters or fewer
- Must be globally unique within Firebase

To each site, you can also optionally[add custom domains](https://firebase.google.com/docs/hosting/custom-domain)to serve the same content and configuration to multiple URLs.
| **Note:** If you created multipleFirebase Realtime Databaseinstances in your Firebase project before August 2018, Firebase automatically provisioned a corresponding site for each database instance. If you don't need these additional sites, you can delete them without affecting your database instances.

### Delete a secondary site

Delete unwanted sites from a Firebase project using one of the following methods:

- Use the workflow in the[Hostingpage](https://console.firebase.google.com/project/_/hosting/sites)of theFirebaseconsole

- Use theFirebaseCLI command:`firebase hosting:sites:delete `<var translate="no">SITE_ID</var>

- Use theHostingREST API:[`projects.sites.delete`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites/delete)

Note that you cannot delete the default site, which has the same`SITE_ID`as your Firebase project ID.
| **Caution:** Deleting a site is a permanent action. If you delete a site, Firebase doesn't maintain records of deployed files or deployment history, and the`SITE_ID`cannot be reactivated by you or anyone else.

## **Step 3**: Set up deploy targets for your sites

When you have multiple sites and you runFirebaseCLI deploy commands, the CLI needs a way to communicate which settings should be deployed to each site. With[***deploy targets***](https://firebase.google.com/docs/cli/targets)you can uniquely identify a*specific* site with a`TARGET_NAME`in your[`firebase.json`configuration file](https://firebase.google.com/docs/hosting/multisites#define_hosting_config)and in your[FirebaseCLI commands](https://firebase.google.com/docs/hosting/multisites#cli-commands-with-deploy-targets)for testing or deploying to your sites.
| **Important:** Using deploy targets is the recommended way to configure deploys for multipleHostingsites.  
| If you previously configured your`firebase.json`file by explicitly referencing your<var translate="no">SITE_ID</var>, you should edit your[`firebase.json`configuration](https://firebase.google.com/docs/hosting/multisites#define_hosting_config)and your[CLI commands](https://firebase.google.com/docs/hosting/multisites#cli-commands-with-deploy-targets)to use deploy targets instead.

To create a deploy target and apply a`TARGET_NAME`to aHostingsite, run the following CLI command from the root of your project directory:

<br />

```
firebase target:apply hosting TARGET_NAME RESOURCE_IDENTIFIER
```

<br />

Where the parameters are:

- <var translate="no">TARGET_NAME</var>--- a unique name (that you've defined yourself) for theHostingsite that you're deploying to

- <var translate="no">RESOURCE_IDENTIFIER</var>--- the`SITE_ID`for theHostingsite***as listed in your Firebase project***

For example, if you've created two sites (`myapp-blog`and`myapp-app`) in your Firebase project, you could apply a unique`TARGET_NAME`(`blog`and`app`, respectively) to each site by running the following commands:

<br />

```
firebase target:apply hosting blog myapp-blog
```  

```
firebase target:apply hosting app myapp-app
```

<br />

The settings for deploy targets are stored in the`.firebaserc`file in your project directory, so you only need to set up deploy targets one time per project.

## **Step 4**: Define the hosting configuration for each site

Use a site's applied`TARGET_NAME`when you're defining its hosting configuration in your[`firebase.json`](https://firebase.google.com/docs/hosting/full-config#firebase-json_example)file.

- If your`firebase.json`file defines the configuration for multiple sites, use an array format:

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
  ```
- If your`firebase.json`file defines the configuration for only one site, it's not necessary to use an array format:

  ```text
  {
    "hosting": {
        "target": "blog",
        "public": "dist",

        // ...

        "rewrites": [...]
    }
  }
  ```

## **Step 5**: Test locally, preview changes, and deploy to your sites

Run any of the following commands from the root of your local project directory.

|                                                         Command                                                         |                                                      Description                                                      |
|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `firebase emulators:start --only hosting`                                                                               | Emulates theHostingcontent and configuration of the***default*** Hostingsite at a locally hosted URL                  |
| `firebase emulators:start --only hosting:`<var translate="no">TARGET_NAME</var>                                         | Emulates theHostingcontent and configuration of the specifiedHostingsite at a locally hosted URL                      |
| `firebase hosting:channel:deploy \` <var translate="no">CHANNEL_ID</var>                                                | Deploys theHostingcontent and configuration of the***default*** Hostingsite at a preview URL                          |
| `firebase hosting:channel:deploy \` <var translate="no">CHANNEL_ID</var>` --only `<var translate="no">TARGET_NAME</var> | Deploys theHostingcontent and configuration of the specifiedHostingsite at a preview URL                              |
| `firebase deploy --only hosting`                                                                                        | Deploys theHostingcontent and configuration to the live channel of***all*** Hostingsites configured in`firebase.json` |
| `firebase deploy --only hosting:`<var translate="no">TARGET_NAME</var>                                                  | Deploys theHostingcontent and configuration to the live channel of the specifiedHostingsite                           |

|                                                        Command                                                         |                                            Description                                             |
|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| *(not recommended; use`emulators:start`instead)* `firebase serve --only hosting`                                       | Serves theHostingcontent and configuration of the***default*** Hostingsite at a locally hosted URL |
| *(not recommended; use`emulators:start`instead)* `firebase serve --only hosting:`<var translate="no">TARGET_NAME</var> | Serves theHostingcontent and configuration of the specifiedHostingsite at a locally hosted URL     |

| **Note:** By running commands with the`--only hosting`flag, you're only emulating or deploying yourHostingcontent and config. If you*also* want to emulate or deploy[other project resources or configurations](https://firebase.google.com/docs/cli#partial_deploys)(like functions or database rules), run commands with a comma-separated list in the flag (for example,`--only hosting,functions`).
|
| For deploys to preview channels, you don't specify`hosting`in the`--only`flag because those commands can*only* deploy yourHostingcontent and config.