# Source: https://loops.so/docs/add-users/loops-api.md

# API

> Loops provides a REST API to manage your contacts.

With [the Loops API](/api-reference), you can easily manage contacts directly from your application or service.

For example, creating a new contact is as easy as sending a `POST` request to `https://app.loops.so/api/v1/contacts/create`.

```json  theme={"dark"}
{
  "email": "adam@loops.so",
  "firstName": "Adam",
  "lastName": "Kaczmarek",
  "favoriteColor": "blue",
  "userGroup": "Founders",
  "source": "Signup form Service"
}
```

We also offer endpoints for finding, updating and deleting contacts (plus some other features like sending transactional email and sending events).

## Learn more

<CardGroup>
  <Card title="API Reference" icon="rectangle-terminal" href="/api-reference">
    Find out how to send events using our API.
  </Card>
</CardGroup>
