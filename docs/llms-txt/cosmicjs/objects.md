# Source: https://www.cosmicjs.com/docs/api/objects.md

# Objects

Learn about Objects; the basic building blocks of content in your Cosmic Bucket.

Use the following methods to create, read, update, and delete Objects.

## The Object model

The Object model contains all the information about Objects.

### Properties

Unique identifier for Object.

Object type slug.

Object title.

Object slugs are unique per each Object type. Localized versions of Objects
are linked with the same slug. See [localization](/docs/api/localization).

Object status.
Options `published | draft`

HTML Content. (deprecatated in API v3, use Metafield instead)

Values of the Metafields created in the Object type.

The id of the user who created the Object.

Date the Object was created.

The id of the user who last modified the Object.

Date Object was last modified.

Date Object was last published.

UNIX millisecond timestamp. Publish automatically at a later time.

UNIX millisecond timestamp. Unpublish automatically at a later time.

See [localization](/docs/api/localization) for locale options.

Media `name`. Media must be available in Bucket. See [media](/docs/api/media).
```json
{
  "id": "63dc57ca24090e0008683d42",
  "slug": "add-a-headless-cms-to-astro-in-3-easy-steps",
  "title": "Add a headless CMS to Astro in 3 easy steps",
  "bucket": "63dc24a4d71e244b63c88fca",
  "created_at": "2023-02-03T00:39:38.35Z",
  "modified_at": "2023-03-23T12:08:13.547Z",
  "status": "published",
  "thumbnail": "https://imgix.cosmicjs.com/1c8531f0-97fb-11ed-81d8-8f0123e10511-A-photo-of-Michelangelos-sculpture-of-David-wearing-headphones-djing.webp",
  "published_at": "2023-03-23T12:08:13.547Z",
  "modified_by": "629e6cdda6f4f100091ae2e0",
  "publish_at": null,
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

## Get Objects 

This endpoint enables you to retrieve a list of your Objects.

### Optional parameters

A JSON object to perform Object search and filtering. See [queries section](/docs/api/queries) for more detail. Must be URL encoded for REST requests.

### Optional methods

Declare which properties to return in comma-separated string (or array if using the NPM module). Remove to see all Object properties. Can include nested metadata. Example: `id,title,metadata.author.metadata.image.url`.

If you are using the Cosmic JavaScript SDK, you can format the `props` string in a graph syntax such as:
```graphql
{
  id
  slug
  title
  metadata {
    content
    description
    parent {
      title
    }
  }
}

```
Set to `any` for latest version of draft or published Object.
Options `published | draft | any`
Default `published`

Order of Objects returned.
Options `created_at, -created_at, modified_at, -modified_at, random, order, metadata.$key, -metadata.$key`
Use `-` for descending order.
Default `-order` (order in dashboard, top down)
Sort by Metadata
Sort by metadata using `metadata.$key` and `-metadata.$key`. For example, setting `sort` to `metadata.price` will return Objects from low to high price. To enable sortable Metafields, go to Object type > Settings in the dashboard. Metafields that can be sortable include Text, Number, and Date Metafields. You are currently limited to 2 sortable Metafields per Object type.

Limit the number of Objects returned.
Default `1000`

Used for pagination. The number of Objects to skip.
Default `0`

The depth of Object references using Object Relationship Metafields. Circular reference is prohibited.
Default `0`

Used for pagination. Get Objects after specified Object `id` (can only use one of `skip` or `after`).

Set to `false` for real-time updates. Increases latency of endpoint.
Default `true`

Set to `true` for reader-friendly formated JSON response.
Default `false`

Used to get more media data. Contains a `media` object with a `props` property. This is handy for getting media size, dimensions, alt text, metadata, etc. See the [Media model](/docs/api/media) for more available properties. Available only on the Cosmic JavaScript SDK. For example:
```js
await cosmic.objects.find({
  type: 'object-type-slug'
}).props(props)
.options({
  media: {
    props: 'alt_text,width,height'
  }
})

```
```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY'
})

const props = `{
  id
  slug
  title
  metadata {
    content
    description
    parent {
      title
    }
  }
}`

await cosmic.objects.find({
  type: 'object-type-slug'
}).props(props).limit(1)
```

```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/objects \
    -d read_key=${BUCKET_READ_KEY} \
    --data-urlencode query='{"type":"object-type-slug"}' \
    -d props=id,slug,title,metadata.content,metadata.description,metadata.parent.title \
    -d limit=1 \
    -G
```
```swift {{ title: 'Swift' }}
let cosmic = CosmicSDKSwift(
  .createBucketClient(
      bucketSlug: "BUCKET_SLUG",
      readKey: "READ_KEY",
      writeKey: "WRITE_KEY"
  )
)

