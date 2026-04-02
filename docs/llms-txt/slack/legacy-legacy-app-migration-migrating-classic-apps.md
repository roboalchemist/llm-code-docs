Source: https://docs.slack.dev/legacy/legacy-app-migration/migrating-classic-apps

# Migrating classic apps

Classic apps deprecation has been paused

We have paused the [previously announced](/changelog/2024-09-legacy-custom-bots-classic-apps-deprecation) deprecation of classic apps. Classic apps will continue to work for the foreseeable future but are still considered a legacy method of integrating with Slack, and new classic apps cannot be created. We highly recommend you [migrate your classic app to a Slack app](/legacy/legacy-app-migration/migrating-classic-apps/) to avoid any future service interruptions.

If you're a developer who has built an app on the Slack platform in the past, you may know that apps have since changed. With the help of explicit permissions tied to the app rather than an installing user, Slack apps are more pleasant to build and install.

Slack apps act independently of an installing user. They have more functionality, and they're more likely to be approved by a Slack admin—and less likely to be accidentally uninstalled.

Good news: _existing_, classic apps won't be left out in the cold. You can migrate an existing app to use the new system of permissions. Along the way, you'll gain more control over the permissions you request.

Before starting migration, you can read our guide to [building a Slack app from scratch](/app-management/quickstart-app-settings) if you've never built a Slack app before. Otherwise, [read on to start your app's great migration](#overview).

## Overview {#overview}

Migrating your app is a trip in two parts.

First, you'll [update](#update_ui) your app's scopes on its **Development Workspace**, the workspace where you originally built and tested your app. To change the scopes your app has on the workspace, you'll follow the [update UI](#update_ui) and _touch no code_. At the end of the update flow, you'll obtain a new [OAuth redirect URL](/authentication/installing-with-oauth).

![Link to new scope update tool found in app management page](/assets/images/scope_update_tool-003e3d8d34e2858560c39c5de2c8ab7f.png)

[Secondly](#update_oauth), you'll change the URL where you redirect users to initiate the v2 OAuth flow. The [v2 OAuth flow](/authentication/installing-with-oauth) is nearly identical to the [old OAuth flow](/authentication). The only differences are a couple new v2s added to method names and a slightly altered structure for the final [`oauth.v2.access`](/authentication/installing-with-oauth) response.

Start your journey with a tiny first step—[read on.](#start)

## Updating scopes with the update UI {#update_ui}

This section of the migration guide walks you through updating scopes for your app on its **Development Workspace**. All of the migration here is powered by a UI; you won't have to touch a line of code.

### Starting an app migration {#start}

Updating your app begins close to home: your [App Management page](https://api.slack.com/apps). When you navigate to your app's page, your classic app will now display a **Tools** section in the sidebar. Select **Update to Granular Scopes** to begin your app migration.

### Selecting bot user scopes {#select_bot}

Work through the checklist on the **Update your app's scopes** page to select the right scopes for your newly scope-conscious app.

The scope updater page does not automatically select the specific scopes your app needs. You'll still need to individually select the right scopes for your app.

Read through each part of the checklist and select the scopes needed. If you're not sure whether you need a particular scope to call a Slack API method or to listen to a Slack API event, look at the reference [pages for methods](/reference/methods) and [events](/reference/events) to see details on what scopes are needed for each.

You'll notice that [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks) and [Slash commands](/interactivity/implementing-slash-commands) are attached to your app's bot user only, rather than an authenticated user. That's great news: it means that webhooks and Slash commands no longer unexpectedly get uninstalled when an installing user departs. If you use either webhooks or Slash commands, add the [`incoming-webhook`](/reference/scopes/incoming-webhook) or [`commands`](/reference/scopes/commands) scopes.

If your app used the deprecated umbrella [`bot`](/reference/scopes/bot) scope, you'll see that all the scopes contained in it— all the permissions that the `bot` scope previously conferred on your app—are already checked in the checklist.

You probably don't need each of those scopes (for example, the `remote_files:*` scopes are rarely required), which is why the old umbrella `bot` scope caused some problems in the first place. Uncheck the scopes you don't want!

You'll find fancy new features that previously required a user scope, now available to your app's bot user. Request these scopes for your bot and not the equivalent user token scopes.

Rule of thumb: Slack apps _nearly_ all work from the perspective of the app, not from the perspective of an installing user. If you're not sure whether to select a bot scope or user scope, select it as a bot scope.

One last aside: if you're worried about taking a wrong step, remember that this update tool only applies to your app on its **Development Workspace**. Missteps are no big deal. If you miss a scope that your app eventually requires, your app will receive an error from the Slack API noting which scope it needs. Once you add that scope, request it via the [App Management page](https://api.slack.com/apps), and you'll be on your way.

### Selecting authenticated user scopes {#select_user}

After selecting all the bot user scopes your app needs, click **Continue** to select user scopes—i.e., scopes that allow you to act from the perspective of the installing user.

These scopes should be restricted or avoided if possible. Only request a scope for acting as your authenticating user if the action needs to be performed from the user's perspective: for example, reading or starting group DMs for a specific user.

Slack apps **may not access** the legacy [RTM](/legacy/legacy-rtm-api) API. For most apps, the [Events API](/apis/events-api/) lets your app listen to Slack goings-on in a more structured, safe way. If you require access to the legacy RTM API (say, because you're building your app behind a corporate firewall), continue to use a classic app bot token to call [`rtm.connect`](/reference/methods/rtm.connect).

### Reinstalling your app {#reinstall}

After one more **Continue**, you'll see a **Verification** page that shows you all the scopes your app now requests during installation.

If the list seems long, rest assured that admins and installing users will now have a much clearer idea of what your app can actually do. And your app is less likely to be accidentally uninstalled if an installing user departs. Select **Yes, this looks good**.

You'll see a button on the following page that allows you to reinstall your app with the granular scopes. Before you click the button, copy down the OAuth redirect URL listed at the bottom of the page. You'll use that in [part 2 of migration](#update_oauth), where you slightly change your OAuth flow to receive granular scopes on _other_ workspaces.

Click **Reinstall**. Congratulations, your app now uses new permissions on its **Development Workspace** and can act independently of the installing user!

## Updating your OAuth flow {#update_oauth}

If your app is not distributed beyond your development workspace, your migration is complete. Touch down in the sand, stretch your feet out, grab some coffee, and go on with life in the new land of apps. Check out the [migration quickstart guide](/legacy/legacy-app-migration/differences-between-classic-apps-and-granular-slack-apps) to see a list of differences between classic apps and granular Slack apps.

If your app _is_ distributed to other workspaces, you'll want to update your OAuth flow. Read our [guide to the Slack V2 OAuth flow](/authentication/installing-with-oauth). You don't have much additional migration ahead of you! With the redirect URL obtained [above](#reinstall), you'll automatically initiate the new V2 OAuth flow whenever you redirect a user. Then, you'll have to update to the [`oauth.v2.access`](/reference/methods/oauth.v2.access) method, which you call after obtaining a temporary code from the installing user. After parsing the slightly different endpoint response, you'll be ready for reinstall.

## Cleanup {#cleanup}

Now that you've updated your code to the [Slack V2 OAuth flow](/authentication/installing-with-oauth), you'll want to make sure your app is reinstalled on each workspace. You might gently direct users to reinstall with a DM containing an updated redirect to your oauth/v2/authorize URL. If you're comfortable forcing a reinstall, you can even use the [auth.revoke](/reference/methods/auth.revoke) method to revoke a previous installation on a given workspace.

Remember, there's no hurry to force a reinstall if you're comfortable dealing with two sets of scopes at once, depending on whether each installation of your app is a classic installation or uses the new V2 flow. However, for simplicity we think it's easiest to get all installations of your app updated to new permissions as soon as possible.

There's no automatic way to convert existing bot and user tokens into the new kind of app, except on your **Development Workspace** using the [update UI](#update_ui).

## Resubmitting your app to the Slack Marketplace {#resubmit}

If your app is listed in the Slack Marketplace, migrating your app requires a little more care. Upgrading your app to granular permission will likely mean creating a separate testing app that we can install and test.

As an example, if your app is called `cycling_tips`, create a staging app called `cycling_tips-dev` that we can install. You can use this staging app to test updates.

Creating a distributed, staging version of your app allows us to test how the new scopes will work on your app, leaving your published (live) app as is until those changes can be approved. The staging app should use the same scopes requested in the resubmission for your published app.

You can add these details to the test instructions box in the "Help us review your app" section when you resubmit. If your web service requires an account or a paid plan to access, please include test details for this as well.

If it's been a while since you’ve submitted your app, or if you're also making other changes to your app, [please review our general guidelines again](/slack-marketplace/slack-marketplace-review-guide#testing).

### Testing requirements for app migration {#faq_summary}

* Choose new scopes.
* If you haven’t done so, create a separate Slack app for testing and use in development/staging environments, e.g. _\[app\_name\]-staging_. Make sure that this app can be [distributed on other workspaces](/app-management/distribution).
* Use separate _\[app\_name\]-staging_ app to test the new scopes and OAuth endpoints. Ensure that the scopes on your staging app match the requested scopes in your resubmission.
* Test that code and features work.
* Switch your production app over to new scopes and endpoints.
* Submit your app to the Slack Marketplace with credentials and an environment for the test app.
* Take your app and new code live at the same time.
* (Optional) Send a message to existing users asking them to upgrade their app to granular permissions.

## FAQs {#faq}

### How do Slack apps differ from classic apps? {#faq_permissions_app_differences}

Check out our [migration quickstart](/legacy/legacy-app-migration/differences-between-classic-apps-and-granular-slack-apps) guide for a rundown on updated behavior for Slack apps.

### When would I need to request a user token? {#faq_permissions_user_token}

User scopes and tokens should only be requested as necessary when the app must perform an action on behalf of the user.

### How can I post in public channels without joining them? {#public}

Slack apps can explicitly request the ability to post in any public channel using the [`chat:write.public`](/reference/scopes/chat.write.public) scope.

### Can I use the as_user parameter for chat.postMessage? {#as_user}

Slack apps typically act and post on their own behalf. However, if you'd like to adjust the authorship of your app's messages, request the [`chat:write.customize`](/reference/scopes/chat.write.customize) scope. Read the [`chat.postMessage`](/reference/methods/chat.postMessage#authorship) documentation for more details.

### My app uses the legacy RTM API, which is not supported by granular permissions. What do we need to do to migrate to the Events API? {#faq_permissions_rtm_support}

If you are using the legacy RTM API for security reasons with an app you’ve built for your own team (internal integration), check out [Socket Mode](/apis/events-api/using-socket-mode).

If your app is distributed, you’ll first need to identify the events your app is consuming from Slack’s RTM API and determine their equivalents in the [Events API](/apis/events-api/#event_types). Once you’ve done that work, you’ll need to configure event subscriptions in your app configuration, as well as an endpoint where Slack can send those event payloads. Store the data your app is consuming from the Events API as you currently do with RTM events.

### What are the differences between the legacy RTM API and the Events API? {#faq_permissions_event_differences}

Besides the legacy RTM API being a much more robust and undiscerning stream of events from Slack, there are a few features not available in the Events API.

* The Events API is not WebSocket-based.
* The Events API does not make the typing indicator available.
* The team plan information available by calling `rtm.start` is not available via the Events API.

Read on: [Events supported by the legacy RTM API and the Events API](/reference/events).

### Can I automatically determine which new scopes my app needs? {#faq_permissions_autodetect}

At this time, there's no way for Slack to determine which scopes your app needs. You'll have to run through each [method](/reference/methods) and [event](/reference/events) that your app makes use of, requesting the scope for each.

### Why does my app require more scopes in the new model? {#faq_permissions_more_scopes}

The legacy `bot` scope consisted of many scopes that are now broken down and requested separately, allowing developers to request the least access possible on a Slack customer workspace. The new scopes are a better, more honest representation of the permissions your app has on a workspace. Ensure that you request only the scopes absolutely necessary to enable your app’s features in Slack. When your app goes to our Slack Marketplace team for review, they will review your app’s use of each scope.

### How do I migrate users to the new token model? {#faq_migration_users}

In order to migrate users, direct them to reinstall via a DM containing an updated redirect to your `oauth/v2/authorize` URL.

### Will classic bot tokens still work after someone else has installed the app on the same workspace using V2 OAuth? {#faq_migration_classic_bot}

Classic bot tokens will continue to work after another user has installed the app using V2 OAuth.

### Can I still use the V1 OAuth endpoint once my app configuration has been migrated? {#faq_migration_oauth_v1}

No, once an app’s configuration has been migrated it’s no longer possible to use the V1 OAuth endpoint.

### Production versus development Slack Marketplace switchover {#faq_slack_marketplace_development}

To assist with migrating to granular permissions, we recommend that developers create a separate Slack app for testing and use in their development/staging environments, e.g. _\[app\_name\]-staging_. This provides a few of key benefits:

* It allows you to configure the app to work in your development/staging environment without impacting the settings for your published app, e.g. you can use staging specific endpoints.
* It allows you to test new features and scopes (granular permissions) without being subject to the restrictions associated with your published app, e.g. you can add new scopes/redirect URIs.
* It gives us a handy way to test new changes as part of reviewing resubmissions.

Use this app to test your granular permissions before adding these new scopes to your published app’s settings and resubmitting. Please be sure to include instructions for how to install the app you tested with in your submission.

### How should I time the switchover in the Slack Marketplace and in my app? {#faq_slack_marketplace_switchover}

Unfortunately there is no avoiding a small window of time where app installations cannot be performed while the switchover is taking place. The best way to coordinate this is to first deploy any code changes required to update the authorization flow, and then publish your app’s changes as the latter process will take effect almost instantaneously.

### When and how should I submit my new app? {#faq_slack_marketplace_submission}

Submissions should be made as soon as possible, and can be made by visiting the [Slack Marketplace](/slack-marketplace), navigating to the app in question, and heading to the **Submit changes for review** section.

### Do you have any rollback mechanisms if the migration fails? {#faq_slack_marketplace_rollback}

Yes, we can roll the app back to the previous set of non-granular scopes your app is using if you confirm the scope list with us. The most common reason for rollback is an app developer migrating an app’s OAuth settings and scope selections before any development work has been done.

_Note: it is a complicated process and there may be a delay in the rollback._

### Timeline {#faq_slack_marketplace_timeline}

As of **December 2020**, we no longer accept new classic app submissions or updates to classic apps.

As of **May 27th, 2022**, granular permissions have been required for apps in the Slack Marketplace.

### How will the Slack Marketplace team test the new version of the app? {#faq_slack_marketplace_testing}

As part of reviewing your resubmission we need to be able to install and test a version of your Slack app that is using the new granular permissions, e.g. the Slack app you use in your development/staging environment.

We cannot use your published app to test with, as it is restricted to requesting approved scopes.
