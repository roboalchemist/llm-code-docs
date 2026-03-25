# Source: https://documentation.onesignal.com/docs/en/delete-users.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete users

> Learn how to safely delete users and subscriptions in OneSignal using the Dashboard or API, including bulk deletion, automatic deletion rules, and privacy compliance.

## Why delete users or subscriptions?

You may want to delete [Users](./users) and [Subscriptions](./subscriptions) for a few reasons:

1. **Data privacy compliance** – to honor user requests for data removal.
2. **Cleanup inactive data** – remove old subscriptions from users who no longer use your app or website, or have switched devices.

<Warning>
  Once you delete users, this action is irreversible. Deleted users can only receive messages again if they:

* **Web:** Clear browser cookies and revisit your site.
* **Mobile:** Reopen the app (ensure the app uses the latest OneSignal SDK).
* **Email/SMS:** Are re-added with the same email or phone number.
</Warning>

***

## Recommendations before deletion

1. [**Export user data**](./exporting-data)
   Download a CSV containing all user data and custom fields for backup or compliance.

2. **Understand the difference** between [Users](./users) and [Subscriptions](./subscriptions).

3. **Double-check your audience** to prevent accidental deletion.

<Warning>
  Always verify your filters and data before proceeding. Deletions cannot be undone.
</Warning>

***

## Automatic subscription deletion (Free Plan only)

* On **Paid Plans**, subscriptions are kept until manually deleted.
* On the **Free Plan**, OneSignal **automatically deletes dormant push subscriptions** after 18 months of inactivity.

**Dormancy means:**

* The app or site hasn't been opened in 18+ months, **or**
* No activity has been recorded in that time

See our [Privacy Policy](https://onesignal.com/privacy_policy) for more information.

***

## Delete users and subscriptions with the API

<Warning>
  Always verify data before proceeding. Deletions cannot be undone.
</Warning>

Use the [**Delete User API**](/reference/delete-user) to remove a user and all associated data.

* Supports deletion using `external_id`, `onesignal_id`, or other aliases.
* Best for privacy compliance or full user record removal.

Use the [**Delete Subscription API**](/reference/delete-subscription) to delete individual [Subscriptions](./subscriptions), such as old devices or sessions.

***

## Delete users and subscriptions in the dashboard

<Warning>
  Always verify data before proceeding. Deletions cannot be undone.
</Warning>

<Tabs>
  <Tab title="Individual deletion">
    1. Go to **Audience > Subscriptions**
    2. Search for the subscription you want to delete
    3. Click **Options > Delete**

    <Frame caption="Delete Subscription">
      <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/c84b86c-Screenshot_2024-04-12_at_11.27.44_AM.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=65f65ebe63052c9ea8d67e84cd26a82f" width="2252" height="908" data-path="images/docs/c84b86c-Screenshot_2024-04-12_at_11.27.44_AM.png" />
    </Frame>
  </Tab>

  <Tab title="Bulk deletion">
    To delete multiple users or subscriptions:

    1. Create a segment

    * Follow [Segmentation docs](./segmentation) to build your segment.
    * To target a list, [upload a CSV](./import) and apply tags.
    * To remove inactive users, filter by **Last Session > 4321 hours** (\~6 months). Ensure you're using "greater than" (not "less than").

    <Note>
      We also recommend sending two re-engagement notifications to the segment before deletion.
    </Note>

    2. View the segment

    * Navigate to **Options > View Subscriptions** from the segment view.

    <Frame caption="View Subscriptions Screenshot">
      <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/4ed62fb6c622c8d015748d361a05dc1559a2a7ae1b7c4d4e2c59a2dfcfd629b5-view_subscribtions.jpg?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=c16c52d41ffcd4d7fa993e447638a5d5" width="2302" height="1274" data-path="images/docs/4ed62fb6c622c8d015748d361a05dc1559a2a7ae1b7c4d4e2c59a2dfcfd629b5-view_subscribtions.jpg" />
    </Frame>

    3. Delete

    * In **Audience > Subscriptions**:
      * Select the segment.
      * Click the arrow next to **Update/Import Users**.
      * Choose **Delete Subscriptions In Segment**.

    <Frame caption="Bulk Delete Dropdown">
      <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/6dbc5ea-Screenshot_2024-04-12_at_11.32.38_AM.png?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=d39a8b033e7cd299ccbcbc34bb06e27e" width="1914" height="620" data-path="images/docs/6dbc5ea-Screenshot_2024-04-12_at_11.32.38_AM.png" />
    </Frame>

    You'll see a confirmation screen with the number of records and a prompt to input the segment name.

    <Warning>
      Once you confirm deletion, it cannot be undone.
    </Warning>

    <Frame caption="Delete confirmation">
      <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/f8b9b27-Screenshot_2024-04-12_at_11.42.33_AM.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=e454ff5ad379903a9b77a764bad3d6f9" width="764" height="606" data-path="images/docs/f8b9b27-Screenshot_2024-04-12_at_11.42.33_AM.png" />
    </Frame>

    After confirmation, a success screen will appear and you'll receive a confirmation email.

    You can only delete one segment at a time per app.

    <Frame caption="Deletion confirmation">
      <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/7d4d5b0-Screenshot_2024-04-12_at_12.03.04_PM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=bbcf7c3c5abda50eaf75ae4a1b953134" width="760" height="402" data-path="images/docs/7d4d5b0-Screenshot_2024-04-12_at_12.03.04_PM.png" />
    </Frame>
  </Tab>
</Tabs>

***

Built with [Mintlify](https://mintlify.com).
