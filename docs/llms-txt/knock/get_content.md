# Source: https://docs.knock.app/api-reference/messages/batch/get_content.md

# Source: https://docs.knock.app/api-reference/messages/get_content.md

### Get message content

Returns the fully rendered contents of a message, where the response depends on which channel the message was sent through.

#### Endpoint

`GET /v1/messages/{message_id}/content`

**Rate limit tier:** 4

#### Path parameters

- **message_id** (string) *required* - The ID of the message to fetch contents of.

#### Responses

##### 200

OK

###### Example

```json
{
  "__typename": "MessageContent",
  "data": {
    "__typename": "MessageSmsContent",
    "body": "URGENT: Power failure detected in perimeter fencing. Backup generators failed to engage. Technical team dispatched. Maintain lockdown protocols.",
    "to": "+15553982647"
  },
  "inserted_at": "1993-06-11T20:30:00Z",
  "message_id": "2w3YUpTTOxuDvZFji8OMsKrG176"
}
```

