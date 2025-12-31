# Source: https://loops.so/docs/events/properties.md

# Source: https://loops.so/docs/contacts/properties.md

# Source: https://loops.so/docs/events/properties.md

# Source: https://loops.so/docs/contacts/properties.md

# Source: https://loops.so/docs/events/properties.md

# Source: https://loops.so/docs/contacts/properties.md

# Source: https://loops.so/docs/events/properties.md

# Source: https://loops.so/docs/contacts/properties.md

# Contact properties

> How to add, edit and delete contact properties.

## Default contact properties

These are the default properties for every contact on Loops. They cannot be deleted.

| Contact Property | Example                                 | Email Tag\*   | API Name\*\* |
| ---------------- | --------------------------------------- | ------------- | ------------ |
| Email            | *[hi@example.co](mailto:hi@example.co)* | `{email}`     | `email`      |
| First Name       | *Chris*                                 | `{firstName}` | `firstName`  |
| Last Name        | *Frantz*                                | `{lastName}`  | `lastName`   |
| Notes            | *Favorite color is blue.*               | `{notes}`     | N/A          |
| Source           | *API*                                   | `{source}`    | `source`     |
| Subscribed       | `true`                                  | N/A           | `subscribed` |
| User Group       | *Investors*                             | `{userGroup}` | `userGroup`  |
| User Id          | *ask523236*                             | `{userId}`    | `userId`     |

