# Source: https://docs.logrocket.com/reference/react-native-identify.md

# Identify Users (React Native)

Identify users within your React Native application

Identifying your users helps you find you find their sessions in the LogRocket dashboard.

Call `LogRocket.identify()` on page loads to associate your own application-specific user ID with the active user. These user identifiers will be referred to as "UIDs".

`LogRocket.identify()` can be called up to 10 times per session.

```javascript JavaScript
LogRocket.identify(uid);
```

You can use any string that uniquely identifies the user of your application, such as a database ID, an email, or a username.

If you do not provide a UID, the user will be assigned a random one and shown as "Anonymous" in the UI.

```javascript Examples
LogRocket.identify('123456') // an immutable ID from your database (preferred)
LogRocket.identify('foo@bar.com') // the user's email
```

It's recommended to use an immutable database ID if available. Names and email addresses can be added as user traits as they could change.

## Specify other user traits

Other user information can also be given. This information will not be displayed in the session list directly, but can used for searching through sessions using a **User Traits** filter. They will also be displayed in the user details section of the session playback.

```javascript
LogRocket.identify('123456', {
  name: 'Jane Smith',
  email: 'janesmith@logrocket.com',
  age: 43,
  favoriteColor: 'blue',
});
```

> 📘
>
> Here are a few gotchas to avoid while using `LogRocket.identify`:
>
> * `LogRocket.identify` only accepts strings as UIDs. Make sure to cast your UID to a string before calling this function.
> * There is no need to call `LogRocket.identify` for anonymous or logged out users.
> * If `LogRocket.identify` is called multiple times during a recording, you can search for any of the identified users in the session, however only 1 user will be displayed in the session list at a time.

> 🚧
>
> Custom user traits are identified on the **user** and will be the same across all of their sessions. Use [LogRocket.track()](#track) to add information to individual sessions.

> 🚧
>
> When searching within LogRocket using the [User Trait filter](https://docs.logrocket.com/docs/logrocket-filters#user-identification-filters), please note that we limit the search to 512 characters.  Any terms greater than this length will be discarded.