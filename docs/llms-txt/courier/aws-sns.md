# Source: https://www.courier.com/docs/external-integrations/other/aws-sns.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# AWS SNS

> Learn how to send push, SMS, and email notifications using Courier with AWS SNS, including setup, profile requirements, and support for override credentials.

## Setup

The AWS SNS provider is listed as a Push integration but can handle push, SMS, and email notifications. To add it to your workflow in the designer, follow one of these paths:

1. **Add AWS SNS as a channel provider:** Click "Add Channel" and select the Push channel. A Push option will be added to the left menu under "Channels". Hover over this and click on the Settings icon that will appear. In the pop-up, navigate to "+ Add Integration" and search for AWS SNS.

<Frame caption="Push Channel">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/channels/push-channel.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=49b4fbdf6f2e11562218f44699f57217" alt="Push Channel" width="2504" height="900" data-path="assets/platform/channels/push-channel.png" />
</Frame>

<Frame caption="Push Channel Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/channels/push-channel-settings.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=2d3af49182b424511af9767354430129" alt="Push Channel Settings" width="2068" height="1218" data-path="assets/platform/channels/push-channel-settings.png" />
</Frame>

2. **Add AWS SNS as a provider:** Click "Add Channel" and use the search bar to find "AWS SNS"

<Frame caption="AWS SNS Integration">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/channels/aws-sns-integration.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=5d73ac8183af88b9ffba28edaaaf780b" alt="AWS SNS Integration" width="2500" height="1044" data-path="assets/platform/channels/aws-sns-integration.png" />
</Frame>

## Profile Requirements

### Push

To deliver a message to a mobile device over SNS, Courier must be provided either the Topic ARN, that the device is subscribed to, or the Target ARN that the device is subscribed to. If using a Target ARN, then this value should be included in the recipient profile as `target_arn`.

```json  theme={null}
{
  "message": {
    "to": {
      "target_arn": "your:target:arn"
    }
  }
}
```

If no `target_arn` is provided in the recipient profile then the Topic ARN will be used from the Courier configuration.

Either the Target ARN or the Topic ARN should be provided, not both.

### SMS

To deliver a message to a recipient over AWS SNS, Courier must be provided the recipient's phone number. This value should be included in the recipient profile as `phone_number`.

```json  theme={null}
{
  "message": {
    "to": {
      "phone_number": "+12345678901"
    }
  }
}
```

## Overrides

You can override the Access Key ID, Secret Access Key, and region via the `config` override. See all [SNS publish properties](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/SNS.html#publish-property).

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {},
    "providers": {
      "aws-sns": {
        "override": {
          "config": {
            "accessKeyId": "RUNTIME_ACCESS_KEY_ID",
            "secretAccessKey": "RUNTIME_SECRET_ACCESS_KEY",
            "region": "eu-west-1"
          }
        }
      }
    }
  }
}
```
