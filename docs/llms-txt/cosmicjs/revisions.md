# Source: https://www.cosmicjs.com/docs/api/revisions.md

# Revisions

Learn about Revisions; the version history of content in your Cosmic Bucket.

Use the following methods to view and manage Revisions. Note: Revisions cannot be edited or deleted.

## The Revision model

The Revision model contains all the information about content revisions.

### Properties

Unique identifier for Revision.

ID of the Object this revision belongs to.

Object title at time of revision.

Object slug at time of revision.

HTML Content at time of revision. (deprecatated in API v3, use Metafield instead)

Values of the Metafields at time of revision.

The id of the user who created the revision.

Date the revision was created.

Status of the revision.
Options `published | draft`

Date revision was published (if applicable).

Date revision was last modified.

See [localization](/docs/api/localization) for locale options.
```json
{
  "id": "64fe8a1b24090e0008683e53",
  "object_id": "63dc57ca24090e0008683d42",
  "title": "Add a headless CMS to Astro in 3 easy steps",
  "slug": "add-a-headless-cms-to-astro-in-3-easy-steps",
  "bucket": "63dc24a4d71e244b63c88fca",
  "created_at": "2023-03-23T12:08:13.547Z",
  "modified_at": "2023-03-23T12:08:13.547Z",
  "status": "published",
  "thumbnail": "https://imgix.cosmicjs.com/1c8531f0-97fb-11ed-81d8-8f0123e10511-A-photo-of-Michelangelos-sculpture-of-David-wearing-headphones-djing.webp",
  "published_at": "2023-03-23T12:08:13.547Z",
  "created_by": "629e6cdda6f4f100091ae2e0",
  "type": "blog-posts",
  "metadata": {
    "content": "Astro is a lightweight web framework capable of shipping highly performant websites with minimal (or non-existent) JavaScript bundles. In this guide...",
    "image": {
      "url": "https://cdn.cosmicjs.com/02670ac0-38ef-11ed-adfd-ddb1795c6ac6-add-a-headless-cms-to-astro-in-3-easy-steps.png",
      "imgix_url": "https://imgix.cosmicjs.com/02670ac0-38ef-11ed-adfd-ddb1795c6ac6-add-a-headless-cms-to-astro-in-3-easy-steps.png"
    },
    "published_date": "2022-09-20",
    "author": {
      "title": "Bill Brasky"
    }
  }
}

```
---

## Get Revisions 

This endpoint enables you to retrieve a list of revisions for a specific Object.

### Required parameters

ID of the Object to retrieve revisions for.

### Optional methods

Declare which properties to return in comma-separated string (or array if using the NPM module). Remove to see all Revision properties.

Limit the number of Revisions returned.
Default `1000`

Used for pagination. The number of Revisions to skip.
Default `0`

Order of Revisions returned.
Options `created_at, -created_at`
Use `-` for descending order.
Default `-created_at` (newest first)

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

await cosmic.objectRevisions.find('object-id').props([
  'id',
  'title',
  'created_at',
  'status'
]).limit(10)

```
```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/objects/${OBJECT_ID}/revisions \
    -d read_key=${BUCKET_READ_KEY} \
    -d props=id,title,created_at,status \
    -d limit=10 \
    -G
```

```json {{ title: 'Response' }}
{
  "revisions": [
    {
      "id": "64fe8a1b24090e0008683e53",
      "title": "Add a headless CMS to Astro in 3 easy steps",
      "created_at": "2023-03-23T12:08:13.547Z",
      "status": "published"
    },
    {
      "id": "64fe8a0924090e0008683e52",
      "title": "Add a headless CMS to Astro in 3 easy steps (Draft)",
      "created_at": "2023-03-23T12:07:45.123Z",
      "status": "draft"
    }
  ],
  "total": 2,
  "limit": 10
}
```
---

## Get a single Revision 

This endpoint enables you to get a single Revision by its ID.

### Required parameters

ID of the Object the revision belongs to.

ID of the specific revision to retrieve.

### Optional methods

Declare which properties to return in comma-separated string (or array if using the NPM module). Remove to see all Revision properties.

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

await cosmic.objectRevisions.findOne({
  objectId: 'object-id',
  revisionId: 'revision-id'
}).props([
  'id',
  'title',
  'metadata',
  'created_at'
])
```
```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/objects/${OBJECT_ID}/revisions/${REVISION_ID} \
    -d read_key=${BUCKET_READ_KEY} \
    -d props=id,title,metadata,created_at \
    -G
```

```json {{ title: 'Response' }}
{
  "revision": {
    "id": "64fe8a1b24090e0008683e53",
    "title": "Add a headless CMS to Astro in 3 easy steps",
    "created_at": "2023-03-23T12:08:13.547Z",
    "metadata": {
      "content": "Astro is a lightweight web framework capable of shipping highly performant websites with minimal (or non-existent) JavaScript bundles. In this guide...",
      "image": {
        "url": "https://cdn.cosmicjs.com/02670ac0-38ef-11ed-adfd-ddb1795c6ac6-add-a-headless-cms-to-astro-in-3-easy-steps.png",
        "imgix_url": "https://imgix.cosmicjs.com/02670ac0-38ef-11ed-adfd-ddb1795c6ac6-add-a-headless-cms-to-astro-in-3-easy-steps.png"
      },
      "published_date": "2022-09-20",
      "author": {
        "title": "Bill Brasky"
      }
    }
  }
}
```
---

## Add a Revision 

This endpoint enables you to add a new revision to an existing Object.

Adding a revision creates a new version of the Object without publishing it.

### Required parameters

ID of the Object to add a revision to.

### Optional parameters

Updated title for the revision.

Updated slug for the revision.

Updated metadata values for the revision.

Status of the revision.
Options `published | draft`
Default `draft`

Triggers corresponding Object action webhook (See Webhooks).

```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY',
  writeKey: 'BUCKET_WRITE_KEY'
})

await cosmic.objectRevisions.insertOne('object-id', {
  title: 'Updated Blog Post Title',
  metadata: {
    content: 'This is the updated content for the blog post...',
    featured_post: true
  },
  status: 'draft'
})
```
```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/objects/${OBJECT_ID}/revisions \
-d '{"title":"Updated Blog Post Title","metadata":{"content":"This is the updated content for the blog post...","featured_post":true},"status":"draft"}' \
-H 'Content-Type: application/json' \
-H "Authorization: Bearer ${BUCKET_WRITE_KEY}" \
-X POST
```

```json {{ title: 'Response' }}
{
  "revision": {
    "id": "65fe8a1b24090e0008683e54",
    "object_id": "63dc57ca24090e0008683d42",
    "title": "Updated Blog Post Title",
    "slug": "add-a-headless-cms-to-astro-in-3-easy-steps",
    "status": "draft",
    "created_at": "2023-04-15T09:22:45.123Z",
    "created_by": "629e6cdda6f4f100091ae2e0",
    "metadata": {
      "content": "This is the updated content for the blog post...",
      "featured_post": true,
      "image": {
        "url": "https://cdn.cosmicjs.com/02670ac0-38ef-11ed-adfd-ddb1795c6ac6-add-a-headless-cms-to-astro-in-3-easy-steps.png",
        "imgix_url": "https://imgix.cosmicjs.com/02670ac0-38ef-11ed-adfd-ddb1795c6ac6-add-a-headless-cms-to-astro-in-3-easy-steps.png"
      }
    }
  }
}

```
---