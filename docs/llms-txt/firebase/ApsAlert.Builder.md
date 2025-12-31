# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder.md.txt

# ApsAlert.Builder

public static class **ApsAlert.Builder** extends Object  

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder) | [addAllLocalizationArgs](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder#addAllLocalizationArgs(java.util.List<java.lang.String>))(List\<String\> args) Adds a list of resource keys that will be used in place of the format specifiers in `bodyLocKey`.   |
| [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder) | [addAllSubtitleLocArgs](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder#addAllSubtitleLocArgs(java.util.List<java.lang.String>))(List\<String\> args) Adds a list of resource keys that will be used in place of the format specifiers in `subtitleLocKey`. |
| [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder) | [addAllTitleLocArgs](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder#addAllTitleLocArgs(java.util.List<java.lang.String>))(List\<String\> args) Adds a list of resource keys that will be used in place of the format specifiers in `titleLocKey`.          |
| [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder) | [addLocalizationArg](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder#addLocalizationArg(java.lang.String))(String arg) Adds a resource key string that will be used in place of the format specifiers in `bodyLocKey`.                                      |
| [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder) | [addSubtitleLocalizationArg](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder#addSubtitleLocalizationArg(java.lang.String))(String arg) Adds a resource key string that will be used in place of the format specifiers in `subtitleLocKey`.                  |
| [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder) | [addTitleLocalizationArg](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder#addTitleLocalizationArg(java.lang.String))(String arg) Adds a resource key string that will be used in place of the format specifiers in `titleLocKey`.                           |
| [ApsAlert](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder#build())() Creates a new [ApsAlert](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert) instance from the parameters set on this builder.       |
| [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder) | [setActionLocalizationKey](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder#setActionLocalizationKey(java.lang.String))(String actionLocKey) Sets the key of the text in the app's string resources to use to localize the action button text.               |
| [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder) | [setBody](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder#setBody(java.lang.String))(String body) Sets the body of the alert.                                                                                                                               |
| [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder) | [setLaunchImage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder#setLaunchImage(java.lang.String))(String launchImage) Sets the launch image for the notification action.                                                                                   |
| [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder) | [setLocalizationKey](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder#setLocalizationKey(java.lang.String))(String locKey) Sets the key of the body string in the app's string resources to use to localize the body text.                                   |
| [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder) | [setSubtitle](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder#setSubtitle(java.lang.String))(String subtitle) Sets the subtitle of the alert.                                                                                                               |
| [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder) | [setSubtitleLocalizationKey](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder#setSubtitleLocalizationKey(java.lang.String))(String subtitleLocKey) Sets the key of the subtitle string in the app's string resources to use to localize the subtitle text.   |
| [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder) | [setTitle](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder#setTitle(java.lang.String))(String title) Sets the title of the alert.                                                                                                                           |
| [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder) | [setTitleLocalizationKey](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder#setTitleLocalizationKey(java.lang.String))(String titleLocKey) Sets the key of the title string in the app's string resources to use to localize the title text.                  |

### Inherited Method Summary

From class java.lang.Object  

|------------------|---------------------------|
| Object           | clone()                   |
| boolean          | equals(Object arg0)       |
| void             | finalize()                |
| final Class\<?\> | getClass()                |
| int              | hashCode()                |
| final void       | notify()                  |
| final void       | notifyAll()               |
| String           | toString()                |
| final void       | wait(long arg0, int arg1) |
| final void       | wait(long arg0)           |
| final void       | wait()                    |

## Public Methods

#### public [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder)
**addAllLocalizationArgs**
(List\<String\> args)

Adds a list of resource keys that will be used in place of the format specifiers in
`bodyLocKey`.  

##### Parameters

| args | List of resource key strings. |
|------|-------------------------------|

##### Returns

- This builder.  

#### public [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder)
**addAllSubtitleLocArgs**
(List\<String\> args)

Adds a list of resource keys that will be used in place of the format specifiers in
`subtitleLocKey`.  

##### Parameters

| args | List of resource key strings. |
|------|-------------------------------|

##### Returns

- This builder.  

#### public [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder)
**addAllTitleLocArgs**
(List\<String\> args)

Adds a list of resource keys that will be used in place of the format specifiers in
`titleLocKey`.  

##### Parameters

| args | List of resource key strings. |
|------|-------------------------------|

##### Returns

- This builder.  

#### public [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder)
**addLocalizationArg**
(String arg)

Adds a resource key string that will be used in place of the format specifiers in
`bodyLocKey`.  

##### Parameters

| arg | Resource key string. |
|-----|----------------------|

##### Returns

- This builder.  

#### public [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder)
**addSubtitleLocalizationArg**
(String arg)

Adds a resource key string that will be used in place of the format specifiers in
`subtitleLocKey`.  

##### Parameters

| arg | Resource key string. |
|-----|----------------------|

##### Returns

- This builder.  

#### public [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder)
**addTitleLocalizationArg**
(String arg)

Adds a resource key string that will be used in place of the format specifiers in
`titleLocKey`.  

##### Parameters

| arg | Resource key string. |
|-----|----------------------|

##### Returns

- This builder.  

#### public [ApsAlert](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert)
**build**
()

Creates a new [ApsAlert](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert) instance from the parameters set on this builder.  

##### Returns

- A new [ApsAlert](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert) instance.  

##### Throws

| IllegalArgumentException | If any of the parameters set on the builder are invalid. |
|--------------------------|----------------------------------------------------------|

#### public [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder)
**setActionLocalizationKey**
(String actionLocKey)

Sets the key of the text in the app's string resources to use to localize the action button
text.  

##### Parameters

| actionLocKey | Resource key string. |
|--------------|----------------------|

##### Returns

- This builder.  

#### public [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder)
**setBody**
(String body)

Sets the body of the alert. When provided, overrides the body sent
via [Notification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification).  

##### Parameters

| body | Body of the notification. |
|------|---------------------------|

##### Returns

- This builder.  

#### public [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder)
**setLaunchImage**
(String launchImage)

Sets the launch image for the notification action.  

##### Parameters

| launchImage | An image file name. |
|-------------|---------------------|

##### Returns

- This builder.  

#### public [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder)
**setLocalizationKey**
(String locKey)

Sets the key of the body string in the app's string resources to use to localize the body
text.  

##### Parameters

| locKey | Resource key string. |
|--------|----------------------|

##### Returns

- This builder.  

#### public [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder)
**setSubtitle**
(String subtitle)

Sets the subtitle of the alert.  

##### Parameters

| subtitle | Subtitle of the notification. |
|----------|-------------------------------|

##### Returns

- This builder.  

#### public [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder)
**setSubtitleLocalizationKey**
(String subtitleLocKey)

Sets the key of the subtitle string in the app's string resources to use to localize
the subtitle text.  

##### Parameters

| subtitleLocKey | Resource key string. |
|----------------|----------------------|

##### Returns

- This builder.  

#### public [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder)
**setTitle**
(String title)

Sets the title of the alert. When provided, overrides the title sent
via [Notification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification).  

##### Parameters

| title | Title of the notification. |
|-------|----------------------------|

##### Returns

- This builder.  

#### public [ApsAlert.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert.Builder)
**setTitleLocalizationKey**
(String titleLocKey)

Sets the key of the title string in the app's string resources to use to localize the title
text.  

##### Parameters

| titleLocKey | Resource key string. |
|-------------|----------------------|

##### Returns

- This builder.