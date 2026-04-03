# Source: https://firebase.google.com/docs/hosting/manage-hosting-resources.md.txt

<br />

<br />

Firebase Hostingprovides tooling via both theFirebaseconsole and theFirebaseCLI to manage the channels, releases, and versions for yourHostingsite.

## Overview of theHostinginfrastructure

Understanding theHostinginfrastructure helps you to understand the management options described on this page.

Every Firebase project has a defaultHosting***site*** with access to all the project's resources (databases, authentication, functions, etc.). A site contains one or more***channels*** , where each channel is associated with a URL that serves specific content and aHostingconfiguration.
| **Note:** You can have[multipleHostingsites](https://firebase.google.com/docs/hosting/multisites)in your project, with eachHostingsite following the same infrastructure as the defaultHostingsite.

![an image of <span class=](https://firebase.google.com/static/docs/hosting/images/hosting-single-site-hierarchy.png)Firebase Hostinghierarchy" /\>

EveryHostingsite has a "live" channel that serves content and aHostingconfig at (1) the site's Firebase-provisioned subdomains (<var translate="no">SITE_ID</var>`.web.app`and<var translate="no">SITE_ID</var>`.firebaseapp.com`) and (2) any connected[custom domains](https://firebase.google.com/docs/hosting/custom-domain). You can also optionally create "preview" channels that serve their own content and configuration at temporary, sharable "preview URLs" (**<var translate="no">SITE_ID</var>*--* <var translate="no">CHANNEL_ID</var>*-*** <var translate="no">RANDOM_HASH</var>`.web.app`).
| **Note:** If you use the[`pinTag`feature with rewrites to functions](https://firebase.google.com/docs/hosting/full-config#pintag-in-rewrites-to-function), then each channel can point to different functions.

The content and configuration served by each channel is packaged into a***version*** object that has a unique identifier. When you deploy to your site, Firebase creates a***release***object that points to a specific version. A release contains metadata about the deployment, like who deployed and when they deployed.

From your Firebase project's[Hostingdashboard](https://console.firebase.google.com/project/_/hosting/sites), you can see a full history of your live channel's releases in a*Release history* table. If you have[multipleHostingsites](https://firebase.google.com/docs/hosting/multisites), click**View** for the desired site to see its release history. If you have any preview channels, they are also displayed on theHostingdashboard.
| Preview channels are a beta release. This means that the functionality might change in backward-incompatible ways or have limited support. A beta release is not subject to any SLA or deprecation policy. Feature availability and support for preview channels will continue to improve as the tool matures.

## Manage a channel's settings

For each channel of your site, you can control its settings. Some settings, like channel expiration, are only applicable for preview channels.

### Limit the number of releases to keep

Each time you deploy to a channel (and create a release),Hostingkeeps the version associated with the previous release in your project'sHostingstorage. You can set the number of releases to keep for*each channel*in your project, both live and preview channels.

- Why doesHostingkeep previous releases?  
  For your live channel, keeping previous releases enables you to[roll back](https://firebase.google.com/docs/hosting/manage-hosting-resources#roll-back)to a previous version of your site, if needed. For your preview channels, rolling back is not yet available.

- Why limit the number of releases to keep?  
  This feature can help you control the usage level of your[project'sHostingstorage](https://firebase.google.com/docs/hosting/usage-quotas-pricing), as the content for previous releases is kept in this storage. You can monitor yourHostingstorage from the[*Storage*tab](https://console.firebase.google.com/project/_/hosting/usage/current-billing/storage)in the console.

- What happens when you limit the releases to keep?  
  When you set a limit for releases to keep, the content of any releases over your set limit is scheduled for deletion,*starting with the oldest releases first*.

Here's how to set the release storage limit for a channel:

1. In the[Firebaseconsole](https://console.firebase.google.com/project/_/hosting/sites), access the release storage setting dialog:

   - For your live channel  
     In the*Release History* table for your site, clickmore_vert, then select**Release storage settings**.

   - For any preview channel  
     In the row for the preview channel, clickmore_vert, then select**Channel settings**.

2. Enter the number of releases that you'd like to keep, then click**Save**.

### Set the expiration of a preview channel

By default, a preview channel expires 7 days from its creation date, but your site's live channel will never expire.

When a preview channel expires, the channel, along with its releases and associated versions, are scheduled for deletion within 24 hours. The associated preview URL is also deactivated. An exception to this version-deletion is if a version is associated with another release (this happens, for example, if you clone a version from one channel to another*within the same site*).

Hostingsupports two different ways to control the expiration of a channel:

- [Firebaseconsole](https://console.firebase.google.com/project/_/hosting/sites)  
  In the row for the preview channel, clickmore_vert, then select**Channel settings**. Enter the date and time for expiration.

- FirebaseCLI  
  When you deploy to your preview channel, pass the`--expires `<var translate="no">DURATION</var>flag, for example:

  ```
  firebase hosting:channel:deploy new-awesome-feature --expires 7d
  ```

  The expiration can be up to 30 days from the date of deploy. Use`h`for hours,`d`for days, and`w`for weeks (for example,`12h`,`7d`,`2w`, respectively).
  | **Note:** If you deploy to an existing preview channel without passing an`--expires`flag, and it's within 7 days of the channel's expiration date,Hostingautomatically extends the life of the channel so that it remains active 7 days after the new deploy.

## Clone a version from one channel to another

You can clone a deployed version from one channel to a different channel. You can clone across live or preview channels, acrossHostingsites, or even across Firebase projects.

The clone command also*deploys* to the "target" channel so that the clonedHostingcontent and config are automatically served at the "target" channel's associated URL.

This feature is useful for version tracking or if you want confidence that you're deploying the*exact*content you've viewed and/or tested on another channel. Here are some examples:

- Clone from a "QA" preview channel to the live channel of your site (going live!)

- Clone from the live channel of your site to a "debug" preview channel (like before a rollback)

- Clone from a channel in your "staging" Firebase project to a preview channel in your "prod" Firebase project

To clone a version, run the following command from any directory:  

```
firebase hosting:clone SOURCE_SITE_ID:SOURCE_CHANNEL_ID TARGET_SITE_ID:TARGET_CHANNEL_ID
```

Replace each placeholder with the following:

- <var translate="no">SOURCE_SITE_ID</var>and<var translate="no">TARGET_SITE_ID</var>: These are the IDs of theHostingsites that contain the channels.

  - For your defaultHostingsite, use your Firebase project ID.
  - You can specifyHostingsites that are in the same Firebase project or even in different Firebase projects.
- <var translate="no">SOURCE_CHANNEL_ID</var>and<var translate="no">TARGET_CHANNEL_ID</var>: These are the identifiers for the channels.

  - For a live channel, use`live`as the channel ID.
  - If the specified "target" channel doesn't yet exist, this command creates the channel before deploying to it.

<br />

Expand this section to learn about the nuances of version cloning

<br />

> When you clone a version from one channel to another channel*in the sameHostingsite* , Firebase creates a new release object that points to the*exact same version* . You will see two releases in yourHostingsite that both point to the same version (as identified by the version ID).
>
> However, if you clone a version to a channel*in a differentHostingsite*(or a different Firebase project), Firebase creates both a new release and a new version (as identified by a different version ID).

<br />

<br />

## Roll back to a previous version of your site

You can roll back to serve a previous version of your site's live channel. This action is useful if your current release has an issue and you want to roll back to serve a known working version of your site. Or perhaps your site served temporary content for a holiday or special event, but now you want to roll back to serve your "regular" content.

By rolling back, you create a new release that serves the same version of content as a previous release. In your*Release history*table, both releases will list the same version identifier.

Here's how to roll back:

1. In the[Firebaseconsole](https://console.firebase.google.com/project/_/hosting/sites), in the*Release History*table for your site, hover over the previous release entry that you want to roll back to.

2. Clickmore_vert, then select**Roll back**.

## Manually delete a release

You might need to manually delete a release from your live channel to free up[Hostingstorage](https://firebase.google.com/docs/hosting/usage-quotas-pricing)for your project. You can only delete previous releases, not the release currently being served on your live site.

When you delete a release, you're actually deleting its content, which is scheduled for deletion within 24 hours. The release object itself is kept so that you can still see its metadata (who deployed and when they deployed).

Here's how to delete a release:

1. In the[Firebaseconsole](https://console.firebase.google.com/project/_/hosting/sites), in the*Release History*table for your site, hover over the previous release entry that you want to delete.

2. Clickmore_vert, then select**Delete**.

## Manually delete files

InFirebase Hosting, the primary way to delete selected files from a deployed site is to delete the files locally, and then redeploy.

## Manually delete a preview channel

You can preview your channels by clicking on the channel you want to preview. From this view, you can see, delete, and revert the newest deployments and release that are tied to the specific channel. You can delete a preview channel, but you can't delete your site's live channel.

When you delete a preview channel, the channel, along with its releases and associated versions, are scheduled for deletion within 24 hours. The associated preview URL is also deactivated. An exception to the version-deletion is if a version is associated with another release (this happens, for example, if you clone a version from one channel to another*within the same site*).

Hostingsupports two different ways to delete a preview channel:

- [Firebaseconsole](https://console.firebase.google.com/project/_/hosting/sites)  
  In the row for the preview channel, clickmore_vert, then select**Delete channel**. Confirm the deletion.

- FirebaseCLI  
  Run the following command from any directory:

  ```
  firebase hosting:channel:delete CHANNEL_ID
  ```

## CLI commands for preview channels and cloning

### Commands for preview channels

All commands for preview channels support deploy targets if you have[multipleHostingsites](https://firebase.google.com/docs/hosting/multisites).

|                                Command                                 |                                                                                                     Description                                                                                                     |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `firebase hosting:channel:create `<var translate="no">CHANNEL_ID</var> | Creates a new preview channel in the***default*** Hostingsite using the specified`CHANNEL_ID` This command does not deploy to the channel.                                                                          |
| `firebase hosting:channel:delete `<var translate="no">CHANNEL_ID</var> | Deletes the specified preview channel You cannot delete a site's live channel.                                                                                                                                      |
| `firebase hosting:channel:deploy `<var translate="no">CHANNEL_ID</var> | Deploys yourHostingcontent and config to the specified preview channel If the preview channel does not yet exist, this command creates the channel in the***default*** Hostingsite before deploying to the channel. |
| `firebase hosting:channel:list`                                        | Lists all channels (including the "live" channel) in the***default*** Hostingsite                                                                                                                                   |
| `firebase hosting:channel:open `<var translate="no">CHANNEL_ID</var>   | Opens a browser to the specified channel's URL or returns the URL if opening in a browser isn't possible                                                                                                            |

### Commands for version cloning

|                                                                                                           Command                                                                                                            |                                                                                                                                                                                                      Description                                                                                                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `firebase hosting:clone \` ` `<var translate="no">SOURCE_SITE_ID</var>***:*** <var translate="no">SOURCE_CHANNEL_ID</var>` \` ` `<var translate="no">TARGET_SITE_ID</var>***:*** <var translate="no">TARGET_CHANNEL_ID</var> | Clones the most recently deployed version on the specified "source" channel to the specified "target" channel This command also deploys to the specified "target" channel. If the "target" channel does not yet exist, this command creates a new preview channel in the "target"Hostingsite before deploying to the channel.                                                                                          |
| `firebase hosting:clone \` ` `<var translate="no">SOURCE_SITE_ID</var>***:@*** <var translate="no">VERSION_ID</var>` \` ` `<var translate="no">TARGET_SITE_ID</var>***:*** <var translate="no">TARGET_CHANNEL_ID</var>       | Clones the specified version to the specified "target" channel This command also deploys to the specified "target" channel. If the "target" channel does not yet exist, this command creates a new preview channel in the "target"Hostingsite before deploying to the channel. You can find the`VERSION_ID`in the[Hostingdashboard](https://console.firebase.google.com/project/_/hosting/sites)of theFirebaseconsole. |