\* Used to [add personalization to emails](/creating-emails/personalizing-emails#dynamic-tag-syntax).\
\*\* Used in [API requests](/api-reference).

### Source

"Source" describes where the contact originated from.

By default, this value will be "Form" for contacts added [via a form](/forms/simple-form), or "API" for contacts added [via the API](/api-reference). You can specifiy custom "Source" values when adding contacts via forms and the API.

### Subscribed

The "Subscribed" value determines whether a contact is able to receive **loops and campaigns**. Unsubscribed contacts *will continue to receive all transactional emails*.

Contacts can unsubscribe from your emails using an [Unsubscribe link](/creating-emails/editor#footer-content) automatically added to your campaigns and loops.

Some important notes:

* We do not charge for unsubscribed contacts.
* We suggest you keep unsubscribed contacts in your audience. If you delete and then re-add them in the future somehow, they may end up being "subscribed" even though they have been unsubscribed.
* You cannot re-subscribe contacts via a [CSV upload](/add-users/csv-upload) or from the Audience page in Loops. You can re-subscribe contacts [with the API](/api-reference/update-contact) and with some of [our integrations](/integrations#manage-contacts).

#### Using `subscribed` in API requests

When you include a `subscribed` value in your API requests, you will manually change the contact's subscribed status. For example, if you send `subscribed: true` when updating a contact, previously unsubscribed contacts will be re-subscribed.

<Tip>
  We recommend leaving `subscribed` out of your API requests unless you specifically want to unsubscribe or re-subscribe a contact. All new contacts are subscribed by default (`subscribed: true`).
</Tip>

### User Group

"User Group" is a useful optional property that you can use to segment contacts. It is a free text field that allows you to easily divide contacts into groups like "Users", "VIPs", "Investors" or "Customers".

Contacts can currently only have one user group value.

### User Id

"User Id" is a unique external ID you can assign to each contact in your audience. For example, this could be a customer ID from your store or a user ID from your SaaS.

This field is optional but is very useful if you are working with our API. For example, you need a user ID to be able to [change a contact's email address](/api-reference/update-contact).

### Mailing lists

Read about [how to use mailing lists](/contacts/mailing-lists) in Loops.

## Custom contact properties

Custom contact properties are additional fields that you can create to store information about contacts.

### Types of property

Custom contact properties can be one of four different types:

* String
* Number
* Boolean
* Date (see below)

You can specify a property type when creating new properties in Loops.

#### Dates

When sending dates with the [API](/api-reference) or via one of our [integrations](/integrations), you can use either a Unix timestamp (*in milliseconds*) or an [ECMA-262 date-time string](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-date-time-string-format).

Timestamps must be in milliseconds and can be sent as either an integer or string.

* `1705486871000` (if the Unix timestamp is `1705486871`)

Supported date formats are shown below. These must be sent as a string. Adding a time offset at the end (e.g. `+02:00` or `-07:00`) is optional (if omitted, the date will default to UTC).

* `YYYY-MM-DDTHH:MM:SS.sss`
* `YYYY-MM-DDTHH:MM:SS`
* `YYYY-MM-DDTHH:MM`
* `YYYY-MM-DD HH:MM:SS.sss`
* `YYYY-MM-DD HH:MM:SS`
* `YYYY-MM-DD HH:MM`
* `YYYY-MM-DD`

### Reserved names

Note that Loops does not allow the creation of properties with the following reserved names:

* `id`
* `listId`
* `softDeleteAt`
* `teamId`
* `updatedAt`

### Add a property

One way to create custom contact properties is to go to [your Audience](https://app.loops.so/audience) and click on any of the column headers, then select **Add property**.

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/option-1.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=dfd54fc9d1617522bd38fb9728c86339" alt="" data-og-width="2280" width="2280" data-og-height="1164" height="1164" data-path="images/option-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/option-1.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=bb60c6c7a809e7e1345aec2d96c2c7c5 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/option-1.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=30a04aaa869bedf437bac488cf4e4816 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/option-1.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=ace204c0693bd6dd55fd31fbc3d053e7 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/option-1.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=4a58fa3d13bb2cdcc9e4dc1e695272ef 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/option-1.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=1d32cb00afcbf9da7b7e91ad5d2d4ea7 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/option-1.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=5fb641e0f9fa6a4279899dd1b61a0d9e 2500w" />

Alternatively you can scroll to the end of the Audience table and click the `+` button at the end of the column headers.

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/option-2.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=06f5d71eb384b3394aed91d72b190d84" alt="" data-og-width="2280" width="2280" data-og-height="1164" height="1164" data-path="images/option-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/option-2.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=c13a851bf6cea6397a0c8ac0906495b2 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/option-2.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=806dff1de628fbf4bb31cc247f6afe76 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/option-2.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=f111d3274c811fdd8f686b0a75e7df53 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/option-2.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=f1901f4dc9a67335c76cd5dd28902427 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/option-2.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=7ee27545c925385fa5151238244e3f8e 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/option-2.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=b0b0fb3cc8dc64e70e8b495a634ee53b 2500w" />

A third way is to go your [API Settings](http://app.loops.so/settings?page=api) page, scroll down to the Contact properties section and click **Add property**.

In each of these cases, you'll see a form asking you for a property name and type.

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-property-form.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=7d7f6415ba25b44524450e9dd534a867" alt="" data-og-width="2280" width="2280" data-og-height="1418" height="1418" data-path="images/add-property-form.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-property-form.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=246b4218146462032b2b9aebf655e28e 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-property-form.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=a14032af7c442bcd6949b95b00be8318 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-property-form.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=e7877cc7c2cc80cfac2cb2aabdca78c8 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-property-form.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=fad9f62cb34ac9ab0ce493115fd4c533 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-property-form.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=e68ef39d22b421a15ffe661c82f91c9f 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-property-form.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=f07d15294f78937209b7040e1dcb0907 2500w" />

It's also possible to [create contact properties with the API](/api-reference/create-contact-property).

```json  theme={"dark"}
POST https://app.loops.so/api/v1/contacts/properties

{
  "name": "myCustomProperty",
  "type": "string"
}
```

### Deleting contact properties

You can delete properties on the Audience page by clicking on column headers.

<img src="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-property-dropdown.png?fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=69c4c0de2c58c54654596903fc2db51e" alt="" data-og-width="2280" width="2280" data-og-height="1217" height="1217" data-path="images/delete-property-dropdown.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-property-dropdown.png?w=280&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=43859e350445d349372519e122c946ef 280w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-property-dropdown.png?w=560&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=1b1a5b27a4e5e800e6cf2368cb7b58bf 560w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-property-dropdown.png?w=840&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=f8ea49501ad9be5d76550c2d643eeba6 840w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-property-dropdown.png?w=1100&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=cc31dc0af7e6e8201fb1ce3b349bebef 1100w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-property-dropdown.png?w=1650&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=ee5a29e45f1809ead75db0a95885d6b8 1650w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-property-dropdown.png?w=2500&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=c829c7a586d4b5b60ed06d320efb1bc8 2500w" />

You can also delete properties from your [API Settings](http://app.loops.so/settings?page=api) page by clicking the trashcan icons.

It is not possible to delete default contact properties.

<Warning>
  Once a contact property is deleted, all associated data will also be deleted and cannot be recovered. It's important to be sure that you won't need the information stored in a property before deleting it.
</Warning>

#### Property in use warning

If you receive a “Property in use” warning modal while deleting a contact property, there are a few things you can check before you're able to delete the property.

* If the listed email is a Campaign:
  * Check if the property is in use as [dynamic content](/creating-emails/personalizing-emails) inside the email editor
  * Ensure this property is not being actively used in the Audience filter
* If the listed email inside a Loop:
  * Make sure a draft or running Loop is not using it as part of the Audience filter or as a Trigger

<img src="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-property.png?fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=03f0aeba3e3e36b18ebca459b3ced831" alt="" data-og-width="1430" width="1430" data-og-height="584" height="584" data-path="images/delete-property.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-property.png?w=280&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=a90302c362686ea0fe10ffc7292277fc 280w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-property.png?w=560&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=e44cea1447454fde3cf8358e4d85645d 560w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-property.png?w=840&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=cc8a93f6304979293d249394c255f510 840w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-property.png?w=1100&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=5061243cc3274030122a9418d7e6efef 1100w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-property.png?w=1650&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=7ff6abcf9c10eec9a92d23b150ac710d 1650w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-property.png?w=2500&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=e7d56527ec8d809a9be3d28f64aa7e65 2500w" />
