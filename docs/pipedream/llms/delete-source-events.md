# Source: https://pipedream.com/docs/rest-api/api-reference/events/delete-source-events.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete source events

### Delete source events

Deletes all events, or a specific set of events, tied to a source.

By default, making a `DELETE` request to this endpoint deletes **all** events associated with a source. To delete a specific event, or a range of events, you can use the `start_id` and `end_id` parameters.

These IDs can be retrieved by using the [`GET /sources/{id}/event_summaries` endpoint](/rest-api/#get-source-events), and are tied to the timestamp at which the event was emitted — e.g. `1589486981597-0`. They are therefore naturally ordered by time.

#### Endpoint

```
DELETE /sources/{id}/events
```

#### Parameters

<ParamField body="start_id" type="string">
  The event ID from which you’d like to start deleting events.

  If `start_id` is passed without `end_id`, the request will delete all events starting with and including this event ID. For example, if your source has 3 events:

* `1589486981597-0`
* `1589486981598-0`
* `1589486981599-0`

  and you issue a `DELETE` request like so:

  ```bash  theme={null}
  curl -X DELETE \
    -H "Authorization: Bearer <api key>" \
    "https://api.pipedream.com/v1/sources/dc_abc123/events?start_id=1589486981598-0"
  ```

  The request will delete the **last two events**.
</ParamField>

***

<ParamField body="end_id" type="string">
  The event ID from which you’d like to end the range of deletion.

  If `end_id` is passed without `start_id`, the request will delete all events up to and including this event ID. For example, if your source has 3 events:

* `1589486981597-0`
* `1589486981598-0`
* `1589486981599-0`

  and you issue a `DELETE` request like so:

  ```bash  theme={null}
  curl -X DELETE \
    -H "Authorization: Bearer <api key>" \
    "https://api.pipedream.com/v1/sources/dc_abc123/events?end_id=1589486981598-0"
  ```

  The request will delete the **first two events**.
</ParamField>

<RequestExample>
  ```bash  theme={null}
  # You can delete a single event by passing its event ID in both the value of the `start_id` and `end_id` params:

  curl -X DELETE \
    -H "Authorization: Bearer <api key>" \
    "https://api.pipedream.com/v1/sources/dc_abc123/events?start_id=1589486981598-0&end_id=1589486981598-0"

  ```
</RequestExample>

<ResponseExample>
  ```

  Deletion happens asynchronously, so you’ll receive a `202 Accepted` HTTP status code in response to any deletion requests.

  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).
