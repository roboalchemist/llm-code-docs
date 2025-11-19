# Source: https://docs.apify.com/platform/actors/development/permissions/migration-guide.md

# Migration guide

**Migrate your Actor to limited permissions, review common migration paths, code examples, and solutions to common issues.**

***

This guide explains how to migrate your existing Actors to use https://docs.apify.com/platform/actors/development/permissions.md#how-actor-permissions-work. Before you start, make sure your Actor uses the latest https://docs.apify.com/sdk.

Recommended minimum SDK versions:

* JavaScript SDK: https://github.com/apify/apify-sdk-js/releases/tag/apify%403.4.4
* Python SDK: https://github.com/apify/apify-sdk-python/releases/tag/v3.0.0

Before you start it's helpful to understand https://docs.apify.com/platform/actors/development/permissions.md#how-actor-permissions-work.

## Test your Actor with limited permissions before migrating

You can override the permission level for a single run using run options under the **Actor Source** tab in Console:

![Forcing Actor permissions for a single run.](/assets/images/actor_run_permission_override-d681faa60e9023a1a06b87c5365f74ff.png)

You can do the same using the Apify Client as well:


```
await apifyClient.actor(actorId).call(input, {
    forcePermissionLevel: ACTOR_PERMISSION_LEVEL.LIMITED_PERMISSIONS,
});
```


Or just using the API:


```
POST https://api.apify.com/v2/acts/<actor_id>/runs?**forcePermissionLevel=LIMITED_PERMISSIONS**
```


## Common migration paths

Most public Actors can migrate to limited permissions with minor adjustments, if any. The general prerequisite is to **update the Actor to use the latest https://docs.apify.com/sdk**. To assess what needs to change in your Actor, review these areas:

* How your Actor uses storages (e.g. named storages and storages provided via input)
* Whether it requests correct resource access for user-provided storages
* Whether it needs to access information about the user (specifically if the user is paying or access their proxy configuration)

Once you have updated and  your Actor, you can change the permissions in the Actor settings. The setting takes immediate effect.

Below you can review common migration paths for advanced cases in greater detail.

### The Actor only pushes data to default storages

This is the most common and simplest use case. If your Actor only reads its input and writes results to its default dataset, key-value store, or request queue, *no changes are needed*. Limited permissions fully support this behavior out of the box.

### The Actor calls other Actors

An Actor with limited permissions can only call other Actors that also have limited permissions. If your Actor calls another one, you will need to ensure the target Actor has been migrated first.

### The Actor accesses storages provided by the user

If your Actor reads from or writes to a storage that the user provides via an input field, you must explicitly declare what access you need in the Actor's input schema.

1. Populate `resourceType` property on the field to enable the native resource picker.
2. Populate `resourcePermissions` with permissions you need for the resource.

For example, your Actor allows the user to provide a custom dataset for the Actor results. Your `input_schema.json` might contain something like this:


```
{
    "title": "Output",
    "type": "string",
    "description": "Select a dataset for the Actor results",
}
```


To support limited permissions, change it to this:


```
{
    "title": "Output",
    "type": "string",
        "description": "Select a dataset for the Actor results",
    "resourceType": "dataset",
    "resourcePermissions": ["READ", "WRITE"],
    "editor": "textfield", // If you want to preserve the plain "string" input UI, instead of rich resource picker.
}
```


Now when the platform runs your Actor, it’ll automatically add the user-provided storage to the Actor’s scope so that it can access it.

Backward compatibility

Users can provide the resource both via its name and its ID. If you have users with inputs that specify the resource via its name, this change to the input schema will not break it.

### The Actor accesses named storages

Actors sometimes use named storages for caching or persisting state across runs. With limited permissions, an Actor can create a named storage on its first run and will automatically retain access to it in all subsequent runs by the same user.

If your Actor previously relied on accessing a pre-existing named storage, you will need to rename it in your code. This will cause the Actor to recreate the storage under the new system on its next run.

To achieve a smooth migration without disrupting your Actor’s users, you will need to make sure that your Actor can handle the transition. The suggested approach is the following:

1. Adjust the code of the Actor so that it can run with both limited and full permissions.
2. Change the Actor setting to limited permissions.
3. Clean up the migration code.


```
const OLD_CACHE_STORE_NAME = 'my-actor-cache';
const NEW_CACHE_STORE_NAME = 'my-actor-cache-updated';

let store;

if (process.env.ACTOR_PERMISSION_LEVEL === 'LIMITED_PERMISSIONS') {
    // If the Actor is running with limited permissions and we need to create
    // a new store. The platform will remember that the store was created by this Actor
    // and will allow access in all follow-up runs.
    store = await Actor.openKeyValueStore(NEW_CACHE_STORE_NAME);
} else {
  // If the Actor is still running with full permissions and we should use
    // the existing store.
    store = await Actor.openKeyValueStore(OLD_CACHE_STORE_NAME);
}
```


Re-create cache only under limited permissions.

Create the new storage *only once the Actor runs with limited permissions*. Only that way the access is retained in follow-up runs.

If the contents of the named storage are critical for your Actor to keep functioning for users and it is impossible, costly or highly impractical to migrate, contact support or reach out to us https://discord.gg/eN73Xdhtqc. We can discuss the available options.

### The Actor needs to know whether the user is paying

Some Actors have different logic for free and paying users. Previously you could retrieve this information by calling the `/users/me` API endpoint. However, Actors running under limited permissions don't have access to that endpoint. To get this information, your Actor should read the `APIFY_USER_IS_PAYING` environment variable, or use the SDK to obtain the value:


```
const { userIsPaying } = Actor.getEnv();
```


### The Actor uses Proxy

Similarly, if your Actor uses https://docs.apify.com/platform/proxy.md and needs to retrieve the user's proxy password, it should get it from the `APIFY_PROXY_PASSWORD` environment variable instead of calling the `/users/me` endpoint or, preferably, rely on the SDK to handle proxy configuration automatically.
