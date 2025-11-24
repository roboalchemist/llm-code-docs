# Source: https://docs.frigade.com/platform/users-and-groups.md

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
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/platform/users.png" alt="Users" />
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
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/platform/groups.png" alt="Groups" />
</Frame>
