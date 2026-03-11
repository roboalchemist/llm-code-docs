# Source: https://novita.ai/docs/api-reference/model-apis-task-result.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Task Result

**This API is used to retrieve images, audio, or video results from v3 asynchronous tasks using the `task_id`.**

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Query Parameters

<ParamField query="task_id" type="string" required={true}>
  Returned in the 200 response of v3 asynchronous APIs.
</ParamField>

## Response

<ResponseField name="extra" type="object" required={false}>
  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="seed" type="string" required={false}>
      A seed is a number from which Stable Diffusion generates noise, making generation deterministic. Using the same seed and set of parameters will produce identical images each time, minimum -1.
    </ResponseField>

    <ResponseField name="enable_nsfw_detection" type="boolean" required={false}>
      When set to true, NSFW detection will be enabled, incurring an additional cost of \$0.0015 for each generated image.
    </ResponseField>

    <ResponseField name="debug_info" type="object" required={false}>
      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="request_info" type="string" required={false}>
          Records request parameters for debugging purposes.
        </ResponseField>

        <ResponseField name="submit_time_ms" type="string" required={false}>
          The timestamp (in milliseconds) of when the task was submitted.
        </ResponseField>

        <ResponseField name="execute_time_ms" type="string" required={false}>
          The timestamp (in milliseconds) of when the task started execution.
        </ResponseField>

        <ResponseField name="complete_time_ms" type="string" required={false}>
          The timestamp (in milliseconds) of when the task was completed.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="task" type="object" required={false}>
  Task information.

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="task_id" type="string" required={false}>
      Task ID.
    </ResponseField>

    <ResponseField name="status" type="string" required={false}>
      Indicates the current status of a task. This parameter allows you to filter results based on the following status categories: `TASK_STATUS_QUEUED`: The task is queued and awaiting processing. `TASK_STATUS_SUCCEED`: The task has been processed successfully. `TASK_STATUS_FAILED`: The task failed during processing. `TASK_STATUS_PROCESSING`: The task is currently being processed.<br />
      Enum: `TASK_STATUS_QUEUED`, `TASK_STATUS_SUCCEED`, `TASK_STATUS_FAILED`, `TASK_STATUS_PROCESSING`
    </ResponseField>

    <ResponseField name="reason" type="string" required={false}>
      Provides the reason for a task's failure. This parameter specifies the explanation or error message associated with tasks that did not succeed. Utilizing this filter can aid in diagnosing issues and implementing corrective actions for failed processes.
    </ResponseField>

    <ResponseField name="task_type" type="string" required={false}>
      Specifies the type of task.
    </ResponseField>

    <ResponseField name="eta" type="number" required={false}>
      Specifies the estimated time of completion for tasks, measured in seconds. This parameter is particularly relevant for video-type tasks, providing a forecast of how long it will take to complete the task based on current processing parameters and system load. This information can be vital for planning and resource management in environments with time-sensitive video processing requirements.
    </ResponseField>

    <ResponseField name="progress_percent" type="number" required={false}>
      Progress of task completion in percentage. This feature is currently available only for: <br /> 1. Video Generator APIs; <br /> 2. Text-to-Image API and Image-to-Image API.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="images" type="object[]" required={false}>
  Contains information about images associated with image-type tasks. This parameter provides detailed data on each image processed or generated during the task, such as file paths, metadata, or any image-specific attributes. It is returned only for tasks that involve image operations, facilitating enhanced tracking and management of image data.

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="image_url" type="string" required={false}>
      Image URL.
    </ResponseField>

    <ResponseField name="image_url_ttl" type="integer" required={false}>
      Image expiration time in seconds.
    </ResponseField>

    <ResponseField name="image_type" type="string" required={false}>
      Image type.<br />
      Enum: `jpeg`, `png`, `webp`
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="videos" type="object[]" required={false}>
  Contains information about videos associated with video-type tasks. This parameter provides detailed data on each video processed or generated during the task, such as file paths, metadata, or any video-specific attributes. It is returned only for tasks that involve video operations, facilitating enhanced tracking and management of video data.

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="video_url" type="string" required={false}>
      Video URL.
    </ResponseField>

    <ResponseField name="video_url_ttl" type="string" required={false}>
      Video expiration time in seconds.
    </ResponseField>

    <ResponseField name="video_type" type="string" required={false}>
      Video type.<br />
      Enum: `mp4`, `gif`
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="audios" type="object[]" required={false}>
  Contains information about audios associated with audio type tasks. This parameter provides detailed data on each audio processed or generated during the task, such as file paths, metadata, or any image-specific attributes. It is returned only for tasks that involve audio operations, facilitating enhanced tracking and management of audio data.

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="audio_url" type="string" required={false}>
      Audio url.
    </ResponseField>

    <ResponseField name="audio_url_ttl" type="string" required={false}>
      Audio url expire time in seconds.
    </ResponseField>

    <ResponseField name="audio_type" type="string" required={false}>
      Audio type.<br />
      Enum: `wav`
    </ResponseField>

    <ResponseField name="audio_metadata" type="object" required={false}>
      Contains detailed metadata about audio files processed or generated during audio-related tasks.

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="text" type="string" required={false} />

        <ResponseField name="start_time" type="float32" required={false}>
          the start\_time of the text in seconds.
        </ResponseField>

        <ResponseField name="end_time" type="float32" required={false}>
          the end\_time of the text in seconds.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

## Example

request

```bash  theme={"system"}
curl --location --globoff 'https://api.novita.ai/v3/async/task-result?task_id={{Novita-TaskID}}' \
--header 'Authorization: Bearer {{API Key}}'
```

response

```json  theme={"system"}
{
  "extra": {
    "seed": "158881667",
    "enable_nsfw_detection": false,
    "debug_info": {
      "request_info": "",
      "submit_time_ms": "",
      "execute_time_ms": "",
      "complete_time_ms": ""
    }
  },
  "task": {
    "task_id": "830d9c90-d53f-4c5a-8009-xxx",
    "status": "TASK_STATUS_SUCCEED",
    "reason": "",
    "task_type": "TXT_TO_IMG",
    "eta": 0,
    "progress_percent": 0
  },
  "images": [
    {
      "image_url": "https://faas-output-image.s3.ap-southeast-1.amazonaws.com/prod/xxx",
      "image_url_ttl": 3600,
      "image_type": "jpeg",
      "nsfw_detection_result": {}
    }
  ],
  "videos": [],
  "audios": []
}
```


Built with [Mintlify](https://mintlify.com).