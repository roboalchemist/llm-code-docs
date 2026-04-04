# Source: https://firebase.google.com/docs/cloud-messaging/encryption.md.txt

<br />

The**Android Transport Layer** , along with the entire connection between your server, FCM backends, and client devices, is secured using**Transport Layer Security (TLS)** . This provides strong**point-to-point encryption** for all data while it's in transit, protecting it from being intercepted on the network. This robust security model is suitable for the vast majority of applications. You can find more details in the[FCM Architecture](https://firebase.google.com/docs/cloud-messaging/fcm-architecture)documentation.

One of the limitations of point to point encryption is that it's not encrypted for its entire path where only the sender and receiver can decode the message. This is whyFCMrecommends using end to end encryption for privacy sensitive communications like chat messages or authentication transcations. In order to get the most from end to end encryption, it must be implemented at a higher level, such as within your servers and app code.

## Add End-to-End Encryption for Sensitive Data

For applications handling particularly sensitive data, like private messages or personal credentials, you can add an additional layer of protection with**end-to-end encryption (E2EE)** . The process involves encrypting the message payload on your server before sending it toFCMand decrypting it within your app on the user's device. This works withFCMdata messages, as standard notification payloads are handled by the operating system and cannot be decrypted by your app before being displayed.

Note thatFCMdoesn't provide a built-in solution for end-to-end encryption. You are responsible for implementing this security layer within your application. There are external libraries and protocols designed for this purpose, such as[Capillary](https://android-developers.googleblog.com/2018/06/project-capillary-end-to-end-encryption.html)or[DTLS](https://en.wikipedia.org/wiki/Datagram_Transport_Layer_Security).

### Conceptual Example

Here is how theFCM`data`payload changes when using E2EE.

Before Encryption (Standard Payload):  

        {
          "token": "DEVICE_REGISTRATION_TOKEN",
          "data": {
            "sender": "user123",
            "message_body": "Your 2FA code is 555-123",
            "timestamp": "1661299200"
          }
        }

After Encryption (E2EE Payload):  

      {
        "token": "DEVICE_REGISTRATION_TOKEN",
        "data": {
          "encrypted_payload": "aG9va2Vk...so much encrypted gibberish...ZW5jcnlwdA=="
        }
      }

If you have implemented your e2e encryption correctly, the client application is the only party capable of decrypting encrypted payload to reveal the original message.
| **Caution:** When implementing end-to-end encryption, never store your encryption keys directly in your APK or in shared storage. This makes them vulnerable to decompilation or unauthorized access, compromising your entire security model.

## Alternative: Fetching Content Directly from Your Server

If end-to-end encryption isn't suitable for your app, you can instead send empty data messages. These messages act as a signal for the app to fetch the content directly from your servers. This means the sensitive data is only transported between your app and your servers, bypassingFCMfor the data transfer.

A drawback of this method is the potential delay caused by the app connecting to your server to retrieve the data. When an app receives a data message, it typically has only a few seconds to display a notification before being backgrounded. Fetching data from your server might not complete within this window. The success of this data fetch depends on factors like the user's device connectivity.

Therefore, consider user experience alternatives for situations where the data fetch might take too long. For example, you could display a generic notification like "You have a new message" and then update it once the full content is retrieved.