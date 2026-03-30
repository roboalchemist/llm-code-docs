# Source: https://documentation.onesignal.com/docs/en/faq-data-tags.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tags FAQ

> Get answers to all of your data tag questions

## How many tags can I set?

Check your [plan limits](https://onesignal.com/pricing), for the number of data tags that can be set per user. You are only limited on the number of data tags that can be set on each user. There is no limit to the total amount of data tag combinations that can exist within an app.

For example, free plans can have 2 tags per user, but you can still have an unlimited amount of keys and values that can be used. For example:

* UserA has tags: `first_name : Jon` and `vip_status : gold`
* UserB can have tags: `favorite_color : red` and `dogs_favorite_color : brown`.

In this case, UserA cannot have another tag like `favorite_color : green` until the `first_name` or `vip_status` tag is removed or your plan is upgraded.

If you need more data tags, [contact our sales team](https://onesignal.com/contact) to discuss more options.

### What happens to my data tags if am over the plan entitlement?

Your application will continue to have the data tags set per user. When adding or updating tags, you won't be able to make changes to users over your plan limits. This means if a user is at or over their tag limit, you will first need to delete the unwanted tags, then make another request to add or update the desired tags.

**Example:** Your account tag limit is 20. This means each user can only have 20 unique tag "keys" set at once:

<Tabs>
  <Tab title="If a user has 0 tags:">
    * Any request to set 1-20 tag keys, will succeed.
    * Any request to set 21+ tag keys, will fail, no tags will be set.
  </Tab>

  <Tab title="If a user has 19 tags:">
    * A request to set 1 new tag key will succeed.
    * A request to set 2+ new tag keys will fail, no new tags will be set.
    * A request to update 1-19 of the currently set tag values and set 1 new tag will succeed.
    * A request to update 1-19 of the currently set tag values and set 2+ new tag will fail. You need to make 2 requests. 1st to delete the unwanted tag keys, 2nd to set the new tag keys.
  </Tab>
</Tabs>

### Where can I check how many tags my users have?

Navigate to **Audience > Users** page "Tags" column or see [Exporting User Data](./exporting-data).

### How do I reduce the number of data tags my app is using?

There are several options including API updates to uploading a CSV. See [Tags](./add-user-data-tags) for a list of all options.

***

## Why are data tags not showing on a user?

There are a few reasons why tags may not be set or shown:

**Network connection and page session**

The most common reason for tags not showing on a user is due to unstable or no network connection when the tag update request is made.

**v5 Mobile SDKs** will cache data tags locally and will retry adding the tag upon detecting a stable internet connection.

**Web SDK** requires the user to be created before tags can be set. This means the user subscribed to web push or you called the `addEmail/addSms` methods to create a subscription (we recommend calling the `login` method to associate the subscription with a user).

Once the user is created, the tags will automatically be sent to our server as long as the page session is the same (the user has not navigated to another page).

If the user leaves the page before the tags are set, they will not get the tags. Use the `getTags` method to check if the tags are set or call the `addTags` method again.

**Clearing browser cache**

When web subscribers clear their browser data it destroys the subscription data stored on the browser. OneSignal provides a feature to automatically resubscribe the user upon returning to the site, but this will not add the tags back unless either:

1. The `login` method is called which will associate the new subscription with the existing user and their tags.
2. The tagging methods are called again.

<Note>
  See [Web push browser behavior](./browser-behavior-and-unsubscribes) for more details.
</Note>

***

Built with [Mintlify](https://mintlify.com).
