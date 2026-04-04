# Source: https://docs.logrocket.com/docs/session-highlights-api.md

# Galileo Highlights API

## Overview

Use the Highlights API to get a summary of a user’s recent interactions with your application. The API gives your team an immediate understanding of the user's journey, allowing them to provide personalized assistance and address issues efficiently. It can be used to, for example:

* Add summaries of a user's recent behavior to their support ticket, helping to save time understanding and reproducing their issue
* Update your outgoing sales or account management workflows with short summaries of a user's recent experiences that can be reviewed before contacting them
* Send summaries of the actions taken before a low NPS score was given to a Slack channel for added context when reviewing feedback

<Image align="center" caption="Example of Highlights being sent to a ticketing system" src="https://files.readme.io/b7961ff36de6dc8e4a268b43c8818953b1af30cf1236ec1d075c758b13801825-image.png" />

For an overview of Highlights and how to access them, see [here](https://docs.logrocket.com/docs/galileo-highlights). This feature is available for Pro and Enterprise plans. We offer a complimentary trial period followed by a range of pricing options.

Using Zendesk? See our [Zendesk Highlights Integration](https://docs.logrocket.com/docs/zendesk#ai-powered-summaries-from-galileo-highlights).

Using Intercom? See our [Intercom Highlights Integration](https://docs.logrocket.com/docs/intercom#ai-powered-summaries-from-galileo-highlights).

## Request Highlights

`POST - https://api.logrocket.com/v1/orgs/<your_org_id>/apps/<your_project_id>/highlights/`

The values for `your_org_id` and `your_project_id` will come from your App ID, which can be found under **Settings > Project Settings**, or in the URL for your LogRocket dashboard. For example, an App ID of `foo/bar` is composed of an org ID `foo` and a project ID `bar`:

`POST - https://api.logrocket.com/v1/orgs/foo/apps/bar/highlights/`

### Authentication

To make Highlights requests, you'll need your API key. You can find your API key in the LogRocket dashboard under **Settings > Project Settings**. Once you have your API key, provide it in the `Authorization` header when making requests to the Highlights API. For example:

```shell
curl -X POST 'https://api.logrocket.com/v1/orgs/<your_org_id>/apps/<your_project_id>/highlights/' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token <your-api-key>' \
  -d '{"userEmail": "alice@example.com"}'
```

### Example request bodies

#### Request with userEmail

Send the following request body to summarize up to 10 most recent sessions recorded in the last 30 days for the user associated with the email `alice@example.com`. The results must be retrieved using the `id` in the response body.

```json
{
  "userEmail": "alice@example.com"
}
```

#### Request with userID, timeRange, and webhookURL

Send the following request body to summarize up to 10 most recent sessions recorded in the provided time range for the user associated with ID `google-oauth2|abc123`. When ready, the results will be included in the body of a POST request sent to `https://example.com/endpoint`:

```json
{
  "userID": "google-oauth2|abc123",
  "question": "What issue did this user experience?",
  "timeRange": {
    "startMs": 1715481030000,
    "endMs": 1715567430000
  },
  "webhookURL: "https://example.com/endpoint"
}
```

| Field               | Optional or Required                       | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| :------------------ | :----------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `userEmail`         | One of `userEmail` or `userID` is required | The email of a user provided in `LogRocket.identify()` calls                                                                                                                                                                                                                                                                                                                                              |
| `userID`            | One of `userEmail` or `userID` is required | The ID of a user provided in `LogRocket.identify()` calls                                                                                                                                                                                                                                                                                                                                                 |
| `question`          | Optional                                   | A string of what question you want answered about the user(s) experiences. If you leave this blank, Galileo will generate a general summary of the user(s) experiences.                                                                                                                                                                                                                                   |
| `timeRange`         | Optional                                   | An object containing `startMs`and `endMs` timestamps between which sessions for the requested Highlights will be selected. When `timeRange` is provided, up to 10 most recent sessions recorded within that `timeRange` will be summarized (limited by your org's retention period). When `timeRange` is not provided, up to 10 most recent sessions recorded within the last 30 days will be summarized. |
| `timeRange.startMs` | Required when a `timeRange` is provided    | Integer epoch timestamp in milliseconds that defines the beginning of the requested `timeRange`. Must be a value smaller than `endMs`.                                                                                                                                                                                                                                                                    |
| `timeRange.endMs`   | Required when a `timeRange` is provided    | Integer epoch timestamp in milliseconds that defines the end of the requested `timeRange`. Must be a value larger than `startMs`.                                                                                                                                                                                                                                                                         |
| `webhookURL`        | Optional                                   | When ready, Highlights results will be included in the body of a POST request sent to this URL                                                                                                                                                                                                                                                                                                            |

## Receive Highlights Results

Requests sent to the Highlights API will receive an immediate response with an `id` in the body. For example:

```json
{
    "id": "0cc12cad4b5b8b93760edf7fb5731ac66fbc8a766f9431df6c1e72b214ed6a65"
}
```

The `id` is a reference to your request that you can use to retrieve your results when they're ready. Highlights results generally take 1-3 minutes to be generated. If you included a `webhookURL` in your request, no further action is necessary to receive results: when they're ready, they'll be included in the body of a POST request sent to the URL you provided.

If you didn't include a `webhookURL` in your request, make a GET request with the `id` query parameter to check on the status of your results:

```shell
curl -X GET 'https://api.logrocket.com/v1/orgs/<your_org_id>/apps/<your_project_id>/highlights?id=0cc12cad4b5b8b93760edf7fb5731ac66fbc8a766f9431df6c1e72b214ed6a65' \
  -H 'Authorization: token <your-api-key>'
```

If Highlights are still being generated, you'll receive the following in the response body:

```json
{
  "result": null,
  "status": "PENDING",
  "appID": "<your_org_id>/<your_project_id>",
  "requestID": "0cc12cad4b5b8b93760edf7fb5731ac66fbc8a766f9431df6c1e72b214ed6a65"
}
```

If Highlights are ready, you'll receive a response body like:

```json
{
  "result": {
    "highlights": "The user [checks out their cart](https://app.logrocket.com/<your_org_id>/<your_project_id>/s/5-14de95d6-d5b8-1a62-0a3a-4858caf874b0/0?t=1715564734801) and [encounters an error loading settings](https://app.logrocket.com/<your_org_id>/<your_project_id>/s/5-3cde95d6-a5b8-4a62-9b3a-6aa834f8747c/0?t=1715564554783).",
    "sessions": [
      {
        "recordingID": "5-3cde95d6-a5b8-4a62-9b3a-6aa834f8747c",
        "sessionID": 0,
        "highlights": "The user [encounters an error loading settings](https://app.logrocket.com/<your_org_id>/<your_project_id>/s/5-3cde95d6-a5b8-4a62-9b3a-6aa834f8747c/0?t=1715564554783) and [the issue persists](https://app.logrocket.com/<your_org_id>/<your_project_id>/s/5-3cde95d6-a5b8-4a62-9b3a-6aa834f8747c/0?t=1715564734801)."
      },
      {
        "recordingID": "5-14de95d6-d5b8-1a62-0a3a-4858caf874b0",
        "sessionID": 0,
        "highlights": "The user [adds an item to their cart](https://app.logrocket.com/<your_org_id>/<your_project_id>/s/5-14de95d6-d5b8-1a62-0a3a-4858caf874b0/0?t=1715564554783) and [proceeds to checkout](https://app.logrocket.com/<your_org_id>/<your_project_id>/s/5-14de95d6-d5b8-1a62-0a3a-4858caf874b0/0?t=1715564734801)"
      },
      ...
    ]
  },
  "status": "READY",
  "appID": "<your_org_id>/<your_project_id>",
  "requestID": "0cc12cad4b5b8b93760edf7fb5731ac66fbc8a766f9431df6c1e72b214ed6a65"
}
```

`result.highlights` is a summary across all sessions included in the result. Each session included in the result also has its own individual summary at `result.sessions[].highlights`. The `highlights` strings also contain Markdown-formatted links to relevant times in the referenced session(s) that you can follow to learn more about the described events.

Finally, if Highlights fail to generate, you'll receive the following in the response body:

```json
{
  "result": null,
  "status": "FAILED",
  "appID": "<your_org_id>/<your_project_id>",
  "requestID": "0cc12cad4b5b8b93760edf7fb5731ac66fbc8a766f9431df6c1e72b214ed6a65"
}
```

In this case, the original POST request can be made again to retry Highlights generation.

<br />