# Source: https://developers-classic.mailerlite.com/reference/single-subscriber.md

# /subscribers/(:id or :email)

Get single subscriber [Rate limited]

## Response Body Parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`id`",
    "0-1": "_integer_",
    "0-2": "ID of a subscriber",
    "1-0": "`email`",
    "1-1": "_string_",
    "1-2": "Email address",
    "2-0": "`name`",
    "2-1": "_string_",
    "2-2": "Name of a subscriber",
    "3-0": "`sent`",
    "3-1": "_integer_",
    "3-2": "Count of emails sent to subscriber",
    "4-0": "`opened`",
    "4-1": "_integer_",
    "4-2": "Count of emails opened by subscriber",
    "5-0": "`clicked`",
    "5-1": "_integer_",
    "5-2": "Count of clicks made by subscriber",
    "6-0": "`type`",
    "6-1": "_string_",
    "6-2": "**Available values:**  \n  \n- `active`\n- `bounced`\n- `unsubscribed`\n- `junk`\n- `unconfirmed`",
    "7-0": "`signup_ip`",
    "7-1": "_string_",
    "7-2": "IPv4 or IPv6 address indicating the subscriber's signup",
    "8-0": "`signup_timestamp`",
    "8-1": "_string_",
    "8-2": "UTC in format Y-m-d H:i:s",
    "9-0": "`confirmation_ip`",
    "9-1": "_string_",
    "9-2": "IPv4 or IPv6 address indicating the subscriber's opt-in",
    "10-0": "`confirmation_timestamp`",
    "10-1": "_string_",
    "10-2": "UTC in format Y-m-d H:i:s",
    "11-0": "`fields`",
    "11-1": "_array_ of _objects_ [Subscriber's Field Value](https://developers-classic.mailerlite.com/docs/subscriber-custom-field)",
    "11-2": "Array which contains default and custom fields.",
    "12-0": "`date_subscribe`",
    "12-1": "_string_",
    "12-2": "Important only when getting [Subscribers in a Group](https://developers-classic.mailerlite.com/docs/subscribers-in-a-group). It shows when subscriber is added to group.  \n  \nDate format: `Y-m-d`  \nDefault value: `null`.",
    "13-0": "`date_unsubscribe`",
    "13-1": "_string_",
    "13-2": "Important only when getting [Subscribers in a Group](https://developers-classic.mailerlite.com/docs/subscribers-in-a-group). It shows when subscriber's `status` changed to `unsubscribed`.  \n  \nDate format: `Y-m-d H:i:s`  \nDefault value: `null`.",
    "14-0": "`date_created`",
    "14-1": "_string_",
    "14-2": "Date when subscriber is created  \n  \nFormat: `Y-m-d H:i:s`",
    "15-0": "`date_updated`",
    "15-1": "_string_",
    "15-2": "Datetime when subscriber is updated:  \n  \nFormat: `Y-m-d H:i:s`"
  },
  "cols": 3,
  "rows": 16,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]

> 📘 Signup & Confirmation fields
>
> * `signup_ip`
> * `signup_timestamp`
> * `confirmation_ip`
> * `confirmation_timestamp`
>
> Those fields are filled automatically using our built-in webforms.
>
> When double opt-in is enabled and subscriber signs up, we fill only `signup_*` fields. After subscriber's confirmation, `confirmation_*` fields are updated too.
>
> When double opt-in is disabled, all the fields are filled with the same data because sign up and confirmation is performed as a single action.

## Subscriber profile image

We use [Gravatar](http://gravatar.com) profile images for subscriber profile in web application. The image below is used as default.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/E5ooal9BRGSuQqqNvqpr_subscriber_big.png",
        "subscriber_big.png",
        "100"
      ],
      "align": "center",
      "caption": "<http://app.mailerlite.com/images/subscriber_big.png>"
    }
  ]
}
[/block]