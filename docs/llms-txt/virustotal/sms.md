# Source: https://virustotal.readme.io/reference/sms.md

# sms_sent

Sent SMSs during the execution of the file under study.

`sms_sent` contains a list of **sent SMSs during the execution of a given file.**

It is a list, every item on the list containing the following fields:

* `body`<*string*> message text itself.
* `destination` <*string*> telephone number to which the SMS is sent.

```json Sent SMSs
{
    "data": {
        "attributes": {
            "sms_sent": [
                {
                    "body": "<string>",
                    "destination": "<string>"
                }
            ]
        }
    }
}
```
```json Example
{
    "data": {
        "attributes": {
            "sms_sent": [
                {
                    "body": "40659+3079+123636+x+a",
                    "destination": "3865"
                },
                {
                    "body": "40659+3079+123636+x+a",
                    "destination": "2865"
                },
                {
                    "body": "40659+3079+123636+x+a",
                    "destination": "4865"
                },
            ]
        }
    }
}
```