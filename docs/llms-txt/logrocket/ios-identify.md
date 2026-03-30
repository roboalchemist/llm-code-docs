# Source: https://docs.logrocket.com/reference/ios-identify.md

# Identify Users (iOS)

Identify users within your iOS Native application

Associate a user identifier with the active user. You can use any string that uniquely identifies the user of your application such as a database ID, an email, or a username.

```swift Swift
SDK.identify(userID: "28dvm2jfa")
```

```objectivec Objective-C
[LROSDK identifyWithUserID:@"28dvm2jfa" userInfo:@{}]
```

`SDK.identify()` can be called up to 10 times per session.

User traits can be added with a map as the second argument to SDK.identify.

```swift Swift
SDK.identify(userID: "28dvm2jfa", [
  "name": "Jane Smith",
  "email": "janesmith@gmail.com",
  "favoriteColor": "blue",
])
```

```objectivec Objective-C
[LROSDK identifyWithUserID:@"28dvm2jfa", userInfo:@{
  "name": "Jane Smith",
  "email": "janesmith@gmail.com",
  "favoriteColor": "blue",
}]
```