# Source: https://docs.frigade.com/sdk/advanced/linking-guest-users.md

# Merging a guest session with a authenticated user

> Link a guest session's state to a user when they register or log in

Frigade will generate a guest user ID for you if you do not provide a user id. This ID is stored in the user's browser using `localStorage`.
This allows unauthenticated users to have state in Frigade Flows and to be able to continue their session when they return to your application.

Often it is useful to link a guest session to a user when they register or log in and transfer all state and data.

You can do this by calling the [Users API endpoint](/api-reference/users/overview) with a `linkGuestId` parameter. This will merge all state from the guest session to the user with the `userId` you provide. Note that this will only take affect if the given `userId` does not yet have any state in Frigade.

To do this in Javascript, you can use the `fetch` API:

```jsx
const options = {
  method: 'POST',
  headers: { Authorization: 'Bearer <FRIGADE_PUBLIC_API_KEY>',
            'Content-Type': 'application/json' },
  body: '{"userId":"<USER_ID>", "linkGuestId":"<GUEST_ID>"}'
};

fetch('https://api.frigade.com/v1/public/users', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));
```
