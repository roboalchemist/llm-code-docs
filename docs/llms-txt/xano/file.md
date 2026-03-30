# Source: https://docs.xano.com/xano-features/metadata-api/file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# File

The Metadata API allows you to interact with the files of a given workspace. You can upload, get, delete, and bulk delete files.

<Frame>
  <iframe width="1000" height="500" src="https://www.youtube.com/embed/JeKnXnGTRJU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />
</Frame>

### Upload

Upload a file to a workspace.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/7019f812-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=c9f4e8d66978c3f04ce6c1f14ae40211" width="1314" height="669" data-path="images/7019f812-image.jpeg" />
</Frame>

* workspace\_id - required to determine which workspace the file should live.

* content - the file that is being uploaded.

* type - optionally enforce a file type: image, video, or audio. An attachment is the default selection.

Example Response Body:

```json  theme={null}
{
  "created_at": "2023-04-21T18:05:57.000000Z",
  "id": 16,
  "name": "Pizza.jpg",
  "size": 3724142,
  "type": "image",
  "mime": "image/jpeg",
  "path": "/vault/-TJh6gvN/GgwIFTsoTTIxlacoz01j1xwGY3w/U0y4tw../Pizza.jpg"
}
```

#### Upload a File then Add it as Content to a Table

Taking part of the response body from the previous example, we can add the file to a database table.

```json  theme={null}
// required metadata object from the previous example (created_at and id not needed):

{
  "name": "Pizza.jpg",
  "size": 3724142,
  "type": "image",
  "mime": "image/jpeg",
  "path": "/vault/-TJh6gvN/GgwIFTsoTTIxlacoz01j1xwGY3w/U0y4tw../Pizza.jpg"
}
```

We can take the metadata object and use it for creating content of an image field.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/230b0dbf-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=e904d05fbc09398c23d32bfadd7612e9" width="1306" height="791" data-path="images/230b0dbf-image.jpeg" />
</Frame>

In this example, we take part of the object from the Upload File endpoint and use it to create content that includes an image field.


Built with [Mintlify](https://mintlify.com).