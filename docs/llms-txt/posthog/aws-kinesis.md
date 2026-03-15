# Source: https://posthog.com/docs/cdp/destinations/aws-kinesis.md

# Send PostHog event data to AWS Kinesis - Docs

Send event data from PostHog into an AWS Kinesis stream.

You'll also need access to the relevant AWS account.

## Installation

1.  In PostHog, click the [Data pipeline](https://app.posthog.com/data-management/destinations) tab in the left sidebar.
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations) tab.
3.  Search for 'AWS Kinesis' and click **\+ Create**.
4.  Add your AWS Access Key ID and Secret Access Key at the configuration step.
5.  Press **Create & Enable** and watch your 'Events' get sent to AWS Kinesis!

## Configuration

| Option | Description |
| --- | --- |
| AWS Access Key IDType: stringRequired: True |
| AWS Secret Access KeyType: stringRequired: True |
| AWS RegionType: stringRequired: True |
| Kinesis Stream NameType: stringRequired: True |
| Kinesis Partition KeyType: stringRequired: False | If not provided, a random UUID will be generated. |
| Message PayloadType: jsonRequired: False |

How to create this via the API

Using our REST API you can create this destination like so:

Terminal

PostHog AI

```bash
# Create a new destination
curl --location 'https://us.i.posthog.com/api/environments/:project_id/hog_functions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <POSTHOG_PERSONAL_API_KEY>' \
--data '{
    "type": "destination",
    "name": "AWS Kinesis",
    "inputs": {
        "aws_access_key_id": {
            "value": ""
        },
        "aws_secret_access_key": {
            "value": ""
        },
        "aws_region": {
            "value": "us-east-1"
        },
        "aws_kinesis_stream_name": {
            "value": ""
        },
        "aws_kinesis_partition_key": {
            "value": "{event.uuid}"
        },
        "payload": {
            "value": {
                "event": "{event}",
                "person": "{person}"
            }
        }
    },
    "enabled": true,
    "template_id": "template-aws-kinesis"
}'
```

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/aws_kinesis/template_aws_kinesis.py) is available on GitHub.

### Who maintains this?

This is maintained by PostHog. If you have issues with it not functioning as intended, please [let us know](https://us.posthog.com/#panel=support%3Asupport%3Aapps%3A%3Atrue)!

### What if I have feedback on this destination?

We love feature requests and feedback. Please [tell us what you think](https://us.posthog.com/#panel=support%3Afeedback%3Aapps%3Alow%3Atrue).

### What if my question isn't answered above?

We love answering questions. Ask us anything via [our community forum](/questions.md).

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better