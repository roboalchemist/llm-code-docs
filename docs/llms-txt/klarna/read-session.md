# Source: https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/integrate-via-hpp/api-documentation/read-session.md

# Read Session with Hosted Payment Page - API Details

When you have created an **HPP Session**you will have the ability to read its content by using thesession_urlthat you got back in the create session response. For that, you only to make a request to the endpoint and you will get data that lets you track the update of the session. It is advised to read our [guide on how to track the HPP Session status changes](https://docs.klarna.com/payments/other-products/hosted-payment-page/before-you-start/tracking-session-status/).

## Endpoint description

| **Description** | **Gets the status of the HPP Session** |
|----|----|
| Reference | For a full list of returned values, please read [API Reference](https://docs.klarna.com/api/api-urls/). |
| Url structure | <https: %7bendpoint%7d="" %7bsession_id%7d="" hpp="" sessions="" v1=""> |
| Operation | GET |
| Example | curl <https: api.klarna.com="" hpp="" sessions="" v1=""></https:><session_id> --header "Authorization: Basic <token> " --header "Content-Type: application/json" --header “Cache-Control: no-cache” |

| Field Key | **Type** | **Description** |
|----|----|----|
| **session_id** | String | Identifier of the session that was read. |
| **status** | String | The current status of the Session. You can read more about statuses in our [session lifecycle article](https://docs.klarna.com/payments/other-products/hosted-payment-page/before-you-start/tracking-session-status/). |
| **updated_at** | Date | Last time this session was updated. [Dates format is described here](https://docs.klarna.com/api/api-urls/#data-types). |
| **expires_at** | Date | Date when this session will not be able for the consumer to pay anymore. You can read more about lifetime in our [session lifetime article](https://docs.klarna.com/payments/other-products/hosted-payment-page/before-you-start/tracking-session-status/). [Dates format is described here](https://docs.klarna.com/api/api-urls/#data-types). |

| **Status name** | **Status description** |
|----|----|
| **WAITING** | Session is created and Consumer has not entered the Payment Page yet |
| **IN_PROGRESS** | Consumer has entered the Payment Page on updated_at |
| **COMPLETED** | Consumer has successfully gotten an Authorization from the Payment system onupdated_at, **Authorization Token**is contained in the authorization_tokenfield. |
| **FAILED** | Consumer was not able to completely fulfil the payment on updated_at |
| **CANCELLED** | Consumer has pressed the Back button on updated_at |
| **ERROR** | Consumer encountered an error while paying on updated_at |
| **DISABLED** | Session was disabled by API Call on the Merchant initiative on updated_at |

## Happy flow examples

These are the responses that an integration layer will get when polling the HPP Session during its fulfilment.

``` json
{
    "session_id": "39a1c773-bafd-754d-af1f-b30c592f1267",
    "status": "WAITING",
    "updated_at": "2019-05-13T14:51:46.288Z",
    "expires_at": "2019-05-15T13:51:43.507Z"
}
```

Newly created HPP Session

``` json
{
    "session_id": "39a1c773-bafd-754d-af1f-b30c592f1267",
    "status": "IN_PROGRESS",
    "updated_at": "2019-05-13T14:52:57.540Z",
    "expires_at": "2019-05-15T13:51:43.507Z"
}
```

Consumer has loaded the HPP Session

``` json
{
    "session_id": "39a1c773-bafd-754d-af1f-b30c592f1267",
    "status": "COMPLETED",
    "authorization_token": "a1a8f727-2756-6058-bd3c-40069be0994b",
    "updated_at": "2019-05-13T14:54:04.675Z",
    "expires_at": "2019-05-15T13:51:43.507Z"
}
```

Completed HPP Session - Default value forplace_order_mode

``` json
{
    "session_id": "39a1c773-bafd-754d-af1f-b30c592f1267",
    "status": "COMPLETED",
    "order_id": "a1a8f727-2756-6058-bd3c-40069be0994b",
    "klarna_reference": "X438HG0Q",
    "updated_at": "2019-05-13T14:54:04.675Z",
    "expires_at": "2019-05-15T13:51:43.507Z"
}
```

With place_order_mode as PLACE_ORDER or CAPTURE_ORDER

``` json
{
    "session_id": "39a1c773-bafd-754d-af1f-b30c592f1267",
    "status": "COMPLETED",
    "order_id": "a1a8f727-2756-6058-bd3c-40069be0994b",
    "klarna_reference": "X438HG0Q",
    "updated_at": "2019-05-13T14:54:04.675Z",
    "expires_at": "2019-05-15T13:51:43.507Z"
}
```</token></session_id></https:>