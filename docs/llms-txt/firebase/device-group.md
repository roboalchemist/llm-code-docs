# Source: https://firebase.google.com/docs/cloud-messaging/js/device-group.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/cpp/device-group.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/unity/device-group.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/ios/device-group.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/android/device-group.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/unity/device-group.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/ios/device-group.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/android/device-group.md.txt

<br />

Device group messaging allows you to add multiple devices to a single group.
This is similar to topic messaging, but includes authentication to ensure that
group membership is managed only by your servers. For example, if you want to
send different messages to different phone models, your servers can add/remove
registrations to the appropriate groups and send the appropriate message to each
group. Device group messaging differs from topic messaging in that it involves
managing device groups from your servers instead of directly within your
application.

The maximum number of members allowed for a notification key is 20.

## Managing device groups


Before sending messages to a device group, you must:

1.
   Obtain registration tokens for each device you want to add
   to the group.

2.
   Create the `notification_key`, which identifies
   the device group by mapping a particular group (typically a
   user) to all of the group's associated registration tokens.
   You can create notification keys on the app server.


Basic management of device groups --- creating and removing groups,
and adding or removing devices --- is performed via the HTTP v1 API,
using short-lived tokens to
[authorize send requests](https://firebase.google.com/docs/cloud-messaging/auth-server).
See [Device group management keys](https://firebase.google.com/docs/cloud-messaging/android/device-group#device-group-management-keys) for a list of supported keys.

### Managing device groups on the app server

#### Creating a device group


To create a device group, send a POST request that provides a name
for the group, and a list of registration tokens for the devices.
FCM returns a new `notification_key`
that represents the device group.

**HTTP POST request**


Send a request like the following to
`https://fcm.googleapis.com/fcm/notification`:  

```verilog
https://fcm.googleapis.com/fcm/notification
Content-Type:application/json
access_token_auth: true
Authorization: Bearer ya29.ElqKBGN2Ri_Uz...HnS_uNreA
project_id:SENDER_ID

{
   "operation": "create",
   "notification_key_name": "appUser-Chris",
   "registration_ids": ["bk3RNwTe3H0:CI2k_HHwgIpoDKCIZvvDMExUdFQ3P1...",
                        "cR1rjyj4_Kc:APA91bGusqbypSuMdsh7jSNrW4nzsM...",
                        ... ]
```


The `notification_key_name` is a name or identifier
(e.g., it can be a username) that is unique to a given group. The
`notification_key_name` and
`notification_key` are unique to a group of registration
tokens. It is important that `notification_key_name` is
unique per client app if you have multiple client apps for the same
[sender ID](https://firebase.google.com/docs/cloud-messaging/concept-options#senderid).
This ensures that messages only go to the intended target app.

**Response format**

A successful request returns a `notification_key` like
the following:  

```scdoc
{
   "notification_key": "APA91bGHXQBB...9QgnYOEURwm0I3lmyqzk2TXQ"
}
```


Save the `notification_key` and the corresponding
`notification_key_name` to use in subsequent operations.
| Invalid registration tokens are dropped when a device group is successfully created.

#### Retrieving a notification key


If you need to retrieve an existing notification key, use the
`notification_key_name` in a GET request as shown:  

```component-pascal
https://fcm.googleapis.com/fcm/notification?notification_key_name=appUser-Chris
Content-Type:application/json
access_token_auth: true
Authorization: Bearer ya29.ElqKBGN2Ri_Uz...HnS_uNreA
project_id:SENDER_ID
{}
```

For each GET request for a given notification key name, the server
returns a unique encoded string. Though each string may appear to be
a different key, it is actually a valid \`notification_key\` value.

#### Adding and removing devices from a device group


To add or remove devices from an existing group, send a POST
request with the `operation` parameter set to
`add` or `remove`, and provide the
registration tokens for addition or removal.
| If you remove all existing registration tokens from a device group, FCM deletes the device group.

**HTTP POST request**

For example, to add a
device with the registration token `bk3RNwTe3H0:CI2k_HHwgIpoDKCIZvvDMExUdFQ3P1...`
to `appUser-Chris`, you would send this request:  

    {
       "operation": "add",
       "notification_key_name": "appUser-Chris",
       "notification_key": "APA91bGHXQBB...9QgnYOEURwm0I3lmyqzk2TXQ",
       "registration_ids": ["bk3RNwTe3H0:CI2k_HHwgIpoDKCIZvvDMExUdFQ3P1..."]
    }

**Response format**

A successful request to either add or remove a device returns a
`notification_key` like the following:  

```scdoc
{
   "notification_key": "APA91bGHXQBB...9QgnYOEURwm0I3lmyqzk2TXQ"
}
```
| **Note:** `notification_key_name` is not required for adding/removing registration tokens, but including it protects you against accidentally using the incorrect `notification_key`.

## Device group management keys

The following table lists the keys for creating device groups
and adding and removing members.


**Table 10.** Device group management keys.

|        Parameter        |                      Usage                      |                                                                                      Description                                                                                      |
|-------------------------|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `operation`             | Required, string                                | The operation to run.Valid values are `create`, `add`, and `remove`.                                                                                                                  |
| `notification_key_name` | Required, string                                | The user-defined name of the device group to create or modify.                                                                                                                        |
| `notification_key`      | Required (except for `create` operation, string | Unique identifier of the device group. This value is returned in the response for a successful `create` operation, and is required for all subsequent operations on the device group. |
| `registration_ids`      | Required, array of strings                      | The device tokens to add or remove. If you remove all existing registration tokens from a device group, FCM deletes the device group.                                                 |

## Sending messages to device groups

Sending messages to a device group is very similar to sending
messages to an individual device, using the same method to
[authorize send requests](https://firebase.google.com/docs/cloud-messaging/auth-server). Set the `token`
field to the group notification key:  

### REST

POST https://fcm.googleapis.com/v1/projects/myproject-b5ae1/messages:send HTTP/1.1

Content-Type: application/json
Authorization: Bearer ya29.ElqKBGN2Ri_Uz...HnS_uNreA

{
"message":{
"token":"APA91bGHXQBB...9QgnYOEURwm0I3lmyqzk2TXQ",
"notification": {
"title": "Hello",
"body": "This is a Firebase Cloud Messaging device group message!"
}
}
}

### cURL command

curl -X POST -H "Authorization: Bearer ya29.ElqKBGN2Ri_Uz...HnS_uNreA" -H
"Content-Type: application/json" -d '{
"message":{
"notification": {
"title": "Hello",
"body": "This is a Firebase Cloud Messaging device group message!"
},
"token":"APA91bGHXQBB...9QgnYOEURwm0I3lmyqzk2TXQ"
}}' https://fcm.googleapis.com/v1/projects/myproject-b5ae1/messages:send
| **Note:** Unlike the device group send methods in deprecated legacy APIs, the HTTP v1 response does not contain success and failure counts. A successful send returns an empty response.