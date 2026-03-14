# Source: https://novita.ai/docs/api-reference/model-apis-fish-audio-voice-cloning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Fish Audio Voice Cloning

Fish Audio API for creating a voice model (voice cloning).

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="type" type="enum<string>" required={true}>
  Model type, tts is for text to speech.

  Available options: `tts`

  Allowed value: `"tts"`
</ParamField>

<ParamField body="title" type="string" required={true}>
  Model title or name.
</ParamField>

<ParamField body="train_mode" type="enum<string>" required={true}>
  Model train mode, for TTS model, fast means model instantly available after creation.

  Available options: `fast`

  Allowed value: `"fast"`
</ParamField>

<ParamField body="voices" type="file[]" required={true}>
  Upload voices files that will be used to tune the model.
</ParamField>

<ParamField body="visibility" type="enum<string>" default="public">
  Model visibility, public will be shown in the discovery page, unlist allows anyone with the link to access, private only be visible to the creator.

  Available options: `public`, `unlist`, `private`
</ParamField>

<ParamField body="description" type="string | null">
  Model description.
</ParamField>

<ParamField body="cover_image" type="file | null">
  Model cover image, this is required if the model is public.
</ParamField>

<ParamField body="texts" type="string[]">
  Texts corresponding to the voices, if unspecified, ASR will be performed on the voices.
</ParamField>

<ParamField body="tags" type="string[]">
  Model tags.
</ParamField>

<ParamField body="enhance_audio_quality" type="boolean" default={false}>
  Enhance audio quality.
</ParamField>

## Response

<ResponseField name="_id" type="string" required={true}>
  Unique identifier for the created model.
</ResponseField>

<ResponseField name="type" type="enum<string>" required={true}>
  Model type.

  Available options: `svc`, `tts`
</ResponseField>

<ResponseField name="title" type="string" required={true}>
  Model title or name.
</ResponseField>

<ResponseField name="description" type="string" required={true}>
  Model description.
</ResponseField>

<ResponseField name="cover_image" type="string" required={true}>
  URL of the model cover image.
</ResponseField>

<ResponseField name="state" type="enum<string>" required={true}>
  Current state of the model.

  Available options: `created`, `training`, `trained`, `failed`
</ResponseField>

<ResponseField name="tags" type="string[]" required={true}>
  Model tags.
</ResponseField>

<ResponseField name="created_at" type="string<date-time>" required={true}>
  Timestamp when the model was created.
</ResponseField>

<ResponseField name="updated_at" type="string<date-time>" required={true}>
  Timestamp when the model was last updated.
</ResponseField>

<ResponseField name="visibility" type="enum<string>" required={true}>
  Model visibility setting.

  Available options: `public`, `unlist`, `private`
</ResponseField>

<ResponseField name="like_count" type="integer" required={true}>
  Number of likes the model has received.
</ResponseField>

<ResponseField name="mark_count" type="integer" required={true}>
  Number of marks/bookmarks the model has received.
</ResponseField>

<ResponseField name="shared_count" type="integer" required={true}>
  Number of times the model has been shared.
</ResponseField>

<ResponseField name="task_count" type="integer" required={true}>
  Number of tasks associated with the model.
</ResponseField>

<ResponseField name="author" type="AuthorEntity · object" required={true}>
  Information about the model author.

  <Expandable title="properties">
    <ResponseField name="_id" type="string" required={true}>
      Author's unique identifier.
    </ResponseField>

    <ResponseField name="nickname" type="string" required={true}>
      Author's nickname.
    </ResponseField>

    <ResponseField name="avatar" type="string" required={true}>
      URL of the author's avatar image.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="train_mode" type="enum<string>" default="full">
  Training mode used for the model.

  Available options: `fast`, `full`
</ResponseField>

<ResponseField name="samples" type="SampleEntity · object[]">
  Sample data associated with the model.

  <Expandable title="properties">
    <ResponseField name="title" type="string" required={true}>
      Sample title.
    </ResponseField>

    <ResponseField name="text" type="string" required={true}>
      Text content of the sample.
    </ResponseField>

    <ResponseField name="task_id" type="string" required={true}>
      Task identifier for the sample.
    </ResponseField>

    <ResponseField name="audio" type="string" required={true}>
      URL of the sample audio file.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="languages" type="string[]">
  Languages supported by the model.
</ResponseField>

<ResponseField name="lock_visibility" type="boolean" default={false}>
  Whether the visibility setting is locked.
</ResponseField>

<ResponseField name="unliked" type="boolean" default={false}>
  Whether the current user has unliked the model.
</ResponseField>

<ResponseField name="liked" type="boolean" default={false}>
  Whether the current user has liked the model.
</ResponseField>

<ResponseField name="marked" type="boolean" default={false}>
  Whether the current user has marked/bookmarked the model.
</ResponseField>


Built with [Mintlify](https://mintlify.com).