@State var objects: [Object] = []

cosmic.find(
    type: "object-type-slug",
    props: "id,
            slug,
            title,
            metadata.content,
            metadata.description,
            metadata.parent.title",
    limit: "1",
    sort: .random,
    status: .any
    ) { results in
    switch results {
    case .success(let result):
        self.objects = result.objects
    case .failure(let error):
        print(error)
    }
}
```

```json {{ title: 'Response' }}
{
  "objects": [
    {
      "id": "5f7357967286d7773adc551e",
      "slug": "learning",
      "title": "Learning",
      "metadata": {
        "content": "<p>Learning is fun!!</p>",
        "description": "This is the example description",
        "parent": {
          "title": "Example Post"
        }
      }
    }
  ],
  "total": 6,
  "limit": 1
}
```
---

## Get a single Object by slug 

This endpoint enables you to get a single Object by `slug`. To get a single Object by `slug` indicate the `type` and `slug` in the `query` parameter.

With the Cosmic NPM module, you can use the `findOne` method to return an `object`. If using the REST API, it will return an `array`.

### Optional parameters

A JSON object to perform Object search and filtering. See [queries section](/docs/api/queries) for more detail. Must be URL encoded for REST requests.

### Optional methods

Declare which properties to return in comma-separated string (or array if using the NPM module). Remove to see all Object properties. Can include nested metadata. Example: `slug,title,metadata.content,metadata.image.imgix_url`.

If you are using the Cosmic JavaScript SDK, you can format the `props` string in a graph syntax such as:

```graphql
{
  slug
  title
  metadata {
    content
    image {
      imgix_url
    }
  }
}
```
Set to `any` for latest version of draft or published Object.
Options `published | draft | any`
Default `published`

The depth of Object references using Object Relationship Metafields. Circular reference is prohibited.
Default `0`

Set to `false` for real-time updates. Increases latency of endpoint.
Default `true`

Set to `true` for reader-friendly formated JSON response.
Default `false`

Used to get more media data. Contains a `media` object with a `props` property. This is handy for getting media size, dimensions, alt text, metadata, etc. See the  Available only on the Cosmic JavaScript SDK. For example:

```js
await cosmic.objects.findOne({
  type: 'object-type-slug',
  slug: 'object-slug'
}).props(props)
.options({
  media: {
    props: 'alt_text,width,height'
  }
})
```
```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY'
})

const props = `{
  slug
  title
  metadata {
    content
    image {
      imgix_url
    }
  }
}`

await cosmic.objects.findOne({
  type: 'object-type-slug',
  slug: 'object-slug'
}).props(props)
.options({
  media: {
    props: 'alt_text,width,height'
  }
})
```
`

```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/objects \
    -d read_key=${BUCKET_READ_KEY} \
    --data-urlencode query='{"type":"object-type-slug","slug":"object-slug"}' \
    -d props=slug,title,metadata.content,metadata.image.imgix_url \
    -d limit=1 \
    -G
```
```json {{ title: 'Response' }}
{
  "object": {
    "slug": "my-blog-post-slug",
    "title": "My Blog Post",
    "metadata": {
      "content": "<p>Learning is fun!!</p>",
      "image": {
        "imgix_url": "https://imgix.cosmicjs.com/123asdf...",
        "alt_text": "This is an example image alt text",
        "width": 1200,
        "height": 600
      }
    }
  }
}
```

---

## Get a single Object by id 

