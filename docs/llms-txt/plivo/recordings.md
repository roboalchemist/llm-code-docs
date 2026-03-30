# Source: https://plivo.com/docs/voice/api/recordings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Recordings

> Retrieve, list, and manage call recordings

The Recording API lets you retrieve and manage recordings created during voice calls or conferences. Recordings can be created using the [Record a Call](/voice/api/calls#record-a-call) API or the [Record XML element](/voice/xml/record/).

## The Recording Object

<ParamField body="recording_id" type="string">
  Unique identifier for the recording.
</ParamField>

<ParamField body="call_uuid" type="string">
  Identifier of the call that was recorded.
</ParamField>

<ParamField body="conference_name" type="string">
  Name of the conference that was recorded. `null` for regular calls.
</ParamField>

<ParamField body="recording_url" type="string">
  URL where the recording file can be accessed.
</ParamField>

<ParamField body="recording_format" type="string">
  File format. Values: `wav`, `mp3`.
</ParamField>

<ParamField body="recording_type" type="string">
  Type of recording. Values: `conference`, `normal`.
</ParamField>

<ParamField body="recording_duration_ms" type="string">
  Duration of the recording in milliseconds.
</ParamField>

<ParamField body="rounded_recording_duration" type="integer">
  Duration rounded to nearest 60-second interval. Recordings under 60s are rounded up.
</ParamField>

<ParamField body="recording_storage_duration" type="integer">
  Time in days the recording has been stored. Increments after 24 hours from add time.
</ParamField>

<ParamField body="recording_storage_rate" type="string">
  Unit cost of storing the recording per month.
</ParamField>

<ParamField body="monthly_recording_storage_amount" type="string">
  Monthly storage cost in the latest billing cycle.
</ParamField>

<ParamField body="add_time" type="string">
  Datetime when the recording was created.
</ParamField>

### Example Recording Object

```json  theme={null}
{
  "add_time": "2020-08-05 16:15:15.852059+05:30",
  "api_id": "7abf0744-1ca0-11e4-a2d1-22000ac5040c",
  "call_uuid": "c2c128e2-1c8c-11e4-9bff-1db8a9db0432",
  "conference_name": "noname",
  "recording_duration_ms": "345100.00000",
  "recording_end_ms": "1407235509007.00000",
  "recording_format": "mp3",
  "recording_id": "c2186400-1c8c-11e4-a664-0026b945b52x",
  "recording_start_ms": "1407235163907.00000",
  "recording_type": "conference",
  "recording_url": "http://s3.amazonaws.com/recordings_2013/c2186400-1c8c-11e4-a664-0026b945b52x.mp3",
  "resource_uri": "/v1/Account/MA2025RK4E639VJFZAGV/Recording/c2186400-1c8c-11e4-a664-0026b945b52x/",
  "recording_storage_duration": "723",
  "rounded_recording_duration": "3456",
  "recording_storage_rate": "0.0004",
  "monthly_recording_storage_amount": "0.02304"
}
```

***

## Recording Authentication

By default, recording URLs are publicly accessible. You can enable HTTP Basic Auth to restrict access to your recording media.

**To enable:**

1. Go to [Voice Settings](https://cx.plivo.com/voice-settings) in the Plivo console
2. Enable **HTTP Auth on recordings**

When enabled, all GET requests for recording media require HTTP Basic Auth:

* **Username:** Your Auth ID
* **Password:** Your Auth Token

For recordings created via a subaccount, use the subaccount's Auth ID and Auth Token.

***

## Retrieve a Recording

Get details of a specific recording by its ID.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Recording/{recording_id}/
```

### Arguments

No arguments required.

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Recording/{recording_id}/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>','<auth_token>')
  response = client.recordings.get(recording_id='1ca34b00-3c5c-11e7-b213-06bcf6c57c65')
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new("<auth_id>","<auth_token>")
  response = api.recordings.get('c2186400-1c8c-1124-a664-0026b945b522')
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client("<auth_id>","<auth_token>");
  client.recordings.get("c2186400-1c8c-1124-a664-0026b945b522")
      .then(console.log);
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient("<auth_id>","<auth_token>");
  $response = $client->recordings->get('c2186400-1c8c-1124-a664-0026b945b522');
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.recording.Recording;

  Plivo.init("<auth_id>","<auth_token>");
  Recording response = Recording.getter("c2186400-1c8c-1124-a664-0026b945b522").get();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>","<auth_token>");
  var response = api.Recording.Get(recordingId: "3ebae784-54fd-11e7-975a-024cb8ab2db9");
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      response, _ := client.Recordings.Get("c2186400-1c8c-1124-a664-0026b945b522")
  }
  ```
</CodeGroup>

#### Response

```json  theme={null}
{
  "add_time": "2020-08-05 16:15:15.852059+05:30",
  "api_id": "7abf0744-1ca0-11e4-a2d1-22000ac5040c",
  "call_uuid": "c2c128e2-1c8c-11e4-9bff-1db8a9db0432",
  "conference_name": "noname",
  "recording_duration_ms": "345100.00000",
  "recording_end_ms": "1407235509007.00000",
  "recording_format": "mp3",
  "recording_id": "c2186400-1c8c-11e4-a664-0026b945b52x",
  "recording_start_ms": "1407235163907.00000",
  "recording_type": "conference",
  "recording_url": "http://s3.amazonaws.com/recordings_2013/c2186400-1c8c-11e4-a664-0026b945b52x.mp3",
  "resource_uri": "/v1/Account/MA2025RK4E639VJFZAGV/Recording/c2186400-1c8c-11e4-a664-0026b945b52x/"
}
```

***

## List All Recordings

Retrieve all recordings in your account with optional filters.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Recording/
```

### Arguments

| Parameter                    | Description                                                                                                                                    |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `from_number`                | Filter by source phone number (E.164 format) or SIP endpoint.                                                                                  |
| `to_number`                  | Filter by destination phone number (E.164 format) or SIP endpoint.                                                                             |
| `subaccount`                 | Filter by subaccount `auth_id`.                                                                                                                |
| `call_uuid`                  | Filter by specific call UUID.                                                                                                                  |
| `add_time`                   | Filter by creation time. Format: `YYYY-MM-DD HH:MM[:ss[.uuuuuu]]`. Supports: `add_time__gt`, `add_time__gte`, `add_time__lt`, `add_time__lte`. |
| `mpc_name`                   | Filter by multiparty call name.                                                                                                                |
| `mpc_uuid`                   | Filter by multiparty call UUID.                                                                                                                |
| `conference_name`            | Filter by conference name.                                                                                                                     |
| `conference_uuid`            | Filter by conference UUID.                                                                                                                     |
| `recording_storage_duration` | Filter by storage duration in days. Supports: `__gt`, `__gte`, `__lt`, `__lte`. Cannot be used with `add_time`.                                |
| `limit`                      | Number of results per page. Max: 20.                                                                                                           |
| `offset`                     | Number of records to skip for pagination.                                                                                                      |

<Note>
  * If no time filter is used, Plivo defaults to a 7-day search window.
  * `add_time` allows searching within a 30-day window. Exceeding 30 days returns a 400 error.
  * All timestamps must be in UTC.
</Note>

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Recording/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>','<auth_token>')
  response = client.recordings.list(offset=0, limit=5)
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new("<auth_id>","<auth_token>")
  response = api.recordings.list(limit: 5, offset: 0)
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client("<auth_id>","<auth_token>");
  client.recordings.list({ offset: 0, limit: 5 }).then(console.log);
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient("<auth_id>","<auth_token>");
  $response = $client->recordings->list(['limit' => 2, 'offset' => 2]);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.recording.Recording;

  Plivo.init("<auth_id>","<auth_token>");
  ListResponse<Recording> response = Recording.lister().offset(0).limit(5).list();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>","<auth_token>");
  var response = api.Recording.List(limit: 5, offset: 0);
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      response, _ := client.Recordings.List(plivo.RecordingListParams{Offset: 0, Limit: 5})
  }
  ```
</CodeGroup>

#### Response

```json  theme={null}
{
  "api_id": "ff25223a-1c9f-11e4-80aa-12313f048015",
  "meta": {
    "limit": 3,
    "next": "/v1/Account/MA2025RK4E639VJFZAGV/Recording/?limit=3&offset=3",
    "offset": 0,
    "previous": null,
    "total_count": 948
  },
  "objects": [
    {
      "add_time": "2022-08-05 16:15:15.852059+05:30",
      "call_uuid": "c2c128e2-1c8c-11e4-9bff-1db8a9db0432",
      "conference_name": "noname",
      "recording_duration_ms": "345100.00000",
      "recording_format": "mp3",
      "recording_id": "c2186400-1c8c-1124-a664-0026b945b522",
      "recording_type": "conference",
      "recording_url": "http://s3.amazonaws.com/recordings_2013/c2186400-1c8c-1124-a664-0026b945b522.mp3"
    }
  ]
}
```

***

## Delete a Recording

Permanently delete a recording from your account.

```
DELETE https://api.plivo.com/v1/Account/{auth_id}/Recording/{recording_id}/
```

### Arguments

No arguments required.

### Returns

Returns `204 No Content` on success. Returns `404 Not Found` if the recording doesn't exist.

<CodeGroup>
  ```bash cURL theme={null}
  curl -X DELETE --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Recording/{recording_id}/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>','<auth_token>')
  response = client.recordings.delete(recording_id='9684e812-4b88-11e7-b285-02fb5b2555e7')
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new("<auth_id>","<auth_token>")
  response = api.recordings.delete('c2186400-1c8c-1124-a664-0026b945b522')
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient("<auth_id>","<auth_token>");
  $response = $client->recordings->delete('c2186400-1c8c-1124-a664-0026b945b522');
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.recording.Recording;

  Plivo.init("<auth_id>","<auth_token>");
  Recording.deleter("c2186400-1c8c-1124-a664-0026b945b522").delete();
  System.out.println("Deleted successfully.");
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>","<auth_token>");
  var response = api.Recording.Delete(recordingId: "3ebae784-54fd-11e7-975a-024cb8ab2db9");
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      client.Recordings.Delete("c2186400-1c8c-1124-a664-0026b945b522")
  }
  ```
</CodeGroup>

#### Response

```
HTTP Status Code: 204
```

***

## Get Recordings by Call UUID

To find all recordings for a specific call, use the `call_uuid` filter:

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      "https://api.plivo.com/v1/Account/{auth_id}/Recording/?call_uuid=c2c128e2-1c8c-11e4-9bff-1db8a9db0432"
  ```

  ```python Python theme={null}
  recordings = client.recordings.list(call_uuid='c2c128e2-1c8c-11e4-9bff-1db8a9db0432')
  for recording in recordings:
      print(f"Recording URL: {recording.recording_url}")
  ```
</CodeGroup>

***

## Recording Pricing

| Component                   | Rate                  |
| --------------------------- | --------------------- |
| **Recording generation**    | Free                  |
| **Storage (first 90 days)** | Free                  |
| **Storage (after 90 days)** | \$0.0004/minute/month |

The `recording_storage_rate` and `monthly_recording_storage_amount` fields in the recording object show current storage costs for recordings stored beyond 90 days.

See [Voice Pricing](https://www.plivo.com/pricing/voice/) for complete pricing details.

***

## Related

* [Record a Call](/voice/api/calls#record-a-call) - Start/stop recording during an active call
* [Record XML Element](/voice/xml/record/) - Record using XML
* [Conference Recording](/voice/api/conferences#record-a-conference) - Record conference calls
