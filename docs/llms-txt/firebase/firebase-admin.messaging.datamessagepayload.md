# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.datamessagepayload.md.txt

# DataMessagePayload interface

Interface representing an FCM legacy API data message payload. Data messages let developers send up to 4KB of custom key-value pairs. The keys and values must both be strings. Keys can be any custom string, except for the following reserved strings:

- `from`
- Anything starting with `google.`

See [Build send requests](https://firebase.google.com/docs/cloud-messaging/send-message) for code samples and detailed documentation.

**Signature:**  

    export interface DataMessagePayload