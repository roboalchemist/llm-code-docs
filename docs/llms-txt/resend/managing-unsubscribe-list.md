# Source: https://resend.com/docs/dashboard/audiences/managing-unsubscribe-list.md

# Managing Unsubscribed Contacts

> Learn how to check and remove recipients who have unsubscribed to your marketing emails.

It's essential to update your Contact list when someone unsubscribes to maintain a good sender reputation.

Benefits of managing your unsubscribe list:

* reduces the likelihood of your emails being marked as spam
* improves deliverability for any other marketing or transactional emails you send

When you include an [an unsubscribe link in your Broadcasts](/dashboard/segments/introduction#automatic-unsubscribes), Resend will automatically handle the unsubscribe flow for you.

## Unsubscribe Statuses

The Contacts page shows the global unsubscribe status of each Contact.

<img alt="Unsubscribe Statuses" src="https://mintcdn.com/resend/2SHIfycCcJlAJEpt/images/audiences-contacts-intro.png?fit=max&auto=format&n=2SHIfycCcJlAJEpt&q=85&s=82101b2b495815ad50f8b7eb823876bd" data-og-width="3736" width="3736" data-og-height="1916" height="1916" data-path="images/audiences-contacts-intro.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/2SHIfycCcJlAJEpt/images/audiences-contacts-intro.png?w=280&fit=max&auto=format&n=2SHIfycCcJlAJEpt&q=85&s=f3b2b71bdfea53d79059b32998f6f5b1 280w, https://mintcdn.com/resend/2SHIfycCcJlAJEpt/images/audiences-contacts-intro.png?w=560&fit=max&auto=format&n=2SHIfycCcJlAJEpt&q=85&s=e462617c4ca2d5686bba2a830acfedef 560w, https://mintcdn.com/resend/2SHIfycCcJlAJEpt/images/audiences-contacts-intro.png?w=840&fit=max&auto=format&n=2SHIfycCcJlAJEpt&q=85&s=434b36d4ffefb9dd2d67cb69ddc35b80 840w, https://mintcdn.com/resend/2SHIfycCcJlAJEpt/images/audiences-contacts-intro.png?w=1100&fit=max&auto=format&n=2SHIfycCcJlAJEpt&q=85&s=20f9918270fc74bb725d0f90e40f55f6 1100w, https://mintcdn.com/resend/2SHIfycCcJlAJEpt/images/audiences-contacts-intro.png?w=1650&fit=max&auto=format&n=2SHIfycCcJlAJEpt&q=85&s=2dd5574fa06aac2bd8eec24f053e8409 1650w, https://mintcdn.com/resend/2SHIfycCcJlAJEpt/images/audiences-contacts-intro.png?w=2500&fit=max&auto=format&n=2SHIfycCcJlAJEpt&q=85&s=defb3039f2d4defb1db1b783cb78f131 2500w" />

* **Unsubscribed**: the Contact has unsubscribed from all emails from your account.
* **Subscribed**: the Contact is subscribed to at least one Topic.

To filter by Status, click on the **All Statuses** filter next to the search bar, then select a value.

## Topic Subscription Statuses

You can view the subscription status of each Topic for a given Contact by clicking on the Contact's row.

<img alt="Topic Subscription Statuses" src="https://mintcdn.com/resend/m2xttJpF68pi6Mw0/images/audiences-contacts-topics.png?fit=max&auto=format&n=m2xttJpF68pi6Mw0&q=85&s=56b25853b46fec447005f7aab32796fa" data-og-width="1800" width="1800" data-og-height="923" height="923" data-path="images/audiences-contacts-topics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/m2xttJpF68pi6Mw0/images/audiences-contacts-topics.png?w=280&fit=max&auto=format&n=m2xttJpF68pi6Mw0&q=85&s=d69e628fcb8cdc5830a8a6b2609849ea 280w, https://mintcdn.com/resend/m2xttJpF68pi6Mw0/images/audiences-contacts-topics.png?w=560&fit=max&auto=format&n=m2xttJpF68pi6Mw0&q=85&s=85bebe98d5e38b5a81623c5af3ac7d50 560w, https://mintcdn.com/resend/m2xttJpF68pi6Mw0/images/audiences-contacts-topics.png?w=840&fit=max&auto=format&n=m2xttJpF68pi6Mw0&q=85&s=aa9a9c13e9b89692786b250b48e2a4e0 840w, https://mintcdn.com/resend/m2xttJpF68pi6Mw0/images/audiences-contacts-topics.png?w=1100&fit=max&auto=format&n=m2xttJpF68pi6Mw0&q=85&s=27fe8caa6bd5871868894fedf4db78c5 1100w, https://mintcdn.com/resend/m2xttJpF68pi6Mw0/images/audiences-contacts-topics.png?w=1650&fit=max&auto=format&n=m2xttJpF68pi6Mw0&q=85&s=d8d1067a9441776235b57aa7a04c6be5 1650w, https://mintcdn.com/resend/m2xttJpF68pi6Mw0/images/audiences-contacts-topics.png?w=2500&fit=max&auto=format&n=m2xttJpF68pi6Mw0&q=85&s=c34271e723eea526e72a0bfed87d23ee 2500w" />

* **Subscribed**: the global subscription status for the Contact.
* **Topics**: the list of Topics the Contact is subscribed to.

You can also check a Contact's Topic subscription status [via the API or SDKs](/api-reference/contacts/get-contact-topics).

## Updating a Topic Subscription for a Contact

You can update a Topic subscription for a Contact by clicking the **Edit** button in the Topic's row.

<img alt="Add Contact to Topic" src="https://mintcdn.com/resend/WTZjpSkJsZf7Ubl_/images/dashboard-save-contact-topic.png?fit=max&auto=format&n=WTZjpSkJsZf7Ubl_&q=85&s=66e212d282f450c371f42a1b214029cd" data-og-width="1800" width="1800" data-og-height="923" height="923" data-path="images/dashboard-save-contact-topic.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/WTZjpSkJsZf7Ubl_/images/dashboard-save-contact-topic.png?w=280&fit=max&auto=format&n=WTZjpSkJsZf7Ubl_&q=85&s=b797e3daddfe352e8234a31051b404fb 280w, https://mintcdn.com/resend/WTZjpSkJsZf7Ubl_/images/dashboard-save-contact-topic.png?w=560&fit=max&auto=format&n=WTZjpSkJsZf7Ubl_&q=85&s=5cbd883c87088364c7d0c10ffc6e9032 560w, https://mintcdn.com/resend/WTZjpSkJsZf7Ubl_/images/dashboard-save-contact-topic.png?w=840&fit=max&auto=format&n=WTZjpSkJsZf7Ubl_&q=85&s=af1b159c7b2d4ffcdffa3dc08db79436 840w, https://mintcdn.com/resend/WTZjpSkJsZf7Ubl_/images/dashboard-save-contact-topic.png?w=1100&fit=max&auto=format&n=WTZjpSkJsZf7Ubl_&q=85&s=a3333dcc26612cbf90a06df77c5e91aa 1100w, https://mintcdn.com/resend/WTZjpSkJsZf7Ubl_/images/dashboard-save-contact-topic.png?w=1650&fit=max&auto=format&n=WTZjpSkJsZf7Ubl_&q=85&s=512909f7997ceaa67f98cbd55bff4da5 1650w, https://mintcdn.com/resend/WTZjpSkJsZf7Ubl_/images/dashboard-save-contact-topic.png?w=2500&fit=max&auto=format&n=WTZjpSkJsZf7Ubl_&q=85&s=4bff4c8288e55640c341976821ee7fa9 2500w" />

You can also update a Topic subscription for a Contact [via the API or SDKs](/api-reference/contacts/update-contact-topics).
