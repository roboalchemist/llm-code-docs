# Source: https://www.cosmicjs.com/docs/api/authentication.md

# Authentication

Learn how to authenticate your requests to the Cosmic API.

## Get your API keys

Cosmic uses API keys to authenticate requests. For the following examples, you will need your:

1. Bucket slug
2. Bucket read key
3. Bucket write key

You can get your API access keys by going to Bucket Settings > API Access in [the Cosmic dashboard](https://app.cosmicjs.com/login).

## Use your API keys

Use the methods below to use your Cosmic API keys.

Before you can make requests to the Cosmic API, you will need to grab your
Bucket slug and API keys from your dashboard. Find them in [Bucket Settings
&raquo; API Access](https://app.cosmicjs.com/login).
```js
// Import
import { createBucketClient } from '@cosmicjs/sdk';

// Authenticate
const cosmic = createBucketClient({
  bucketSlug: 'BUCKET_SLUG',
  readKey: 'BUCKET_READ_KEY',
  writeKey: 'BUCKET_WRITE_KEY',
});

// Fetch content
await cosmic.objects
  .find({
    type: 'posts',
  })
  .limit(1);

// Write content
await cosmic.objects.insertOne({
  title: 'Blog Post Title',
  type: 'posts',
  metadata: {
    content: 'Here is the blog post content...',
    seo_description: 'This is the blog post SEO description.',
    featured_post: true,
  },
});

```
```bash {{ title: 'cURL' }}
# Fetch content
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/objects \
  -d read_key=${BUCKET_READ_KEY} \
  --data-urlencode query='{"type": "posts"}' \
  -d limit=1 \
  -G

# Write content
curl https://api.cosmicjs.com/v3/buckets/${BUCKET_SLUG}/objects \
  -d '{"title":"Blog Post Title","type":"posts","metadata":{"seo_description":"This is the blog post SEO description.","featured_post": true}}' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer {BUCKET_WRITE_KEY}"
```

```swift {{ title: 'Swift' }}
// Import
import CosmicSDK

// Authenticate
let cosmic = CosmicSDKSwift(
    .createBucketClient(
        bucketSlug: BUCKET,
        readKey: READ_KEY,
        writeKey: WRITE_KEY
    )
)

// Fetch content
@State var posts: [Object] = []

cosmic.find(type: posts) { results in
    switch results {
    case .success(let result):
        self.posts = result.objects
    case .failure(let error):
        print(error)
    }
}

// Write content
@State private var post: Object?

cosmic.insertOne(
    type: posts,
    title: post.title
    ) { results in
    switch results {
    case .success(_):
        print("Updated \(post.id)")
    case .failure(let error):
        print(error)
    }
}

```
Never expose your Bucket write key in any client-side code.