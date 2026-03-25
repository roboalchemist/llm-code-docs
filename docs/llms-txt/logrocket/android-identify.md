# Source: https://docs.logrocket.com/reference/android-identify.md

# Identify Users (Android)

Identify users within your Android Native application

Associate a user identifier with the active user. You can use any string that uniquely identifies the user of your application such as a database ID, an email, or a username.

```java
SDK.identify("28dvm2jfa");
```

`SDK.identify()` can be called up to 10 times per session.

User traits can be added with a map as the second argument to `SDK.identify`.

```java
Map<String, String> userData = new HashMap<>();

userData.put("name", "Jane Smith");
userData.put("email", "janesmith@gmail.com");
userData.put("favoriteColor", "blue");

SDK.identify("28dvm2jfa", userData);
```

For more detailed information on User Identication at LogRocket check out our [identification reference documentation](https://docs.logrocket.com/reference/identify).