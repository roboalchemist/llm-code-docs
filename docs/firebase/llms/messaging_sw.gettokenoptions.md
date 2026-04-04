# Source: https://firebase.google.com/docs/reference/js/messaging_sw.gettokenoptions.md.txt

# GetTokenOptions interface

Options for [getToken()](https://firebase.google.com/docs/reference/js/messaging_.md#gettoken_b538f38).

**Signature:**  

    export interface GetTokenOptions 

## Properties

|                                                                      Property                                                                       |           Type            |                                                                                                                                                                                                                                                                                                                                                      Description                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [serviceWorkerRegistration](https://firebase.google.com/docs/reference/js/messaging_sw.gettokenoptions.md#gettokenoptionsserviceworkerregistration) | ServiceWorkerRegistration | The service worker registration for receiving push messaging. If the registration is not provided explicitly, you need to have a `firebase-messaging-sw.js` at your root location. See [Access the registration token](https://firebase.google.com/docs/cloud-messaging/js/client#access_the_registration_token) for more details.                                                                                                                                                                                                                                                                                                                                                                                     |
| [vapidKey](https://firebase.google.com/docs/reference/js/messaging_sw.gettokenoptions.md#gettokenoptionsvapidkey)                                   | string                    | The public server key provided to push services. The key is used to authenticate push subscribers to receive push messages only from sending servers that hold the corresponding private key. If it is not provided, a default VAPID key is used. Note that some push services (Chrome Push Service) require a non-default VAPID key. Therefore, it is recommended to generate and import a VAPID key for your project with [Configure Web Credentials with FCM](https://firebase.google.com/docs/cloud-messaging/js/client#configure_web_credentials_in_your_app). See [The Web Push Protocol](https://developers.google.com/web/fundamentals/push-notifications/web-push-protocol) for details on web push services. |

## GetTokenOptions.serviceWorkerRegistration

The service worker registration for receiving push messaging. If the registration is not provided explicitly, you need to have a `firebase-messaging-sw.js` at your root location. See [Access the registration token](https://firebase.google.com/docs/cloud-messaging/js/client#access_the_registration_token) for more details.

**Signature:**  

    serviceWorkerRegistration?: ServiceWorkerRegistration;

## GetTokenOptions.vapidKey

The public server key provided to push services. The key is used to authenticate push subscribers to receive push messages only from sending servers that hold the corresponding private key. If it is not provided, a default VAPID key is used. Note that some push services (Chrome Push Service) require a non-default VAPID key. Therefore, it is recommended to generate and import a VAPID key for your project with [Configure Web Credentials with FCM](https://firebase.google.com/docs/cloud-messaging/js/client#configure_web_credentials_in_your_app). See [The Web Push Protocol](https://developers.google.com/web/fundamentals/push-notifications/web-push-protocol) for details on web push services.

**Signature:**  

    vapidKey?: string;