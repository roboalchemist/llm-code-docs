# Source: https://docs.fireflies.ai/schema/audio-upload-status.md

# AudioUploadStatus

> Schema for AudioUploadStatus

<ResponseField name="success" type="Boolean">
  Indicates whether the AudioUpload request was a success or not.
</ResponseField>

<ResponseField name="title" type="String">
  Title of the uploaded file.
</ResponseField>

<ResponseField name="message" type="String">
  Message from AudioUpload request.
</ResponseField>

## Additional Resources

<CardGroup cols={2}>
  <Card title="Transcript" icon="link" href="/schema/transcript">
    Schema for Transcript
  </Card>

  <Card title="Upload Audio" icon="link" href="/graphql-api/mutation/upload-audio">
    Use the API to upload audio to Fireflies.ai
  </Card>
</CardGroup>
