# Source: https://docs.carv.io/carv-ecosystem/carv-play/carv-intro/api-verified-quest-restful.md

# API-Verified Quest (RESTFUL)

## Introduction

CARV allows the use of OpenAPI to verify whether a user has completed a quest.&#x20;

## Sequence Digram

<figure><img src="https://758822945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6A1MZN6YkMg4U1B64H4g%2Fuploads%2F0nGZz2JzFrKPMDWeWbRz%2Fimage.png?alt=media&#x26;token=db4b3af0-b618-4d6c-959c-c371cd7692a3" alt=""><figcaption></figcaption></figure>

## Specifications&#x20;

**Request**

The API used for verification must be an open API. \
You can choose to use either **email** or **wallet address** or **user ID of third-party platforms** as the identifier to verify a user. \
You can choose *optionally* to add custom headers to the request, such as an API key.\
We will also include **begin time** and **end time** (timestamp in milliseconds) for a quest in case this information is required for verification.&#x20;

So a GET Request will look like the followings:

{% code overflow="wrap" %}

```sh
# wallet address
curl https://<domain>/<serverpath>?address=<userAddress>&begin_time=<timestamp>&end_time=<timestamp>
```

{% endcode %}

OR

{% code overflow="wrap" %}

```sh
# email
curl https://<domain>/<serverpath>?email=<userEmail>&begin_time=<timestamp>&end_time=<timestamp>
```

{% endcode %}

OR

{% code overflow="wrap" %}

```sh
# Telegram id
curl https://<domain>/<serverpath>?telegram_id=<userTelegramId>&begin_time=<timestamp>&end_time=<timestamp>
```

{% endcode %}

OR

{% code overflow="wrap" %}

```sh
# Line id
curl https://<domain>/<serverpath>?line_id=<userTelegramId>&begin_time=<timestamp>&end_time=<timestamp>
```

{% endcode %}

#### Response Format

{% code overflow="wrap" %}

```json
{
    "result":{                    //required on success
        "isValid":<true | false>  //boolean: whether the user completed the quest.
    },
    "error":{                      //required on error, this field MUST NOT exist if there was no error triggered during invocation.
        "code":<error code>,       //number
        "message":"<error message>"
    }
}
```

{% endcode %}
