# Source: https://loops.so/docs/contacts/delete-contacts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete contacts

> Remove contacts from your audience.

## Delete single contacts

You can delete contacts from your audience on the [Audience page](https://app.loops.so/audience).

Click the `•••` menu icon on the contact you want to delete and select **Delete**.

<img src="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-contact.png?fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=ced0bc6159407807c091a018541568d4" alt="Deleting a contact" data-og-width="2280" width="2280" data-og-height="1080" height="1080" data-path="images/delete-contact.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-contact.png?w=280&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=a38326c1e8cea28801983411e25d618d 280w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-contact.png?w=560&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=f7d756cd1f68f9ebb62d2ef2b42179b5 560w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-contact.png?w=840&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=63ccf511bc123e4cebd1491bd6036d5d 840w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-contact.png?w=1100&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=76ae269ced315eb021d6c61a0ece46cc 1100w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-contact.png?w=1650&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=830524ad7b1c6873b204d2024b1e1df3 1650w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-contact.png?w=2500&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=610f52c182c4a8c043115fd9705766c1 2500w" />

## Delete groups of contacts

To delete contacts in bulk, use the filters on the [Audience page](https://app.loops.so/audience) to narrow down the selection of contacts you want to delete.

Then click the `•••` menu icon in the filter box at the top of the Audience page and select **Delete contacts**.

This button will delete all contacts listed in the table below, based on the filter(s) you set up.

<img src="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-contacts.png?fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=6424b46a47d391683bbe514630d3a4d5" alt="Deleting contacts in bulk using filters" data-og-width="2280" width="2280" data-og-height="1080" height="1080" data-path="images/delete-contacts.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-contacts.png?w=280&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=11e319c65d3c553e3214a70b3a140310 280w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-contacts.png?w=560&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=bcb91286edfdde88a2eae5cbeee2ff8b 560w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-contacts.png?w=840&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=a2c0d4b6120b8926589675c7e96d8c23 840w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-contacts.png?w=1100&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=c29e13a36b9a03c7e05b1f1072880b81 1100w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-contacts.png?w=1650&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=e60ee765dea1550429454b60bd74d8e2 1650w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-contacts.png?w=2500&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=8753f4139f40eda5d87a042d69e2e128 2500w" />

## Delete contacts with the API

You can delete single contacts using the API's [Delete contact](/api-reference/delete-contact) endpoint, by email address or `userId` value.

```json  theme={"dark"}
POST https://app.loops.so/api/v1/contacts/delete

{
  "email": "contact123@mail.com"
}
```
