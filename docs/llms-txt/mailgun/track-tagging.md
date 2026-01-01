# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/tracking-messages/track-tagging.md

# Tags

Mailgun allows you to tag your email with unique identifiers. They can help segment your email into relevant categories for later analysis and optimization. Tags are visible via event data and will be included in webhook payloads.

Examples of when to use a tag:

- Identifying mail type, like âpassword resetâ or âwelcomeâ
- Identifying campaign or audience, like âBlack Fridayâ or ânew signupâ


Tags are further enhanced when using Mailgun for open and click tracking. You can understand the full performance of your tag via Analytics in the Mailgun UI, including comparison to other tags.

### Tagging Code Sample


```
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages \
    -F from='Excited User <postmaster@YOUR_DOMAIN_NAME>' \
    -F to=recipient@example.com \
    -F subject="Hello there!" \
    -F text='Testing some Mailgun awesomeness!' \
    -F o:tag='September newsletter' \
    -F o:tag='newsletters
```

Note:
- By default, each account is allowed a maximum of 20,000 tags per domain. If more tags are needed, please go [here](https://app.mailgun.com/support/list) to create a ticket for Mailgun's Support Team.
- A single message may be marked with up to 3 tags. Tags are case insensitive and should be ascii only. The maximum length of characters is 128.