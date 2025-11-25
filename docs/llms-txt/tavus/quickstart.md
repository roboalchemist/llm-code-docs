# Source: https://docs.tavus.io/sections/video/quickstart.md

# Source: https://docs.tavus.io/sections/replica/quickstart.md

# Source: https://docs.tavus.io/sections/video/quickstart.md

# Source: https://docs.tavus.io/sections/replica/quickstart.md

# Quickstart

> Create high-quality Personal or Non-human Replicas for use in conversations.

## Prerequisites

Before starting, ensure you have:

* Pre-recorded training and consent videos that meet the requirements outlined in [Replica Training](/sections/replica/replica-training).
* Publicly accessible **S3 URLs** for:
  * Your training video
  * Your consent video

<Note>
  Ensure both URLs remain valid for at least **24 hours**.
</Note>

## Create a Replica

<Steps>
  <Step title="Step 1: Create Your Replica">
    Use the following request to create the replica:

    <Tip>
      By default, replicas are trained using the `phoenix-3` model. To use an older version, set `"model_name": "phoenix-2"` in your request body. However, we strongly recommend using the latest `phoenix-3` model for improved quality and performance.
    </Tip>

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/replicas \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api-key>' \
      --data '{
        "callback_url": "",
        "replica_name": "<your_replica_name>",
        "train_video_url": "<prerecorded_video_s3_url>",
        "consent_video_url": "<prerecorded_consent_video_s3_url>"
      }'
    ```

    <Note>
      * Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys" target="_blank">Developer Portal</a>.
      * Replace `<prerecorded_video_s3_url>` with the downloadable URL of your training video.
      * Replace `<prerecorded_consent_video_s3_url>` with the downloadable URL of your consent video.
    </Note>

    Once submitted, your replica will begin training in the background.

    <Note>
      This process typically takes 4–6 hours.
    </Note>
  </Step>

  <Step title="Step 2: Check Replica Status">
    You can monitor the training status using the <a href="/api-reference/phoenix-replica-model/get-replica" target="_blank">Get Replica</a> endpoint:

    ```shell cURL theme={null}
    curl --request GET \
      --url https://tavusapi.com/v2/replicas/{replica_id} \
      --header 'x-api-key: <api-key>'

    ```

    <Note>
      Replace `<api_key>` with your actual API key.
    </Note>
  </Step>

  <Step title="Step 3: Start Using Your Replica">
    Once training is complete, you can use your non-human replica for:

    * [Conversational Video Interface](/sections/conversational-video-interface/overview-cvi)
    * [Video Generation](/sections/video/overview)
  </Step>
</Steps>

## Non-human Replica

To create a non-human replica, you do not need a **consent video**:

<Note> If you're using the <a href="https://platform.tavus.io/" target="_blank">Developer Portal</a>, select the **Skip** tab in the consent video window. </Note>

```shell cURL theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/replicas \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '{
    "callback_url": "",
    "replica_name": "<replica_name>",
    "train_video_url": "<prerecorded_video_s3_url>"
  }'
```

<Note>
  * Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys" target="_blank">Developer Portal</a>.
  * Replace `<your_replica_name>` with the name for your non-human replica.
  * Replace `<prerecorded_video_s3_url>` with the downloadable URL of your training video.
</Note>
