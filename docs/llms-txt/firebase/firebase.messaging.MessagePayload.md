# Source: https://firebase.google.com/docs/reference/js/v8/firebase.messaging.MessagePayload.md.txt

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [messaging](https://firebase.google.com/docs/reference/js/v8/firebase.messaging).
- MessagePayload


Message payload that contains the notification payload that is represented with
[firebase.messaging.NotificationPayload](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.NotificationPayload)
and the data payload that contains an arbitrary number of key-value pairs sent by
developers through the
[Send API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#notification)

## Index

### Properties

- [collapseKey](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.MessagePayload#collapsekey)
- [data](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.MessagePayload#data)
- [fcmOptions](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.MessagePayload#fcmoptions)
- [from](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.MessagePayload#from)
- [notification](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.MessagePayload#notification)

## Properties

### collapseKey

collapseKey: string  

The collapse key of this message. See
[Collapsible and non-collapsible messages](https://firebase.google.com/docs/cloud-messaging/customize-messages/collapsible-message-types).

### Optional data

data: {}  
Arbitrary key/value pairs.  

#### Type declaration

-

  ##### \[key:
  string\]: string

### Optional fcmOptions

fcmOptions: [FcmOptions](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.FcmOptions)  

See
[firebase.messaging.FcmOptions](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.FcmOptions).

### from

from: string  
The sender of this message.

### Optional notification

notification: [NotificationPayload](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.NotificationPayload)  

See
[firebase.messaging.NotificationPayload](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.NotificationPayload).