# Source: https://docs.logrocket.com/reference/flutter-identify.md

# Identify Users (Flutter)

Identify users within your Flutter application

## Identify

Identifying your users helps you find you find their sessions in the LogRocket dashboard.

Call `LogRocket.identify()` on page loads to associate your own application-specific user ID with the active user. These user identifiers will be referred to as "UIDs".

`LogRocket.identify()` can be called up to 10 times per session.

```dart Flutter
LogRocket.identify(uid, null);
```

You can use any string that uniquely identifies the user of your application, such as a database ID, an email, or a username. It's recommended to use an immutable ID if available. Names and email addresses can be added as user traits as they could change.

If you do not provide a UID, the user will be assigned a random one and shown as "Anonymous" in the UI.

```dart Flutter
LogRocket.identify('123456', null) // an immutable ID from your database (preferred)
LogRocket.identify('foo@bar.com', null) // the user's email
```

## Specify user traits

Other user information can also be provided. This information will not be displayed in the session list, but it will be displayed in the User Details section in session playback., and can used to search for session by using a User Traits filter.

```dart Flutter
LogRocket.identify(uid, {
  'name': 'Jane Smith',
  'email': 'janesmith@logrocket.com',
  'signup_year': '2025',
  'favorite_color': 'purple',
});
```

> 🚧 LogRocket.identify Gotchas
>
> * `LogRocket.identify` only accepts Strings as UIDs, user trait names, and user trait values.
> * There is no need to call `LogRocket.identify` for anonymous or logged out users.
> * User Traits are identified on the **user** and will be the same across all of their sessions. Use LogRocket.track() to add information to individual sessions
> * If `LogRocket.identify` is called multiple times during a recording, you can search for any of the identified users in the session, however only 1 user will be displayed in the session list at a time.
> * When searching within LogRocket using the [User Trait filter,](https://docs.logrocket.com/docs/logrocket-filters#user-identification-filters) please note that we limit the search to 512 characters. Any terms greater than this length will be discarded.