This endpoint enables you to get a single Object by `id`. To get a single Object by `id`, indicate the `id` in the `query` parameter.
To get an Object by slug, see the [above example](/docs/api/objects#get-a-single-object-by-slug).

### Optional parameters

A JSON object to perform Object search and filtering. See [queries section](/docs/api/queries) for more detail. Must be URL encoded for REST requests.

### Optional methods

Declare which properties to return in comma-separated string (or array if using the NPM module). Remove to see all Object properties. Can include nested metadata. Example: `slug,title,metadata.content,metadata.image.imgix_url`.

If you are using the Cosmic JavaScript SDK, you can format the `props` string in a graph syntax such as:

```graphql
{
  slug
  title
  metadata {
    content
    image {
      imgix_url
    }
  }
}
```
Set to `any` for latest version of draft or published Object.
Options `published | draft | any`
Default `published`

The depth of Object references using Object Relationship Metafields. Circular reference is prohibited.
Default `0`

Set to `false` for real-time updates. Increases latency of endpoint.
Default `true`

Set to `true` for reader-friendly formated JSON response.
Default `false`

Used to get more media data. Contains a `media` object with a `props` property. This is handy for getting media size, dimensions, alt text, metadata, etc. See the  Available only on the Cosmic JavaScript SDK. For example:

```js
await cosmic.objects.findOne({
  id: 'object-id'
}).props(props)
.options({
  media: {
    props: 'alt_text,width,height'
  }
})
```
```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY'
})

const props = `{
  slug
  title
  metadata {
    content
    image {
      imgix_url
    }
  }
}`

await cosmic.objects.findOne({
  id: 'object-id'
}).props(props)
.options({
  media: {
    props: 'alt_text,width,height'
  }
})
```

```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/objects/:id \
    -d read_key=${BUCKET_READ_KEY} \
    -d props=slug,title,content,metadata.image.imgix_url \
    -G
```
```swift {{ title: 'Swift' }}
let cosmic = CosmicSDKSwift(
  .createBucketClient(
      bucketSlug: "BUCKET_SLUG",
      readKey: "READ_KEY",
      writeKey: "WRITE_KEY"
  )
)

@State private var object: Object?

cosmic.findOne(type: "object-type", id: "object.id") { results in
    switch results {
    case .success(let result):
        self.object = result.object
    case .failure(let error):
        print(error)
    }
}
```

```json {{ title: 'Response' }}
{
  "object": {
    "slug": "learning",
    "title": "Learning",
    "metadata": {
      "content": "<p>Learning is fun!!</p>",
      "image": {
        "imgix_url": "https://imgix.cosmicjs.com/123asdf...",
        "alt_text": "This is an example image alt text",
        "width": 1200,
        "height": 600
      }
    }
  }
}
```
---

## Create an Object 

This endpoint enables you to create an Object in your Bucket.

The data request payload will need to be sent in JSON format with the `Content-Type: application/json` header set.

### Required parameters

Object title.

Object type `slug`.

### Optional parameters

If `slug` is not included, the `title` will be converted into the `slug`.

If validation requirements are set on Metafields on the Object type, they will need to pass the validation requirements.

Triggers corresponding Object action webhook (See Webhooks).

```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY',
  writeKey: 'BUCKET_WRITE_KEY'
})

await cosmic.objects.insertOne({
  title: 'Blog Post Example Title',
  type: 'blog-posts',
  metadata: {
    content: 'Here is an example blog post content...',
    seo_description: 'This is an example blog post SEO description.',
    featured_post: true
  }
})
```
```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/objects \
-d '{"title":"Blog Post Example Title","type":"blog-posts","metadata":{"content": "Here is an example blog post content...","seo_description":"This is an example blog post SEO description.","featured_post": true}}' \
-H 'Content-Type: application/json' \
-H "Authorization: Bearer {BUCKET_WRITE_KEY}"
```

```swift {{ title: 'Swift' }}
let cosmic = CosmicSDKSwift(
  .createBucketClient(
      bucketSlug: "BUCKET_SLUG",
      readKey: "READ_KEY",
      writeKey: "WRITE_KEY"
  )
)

@State private var object: Object?

cosmic.insertOne(
    type: "object-type",
    title: "object.title"
    ) { results in
    switch results {
    case .success(_):
        print("Updated \(object.id)")
    case .failure(let error):
        print(error)
    }
}
```
```json {{ title: 'Response' }}
{
  "object": {
    "id": "5ff75368c2dfa81a91695cec",
    "title": "Blog Post Example Title",
    "slug": "blog-post-example-title",
    "type":"blog-posts-type-slug",
    "metadata":{
    "content": "Here is an example blog post content...",
    "seo_description": "This is an example blog post SEO description.",
      "featured_post": true
    }
  }
}
```

---

## Update an Object 

This endpoint enables you to update an Object.

The data request payload will need to be sent in JSON format with the `Content-Type: application/json` header set.

### Required parameters

Object id.

### Optional parameters

Object title.

Object slug.

Status of the Object.
Options `published | draft`

If validation requirements are set on Metafields on the Object type, they will need to pass the validation requirements.

UNIX millisecond timestamp. Publish automatically at a later time.

UNIX millisecond timestamp. Unpublish automatically at a later time.

See [localization](/docs/api/localization) for locale options.

Media `name`. Media must be available in Bucket. See Media(link to media).

Triggers corresponding Object action webhook (See Webhooks).

```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY',
  writeKey: 'BUCKET_WRITE_KEY'
})

await cosmic.objects.updateOne("object-id", {
  title: 'New Title Edit',
  metadata: {
    featured_post: false
  }
})
```
```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/objects/:id \
  -d '{"title":"New Title Edit"}' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer {BUCKET_WRITE_KEY}" \
  -X PATCH
```

```swift {{ title: 'Swift' }}
let cosmic = CosmicSDKSwift(
  .createBucketClient(
      bucketSlug: "BUCKET_SLUG",
      readKey: "READ_KEY",
      writeKey: "WRITE_KEY"
  )
)

@State private var object: Object?

cosmic.updateOne(
    type: "object-type",
    id: "object.id",
    title: "New Title Edit",
    metadata: ["featured_post": false]
    ) { results in
    switch results {
    case .success(_):
        print("Updated \(object.id)")
    case .failure(let error):
        print(error)
    }
}
```
```json {{ title: 'Response' }}
{
  "object": {
    "id": "5ff75368c2dfa81a91695cec",
    "title": "New Title Edit",
    "slug": "blog-post-title",
    "type":"blog-posts",
    "metadata":{
      "content": "Here is the blog post content...",
      "seo_description": "This is the blog post SEO description.",
      "featured_post": false
    }
  }
}
```

---

## Update Object metadata 

Learn how to update Object metadata.

Use the `metadata` property when doing create or update requests to the Objects API endpoint.

### Update basic Metafields

To update basic Metafields on Objects such as text and numbers, make sure to send the corresponding type.

### Required parameter

Using the `metadata` property, update metadata values using the Object type Metafield `key:value` format.

```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY',
  writeKey: 'BUCKET_WRITE_KEY'
})

await cosmic.objects.updateOne('object-id', {
  metadata: {
    headline: 'This guitar amp is LOUD!',
    max_volume: 11,
    on_sale: true
  }
})
```
```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/objects/:id \
  -d '{"metadata":{"headline":"This guitar amp is LOUD!","max_volume":11,"on_sale":true}}' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer {BUCKET_WRITE_KEY}" \
  -X PATCH
```

```swift {{ title: 'Swift' }}
let cosmic = CosmicSDKSwift(
  .createBucketClient(
      bucketSlug: "BUCKET_SLUG",
      readKey: "READ_KEY",
      writeKey: "WRITE_KEY"
  )
)

@State private var object: Object?

cosmic.updateOne(
      type: "object-type",
      id: "object.id",
      metadata: [
        "headline": "This guitar amp is LOUD!",
        "max_volume": 11,
        "on_sale": true
      ]
    ) { results in
    switch results {
    case .success(_):
        print("Updated \(object.id)")
    case .failure(let error):
        print(error)
    }
}
```
```json {{ title: 'Response' }}
{
  "object": {
    "id": "5ff75368c2dfa81a91695cec",
    "title": "Fender Spinal Tap Edition Amp",
    "slug": "fender-spinal-tap-edition-amp",
    "metadata": {
      "headline": "This guitar amp is LOUD!",
      "max_volume": 11,
      "on_sale": true
    }
  }
}
```
`

### Object relationship Metafield

**Single Object**
To add or update a single Object relationship Metafield, set the Object `id` as a `string` in the `metadata.$key` value.

**Multiple Object**
To add or update a multiple Object relationship Metafield, use an `array` of Object ids.

```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY',
  writeKey: 'BUCKET_WRITE_KEY'
})

