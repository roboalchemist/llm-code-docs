# Source: https://firebase.google.com/docs/reference/js/v8/firebase.messaging.FcmOptions.md.txt

# FcmOptions | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [messaging](https://firebase.google.com/docs/reference/js/v8/firebase.messaging).
- FcmOptions

Options for features provided by the FCM SDK for Web. See
[WebpushFcmOptions](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#webpushfcmoptions).

## Index

### Properties

- [analyticsLabel](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.FcmOptions#analyticslabel)
- [link](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.FcmOptions#link)

## Properties

### Optional analyticsLabel

analyticsLabel: string  
Label associated with the message's analytics data. See
[Adding analytics labels](https://firebase.google.com/docs/cloud-messaging/understand-delivery#adding-analytics-labels-to-messages).

### Optional link

link: string  
The link to open when the user clicks on the notification. For all URL values, HTTPS is
required. For example, by setting this value to your app's URL, a notification click event
will put your app in focus for the user.