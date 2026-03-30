# Nivo Documentation

Source: https://docs.nivo.video/llms-full.txt

---

# Create Upload Request
Source: https://docs.nivo.video/api-reference/endpoint/create-upload-request

POST /upload
Creates a new upload request to process a media file from a URL. The file will be processed asynchronously.

Creates a new upload request to process a media file from a URL. The file will be processed asynchronously.


# Introduction
Source: https://docs.nivo.video/api-reference/introduction

Documentation about the Nivo API endpoints

{/* ## Welcome

  There are two ways to build API documentation: [OpenAPI](https://mintlify.com/docs/api-playground/openapi/setup) and [MDX components](https://mintlify.com/docs/api-playground/mdx/configuration). For the starter kit, we are using the following OpenAPI specification.

  <Card
  title="OpenAPI Specification"
  icon="code"
  href="https://github.com/mintlify/starter/blob/main/api-reference/openapi.json"
  >
  View the OpenAPI specification file
  </Card> */}

## Authentication

All API endpoints are authenticated using API keys that must be provided by using the `Authorization` header.

You can get your API key from the Nivo dashboard inside account settings.

```json
"headers": {
  "Authorization": "<your-api-key>"
}
```


# Introduction
Source: https://docs.nivo.video/index

Welcome to the home of your new documentation

Documentation from Nivo HTTP API and Webhooks.

<CardGroup cols={2}>
  <Card title="API Reference" icon="code" href="/api-reference/introduction">
    Documentation for the Nivo HTTP API
  </Card>

  <Card title="Webhooks" icon="webhook" href="/webhooks/introduction">
    Documentation for the Nivo Webhooks
  </Card>
</CardGroup>


# Events
Source: https://docs.nivo.video/webhooks/events

Documentation about the Nivo webhook events

Below you can check the types of events that are available to be used in your webhooks.

## Upload created

This event is triggered when a new upload is created.

<CodeGroup>
  ```typescript Types
  export interface UploadCreatedWebhookEvent {
    trigger: 'upload.created',
    payload: {
      id: string;
      title: string;
      description: string | null;
      duration: number;
      collectionId: string;
      folderId?: string | null;
      externalId?: string | null;
      streamUrl?: string | null;
      tags: string[];
      metadata?: Record<string, string> | null;
    }
  }
  ```

  ```json Example
  {
    "trigger": "upload.created",
    "payload": {
      "id": "23a8e2ba-ca40-4ed0-ab0a-fe0847c1fbf5",
      "title": "Sample video",
      "description": null,
      "duration": 286,
      "collectionId": "81a8d44e-930d-460c-a178-55d571810833",
      "folderId": null,
      "externalId": null,
      "streamUrl": null,
      "tags": ["courses", "tutorials"],
      "metadata": {
        "custom_platform_id": "8B710CBD-47B0-48DA-8CF1-629797572FF8"
      }
    }
  }
  ```

  ```typescript Zod Schema
  import { z } from 'zod'

  export const uploadCreatedSchema = z.object({
    id: z.string().uuid(),
    title: z.string(),
    description: z.string().nullable(),
    duration: z.number(),
    collectionId: z.string().nullish(),
    folderId: z.string().nullish().default(null),
    externalId: z.string().nullable(),
    streamUrl: z.string().url().nullable(),
    tags: z.array(z.string()),
    metadata: z.record(z.string(), z.string()).nullable(),
  })

  export type UploadCreated = z.infer<typeof uploadCreatedSchema>
  ```
</CodeGroup>

## Upload updated

This event is triggered when an upload is updated.

<CodeGroup>
  ```typescript Types
  export interface UploadUpdatedWebhookEvent {
    trigger: 'upload.updated',
    payload: {
      id: string;
      title: string;
      description: string | null;
      duration: number;
      collectionId: string;
      folderId?: string | null;
      externalId?: string | null;
      streamUrl?: string | null;
      tags: string[];
      metadata?: Record<string, string> | null;
    }
  }
  ```

  ```json Example
  {
    "trigger": "upload.updated",
    "payload": {
      "id": "23a8e2ba-ca40-4ed0-ab0a-fe0847c1fbf5",
      "title": "Sample video",
      "description": "This is a sample video",
      "duration": 286,
      "collectionId": "81a8d44e-930d-460c-a178-55d571810833",
      "folderId": "9DDCFF93-C38B-4CE2-BB2D-FBAC50A423EA",
      "externalId": "8B710CBD-47B0-48DA-8CF1-629797572FF8",
      "streamUrl": "https://nivo.video/stream/23a8e2ba-ca40-4ed0-ab0a-fe0847c1fbf5",
      "tags": ["courses", "tutorials", "sample"],
      "metadata": {
        "custom_platform_id": "8B710CBD-47B0-48DA-8CF1-629797572FF8"
      }
    }
  }
  ```

  ```typescript Zod Schema
  import { z } from 'zod'

  export const uploadUpdatedSchema = z.object({
    id: z.string().uuid(),
    title: z.string(),
    description: z.string().nullable(),
    duration: z.number(),
    collectionId: z.string().nullish(),
    folderId: z.string().nullish().default(null),
    externalId: z.string().nullable(),
    streamUrl: z.string().url().nullable(),
    tags: z.array(z.string()),
    metadata: z.record(z.string(), z.string()).nullable(),
  })

  export type UploadCreated = z.infer<typeof uploadCreatedSchema>
  ```
</CodeGroup>

## Upload deleted

This event is triggered when an upload is deleted.

