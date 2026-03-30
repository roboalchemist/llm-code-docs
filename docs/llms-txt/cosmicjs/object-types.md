# Source: https://www.cosmicjs.com/docs/api/object-types.md

# Object types

Learn about Object types; used to organize and model Objects in your Cosmic Bucket.

## The Object type model

The Object type model contains all the information about the Object type including content modeling using Metafields, localization, preview links, and more.

### Properties

Unique identifier for Object type.

Object type title.

Singular title of the Object type.

Object type slugs are unique per Bucket.

Single or multiple Objects in this type.

Valid Unicode emoji displayed on the Object type table.

Array of Metafields. See [Metafields](/docs/api/metafields).

Contains boolean property `slug_field` which controls
the display options for the `slug` field for Objects in the
type.

Add localization to the Object type. Default: `false`

Array of available locales in the Object type. See [available locale
codes](#localization).

Default locale when creating new Objects in this type. Objects will be
grouped by this locale in the Object type table in the dashboard.
```json
{
  "id": "63bde47897d49d0008a270b3",
  "title": "Bikes",
  "slug": "bikes",
  "singular": "Bike",
  "emoji": "🏍️",
  "created_at": "2023-01-10T22:19:36.128Z",
  "modified_at": "2023-03-16T21:09:09.914Z",
  "singleton": false,
  "options": {
    "slug_field": true
  },
  "metafields": [
    {
      "id": "c7c50911-3b38-4b22-a307-392eb9f84739",
      "title": "Image",
      "key": "image",
      "type": "file",
      "helptext": "",
      "required": false,
      "media_validation_type": "image"
    },
    {
      "id": "1157a40b-9a1a-4d06-96e0-2338f01d366d",
      "title": "Headline",
      "key": "headline",
      "type": "text",
      "helptext": "",
      "required": false
    }
  ]
}

```
---

## Get Object types 

This endpoint enables you to retrieve a list of your Object types in the Bucket.
```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY'
})

await cosmic.objectTypes.find()

```
```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/object-types \
    -d read_key=${BUCKET_READ_KEY} \
    -G
```

```json {{ title: 'Response' }}
{
  "object_types": [
    {
      "id": "63bde47897d49d0008a270b3",
      "title": "Bikes",
      "slug": "bikes",
      "singular": "Bike",
      "emoji": "🏍️",
      "created_at": "2023-01-10T22:19:36.128Z",
      "modified_at": "2023-03-16T21:09:09.914Z",
      "singleton": false,
      "options": {
        "slug_field": true
      },
      "metafields": [
        {
          "id": "c7c50911-3b38-4b22-a307-392eb9f84739",
          "title": "Image",
          "key": "image",
          "type": "file",
          "helptext": "",
          "required": false,
          "media_validation_type": "image"
        },
        {
          "id": "1157a40b-9a1a-4d06-96e0-2338f01d366d",
          "title": "Headline",
          "key": "headline",
          "type": "text",
          "helptext": "",
          "required": false
        }
       ...
      ]
    },
    {
      "id": "63bde4c297d49d0008a270b4",
      "title": "Cars",
      "slug": "cars",
      "singular": "Car",
      "emoji": "🚗",
      "created_at": "2023-01-10T22:19:36.128Z",
      "modified_at": "2023-03-16T21:09:09.914Z",
      "singleton": false,
      "options": {
        "slug_field": true
      },
      "metafields": [
        {
          "id": "c7c50911-3b38-4b22-a307-392eb9f84739",
          "title": "Image",
          "key": "image",
          "type": "file",
          "helptext": "",
          "required": false,
          "media_validation_type": "image"
        },
        {
          "id": "1157a40b-9a1a-4d06-96e0-2338f01d366d",
          "title": "Headline",
          "key": "headline",
          "type": "text",
          "helptext": "",
          "required": false
        }
       ...
      ]
    }
  ]
}
```
---

## Get a single Object type 

Get a single Object type by `slug`.

### Required parameters

The Object type slug.

```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY'
})

await cosmic.objectTypes.findOne('object-type-slug')
```
```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/object-types/:slug \
    -d read_key=${BUCKET_READ_KEY} \
    -G
```

```json {{ title: 'Response' }}
{
  "object_type": {
    "id": "63bde47897d49d0008a270b3",
    "title": "Bikes",
    "slug": "bikes",
    "singular": "Bike",
    "emoji": "🏍️",
    "created_at": "2023-01-10T22:19:36.128Z",
    "modified_at": "2023-03-16T21:09:09.914Z",
    "singleton": false,
    "options": {
      "slug_field": true
    },
    "metafields": [
      {
        "id": "c7c50911-3b38-4b22-a307-392eb9f84739",
        "title": "Image",
        "key": "image",
        "type": "file",
        "helptext": "",
        "required": false,
        "media_validation_type": "image"
      },
      {
        "id": "1157a40b-9a1a-4d06-96e0-2338f01d366d",
        "title": "Headline",
        "key": "headline",
        "type": "text",
        "helptext": "",
        "required": false
      }
      ...
    ]
  }
}
```
---

## Create an Object type 

This endpoint enables you to create an Object type in your Bucket.

The data request payload will need to be sent in JSON format with the `Content-Type: application/json` header set.

### Required parameters

Object type title.

### Optional parameters

Singular title of the Object type.

Object type slugs are unique per Bucket.
Default: `title` converted to slug.

Single or multiple Objects in this type.

Valid Unicode emoji displayed on the Object type table.

Array of Metafields. See [Metafields](/docs/api/metafields).

Contains boolean property `slug_field` which controls
the display options for the `slug` field for Objects in the
type.

Add localization to the Object type. Default: `false`

Array of available locales in the Object type. See [available locale
codes](#localization).

Default locale when creating new Objects in this type. Objects will be
grouped by this locale in the Object type table in the dashboard.

```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY',
  writeKey: 'BUCKET_WRITE_KEY'
})

await cosmic.objectTypes.insertOne({
  title: "Bikes",
  slug: "bikes",
  emoji: "🏍️",
  metafields: [
    {
      "title": "Image",
      "key": "image",
      "type": "file",
      "required": true,
      "media_validation_type": "image"
    },
    {
      "title": "Headline",
      "key": "headline",
      "type": "text",
      "required": false
    }
  ]
})
```
```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/object-types \
-d '{"title":"Motorcycles","slug":"motorcycles"}' \
-H 'Content-Type: application/json' \
-H "Authorization: Bearer {BUCKET_WRITE_KEY}"
```

```json {{ title: 'Response' }}
{
  "object_type": {
    "id": "63bde47897d49d0008a270b3",
    "title": "Bikes",
    "slug": "bikes",
    "singular": "Bike",
    "emoji": "🏍️",
    "created_at": "2023-01-10T22:19:36.128Z",
    "modified_at": "2023-03-16T21:09:09.914Z",
    "singleton": false,
    "options": {
      "slug_field": true
    },
    "metafields": [
      {
        "id": "c7c50911-3b38-4b22-a307-392eb9f84739",
        "title": "Image",
        "key": "image",
        "type": "file",
        "helptext": "",
        "required": false,
        "media_validation_type": "image"
      },
      {
        "id": "1157a40b-9a1a-4d06-96e0-2338f01d366d",
        "title": "Headline",
        "key": "headline",
        "type": "text",
        "helptext": "",
        "required": false
      }
      ...
    ]
  }
}
```
---

## Update an Object type 

This endpoint enables you to update an Object type.

If using the NPM module, use the `$set` method to update the Object type properties specificed.

### Optional parameters

Singular title of the Object type.

Object type slugs are unique per Bucket.
Default: `title` converted to slug.

Single or multiple Objects in this type.

Valid Unicode emoji displayed on the Object type table.

Array of Metafields. See [Metafields](/docs/api/metafields).

Contains boolean property `slug_field` which controls
the display options for the `slug` field for Objects in the
type.

Add localization to the Object type. Default: `false`

Array of available locales in the Object type. See [available locale
codes](#localization).

Default locale when creating new Objects in this type. Objects will be
grouped by this locale in the Object type table in the dashboard.

```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY',
  writeKey: 'BUCKET_WRITE_KEY'
})

await cosmic.objectTypes.updateOne('object-type-slug', {
  title: 'Motorcycles',
  slug: 'motorcycles',
  singular: 'Motorcycle'
})
```
```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/object-types/bikes \
  -d '{"title":"Motorcycles","slug":"motorcycles","singular":"Motorcycle"}' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer {BUCKET_WRITE_KEY}" \
  -X PATCH
```

```json {{ title: 'Response' }}
{
  "object_type": {
    "id": "63bde47897d49d0008a270b3",
    "title": "Motorcycles",
    "slug": "motorcycles",
    "singular": "Motorcycle",
    "emoji": "🏍️",
    "created_at": "2023-01-10T22:19:36.128Z",
    "modified_at": "2023-03-16T21:09:09.914Z",
    "singleton": false,
    "options": {
      "slug_field": true
    },
    "metafields": [
      {
        "id": "c7c50911-3b38-4b22-a307-392eb9f84739",
        "title": "Image",
        "key": "image",
        "type": "file",
        "helptext": "",
        "required": false,
      },
      {
        "id": "1157a40b-9a1a-4d06-96e0-2338f01d366d",
        "title": "Headline",
        "key": "headline",
        "type": "text",
        "helptext": "",
        "required": false
      }
      ...
    ]
  }
}
```
---

## Delete an Object type 

This endpoint enables you to delete an Object type and all Objects in this type from your Bucket.

### Required parameters

Object type slug.

### Optional parameters

Triggers corresponding Object action webhook (See Webhooks).

```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY',
  writeKey: 'BUCKET_WRITE_KEY'
})

await cosmic.objectTypes.deleteOne("object-type-slug")
```
```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/object-types/:slug \
  -H "Authorization: Bearer {BUCKET_WRITE_KEY}" \
  -X DELETE
```

```json {{ title: 'Response' }}
{
  "message": "Object type with slug ':slug' deleted successfully from bucket."
}

```
## Metafields

Learn about adding Metafields to Object types in the [Metafields page](/docs/api/metafields).