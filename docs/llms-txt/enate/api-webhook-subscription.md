# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/webhooks/api-webhook-subscription.md

# API Webhook Subscription

Two [**GET** operations ](#get-all-webhook-subscriptions)and three [**POST** operations](#post-operations) are present under Webhook Subscription. These are the API for the client to consume and subscribe to the webhooks.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWnb30vDLQE7_ULyA2F%2F-MWnb6C1NkNl5Kwq6Mgs%2Fimage.png?alt=media\&token=78c0c101-2c53-4b24-98f0-abcedaea719a)

## GET Operations <a href="#get-all-webhook-subscriptions" id="get-all-webhook-subscriptions"></a>

* [Get All Webhook Subscriptions](#get-all-webhook-subscriptions-2) - use this to get a list of all available webhooks you can subscribe to.
* [Get Webhook Subscriptions ](#get-webhook-subscription-1)- use this to get more details for a single kind of subscription.

### Get All Webhook Subscriptions <a href="#get-all-webhook-subscriptions" id="get-all-webhook-subscriptions"></a>

Path /WebHookSubscription/GetAllWebhookSubscriptions&#x20;

* Type: GET&#x20;
* Function: Returns a list of all Webhook Subscriptions&#x20;
* No parameters required
* Expected Response – list of subscriptions in the following format:

```
[
  {
    "GUID": "00000000-0000-0000-0000-000000000000",
    "Webhook": "PacketCreated",
    "FilterObjectGUID": "00000000-0000-0000-0000-000000000000",
    "FilterObjectType": "None",
    "SubscriberURL": "string",
    "Signature": "string",
    "CustomHeader": "string",
    "CustomHeaderValue": "string"
  }
]
```

### Get Webhook Subscription <a href="#get-webhook-subscription" id="get-webhook-subscription"></a>

Path: /WebHookSubscription/GetWebhookSubscription&#x20;

* Type: GET&#x20;
* Function: Returns detail of a specific Webhook Subscription&#x20;
* Parameter to set: webhookSubscriptionGUID&#x20;
* Parameter values: GUID value present in GUID column of tblWebhookSubscriptions table.

Expected Response – a single subscription in the following format:

```
[
  {
    "GUID": "00000000-0000-0000-0000-000000000000",
    "Webhook": "PacketCreated",
    "FilterObjectGUID": "00000000-0000-0000-0000-000000000000",
    "FilterObjectType": "None",
    "SubscriberURL": "string",
    "Signature": "string",
    "CustomHeader": "string",
    "CustomHeaderValue": "string"
  }
]
```

Response Code: 200 :

Expected Response in case of invalid GUID: \
Response Code:400 - Bad Request \
The response should contain the below message: \
‘The request is invalid’ Request:

## POST Operations

* [Subscribe to Webhook](#subscribe-to-webhook-api) - use this to subscribe to an individual webhook.
* [Update Webhook Subscription](#update-webhook-subcription) - use this to update an existing subscription to an individual webhook
* [Unsubscribe ](#delete-webhook-subscription)- use this to permanently delete an existing subscription for an individual webhook.

### Subscribe to Webhook API <a href="#subscribe-to-webhook-api" id="subscribe-to-webhook-api"></a>

Path: /WebHookSubscription/SubscribeToWebhook&#x20;

* Type: POST&#x20;
* Function: Used to create a new subscription and the API returns the details of newly created
* Webhook Subscription&#x20;
* Parameters:

  ```
  {
    "Webhook": "PacketCreated",
    "FilterObjectGUID": "00000000-0000-0000-0000-000000000000",
    "FilterObjectType": "None",
    "SubscriberURL": "string",
    "CustomHeader": "string",
    "CustomHeaderValue": "string"
  }
  ```

Expected Response: \
Response Code:200 \
Expected Response – subscription data in the following format:

```
[
  {
    "GUID": "00000000-0000-0000-0000-000000000000",
    "Webhook": "PacketCreated",
    "FilterObjectGUID": "00000000-0000-0000-0000-000000000000",
    "FilterObjectType": "None",
    "SubscriberURL": "string",
    "Signature": "string",
    "CustomHeader": "string",
    "CustomHeaderValue": "string"
  }
]
```

{% hint style="info" %}
Note: The subscriber URL is the address of the client that will receive the webhook messages. We can use <https://webhook.site/> to get the subscriber URL.
{% endhint %}

The signature should be added by the server when the subscription is created and then included in the webhook messages which are sent out.

### Update Webhook Subcription <a href="#update-webhook-subcription" id="update-webhook-subcription"></a>

Parameters and response as for [SubscribeToWebhook](#subscribe-to-webhook-api) plus the GUID of the WebHookSubscription to update

### Unsubscribe (Delete Webhook Subscription) <a href="#delete-webhook-subscription" id="delete-webhook-subscription"></a>

* Takes a Webhook subscription GUID as the only parameter.&#x20;
* Permanently deletes a subscription from the database.

## API: Webhook Test-Simulate Event <a href="#api-webhook-test-simulate-event" id="api-webhook-test-simulate-event"></a>

A GET API called Simulate Event is present under Webhook Test.

* Parameter: any valid webHookSubscriptionGUID&#x20;
* Creates a test WebHook message for a provided webHookSubscriptionGUID

## General API Validations <a href="#general-api-validations" id="general-api-validations"></a>

### Authorization <a href="#authorization" id="authorization"></a>

When an unauthorized request is sent, the APIs need to show a message stating ‘Authorization has been denied for this request’. Below is the response in case of an unauthorised request:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWnb30vDLQE7_ULyA2F%2F-MWnc1MM21rFTndNjZ3c%2Fimage.png?alt=media\&token=0c85f281-0743-4b6e-ab0e-c4caf7e14a60)

Quick steps to vaidate authorization:

1. Open the Swagger UI&#x20;
2. Do not login to the test instance&#x20;
3. Send a request with all the valid details&#x20;
4. API throws an error saying Authorization has been denied&#x20;
5. Login to the test instance&#x20;
6. Retry the same request&#x20;
7. API returns successful response as the request is authorized.&#x20;

### Invalid Requests <a href="#invalid-requests" id="invalid-requests"></a>

When an invalid request is submitted, the APIs need to return 400-Bad Request Error and display a message stating, ‘The request is invalid’. Below is the response in case of invalid requests:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWnb30vDLQE7_ULyA2F%2F-MWnc8YyoAVD60fvx_8F%2Fimage.png?alt=media\&token=8dedc586-05c9-4710-8d86-519259e2dd0e)

General scenarios where bad request error is seen are mentioned below:

* Wrong/Incorrect GUID values
* Syntax errors in the Request json
* Non existing values