<CodeGroup>
  ```typescript Types
  export interface UploadDeletedWebhookEvent {
    trigger: 'upload.deleted',
    payload: {
      id: string;
      collectionId: string;
      metadata?: Record<string, string> | null;
    }
  }
  ```

  ```json Example
  {
    "trigger": "upload.deleted",
    "payload": {
      "id": "23a8e2ba-ca40-4ed0-ab0a-fe0847c1fbf5",
      "collectionId": "81a8d44e-930d-460c-a178-55d571810833",
      "metadata": {
        "custom_platform_id": "8B710CBD-47B0-48DA-8CF1-629797572FF8"
      }
    }
  }
  ```

  ```typescript Zod Schema
  import { z } from 'zod'

  export const uploadDeletedSchema = z.object({
    id: z.string().uuid(),
    collectionId: z.string().nullish(),
    metadata: z.record(z.string(), z.string()).nullable(),
  })

  export type UploadDeleted = z.infer<typeof uploadDeletedSchema>
  ```
</CodeGroup>

## Upload transcription created

This event is triggered when a transcription is created for an upload.

<CodeGroup>
  ```typescript Types
  export interface UploadTranscriptionCreatedWebhookEvent {
    trigger: 'upload.transcription.created',
    payload: {
      id: string;
      uploadId: string;
      collectionId: string;
      metadata: Record<string, string> | null;
      text: string;
      segments: {
        text: string;
        timestamp: [number, number];
      }[];
      metadata?: Record<string, string> | null;
    }
  }
  ```

  ```json Example
  {
    "trigger": "upload.transcription.created",
    "payload": {
      "id": "23a8e2ba-ca40-4ed0-ab0a-fe0847c1fbf5",
      "uploadId": "23a8e2ba-ca40-4ed0-ab0a-fe0847c1fbf5",
      "collectionId": "81a8d44e-930d-460c-a178-55d571810833",
      "metadata": {
        "custom_platform_id": "8B710CBD-47B0-48DA-8CF1-629797572FF8"
      },
      "text": "These are the first words of the transcription and these are the rest of the words of the transcription",
      "segments": [
        {
          "text": "These are the first words of the transcription",
          "timestamp": [0, 4]
        },
        {
          "text": "and these are the rest of the words of the transcription",
          "timestamp": [4, 10]
        }
      }
    }
  }
  ```

  ```typescript Zod Schema
  import { z } from 'zod'

  export const uploadTranscriptionCreatedSchema = z.object({
    id: z.string().uuid(),
    uploadId: z.string().uuid(),
    collectionId: z.string().nullish(),
    metadata: z.record(z.string(), z.string()).nullable(),
    text: z.string(),
    segments: z.array(
      z.object({
        text: z.string(),
        timestamp: z.tuple([z.number(), z.number()]),
      })
    ),
  })

  export type UploadTranscriptionCreated = z.infer<
    typeof uploadTranscriptionCreatedSchema
  >
  ```
</CodeGroup>

## Tag created

This event is triggered when a new tag is created.

<CodeGroup>
  ```typescript Types
  export interface TagCreatedWebhookEvent {
    trigger: 'tag.created',
    payload: {
      slug: string;
    }
  }
  ```

  ```json Example
  {
    "trigger": "tag.created",
    "payload": {
      "slug": "sample-tag"
    }
  }
  ```

  ```typescript Zod Schema
  import { z } from 'zod'

  export const tagCreatedSchema = z.object({
    slug: z.string(),
  })

  export type TagCreated = z.infer<typeof tagCreatedSchema>
  ```
</CodeGroup>

## Tag deleted

This event is triggered when a tag is deleted.

<CodeGroup>
  ```typescript Types
  export interface TagDeletedWebhookEvent {
    trigger: 'tag.deleted',
    payload: {
      slug: string;
    }
  }
  ```

  ```json Example
  {
    "trigger": "tag.deleted",
    "payload": {
      "slug": "sample-tag"
    }
  }
  ```

  ```typescript Zod Schema
  import { z } from 'zod'

  export const tagDeletedSchema = z.object({
    slug: z.string(),
  })

  export type TagDeleted = z.infer<typeof tagDeletedSchema>
  ```
</CodeGroup>


# Getting started
Source: https://docs.nivo.video/webhooks/intro

Documentation about the Nivo webhooks

## Introduction

Webhooks are used to receive events from Nivo. You can use webhooks to receive events like when a video is uploaded, a transcription is created, etc.

All webhooks are sent using HTTP `POST` requests.

### Example payload

Below you can check an example payload for a `upload.created` webhook event.

```json Example payload
{
  "trigger": "upload.created",
  "payload": {
    "id": "23a8e2ba-ca40-4ed0-ab0a-fe0847c1fbf5",
    "title": "Sample video",
    "description": null,
    "duration": 286,
    "collectionId": "81a8d44e-930d-460c-a178-55d571810833",
    "folderId": null,
    "externalId": null,
    "streamUrl": null,
    "tags": ["courses", "tutorials"],
    "metadata": {
      "custom_platform_id": "8B710CBD-47B0-48DA-8CF1-629797572FF8"
    }
  }
}
```

## Signature verification

All webhooks are signed using a HTTP header called `Nivo-Signature`. This header contains a JWT that is signed using the secret key present in the webhook list inside Nivo dashboard.

```json Example HTTP headers
{
  "Nivo-Signature": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmNDgzZTgzNi1mMzRlLTQ1NjgtYjBhOS0zN2VkOWVlNGNiMjYiLCJleHAiOjE3MzYyNzY3NjIsImlzcyI6Im5pdm8iLCJzdWIiOiJodHRwczovL2JhZC1hbGxpZ2F0b3ItNDQud2ViaG9vay5jb29sIn0.t4Auv7rKjEmN-4oXQb4kuWIV2uN0wo8b0S2-nWb6S0Q"
}
```

## Retries

Webhooks are retried 3 times with an exponential backoff. After 3 retries, the webhook is considered failed and will not be retried again.


