# Source: https://novita.ai/docs/api-reference/model-apis-heygen-video-translate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Heygen Video-translate

Translate videos into 175+ languages using natural voice cloning and accurate lip-sync alignment.

<Tip>
  This is an **asynchronous** API; only the **task\_id** will be returned. You should use the **task\_id** to request the [**Task Result API**](/api-reference/model-apis-task-result) to retrieve the video generation results.
</Tip>

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Supports: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="video" type="string" required={true}>
  Video URL to translate. Must be publicly accessible. Supports direct URLs, Google Drive, and YouTube links.
</ParamField>

<ParamField body="output_language" type="string" required={true}>
  Target translation language. Supports 70+ languages and 175+ dialects, with natural voice cloning and lip-sync adjustment.

  Optional values: `English`, `English (Australia)`, `English (India)`, `English (UK)`, `English (US)`, `Spanish`, `Spanish (Mexico)`, `Spanish (Spain)`, `French`, `French (Canada)`, `French (France)`, `Hindi`, `Italian`, `German`, `Polish`, `Portuguese`, `Portuguese (Brazil)`, `Portuguese (Portugal)`, `Chinese`, `Chinese (Cantonese, Traditional)`, `Chinese (Mandarin, Simplified)`, `Chinese (Mandarin, Traditional)`, `Japanese`, `Dutch`, `Turkish`, `Korean`, `Danish`, `Arabic`, `Romanian`, `Mandarin`, `Filipino`, `Swedish`, `Indonesian`, `Ukrainian`, `Greek`, `Czech`, `Bulgarian`, `Malay`, `Slovak`, `Croatian`, `Tamil`, `Finnish`, `Russian`
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={false}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>

<ResponseField name="provider_request_id" type="string" required={false}>
  Provider request ID
</ResponseField>


Built with [Mintlify](https://mintlify.com).