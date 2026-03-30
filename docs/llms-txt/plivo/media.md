# Source: https://plivo.com/docs/messaging/api/media.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Media

> Upload, retrieve, and manage media files for MMS messaging

Use the Media API to upload and manage media files for MMS messages. Plivo supports images, videos, and other media types.

## The Media Object

### Attributes

<ParamField body="media_id" type="string">
  A unique identifier for the media file.
</ParamField>

<ParamField body="file_name" type="string">
  The name of the uploaded file.
</ParamField>

<ParamField body="content_type" type="string">
  The MIME type of the media. Valid types: JPG, PNG, MP4, GIF, PDF, text.
</ParamField>

<ParamField body="media_url" type="string">
  The URL of the media file on Plivo's system.
</ParamField>

<ParamField body="media_size" type="integer">
  Size of the media in bytes. Maximum: 2MB per file.
</ParamField>

<ParamField body="upload_time" type="string">
  Timestamp when the media was uploaded.
</ParamField>

<Note>
  Unused media (not sent in an MMS) is automatically deleted after 6 hours. Media sent in MMS messages is retained for 1 year.
</Note>

### Example Media Object

```json  theme={null}
{
  "content_type": "image/jpeg",
  "file_name": "sample.jpg",
  "media_id": "801c2056-33ab-499c-80ef-58b574a462a2",
  "size": 85277,
  "upload_time": "2021-02-17T07:16:09.153289Z",
  "media_url": "https://media.plivo.com/Account/{auth_id}/Media/{media_id}"
}
```

***

## Upload Media

Upload media files to be used in MMS messages. Supports up to 10 attachments per request, with a maximum of 2MB per file.

```
POST https://api.plivo.com/v1/Account/{auth_id}/Media/
```

### Headers

Set `Content-Type` to `multipart/form-data`.

### Arguments

<ParamField body="file" type="file" required>
  One or more files to upload (max 10 files per request).
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.media.upload([
      '/path/to/image1.jpg',
      '/path/to/image2.png'
  ])
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.media.upload(['/tmp/image1.jpg', '/tmp/image2.png'])
      .then(console.log);
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = api.media.upload(['file1.jpg', 'file2.png'])
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->media->upload(['/path/to/image.jpg']);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.media.Media;

  public class UploadMedia {
      public static void main(String[] args) {
          Plivo.init("<auth_id>", "<auth_token>");

          MediaResponse response = Media.creator(
              new String[]{"file1.jpg", "file2.png"}
          ).create();
          System.out.println(response);
      }
  }
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  string[] files = { "file1.jpg", "file2.png" };
  var response = api.Media.Upload(files);
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})

      response, _ := client.Media.Upload(plivo.MediaUpload{
          UploadFiles: []plivo.Files{
              {FilePath: "image.jpg", ContentType: "image/jpeg"},
          },
      })
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: multipart/form-data" \
      --form 'file=@/path/to/image.jpg' \
      https://api.plivo.com/v1/Account/{auth_id}/Media/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "objects": [
    {
      "content_type": "image/jpeg",
      "file_name": "image1.jpg",
      "media_id": "801c2056-33ab-499c-80ef-58b574a462a2",
      "size": 85277,
      "status": "success",
      "status_code": 201,
      "upload_time": "2021-02-17T07:16:09.153289Z",
      "media_url": "https://media.plivo.com/Account/{auth_id}/Media/{media_id}"
    }
  ]
}
```

***

## Retrieve Media

Get details of a specific media file by its ID.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Media/{media_id}/
```

### Arguments

<ParamField path="media_id" type="string" required>
  The unique identifier of the media to retrieve.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.media.get('media_id')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');
  client.media.get('media_id').then(console.log);
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Media/{media_id}/
  ```
</CodeGroup>

***

## List All Media

Retrieve a paginated list of all uploaded media files.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Media/
```

### Arguments

<ParamField query="limit" type="integer">
  Number of results per page. Default: 20, Max: 20.
</ParamField>

<ParamField query="offset" type="integer">
  Number of records to skip. Default: 0.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.media.list(limit=10, offset=0)
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');
  client.media.list({ limit: 10, offset: 0 }).then(console.log);
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      "https://api.plivo.com/v1/Account/{auth_id}/Media/?limit=10"
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "meta": {
    "limit": 20,
    "next": null,
    "offset": 0,
    "previous": null,
    "total_count": 2
  },
  "objects": [
    {
      "content_type": "image/jpeg",
      "file_name": "image1.jpg",
      "media_id": "801c2056-33ab-499c-80ef-58b574a462a2",
      "size": 85277,
      "upload_time": "2021-02-17T07:16:09.153289Z",
      "media_url": "https://media.plivo.com/Account/{auth_id}/Media/{media_id}"
    }
  ]
}
```
