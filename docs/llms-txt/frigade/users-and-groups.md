# Source: https://docs.frigade.com/platform/users-and-groups.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Users and Groups

> Easily manage users and groups as they engage with your Flows

## User Management

***

You can view all of the users interacting with your Flows on the <a href="https://app.frigade.com/users" target="_blank">users</a> page. Users will automatically appear in Frigade once they have been identified in your app (see [SDK](/sdk/hooks/user) or [API](/api-reference/users) docs for more info).

You can see all of the Flows that a user has engaged with and their status for each Flow on the user detail page. This can be especially useful for Customer Success teams to see which customers may be stuck and where.

If needed, you can also reset a user's status for a Flow to allow them to start over. This is an especially helpful feature when developing with Frigade to reset your own Flow status.

### Exporting User Data

You can export your users and their state in a given Flow by clicking the **Export** button on **Users** tab on a Flow detail page. This will download a CSV file with all of the user's data and state in the given Flow. Alternatively, you can use the [API](/api-reference/users/users-get) to fetch user data programmatically or use the [Webhooks](/api-reference/webhooks) whenever a user takes actions in your Flows.

### Standardized User Fields

When sending user properties to Frigade, the platform will automatically decorate the following fields on the user profile:

* `firstName`
* `lastName`
* `email`
* `organization`
* `profilePicture`

<Frame>
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/users.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7a218d9c17ffbcb2d6f67c0a842f6565" alt="Users" data-og-width="3456" width="3456" data-og-height="1994" height="1994" data-path="images/platform/users.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/users.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=517ef6bc15d92776657a8953a4af2a66 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/users.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=97bde8fb87ea0c0082a6afea0d884a21 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/users.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=227aa3ff5152e2dc650dbc05dc53079e 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/users.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=773cdc62a48d84bb5b769ad63c2d6caa 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/users.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=efaf9617808beb2a0bce5e864157638e 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/users.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=400db77cda1008ae1662e33138f08fc8 2500w" />
</Frame>

## Group Management

***

You can view all of your groups and their associated data on the <a href="https://app.frigade.com/users" target="_blank">groups</a> page. Groups allows you to associate an individual user with a group (e.g. a company, organization, account, project, or team).
Groups will automatically show up in Frigade once they have been identified in your app (see [SDK](/sdk/hooks/group) or [API](/api-reference/groups) docs for more info).

The group detail page will show all of a group's members and where they are in your onboarding Flows. Groups are especially helpful if you have any tasks in your product that are shared across a group of users.

For example, you may want to implement a checklist with a Step that can be completed by any user in the group (e.g. connecting a third party API). You can use groups to ensure once that Step is completed by one user it will be completed for all users.

### Standardized Group Fields

When sending group properties to Frigade, the platform will automatically decorate the following fields on the group:

* `name`
* `imageUrl`
* `website`

<Frame>
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/groups.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=957acdd5f519204940f3b7f198b4ea68" alt="Groups" data-og-width="3456" width="3456" data-og-height="1994" height="1994" data-path="images/platform/groups.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/groups.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7a4fb43d40363ff5644375702bb6479f 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/groups.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=e0c1512862f2a766aa80652411ec2580 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/groups.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=73f10d589c4c75568125a705875b2386 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/groups.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=cec457cf4b9558359c3a44d8d2ee2054 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/groups.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7e10e3ce61a5fc4a8f6b1c9eb11257b1 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/groups.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=c3faa8ccd79a8fd33e5ae8e8588ee008 2500w" />
</Frame>