await cosmic.objects.updateOne('object-id', {
  metadata: {
    author: 'author-object-id', // Object id
    categories: ['cat1-object-id','cat2-object-id','cat3-object-id']  // Object ids
  }
})
```
```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/objects/:id \
  -d '{"metadata":{"author":"author-object-id","categories":["cat1-object-id","cat2-object-id","cat3-object-id"]}}' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer {BUCKET_WRITE_KEY}" \
  -X PATCH
```

```swift {{ title: 'Swift' }}
let cosmic = CosmicSDKSwift(
  .createBucketClient(
      bucketSlug: BUCKET,
      readKey: READ_KEY,
      writeKey: WRITE_KEY
  )
)

@State private var object: Object?

cosmic.updateOne(
    type: "object-type",
    id: "object.id",
    metadata: [
      "author": "author-object-id",
      "categories": [
        "cat1-object-id",
        "cat2-object-id",
        "cat3-object-id"
        ]
      ]
    ) { results in
    switch results {
    case .success(_):
        print("Updated \(object.id)")
    case .failure(let error):
        print(error)
    }
}
```
```json {{ title: 'Response' }}
{
  "object": {
    "id": "5ff75368c2dfa81a91695cec",
    "title": "New Title Edit",
    "slug": "blog-post-title",
    "metadata": {
      "author": "author-object-id",
      "categories": ["cat1-object-id", "cat2-object-id", "cat3-object-id"]
    }
  }
}
```

### Media Metafields

To add a value to a media Metafield, use the `name` of an existing media resource in the Bucket.

**Single Media**

To add a single media Metafield, use the media `name` value such as:

```json
{
  "metadata": {
    "image": "image-name-in-bucket.jpg"
  }
}
```
**Multi Media**

For the Multi Media Metafield, use an `array` of media `name` values such as:

```json
{
  "metadata": {
    "images": ["image-name-1.jpg", "image-name-2.jpg", "image-name-3.jpg"]
  }
}
```
See [media model](/docs/api/media).

```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY',
  writeKey: 'BUCKET_WRITE_KEY'
})

