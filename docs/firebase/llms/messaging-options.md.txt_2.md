# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/messaging-options.md.txt

# firebase::messaging::MessagingOptions Struct Reference

# firebase::messaging::MessagingOptions


`#include <messaging.h>`

A class to configure the behavior of Firebase Cloud Messaging.

## Summary

This class contains various configuration options that control some of Firebase Cloud Messaging's behavior.

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/messaging-options#structfirebase_1_1messaging_1_1_messaging_options_1a06a963c548d00be65b157f909e3a389f()` Default constructor. ||

| ### Public attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/messaging/messaging-options#structfirebase_1_1messaging_1_1_messaging_options_1a271b720f0fdfc7394a7e47b1c04dca87` | `bool` If true, do not display the prompt to the user requesting permission to allow notifications to this app. |

## Public attributes

### suppress_notification_permission_prompt

```c++
bool firebase::messaging::MessagingOptions::suppress_notification_permission_prompt
```
If true, do not display the prompt to the user requesting permission to allow notifications to this app.

If the prompt is suppressed in this way, the developer must manually prompt the user for permission at some point in the future using `https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#namespacefirebase_1_1messaging_1abb0bdae9b9173ae0eb7901401f5f8a51`.

If this prompt has already been accepted once in the past the prompt will not be displayed again.

This option currently only applies to iOS and tvOS.

## Public functions

### MessagingOptions

```c++
 firebase::messaging::MessagingOptions::MessagingOptions()
```
Default constructor.