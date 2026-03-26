# Source: https://www.cosmicjs.com/docs/api/media.md

# Media

Learn about media; the images, files, and documents stored in your Cosmic Bucket.

## The media model

The media model contains all the information about your media.

### Properties

Unique identifier for the media.

Unique name of the uploaded file, used in media Metafield value. (See
[updating Object metadata](/docs/api/objects#update-object-metadata))

Media CDN URL.

imgix URL (used for image processing and optimizations). See
[using imgix](#using-imgix).

Media folder.

Alt text. Available for images only.

Image width in pixels. Available for images only.

Image height in pixels. Available for images only.

User-added JSON metadata.

Original file name.

File size in bytes.

File type.

Bucket id.

Date created.
```json
{
  "id": "641c6b898bb999b71f8a0dde",
  "name": "7f9403a32f29-toucan.jpg",
  "original_name": "toucan.jpg",
  "size": 32466,
  "type": "image/png",
  "bucket": "63dc24a4d71e244b63c88fca",
  "created_at": "2024-03-23T15:08:57.913Z",
  "folder": "wildlife",
  "alt_text": "A picture of a Toucan.",
  "width": 1200,
  "height": 600,
  "url": "https://cdn.cosmicjs.com/7f9403a32f29-toucan.jpg",
  "imgix_url": "https://imgix.cosmicjs.com/7f9403a32f29-toucan.jpg"
}

```
---

## Get media list 

This endpoint enables you to retrieve a list of your media. By default, a maximum of 1000 media items are shown per page.

### Optional parameters

A JSON object to perform media search and filtering. See [queries section](/docs/api/queries) for more detail. Must be URL encoded for REST requests.

### Optional methods

Declare which properties to return in comma-separated string (or array if using the NPM module). Remove to see all media properties. Can include nested metadata. Example: `id,title,metadata.author.metadata.image.url`.

Order of media returned.
Options `created_at, -created_at, modified_at, -modified_at, random`
Use `-` for descending order.

Limit the number of media returned.
Default `1000`

Used for pagination. The number of media to skip.
Default `0`

Set to `false` for real-time updates. Increases latency of endpoint.
Default `true`

Set to `true` for reader-friendly formated JSON response.
Default `false`
```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY'
})

await cosmic.media.find({
  folder: "product-images", // Get media in folder
})
.props('url')
.limit(2)

```
```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/media \
    -d read_key=${BUCKET_READ_KEY} \
    --data-urlencode query='{"folder":"product-images"}' \
    -d props=url \
    -d limit=2 \
    -G
```

```json {{ title: 'Response' }}
{
  "media": [
    {
      "url": "https://cdn.cosmicjs.com/9c4d6b70-49e5-11eb...",
    },
    {
      "url": "https://cdn.cosmicjs.com/9c4d6b70-49e5-11eb...",
    }
  ],
  "total": 10,
  "limit": 2
}
```
---

---

## Get a single media 

This endpoint enables you to get a single media.

With the Cosmic NPM module, you can use the `findOne` method to return an `object` type instead of `array`. If using the REST API, it will return an `array`.

### Optional parameters

Use any of the properties on the media model. A common one would be the file name.

A JSON object to perform Object search and filtering. See [queries section](/docs/api/queries) for more detail. Must be URL encoded for REST requests.

### Optional methods

Declare which properties to return in comma-separated string (or array if using the NPM module). Remove to see all media properties. Can include nested metadata. Example: `id,title,metadata.author.metadata.image.url`.

Order of media returned.
Options `created_at, -created_at, modified_at, -modified_at, random`
Use `-` for descending order.

Used for pagination. The number of media to skip.
Default `0`

Set to `false` for real-time updates. Increases latency of endpoint.
Default `true`

Set to `true` for reader-friendly formated JSON response.
Default `false`

```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY'
})

await cosmic.media.findOne({
  name: 'asdf-1234-toucan.png'
}).props([
  'name',
  'imgix_url',
  'alt_text',
  'metadata'
])
```
```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/media \
    -d read_key=${BUCKET_READ_KEY} \
    --data-urlencode query='{"name":"7f9403a32f29-toucan.jpg"}' \
    -d props=name,imgix_url,alt_text,metadata \
    -G
```

```json {{ title: 'Response' }}
{
  "media": {
    "name": "7f9403a32f29-toucan.jpg",
    "imgix_url": "https://imgix.cosmicjs.com/7f9403a32f29-toucan.jpg",
    "alt_text": "Picture of a Toucan.",
    "metadata": {
      "caption": "Toucan in the wild.",
      "credit": "Bird Watchers of America"
    }
  }
}
```
---

## Create media 

This endpoint enables you to upload media to your Bucket.

### Base URL

Use the following endpoint to create media in your Cosmic Bucket.

```
https://workers.cosmicjs.com
```
### Upload limits

The size limit for uploads to the upload URL is `900MB`.

### Required parameters

Media object.

### Media object

The Media Object must be an object with certain properties indicated below.

If using [Multer NPM module](https://www.npmjs.com/package/multer), the popular Node.js package for handling `multipart/form-data`, the file object will have these by default. Otherwise, you should create an object with these properties:

The name of your file (For example: something.jpg)

The File Buffer.

### Optional parameters

Media folder.

Alt text (available for images only).

User-added JSON metadata.

Triggers corresponding media action webhook (See Webhooks).

```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY',
  writeKey: 'BUCKET_WRITE_KEY'
})

// Using Multer:
const media = req.files[0]
// or not using Multer:
// const media = { originalname: filename, buffer: filedata }

const data = await cosmic.media.insertOne({
  media: media,
  folder: "album-covers",
  metadata: {
    caption: "None more black",
    credit: "Nigel Tufnel",
  }
})
```
```bash {{ title: 'cURL' }}
curl https://workers.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/media \
  --form 'media=@none-more-black.png' \
  --form 'folder=album-covers' \
  --form 'metadata={"caption":"None more black","credit":"Nigel Tufnel"}' \
  -H 'Authorization: Bearer {BUCKET_WRITE_KEY}'
```

```json {{ title: 'Response' }}
{
  "media": {
    "id": "602fd622853cca45f4c9fd96",
    "name": "c20391e0-b8a4-11e6-8836-fbdfd6956b31-test.png",
    "original_name": "none-more-black.png",
    "size": 457307,
    "folder": "album-covers",
    "type": "image/png",
    "bucket": "5839c67f0d3201c114000004",
    "created_at": "2016-12-02T15:34:05.054Z",
    "url": "https://cdn.cosmicjs.com/asdf-1234-none-more-black.png",
    "imgix_url": "https://imgix.cosmicjs.com/asdf-1234-none-more-black.png",
    "metadata": {
      "caption": "None more black",
      "credit": "Nigel Tufnel"
    }
  }
}
```
## Upload example

### React Dropzone and React Server Actions

Go to the [Cosmic Next File Upload](https://github.com/cosmicjs/cosmic-next-file-upload) example code to see how to use [React Dropzone](https://react-dropzone.js.org/) and React Server Actions to upload your media without exposing your Cosmic API keys to the client.

---

## Update media 

This endpoint enables you to update media data.

### Required parameters

Media id.

### Optional parameters

Media folder.

Alt text (available for images only).

User-added JSON metadata.

Triggers corresponding media action webhook (See Webhooks).

```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY',
  writeKey: 'BUCKET_WRITE_KEY'
})

await cosmic.media.updateOne('media-id', {
  folder: "national-parks",
  alt_text: "Picture of Grand Teton National Park".
})
```
```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/media/:id \
  -d '{"folder":"national-parks","alt_text":"Picture of Grand Teton National Park"}' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer {BUCKET_WRITE_KEY}" \
  -X PATCH
```

```json {{ title: 'Response' }}
{
  "media": {
    "id": "602fd622853cca45f4c9fd96",
    "name": "c20391e0-grand-tetons.png",
    "original_name": "grand-tetons.png",
    "size": 457307,
    "folder": "national-parks",
    "type": "image/png",
    "bucket": "5839c67f0d3201c114000004",
    "created_at": "2016-12-02T15:34:05.054Z",
    "url": "https://cdn.cosmicjs.com/c20391e0-grand-tetons.png",
    "imgix_url": "https://imgix.cosmicjs.com/c20391e0-grand-tetons.png",
    "alt_text": "Picture of Grand Teton National Park"
  }
}
```
---

## Delete media 

This endpoint enables you to delete media from your Bucket.

### Required parameters

Media id.

### Optional parameters

Triggers corresponding media action webhook (See Webhooks).

```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY',
  writeKey: 'BUCKET_WRITE_KEY'
})

await cosmic.media.deleteOne('media-id')
```
```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/media/:id \
  -H "Authorization: Bearer {BUCKET_WRITE_KEY}" \
  -X DELETE
```

```json {{ title: 'Response' }}
{
  "message": "Media with id ':id' deleted successfully from bucket."
}

```
---

## Using imgix

[imgix](https://imgix.com/) is included with every Cosmic account. You can use the imgix suite of image processing tools on the URL provided by the `imgix_url` property found on Cosmic media and Object API responses.

### Before imgix

The image is full size and not optimized:
![Image](https://imgix.cosmicjs.com/8d508870-9988-11ec-9edf-8d8ed23fd38e-starry.jpg)

https://imgix.cosmicjs.com/8d508870-9988-11ec-9edf-8d8ed23fd38e-starry.jpg

### After imgix

Using imgix, we can create an optimized thumbnail by adding `?w=100&auto=format,compress` to the end of the URL:
![Image](https://imgix.cosmicjs.com/8d508870-9988-11ec-9edf-8d8ed23fd38e-starry.jpg?w=100&auto=format,compress)

https://imgix.cosmicjs.com/8d508870-9988-11ec-9edf-8d8ed23fd38e-starry.jpg?w=100&auto=format,compress

There are lots of image processing capabilities with this library as well as a [React imgix component](https://www.npmjs.com/package/react-imgix) to automate optimizations. Check out the [imgix documentation](https://docs.imgix.com/) for more info.