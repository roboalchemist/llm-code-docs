Source: https://docs.slack.dev/changelog/2020-09-15-events-api-truncate-authed-users

# Events API truncate authed users

September 15, 2020

Your app's [events](/reference/events)—received from the [Events API](/apis/events-api/)—are changing.

Event payloads will no longer contain a full list of `authed_users` or `authed_teams`. These two fields will be deprecated. There'll be a new, compact field called `authorizations` to replace them—**but** `authorizations` will only contain _at most one_ person or workspace that the event is visible to.

If you need a _full_ list of all the parties an event is visible to, you'll [call the `apps.event.authorizations.list` method](#what).

The new, streamlined shape of events allows Slack to deliver them faster.

These changes to the Events API will take place on **February 24, 2021**. You'll be able to **opt in** to them earlier, on September 29, 2020, by going to your [app settings](https://api.slack.com/apps) and selecting the checkbox under **Event Subscription**.

In order to get ready for the changes to authorizations, you can use the [`apps.event.authorizations.list`](#what) method **even without opting in** to the new shape of events, starting September 29, 2020.

Read on for more details on [what's changing](#what) and [how to prepare](#how).

## Why are things changing? {#why}

Previously, the Events API included a _full list_ of `authed_users`, and sometimes `authed_teams`, with every event.

These fields showed who the event is visible to. For example, if your app has been installed by two users in a workspace, and the app listens for the [`file_shared`](/reference/events/file_shared) event, your app might receive an event with `authed_users` containing those two users.

Now, `authed_users` and `authed_teams` **is deprecated**. Events will contain a single, compact `authorizations` field that shows one party that the event is visible to.

The `authed_users` and `authed_teams` fields will continue being delivered, but you'll also only receive a single entry in each collection.

If there's more than one installing party that your app is keeping track of, it's best **not to rely** on the single party listed in `authorizations` to be any particular one. To get a _full list_ of who can see events, [read on](#what) to see how to call the [`apps.event.authorizations.list`](/reference/methods/apps.event.authorizations.list) method.

These changes allow Slack to increase the performance of the Events API, delivering events faster.

## What's changing {#what}

`authed_users` and `authed_teams` **are deprecated**. Events will now include a single, compact `authorizations` field containing _one_ party that the event is visible to and `authed_users` and `authed_teams` will be limited to a single entry.

If you require a full list of authorized users or workspaces, you'll must use the [`apps.event.authorizations.list`](/reference/methods/apps.event.authorizations.list) method.

When you call that method, use the `event_context` parameter, supplying the `event_context` you receive from an event payload.

The response from that method contains a list of authorizations:

```text
  "authorizations": [        {            "enterprise_id": "E12345",            "team_id": "T12345",            "user_id": "U12345",            "is_bot": false        }  ],  "cursor_next" => "quite-a-complex-string-pointing-to-another-virtual-page-of-results"
```text

### App-level tokens are required {#app-level-tokens-are-required}

An important note: **using the `apps.event.authorizations.list` method requires a separate, user-less token**.

You can go to your [app settings](https://api.slack.com/apps), select your app, and you'll find an option to generate a token for this method under the **Basic Information** section.

`enterprise_id` appears in an authorization when there's an entire enterprise organization that the event is visible to. There might be cases where only an `enterprise_id`, with no `team_id`, is found in an authorization, depending on the event.

In order to get ready for the changes to authorizations, you can use the [`apps.event.authorizations.list`](/reference/methods/apps.event.authorizations.list) method **even without opting in** to the new shape of events, starting September 29, 2020.

### Events where context isn't relevant {#no_context}

Some events do **not** have an `event_context` field, since the authorization that the event is visible to is clear from the event.

Events without an `event_context` include:

* Events that are specifically about your app itself—for example, [`app_uninstalled`](/reference/events/app_uninstalled). There are no authorizations to list, because no user or team sees these events.
* Events that apply to an authenticated user's private actions—for example, [`im_open`](/reference/events/im_open). The event is visible only to that user, so the authorization is the user only.
* Events that apply to fully public actions on a workspace—for example, [`channel_created`](/reference/events/channel_created). The entire team makes up the authorization for the event.

### A full list of the events that do not contain an event_context {#full_list}

**Events that apply to your app**:

The following events apply to your app and have no authorizations, because no user or team sees these events:

* [`app_home_opened`](/reference/events/app_home_opened)
* [`app_uninstalled`](/reference/events/app_uninstalled)
* [`grid_migration_started`](/reference/events/grid_migration_started)
* [`grid_migration_finished`](/reference/events/grid_migration_finished)
* [`team_access_granted`](/reference/events/team_access_granted)
* [`team_access_revoked`](/reference/events/team_access_revoked)
* [`tokens_revoked`](/reference/events/tokens_revoked)
* [`workflow_step_execute`](/changelog/2023-08-workflow-steps-from-apps-step-back)
* [`workflow_step_deleted`](/changelog/2023-08-workflow-steps-from-apps-step-back)
* [`workflow_published`](/changelog/2023-08-workflow-steps-from-apps-step-back)
* [`workflow_unpublished`](/changelog/2023-08-workflow-steps-from-apps-step-back)
* [`workflow_deleted`](/changelog/2023-08-workflow-steps-from-apps-step-back)

**Events that apply to a user**:

The following events apply to the private actions of an authenticated user. The authorization that can see the event is the authenticated user in the event payload:

* [`channel_left`](/reference/events/channel_left)
* [`dnd_updated`](/reference/events/dnd_updated)
* [`im_created`](/reference/events/im_created)
* [`im_open`](/reference/events/im_open)
* [`im_close`](/reference/events/im_close)
* [`group_open`](/reference/events/group_open)
* [`group_close`](/reference/events/group_close)
* [`group_left`](/reference/events/group_left)
* [`star_added`](/reference/events/star_added)
* [`star_removed`](/reference/events/star_removed)
* [`subteam_self_added`](/reference/events/subteam_self_added)
* [`subteam_self_removed`](/reference/events/subteam_self_removed)

**Events that apply to a workspace**:

The following events apply to public actions on a workspace. The entire team makes up the authorization for the event.

* [`app_requested`](/reference/events/app_requested)
* [`channel_created`](/reference/events/channel_created)
* [`channel_deleted`](/reference/events/channel_deleted)
* [`channel_rename`](/reference/events/channel_rename)
* [`channel_archive`](/reference/events/channel_archive)
* [`channel_unarchive`](/reference/events/channel_unarchive)
* [`dnd_updated_user`](/reference/events/dnd_updated_user)
* [`email_domain_changed`](/reference/events/email_domain_changed)
* [`emoji_changed`](/reference/events/emoji_changed)
* [`file_deleted`](/reference/events/file_deleted)
* [`invite_requested`](/reference/events/invite_requested)
* [`subteam_created`](/reference/events/subteam_created)
* [`subteam_updated`](/reference/events/subteam_updated)
* [`subteam_members_changed`](/reference/events/subteam_members_changed)
* [`team_join`](/reference/events/team_join)
* [`team_rename`](/reference/events/team_rename)
* [`team_domain_change`](/reference/events/team_domain_change)
* [`user_change`](/reference/events/user_change)

## When is it changing? {#when}

These changes will take place on **February 24, 2021**. You can **opt in** to the new form of events early by going to the **Events Subscriptions** page.

Newly created apps are _automatically_ opted into the new form of events: a single, truncated `authorizations` field with one authorization shown.

## How should I prepare? {#how}

To feel secure that you're well-prepared for this change, review the following:

1. If you **don't use the Events API**, you're good to go. No changes necessary.
2. If you use the Events API, **_review_** whether your implementation uses the `authed_users` or `authed_teams` fields. These are included with each event sent via the Events API.
3. If your app **doesn't inspect these fields**, you're good to go. No changes necessary. Tell us your app is ready to go by opting in to the new form of events on the **Events Subscriptions** page [in your app settings](https://api.slack.com/apps).
4. If your code **does inspect these fields**, you must stop using the fields entirely. Look to the [`apps.event.authorizations.list`](/reference/methods/apps.event.authorizations.list) API method to gather per-event information instead of using `authed_users` or `authed_teams`.

To test if your app is ready, or to mark that your app is ready, opt-in to the new form of events on the **Events Subscriptions** page [in your app settings](https://api.slack.com/apps). For backwards compatibility, we'll continue populating these fields with a **single** authorized user and workspace.

## Tags:

* [Deprecation](/changelog/tags/deprecation)
* [Breaking change](/changelog/tags/breaking-change)
