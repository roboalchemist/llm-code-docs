# Source: https://docs.tavus.io/sections/conversational-video-interface/quickstart/conversation-recordings.md

# Conversation Recordings

> Enable conversation recording and store it in your S3 bucket for on-demand access.

## Prerequisite

Ensure that you have the following:

* An S3 bucket with versioning enabled.

## Enable Conversation Recording

<Steps>
  <Step title="Step 1: Set up IAM Policy and Role" titleSize="h3">
    1. Create an IAM Policy with the following JSON definition:

    ```json  theme={null}
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "VisualEditor0",
          "Effect": "Allow",
          "Action": [
            "s3:PutObject",
            "s3:GetObject",
            "s3:ListBucketMultipartUploads",
            "s3:AbortMultipartUpload",
            "s3:ListBucketVersions",
            "s3:ListBucket",
            "s3:GetObjectVersion",
            "s3:ListMultipartUploadParts"
          ],
          "Resource": [
            "arn:aws:s3:::your-bucket-name",
            "arn:aws:s3:::your-bucket-name/*"
          ]
        }
      ]
    }
    ```

    <Note>
      Replace `your-bucket-name` with your actual bucket name.
    </Note>

    2. Create an IAM role with the following value:
       * Select **"Another AWS account"** and enter this account ID: ***291871421005***.
       * Enable **"Require external ID"**, and use: **tavus**.
       * **"Max session duration"** to **12 hours**.

    <Note>
      Note down your ARN (e.g., `arn:aws:iam::123456789012:role/CVIRecordingRole`).
    </Note>
  </Step>

  <Step title="Step 2: Create a Conversation with Recording Enabled" titleSize="h3">
    Use the following request body example:

    <Info>
      Remember to change the following values:

      * `<api_key>`: Your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys" target="_blank">Developer Portal</a>.
      * `aws_assume_role_arn`: Your AWS ARN.
      * `recording_s3_bucket_region`: Your S3 region.
      * `recording_s3_bucket_name`: Your S3 bucket name.
    </Info>

    ```shell cURL {7-10} theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "properties": {
        "enable_recording": true,
        "aws_assume_role_arn": "<your_aws_arn>",
        "recording_s3_bucket_region": "<your_s3_bucket_region>",
        "recording_s3_bucket_name": "<your_s3_bucket_name>"
      },
      "replica_id": "ra066ab28864"
    }'
    ```

    <Note>
      `enable_recording` allows recording to be possible, but it doesn't start recording automatically. To begin and end recordings, users must do it manually or trigger it through frontend code.
    </Note>
  </Step>

  <Step title="Step 3: Join the Conversation" titleSize="h3">
    To join the conversation, click the **link** in the ***`conversation_url`*** field from the response:

    ```json  theme={null}

    {
      "conversation_id": "c93a7ead335b",
      "conversation_name": "New Conversation 1747654283442",
      "conversation_url": "<conversation_link>",
      "status": "active",
      "callback_url": "",
      "created_at": "2025-05-16T02:09:22.675928Z"
    }

    ```

    <Note>
      You can access the recording file in your S3 bucket.
    </Note>
  </Step>
</Steps>