await cosmic.objects.updateOne('object-id', {
  metadata: {
    image: "image-name-in-bucket.jpg"
  }
})
```
```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/objects/:id \
  -d '{"metadata":{"image":"image-name-in-bucket.jpg"}}' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer {BUCKET_WRITE_KEY}" \
  -X PATCH
```

```swift {{ title: 'Swift' }}
let cosmic = CosmicSDKSwift(
  .createBucketClient(
      bucketSlug: BUCKET,
      readKey: READ_KEY,
      writeKey: WRITE_KEY
  )
)

@State private var object: Object?

cosmic.updateOne(
    type: "object-type",
    id: "object.id",
    metadata: [
      "image": "image-name-in-bucket.jpg"
      ]
    ) { results in
    switch results {
    case .success(_):
        print("Updated \(object.id)")
    case .failure(let error):
        print(error)
    }
}
```
```json {{ title: 'Response' }}
{
  "object": {
    "id": "5ff75368c2dfa81a91695cec",
    "title": "New Title Edit",
    "slug": "blog-post-title",
    "metadata": {
      "image": {
        "url": "https://cdn.cosmicjs.com/image-name-in-bucket.jpg",
        "imgix_url": "https://imgix.cosmicjs.com/image-name-in-bucket.jpg"
      }
    }
  }
}
```

---

## Add Object Revision 

This endpoint enables you to add a revision to an Object.

The data request payload will need to be sent in JSON format with the `Content-Type: application/json` header set.

### Required parameters

Object id.

### Default parameters

The status will always be `draft`. Use the [update methods](/docs/api/objects#update-an-object) to update the status of an Object to `published`.

### Optional parameters

Object title.

Object slug.

HTML Content. (deprecatated in API v3, use Metafield instead)

If validation requirements are set on Metafields on the Object type, they will need to pass the validation requirements.

UNIX millisecond timestamp. Publish automatically at a later time.

UNIX millisecond timestamp. Unpublish automatically at a later time.

Media `name`. Media must be available in Bucket. See Media(link to media).

See [localization](/docs/api/localization) for locale options.

Triggers corresponding Object action webhook (See Webhooks).

```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY',
  writeKey: 'BUCKET_WRITE_KEY'
})

await cosmic.objectRevisions.insertOne("object-id", {
  title: 'New Title Edit',
  metadata: {
    featured_post: false
  }
})
```
```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/objects/:id/revisions \
  -d '{"title":"New Title Edit"}' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer {BUCKET_WRITE_KEY}" \
  -X POST
```

```json {{ title: 'Response' }}
{
  "revision": {
    "id": "5ff75368c2dfa81a91695cec",
    "title": "New Title Edit",
    "slug": "blog-post-title",
    "type":"blog-posts",
    "metadata":{
    "content": "Here is the blog post content...",
    "seo_description": "This is the blog post SEO description.",
      "featured_post": false
    }
  }
}
```
---

## Delete an Object 

This endpoint enables you to delete Objects from your Bucket.

### Required parameters

Object id.

### Optional parameters

Triggers corresponding Object action webhook (See Webhooks).

```js
import { createBucketClient } from '@cosmicjs/sdk'

const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY',
  writeKey: 'BUCKET_WRITE_KEY'
})

await cosmic.objects.deleteOne('object-id')
```
```bash {{ title: 'cURL' }}
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/objects/:id \
  -H "Authorization: Bearer {BUCKET_WRITE_KEY}" \
  -X DELETE
```

```swift {{ title: 'Swift' }}
let cosmic = CosmicSDKSwift(
  .createBucketClient(
      bucketSlug: BUCKET,
      readKey: READ_KEY,
      writeKey: WRITE_KEY
  )
)

@State private var object: Object?

cosmic.deleteOne(type: "object-type", id: "object.id")
{ results in
    switch results {
    case .success(_):
        print("Deleted \(object.id)")
    case .failure(let error):
        print(error)
    }
}
```
```json {{ title: 'Response' }}
{
  "message": "Object with id ':id' deleted successfully from bucket."
}

```

---