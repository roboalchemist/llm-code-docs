# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/sending-messages/mailing-lists.md

# Mailing Lists

Mailing Lists are a great way to send to multiple recipients while using an email alias. When you use mailing lists, Mailgun will send a copy of the message to each subscribed member using the email alias. You can create and maintain your subscriber lists using the API or Control Panel. In addition, you can use Template Variables to create a unique message for each member of the mailing list.

### Using Mailing Lists

1. Create a mailing list email address (example: devs@example.com)
2. Add member email addresses to the mailing list
3. Each time you send a message using the mailing list email address (example: devs@example.com), a copy of the email is delivered to each subscribed member.


### Managing a Mailing List

You can create Mailing Lists using the Mailing Lists tab in the Control Panel or through the API. To make it easier, Mailgun has support for a couple different formats to upload Mailing List members:

- You can upload a CSV file with the members.
- You can use a JSON array form parameter
- You can use form-like file upload


Creating a mailing list through the API:


```bash
curl -s --user 'api:YOUR_API_KEY' \
   https://api.mailgun.net/v3/lists \
   -F address='LIST@YOUR_DOMAIN_NAME' \
   -F description='Mailgun developers list'
```

Adding a single member through the API:


```bash
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/lists/LIST@YOUR_DOMAIN_NAME/members \
    -F subscribed=True \
    -F address='bar@example.com' \
    -F name='Bob Bar' \
    -F description='Developer' \
    -F vars='{"age": 26}'
```

Adding multiple members using the JSON array approach, you can either send a flat list of member addresses:


```bash
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/lists/LIST@YOUR_DOMAIN_NAME/members.json \
    -F members='["alice@example.com","bob@example.com"]'
```

Members added this way are implicitly set as `subscribed`.

Alternatively, you can provide the full JSON payload expected for a member for the same
fine-grained control when adding a single member:


```bash
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/lists/LIST@YOUR_DOMAIN_NAME/members.json \
    -F members='[{"name": "Bob Bar", "address": "bar@example.com", "subscribed": true, "vars": "{}"}]'
```

Info
Note the use of `vars` to attach a JSON dictionary with structured data to each member of the mailing list.
You can reference that data in the body of the message using Template Variables.

There are two modes available when adding a new member, strict and upsert.

- Strict will raise an error in case the member already exists.
- Upsert will update an existing member if it's already in the list or insert a new one.


Learn how to toggle between the modes and skip malformed addresses in the API documentation pages for the Mailing Lists API

### Sending to a Mailing List

Sending to a Mailing List is as easy as using one of our APIs, HTTP or SMTP, and sending an email to the
address created for the Mailing List as the recipient.

You can set the access level on Mailing Lists to:

- Only allow the administrator to post to the list (limited to an API call or authenticated SMTP session)
- Allow Mailing List members to post to the list
- Allow anybody to post to the list


### Replying to a Mailing List

You can set the preferred method to where a reply to the list should go:

- `list` Replies to the list go to the list address. This is the default setting for any new list created, except for read-only lists, where replies can only go to the sender. Reply-all will still go to the list.
- `sender` Replies to the list going to the sender (FROM) address. This is the default and the only option for read-only lists.


### Template Variables

There are some pre-defined variables you can use to personalize your message to each recipient.

| Header | Description |
|  --- | --- |
| `%recipient%` | Full recipient spec, like âBob [bob@example.com](mailto:bob@example.com)â (for using as value for âToâ MIME header). |
| `%recipient_email%` | Recipientâs email address, like bob@example.com. |
| `%recipient_name%` | Recipientâs full name, like âJohn Q. Publicâ. |
| `%recipient_fname%` | Recipientâs first name. |
| `%recipient_lname%` | Recipientâs last name. |
| `%unsubscribe_url%` | A generated URL which allows users to unsubscribe from messages. |
| `%mailing_list_unsubscribe_url%` | A generated URL which allows users to unsubscribe from mailing lists. |
| `%unsubscribe_email%` | An email address which can be used for automatic unsubscription by adding it to List-Unsubscribe MIME header. |
| `%recipient.yourvar%` | Accessing a custom datavalue. (see Attaching Data to Messages) |


### Unsubscribing

To manage unsubscribes in Mailing Lists, you can use %mailing_list_unsubscribe_url%.
Mailgun will generate a unique link to unsubscribe from the mailing list. Once a recipient clicks on the unsubscribe link. The recipient is marked as "unsubscribed" from this mailing list and won't get any further emails addressed to this list.

Info
You can still override the "unsubscribe" setting via the API or the Control Panel (in case of user error or accidental unsubscribe). You can also manually unsubscribe to the customer without using any links via the API or the Control Panel. Read more in the Mailing Lists API section.

### Mailing Lists and Routes

Mailing lists work independently from Routes. When there is a Mailing List or Route with the same address, the incoming message will hit the Route and Mailing List simultaneously. This can be convenient for processing replies to the Mailing List and integrating into things like forums or commenting systems.