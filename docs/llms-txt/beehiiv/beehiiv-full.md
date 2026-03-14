# Beehiiv Documentation

Source: https://developers.beehiiv.com/llms-full.txt

---

***

## subtitle: beehiiv is the newsletter platform built for *growth*.

Harness beehiiv's API to enrich your user records with custom fields from external forms,
manage lists and segmentation programmatically, and integrate your beehiiv publication
more closely with advertising platforms.

<Cards>
  <Card title="API Reference" icon="fa-solid fa-code" href="/api-reference" />

  <Card title="Create an API Key" icon="fa-solid fa-key" href="/welcome/create-an-api-key" />

  <Card title="Sign up for beehiiv" icon="fa-solid fa-user-plus" href="https://app.beehiiv.com/signup" />

  <Download src="https://files.buildwithfern.com/https://beehiiv.docs.buildwithfern.com/6c613e8c584d2745edcd2f2b9a76ff3c2dfb8cb4af29da4f5a01d83eba943c51/assets/beehiiv-API-Specification.yaml" filename="beehiiv - OpenAPI Specification.yaml">
    <Card title="Download OpenAPI Specification" icon="fa-solid fa-file-arrow-down" />
  </Download>
</Cards>

Looking for support? Inspiration? Check out our other resources:

* [Knowledge Base](https://support.beehiiv.com/hc/en-us): Product support, documentation, and assistance.
* [Tutorials](https://www.youtube.com/channel/UCI80tsW3wYNGEJLxwJo42vw): Archive of video tutorials.
* [Course](https://www.beehiiv.com/courses/newsletter-xp): How to build, scale, and monetize your newsletter.
* [Blog](https://blog.beehiiv.com/): Best practices to help scale your newsletter.
* [Submit a support ticket](https://app.beehiiv.com/?new_support_ticket)


***

## subtitle: Get up and running with the beehiiv API.

The beehiiv API key is used as the Bearer Token for all requests.
It enables secure account authentication and should be kept secret at all times.

<Info>
  Building an integration? Use OAuth2 instead of API keys and follow our [OAuth2 guide](/oauth2/oauth2-summary).
</Info>

<Steps>
  ### Log in to [beehiiv](https://app.beehiiv.com/).

  ### Navigate to the API page

  Click on `Settings` and then `API` under the `Workspace Settings` section.

  ### Click the `Create New API Key` button

  After creating your API key, be sure to copy and safely save the key, as it
  will be inaccessible after leaving the page. You may be prompted to verify
  your identity with Stripe.
</Steps>

### Best Practices

To prevent unauthorized access to your beehiiv account, we recommend the following best practices:

* Use a unique API key for each application or service.
* Rotate API keys regularly.
* Store API keys securely (we recommend using environment variables).
* API keys should only be exposed on the [server side of your application](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/). This includes in your code, in your browser's console, or in your browser's local storage. This is especially important for web applications.
* Monitor API key usage and activity.


# Pagination

The beehiiv API uses pagination to manage large result sets efficiently. We support two pagination methods:

1. **Cursor-based pagination** (recommended)
2. **Offset-based pagination** (deprecated)

## Cursor-Based Pagination

Cursor-based pagination provides consistent, efficient navigation through large datasets. It uses opaque cursor tokens to mark positions in the result set.

### How It Works

* Use the `cursor` parameter to specify where to start fetching results
* Set `limit` to control how many results to return per page (max 100)
* The response includes a `next_cursor` for fetching the next page
* Use `has_more` to determine if additional pages exist

### Request Parameters

| Parameter | Type    | Description                                      |
| --------- | ------- | ------------------------------------------------ |
| `cursor`  | string  | Opaque cursor token for pagination position      |
| `limit`   | integer | Number of results to return (1-100, default: 10) |

### Response Format

```json
{
  "data": [...],
  "pagination": {
    "limit": 10,
    "has_more": true,
    "next_cursor": "eyJ0aW1lc3RhbXAiOiIyMDI0LTA3LTAyVDE3OjMwOjAwLjAwMDAwMFoifQ=="
  }
}
```

### Example Usage

**First page:**

```bash
GET /v2/publications/pub_123/subscriptions?limit=10
```

**Next page:**

```bash
GET /v2/publications/pub_123/subscriptions?limit=10&cursor=eyJ0aW1lc3RhbXAiOiIyMDI0LTA3LTAyVDE3OjMwOjAwLjAwMDAwMFoifQ==
```

### Advantages

* **Consistent results**: No duplicates or missing items during pagination
* **Performance**: Efficient for large datasets
* **Real-time friendly**: Works well when data changes frequently
* **No deep pagination issues**: Maintains performance regardless of page depth

<Info>
  Cursor-based pagination is optimized for performance and does not include total counts. Use the `has_more` field to determine if additional pages exist.
</Info>

## Offset-Based Pagination (Deprecated)

<Warning>
  Offset-based pagination is deprecated and will be removed in a future API version. Please migrate to cursor-based pagination.
</Warning>

Offset-based pagination uses page numbers and limits. While still supported, it has several limitations:

* **Page limit**: Requests beyond page 100 are blocked
* **Consistency issues**: Results may shift when data changes
* **Performance degradation**: Slower for deep pagination

### Request Parameters

| Parameter | Type    | Description                                     |
| --------- | ------- | ----------------------------------------------- |
| `page`    | integer | Page number (1-100)                             |
| `limit`   | integer | Number of results per page (1-100, default: 10) |

### Response Format

```json
{
  "data": [...],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total_results": 1500,
    "total_pages": 150
  }
}
```

### Deprecation Timeline

* **Current**: All offset pagination requests return deprecation warning headers
* **After page 100**: Requests return a 400 error with migration guidance
* **Future**: Complete removal of offset pagination support

## Migration Guide

### Step 1: Update Your Code

Replace offset pagination parameters:

```diff
- GET /v2/publications/pub_123/subscriptions?page=1&limit=10
+ GET /v2/publications/pub_123/subscriptions?limit=10
```

### Step 2: Handle Response Changes

Update your response parsing:

```diff
// Old offset pagination
- if (response.pagination.page < response.pagination.total_pages) {
-   fetchNextPage(response.pagination.page + 1);
- }

// New cursor pagination
+ if (response.pagination.has_more) {
+   fetchNextPage(response.pagination.next_cursor);
+ }
```

### Step 3: Update Pagination Logic

```javascript
// Cursor-based pagination example
async function getAllSubscriptions(publicationId, limit = 10) {
  const allSubscriptions = [];
  let cursor = null;
  let hasMore = true;

  while (hasMore) {
    const params = new URLSearchParams({ limit: limit.toString() });
    if (cursor) {
      params.append('cursor', cursor);
    }

    const response = await fetch(
      `/v2/publications/${publicationId}/subscriptions?${params}`
    );
    const data = await response.json();

    allSubscriptions.push(...data.data);
    
    hasMore = data.pagination.has_more;
    cursor = data.pagination.next_cursor;
  }

  return allSubscriptions;
}
```

### Key Differences

| Feature           | Offset Pagination        | Cursor Pagination                    |
| ----------------- | ------------------------ | ------------------------------------ |
| **Page limit**    | 100 pages max            | Unlimited                            |
| **Performance**   | Degrades with depth      | Consistent                           |
| **Consistency**   | May have gaps/duplicates | Always consistent                    |
| **Total count**   | Always included          | Not included (performance optimized) |
| **Random access** | Yes (page number)        | No (sequential only)                 |

### Backward Compatibility

During the transition period:

* Both pagination methods are supported
* Offset requests include deprecation warning headers:
  * `X-Pagination-Warning`: Deprecation notice
  * `X-Pagination-Migration-Guide`: Link to this documentation
* Requests beyond page 100 return a 400 error

### Testing Your Migration

1. **Test cursor pagination**: Verify your code handles cursor tokens correctly
2. **Check error handling**: Ensure graceful handling of pagination errors
3. **Performance testing**: Compare performance of cursor vs offset pagination
4. **Monitor headers**: Watch for deprecation warnings in your logs

## Best Practices

### Cursor Pagination

* **Store cursors securely**: Treat cursor tokens as opaque strings
* **Handle missing cursors**: Start from the beginning if cursor is invalid
* **Use appropriate limits**: Balance between API calls and memory usage
* **Cache strategically**: Cache results but not cursor tokens

### Error Handling

```javascript
try {
  const response = await fetch(endpoint);
  
  if (response.status === 400) {
    // Handle pagination error (e.g., invalid cursor)
    console.error('Pagination error:', await response.json());
    // Restart from beginning
    return fetchFromBeginning();
  }
  
  return await response.json();
} catch (error) {
  console.error('Request failed:', error);
  throw error;
}
```

### Rate Limiting

Be mindful of rate limits when implementing pagination:

* **Respect rate limits**: Don't exceed API rate limits
* **Implement backoff**: Use exponential backoff for rate limit errors
* **Batch wisely**: Use appropriate page sizes to minimize requests

## Support

If you need help migrating to cursor-based pagination:

* Check our [API Reference](/api-reference) for endpoint-specific examples
* Review the [Rate Limiting](/welcome/rate-limiting) documentation
* Contact support if you encounter issues during migration


***

subtitle: >-
Prevent unexpected errors by instituting best rate limiting practices in your
application.
------------

The beehiiv API has a rate limit of **180 requests per minute** on a per-organization basis. This is to prevent abuse and ensure the stability of the API.

If you are making requests to the beehiiv API at a rate that exceeds the rate limit, you will receive a `429` (Too Many Requests) error.

To prevent this, we recommend implementing rate limiting and methods like exponential backoff to retry requests that fail due to rate limiting.

## Headers

Each response from the beehiiv API will include the following headers to assist you in your rate limiting implementation:

* `RateLimit-Limit`: The maximum number of requests that are allowed in the current period.
* `RateLimit-Remaining`: The number of requests remaining in the current period.
* `RateLimit-Reset`: The time (in [seconds since the Unix epoch](https://en.wikipedia.org/wiki/Unix_time)) at which the current period will reset.

## Implementation

To effectively implement rate limiting, we recommend instituting a queue system and leveraging [exponential backoff](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html).

Many programming languages and frameworks offer built-in support for queue systems. Some common examples include:

* [Amazon SQS](https://aws.amazon.com/sqs/) (All languages)
* [Upstash QStash](https://upstash.com/docs/qstash/overall/getstarted) (All languages)
* [Sidekiq](https://sidekiq.org/) (Ruby)
* [Goroutines](https://go.dev/tour/concurrency/1) (Go)
* [Laravel Queues](https://laravel.com/docs/12.x/queues) (PHP)
* [Trigger.dev](https://trigger.dev/) (JavaScript)
* [Celery](https://docs.celeryq.dev/) (Python)

Many no-code platforms such as [Zapier](https://zapier.com/apps/beehiiv/integrations) and [Make](https://www.make.com/en/integrations/beehiiv) automatically adhere to our rate limit.

## Example Implementation (JavaScript)

This is a basic example of how to implement rate limiting in your JavaScript code. More complex implementations can be implemented using one of the queue systems mentioned above or by using a library like [Bottleneck](https://github.com/SGrondin/bottleneck).

```javascript
const MAX_REQUESTS_PER_MINUTE = 180;
const MAX_CONCURRENT = 5;
// Beehiiv API: 180 requests / 60 seconds = 3 requests per second.
// 1000ms / 3 requests = ~333ms per request.
const MIN_TIME_BETWEEN_REQUESTS_MS = 350;

let requestQueue = [];
let activeRequestsCount = 0;
let requestTimestamps = [];

async function makeApiCall(endpoint, params) {
  console.log(`Making API call to: ${endpoint} with params:`, params);
  // Replace with your actual fetch/axios call
  // Ensure your actual API call function is asynchronous (returns a Promise)
  return fetch(`https://api.beehiiv.com/v2/${endpoint}`, {
    method: 'GET', // or 'POST', etc.
    headers: {
      'Authorization': 'Bearer YOUR_API_KEY', // Replace YOUR_API_KEY
      'Content-Type': 'application/json'
    },
    // body: JSON.stringify(params) // if it's a POST/PUT request
  })
  .then(response => {
    if (!response.ok) {
      if (response.status === 429) {
        console.warn('Rate limit hit (429). The custom rate limiter should ideally prevent this. Check logic or external factors.');
      }
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  });
}

function processRequestQueue() {
  if (requestQueue.length === 0) {
    return;
  }

  const now = Date.now();

  // 1. Prune old timestamps (older than 1 minute)
  requestTimestamps = requestTimestamps.filter(timestamp => now - timestamp < 60000);

  // 2. Check constraints
  if (activeRequestsCount >= MAX_CONCURRENT) {
    return;
  }

  if (requestTimestamps.length >= MAX_REQUESTS_PER_MINUTE) {
    console.log('Rate limit per minute reached. Waiting for window to reset...');
    const timeToWait = (requestTimestamps[0] + 60000) - now + 100;
    setTimeout(processRequestQueue, Math.max(0, timeToWait));
    return;
  }
  
  if (requestTimestamps.length > 0) {
      const lastDispatchedTime = requestTimestamps[requestTimestamps.length - 1];
      const timeSinceLastDispatched = now - lastDispatchedTime;
      if (timeSinceLastDispatched < MIN_TIME_BETWEEN_REQUESTS_MS) {
          const delay = MIN_TIME_BETWEEN_REQUESTS_MS - timeSinceLastDispatched;
          console.log(`Min time between requests. Waiting ${delay}ms...`);
          setTimeout(processRequestQueue, Math.max(0,delay));
          return;
      }
  }

  // 3. Dequeue and process the request
  const { fnToCall, resolve, reject, args } = requestQueue.shift();
  
  activeRequestsCount++;
  requestTimestamps.push(Date.now()); 

  fnToCall(...args)
    .then(resolve)
    .catch(reject)
    .finally(() => {
      activeRequestsCount--;
      setTimeout(processRequestQueue, 0); 
    });
}

function throttledApiCall(endpoint, params) {
  return new Promise((resolve, reject) => {
    requestQueue.push({ fnToCall: makeApiCall, resolve, reject, args: [endpoint, params] });
    setTimeout(processRequestQueue, 0); 
  });
}

// --- Example Usage ---
async function fetchAllPosts() {
  try {
    const postIds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 /* ... more ids ... */];
    console.log(`Attempting to fetch ${postIds.length} posts sequentially managed by rate limiter...`);
    
    const promises = postIds.map(id => {
      return throttledApiCall(`posts/${id}`)
        .then(post => {
          console.log(`Successfully fetched post ${id}:`, post.id);
          return post;
        })
        .catch(error => {
          console.error(`Failed to fetch post ${id}:`, error.message);
          throw error; 
        });
    });

    const results = await Promise.all(promises);
    console.log('All post fetch attempts completed.');
    console.log('Fetched posts data:', results);
    return results;
  } catch (error) {
    console.error('Error in fetchAllPosts orchestration:', error.message);
  }
}

// To use this:
// fetchAllPosts().then(() => console.log("fetchAllPosts example finished."));

// For debugging/monitoring, you can add more console logs within processRequestQueue or around the `activeRequestsCount` and `requestTimestamps` manipulations.
```

### How it Works:

* **Configuration**:
  * `MAX_REQUESTS_PER_MINUTE`: Set to 180, matching the beehiiv API limit.
  * `MAX_CONCURRENT`: Limits how many requests can be active simultaneously (e.g., 5). This prevents overwhelming the network or the server with too many connections at once, even if within the overall rate limit.
  * `MIN_TIME_BETWEEN_REQUESTS_MS`: Ensures a minimum delay between the start of each request (e.g., 350ms). This helps distribute requests more evenly and provides an additional safeguard against hitting the rate limit due to bursts.

* **State Management**:
  * `requestQueue`: An array that holds API calls waiting to be made. Each item in the queue is an object containing the function to call (`fnToCall`), its arguments (`args`), and the `resolve` and `reject` functions of the Promise returned by `throttledApiCall`.
  * `activeRequestsCount`: Tracks the number of currently in-flight API requests.
  * `requestTimestamps`: Stores the timestamps of when each request was dispatched. This array is used to ensure that no more than `MAX_REQUESTS_PER_MINUTE` are made within any rolling 60-second window.

* **`makeApiCall(endpoint, params)`**:
  * This is your actual function that performs the `fetch` request to the beehiiv API. You'll need to replace `'Bearer YOUR_API_KEY'` with your API key and customize the request as needed.

* **`throttledApiCall(endpoint, params)`**:
  * This function acts as a wrapper around your `makeApiCall`. When you want to make an API request in a rate-limited fashion, you call `throttledApiCall` instead of `makeApiCall` directly.
  * It adds your request details to the `requestQueue` and then triggers `processRequestQueue` (asynchronously via `setTimeout`) to attempt to process it.
  * It returns a Promise that will resolve or reject based on the outcome of the actual API call once it's processed.

* **`processRequestQueue()`**:
  * This is the core of the rate limiter. It's called to attempt to process the next request in the queue.
  * It first checks several conditions:
    1. If the `requestQueue` is empty, it does nothing.
    2. It prunes `requestTimestamps` to only keep those within the last 60 seconds.
    3. If `activeRequestsCount` is already at `MAX_CONCURRENT`, it returns, waiting for an active request to complete.
    4. If `requestTimestamps` indicates that `MAX_REQUESTS_PER_MINUTE` have been made in the last 60 seconds, it calculates the time needed to wait until the oldest request in the window expires and schedules `processRequestQueue` to run after that delay.
    5. It checks if the time since the last dispatched request is less than `MIN_TIME_BETWEEN_REQUESTS_MS`. If so, it schedules `processRequestQueue` to run after the necessary delay.
  * If none of the limiting conditions are met, it dequeues a request from `requestQueue`, increments `activeRequestsCount`, records the dispatch timestamp, and executes the API call (`fnToCall`).
  * When the API call's Promise settles (either resolves or rejects), the `finally` block decrements `activeRequestsCount` and calls `setTimeout(processRequestQueue, 0)` to ensure the queue processing continues for any subsequent requests.

* **Example Usage (`fetchAllPosts`)**:
  * This asynchronous function demonstrates how you might schedule multiple API calls using `throttledApiCall`. The rate limiter manages the queue and dispatches these calls according to the defined limits, preventing `429` errors.

This vanilla JavaScript approach helps prevent `429` errors by managing request flow. Remember to adjust `YOUR_API_KEY` and the API endpoints in the `makeApiCall` function.

<Info>
  This vanilla JavaScript example focuses on managing request rates within a single Node.js process, like running a script locally on your machine.

  It does not cover persistent storage of rate limit states (which would be needed if the application restarts) or distributed rate limiting across multiple instances. For those scenarios, or for handling very large queues robustly, you would typically integrate server-side queuing systems (like Amazon SQS or others mentioned above) often backed by stores like [Redis](https://redis.io/) or [Valkey](https://valkey.io/).
</Info>


***

## subtitle: Not a developer? Not a problem.

If you're wanting to work with the beehiiv API to integrate your publications with other software but don't have the time or resources to build an integration yourself, there's a few options available to you.

The beehiiv team currently maintains a [Zapier integration](https://zapier.com/apps/beehiiv/integrations) and a [Make integration](https://www.make.com/en/integrations/beehiiv). Both offer a no-code way to integrate your publication with other software.

## Zapier

Zapier is a platform that allows you to connect your publication to other software without having to write any code. You can use Zapier to receive real-time notifications when certain events occur on your publication, such as when a new subscriber signs up, or to make changes to your publication, such as adding a new subscriber from another service.

To get started, you'll need to [sign up for an account](https://zapier.com/sign-up), create a new "Zap", and search for "beehiiv" in the list of apps to connect to.

`Triggers` are how Zapier refers to webhooks. When you create a new Zap, you'll be able to select the type of event you want to trigger your Zap. `Actions` are how Zapier refers to the API calls that you want to make to the beehiiv API. Both follow similar patterns to the webhooks and API reference found elsewhere in this documentation, but are tailored to Zapier's UI and capabilities.

For more information on how to use Zapier, check out their [documentation](https://learn.zapier.com/).

## Make

Make is another platform that allows you to connect your publication to other software without having to write any code. You can also use Make to receive real-time notifications when certain events occur on your publication, such as when a new subscriber signs up, or to make changes to your publication, such as adding a new subscriber from another service.

To get started, you'll need to [sign up for an account](https://www.make.com/en/register), create a new "Scenario", and search for "beehiiv" in the list of apps to connect to.

To use webhooks with Make, please refer to our [webhooks documentation](/webhooks) for more information. For other actions, Make provides a UI for you to interact with the beehiiv API in a similar fashion to the API reference.

Compared to Zapier, Make offers additional functionality, such as easy-to-use functions for formatting and manipulating data in between steps.

For more information on how to use Make, check out their [documentation](https://www.make.com/en/help).

<Warning>
  The beehiiv support team only services Make and Zapier for no-code integrations. If you're using other no-code
  platforms, we may not be able to provide direct support for your integration.
</Warning>


***

subtitle: >-
An easy way to receive real-time notifications when certain events occur on
your beehiiv publication.
-------------------------

<Warning>
  Webhooks are currently only available for paid users on the Scale plan and above. To upgrade your account, click
  [here](https://app.beehiiv.com/settings/billing).
</Warning>

## Why use webhooks

Webhooks are a way to receive real-time notifications when certain events occur on your beehiiv publication. These can be helpful for:

* Integrating your publication with other services.
* Keeping track of your audience in third-party apps.
* And more.

## How to configure webhooks

Webhooks can be configured in two ways:

1. In the app: Navigate to `Settings > Integrations > Webhooks`.
2. Using the API: Send a `POST` request to the `/webhooks` endpoint (see [API reference](/api-reference/webhooks/post-webhooks)).

The event types are listed in the sidebar of this page and are organized by the resource they are associated with.

## Webhooks in Zapier and Make

The beehiiv team currently maintain a [Zapier integration](https://zapier.com/apps/beehiiv/integrations) and a [Make integration](https://www.make.com/en/integrations/beehiiv).

In Zapier, webhooks are known as "Triggers," which assist the user set up a webhook without having to set them up in the app as outlined above. In Make, users should use the [Custom Webhook](https://www.make.com/en/help/tools/webhooks) module and follow step 1 above to set up their webhook to point to the Make-provided URL.


# Post Sent

POST 

Reference: https://developers.beehiiv.com/webhooks/post/sent

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: webhooks
  version: 1.0.0
paths: {}
webhooks:
  sent:
    post:
      operationId: sent
      summary: Post Sent
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/type_post:Post'
components:
  schemas:
    type_post:PostStatus:
      type: string
      enum:
        - draft
        - confirmed
        - archived
      description: >-
        The status of the post.<br>`draft` - not been scheduled.<br>`confirmed`
        - The post will be active after the `scheduled_at`.<br>`archived` - The
        post is no longer active.
      title: PostStatus
    type_post:PostData:
      type: object
      properties:
        audience:
          type: string
          description: >-
            The audience that the post is available to on the web. Only
            applicable if the platform is `web` or `both`.
        authors:
          type: array
          items:
            type: string
          description: An array of author names
        content_tags:
          type: array
          items:
            type: string
          description: All content tags that were associated with the post.
        created:
          type: integer
          description: >-
            The time the post was created. Measured in seconds since the Unix
            epoch
        displayed_date:
          type: integer
          description: >-
            The time displayed in place of the `publish_date`. Measured in
            seconds since the Unix epoch
        id:
          type: string
          description: The prefixed post id
        preview_text:
          type: string
          description: The email preview text
        publish_date:
          type: integer
          description: >-
            The time the post was set to be published. Measured in seconds since
            the Unix epoch
        slug:
          type: string
          description: The web slug where this post can be accessed.
        split_tested:
          type: boolean
          description: >-
            A flag to indicate if a split test was done. Only applicable to
            email posts.
        status:
          $ref: '#/components/schemas/type_post:PostStatus'
          description: >-
            The status of the post.<br>`draft` - not been
            scheduled.<br>`confirmed` - The post will be active after the
            `scheduled_at`.<br>`archived` - The post is no longer active.
        subject_line:
          type: string
          description: >-
            The email subject line. In cases of A/B Testing, this will be
            adjusted to the winning subject line.
        subtitle:
          type: string
          description: The subtitle displayed in web views
        thumbnail_url:
          type: string
          description: >-
            The URL of the thumbnail. Defaults to the Publication logo if not
            set.
        title:
          type: string
          description: The title displayed in web views
        web_url:
          type: string
          description: >-
            The full URL where this post can be accessed on the web. Only
            applicable if the platform is `web` or `both`.
        platform:
          type: string
          description: The platform that the post is or will be published to.
        meta_default_description:
          type: string
          description: >-
            Meta tag description for the post, called SEO Description in the
            admin UI
        meta_default_title:
          type: string
          description: Meta tag title for the post, called SEO Title in the admin UI
        hidden_from_feed:
          type: boolean
          description: A flag to indicate if the post is hidden from the website feed.
        enforce_gated_content:
          type: boolean
          description: >-
            A flag to indicate if the post enforces gated content for
            non-subscribers.
        email_capture_popup:
          type: boolean
          description: A flag to indicate if popup email capture is enabled for this post.
      required:
        - audience
        - authors
        - content_tags
        - created
        - id
        - preview_text
        - slug
        - split_tested
        - status
        - subject_line
        - subtitle
        - thumbnail_url
        - title
        - platform
        - hidden_from_feed
        - enforce_gated_content
        - email_capture_popup
      title: PostData
    type_post:Post:
      type: object
      properties:
        uid:
          type: string
          description: The prefixed event ID, unique to each webhook event.
        event_timestamp:
          type: integer
          description: >-
            The date the event was created. Measured in seconds since the Unix
            epoch.
        event_type:
          type: string
          description: The event type.
        data:
          $ref: '#/components/schemas/type_post:PostData'
      title: Post

```

# Post Updated

POST 

Reference: https://developers.beehiiv.com/webhooks/post/updated

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: webhooks
  version: 1.0.0
paths: {}
webhooks:
  updated:
    post:
      operationId: updated
      summary: Post Updated
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/type_post:Post'
components:
  schemas:
    type_post:PostStatus:
      type: string
      enum:
        - draft
        - confirmed
        - archived
      description: >-
        The status of the post.<br>`draft` - not been scheduled.<br>`confirmed`
        - The post will be active after the `scheduled_at`.<br>`archived` - The
        post is no longer active.
      title: PostStatus
    type_post:PostData:
      type: object
      properties:
        audience:
          type: string
          description: >-
            The audience that the post is available to on the web. Only
            applicable if the platform is `web` or `both`.
        authors:
          type: array
          items:
            type: string
          description: An array of author names
        content_tags:
          type: array
          items:
            type: string
          description: All content tags that were associated with the post.
        created:
          type: integer
          description: >-
            The time the post was created. Measured in seconds since the Unix
            epoch
        displayed_date:
          type: integer
          description: >-
            The time displayed in place of the `publish_date`. Measured in
            seconds since the Unix epoch
        id:
          type: string
          description: The prefixed post id
        preview_text:
          type: string
          description: The email preview text
        publish_date:
          type: integer
          description: >-
            The time the post was set to be published. Measured in seconds since
            the Unix epoch
        slug:
          type: string
          description: The web slug where this post can be accessed.
        split_tested:
          type: boolean
          description: >-
            A flag to indicate if a split test was done. Only applicable to
            email posts.
        status:
          $ref: '#/components/schemas/type_post:PostStatus'
          description: >-
            The status of the post.<br>`draft` - not been
            scheduled.<br>`confirmed` - The post will be active after the
            `scheduled_at`.<br>`archived` - The post is no longer active.
        subject_line:
          type: string
          description: >-
            The email subject line. In cases of A/B Testing, this will be
            adjusted to the winning subject line.
        subtitle:
          type: string
          description: The subtitle displayed in web views
        thumbnail_url:
          type: string
          description: >-
            The URL of the thumbnail. Defaults to the Publication logo if not
            set.
        title:
          type: string
          description: The title displayed in web views
        web_url:
          type: string
          description: >-
            The full URL where this post can be accessed on the web. Only
            applicable if the platform is `web` or `both`.
        platform:
          type: string
          description: The platform that the post is or will be published to.
        meta_default_description:
          type: string
          description: >-
            Meta tag description for the post, called SEO Description in the
            admin UI
        meta_default_title:
          type: string
          description: Meta tag title for the post, called SEO Title in the admin UI
        hidden_from_feed:
          type: boolean
          description: A flag to indicate if the post is hidden from the website feed.
        enforce_gated_content:
          type: boolean
          description: >-
            A flag to indicate if the post enforces gated content for
            non-subscribers.
        email_capture_popup:
          type: boolean
          description: A flag to indicate if popup email capture is enabled for this post.
      required:
        - audience
        - authors
        - content_tags
        - created
        - id
        - preview_text
        - slug
        - split_tested
        - status
        - subject_line
        - subtitle
        - thumbnail_url
        - title
        - platform
        - hidden_from_feed
        - enforce_gated_content
        - email_capture_popup
      title: PostData
    type_post:Post:
      type: object
      properties:
        uid:
          type: string
          description: The prefixed event ID, unique to each webhook event.
        event_timestamp:
          type: integer
          description: >-
            The date the event was created. Measured in seconds since the Unix
            epoch.
        event_type:
          type: string
          description: The event type.
        data:
          $ref: '#/components/schemas/type_post:PostData'
      title: Post

```

# Subscription Created

POST 

Reference: https://developers.beehiiv.com/webhooks/subscription/created

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: webhooks
  version: 1.0.0
paths: {}
webhooks:
  created:
    post:
      operationId: created
      summary: Subscription Created
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/type_subscription:Subscription'
components:
  schemas:
    type_subscription:SubscriptionDataStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
      description: The status of the subscription.
      title: SubscriptionDataStatus
    type_subscription:CustomFieldKind:
      type: string
      enum:
        - string
        - integer
        - number
        - boolean
        - date
        - datetime
        - list
      description: The type of the custom field.
      title: CustomFieldKind
    type_subscription:CustomFieldValue:
      type: object
      properties:
        name:
          type: string
          description: The display name of the custom field.
        kind:
          $ref: '#/components/schemas/type_subscription:CustomFieldKind'
          description: The type of the custom field.
        value:
          type: string
          description: >-
            The formatted value of the custom field. The actual JSON type
            depends on the kind: - string: the value as a string - integer,
            number: the value as a number (JSON number type) - boolean: true or
            false (JSON boolean type) - date: formatted date string (e.g., "Jan
            15, 2024") - datetime: formatted date and time string (e.g., "Jan
            15, 2024 3:45 PM") - list: comma-separated values as a string
      required:
        - name
        - kind
      title: CustomFieldValue
    type_subscription:SubscriptionData:
      type: object
      properties:
        created:
          type: integer
          description: >-
            The time the subscription was created. Measured in seconds since the
            Unix epoch.
        email:
          type: string
          description: The email address of the subscription.
        id:
          type: string
          description: The prefixed ID of the subscription.
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        referring_site:
          type: string
          description: The website that the subscriber was referred from.
        status:
          $ref: '#/components/schemas/type_subscription:SubscriptionDataStatus'
          description: The status of the subscription.
        subscription_tier:
          type: string
          description: The tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: The names of the premium tiers associated with the subscription.
        stripe_customer_id:
          type: string
          description: The Stripe customer ID associated with the subscription.
        utm_campaign:
          type: string
          description: The acquisition campaign that the subscriber was acquired from.
        utm_channel:
          type: string
          description: The channel that the subscriber was acquired from.
        utm_medium:
          type: string
          description: The medium that the subscriber was acquired from.
        utm_source:
          type: string
          description: The source that the subscriber was acquired from.
        custom_fields:
          type: array
          items:
            $ref: '#/components/schemas/type_subscription:CustomFieldValue'
          description: >-
            An array of custom field values that have been set on the
            subscription. Each custom field value includes the field name, kind
            (type), and formatted value.
        tags:
          type: array
          items:
            type: string
          description: An array of tag names that have been applied to the subscription.
      title: SubscriptionData
    type_subscription:Subscription:
      type: object
      properties:
        uid:
          type: string
          description: The prefixed event ID, unique to each webhook event.
        event_timestamp:
          type: integer
          description: >-
            The date the event was created. Measured in seconds since the Unix
            epoch.
        event_type:
          type: string
          description: The event type.
        data:
          $ref: '#/components/schemas/type_subscription:SubscriptionData'
      title: Subscription

```

# Subscription Confirmed

POST 

Reference: https://developers.beehiiv.com/webhooks/subscription/confirmed

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: webhooks
  version: 1.0.0
paths: {}
webhooks:
  confirmed:
    post:
      operationId: confirmed
      summary: Subscription Confirmed
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/type_subscription:Subscription'
components:
  schemas:
    type_subscription:SubscriptionDataStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
      description: The status of the subscription.
      title: SubscriptionDataStatus
    type_subscription:CustomFieldKind:
      type: string
      enum:
        - string
        - integer
        - number
        - boolean
        - date
        - datetime
        - list
      description: The type of the custom field.
      title: CustomFieldKind
    type_subscription:CustomFieldValue:
      type: object
      properties:
        name:
          type: string
          description: The display name of the custom field.
        kind:
          $ref: '#/components/schemas/type_subscription:CustomFieldKind'
          description: The type of the custom field.
        value:
          type: string
          description: >-
            The formatted value of the custom field. The actual JSON type
            depends on the kind: - string: the value as a string - integer,
            number: the value as a number (JSON number type) - boolean: true or
            false (JSON boolean type) - date: formatted date string (e.g., "Jan
            15, 2024") - datetime: formatted date and time string (e.g., "Jan
            15, 2024 3:45 PM") - list: comma-separated values as a string
      required:
        - name
        - kind
      title: CustomFieldValue
    type_subscription:SubscriptionData:
      type: object
      properties:
        created:
          type: integer
          description: >-
            The time the subscription was created. Measured in seconds since the
            Unix epoch.
        email:
          type: string
          description: The email address of the subscription.
        id:
          type: string
          description: The prefixed ID of the subscription.
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        referring_site:
          type: string
          description: The website that the subscriber was referred from.
        status:
          $ref: '#/components/schemas/type_subscription:SubscriptionDataStatus'
          description: The status of the subscription.
        subscription_tier:
          type: string
          description: The tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: The names of the premium tiers associated with the subscription.
        stripe_customer_id:
          type: string
          description: The Stripe customer ID associated with the subscription.
        utm_campaign:
          type: string
          description: The acquisition campaign that the subscriber was acquired from.
        utm_channel:
          type: string
          description: The channel that the subscriber was acquired from.
        utm_medium:
          type: string
          description: The medium that the subscriber was acquired from.
        utm_source:
          type: string
          description: The source that the subscriber was acquired from.
        custom_fields:
          type: array
          items:
            $ref: '#/components/schemas/type_subscription:CustomFieldValue'
          description: >-
            An array of custom field values that have been set on the
            subscription. Each custom field value includes the field name, kind
            (type), and formatted value.
        tags:
          type: array
          items:
            type: string
          description: An array of tag names that have been applied to the subscription.
      title: SubscriptionData
    type_subscription:Subscription:
      type: object
      properties:
        uid:
          type: string
          description: The prefixed event ID, unique to each webhook event.
        event_timestamp:
          type: integer
          description: >-
            The date the event was created. Measured in seconds since the Unix
            epoch.
        event_type:
          type: string
          description: The event type.
        data:
          $ref: '#/components/schemas/type_subscription:SubscriptionData'
      title: Subscription

```

# Subscription Deleted

POST 

Reference: https://developers.beehiiv.com/webhooks/subscription/deleted

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: webhooks
  version: 1.0.0
paths: {}
webhooks:
  deleted:
    post:
      operationId: deleted
      summary: Subscription Deleted
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/type_subscription:Subscription'
components:
  schemas:
    type_subscription:SubscriptionDataStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
      description: The status of the subscription.
      title: SubscriptionDataStatus
    type_subscription:CustomFieldKind:
      type: string
      enum:
        - string
        - integer
        - number
        - boolean
        - date
        - datetime
        - list
      description: The type of the custom field.
      title: CustomFieldKind
    type_subscription:CustomFieldValue:
      type: object
      properties:
        name:
          type: string
          description: The display name of the custom field.
        kind:
          $ref: '#/components/schemas/type_subscription:CustomFieldKind'
          description: The type of the custom field.
        value:
          type: string
          description: >-
            The formatted value of the custom field. The actual JSON type
            depends on the kind: - string: the value as a string - integer,
            number: the value as a number (JSON number type) - boolean: true or
            false (JSON boolean type) - date: formatted date string (e.g., "Jan
            15, 2024") - datetime: formatted date and time string (e.g., "Jan
            15, 2024 3:45 PM") - list: comma-separated values as a string
      required:
        - name
        - kind
      title: CustomFieldValue
    type_subscription:SubscriptionData:
      type: object
      properties:
        created:
          type: integer
          description: >-
            The time the subscription was created. Measured in seconds since the
            Unix epoch.
        email:
          type: string
          description: The email address of the subscription.
        id:
          type: string
          description: The prefixed ID of the subscription.
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        referring_site:
          type: string
          description: The website that the subscriber was referred from.
        status:
          $ref: '#/components/schemas/type_subscription:SubscriptionDataStatus'
          description: The status of the subscription.
        subscription_tier:
          type: string
          description: The tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: The names of the premium tiers associated with the subscription.
        stripe_customer_id:
          type: string
          description: The Stripe customer ID associated with the subscription.
        utm_campaign:
          type: string
          description: The acquisition campaign that the subscriber was acquired from.
        utm_channel:
          type: string
          description: The channel that the subscriber was acquired from.
        utm_medium:
          type: string
          description: The medium that the subscriber was acquired from.
        utm_source:
          type: string
          description: The source that the subscriber was acquired from.
        custom_fields:
          type: array
          items:
            $ref: '#/components/schemas/type_subscription:CustomFieldValue'
          description: >-
            An array of custom field values that have been set on the
            subscription. Each custom field value includes the field name, kind
            (type), and formatted value.
        tags:
          type: array
          items:
            type: string
          description: An array of tag names that have been applied to the subscription.
      title: SubscriptionData
    type_subscription:Subscription:
      type: object
      properties:
        uid:
          type: string
          description: The prefixed event ID, unique to each webhook event.
        event_timestamp:
          type: integer
          description: >-
            The date the event was created. Measured in seconds since the Unix
            epoch.
        event_type:
          type: string
          description: The event type.
        data:
          $ref: '#/components/schemas/type_subscription:SubscriptionData'
      title: Subscription

```

# Subscription Upgraded

POST 

Reference: https://developers.beehiiv.com/webhooks/subscription/upgraded

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: webhooks
  version: 1.0.0
paths: {}
webhooks:
  upgraded:
    post:
      operationId: upgraded
      summary: Subscription Upgraded
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/type_subscription:Subscription'
components:
  schemas:
    type_subscription:SubscriptionDataStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
      description: The status of the subscription.
      title: SubscriptionDataStatus
    type_subscription:CustomFieldKind:
      type: string
      enum:
        - string
        - integer
        - number
        - boolean
        - date
        - datetime
        - list
      description: The type of the custom field.
      title: CustomFieldKind
    type_subscription:CustomFieldValue:
      type: object
      properties:
        name:
          type: string
          description: The display name of the custom field.
        kind:
          $ref: '#/components/schemas/type_subscription:CustomFieldKind'
          description: The type of the custom field.
        value:
          type: string
          description: >-
            The formatted value of the custom field. The actual JSON type
            depends on the kind: - string: the value as a string - integer,
            number: the value as a number (JSON number type) - boolean: true or
            false (JSON boolean type) - date: formatted date string (e.g., "Jan
            15, 2024") - datetime: formatted date and time string (e.g., "Jan
            15, 2024 3:45 PM") - list: comma-separated values as a string
      required:
        - name
        - kind
      title: CustomFieldValue
    type_subscription:SubscriptionData:
      type: object
      properties:
        created:
          type: integer
          description: >-
            The time the subscription was created. Measured in seconds since the
            Unix epoch.
        email:
          type: string
          description: The email address of the subscription.
        id:
          type: string
          description: The prefixed ID of the subscription.
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        referring_site:
          type: string
          description: The website that the subscriber was referred from.
        status:
          $ref: '#/components/schemas/type_subscription:SubscriptionDataStatus'
          description: The status of the subscription.
        subscription_tier:
          type: string
          description: The tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: The names of the premium tiers associated with the subscription.
        stripe_customer_id:
          type: string
          description: The Stripe customer ID associated with the subscription.
        utm_campaign:
          type: string
          description: The acquisition campaign that the subscriber was acquired from.
        utm_channel:
          type: string
          description: The channel that the subscriber was acquired from.
        utm_medium:
          type: string
          description: The medium that the subscriber was acquired from.
        utm_source:
          type: string
          description: The source that the subscriber was acquired from.
        custom_fields:
          type: array
          items:
            $ref: '#/components/schemas/type_subscription:CustomFieldValue'
          description: >-
            An array of custom field values that have been set on the
            subscription. Each custom field value includes the field name, kind
            (type), and formatted value.
        tags:
          type: array
          items:
            type: string
          description: An array of tag names that have been applied to the subscription.
      title: SubscriptionData
    type_subscription:Subscription:
      type: object
      properties:
        uid:
          type: string
          description: The prefixed event ID, unique to each webhook event.
        event_timestamp:
          type: integer
          description: >-
            The date the event was created. Measured in seconds since the Unix
            epoch.
        event_type:
          type: string
          description: The event type.
        data:
          $ref: '#/components/schemas/type_subscription:SubscriptionData'
      title: Subscription

```

# Subscription Downgraded

POST 

Reference: https://developers.beehiiv.com/webhooks/subscription/downgraded

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: webhooks
  version: 1.0.0
paths: {}
webhooks:
  downgraded:
    post:
      operationId: downgraded
      summary: Subscription Downgraded
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/type_subscription:Subscription'
components:
  schemas:
    type_subscription:SubscriptionDataStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
      description: The status of the subscription.
      title: SubscriptionDataStatus
    type_subscription:CustomFieldKind:
      type: string
      enum:
        - string
        - integer
        - number
        - boolean
        - date
        - datetime
        - list
      description: The type of the custom field.
      title: CustomFieldKind
    type_subscription:CustomFieldValue:
      type: object
      properties:
        name:
          type: string
          description: The display name of the custom field.
        kind:
          $ref: '#/components/schemas/type_subscription:CustomFieldKind'
          description: The type of the custom field.
        value:
          type: string
          description: >-
            The formatted value of the custom field. The actual JSON type
            depends on the kind: - string: the value as a string - integer,
            number: the value as a number (JSON number type) - boolean: true or
            false (JSON boolean type) - date: formatted date string (e.g., "Jan
            15, 2024") - datetime: formatted date and time string (e.g., "Jan
            15, 2024 3:45 PM") - list: comma-separated values as a string
      required:
        - name
        - kind
      title: CustomFieldValue
    type_subscription:SubscriptionData:
      type: object
      properties:
        created:
          type: integer
          description: >-
            The time the subscription was created. Measured in seconds since the
            Unix epoch.
        email:
          type: string
          description: The email address of the subscription.
        id:
          type: string
          description: The prefixed ID of the subscription.
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        referring_site:
          type: string
          description: The website that the subscriber was referred from.
        status:
          $ref: '#/components/schemas/type_subscription:SubscriptionDataStatus'
          description: The status of the subscription.
        subscription_tier:
          type: string
          description: The tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: The names of the premium tiers associated with the subscription.
        stripe_customer_id:
          type: string
          description: The Stripe customer ID associated with the subscription.
        utm_campaign:
          type: string
          description: The acquisition campaign that the subscriber was acquired from.
        utm_channel:
          type: string
          description: The channel that the subscriber was acquired from.
        utm_medium:
          type: string
          description: The medium that the subscriber was acquired from.
        utm_source:
          type: string
          description: The source that the subscriber was acquired from.
        custom_fields:
          type: array
          items:
            $ref: '#/components/schemas/type_subscription:CustomFieldValue'
          description: >-
            An array of custom field values that have been set on the
            subscription. Each custom field value includes the field name, kind
            (type), and formatted value.
        tags:
          type: array
          items:
            type: string
          description: An array of tag names that have been applied to the subscription.
      title: SubscriptionData
    type_subscription:Subscription:
      type: object
      properties:
        uid:
          type: string
          description: The prefixed event ID, unique to each webhook event.
        event_timestamp:
          type: integer
          description: >-
            The date the event was created. Measured in seconds since the Unix
            epoch.
        event_type:
          type: string
          description: The event type.
        data:
          $ref: '#/components/schemas/type_subscription:SubscriptionData'
      title: Subscription

```

# Subscription Paused

POST 

Reference: https://developers.beehiiv.com/webhooks/subscription/paused

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: webhooks
  version: 1.0.0
paths: {}
webhooks:
  paused:
    post:
      operationId: paused
      summary: Subscription Paused
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/type_subscription:Subscription'
components:
  schemas:
    type_subscription:SubscriptionDataStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
      description: The status of the subscription.
      title: SubscriptionDataStatus
    type_subscription:CustomFieldKind:
      type: string
      enum:
        - string
        - integer
        - number
        - boolean
        - date
        - datetime
        - list
      description: The type of the custom field.
      title: CustomFieldKind
    type_subscription:CustomFieldValue:
      type: object
      properties:
        name:
          type: string
          description: The display name of the custom field.
        kind:
          $ref: '#/components/schemas/type_subscription:CustomFieldKind'
          description: The type of the custom field.
        value:
          type: string
          description: >-
            The formatted value of the custom field. The actual JSON type
            depends on the kind: - string: the value as a string - integer,
            number: the value as a number (JSON number type) - boolean: true or
            false (JSON boolean type) - date: formatted date string (e.g., "Jan
            15, 2024") - datetime: formatted date and time string (e.g., "Jan
            15, 2024 3:45 PM") - list: comma-separated values as a string
      required:
        - name
        - kind
      title: CustomFieldValue
    type_subscription:SubscriptionData:
      type: object
      properties:
        created:
          type: integer
          description: >-
            The time the subscription was created. Measured in seconds since the
            Unix epoch.
        email:
          type: string
          description: The email address of the subscription.
        id:
          type: string
          description: The prefixed ID of the subscription.
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        referring_site:
          type: string
          description: The website that the subscriber was referred from.
        status:
          $ref: '#/components/schemas/type_subscription:SubscriptionDataStatus'
          description: The status of the subscription.
        subscription_tier:
          type: string
          description: The tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: The names of the premium tiers associated with the subscription.
        stripe_customer_id:
          type: string
          description: The Stripe customer ID associated with the subscription.
        utm_campaign:
          type: string
          description: The acquisition campaign that the subscriber was acquired from.
        utm_channel:
          type: string
          description: The channel that the subscriber was acquired from.
        utm_medium:
          type: string
          description: The medium that the subscriber was acquired from.
        utm_source:
          type: string
          description: The source that the subscriber was acquired from.
        custom_fields:
          type: array
          items:
            $ref: '#/components/schemas/type_subscription:CustomFieldValue'
          description: >-
            An array of custom field values that have been set on the
            subscription. Each custom field value includes the field name, kind
            (type), and formatted value.
        tags:
          type: array
          items:
            type: string
          description: An array of tag names that have been applied to the subscription.
      title: SubscriptionData
    type_subscription:Subscription:
      type: object
      properties:
        uid:
          type: string
          description: The prefixed event ID, unique to each webhook event.
        event_timestamp:
          type: integer
          description: >-
            The date the event was created. Measured in seconds since the Unix
            epoch.
        event_type:
          type: string
          description: The event type.
        data:
          $ref: '#/components/schemas/type_subscription:SubscriptionData'
      title: Subscription

```

# Subscription Resumed

POST 

Reference: https://developers.beehiiv.com/webhooks/subscription/resumed

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: webhooks
  version: 1.0.0
paths: {}
webhooks:
  resumed:
    post:
      operationId: resumed
      summary: Subscription Resumed
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/type_subscription:Subscription'
components:
  schemas:
    type_subscription:SubscriptionDataStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
      description: The status of the subscription.
      title: SubscriptionDataStatus
    type_subscription:CustomFieldKind:
      type: string
      enum:
        - string
        - integer
        - number
        - boolean
        - date
        - datetime
        - list
      description: The type of the custom field.
      title: CustomFieldKind
    type_subscription:CustomFieldValue:
      type: object
      properties:
        name:
          type: string
          description: The display name of the custom field.
        kind:
          $ref: '#/components/schemas/type_subscription:CustomFieldKind'
          description: The type of the custom field.
        value:
          type: string
          description: >-
            The formatted value of the custom field. The actual JSON type
            depends on the kind: - string: the value as a string - integer,
            number: the value as a number (JSON number type) - boolean: true or
            false (JSON boolean type) - date: formatted date string (e.g., "Jan
            15, 2024") - datetime: formatted date and time string (e.g., "Jan
            15, 2024 3:45 PM") - list: comma-separated values as a string
      required:
        - name
        - kind
      title: CustomFieldValue
    type_subscription:SubscriptionData:
      type: object
      properties:
        created:
          type: integer
          description: >-
            The time the subscription was created. Measured in seconds since the
            Unix epoch.
        email:
          type: string
          description: The email address of the subscription.
        id:
          type: string
          description: The prefixed ID of the subscription.
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        referring_site:
          type: string
          description: The website that the subscriber was referred from.
        status:
          $ref: '#/components/schemas/type_subscription:SubscriptionDataStatus'
          description: The status of the subscription.
        subscription_tier:
          type: string
          description: The tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: The names of the premium tiers associated with the subscription.
        stripe_customer_id:
          type: string
          description: The Stripe customer ID associated with the subscription.
        utm_campaign:
          type: string
          description: The acquisition campaign that the subscriber was acquired from.
        utm_channel:
          type: string
          description: The channel that the subscriber was acquired from.
        utm_medium:
          type: string
          description: The medium that the subscriber was acquired from.
        utm_source:
          type: string
          description: The source that the subscriber was acquired from.
        custom_fields:
          type: array
          items:
            $ref: '#/components/schemas/type_subscription:CustomFieldValue'
          description: >-
            An array of custom field values that have been set on the
            subscription. Each custom field value includes the field name, kind
            (type), and formatted value.
        tags:
          type: array
          items:
            type: string
          description: An array of tag names that have been applied to the subscription.
      title: SubscriptionData
    type_subscription:Subscription:
      type: object
      properties:
        uid:
          type: string
          description: The prefixed event ID, unique to each webhook event.
        event_timestamp:
          type: integer
          description: >-
            The date the event was created. Measured in seconds since the Unix
            epoch.
        event_type:
          type: string
          description: The event type.
        data:
          $ref: '#/components/schemas/type_subscription:SubscriptionData'
      title: Subscription

```

# Subscription Tier Paused

POST 

Reference: https://developers.beehiiv.com/webhooks/subscription/tier-paused

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: webhooks
  version: 1.0.0
paths: {}
webhooks:
  tier-paused:
    post:
      operationId: tier-paused
      summary: Subscription Tier Paused
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/type_subscription:Subscription'
components:
  schemas:
    type_subscription:SubscriptionDataStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
      description: The status of the subscription.
      title: SubscriptionDataStatus
    type_subscription:CustomFieldKind:
      type: string
      enum:
        - string
        - integer
        - number
        - boolean
        - date
        - datetime
        - list
      description: The type of the custom field.
      title: CustomFieldKind
    type_subscription:CustomFieldValue:
      type: object
      properties:
        name:
          type: string
          description: The display name of the custom field.
        kind:
          $ref: '#/components/schemas/type_subscription:CustomFieldKind'
          description: The type of the custom field.
        value:
          type: string
          description: >-
            The formatted value of the custom field. The actual JSON type
            depends on the kind: - string: the value as a string - integer,
            number: the value as a number (JSON number type) - boolean: true or
            false (JSON boolean type) - date: formatted date string (e.g., "Jan
            15, 2024") - datetime: formatted date and time string (e.g., "Jan
            15, 2024 3:45 PM") - list: comma-separated values as a string
      required:
        - name
        - kind
      title: CustomFieldValue
    type_subscription:SubscriptionData:
      type: object
      properties:
        created:
          type: integer
          description: >-
            The time the subscription was created. Measured in seconds since the
            Unix epoch.
        email:
          type: string
          description: The email address of the subscription.
        id:
          type: string
          description: The prefixed ID of the subscription.
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        referring_site:
          type: string
          description: The website that the subscriber was referred from.
        status:
          $ref: '#/components/schemas/type_subscription:SubscriptionDataStatus'
          description: The status of the subscription.
        subscription_tier:
          type: string
          description: The tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: The names of the premium tiers associated with the subscription.
        stripe_customer_id:
          type: string
          description: The Stripe customer ID associated with the subscription.
        utm_campaign:
          type: string
          description: The acquisition campaign that the subscriber was acquired from.
        utm_channel:
          type: string
          description: The channel that the subscriber was acquired from.
        utm_medium:
          type: string
          description: The medium that the subscriber was acquired from.
        utm_source:
          type: string
          description: The source that the subscriber was acquired from.
        custom_fields:
          type: array
          items:
            $ref: '#/components/schemas/type_subscription:CustomFieldValue'
          description: >-
            An array of custom field values that have been set on the
            subscription. Each custom field value includes the field name, kind
            (type), and formatted value.
        tags:
          type: array
          items:
            type: string
          description: An array of tag names that have been applied to the subscription.
      title: SubscriptionData
    type_subscription:Subscription:
      type: object
      properties:
        uid:
          type: string
          description: The prefixed event ID, unique to each webhook event.
        event_timestamp:
          type: integer
          description: >-
            The date the event was created. Measured in seconds since the Unix
            epoch.
        event_type:
          type: string
          description: The event type.
        data:
          $ref: '#/components/schemas/type_subscription:SubscriptionData'
      title: Subscription

```

# Subscription Tier Resumed

POST 

Reference: https://developers.beehiiv.com/webhooks/subscription/tier-resumed

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: webhooks
  version: 1.0.0
paths: {}
webhooks:
  tier-resumed:
    post:
      operationId: tier-resumed
      summary: Subscription Tier Resumed
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/type_subscription:Subscription'
components:
  schemas:
    type_subscription:SubscriptionDataStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
      description: The status of the subscription.
      title: SubscriptionDataStatus
    type_subscription:CustomFieldKind:
      type: string
      enum:
        - string
        - integer
        - number
        - boolean
        - date
        - datetime
        - list
      description: The type of the custom field.
      title: CustomFieldKind
    type_subscription:CustomFieldValue:
      type: object
      properties:
        name:
          type: string
          description: The display name of the custom field.
        kind:
          $ref: '#/components/schemas/type_subscription:CustomFieldKind'
          description: The type of the custom field.
        value:
          type: string
          description: >-
            The formatted value of the custom field. The actual JSON type
            depends on the kind: - string: the value as a string - integer,
            number: the value as a number (JSON number type) - boolean: true or
            false (JSON boolean type) - date: formatted date string (e.g., "Jan
            15, 2024") - datetime: formatted date and time string (e.g., "Jan
            15, 2024 3:45 PM") - list: comma-separated values as a string
      required:
        - name
        - kind
      title: CustomFieldValue
    type_subscription:SubscriptionData:
      type: object
      properties:
        created:
          type: integer
          description: >-
            The time the subscription was created. Measured in seconds since the
            Unix epoch.
        email:
          type: string
          description: The email address of the subscription.
        id:
          type: string
          description: The prefixed ID of the subscription.
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        referring_site:
          type: string
          description: The website that the subscriber was referred from.
        status:
          $ref: '#/components/schemas/type_subscription:SubscriptionDataStatus'
          description: The status of the subscription.
        subscription_tier:
          type: string
          description: The tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: The names of the premium tiers associated with the subscription.
        stripe_customer_id:
          type: string
          description: The Stripe customer ID associated with the subscription.
        utm_campaign:
          type: string
          description: The acquisition campaign that the subscriber was acquired from.
        utm_channel:
          type: string
          description: The channel that the subscriber was acquired from.
        utm_medium:
          type: string
          description: The medium that the subscriber was acquired from.
        utm_source:
          type: string
          description: The source that the subscriber was acquired from.
        custom_fields:
          type: array
          items:
            $ref: '#/components/schemas/type_subscription:CustomFieldValue'
          description: >-
            An array of custom field values that have been set on the
            subscription. Each custom field value includes the field name, kind
            (type), and formatted value.
        tags:
          type: array
          items:
            type: string
          description: An array of tag names that have been applied to the subscription.
      title: SubscriptionData
    type_subscription:Subscription:
      type: object
      properties:
        uid:
          type: string
          description: The prefixed event ID, unique to each webhook event.
        event_timestamp:
          type: integer
          description: >-
            The date the event was created. Measured in seconds since the Unix
            epoch.
        event_type:
          type: string
          description: The event type.
        data:
          $ref: '#/components/schemas/type_subscription:SubscriptionData'
      title: Subscription

```

# Subscription Tier Added

POST 

Reference: https://developers.beehiiv.com/webhooks/subscription/tier-added

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: webhooks
  version: 1.0.0
paths: {}
webhooks:
  tier-added:
    post:
      operationId: tier-added
      summary: Subscription Tier Added
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/type_subscription:Subscription'
components:
  schemas:
    type_subscription:SubscriptionDataStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
      description: The status of the subscription.
      title: SubscriptionDataStatus
    type_subscription:CustomFieldKind:
      type: string
      enum:
        - string
        - integer
        - number
        - boolean
        - date
        - datetime
        - list
      description: The type of the custom field.
      title: CustomFieldKind
    type_subscription:CustomFieldValue:
      type: object
      properties:
        name:
          type: string
          description: The display name of the custom field.
        kind:
          $ref: '#/components/schemas/type_subscription:CustomFieldKind'
          description: The type of the custom field.
        value:
          type: string
          description: >-
            The formatted value of the custom field. The actual JSON type
            depends on the kind: - string: the value as a string - integer,
            number: the value as a number (JSON number type) - boolean: true or
            false (JSON boolean type) - date: formatted date string (e.g., "Jan
            15, 2024") - datetime: formatted date and time string (e.g., "Jan
            15, 2024 3:45 PM") - list: comma-separated values as a string
      required:
        - name
        - kind
      title: CustomFieldValue
    type_subscription:SubscriptionData:
      type: object
      properties:
        created:
          type: integer
          description: >-
            The time the subscription was created. Measured in seconds since the
            Unix epoch.
        email:
          type: string
          description: The email address of the subscription.
        id:
          type: string
          description: The prefixed ID of the subscription.
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        referring_site:
          type: string
          description: The website that the subscriber was referred from.
        status:
          $ref: '#/components/schemas/type_subscription:SubscriptionDataStatus'
          description: The status of the subscription.
        subscription_tier:
          type: string
          description: The tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: The names of the premium tiers associated with the subscription.
        stripe_customer_id:
          type: string
          description: The Stripe customer ID associated with the subscription.
        utm_campaign:
          type: string
          description: The acquisition campaign that the subscriber was acquired from.
        utm_channel:
          type: string
          description: The channel that the subscriber was acquired from.
        utm_medium:
          type: string
          description: The medium that the subscriber was acquired from.
        utm_source:
          type: string
          description: The source that the subscriber was acquired from.
        custom_fields:
          type: array
          items:
            $ref: '#/components/schemas/type_subscription:CustomFieldValue'
          description: >-
            An array of custom field values that have been set on the
            subscription. Each custom field value includes the field name, kind
            (type), and formatted value.
        tags:
          type: array
          items:
            type: string
          description: An array of tag names that have been applied to the subscription.
      title: SubscriptionData
    type_subscription:Subscription:
      type: object
      properties:
        uid:
          type: string
          description: The prefixed event ID, unique to each webhook event.
        event_timestamp:
          type: integer
          description: >-
            The date the event was created. Measured in seconds since the Unix
            epoch.
        event_type:
          type: string
          description: The event type.
        data:
          $ref: '#/components/schemas/type_subscription:SubscriptionData'
      title: Subscription

```

# Subscription Tier Deleted

POST 

Reference: https://developers.beehiiv.com/webhooks/subscription/tier-deleted

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: webhooks
  version: 1.0.0
paths: {}
webhooks:
  tier-deleted:
    post:
      operationId: tier-deleted
      summary: Subscription Tier Deleted
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/type_subscription:Subscription'
components:
  schemas:
    type_subscription:SubscriptionDataStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
      description: The status of the subscription.
      title: SubscriptionDataStatus
    type_subscription:CustomFieldKind:
      type: string
      enum:
        - string
        - integer
        - number
        - boolean
        - date
        - datetime
        - list
      description: The type of the custom field.
      title: CustomFieldKind
    type_subscription:CustomFieldValue:
      type: object
      properties:
        name:
          type: string
          description: The display name of the custom field.
        kind:
          $ref: '#/components/schemas/type_subscription:CustomFieldKind'
          description: The type of the custom field.
        value:
          type: string
          description: >-
            The formatted value of the custom field. The actual JSON type
            depends on the kind: - string: the value as a string - integer,
            number: the value as a number (JSON number type) - boolean: true or
            false (JSON boolean type) - date: formatted date string (e.g., "Jan
            15, 2024") - datetime: formatted date and time string (e.g., "Jan
            15, 2024 3:45 PM") - list: comma-separated values as a string
      required:
        - name
        - kind
      title: CustomFieldValue
    type_subscription:SubscriptionData:
      type: object
      properties:
        created:
          type: integer
          description: >-
            The time the subscription was created. Measured in seconds since the
            Unix epoch.
        email:
          type: string
          description: The email address of the subscription.
        id:
          type: string
          description: The prefixed ID of the subscription.
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        referring_site:
          type: string
          description: The website that the subscriber was referred from.
        status:
          $ref: '#/components/schemas/type_subscription:SubscriptionDataStatus'
          description: The status of the subscription.
        subscription_tier:
          type: string
          description: The tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: The names of the premium tiers associated with the subscription.
        stripe_customer_id:
          type: string
          description: The Stripe customer ID associated with the subscription.
        utm_campaign:
          type: string
          description: The acquisition campaign that the subscriber was acquired from.
        utm_channel:
          type: string
          description: The channel that the subscriber was acquired from.
        utm_medium:
          type: string
          description: The medium that the subscriber was acquired from.
        utm_source:
          type: string
          description: The source that the subscriber was acquired from.
        custom_fields:
          type: array
          items:
            $ref: '#/components/schemas/type_subscription:CustomFieldValue'
          description: >-
            An array of custom field values that have been set on the
            subscription. Each custom field value includes the field name, kind
            (type), and formatted value.
        tags:
          type: array
          items:
            type: string
          description: An array of tag names that have been applied to the subscription.
      title: SubscriptionData
    type_subscription:Subscription:
      type: object
      properties:
        uid:
          type: string
          description: The prefixed event ID, unique to each webhook event.
        event_timestamp:
          type: integer
          description: >-
            The date the event was created. Measured in seconds since the Unix
            epoch.
        event_type:
          type: string
          description: The event type.
        data:
          $ref: '#/components/schemas/type_subscription:SubscriptionData'
      title: Subscription

```

# Survey Response Submitted

POST 

Reference: https://developers.beehiiv.com/webhooks/survey/submitted

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: webhooks
  version: 1.0.0
paths: {}
webhooks:
  submitted:
    post:
      operationId: submitted
      summary: Survey Response Submitted
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/type_survey:SurveyResponse'
components:
  schemas:
    type_survey:SurveyResponseQuestion:
      type: object
      properties:
        answer:
          type: string
          description: The answer provided to the question.
        prompt:
          type: string
          description: The question that was asked.
        type:
          type: string
          description: The type of question asked (e.g. multiple choice).
      title: SurveyResponseQuestion
    type_survey:SurveyResponseAnswer:
      type: object
      properties:
        answer:
          type: string
          description: The answer provided to the question.
        created:
          type: integer
          description: >-
            The time the answer was created. Measured in seconds since the Unix
            epoch.
        id:
          type: integer
          description: The ID of the answer.
        question_data:
          $ref: '#/components/schemas/type_survey:SurveyResponseQuestion'
        updated:
          type: integer
          description: >-
            The date the answer was updated. Measured in seconds since the Unix
            epoch.
      title: SurveyResponseAnswer
    type_subscription:SubscriptionDataStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
      description: The status of the subscription.
      title: SubscriptionDataStatus
    type_subscription:CustomFieldKind:
      type: string
      enum:
        - string
        - integer
        - number
        - boolean
        - date
        - datetime
        - list
      description: The type of the custom field.
      title: CustomFieldKind
    type_subscription:CustomFieldValue:
      type: object
      properties:
        name:
          type: string
          description: The display name of the custom field.
        kind:
          $ref: '#/components/schemas/type_subscription:CustomFieldKind'
          description: The type of the custom field.
        value:
          type: string
          description: >-
            The formatted value of the custom field. The actual JSON type
            depends on the kind: - string: the value as a string - integer,
            number: the value as a number (JSON number type) - boolean: true or
            false (JSON boolean type) - date: formatted date string (e.g., "Jan
            15, 2024") - datetime: formatted date and time string (e.g., "Jan
            15, 2024 3:45 PM") - list: comma-separated values as a string
      required:
        - name
        - kind
      title: CustomFieldValue
    type_subscription:SubscriptionData:
      type: object
      properties:
        created:
          type: integer
          description: >-
            The time the subscription was created. Measured in seconds since the
            Unix epoch.
        email:
          type: string
          description: The email address of the subscription.
        id:
          type: string
          description: The prefixed ID of the subscription.
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        referring_site:
          type: string
          description: The website that the subscriber was referred from.
        status:
          $ref: '#/components/schemas/type_subscription:SubscriptionDataStatus'
          description: The status of the subscription.
        subscription_tier:
          type: string
          description: The tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: The names of the premium tiers associated with the subscription.
        stripe_customer_id:
          type: string
          description: The Stripe customer ID associated with the subscription.
        utm_campaign:
          type: string
          description: The acquisition campaign that the subscriber was acquired from.
        utm_channel:
          type: string
          description: The channel that the subscriber was acquired from.
        utm_medium:
          type: string
          description: The medium that the subscriber was acquired from.
        utm_source:
          type: string
          description: The source that the subscriber was acquired from.
        custom_fields:
          type: array
          items:
            $ref: '#/components/schemas/type_subscription:CustomFieldValue'
          description: >-
            An array of custom field values that have been set on the
            subscription. Each custom field value includes the field name, kind
            (type), and formatted value.
        tags:
          type: array
          items:
            type: string
          description: An array of tag names that have been applied to the subscription.
      title: SubscriptionData
    type_survey:SurveyResponseData:
      type: object
      properties:
        answers:
          type: array
          items:
            $ref: '#/components/schemas/type_survey:SurveyResponseAnswer'
          description: An array of answers from the survey response.
        created:
          type: integer
          description: >-
            The time the survey response was created. Measured in seconds since
            the Unix epoch.
        id:
          type: string
          description: The response ID. This is unique to the individual submission.
        survey_id:
          type: string
          description: The ID of the survey that the response was submitted to.
        subscription:
          $ref: '#/components/schemas/type_subscription:SubscriptionData'
        updated:
          type: integer
          description: >-
            The date the survey response was updated. Measured in seconds since
            the Unix epoch.
      title: SurveyResponseData
    type_survey:SurveyResponse:
      type: object
      properties:
        uid:
          type: string
          description: The prefixed event ID, unique to each webhook event.
        event_timestamp:
          type: integer
          description: >-
            The date the event was created. Measured in seconds since the Unix
            epoch.
        event_type:
          type: string
          description: The event type.
        data:
          $ref: '#/components/schemas/type_survey:SurveyResponseData'
      title: SurveyResponse

```

***

## subtitle: Implement OAuth2 authorization code flow for beehiiv integrations.

<Warning>
  For more information about registering an OAuth client, contact [beehiiv Support](https://support.beehiiv.com/hc/en-us).
</Warning>

For integrations looking to integrate more seamlessly with beehiiv, the beehiiv API supports the standard OAuth2 authorization code flow.

OAuth2 endpoints are served under the `/oauth` namespace on the app domain (for example, `https://app.beehiiv.com/oauth/...`).

This guide will walk you through the steps to implement the OAuth2 authorization code flow for your integration.

## Authorization Code Flow

<Steps>
  ### Redirect the user to authorize your app

  Send users to `GET /oauth/authorize` with:

  * `client_id`
  * `redirect_uri`
  * `response_type=code`
  * `scope` (space-delimited)
  * `state` (recommended for CSRF protection)
  * `code_challenge` and `code_challenge_method` (recommended for public clients)

  Example:

  ```text
  https://app.beehiiv.com/oauth/authorize?client_id=WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc&redirect_uri=http%3A%2F%2Flocalhost%3A3008%2Fcallback&response_type=code&scope=posts%3Aread&state=12345678
  ```

  ### Receive an authorization code

  After login and consent, beehiiv redirects to your `redirect_uri` with:

  * `code`
  * `state` (if provided)

  ### Exchange the code for tokens

  Call `POST /oauth/token` with `application/x-www-form-urlencoded` body:

  * `grant_type=authorization_code`
  * `code`
  * `redirect_uri`
  * `client_id`
  * `client_secret` (confidential clients)
  * `code_verifier` (when using PKCE)

  The response contains `access_token`, `token_type`, `expires_in`, and `refresh_token` (when available).

  ### Call beehiiv APIs with the access token

  Use the token as a bearer token in API requests:

  ```text
  Authorization: Bearer <access_token>
  ```
</Steps>

## Refreshing tokens

Use `POST /oauth/token` with:

* `grant_type=refresh_token`
* `refresh_token`
* `client_id`
* `client_secret` (confidential clients)

## Token utilities

* `POST /oauth/revoke` revokes access or refresh tokens.
* `POST /oauth/introspect` checks token activity and metadata.
* `GET /oauth/token/info` returns metadata for the current bearer token.

## Available scopes

Each scope maps to a resource type (for example, `posts:*` scopes apply to posts endpoints).

Scope permission levels map to endpoint actions:

* `:read` permits read actions (for example, `GET` requests).
* `:write` is required for mutating actions (for example, `POST`, `PUT`, and `DELETE` requests).

Default scope:

* `identify:read`

Optional scopes:

* `automations:read`, `automations:write`
* `custom_fields:read`, `custom_fields:write`
* `subscriptions:read`, `subscriptions:write`
* `polls:read`, `polls:write`
* `posts:read`, `posts:write`
* `publications:read`, `publications:write`
* `referral_program:read`, `referral_program:write`
* `segments:read`, `segments:write`
* `tiers:read`, `tiers:write`
* `webhooks:read`, `webhooks:write`


# Authorize

GET https://app.beehiiv.com/oauth/authorize

Starts the OAuth2 authorization code flow. This endpoint redirects the user to login and consent (if needed), then redirects back to your `redirect_uri` with a `code` and `state`.

Reference: https://developers.beehiiv.com/oauth2/authorizations/authorize

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: oauth2
  version: 1.0.0
paths:
  /oauth/authorize:
    get:
      operationId: authorize
      summary: Authorize
      description: >-
        Starts the OAuth2 authorization code flow. This endpoint redirects the
        user to login and consent (if needed), then redirects back to your
        `redirect_uri` with a `code` and `state`.
      tags:
        - subpackage_authorizations
      parameters:
        - name: client_id
          in: query
          description: The OAuth application client ID (`uid`).
          required: true
          schema:
            type: string
        - name: redirect_uri
          in: query
          description: Must exactly match one of the app's configured redirect URIs.
          required: true
          schema:
            type: string
        - name: response_type
          in: query
          description: Must be `code` for the authorization code flow.
          required: true
          schema:
            type: string
        - name: scope
          in: query
          description: Space-delimited list of requested scopes.
          required: false
          schema:
            type: string
        - name: state
          in: query
          description: Opaque value returned to your callback for CSRF protection.
          required: false
          schema:
            type: string
        - name: code_challenge
          in: query
          description: PKCE code challenge for public clients.
          required: false
          schema:
            type: string
        - name: code_challenge_method
          in: query
          description: PKCE challenge method (`plain` or `S256`).
          required: false
          schema:
            $ref: '#/components/schemas/type_:CodeChallengeMethod'
      responses:
        '302':
          description: Redirect
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:EmptyResponse'
        '400':
          description: The request is invalid or missing required parameters.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:OAuthError'
        '401':
          description: Client authentication failed or the token is invalid.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:OAuthError'
servers:
  - url: https://app.beehiiv.com
components:
  schemas:
    type_:CodeChallengeMethod:
      type: string
      enum:
        - plain
        - S256
      description: The PKCE code challenge method.
      title: CodeChallengeMethod
    type_:EmptyResponse:
      type: object
      properties: {}
      title: EmptyResponse
    type_:OAuthError:
      type: object
      properties:
        error:
          type: string
        error_description:
          type: string
        error_uri:
          type: string
        state:
          type: string
      required:
        - error
      description: Standard OAuth2 error response.
      title: OAuthError

```

# Create token

POST https://app.beehiiv.com/oauth/token
Content-Type: application/json

Exchanges an authorization code for an access token, or exchanges a refresh token for a new access token. Send parameters as application/x-www-form-urlencoded.

Reference: https://developers.beehiiv.com/oauth2/tokens/token

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: oauth2
  version: 1.0.0
paths:
  /oauth/token:
    post:
      operationId: token
      summary: Create token
      description: >-
        Exchanges an authorization code for an access token, or exchanges a
        refresh token for a new access token. Send parameters as
        application/x-www-form-urlencoded.
      tags:
        - subpackage_tokens
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:TokenResponse'
        '400':
          description: The request is invalid or missing required parameters.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:OAuthError'
        '401':
          description: Client authentication failed or the token is invalid.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:OAuthError'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                grant_type:
                  $ref: '#/components/schemas/type_:GrantType'
                  description: authorization_code or refresh_token.
                code:
                  type: string
                  description: Authorization code returned from /oauth/authorize.
                redirect_uri:
                  type: string
                  description: >-
                    Must match the redirect URI used in the authorization
                    request.
                client_id:
                  type: string
                  description: OAuth application client ID (uid).
                client_secret:
                  type: string
                  description: Required for confidential clients.
                refresh_token:
                  type: string
                  description: Refresh token returned from a previous token exchange.
                code_verifier:
                  type: string
                  description: >-
                    PKCE code verifier (required when a code challenge was
                    sent).
              required:
                - grant_type
servers:
  - url: https://app.beehiiv.com
components:
  schemas:
    type_:GrantType:
      type: string
      enum:
        - authorization_code
        - refresh_token
      description: The OAuth2 grant type.
      title: GrantType
    type_:TokenType:
      type: string
      enum:
        - Bearer
      description: The token type returned by OAuth2 token endpoints.
      title: TokenType
    type_:TokenResponse:
      type: object
      properties:
        access_token:
          type: string
        token_type:
          $ref: '#/components/schemas/type_:TokenType'
        expires_in:
          type: integer
        refresh_token:
          type: string
        scope:
          type: string
        created_at:
          type: integer
      required:
        - access_token
        - token_type
        - expires_in
        - created_at
      description: Access token response from `/oauth/token`.
      title: TokenResponse
    type_:OAuthError:
      type: object
      properties:
        error:
          type: string
        error_description:
          type: string
        error_uri:
          type: string
        state:
          type: string
      required:
        - error
      description: Standard OAuth2 error response.
      title: OAuthError

```

## SDK Code Examples

```python Exchange authorization code
import requests

url = "https://app.beehiiv.com/oauth/token"

payload = {
    "grant_type": "authorization_code",
    "code": "SplxlOBeZQQYbYS6WxSbIA",
    "redirect_uri": "http://localhost:3008/callback",
    "client_id": "WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc",
    "client_secret": "your-client-secret"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript Exchange authorization code
const url = 'https://app.beehiiv.com/oauth/token';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"grant_type":"authorization_code","code":"SplxlOBeZQQYbYS6WxSbIA","redirect_uri":"http://localhost:3008/callback","client_id":"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc","client_secret":"your-client-secret"}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Exchange authorization code
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://app.beehiiv.com/oauth/token"

	payload := strings.NewReader("{\n  \"grant_type\": \"authorization_code\",\n  \"code\": \"SplxlOBeZQQYbYS6WxSbIA\",\n  \"redirect_uri\": \"http://localhost:3008/callback\",\n  \"client_id\": \"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc\",\n  \"client_secret\": \"your-client-secret\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Exchange authorization code
require 'uri'
require 'net/http'

url = URI("https://app.beehiiv.com/oauth/token")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"grant_type\": \"authorization_code\",\n  \"code\": \"SplxlOBeZQQYbYS6WxSbIA\",\n  \"redirect_uri\": \"http://localhost:3008/callback\",\n  \"client_id\": \"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc\",\n  \"client_secret\": \"your-client-secret\"\n}"

response = http.request(request)
puts response.read_body
```

```java Exchange authorization code
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://app.beehiiv.com/oauth/token")
  .header("Content-Type", "application/json")
  .body("{\n  \"grant_type\": \"authorization_code\",\n  \"code\": \"SplxlOBeZQQYbYS6WxSbIA\",\n  \"redirect_uri\": \"http://localhost:3008/callback\",\n  \"client_id\": \"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc\",\n  \"client_secret\": \"your-client-secret\"\n}")
  .asString();
```

```php Exchange authorization code
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://app.beehiiv.com/oauth/token', [
  'body' => '{
  "grant_type": "authorization_code",
  "code": "SplxlOBeZQQYbYS6WxSbIA",
  "redirect_uri": "http://localhost:3008/callback",
  "client_id": "WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc",
  "client_secret": "your-client-secret"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp Exchange authorization code
using RestSharp;

var client = new RestClient("https://app.beehiiv.com/oauth/token");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"grant_type\": \"authorization_code\",\n  \"code\": \"SplxlOBeZQQYbYS6WxSbIA\",\n  \"redirect_uri\": \"http://localhost:3008/callback\",\n  \"client_id\": \"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc\",\n  \"client_secret\": \"your-client-secret\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Exchange authorization code
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "grant_type": "authorization_code",
  "code": "SplxlOBeZQQYbYS6WxSbIA",
  "redirect_uri": "http://localhost:3008/callback",
  "client_id": "WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc",
  "client_secret": "your-client-secret"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://app.beehiiv.com/oauth/token")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

```python Refresh access token
import requests

url = "https://app.beehiiv.com/oauth/token"

payload = {
    "grant_type": "refresh_token",
    "client_id": "WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc",
    "client_secret": "your-client-secret",
    "refresh_token": "tGzv3JOkF0XG5Qx2TlKWIA"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript Refresh access token
const url = 'https://app.beehiiv.com/oauth/token';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"grant_type":"refresh_token","client_id":"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc","client_secret":"your-client-secret","refresh_token":"tGzv3JOkF0XG5Qx2TlKWIA"}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Refresh access token
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://app.beehiiv.com/oauth/token"

	payload := strings.NewReader("{\n  \"grant_type\": \"refresh_token\",\n  \"client_id\": \"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc\",\n  \"client_secret\": \"your-client-secret\",\n  \"refresh_token\": \"tGzv3JOkF0XG5Qx2TlKWIA\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Refresh access token
require 'uri'
require 'net/http'

url = URI("https://app.beehiiv.com/oauth/token")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"grant_type\": \"refresh_token\",\n  \"client_id\": \"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc\",\n  \"client_secret\": \"your-client-secret\",\n  \"refresh_token\": \"tGzv3JOkF0XG5Qx2TlKWIA\"\n}"

response = http.request(request)
puts response.read_body
```

```java Refresh access token
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://app.beehiiv.com/oauth/token")
  .header("Content-Type", "application/json")
  .body("{\n  \"grant_type\": \"refresh_token\",\n  \"client_id\": \"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc\",\n  \"client_secret\": \"your-client-secret\",\n  \"refresh_token\": \"tGzv3JOkF0XG5Qx2TlKWIA\"\n}")
  .asString();
```

```php Refresh access token
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://app.beehiiv.com/oauth/token', [
  'body' => '{
  "grant_type": "refresh_token",
  "client_id": "WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc",
  "client_secret": "your-client-secret",
  "refresh_token": "tGzv3JOkF0XG5Qx2TlKWIA"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp Refresh access token
using RestSharp;

var client = new RestClient("https://app.beehiiv.com/oauth/token");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"grant_type\": \"refresh_token\",\n  \"client_id\": \"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc\",\n  \"client_secret\": \"your-client-secret\",\n  \"refresh_token\": \"tGzv3JOkF0XG5Qx2TlKWIA\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Refresh access token
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "grant_type": "refresh_token",
  "client_id": "WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc",
  "client_secret": "your-client-secret",
  "refresh_token": "tGzv3JOkF0XG5Qx2TlKWIA"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://app.beehiiv.com/oauth/token")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Revoke token

POST https://app.beehiiv.com/oauth/revoke
Content-Type: application/json

Revokes an access token or refresh token. Send parameters as `application/x-www-form-urlencoded`.

Reference: https://developers.beehiiv.com/oauth2/tokens/revoke

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: oauth2
  version: 1.0.0
paths:
  /oauth/revoke:
    post:
      operationId: revoke
      summary: Revoke token
      description: >-
        Revokes an access token or refresh token. Send parameters as
        `application/x-www-form-urlencoded`.
      tags:
        - subpackage_tokens
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:EmptyResponse'
        '401':
          description: Client authentication failed or the token is invalid.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:OAuthError'
        '403':
          description: >-
            The authenticated client or token is not allowed to perform this
            action.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:OAuthError'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                token:
                  type: string
                  description: The access or refresh token to revoke.
                token_type_hint:
                  $ref: '#/components/schemas/type_:TokenTypeHint'
                  description: Optional hint to help the server process the token faster.
                client_id:
                  type: string
                  description: OAuth application client ID (`uid`).
                client_secret:
                  type: string
                  description: Required for confidential clients.
              required:
                - token
servers:
  - url: https://app.beehiiv.com
components:
  schemas:
    type_:TokenTypeHint:
      type: string
      enum:
        - access_token
        - refresh_token
      description: A hint about the type of token being sent.
      title: TokenTypeHint
    type_:EmptyResponse:
      type: object
      properties: {}
      title: EmptyResponse
    type_:OAuthError:
      type: object
      properties:
        error:
          type: string
        error_description:
          type: string
        error_uri:
          type: string
        state:
          type: string
      required:
        - error
      description: Standard OAuth2 error response.
      title: OAuthError

```

## SDK Code Examples

```python
import requests

url = "https://app.beehiiv.com/oauth/revoke"

payload = {
    "token": "2YotnFZFEjr1zCsicMWpAA",
    "token_type_hint": "access_token",
    "client_id": "WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc",
    "client_secret": "your-client-secret"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://app.beehiiv.com/oauth/revoke';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"token":"2YotnFZFEjr1zCsicMWpAA","token_type_hint":"access_token","client_id":"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc","client_secret":"your-client-secret"}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://app.beehiiv.com/oauth/revoke"

	payload := strings.NewReader("{\n  \"token\": \"2YotnFZFEjr1zCsicMWpAA\",\n  \"token_type_hint\": \"access_token\",\n  \"client_id\": \"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc\",\n  \"client_secret\": \"your-client-secret\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://app.beehiiv.com/oauth/revoke")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"token\": \"2YotnFZFEjr1zCsicMWpAA\",\n  \"token_type_hint\": \"access_token\",\n  \"client_id\": \"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc\",\n  \"client_secret\": \"your-client-secret\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://app.beehiiv.com/oauth/revoke")
  .header("Content-Type", "application/json")
  .body("{\n  \"token\": \"2YotnFZFEjr1zCsicMWpAA\",\n  \"token_type_hint\": \"access_token\",\n  \"client_id\": \"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc\",\n  \"client_secret\": \"your-client-secret\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://app.beehiiv.com/oauth/revoke', [
  'body' => '{
  "token": "2YotnFZFEjr1zCsicMWpAA",
  "token_type_hint": "access_token",
  "client_id": "WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc",
  "client_secret": "your-client-secret"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://app.beehiiv.com/oauth/revoke");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"token\": \"2YotnFZFEjr1zCsicMWpAA\",\n  \"token_type_hint\": \"access_token\",\n  \"client_id\": \"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc\",\n  \"client_secret\": \"your-client-secret\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "token": "2YotnFZFEjr1zCsicMWpAA",
  "token_type_hint": "access_token",
  "client_id": "WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc",
  "client_secret": "your-client-secret"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://app.beehiiv.com/oauth/revoke")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Introspect token

POST https://app.beehiiv.com/oauth/introspect
Content-Type: application/json

Returns whether a token is active and metadata about the token. Send parameters as `application/x-www-form-urlencoded`.

Reference: https://developers.beehiiv.com/oauth2/tokens/introspect

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: oauth2
  version: 1.0.0
paths:
  /oauth/introspect:
    post:
      operationId: introspect
      summary: Introspect token
      description: >-
        Returns whether a token is active and metadata about the token. Send
        parameters as `application/x-www-form-urlencoded`.
      tags:
        - subpackage_tokens
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:IntrospectionResponse'
        '400':
          description: The request is invalid or missing required parameters.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:OAuthError'
        '401':
          description: Client authentication failed or the token is invalid.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:OAuthError'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                token:
                  type: string
                  description: The access or refresh token to introspect.
                token_type_hint:
                  $ref: '#/components/schemas/type_:TokenTypeHint'
                  description: Optional hint to help the server process the token faster.
                client_id:
                  type: string
                  description: OAuth application client ID (`uid`).
                client_secret:
                  type: string
                  description: Required for confidential clients.
              required:
                - token
servers:
  - url: https://app.beehiiv.com
components:
  schemas:
    type_:TokenTypeHint:
      type: string
      enum:
        - access_token
        - refresh_token
      description: A hint about the type of token being sent.
      title: TokenTypeHint
    type_:TokenType:
      type: string
      enum:
        - Bearer
      description: The token type returned by OAuth2 token endpoints.
      title: TokenType
    type_:IntrospectionResponse:
      type: object
      properties:
        active:
          type: boolean
        scope:
          type: string
        client_id:
          type: string
        token_type:
          $ref: '#/components/schemas/type_:TokenType'
        exp:
          type: integer
        iat:
          type: integer
        nbf:
          type: integer
        sub:
          type: string
        aud:
          type: string
        iss:
          type: string
        jti:
          type: string
      required:
        - active
      description: RFC 7662 token introspection response.
      title: IntrospectionResponse
    type_:OAuthError:
      type: object
      properties:
        error:
          type: string
        error_description:
          type: string
        error_uri:
          type: string
        state:
          type: string
      required:
        - error
      description: Standard OAuth2 error response.
      title: OAuthError

```

## SDK Code Examples

```python
import requests

url = "https://app.beehiiv.com/oauth/introspect"

payload = {
    "token": "2YotnFZFEjr1zCsicMWpAA",
    "token_type_hint": "access_token",
    "client_id": "WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc",
    "client_secret": "your-client-secret"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://app.beehiiv.com/oauth/introspect';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"token":"2YotnFZFEjr1zCsicMWpAA","token_type_hint":"access_token","client_id":"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc","client_secret":"your-client-secret"}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://app.beehiiv.com/oauth/introspect"

	payload := strings.NewReader("{\n  \"token\": \"2YotnFZFEjr1zCsicMWpAA\",\n  \"token_type_hint\": \"access_token\",\n  \"client_id\": \"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc\",\n  \"client_secret\": \"your-client-secret\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://app.beehiiv.com/oauth/introspect")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"token\": \"2YotnFZFEjr1zCsicMWpAA\",\n  \"token_type_hint\": \"access_token\",\n  \"client_id\": \"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc\",\n  \"client_secret\": \"your-client-secret\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://app.beehiiv.com/oauth/introspect")
  .header("Content-Type", "application/json")
  .body("{\n  \"token\": \"2YotnFZFEjr1zCsicMWpAA\",\n  \"token_type_hint\": \"access_token\",\n  \"client_id\": \"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc\",\n  \"client_secret\": \"your-client-secret\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://app.beehiiv.com/oauth/introspect', [
  'body' => '{
  "token": "2YotnFZFEjr1zCsicMWpAA",
  "token_type_hint": "access_token",
  "client_id": "WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc",
  "client_secret": "your-client-secret"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://app.beehiiv.com/oauth/introspect");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"token\": \"2YotnFZFEjr1zCsicMWpAA\",\n  \"token_type_hint\": \"access_token\",\n  \"client_id\": \"WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc\",\n  \"client_secret\": \"your-client-secret\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "token": "2YotnFZFEjr1zCsicMWpAA",
  "token_type_hint": "access_token",
  "client_id": "WDgKDt_bHOXUfWRhGf2ovKZmFHQ9r_Erd01IPmz_boc",
  "client_secret": "your-client-secret"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://app.beehiiv.com/oauth/introspect")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get token info

GET https://app.beehiiv.com/oauth/token/info

Returns metadata for the current access token.

Reference: https://developers.beehiiv.com/oauth2/tokens/token-info

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: oauth2
  version: 1.0.0
paths:
  /oauth/token/info:
    get:
      operationId: token-info
      summary: Get token info
      description: Returns metadata for the current access token.
      tags:
        - subpackage_tokens
      parameters:
        - name: Authorization
          in: header
          description: Bearer access token (`Bearer <access_token>`).
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:TokenInfoResponse'
        '401':
          description: Client authentication failed or the token is invalid.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:OAuthError'
servers:
  - url: https://app.beehiiv.com
components:
  schemas:
    type_:TokenApplication:
      type: object
      properties:
        uid:
          type: string
        name:
          type: string
      description: OAuth application metadata attached to token info responses.
      title: TokenApplication
    type_:TokenInfoResponse:
      type: object
      properties:
        resource_owner_id:
          type: string
        scope:
          type: string
        expires_in_seconds:
          type: integer
        application:
          $ref: '#/components/schemas/type_:TokenApplication'
        created_at:
          type: integer
      description: Metadata for the current access token.
      title: TokenInfoResponse
    type_:OAuthError:
      type: object
      properties:
        error:
          type: string
        error_description:
          type: string
        error_uri:
          type: string
        state:
          type: string
      required:
        - error
      description: Standard OAuth2 error response.
      title: OAuthError

```

## SDK Code Examples

```python
import requests

url = "https://app.beehiiv.com/oauth/token/info"

headers = {"Authorization": "Bearer 2YotnFZFEjr1zCsicMWpAA"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://app.beehiiv.com/oauth/token/info';
const options = {method: 'GET', headers: {Authorization: 'Bearer 2YotnFZFEjr1zCsicMWpAA'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://app.beehiiv.com/oauth/token/info"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer 2YotnFZFEjr1zCsicMWpAA")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://app.beehiiv.com/oauth/token/info")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer 2YotnFZFEjr1zCsicMWpAA'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://app.beehiiv.com/oauth/token/info")
  .header("Authorization", "Bearer 2YotnFZFEjr1zCsicMWpAA")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://app.beehiiv.com/oauth/token/info', [
  'headers' => [
    'Authorization' => 'Bearer 2YotnFZFEjr1zCsicMWpAA',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://app.beehiiv.com/oauth/token/info");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer 2YotnFZFEjr1zCsicMWpAA");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer 2YotnFZFEjr1zCsicMWpAA"]

let request = NSMutableURLRequest(url: NSURL(string: "https://app.beehiiv.com/oauth/token/info")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get advertisement opportunities <Badge intent="info" minimal outlined>OAuth Scope: posts:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/advertisement_opportunities

Retrieve a list of accepted advertisement opportunities for the publication.

Reference: https://developers.beehiiv.com/api-reference/advertisement-opportunities/index

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/advertisement_opportunities:
    get:
      operationId: index
      summary: >-
        Get advertisement opportunities <Badge intent="info" minimal
        outlined>OAuth Scope: posts:read</Badge>
      description: >-
        Retrieve a list of accepted advertisement opportunities for the
        publication.
      tags:
        - subpackage_advertisement_opportunities
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_advertisement_opportunities:AdvertisementOpportunitiesGetResponse
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_advertisement_opportunities:AdvertisementOpportunity:
      type: object
      properties:
        id:
          type: string
          description: The ID of the opportunity.
        advertiser_name:
          type: string
          description: The name of the advertiser.
        payout_rate:
          type: string
          description: The amount you'll earn.
        advertisement_kind:
          type: string
          description: What kind of an ad it is. With or without logo.
        send_by_window_start_at:
          type: integer
          description: >-
            The earliest this ad can be sent. Measured in seconds since the Unix
            epoch.
        send_by_window_end_at:
          type: integer
          description: >-
            When this ad needs to be sent by. Measured in seconds since the Unix
            epoch.
      required:
        - id
        - advertiser_name
        - payout_rate
        - advertisement_kind
        - send_by_window_start_at
        - send_by_window_end_at
      title: AdvertisementOpportunity
    type_advertisement_opportunities:AdvertisementOpportunitiesGetResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_advertisement_opportunities:AdvertisementOpportunity
          description: A list of post templates available for this publication.
        total_results:
          type: integer
          description: The total number of results from all pages.
      required:
        - data
        - total_results
      title: AdvertisementOpportunitiesGetResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/advertisement_opportunities"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/advertisement_opportunities';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/advertisement_opportunities"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/advertisement_opportunities")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/advertisement_opportunities")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/advertisement_opportunities', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/advertisement_opportunities");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/advertisement_opportunities")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# List authors

GET https://api.beehiiv.com/v2/publications/{publicationId}/authors

Retrieve a list of authors available for the publication.

Reference: https://developers.beehiiv.com/api-reference/authors/index

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/authors:
    get:
      operationId: index
      summary: List authors
      description: Retrieve a list of authors available for the publication.
      tags:
        - subpackage_authors
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: limit
          in: query
          description: >-
            A limit on the number of objects to be returned. The limit can range
            between 1 and 100, and the default is 10.
          required: false
          schema:
            type: integer
        - name: page
          in: query
          description: >-
            Pagination returns the results in pages. Each page contains the
            number of results specified by the `limit` (default: 10).<br>If not
            specified, results 1-10 from page 1 will be returned.
          required: false
          schema:
            type: integer
        - name: name
          in: query
          description: >-
            Optionally filter authors by full name or first name
            (case-insensitive).
          required: false
          schema:
            type: string
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_authors:AuthorsListResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_authors:AuthorType:
      type: string
      enum:
        - user
        - guest_author
      title: AuthorType
    type_authors:AuthorSocialMediaLinks:
      type: object
      properties:
        twitter_handle:
          type: string
        facebook_url:
          type: string
        instagram_url:
          type: string
        linkedin_url:
          type: string
        youtube_url:
          type: string
        tiktok_url:
          type: string
        discord_url:
          type: string
        bluesky_url:
          type: string
        rss_url:
          type: string
      title: AuthorSocialMediaLinks
    type_authors:Author:
      type: object
      properties:
        id:
          type: string
          description: The UUID of the author.
        type:
          $ref: '#/components/schemas/type_authors:AuthorType'
          description: The author type.
        name:
          type: string
          description: The author display name.
        bio:
          type: string
          description: The biography text for the author.
        bio_image_url:
          type: string
          description: The profile image URL for the author.
        social_media_links:
          $ref: '#/components/schemas/type_authors:AuthorSocialMediaLinks'
      required:
        - id
        - type
        - name
        - social_media_links
      title: Author
    type_authors:AuthorsListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/type_authors:Author'
          description: A list of authors available for this publication.
        limit:
          type: integer
          description: >-
            The limit placed on the results. If no limit was specified in the
            request, this defaults to 10.
        page:
          type: integer
          default: 1
          description: >-
            The page number the results are from. If no page was specified in
            the request, this defaults to page 1.
        total_results:
          type: integer
          description: The total number of results from all pages.
        total_pages:
          type: integer
          description: The total number of pages.
      required:
        - data
        - limit
        - page
        - total_results
        - total_pages
      title: AuthorsListResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/authors"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/authors';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/authors"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/authors")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/authors")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/authors', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/authors");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/authors")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get author

GET https://api.beehiiv.com/v2/publications/{publicationId}/authors/{authorId}

Retrieve a single author from a publication.

Reference: https://developers.beehiiv.com/api-reference/authors/show

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/authors/{authorId}:
    get:
      operationId: show
      summary: Get author
      description: Retrieve a single author from a publication.
      tags:
        - subpackage_authors
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: authorId
          in: path
          description: >-
            The author identifier. This accepts author UUID, full name, or first
            name.
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_authors:AuthorsGetResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_authors:AuthorType:
      type: string
      enum:
        - user
        - guest_author
      title: AuthorType
    type_authors:AuthorSocialMediaLinks:
      type: object
      properties:
        twitter_handle:
          type: string
        facebook_url:
          type: string
        instagram_url:
          type: string
        linkedin_url:
          type: string
        youtube_url:
          type: string
        tiktok_url:
          type: string
        discord_url:
          type: string
        bluesky_url:
          type: string
        rss_url:
          type: string
      title: AuthorSocialMediaLinks
    type_authors:Author:
      type: object
      properties:
        id:
          type: string
          description: The UUID of the author.
        type:
          $ref: '#/components/schemas/type_authors:AuthorType'
          description: The author type.
        name:
          type: string
          description: The author display name.
        bio:
          type: string
          description: The biography text for the author.
        bio_image_url:
          type: string
          description: The profile image URL for the author.
        social_media_links:
          $ref: '#/components/schemas/type_authors:AuthorSocialMediaLinks'
      required:
        - id
        - type
        - name
        - social_media_links
      title: Author
    type_authors:AuthorsGetResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_authors:Author'
      required:
        - data
      title: AuthorsGetResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/authors/Jane%20Doe"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/authors/Jane%20Doe';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/authors/Jane%20Doe"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/authors/Jane%20Doe")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/authors/Jane%20Doe")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/authors/Jane%20Doe', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/authors/Jane%20Doe");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/authors/Jane%20Doe")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Add subscription to an automation <Badge intent="info" minimal outlined>OAuth Scope: automations:write</Badge>

POST https://api.beehiiv.com/v2/publications/{publicationId}/automations/{automationId}/journeys
Content-Type: application/json

Add an existing subscription to an automation flow. Requires the automation to have an active *Add by API* trigger. The specified `email` or `subscription_id` will be matched against your existing subscribers. If an existing subscriber is found, they will be enrolled immediately.
Looking to enroll new subscribers? Use the **[Create Subscription](/api-reference/subscriptions/create)** endpoint instead and specify the `automation_ids` param.

Reference: https://developers.beehiiv.com/api-reference/automation-journeys/create

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/automations/{automationId}/journeys:
    post:
      operationId: create
      summary: >-
        Add subscription to an automation <Badge intent="info" minimal
        outlined>OAuth Scope: automations:write</Badge>
      description: >-
        Add an existing subscription to an automation flow. Requires the
        automation to have an active *Add by API* trigger. The specified `email`
        or `subscription_id` will be matched against your existing subscribers.
        If an existing subscriber is found, they will be enrolled immediately.

        Looking to enroll new subscribers? Use the **[Create
        Subscription](/api-reference/subscriptions/create)** endpoint instead
        and specify the `automation_ids` param.
      tags:
        - subpackage_automationJourneys
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: automationId
          in: path
          description: The prefixed ID of the automation object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:AutomationId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Created
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_automationJourneys:AutomationJourneysResponse
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                email:
                  type: string
                  description: The email address associated with the subscription.
                subscription_id:
                  $ref: '#/components/schemas/type_ids:SubscriptionId'
                double_opt_override:
                  $ref: '#/components/schemas/type_:DoubleOptOverride'
                  description: >-
                    Override the publication's default double opt-in settings
                    for this subscription. Possible values are:

                    - "on" — The subscriber will receive a double opt-in
                    confirmation email and will need to confirm their
                    subscription prior to being marked as active.

                    - "off" — The subscriber will be marked as active
                    immediately and will not receive a double opt-in
                    confirmation email.

                    - "not_set" — The publication's default double opt-in
                    settings will be applied to this subscription.
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:AutomationId:
      type: string
      description: The prefixed ID of the automation.
      title: AutomationId
    type_ids:SubscriptionId:
      type: string
      description: The prefixed ID of the subscription.
      title: SubscriptionId
    type_:DoubleOptOverride:
      type: string
      description: Override publication double-opt settings for this subscription.
      title: DoubleOptOverride
    type_ids:AutomationJourneyId:
      type: string
      description: The prefixed ID of the automation journey.
      title: AutomationJourneyId
    type_:AutomationJourneyStatus:
      type: string
      enum:
        - in_progress
        - completed
        - exited_early
        - manually_removed
      title: AutomationJourneyStatus
    type_:AutomationJourney:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:AutomationJourneyId'
          description: The prefixed automation journey id
        automation_id:
          $ref: '#/components/schemas/type_ids:AutomationId'
          description: The prefixed automation id
        subscription_id:
          $ref: '#/components/schemas/type_ids:SubscriptionId'
        email:
          type: string
        status:
          $ref: '#/components/schemas/type_:AutomationJourneyStatus'
        started_at:
          type: integer
          description: >-
            The time that the subscriber started their flow through the
            automation. Measured in seconds since the Unix epoch.
        completed_at:
          type: integer
          description: >-
            The time that the subscriber finished their flow through the
            automation. Measured in seconds since the Unix epoch.
      required:
        - id
        - automation_id
        - status
      description: A subscribers' journey through an automation flow.
      title: AutomationJourney
    type_automationJourneys:AutomationJourneysResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_:AutomationJourney'
      required:
        - data
      title: AutomationJourneysResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.automationJourneys.create("pub_00000000-0000-0000-0000-000000000000", "aut_00000000-0000-0000-0000-000000000000");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys"

payload = {
    "email": "test@example.com",
    "double_opt_override": "on"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys"

	payload := strings.NewReader("{\n  \"email\": \"test@example.com\",\n  \"double_opt_override\": \"on\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"email\": \"test@example.com\",\n  \"double_opt_override\": \"on\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"email\": \"test@example.com\",\n  \"double_opt_override\": \"on\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys', [
  'body' => '{
  "email": "test@example.com",
  "double_opt_override": "on"
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"email\": \"test@example.com\",\n  \"double_opt_override\": \"on\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "email": "test@example.com",
  "double_opt_override": "on"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# List automation journeys <Badge intent="info" minimal outlined>OAuth Scope: automations:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/automations/{automationId}/journeys

Retrieve a list of automation journeys that have occurred within a specific automation.

Reference: https://developers.beehiiv.com/api-reference/automation-journeys/index

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/automations/{automationId}/journeys:
    get:
      operationId: index
      summary: >-
        List automation journeys <Badge intent="info" minimal outlined>OAuth
        Scope: automations:read</Badge>
      description: >-
        Retrieve a list of automation journeys that have occurred within a
        specific automation.
      tags:
        - subpackage_automationJourneys
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: automationId
          in: path
          description: The prefixed ID of the automation object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:AutomationId'
        - name: status
          in: query
          description: Optionally filter the results by the automation journey's status.
          required: false
          schema:
            $ref: >-
              #/components/schemas/type_automationJourneys:AutomationJourneysGetRequestStatus
        - name: limit
          in: query
          description: >-
            A limit on the number of objects to be returned. The limit can range
            between 1 and 100, and the default is 10.
          required: false
          schema:
            type: integer
        - name: page
          in: query
          description: >-
            Pagination returns the results in pages. Each page contains the
            number of results specified by the `limit` (default: 10).
          required: false
          schema:
            type: integer
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_automationJourneys:AutomationJourneysIndexResponse
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:AutomationId:
      type: string
      description: The prefixed ID of the automation.
      title: AutomationId
    type_automationJourneys:AutomationJourneysGetRequestStatus:
      type: string
      enum:
        - in_progress
        - completed
        - exited_early
        - all
      default: all
      title: AutomationJourneysGetRequestStatus
    type_ids:AutomationJourneyId:
      type: string
      description: The prefixed ID of the automation journey.
      title: AutomationJourneyId
    type_ids:SubscriptionId:
      type: string
      description: The prefixed ID of the subscription.
      title: SubscriptionId
    type_:AutomationJourneyStatus:
      type: string
      enum:
        - in_progress
        - completed
        - exited_early
        - manually_removed
      title: AutomationJourneyStatus
    type_:AutomationJourney:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:AutomationJourneyId'
          description: The prefixed automation journey id
        automation_id:
          $ref: '#/components/schemas/type_ids:AutomationId'
          description: The prefixed automation id
        subscription_id:
          $ref: '#/components/schemas/type_ids:SubscriptionId'
        email:
          type: string
        status:
          $ref: '#/components/schemas/type_:AutomationJourneyStatus'
        started_at:
          type: integer
          description: >-
            The time that the subscriber started their flow through the
            automation. Measured in seconds since the Unix epoch.
        completed_at:
          type: integer
          description: >-
            The time that the subscriber finished their flow through the
            automation. Measured in seconds since the Unix epoch.
      required:
        - id
        - automation_id
        - status
      description: A subscribers' journey through an automation flow.
      title: AutomationJourney
    type_automationJourneys:AutomationJourneysIndexResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/type_:AutomationJourney'
        limit:
          type: integer
          description: >-
            The limit placed on the results. If no limit was specified in the
            request, this defaults to 10.
        page:
          type: integer
          default: 1
          description: >-
            The page number the results are from. If no page was specified in
            the request, this defaults to page 1.
        total_results:
          type: integer
          description: The total number of results from all pages.
        total_pages:
          type: integer
          description: The total number of pages.
      required:
        - data
        - limit
        - page
        - total_results
        - total_pages
      title: AutomationJourneysIndexResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get automation journey <Badge intent="info" minimal outlined>OAuth Scope: automations:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/automations/{automationId}/journeys/{automationJourneyId}

Retrieve a single automation journey by ID.

Reference: https://developers.beehiiv.com/api-reference/automation-journeys/show

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/automations/{automationId}/journeys/{automationJourneyId}:
    get:
      operationId: show
      summary: >-
        Get automation journey <Badge intent="info" minimal outlined>OAuth
        Scope: automations:read</Badge>
      description: Retrieve a single automation journey by ID.
      tags:
        - subpackage_automationJourneys
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: automationId
          in: path
          description: The prefixed ID of the automation object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:AutomationId'
        - name: automationJourneyId
          in: path
          description: The prefixed automation journey id
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:AutomationJourneyId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_automationJourneys:AutomationJourneysResponse
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:AutomationId:
      type: string
      description: The prefixed ID of the automation.
      title: AutomationId
    type_ids:AutomationJourneyId:
      type: string
      description: The prefixed ID of the automation journey.
      title: AutomationJourneyId
    type_ids:SubscriptionId:
      type: string
      description: The prefixed ID of the subscription.
      title: SubscriptionId
    type_:AutomationJourneyStatus:
      type: string
      enum:
        - in_progress
        - completed
        - exited_early
        - manually_removed
      title: AutomationJourneyStatus
    type_:AutomationJourney:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:AutomationJourneyId'
          description: The prefixed automation journey id
        automation_id:
          $ref: '#/components/schemas/type_ids:AutomationId'
          description: The prefixed automation id
        subscription_id:
          $ref: '#/components/schemas/type_ids:SubscriptionId'
        email:
          type: string
        status:
          $ref: '#/components/schemas/type_:AutomationJourneyStatus'
        started_at:
          type: integer
          description: >-
            The time that the subscriber started their flow through the
            automation. Measured in seconds since the Unix epoch.
        completed_at:
          type: integer
          description: >-
            The time that the subscriber finished their flow through the
            automation. Measured in seconds since the Unix epoch.
      required:
        - id
        - automation_id
        - status
      description: A subscribers' journey through an automation flow.
      title: AutomationJourney
    type_automationJourneys:AutomationJourneysResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_:AutomationJourney'
      required:
        - data
      title: AutomationJourneysResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.automationJourneys.get("pub_00000000-0000-0000-0000-000000000000", "aut_00000000-0000-0000-0000-000000000000", "aj_00000000-0000-0000-0000-000000000000");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys/aj_00000000-0000-0000-0000-000000000000"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys/aj_00000000-0000-0000-0000-000000000000"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys/aj_00000000-0000-0000-0000-000000000000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys/aj_00000000-0000-0000-0000-000000000000")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys/aj_00000000-0000-0000-0000-000000000000', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys/aj_00000000-0000-0000-0000-000000000000");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000/journeys/aj_00000000-0000-0000-0000-000000000000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# List automations <Badge intent="info" minimal outlined>OAuth Scope: automations:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/automations

Retrieve automations for a publication.

Reference: https://developers.beehiiv.com/api-reference/automations/index

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/automations:
    get:
      operationId: index
      summary: >-
        List automations <Badge intent="info" minimal outlined>OAuth Scope:
        automations:read</Badge>
      description: Retrieve automations for a publication.
      tags:
        - subpackage_automations
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: limit
          in: query
          description: >-
            A limit on the number of objects to be returned. The limit can range
            between 1 and 100, and the default is 10.
          required: false
          schema:
            type: integer
        - name: page
          in: query
          description: >-
            Pagination returns the results in pages. Each page contains the
            number of results specified by the `limit` (default: 10).<br>If not
            specified, results 1-10 from page 1 will be returned.
          required: false
          schema:
            type: integer
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_automations:AutomationsListResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:AutomationId:
      type: string
      description: The prefixed ID of the automation.
      title: AutomationId
    type_:AutomationStatus:
      type: string
      enum:
        - running
        - finishing
        - inactive
        - live
        - draft
      title: AutomationStatus
    type_:AutomationTriggerEvent:
      type: string
      enum:
        - api
        - downgrade
        - email_submission
        - form_submission
        - manual
        - poll_submission
        - purchased_product
        - referral_action
        - segment_action
        - signup
        - unengaged
        - upgrade
      title: AutomationTriggerEvent
    type_:Automation:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:AutomationId'
          description: A unique prefixed id of the automation
        status:
          $ref: '#/components/schemas/type_:AutomationStatus'
        name:
          type: string
        trigger_events:
          type: array
          items:
            $ref: '#/components/schemas/type_:AutomationTriggerEvent'
          description: The types of events that can trigger the automation.
        description:
          type: string
      required:
        - id
        - status
        - name
        - trigger_events
      title: Automation
    type_automations:AutomationsListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/type_:Automation'
        limit:
          type: integer
          description: >-
            The limit placed on the results. If no limit was specified in the
            request,this defaults to 10.
        page:
          type: integer
          default: 1
          description: >-
            The page number the results are from. If no page was specified in
            the request, this defaults to page 1.
        total_results:
          type: integer
          description: The total number of results from all pages.
        total_pages:
          type: integer
          description: The total number of pages.
      title: AutomationsListResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.automations.list("pub_00000000-0000-0000-0000-000000000000");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations"

payload = {}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get automation <Badge intent="info" minimal outlined>OAuth Scope: automations:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/automations/{automationId}

Retrieve a single automation for a publication.

Reference: https://developers.beehiiv.com/api-reference/automations/show

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/automations/{automationId}:
    get:
      operationId: show
      summary: >-
        Get automation <Badge intent="info" minimal outlined>OAuth Scope:
        automations:read</Badge>
      description: Retrieve a single automation for a publication.
      tags:
        - subpackage_automations
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: automationId
          in: path
          description: The prefixed ID of the automation object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:AutomationId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_automations:AutomationsGetResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:AutomationId:
      type: string
      description: The prefixed ID of the automation.
      title: AutomationId
    type_:AutomationStatus:
      type: string
      enum:
        - running
        - finishing
        - inactive
        - live
        - draft
      title: AutomationStatus
    type_:AutomationTriggerEvent:
      type: string
      enum:
        - api
        - downgrade
        - email_submission
        - form_submission
        - manual
        - poll_submission
        - purchased_product
        - referral_action
        - segment_action
        - signup
        - unengaged
        - upgrade
      title: AutomationTriggerEvent
    type_:Automation:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:AutomationId'
          description: A unique prefixed id of the automation
        status:
          $ref: '#/components/schemas/type_:AutomationStatus'
        name:
          type: string
        trigger_events:
          type: array
          items:
            $ref: '#/components/schemas/type_:AutomationTriggerEvent'
          description: The types of events that can trigger the automation.
        description:
          type: string
      required:
        - id
        - status
        - name
        - trigger_events
      title: Automation
    type_automations:AutomationsGetResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_:Automation'
      title: AutomationsGetResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.automations.get("pub_00000000-0000-0000-0000-000000000000", "aut_00000000-0000-0000-0000-000000000000");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/automations/aut_00000000-0000-0000-0000-000000000000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Bulk create subscription <Badge intent="info" minimal outlined>OAuth Scope: subscriptions:write</Badge>

POST https://api.beehiiv.com/v2/publications/{publicationId}/bulk_subscriptions
Content-Type: application/json

Create new subscriptions for a publication.

Reference: https://developers.beehiiv.com/api-reference/bulk-subscriptions/create

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/bulk_subscriptions:
    post:
      operationId: create
      summary: >-
        Bulk create subscription <Badge intent="info" minimal outlined>OAuth
        Scope: subscriptions:write</Badge>
      description: Create new subscriptions for a publication.
      tags:
        - subpackage_bulk_subscriptions
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Subscriptions created
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_bulk_subscriptions:BulkSubscriptionCreateResponse
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                subscriptions:
                  type: array
                  items:
                    $ref: '#/components/schemas/type_:SubscriptionRequest'
              required:
                - subscriptions
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_:CustomFieldDataType:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: boolean
        - type: array
          items:
            type: string
      title: CustomFieldDataType
    type_:CustomFieldValue:
      type: object
      properties:
        name:
          type: string
          description: The name of the existing custom field
        value:
          $ref: '#/components/schemas/type_:CustomFieldDataType'
          description: The value stored for the subscription
      description: The object required for setting custom field values on a subscription
      title: CustomFieldValue
    type_:DoubleOptOverride:
      type: string
      description: Override publication double-opt settings for this subscription.
      title: DoubleOptOverride
    type_:SubscriptionsCreateRequestTier:
      type: string
      enum:
        - free
        - premium
      description: The tier for this subscription.
      title: SubscriptionsCreateRequestTier
    type_ids:OptionalStripeCustomerId:
      type: string
      description: The prefixed ID of the Stripe customer.
      title: OptionalStripeCustomerId
    type_:SubscriptionRequest:
      type: object
      properties:
        email:
          type: string
          description: The email address of the subscription.
        reactivate_existing:
          type: boolean
          default: false
          description: >-
            Whether or not to reactivate the subscription if they have already
            unsubscribed. This option should be used only if the subscriber is
            knowingly resubscribing.
        send_welcome_email:
          type: boolean
          default: false
        utm_source:
          type: string
          description: The source of the subscription.
        utm_medium:
          type: string
          description: The medium of the subscription
        utm_campaign:
          type: string
          description: The acquisition campaign of the subscription
        utm_term:
          type: string
          description: The acquisition term; typically the keyword or search term
        utm_content:
          type: string
          description: >-
            The acquisition content; typically used for A/B testing or ad
            variations
        referring_site:
          type: string
          description: The website that the subscriber was referred from
        referral_code:
          type: string
          description: >-
            This should be a subscribers referral_code. This gives referral
            credit for the new subscription.
        custom_fields:
          type: array
          items:
            $ref: '#/components/schemas/type_:CustomFieldValue'
          description: >-
            The custom fields must already exist for the publication. Any new
            custom fields here will be discarded.
        double_opt_override:
          $ref: '#/components/schemas/type_:DoubleOptOverride'
          description: >-
            Override the publication's default double opt-in settings for this
            subscription. Possible values are:

            - "on" — The subscriber will receive a double opt-in confirmation
            email and will need to confirm their subscription prior to being
            marked as active.

            - "off" — The subscriber will be marked as active immediately and
            will not receive a double opt-in confirmation email.

            - "not_set" — The publication's default double opt-in settings will
            be applied to this subscription.
        tier:
          $ref: '#/components/schemas/type_:SubscriptionsCreateRequestTier'
          description: The tier for this subscription.
        premium_tiers:
          type: array
          items:
            type: string
          description: >-
            An array of premium tier names to assign to this subscription. When
            provided, the subscription will be assigned to premium tiers
            matching these names. Can be combined with `premium_tier_ids` to
            include tiers from both (duplicates are removed). Takes precedence
            over the `tier` parameter.
        premium_tier_ids:
          type: array
          items:
            type: string
          description: >-
            An array of premium tier IDs to assign to this subscription. When
            provided, the subscription will be assigned to these specific
            premium tiers. Can be combined with `premium_tiers` to include tiers
            from both (duplicates are removed). Takes precedence over the `tier`
            parameter.
        stripe_customer_id:
          $ref: '#/components/schemas/type_ids:OptionalStripeCustomerId'
          description: The Stripe customer ID for this subscription.
        automation_ids:
          type: array
          items:
            type: string
          description: >-
            Enroll the subscriber into automations after their subscription has
            been created. Requires the automations to have an active *Add by
            API* trigger.
      required:
        - email
      title: SubscriptionRequest
    type_bulk_subscriptions:BulkSubscriptionCreateResponse:
      type: object
      properties:
        message:
          type: string
          description: The result of the create request
        import_id:
          type: string
          description: >-
            The database ID of the import object created from the Bulk
            Subscription Create request
      required:
        - message
        - import_id
      description: The response containing the import ID
      title: BulkSubscriptionCreateResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/bulk_subscriptions"

payload = { "subscriptions": [
        {
            "email": "bruce.wayne@wayneenterprise.com",
            "reactivate_existing": False,
            "send_welcome_email": False,
            "custom_fields": [
                {
                    "name": "Favorite Color",
                    "value": "Red"
                }
            ]
        },
        {
            "email": "lucius.fox@wayneenterprise.com",
            "reactivate_existing": False,
            "send_welcome_email": False,
            "custom_fields": [
                {
                    "name": "Favorite Color",
                    "value": "Blue"
                }
            ]
        }
    ] }
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/bulk_subscriptions';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"subscriptions":[{"email":"bruce.wayne@wayneenterprise.com","reactivate_existing":false,"send_welcome_email":false,"custom_fields":[{"name":"Favorite Color","value":"Red"}]},{"email":"lucius.fox@wayneenterprise.com","reactivate_existing":false,"send_welcome_email":false,"custom_fields":[{"name":"Favorite Color","value":"Blue"}]}]}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/bulk_subscriptions"

	payload := strings.NewReader("{\n  \"subscriptions\": [\n    {\n      \"email\": \"bruce.wayne@wayneenterprise.com\",\n      \"reactivate_existing\": false,\n      \"send_welcome_email\": false,\n      \"custom_fields\": [\n        {\n          \"name\": \"Favorite Color\",\n          \"value\": \"Red\"\n        }\n      ]\n    },\n    {\n      \"email\": \"lucius.fox@wayneenterprise.com\",\n      \"reactivate_existing\": false,\n      \"send_welcome_email\": false,\n      \"custom_fields\": [\n        {\n          \"name\": \"Favorite Color\",\n          \"value\": \"Blue\"\n        }\n      ]\n    }\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/bulk_subscriptions")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"subscriptions\": [\n    {\n      \"email\": \"bruce.wayne@wayneenterprise.com\",\n      \"reactivate_existing\": false,\n      \"send_welcome_email\": false,\n      \"custom_fields\": [\n        {\n          \"name\": \"Favorite Color\",\n          \"value\": \"Red\"\n        }\n      ]\n    },\n    {\n      \"email\": \"lucius.fox@wayneenterprise.com\",\n      \"reactivate_existing\": false,\n      \"send_welcome_email\": false,\n      \"custom_fields\": [\n        {\n          \"name\": \"Favorite Color\",\n          \"value\": \"Blue\"\n        }\n      ]\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/bulk_subscriptions")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"subscriptions\": [\n    {\n      \"email\": \"bruce.wayne@wayneenterprise.com\",\n      \"reactivate_existing\": false,\n      \"send_welcome_email\": false,\n      \"custom_fields\": [\n        {\n          \"name\": \"Favorite Color\",\n          \"value\": \"Red\"\n        }\n      ]\n    },\n    {\n      \"email\": \"lucius.fox@wayneenterprise.com\",\n      \"reactivate_existing\": false,\n      \"send_welcome_email\": false,\n      \"custom_fields\": [\n        {\n          \"name\": \"Favorite Color\",\n          \"value\": \"Blue\"\n        }\n      ]\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/bulk_subscriptions', [
  'body' => '{
  "subscriptions": [
    {
      "email": "bruce.wayne@wayneenterprise.com",
      "reactivate_existing": false,
      "send_welcome_email": false,
      "custom_fields": [
        {
          "name": "Favorite Color",
          "value": "Red"
        }
      ]
    },
    {
      "email": "lucius.fox@wayneenterprise.com",
      "reactivate_existing": false,
      "send_welcome_email": false,
      "custom_fields": [
        {
          "name": "Favorite Color",
          "value": "Blue"
        }
      ]
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/bulk_subscriptions");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"subscriptions\": [\n    {\n      \"email\": \"bruce.wayne@wayneenterprise.com\",\n      \"reactivate_existing\": false,\n      \"send_welcome_email\": false,\n      \"custom_fields\": [\n        {\n          \"name\": \"Favorite Color\",\n          \"value\": \"Red\"\n        }\n      ]\n    },\n    {\n      \"email\": \"lucius.fox@wayneenterprise.com\",\n      \"reactivate_existing\": false,\n      \"send_welcome_email\": false,\n      \"custom_fields\": [\n        {\n          \"name\": \"Favorite Color\",\n          \"value\": \"Blue\"\n        }\n      ]\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["subscriptions": [
    [
      "email": "bruce.wayne@wayneenterprise.com",
      "reactivate_existing": false,
      "send_welcome_email": false,
      "custom_fields": [
        [
          "name": "Favorite Color",
          "value": "Red"
        ]
      ]
    ],
    [
      "email": "lucius.fox@wayneenterprise.com",
      "reactivate_existing": false,
      "send_welcome_email": false,
      "custom_fields": [
        [
          "name": "Favorite Color",
          "value": "Blue"
        ]
      ]
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/bulk_subscriptions")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# List subscription updates <Badge intent="info" minimal outlined>OAuth Scope: subscriptions:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/bulk_subscription_updates

Returns a list of Subscription Update objects for a publication.

Reference: https://developers.beehiiv.com/api-reference/bulk-subscription-updates/index

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/bulk_subscription_updates:
    get:
      operationId: index
      summary: >-
        List subscription updates <Badge intent="info" minimal outlined>OAuth
        Scope: subscriptions:read</Badge>
      description: Returns a list of Subscription Update objects for a publication.
      tags:
        - subpackage_bulkSubscriptionUpdates
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_bulkSubscriptionUpdates:BulkSubscriptionUpdatesListResponse
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_bulkSubscriptionUpdates:BulkSubscriptionUpdatesListResponseDataItemType:
      type: string
      enum:
        - status
        - bulk
      description: The type of update (status or bulk)
      title: BulkSubscriptionUpdatesListResponseDataItemType
    type_bulkSubscriptionUpdates:BulkSubscriptionUpdatesListResponseDataItemStatus:
      type: string
      enum:
        - pending
        - processing
        - complete
        - failed
      description: The status of the update
      title: BulkSubscriptionUpdatesListResponseDataItemStatus
    type_bulkSubscriptionUpdates:BulkSubscriptionUpdatesListResponseDataItem:
      type: object
      properties:
        id:
          type: string
          description: The ID of the update object
        type:
          $ref: >-
            #/components/schemas/type_bulkSubscriptionUpdates:BulkSubscriptionUpdatesListResponseDataItemType
          description: The type of update (status or bulk)
        params:
          type: string
          description: The parameters passed in for the update
        status:
          $ref: >-
            #/components/schemas/type_bulkSubscriptionUpdates:BulkSubscriptionUpdatesListResponseDataItemStatus
          description: The status of the update
        publication_id:
          $ref: '#/components/schemas/type_ids:PublicationId'
          description: The publication ID associated with this update
        failure_reason:
          type: string
          description: If the job as a whole fails, this will detail the errors encountered
        completed:
          type: integer
          description: The timestamp of the job's completion
        created:
          type: integer
          description: The timestamp of the job's creation
        updated:
          type: integer
          description: The timestamp of the job's update
        error_log:
          type: array
          items:
            type: string
          description: An array of errors encountered for individual updates within the job
      title: BulkSubscriptionUpdatesListResponseDataItem
    type_bulkSubscriptionUpdates:BulkSubscriptionUpdatesListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_bulkSubscriptionUpdates:BulkSubscriptionUpdatesListResponseDataItem
          description: An array of Subscription Update objects
      title: BulkSubscriptionUpdatesListResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.bulkSubscriptionUpdates.list("publicationId");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/publicationId/bulk_subscription_updates"

payload = {}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/publicationId/bulk_subscription_updates"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/publicationId/bulk_subscription_updates")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/publicationId/bulk_subscription_updates")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/publicationId/bulk_subscription_updates', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/publicationId/bulk_subscription_updates");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/publicationId/bulk_subscription_updates")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get subscription update <Badge intent="info" minimal outlined>OAuth Scope: subscriptions:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/bulk_subscription_updates/{id}

Returns a single Subscription Update object for a publication.

Reference: https://developers.beehiiv.com/api-reference/bulk-subscription-updates/show

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/bulk_subscription_updates/{id}:
    get:
      operationId: show
      summary: >-
        Get subscription update <Badge intent="info" minimal outlined>OAuth
        Scope: subscriptions:read</Badge>
      description: Returns a single Subscription Update object for a publication.
      tags:
        - subpackage_bulkSubscriptionUpdates
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: id
          in: path
          description: The ID of the Subscription Update object
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_bulkSubscriptionUpdates:BulkSubscriptionUpdatesGetResponse
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_bulkSubscriptionUpdates:BulkSubscriptionUpdatesGetResponseDataType:
      type: string
      enum:
        - bulk
        - status
      description: The type of update (status or bulk)
      title: BulkSubscriptionUpdatesGetResponseDataType
    type_bulkSubscriptionUpdates:BulkSubscriptionUpdatesGetResponseDataStatus:
      type: string
      enum:
        - pending
        - processing
        - complete
        - failed
      description: The status of the update
      title: BulkSubscriptionUpdatesGetResponseDataStatus
    type_bulkSubscriptionUpdates:BulkSubscriptionUpdatesGetResponseData:
      type: object
      properties:
        id:
          type: string
          description: The ID of the update object
        type:
          $ref: >-
            #/components/schemas/type_bulkSubscriptionUpdates:BulkSubscriptionUpdatesGetResponseDataType
          description: The type of update (status or bulk)
        params:
          type: string
          description: The parameters passed in for the update
        status:
          $ref: >-
            #/components/schemas/type_bulkSubscriptionUpdates:BulkSubscriptionUpdatesGetResponseDataStatus
          description: The status of the update
        publication_id:
          $ref: '#/components/schemas/type_ids:PublicationId'
          description: The publication ID associated with this update
        failure_reason:
          type: string
          description: If the job as a whole fails, this will detail the errors encountered
        completed:
          type: integer
          description: The timestamp of the job's completion
        created:
          type: integer
          description: The timestamp of the job's creation
        updated:
          type: integer
          description: The timestamp of the job's update
        error_log:
          type: array
          items:
            type: string
          description: An array of errors encountered for individual updates within the job
      title: BulkSubscriptionUpdatesGetResponseData
    type_bulkSubscriptionUpdates:BulkSubscriptionUpdatesGetResponse:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/type_bulkSubscriptionUpdates:BulkSubscriptionUpdatesGetResponseData
      title: BulkSubscriptionUpdatesGetResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.bulkSubscriptionUpdates.get("publicationId", "id");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/publicationId/bulk_subscription_updates/id"

payload = {}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/publicationId/bulk_subscription_updates/id"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/publicationId/bulk_subscription_updates/id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/publicationId/bulk_subscription_updates/id")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/publicationId/bulk_subscription_updates/id', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/publicationId/bulk_subscription_updates/id");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/publicationId/bulk_subscription_updates/id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Update subscriptions <Badge intent="info" minimal outlined>OAuth Scope: subscriptions:write</Badge>

PUT https://api.beehiiv.com/v2/publications/{publicationId}/subscriptions/bulk_actions
Content-Type: application/json

Bulk update multiple subscriptions fields, including status, custom fields, and tiers.

Reference: https://developers.beehiiv.com/api-reference/bulk-subscription-updates/put

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/subscriptions/bulk_actions:
    put:
      operationId: put
      summary: >-
        Update subscriptions <Badge intent="info" minimal outlined>OAuth Scope:
        subscriptions:write</Badge>
      description: >-
        Bulk update multiple subscriptions fields, including status, custom
        fields, and tiers.
      tags:
        - subpackage_bulkSubscriptionUpdates
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_subscriptions:SubscriptionsPatchResponse
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                subscriptions:
                  type: array
                  items:
                    $ref: >-
                      #/components/schemas/type_bulkSubscriptionUpdates:SubscriptionsPatchRequestSubscriptionsItem
                  description: >-
                    An array of objects representing the subscriptions to be
                    updated (max 1000).
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:SubscriptionId:
      type: string
      description: The prefixed ID of the subscription.
      title: SubscriptionId
    type_bulkSubscriptionUpdates:SubscriptionsPatchRequestSubscriptionsItemTier:
      type: string
      enum:
        - free
        - premium
      description: The Tier of the Subscription (not required)
      title: SubscriptionsPatchRequestSubscriptionsItemTier
    type_ids:OptionalStripeCustomerId:
      type: string
      description: The prefixed ID of the Stripe customer.
      title: OptionalStripeCustomerId
    type_:CustomFieldDataType:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: boolean
        - type: array
          items:
            type: string
      title: CustomFieldDataType
    type_bulkSubscriptionUpdates:SubscriptionsPatchRequestSubscriptionsItemCustomFieldsItem:
      type: object
      properties:
        name:
          type: string
          description: The display value of the custom field
        value:
          $ref: '#/components/schemas/type_:CustomFieldDataType'
          description: The value of the custom field
        delete:
          type: boolean
          description: >-
            A boolean value to specify whether to delete this custom field entry
            from the subscription
      title: SubscriptionsPatchRequestSubscriptionsItemCustomFieldsItem
    type_bulkSubscriptionUpdates:SubscriptionsPatchRequestSubscriptionsItem:
      type: object
      properties:
        subscription_id:
          $ref: '#/components/schemas/type_ids:SubscriptionId'
        tier:
          $ref: >-
            #/components/schemas/type_bulkSubscriptionUpdates:SubscriptionsPatchRequestSubscriptionsItemTier
          description: The Tier of the Subscription (not required)
        stripe_customer_id:
          $ref: '#/components/schemas/type_ids:OptionalStripeCustomerId'
          description: The Stripe Customer ID of the subscription (not required)
        unsubscribe:
          type: boolean
          description: >-
            A boolean value specifying whether to unsubscribe this subscription
            from the publication (not required)
        custom_fields:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_bulkSubscriptionUpdates:SubscriptionsPatchRequestSubscriptionsItemCustomFieldsItem
          description: An array of custom field objects to update
      required:
        - subscription_id
      title: SubscriptionsPatchRequestSubscriptionsItem
    type_subscriptions:SubscriptionsPatchResponseData:
      type: object
      properties:
        subscription_update_id:
          type: string
          description: >-
            The ID of the Subscription Update object responsible for handling
            the update job
      title: SubscriptionsPatchResponseData
    type_subscriptions:SubscriptionsPatchResponse:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/type_subscriptions:SubscriptionsPatchResponseData
      required:
        - data
      title: SubscriptionsPatchResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.subscriptions.put("publicationId");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/publicationId/subscriptions/bulk_actions"

payload = { "subscriptions": [
        {
            "subscription_id": "sub_1234-5678-9012-3456-7890",
            "tier": "premium",
            "stripe_customer_id": "cus_1234567890",
            "unsubscribe": False,
            "custom_fields": [
                {
                    "name": "custom_field_name",
                    "value": "custom_field_value"
                },
                {
                    "name": "custom_field_name_2",
                    "value": "custom_field_value_2"
                }
            ]
        },
        {
            "subscription_id": "sub_9876-5432-1098-7654-3210",
            "tier": "free",
            "stripe_customer_id": "cus_1234567890",
            "unsubscribe": True,
            "custom_fields": [
                {
                    "name": "custom_field_name_3",
                    "value": "custom_field_value_3"
                },
                {
                    "name": "custom_field_name_4",
                    "value": "custom_field_value_4"
                }
            ]
        }
    ] }
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/publicationId/subscriptions/bulk_actions"

	payload := strings.NewReader("{\n  \"subscriptions\": [\n    {\n      \"subscription_id\": \"sub_1234-5678-9012-3456-7890\",\n      \"tier\": \"premium\",\n      \"stripe_customer_id\": \"cus_1234567890\",\n      \"unsubscribe\": false,\n      \"custom_fields\": [\n        {\n          \"name\": \"custom_field_name\",\n          \"value\": \"custom_field_value\"\n        },\n        {\n          \"name\": \"custom_field_name_2\",\n          \"value\": \"custom_field_value_2\"\n        }\n      ]\n    },\n    {\n      \"subscription_id\": \"sub_9876-5432-1098-7654-3210\",\n      \"tier\": \"free\",\n      \"stripe_customer_id\": \"cus_1234567890\",\n      \"unsubscribe\": true,\n      \"custom_fields\": [\n        {\n          \"name\": \"custom_field_name_3\",\n          \"value\": \"custom_field_value_3\"\n        },\n        {\n          \"name\": \"custom_field_name_4\",\n          \"value\": \"custom_field_value_4\"\n        }\n      ]\n    }\n  ]\n}")

	req, _ := http.NewRequest("PUT", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/publicationId/subscriptions/bulk_actions")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"subscriptions\": [\n    {\n      \"subscription_id\": \"sub_1234-5678-9012-3456-7890\",\n      \"tier\": \"premium\",\n      \"stripe_customer_id\": \"cus_1234567890\",\n      \"unsubscribe\": false,\n      \"custom_fields\": [\n        {\n          \"name\": \"custom_field_name\",\n          \"value\": \"custom_field_value\"\n        },\n        {\n          \"name\": \"custom_field_name_2\",\n          \"value\": \"custom_field_value_2\"\n        }\n      ]\n    },\n    {\n      \"subscription_id\": \"sub_9876-5432-1098-7654-3210\",\n      \"tier\": \"free\",\n      \"stripe_customer_id\": \"cus_1234567890\",\n      \"unsubscribe\": true,\n      \"custom_fields\": [\n        {\n          \"name\": \"custom_field_name_3\",\n          \"value\": \"custom_field_value_3\"\n        },\n        {\n          \"name\": \"custom_field_name_4\",\n          \"value\": \"custom_field_value_4\"\n        }\n      ]\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("https://api.beehiiv.com/v2/publications/publicationId/subscriptions/bulk_actions")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"subscriptions\": [\n    {\n      \"subscription_id\": \"sub_1234-5678-9012-3456-7890\",\n      \"tier\": \"premium\",\n      \"stripe_customer_id\": \"cus_1234567890\",\n      \"unsubscribe\": false,\n      \"custom_fields\": [\n        {\n          \"name\": \"custom_field_name\",\n          \"value\": \"custom_field_value\"\n        },\n        {\n          \"name\": \"custom_field_name_2\",\n          \"value\": \"custom_field_value_2\"\n        }\n      ]\n    },\n    {\n      \"subscription_id\": \"sub_9876-5432-1098-7654-3210\",\n      \"tier\": \"free\",\n      \"stripe_customer_id\": \"cus_1234567890\",\n      \"unsubscribe\": true,\n      \"custom_fields\": [\n        {\n          \"name\": \"custom_field_name_3\",\n          \"value\": \"custom_field_value_3\"\n        },\n        {\n          \"name\": \"custom_field_name_4\",\n          \"value\": \"custom_field_value_4\"\n        }\n      ]\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'https://api.beehiiv.com/v2/publications/publicationId/subscriptions/bulk_actions', [
  'body' => '{
  "subscriptions": [
    {
      "subscription_id": "sub_1234-5678-9012-3456-7890",
      "tier": "premium",
      "stripe_customer_id": "cus_1234567890",
      "unsubscribe": false,
      "custom_fields": [
        {
          "name": "custom_field_name",
          "value": "custom_field_value"
        },
        {
          "name": "custom_field_name_2",
          "value": "custom_field_value_2"
        }
      ]
    },
    {
      "subscription_id": "sub_9876-5432-1098-7654-3210",
      "tier": "free",
      "stripe_customer_id": "cus_1234567890",
      "unsubscribe": true,
      "custom_fields": [
        {
          "name": "custom_field_name_3",
          "value": "custom_field_value_3"
        },
        {
          "name": "custom_field_name_4",
          "value": "custom_field_value_4"
        }
      ]
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/publicationId/subscriptions/bulk_actions");
var request = new RestRequest(Method.PUT);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"subscriptions\": [\n    {\n      \"subscription_id\": \"sub_1234-5678-9012-3456-7890\",\n      \"tier\": \"premium\",\n      \"stripe_customer_id\": \"cus_1234567890\",\n      \"unsubscribe\": false,\n      \"custom_fields\": [\n        {\n          \"name\": \"custom_field_name\",\n          \"value\": \"custom_field_value\"\n        },\n        {\n          \"name\": \"custom_field_name_2\",\n          \"value\": \"custom_field_value_2\"\n        }\n      ]\n    },\n    {\n      \"subscription_id\": \"sub_9876-5432-1098-7654-3210\",\n      \"tier\": \"free\",\n      \"stripe_customer_id\": \"cus_1234567890\",\n      \"unsubscribe\": true,\n      \"custom_fields\": [\n        {\n          \"name\": \"custom_field_name_3\",\n          \"value\": \"custom_field_value_3\"\n        },\n        {\n          \"name\": \"custom_field_name_4\",\n          \"value\": \"custom_field_value_4\"\n        }\n      ]\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["subscriptions": [
    [
      "subscription_id": "sub_1234-5678-9012-3456-7890",
      "tier": "premium",
      "stripe_customer_id": "cus_1234567890",
      "unsubscribe": false,
      "custom_fields": [
        [
          "name": "custom_field_name",
          "value": "custom_field_value"
        ],
        [
          "name": "custom_field_name_2",
          "value": "custom_field_value_2"
        ]
      ]
    ],
    [
      "subscription_id": "sub_9876-5432-1098-7654-3210",
      "tier": "free",
      "stripe_customer_id": "cus_1234567890",
      "unsubscribe": true,
      "custom_fields": [
        [
          "name": "custom_field_name_3",
          "value": "custom_field_value_3"
        ],
        [
          "name": "custom_field_name_4",
          "value": "custom_field_value_4"
        ]
      ]
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/publicationId/subscriptions/bulk_actions")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PUT"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Update subscriptions' status <Badge intent="info" minimal outlined>OAuth Scope: subscriptions:write</Badge>

PUT https://api.beehiiv.com/v2/publications/{publicationId}/subscriptions
Content-Type: application/json

Bulk update subscriptions' status.

Reference: https://developers.beehiiv.com/api-reference/bulk-subscription-updates/put-status

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/subscriptions:
    put:
      operationId: put-status
      summary: >-
        Update subscriptions' status <Badge intent="info" minimal outlined>OAuth
        Scope: subscriptions:write</Badge>
      description: Bulk update subscriptions' status.
      tags:
        - subpackage_bulkSubscriptionUpdates
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful response
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                subscription_ids:
                  type: array
                  items:
                    type: string
                  description: An array of subscription IDs to be updated
                new_status:
                  type: string
                  description: The new status to set for the subscriptions
              required:
                - subscription_ids
                - new_status
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/publicationId/subscriptions"

payload = {
    "subscription_ids": ["sub_1234-5678-9012-3456-7890", "sub_9876-5432-1098-7654-3210"],
    "new_status": "active"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/publicationId/subscriptions';
const options = {
  method: 'PUT',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"subscription_ids":["sub_1234-5678-9012-3456-7890","sub_9876-5432-1098-7654-3210"],"new_status":"active"}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/publicationId/subscriptions"

	payload := strings.NewReader("{\n  \"subscription_ids\": [\n    \"sub_1234-5678-9012-3456-7890\",\n    \"sub_9876-5432-1098-7654-3210\"\n  ],\n  \"new_status\": \"active\"\n}")

	req, _ := http.NewRequest("PUT", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/publicationId/subscriptions")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"subscription_ids\": [\n    \"sub_1234-5678-9012-3456-7890\",\n    \"sub_9876-5432-1098-7654-3210\"\n  ],\n  \"new_status\": \"active\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("https://api.beehiiv.com/v2/publications/publicationId/subscriptions")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"subscription_ids\": [\n    \"sub_1234-5678-9012-3456-7890\",\n    \"sub_9876-5432-1098-7654-3210\"\n  ],\n  \"new_status\": \"active\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'https://api.beehiiv.com/v2/publications/publicationId/subscriptions', [
  'body' => '{
  "subscription_ids": [
    "sub_1234-5678-9012-3456-7890",
    "sub_9876-5432-1098-7654-3210"
  ],
  "new_status": "active"
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/publicationId/subscriptions");
var request = new RestRequest(Method.PUT);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"subscription_ids\": [\n    \"sub_1234-5678-9012-3456-7890\",\n    \"sub_9876-5432-1098-7654-3210\"\n  ],\n  \"new_status\": \"active\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "subscription_ids": ["sub_1234-5678-9012-3456-7890", "sub_9876-5432-1098-7654-3210"],
  "new_status": "active"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/publicationId/subscriptions")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PUT"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# List condition sets <Badge intent="info" minimal outlined>OAuth Scope: condition_sets:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/condition_sets

Retrieve all active condition sets for a publication. Condition sets define reusable audience segments for targeting content to specific subscribers. Use the `purpose` parameter to filter by a specific use case.

Reference: https://developers.beehiiv.com/api-reference/condition-sets/index

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/condition_sets:
    get:
      operationId: index
      summary: >-
        List condition sets <Badge intent="info" minimal outlined>OAuth Scope:
        condition_sets:read</Badge>
      description: >-
        Retrieve all active condition sets for a publication. Condition sets
        define reusable audience segments for targeting content to specific
        subscribers. Use the `purpose` parameter to filter by a specific use
        case.
      tags:
        - subpackage_conditionSets
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: limit
          in: query
          description: >-
            A limit on the number of objects to be returned. The limit can range
            between 1 and 100, and the default is 10.
          required: false
          schema:
            type: integer
        - name: cursor
          in: query
          description: >-
            **Cursor-based pagination (recommended)**: Use this opaque cursor
            token to fetch the next page of results. When provided, pagination
            will use cursor-based method which is more efficient and consistent
            than offset-based pagination.
          required: false
          schema:
            type: string
        - name: page
          in: query
          description: >-
            **Offset-based pagination (deprecated)**: Page number for
            offset-based pagination. Please migrate to cursor-based pagination
            using the `cursor` parameter. If not specified, results 1-10 from
            page 1 will be returned.
          required: false
          schema:
            type: integer
        - name: purpose
          in: query
          description: >-
            Filter condition sets by purpose. When not specified, all active
            condition sets are returned.
          required: false
          schema:
            $ref: '#/components/schemas/type_conditionSets:ConditionSetPurpose'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_conditionSets:ConditionSetsListResponse
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_conditionSets:ConditionSetPurpose:
      type: string
      enum:
        - dynamic_content
      description: The purpose of the condition set, indicating its intended use.
      title: ConditionSetPurpose
    type_conditionSets:ConditionSetStatus:
      type: string
      enum:
        - active
        - archived
      title: ConditionSetStatus
    type_conditionSets:ConditionSetListItem:
      type: object
      properties:
        id:
          type: string
          description: The UUID of the condition set.
        name:
          type: string
          description: The display name of the condition set.
        status:
          $ref: '#/components/schemas/type_conditionSets:ConditionSetStatus'
          description: Whether the condition set is currently active or has been archived.
        created:
          type: integer
          description: >-
            The time the condition set was created. Measured in seconds since
            the Unix epoch.
        updated:
          type: integer
          description: >-
            The time the condition set was last updated. Measured in seconds
            since the Unix epoch.
        purpose:
          $ref: '#/components/schemas/type_conditionSets:ConditionSetPurpose'
          description: The purpose of the condition set, indicating its intended use.
      required:
        - id
        - name
        - status
        - created
        - updated
        - purpose
      title: ConditionSetListItem
    type_conditionSets:ConditionSetsListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/type_conditionSets:ConditionSetListItem'
          description: An array of condition sets.
        limit:
          type: integer
          description: >-
            The limit placed on the results. If no limit was specified in the
            request, this defaults to 10.
        has_more:
          type: boolean
          description: >-
            **Cursor pagination only**: Indicates whether there are more results
            available after the current page. Only present when using
            cursor-based pagination.
        next_cursor:
          type: string
          description: >-
            **Cursor pagination only**: The cursor token to use for fetching the
            next page of results. This will be null if has_more is false. Only
            present when using cursor-based pagination.
        total_results:
          type: integer
          description: The total number of results from all pages.
      required:
        - data
      title: ConditionSetsListResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python Default
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets"

querystring = {"limit":"10"}

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

```javascript Default
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets?limit=10';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Default
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets?limit=10"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Default
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets?limit=10")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java Default
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets?limit=10")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php Default
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets?limit=10', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp Default
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets?limit=10");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift Default
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets?limit=10")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get condition set <Badge intent="info" minimal outlined>OAuth Scope: condition_sets:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/condition_sets/{conditionSetId}

Retrieve a single active dynamic content condition set for a publication. Use `expand[]=stats` to calculate and return the active subscriber count synchronously.

Reference: https://developers.beehiiv.com/api-reference/condition-sets/show

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/condition_sets/{conditionSetId}:
    get:
      operationId: show
      summary: >-
        Get condition set <Badge intent="info" minimal outlined>OAuth Scope:
        condition_sets:read</Badge>
      description: >-
        Retrieve a single active dynamic content condition set for a
        publication. Use `expand[]=stats` to calculate and return the active
        subscriber count synchronously.
      tags:
        - subpackage_conditionSets
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: conditionSetId
          in: path
          description: The UUID of the condition set object
          required: true
          schema:
            type: string
        - name: expand[]
          in: query
          description: >-
            Optionally expand the response to include additional data.<br>
            `stats` - Calculates and returns the active subscriber count for
            this condition set synchronously.
          required: false
          schema:
            type: array
            items:
              $ref: >-
                #/components/schemas/type_conditionSets:ConditionSetShowExpandItems
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_conditionSets:ConditionSetShowResponse
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_conditionSets:ConditionSetShowExpandItems:
      type: string
      enum:
        - stats
      title: ConditionSetShowExpandItems
    type_conditionSets:ConditionSetStatus:
      type: string
      enum:
        - active
        - archived
      title: ConditionSetStatus
    type_conditionSets:ConditionSetPurpose:
      type: string
      enum:
        - dynamic_content
      description: The purpose of the condition set, indicating its intended use.
      title: ConditionSetPurpose
    type_conditionSets:ConditionSetStats:
      type: object
      properties:
        active_subscriber_count:
          type: integer
          description: >-
            Count of active subscribers matching this condition set, calculated
            synchronously at request time.
      required:
        - active_subscriber_count
      title: ConditionSetStats
    type_conditionSets:ConditionSet:
      type: object
      properties:
        id:
          type: string
          description: The UUID of the condition set.
        name:
          type: string
          description: The display name of the condition set.
        status:
          $ref: '#/components/schemas/type_conditionSets:ConditionSetStatus'
          description: Whether the condition set is currently active or has been archived.
        created:
          type: integer
          description: >-
            The time the condition set was created. Measured in seconds since
            the Unix epoch.
        updated:
          type: integer
          description: >-
            The time the condition set was last updated. Measured in seconds
            since the Unix epoch.
        purpose:
          $ref: '#/components/schemas/type_conditionSets:ConditionSetPurpose'
          description: The purpose of the condition set, indicating its intended use.
        stats:
          $ref: '#/components/schemas/type_conditionSets:ConditionSetStats'
          description: >-
            Subscriber count statistics for the condition set. Included when
            `expand[]=stats` is specified in the request.
      required:
        - id
        - name
        - status
        - created
        - updated
        - purpose
      title: ConditionSet
    type_conditionSets:ConditionSetShowResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_conditionSets:ConditionSet'
      required:
        - data
      title: ConditionSetShowResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets/00000000-0000-0000-0000-000000000000"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets/00000000-0000-0000-0000-000000000000';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets/00000000-0000-0000-0000-000000000000"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets/00000000-0000-0000-0000-000000000000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets/00000000-0000-0000-0000-000000000000")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets/00000000-0000-0000-0000-000000000000', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets/00000000-0000-0000-0000-000000000000");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets/00000000-0000-0000-0000-000000000000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

```python With stats expansion
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets/00000000-0000-0000-0000-000000000000"

querystring = {"expand[]":"[\"stats\"]"}

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

```javascript With stats expansion
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets/00000000-0000-0000-0000-000000000000?expand%5B%5D=%5B%22stats%22%5D';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go With stats expansion
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets/00000000-0000-0000-0000-000000000000?expand%5B%5D=%5B%22stats%22%5D"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby With stats expansion
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets/00000000-0000-0000-0000-000000000000?expand%5B%5D=%5B%22stats%22%5D")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java With stats expansion
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets/00000000-0000-0000-0000-000000000000?expand%5B%5D=%5B%22stats%22%5D")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php With stats expansion
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets/00000000-0000-0000-0000-000000000000?expand%5B%5D=%5B%22stats%22%5D', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp With stats expansion
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets/00000000-0000-0000-0000-000000000000?expand%5B%5D=%5B%22stats%22%5D");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift With stats expansion
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/condition_sets/00000000-0000-0000-0000-000000000000?expand%5B%5D=%5B%22stats%22%5D")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Create custom field <Badge intent="info" minimal outlined>OAuth Scope: custom_fields:write</Badge>

POST https://api.beehiiv.com/v2/publications/{publicationId}/custom_fields
Content-Type: application/json

Create a custom field on a publication, for use in subscriptions.

Reference: https://developers.beehiiv.com/api-reference/custom-fields/create

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/custom_fields:
    post:
      operationId: create
      summary: >-
        Create custom field <Badge intent="info" minimal outlined>OAuth Scope:
        custom_fields:write</Badge>
      description: Create a custom field on a publication, for use in subscriptions.
      tags:
        - subpackage_customFields
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_customFields:CustomFieldResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                kind:
                  $ref: '#/components/schemas/type_:CustomFieldType'
                display:
                  type: string
              required:
                - kind
                - display
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_:CustomFieldType:
      type: string
      enum:
        - string
        - integer
        - boolean
        - date
        - datetime
        - list
        - double
      description: The type of value being stored in the custom field.
      title: CustomFieldType
    type_customFields:CustomFieldInfo:
      type: object
      properties:
        id:
          type: string
        kind:
          $ref: '#/components/schemas/type_:CustomFieldType'
        display:
          type: string
        created:
          type: integer
        options:
          type: array
          items:
            type: string
          description: Array of option values. Only included when kind is "list".
      title: CustomFieldInfo
    type_customFields:CustomFieldResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_customFields:CustomFieldInfo'
      title: CustomFieldResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient, Beehiiv } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.customFields.create("publicationId", {
    kind: Beehiiv.CustomFieldsCreateRequestKind.String,
    display: "display"
});

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/publicationId/custom_fields"

payload = {
    "kind": "text",
    "display": "Subscriber Notes"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/publicationId/custom_fields"

	payload := strings.NewReader("{\n  \"kind\": \"text\",\n  \"display\": \"Subscriber Notes\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/publicationId/custom_fields")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"kind\": \"text\",\n  \"display\": \"Subscriber Notes\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.beehiiv.com/v2/publications/publicationId/custom_fields")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"kind\": \"text\",\n  \"display\": \"Subscriber Notes\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.beehiiv.com/v2/publications/publicationId/custom_fields', [
  'body' => '{
  "kind": "text",
  "display": "Subscriber Notes"
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/publicationId/custom_fields");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"kind\": \"text\",\n  \"display\": \"Subscriber Notes\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "kind": "text",
  "display": "Subscriber Notes"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/publicationId/custom_fields")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get custom field <Badge intent="info" minimal outlined>OAuth Scope: custom_fields:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/custom_fields/{id}

View a specific custom field on a publication.

Reference: https://developers.beehiiv.com/api-reference/custom-fields/show

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/custom_fields/{id}:
    get:
      operationId: show
      summary: >-
        Get custom field <Badge intent="info" minimal outlined>OAuth Scope:
        custom_fields:read</Badge>
      description: View a specific custom field on a publication.
      tags:
        - subpackage_customFields
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: id
          in: path
          description: The ID of the Custom Fields object
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_customFields:CustomFieldResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_:CustomFieldType:
      type: string
      enum:
        - string
        - integer
        - boolean
        - date
        - datetime
        - list
        - double
      description: The type of value being stored in the custom field.
      title: CustomFieldType
    type_customFields:CustomFieldInfo:
      type: object
      properties:
        id:
          type: string
        kind:
          $ref: '#/components/schemas/type_:CustomFieldType'
        display:
          type: string
        created:
          type: integer
        options:
          type: array
          items:
            type: string
          description: Array of option values. Only included when kind is "list".
      title: CustomFieldInfo
    type_customFields:CustomFieldResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_customFields:CustomFieldInfo'
      title: CustomFieldResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.customFields.get("publicationId", "id");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# List custom fields <Badge intent="info" minimal outlined>OAuth Scope: custom_fields:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/custom_fields

List all custom fields on a publication.

Reference: https://developers.beehiiv.com/api-reference/custom-fields/index

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/custom_fields:
    get:
      operationId: index
      summary: >-
        List custom fields <Badge intent="info" minimal outlined>OAuth Scope:
        custom_fields:read</Badge>
      description: List all custom fields on a publication.
      tags:
        - subpackage_customFields
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_customFields:CustomFieldIndexResponse
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_:CustomFieldType:
      type: string
      enum:
        - string
        - integer
        - boolean
        - date
        - datetime
        - list
        - double
      description: The type of value being stored in the custom field.
      title: CustomFieldType
    type_customFields:CustomFieldInfo:
      type: object
      properties:
        id:
          type: string
        kind:
          $ref: '#/components/schemas/type_:CustomFieldType'
        display:
          type: string
        created:
          type: integer
        options:
          type: array
          items:
            type: string
          description: Array of option values. Only included when kind is "list".
      title: CustomFieldInfo
    type_customFields:CustomFieldIndexResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/type_customFields:CustomFieldInfo'
        limit:
          type: integer
          description: >-
            The limit placed on the results. If no limit was specified in the
            request, this defaults to 10.
        page:
          type: integer
          default: 1
          description: >-
            The page number the results are from. If no page was specified in
            the request, this defaults to page 1.
        total_results:
          type: integer
          description: The total number of results from all pages.
        total_pages:
          type: integer
          description: The total number of pages.
      title: CustomFieldIndexResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/publicationId/custom_fields"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/publicationId/custom_fields';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/publicationId/custom_fields"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/publicationId/custom_fields")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/publicationId/custom_fields")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/publicationId/custom_fields', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/publicationId/custom_fields");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/publicationId/custom_fields")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Update custom field <Badge intent="info" minimal outlined>OAuth Scope: custom_fields:write</Badge>

PUT https://api.beehiiv.com/v2/publications/{publicationId}/custom_fields/{id}
Content-Type: application/json

Update a custom field on a publication.

Reference: https://developers.beehiiv.com/api-reference/custom-fields/put

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/custom_fields/{id}:
    put:
      operationId: put
      summary: >-
        Update custom field <Badge intent="info" minimal outlined>OAuth Scope:
        custom_fields:write</Badge>
      description: Update a custom field on a publication.
      tags:
        - subpackage_customFields
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: id
          in: path
          description: The ID of the Custom Fields object
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_customFields:CustomFieldResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                display:
                  type: string
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_:CustomFieldType:
      type: string
      enum:
        - string
        - integer
        - boolean
        - date
        - datetime
        - list
        - double
      description: The type of value being stored in the custom field.
      title: CustomFieldType
    type_customFields:CustomFieldInfo:
      type: object
      properties:
        id:
          type: string
        kind:
          $ref: '#/components/schemas/type_:CustomFieldType'
        display:
          type: string
        created:
          type: integer
        options:
          type: array
          items:
            type: string
          description: Array of option values. Only included when kind is "list".
      title: CustomFieldInfo
    type_customFields:CustomFieldResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_customFields:CustomFieldInfo'
      title: CustomFieldResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.customFields.put("publicationId", "id");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id"

payload = { "display": "New Display" }
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id"

	payload := strings.NewReader("{\n  \"display\": \"New Display\"\n}")

	req, _ := http.NewRequest("PUT", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"display\": \"New Display\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"display\": \"New Display\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id', [
  'body' => '{
  "display": "New Display"
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id");
var request = new RestRequest(Method.PUT);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"display\": \"New Display\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["display": "New Display"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PUT"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Delete custom field <Badge intent="info" minimal outlined>OAuth Scope: custom_fields:write</Badge>

DELETE https://api.beehiiv.com/v2/publications/{publicationId}/custom_fields/{id}

Delete a custom field from a publication.

Reference: https://developers.beehiiv.com/api-reference/custom-fields/delete

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/custom_fields/{id}:
    delete:
      operationId: delete
      summary: >-
        Delete custom field <Badge intent="info" minimal outlined>OAuth Scope:
        custom_fields:write</Badge>
      description: Delete a custom field from a publication.
      tags:
        - subpackage_customFields
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: id
          in: path
          description: The ID of the Custom Fields object
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '204':
          description: No Content
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_customFields:CustomFieldsDeleteResponse
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_customFields:CustomFieldsDeleteResponse:
      type: object
      properties:
        message:
          type: string
      title: CustomFieldsDeleteResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.customFields.delete("publicationId", "id");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id"

payload = {}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.delete(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("DELETE", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id");
var request = new RestRequest(Method.DELETE);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/publicationId/custom_fields/id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get publication engagements <Badge intent="info" minimal outlined>OAuth Scope: publications:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/engagements

Retrieve email engagement metrics for a specific publication over a defined date range and granularity.<br><br> By default, the endpoint returns metrics for the past day, aggregated daily. The max number of days allowed is 31. All dates and times are in UTC.

Reference: https://developers.beehiiv.com/api-reference/engagements/index

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/engagements:
    get:
      operationId: index
      summary: >-
        Get publication engagements <Badge intent="info" minimal outlined>OAuth
        Scope: publications:read</Badge>
      description: >-
        Retrieve email engagement metrics for a specific publication over a
        defined date range and granularity.<br><br> By default, the endpoint
        returns metrics for the past day, aggregated daily. The max number of
        days allowed is 31. All dates and times are in UTC.
      tags:
        - subpackage_engagements
      parameters:
        - name: publicationId
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: start_date
          in: query
          description: >-
            The starting date for the engagement metrics in `YYYY-MM-DD` format.
            Defaults to 1 day ago if not provided.
          required: false
          schema:
            type: string
            format: date
        - name: number_of_days
          in: query
          description: >-
            The number of days to return engagement metrics for, starting from
            `start_date`. Must be between 1 and 31. Defaults to `1` if not
            provided.
          required: false
          schema:
            $ref: '#/components/schemas/type_engagements:NumberOfDays'
        - name: granularity
          in: query
          description: >-
            The granularity at which to report the engagement metrics. Defaults
            to `day` if not provided.
          required: false
          schema:
            $ref: >-
              #/components/schemas/type_engagements:PublicationEngagementGranularity
        - name: email_type
          in: query
          description: >-
            Filter engagement metrics by email type. If omitted, all email
            engagement is included.<br> `post`: Only post emails.<br> `message`:
            Only automated and system-generated emails.
          required: false
          schema:
            $ref: >-
              #/components/schemas/type_engagements:PublicationEngagementEmailType
        - name: direction
          in: query
          description: >-
            The direction that the results are sorted in. Defaults to `asc`.<br>
            `asc`: Oldest to newest<br> `desc`: Newest to oldest
          required: false
          schema:
            $ref: '#/components/schemas/type_:RequestDirection'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_engagements:PublicationEngagementsResponse
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_engagements:NumberOfDays:
      type: integer
      title: NumberOfDays
    type_engagements:PublicationEngagementGranularity:
      type: string
      enum:
        - day
        - week
        - month
      title: PublicationEngagementGranularity
    type_engagements:PublicationEngagementEmailType:
      type: string
      enum:
        - all
        - post
        - message
      title: PublicationEngagementEmailType
    type_:RequestDirection:
      type: string
      enum:
        - asc
        - desc
      default: asc
      description: The direction of the request. Defaults to `asc`.
      title: RequestDirection
    type_engagements:PublicationEngagementMetrics:
      type: object
      properties:
        date:
          type: string
          format: date
          description: >-
            The starting date of the period for which the engagement metrics are
            reported based on the selected granularity.<br><br> `day`
            granularity: The specific day.<br> `week` granularity: The Monday of
            the week.<br> `month` granularity: The first day of the month.
        total_opens:
          type: integer
          description: The total number of times emails were opened during the period.
        unique_opens:
          type: integer
          description: >-
            The number of unique subscribers who opened emails during the
            period.
        total_clicks:
          type: integer
          description: The total number of times links were clicked during the period.
        total_verified_clicks:
          type: integer
          description: >-
            The total number of times links were clicked, during the period, as
            <a
            href="https://www.beehiiv.com/support/article/28404633659159-introducing-verified-clicks-accurate-email-engagement-metrics?srsltid=AfmBOoregRzZ1N6bcwITVRA-Lo6NE06y6xNwb7WO85Gv0mrWMij-yFgb">verified
            by our system</a>.
        unique_clicks:
          type: integer
          description: >-
            The number of unique subscribers who clicked links during the
            period.
        unique_verified_clicks:
          type: integer
          description: >-
            The number of times links were clicked by unique subscribers, during
            the period, as <a
            href="https://www.beehiiv.com/support/article/28404633659159-introducing-verified-clicks-accurate-email-engagement-metrics?srsltid=AfmBOoregRzZ1N6bcwITVRA-Lo6NE06y6xNwb7WO85Gv0mrWMij-yFgb">verified
            by our system</a>.
      required:
        - date
        - total_opens
        - unique_opens
        - total_clicks
        - total_verified_clicks
        - unique_clicks
        - unique_verified_clicks
      title: PublicationEngagementMetrics
    type_engagements:PublicationEngagementsResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/type_engagements:PublicationEngagementMetrics'
          description: >-
            The list of engagement metrics for the publication within the
            specified date range and granularity. Returns an empty list if there
            is no engagement data for the specified period.
        publication_id:
          $ref: '#/components/schemas/type_ids:PublicationId'
          description: >-
            The unique identifier of the publication. Passed as a path parameter
            in the request.
        granularity:
          $ref: >-
            #/components/schemas/type_engagements:PublicationEngagementGranularity
          description: The granularity at which the engagement metrics are reported.
        email_type:
          $ref: '#/components/schemas/type_engagements:PublicationEngagementEmailType'
          description: >-
            The email type filter applied to the engagement metrics. Defaults to
            `all`.
        start_date:
          type: string
          format: date
          description: The starting date of the engagement metrics.
        number_of_days:
          $ref: '#/components/schemas/type_engagements:NumberOfDays'
          description: The number of days of engagement metrics returned.
      required:
        - data
        - publication_id
        - granularity
        - email_type
        - start_date
        - number_of_days
      title: PublicationEngagementsResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_ad76629e-4a39-43ad-8055-0ee89dc6db15/engagements"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_ad76629e-4a39-43ad-8055-0ee89dc6db15/engagements';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_ad76629e-4a39-43ad-8055-0ee89dc6db15/engagements"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_ad76629e-4a39-43ad-8055-0ee89dc6db15/engagements")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_ad76629e-4a39-43ad-8055-0ee89dc6db15/engagements")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_ad76629e-4a39-43ad-8055-0ee89dc6db15/engagements', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_ad76629e-4a39-43ad-8055-0ee89dc6db15/engagements");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_ad76629e-4a39-43ad-8055-0ee89dc6db15/engagements")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# List polls <Badge intent="info" minimal outlined>OAuth Scope: polls:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/polls

Retrieve all polls belonging to a specific publication. Poll choices are always included. Use `expand[]=stats` to include aggregate vote counts per choice.

Reference: https://developers.beehiiv.com/api-reference/polls/index

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/polls:
    get:
      operationId: index
      summary: >-
        List polls <Badge intent="info" minimal outlined>OAuth Scope:
        polls:read</Badge>
      description: >-
        Retrieve all polls belonging to a specific publication. Poll choices are
        always included. Use `expand[]=stats` to include aggregate vote counts
        per choice.
      tags:
        - subpackage_polls
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: limit
          in: query
          description: >-
            A limit on the number of objects to be returned. The limit can range
            between 1 and 100, and the default is 10.
          required: false
          schema:
            type: integer
        - name: cursor
          in: query
          description: >-
            **Cursor-based pagination (recommended)**: Use this opaque cursor
            token to fetch the next page of results. When provided, pagination
            will use cursor-based method which is more efficient and consistent
            than offset-based pagination.
          required: false
          schema:
            type: string
        - name: page
          in: query
          description: >-
            **Offset-based pagination (deprecated)**: Page number for
            offset-based pagination. Please migrate to cursor-based pagination
            using the `cursor` parameter. If not specified, results 1-10 from
            page 1 will be returned.
          required: false
          schema:
            type: integer
        - name: order_by
          in: query
          description: >-
            The field that the results are sorted by. Defaults to created.<br>
            `created` - The time the poll was created.<br> `name` - The name of
            the poll.
          required: false
          schema:
            $ref: '#/components/schemas/type_polls:PollOrderBy'
        - name: direction
          in: query
          description: >-
            The direction that the results are sorted in. Defaults to asc.<br>
            `asc` - Ascending, sorts from smallest to largest.<br> `desc` -
            Descending, sorts from largest to smallest.
          required: false
          schema:
            $ref: '#/components/schemas/type_:RequestDirection'
        - name: expand[]
          in: query
          description: >-
            Optionally expand the response to include additional data.<br>
            `stats` - Returns aggregate vote counts per choice and total
            completions.<br> `poll_responses` - Returns up to 10 most recent
            subscriber responses. Use /polls/{pollId}/responses for paginated
            access to all responses.<br> `trivia_answer` - Returns the correct
            answer for trivia-type polls.
          required: false
          schema:
            type: array
            items:
              $ref: '#/components/schemas/type_polls:PollsExpandItems'
        - name: post_id
          in: query
          description: >-
            Filter to only return polls that were embedded in the specified
            post. Accepts a prefixed post ID (e.g. `post_abc123`).
          required: false
          schema:
            type: string
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_polls:PollsListResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_polls:PollOrderBy:
      type: string
      enum:
        - created
        - name
      default: created
      title: PollOrderBy
    type_:RequestDirection:
      type: string
      enum:
        - asc
        - desc
      default: asc
      description: The direction of the request. Defaults to `asc`.
      title: RequestDirection
    type_polls:PollsExpandItems:
      type: string
      enum:
        - stats
        - poll_responses
        - trivia_answer
      title: PollsExpandItems
    type_ids:PollId:
      type: string
      description: The prefixed ID of the poll.
      title: PollId
    type_polls:PollType:
      type: string
      enum:
        - voting
        - trivia
      title: PollType
    type_polls:PollStatus:
      type: string
      enum:
        - draft
        - published
      title: PollStatus
    type_polls:PollChoice:
      type: object
      properties:
        id:
          type: string
          description: The unique identifier of the poll choice.
        label:
          type: string
          description: The text label for this choice.
      required:
        - id
        - label
      title: PollChoice
    type_polls:PollStats:
      type: object
      properties:
        completions:
          type: integer
          description: The total number of responses to this poll.
        vote_counts:
          type: object
          additionalProperties:
            type: integer
          description: >-
            A map of poll choice labels to the number of votes each choice
            received.
      required:
        - completions
        - vote_counts
      title: PollStats
    type_ids:SubscriptionId:
      type: string
      description: The prefixed ID of the subscription.
      title: SubscriptionId
    type_polls:PollResponseItem:
      type: object
      properties:
        id:
          type: string
          description: The unique identifier of the poll response.
        subscription_id:
          $ref: '#/components/schemas/type_ids:SubscriptionId'
          description: The prefixed ID of the subscription that responded.
        poll_choice_id:
          type: string
          description: The UUID of the poll choice selected.
        poll_choice_label:
          type: string
          description: The text label of the poll choice selected.
        created_at:
          type: integer
          description: >-
            The time the response was created. Measured in seconds since the
            Unix epoch.
        extended_feedback:
          type: string
          description: Optional extended feedback provided by the subscriber.
        post_id:
          type: string
          description: >-
            The prefixed ID of the post where the response was collected. Only
            included when `expand[]=post` is specified.
        post_title:
          type: string
          description: >-
            The title of the post where the response was collected. Only
            included when `expand[]=post` is specified.
        post_publish_date:
          type: integer
          description: >-
            The scheduled publication date of the post where the response was
            collected. Measured in seconds since the Unix epoch. Only included
            when `expand[]=post` is specified. Null if the post is not yet
            scheduled.
      required:
        - id
        - subscription_id
        - poll_choice_id
        - created_at
      title: PollResponseItem
    type_polls:Poll:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:PollId'
          description: The prefixed ID of the poll.
        name:
          type: string
          description: The name of the poll.
        question:
          type: string
          description: The poll question text.
        description:
          type: string
          description: An optional description of the poll.
        poll_type:
          $ref: '#/components/schemas/type_polls:PollType'
          description: The type of poll.
        status:
          $ref: '#/components/schemas/type_polls:PollStatus'
          description: The current status of the poll.
        created_at:
          type: integer
          description: >-
            The time the poll was created. Measured in seconds since the Unix
            epoch.
        poll_choices:
          type: array
          items:
            $ref: '#/components/schemas/type_polls:PollChoice'
          description: The available choices for this poll.
        trivia_answer:
          type: string
          description: >-
            The correct answer for trivia-type polls. Only included when
            `expand[]=trivia_answer` is specified and the poll is of type
            trivia.
        stats:
          $ref: '#/components/schemas/type_polls:PollStats'
          description: >-
            Aggregate statistics for the poll. Only included when
            `expand[]=stats` is specified.
        total_responses:
          type: integer
          description: >-
            Total number of responses to this poll. Only included when
            `expand[]=poll_responses` is specified.
        poll_responses:
          type: array
          items:
            $ref: '#/components/schemas/type_polls:PollResponseItem'
          description: >-
            Up to 10 most recent subscriber responses. Only included when
            `expand[]=poll_responses` is specified. Use
            /polls/{pollId}/responses for paginated access to all responses.
      required:
        - id
        - name
        - question
        - poll_type
        - status
        - created_at
        - poll_choices
      title: Poll
    type_polls:PollsListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/type_polls:Poll'
          description: An array of polls.
        limit:
          type: integer
          description: >-
            The limit placed on the results. If no limit was specified in the
            request, this defaults to 10.
        page:
          type: integer
          default: 1
          description: >-
            **Offset pagination only**: The page number the results are from.
            Only present when using deprecated offset-based pagination.
        total_pages:
          type: integer
          description: >-
            **Offset pagination only**: The total number of pages. Only present
            when using deprecated offset-based pagination.
        has_more:
          type: boolean
          description: >-
            **Cursor pagination only**: Indicates whether there are more results
            available after the current page. Only present when using
            cursor-based pagination.
        next_cursor:
          type: string
          description: >-
            **Cursor pagination only**: The cursor token to use for fetching the
            next page of results. This will be null if has_more is false. Only
            present when using cursor-based pagination.
        total_results:
          type: integer
          description: The total number of results from all pages.
      required:
        - data
      title: PollsListResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python Cursor-based pagination
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls"

querystring = {"limit":"10"}

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

```javascript Cursor-based pagination
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?limit=10';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Cursor-based pagination
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?limit=10"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Cursor-based pagination
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?limit=10")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java Cursor-based pagination
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?limit=10")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php Cursor-based pagination
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?limit=10', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp Cursor-based pagination
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?limit=10");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift Cursor-based pagination
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?limit=10")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

```python With stats expansion
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls"

querystring = {"limit":"10","expand[]":"[\"stats\"]"}

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

```javascript With stats expansion
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?limit=10&expand%5B%5D=%5B%22stats%22%5D';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go With stats expansion
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?limit=10&expand%5B%5D=%5B%22stats%22%5D"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby With stats expansion
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?limit=10&expand%5B%5D=%5B%22stats%22%5D")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java With stats expansion
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?limit=10&expand%5B%5D=%5B%22stats%22%5D")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php With stats expansion
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?limit=10&expand%5B%5D=%5B%22stats%22%5D', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp With stats expansion
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?limit=10&expand%5B%5D=%5B%22stats%22%5D");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift With stats expansion
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?limit=10&expand%5B%5D=%5B%22stats%22%5D")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

```python Filtered by post
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls"

querystring = {"post_id":"post_00000000-0000-0000-0000-000000000000"}

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

```javascript Filtered by post
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?post_id=post_00000000-0000-0000-0000-000000000000';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Filtered by post
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?post_id=post_00000000-0000-0000-0000-000000000000"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Filtered by post
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?post_id=post_00000000-0000-0000-0000-000000000000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java Filtered by post
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?post_id=post_00000000-0000-0000-0000-000000000000")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php Filtered by post
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?post_id=post_00000000-0000-0000-0000-000000000000', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp Filtered by post
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?post_id=post_00000000-0000-0000-0000-000000000000");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift Filtered by post
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls?post_id=post_00000000-0000-0000-0000-000000000000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get poll <Badge intent="info" minimal outlined>OAuth Scope: polls:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/polls/{pollId}

Retrieve detailed information about a specific poll belonging to a publication. Use `expand[]=stats` for aggregate vote counts, or `expand[]=poll_responses` for individual subscriber responses.

Reference: https://developers.beehiiv.com/api-reference/polls/show

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/polls/{pollId}:
    get:
      operationId: show
      summary: >-
        Get poll <Badge intent="info" minimal outlined>OAuth Scope:
        polls:read</Badge>
      description: >-
        Retrieve detailed information about a specific poll belonging to a
        publication. Use `expand[]=stats` for aggregate vote counts, or
        `expand[]=poll_responses` for individual subscriber responses.
      tags:
        - subpackage_polls
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: pollId
          in: path
          description: The prefixed ID of the poll object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PollId'
        - name: expand[]
          in: query
          description: >-
            Optionally expand the response to include additional data.<br>
            `stats` - Returns aggregate vote counts per choice and total
            completions.<br> `poll_responses` - Returns up to 10 most recent
            subscriber responses. Use /polls/{pollId}/responses for paginated
            access to all responses.<br> `trivia_answer` - Returns the correct
            answer for trivia-type polls.
          required: false
          schema:
            type: array
            items:
              $ref: '#/components/schemas/type_polls:PollsExpandItems'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_polls:PollShowResponse'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:PollId:
      type: string
      description: The prefixed ID of the poll.
      title: PollId
    type_polls:PollsExpandItems:
      type: string
      enum:
        - stats
        - poll_responses
        - trivia_answer
      title: PollsExpandItems
    type_polls:PollType:
      type: string
      enum:
        - voting
        - trivia
      title: PollType
    type_polls:PollStatus:
      type: string
      enum:
        - draft
        - published
      title: PollStatus
    type_polls:PollChoice:
      type: object
      properties:
        id:
          type: string
          description: The unique identifier of the poll choice.
        label:
          type: string
          description: The text label for this choice.
      required:
        - id
        - label
      title: PollChoice
    type_polls:PollStats:
      type: object
      properties:
        completions:
          type: integer
          description: The total number of responses to this poll.
        vote_counts:
          type: object
          additionalProperties:
            type: integer
          description: >-
            A map of poll choice labels to the number of votes each choice
            received.
      required:
        - completions
        - vote_counts
      title: PollStats
    type_ids:SubscriptionId:
      type: string
      description: The prefixed ID of the subscription.
      title: SubscriptionId
    type_polls:PollResponseItem:
      type: object
      properties:
        id:
          type: string
          description: The unique identifier of the poll response.
        subscription_id:
          $ref: '#/components/schemas/type_ids:SubscriptionId'
          description: The prefixed ID of the subscription that responded.
        poll_choice_id:
          type: string
          description: The UUID of the poll choice selected.
        poll_choice_label:
          type: string
          description: The text label of the poll choice selected.
        created_at:
          type: integer
          description: >-
            The time the response was created. Measured in seconds since the
            Unix epoch.
        extended_feedback:
          type: string
          description: Optional extended feedback provided by the subscriber.
        post_id:
          type: string
          description: >-
            The prefixed ID of the post where the response was collected. Only
            included when `expand[]=post` is specified.
        post_title:
          type: string
          description: >-
            The title of the post where the response was collected. Only
            included when `expand[]=post` is specified.
        post_publish_date:
          type: integer
          description: >-
            The scheduled publication date of the post where the response was
            collected. Measured in seconds since the Unix epoch. Only included
            when `expand[]=post` is specified. Null if the post is not yet
            scheduled.
      required:
        - id
        - subscription_id
        - poll_choice_id
        - created_at
      title: PollResponseItem
    type_polls:Poll:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:PollId'
          description: The prefixed ID of the poll.
        name:
          type: string
          description: The name of the poll.
        question:
          type: string
          description: The poll question text.
        description:
          type: string
          description: An optional description of the poll.
        poll_type:
          $ref: '#/components/schemas/type_polls:PollType'
          description: The type of poll.
        status:
          $ref: '#/components/schemas/type_polls:PollStatus'
          description: The current status of the poll.
        created_at:
          type: integer
          description: >-
            The time the poll was created. Measured in seconds since the Unix
            epoch.
        poll_choices:
          type: array
          items:
            $ref: '#/components/schemas/type_polls:PollChoice'
          description: The available choices for this poll.
        trivia_answer:
          type: string
          description: >-
            The correct answer for trivia-type polls. Only included when
            `expand[]=trivia_answer` is specified and the poll is of type
            trivia.
        stats:
          $ref: '#/components/schemas/type_polls:PollStats'
          description: >-
            Aggregate statistics for the poll. Only included when
            `expand[]=stats` is specified.
        total_responses:
          type: integer
          description: >-
            Total number of responses to this poll. Only included when
            `expand[]=poll_responses` is specified.
        poll_responses:
          type: array
          items:
            $ref: '#/components/schemas/type_polls:PollResponseItem'
          description: >-
            Up to 10 most recent subscriber responses. Only included when
            `expand[]=poll_responses` is specified. Use
            /polls/{pollId}/responses for paginated access to all responses.
      required:
        - id
        - name
        - question
        - poll_type
        - status
        - created_at
        - poll_choices
      title: Poll
    type_polls:PollShowResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_polls:Poll'
      required:
        - data
      title: PollShowResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

```python With stats and responses
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000"

querystring = {"expand[]":"[\"stats\",\"poll_responses\"]"}

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

```javascript With stats and responses
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000?expand%5B%5D=%5B%22stats%22%2C%22poll_responses%22%5D';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go With stats and responses
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000?expand%5B%5D=%5B%22stats%22%2C%22poll_responses%22%5D"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby With stats and responses
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000?expand%5B%5D=%5B%22stats%22%2C%22poll_responses%22%5D")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java With stats and responses
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000?expand%5B%5D=%5B%22stats%22%2C%22poll_responses%22%5D")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php With stats and responses
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000?expand%5B%5D=%5B%22stats%22%2C%22poll_responses%22%5D', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp With stats and responses
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000?expand%5B%5D=%5B%22stats%22%2C%22poll_responses%22%5D");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift With stats and responses
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000?expand%5B%5D=%5B%22stats%22%2C%22poll_responses%22%5D")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# List poll responses <Badge intent="info" minimal outlined>OAuth Scope: polls:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/polls/{pollId}/responses

Retrieve all individual subscriber responses for a specific poll with cursor-based pagination. Use this endpoint for large datasets instead of the `expand[]=poll_responses` parameter on the poll show endpoint.

Reference: https://developers.beehiiv.com/api-reference/polls/list-responses

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/polls/{pollId}/responses:
    get:
      operationId: list-responses
      summary: >-
        List poll responses <Badge intent="info" minimal outlined>OAuth Scope:
        polls:read</Badge>
      description: >-
        Retrieve all individual subscriber responses for a specific poll with
        cursor-based pagination. Use this endpoint for large datasets instead of
        the `expand[]=poll_responses` parameter on the poll show endpoint.
      tags:
        - subpackage_polls
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: pollId
          in: path
          description: The prefixed ID of the poll object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PollId'
        - name: limit
          in: query
          description: >-
            A limit on the number of objects to be returned. The limit can range
            between 1 and 100, and the default is 10.
          required: false
          schema:
            type: integer
        - name: cursor
          in: query
          description: >-
            **Cursor-based pagination (recommended)**: Use this opaque cursor
            token to fetch the next page of results.
          required: false
          schema:
            type: string
        - name: page
          in: query
          description: >-
            **Offset-based pagination (deprecated)**: Page number for
            offset-based pagination.
          required: false
          schema:
            type: integer
        - name: order_by
          in: query
          description: The field that the results are sorted by. Defaults to created.
          required: false
          schema:
            $ref: '#/components/schemas/type_polls:PollResponsesOrderBy'
        - name: direction
          in: query
          description: >-
            The direction that the results are sorted in. Defaults to asc.<br>
            `asc` - Ascending, sorts from smallest to largest.<br> `desc` -
            Descending, sorts from largest to smallest.
          required: false
          schema:
            $ref: '#/components/schemas/type_:RequestDirection'
        - name: expand[]
          in: query
          description: >-
            Optionally expand the response to include additional data.<br>
            `post` - Returns the post title and publication date for the post
            where each response was collected.
          required: false
          schema:
            type: array
            items:
              $ref: '#/components/schemas/type_polls:PollResponsesExpandItems'
        - name: post_id
          in: query
          description: >-
            Filter to only return responses collected via the specified post.
            Accepts a prefixed post ID (e.g. `post_abc123`).
          required: false
          schema:
            type: string
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_polls:PollResponsesListResponse'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:PollId:
      type: string
      description: The prefixed ID of the poll.
      title: PollId
    type_polls:PollResponsesOrderBy:
      type: string
      enum:
        - created
      default: created
      title: PollResponsesOrderBy
    type_:RequestDirection:
      type: string
      enum:
        - asc
        - desc
      default: asc
      description: The direction of the request. Defaults to `asc`.
      title: RequestDirection
    type_polls:PollResponsesExpandItems:
      type: string
      enum:
        - post
      title: PollResponsesExpandItems
    type_ids:SubscriptionId:
      type: string
      description: The prefixed ID of the subscription.
      title: SubscriptionId
    type_polls:PollResponseItem:
      type: object
      properties:
        id:
          type: string
          description: The unique identifier of the poll response.
        subscription_id:
          $ref: '#/components/schemas/type_ids:SubscriptionId'
          description: The prefixed ID of the subscription that responded.
        poll_choice_id:
          type: string
          description: The UUID of the poll choice selected.
        poll_choice_label:
          type: string
          description: The text label of the poll choice selected.
        created_at:
          type: integer
          description: >-
            The time the response was created. Measured in seconds since the
            Unix epoch.
        extended_feedback:
          type: string
          description: Optional extended feedback provided by the subscriber.
        post_id:
          type: string
          description: >-
            The prefixed ID of the post where the response was collected. Only
            included when `expand[]=post` is specified.
        post_title:
          type: string
          description: >-
            The title of the post where the response was collected. Only
            included when `expand[]=post` is specified.
        post_publish_date:
          type: integer
          description: >-
            The scheduled publication date of the post where the response was
            collected. Measured in seconds since the Unix epoch. Only included
            when `expand[]=post` is specified. Null if the post is not yet
            scheduled.
      required:
        - id
        - subscription_id
        - poll_choice_id
        - created_at
      title: PollResponseItem
    type_polls:PollResponsesListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/type_polls:PollResponseItem'
          description: An array of poll responses.
        limit:
          type: integer
          description: >-
            The limit placed on the results. If no limit was specified in the
            request, this defaults to 10.
        page:
          type: integer
          default: 1
          description: >-
            **Offset pagination only**: The page number the results are from.
            Only present when using deprecated offset-based pagination.
        total_pages:
          type: integer
          description: >-
            **Offset pagination only**: The total number of pages. Only present
            when using deprecated offset-based pagination.
        has_more:
          type: boolean
          description: >-
            **Cursor pagination only**: Indicates whether there are more results
            available after the current page.
        next_cursor:
          type: string
          description: >-
            **Cursor pagination only**: The cursor token to use for fetching the
            next page of results.
        total_results:
          type: integer
          description: The total number of results from all pages.
      required:
        - data
      title: PollResponsesListResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses"

querystring = {"limit":"10"}

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?limit=10';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?limit=10"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?limit=10")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?limit=10")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?limit=10', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?limit=10");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?limit=10")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

```python With post context expansion
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses"

querystring = {"expand[]":"[\"post\"]"}

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

```javascript With post context expansion
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?expand%5B%5D=%5B%22post%22%5D';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go With post context expansion
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?expand%5B%5D=%5B%22post%22%5D"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby With post context expansion
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?expand%5B%5D=%5B%22post%22%5D")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java With post context expansion
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?expand%5B%5D=%5B%22post%22%5D")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php With post context expansion
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?expand%5B%5D=%5B%22post%22%5D', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp With post context expansion
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?expand%5B%5D=%5B%22post%22%5D");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift With post context expansion
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?expand%5B%5D=%5B%22post%22%5D")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

```python Filtered by post
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses"

querystring = {"post_id":"post_00000000-0000-0000-0000-000000000000"}

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

```javascript Filtered by post
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?post_id=post_00000000-0000-0000-0000-000000000000';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Filtered by post
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?post_id=post_00000000-0000-0000-0000-000000000000"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Filtered by post
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?post_id=post_00000000-0000-0000-0000-000000000000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java Filtered by post
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?post_id=post_00000000-0000-0000-0000-000000000000")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php Filtered by post
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?post_id=post_00000000-0000-0000-0000-000000000000', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp Filtered by post
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?post_id=post_00000000-0000-0000-0000-000000000000");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift Filtered by post
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/polls/poll_00000000-0000-0000-0000-000000000000/responses?post_id=post_00000000-0000-0000-0000-000000000000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Create post <Badge intent="info" minimal outlined>OAuth Scope: posts:write</Badge>

POST https://api.beehiiv.com/v2/publications/{publicationId}/posts
Content-Type: application/json

<Note title="Currently in beta" icon="b">
  This feature is currently in beta, the API is subject to change, and available only to Enterprise users.<br/><br/>To inquire about Enterprise pricing,
  please visit our <a href="https://www.beehiiv.com/enterprise">Enterprise page</a>.
</Note>
Create a post for a specific publication.

Reference: https://developers.beehiiv.com/api-reference/posts/create

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/posts:
    post:
      operationId: create
      summary: >-
        Create post <Badge intent="info" minimal outlined>OAuth Scope:
        posts:write</Badge>
      description: |-
        <Note title="Currently in beta" icon="b">
          This feature is currently in beta, the API is subject to change, and available only to Enterprise users.<br/><br/>To inquire about Enterprise pricing,
          please visit our <a href="https://www.beehiiv.com/enterprise">Enterprise page</a>.
        </Note>
        Create a post for a specific publication.
      tags:
        - subpackage_posts
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_posts:PostsCreateResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                body_content:
                  type: string
                  description: >-
                    The content of the post as raw HTML. Either this field OR
                    the blocks field must be provided.
                blocks:
                  type: array
                  items:
                    $ref: '#/components/schemas/type_posts:Block'
                  description: >-
                    The structured content blocks that make up the post. Either
                    this field OR the body_content field must be provided.
                title:
                  type: string
                  description: The title of the post.
                subtitle:
                  type: string
                  description: The subtitle of the post.
                post_template_id:
                  $ref: '#/components/schemas/type_ids:PostTemplateId'
                  description: >-
                    The ID of the template to use for the post. If not provided,
                    the default template will be used.
                status:
                  $ref: '#/components/schemas/type_posts:PostPublishStatus'
                  description: >-
                    The status of the post. If not provided, the default
                    (`confirmed`) value will be used and the post will either
                    publish immediately (if no `scheduled_at` is provided) or at
                    the `scheduled_at` time.
                scheduled_at:
                  type: string
                  format: date-time
                  description: >-
                    The time in which the post will be published. If not
                    provided, the post will be published immediately unless
                    `status` is set to `draft`. A draft post cannot be
                    scheduled.
                custom_link_tracking_enabled:
                  type: boolean
                  description: >-
                    If true, custom link tracking will be enabled for this post.
                    If not provided, the default value will be used.
                email_capture_type_override:
                  $ref: '#/components/schemas/type_posts:PostEmailCaptureTypeOverride'
                  description: >-
                    The email capture type to use for this post. If not
                    provided, the default value will be used.
                override_scheduled_at:
                  type: string
                  format: date-time
                  description: >-
                    If you wish to display a date other than the scheduled_at
                    date in the email, you can provide a date here. This will
                    not affect the actual publish date of the post.
                social_share:
                  $ref: '#/components/schemas/type_posts:PostSocialShare'
                  description: >-
                    The social share type to use for this post. If not provided,
                    the default value will be used.
                thumbnail_image_url:
                  type: string
                  description: >-
                    The URL of the thumbnail image to use for the post. If not
                    provided, the default value will be used.
                recipients:
                  $ref: '#/components/schemas/type_posts:PostRecipients'
                  description: >-
                    The recipients to use for this post. If not provided, the
                    default value will be used.
                email_settings:
                  $ref: '#/components/schemas/type_posts:PostEmailSettings'
                  description: >-
                    The email settings to use for this post. If not provided,
                    the default value will be used.
                web_settings:
                  $ref: '#/components/schemas/type_posts:PostWebSettings'
                  description: >-
                    The web settings to use for this post. If not provided, the
                    default value will be used.
                seo_settings:
                  $ref: '#/components/schemas/type_posts:PostMetadata'
                  description: >-
                    The metadata to use for this post. If not provided, the
                    default value will be used.
                content_tags:
                  type: array
                  items:
                    type: string
                  description: >-
                    The content tags to use for this post. If not provided, the
                    default value will be used.
                headers:
                  type: object
                  additionalProperties:
                    type: string
                  description: >-
                    The headers to use for this post. If not provided, the
                    default value will be used.
                custom_fields:
                  type: object
                  additionalProperties:
                    type: string
                  description: >-
                    The custom fields to use for this post. If not provided, the
                    default value will be used.
              required:
                - title
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_posts:BorderStyle:
      type: string
      enum:
        - solid
        - dashed
        - dotted
      title: BorderStyle
    type_posts:VisualSettings:
      type: object
      properties:
        background_color:
          type: string
          description: The background color of the block.
        text_color:
          type: string
          description: The text color of the block.
        border_color:
          type: string
          description: The border color of the block.
        border_style:
          $ref: '#/components/schemas/type_posts:BorderStyle'
          description: The border style of the block.
        border_width:
          type: integer
          description: The border width of the block.
        border_width_top:
          type: integer
          description: The border width of the top of the block.
        border_width_bottom:
          type: integer
          description: The border width of the bottom of the block.
        border_width_left:
          type: integer
          description: The border width of the left of the block.
        border_width_right:
          type: integer
          description: The border width of the right of the block.
        border_radius:
          type: integer
          description: The border radius of the block.
        border_radius_top_left:
          type: integer
          description: The border radius of the top left of the block.
        border_radius_top_right:
          type: integer
          description: The border radius of the top right of the block.
        border_radius_bottom_left:
          type: integer
          description: The border radius of the bottom left of the block.
        border_radius_bottom_right:
          type: integer
          description: The border radius of the bottom right of the block.
        inner_spacing:
          type: integer
          description: The inner spacing of the block.
        inner_spacing_top:
          type: integer
          description: The inner spacing of the top of the block.
        inner_spacing_bottom:
          type: integer
          description: The inner spacing of the bottom of the block.
        inner_spacing_left:
          type: integer
          description: The inner spacing of the left of the block.
        inner_spacing_right:
          type: integer
          description: The inner spacing of the right of the block.
        outer_spacing:
          type: integer
          description: The outer spacing of the block.
        outer_spacing_top:
          type: integer
          description: The outer spacing of the top of the block.
        outer_spacing_bottom:
          type: integer
          description: The outer spacing of the bottom of the block.
        outer_spacing_left:
          type: integer
          description: The outer spacing of the left of the block.
        outer_spacing_right:
          type: integer
          description: The outer spacing of the right of the block.
      title: VisualSettings
    type_posts:ReferralCondition:
      type: string
      enum:
        - eq
        - gt
        - lt
      title: ReferralCondition
    type_posts:ConditionSetOperator:
      type: string
      enum:
        - and
        - or
      description: >-
        How multiple condition sets are combined when evaluating dynamic content
        targeting.
      title: ConditionSetOperator
    type_posts:VisibilitySettings:
      type: object
      properties:
        show_on_web:
          type: boolean
          description: Whether to show the block on the web.
        show_on_email:
          type: boolean
          description: Whether to show the block on the email.
        show_to_anonymous_users_web:
          type: boolean
          description: Whether to show the block to anonymous users on the web.
        show_to_free_subscribers:
          type: boolean
          description: Whether to show the block to free subscribers.
        show_to_paid_subscribers:
          type: boolean
          description: Whether to show the block to paid subscribers.
        show_to_subscribers_with_referral_value:
          type: integer
          description: The exact referral count required to show the block to subscribers.
        show_to_subscribers_with_referral_condition:
          $ref: '#/components/schemas/type_posts:ReferralCondition'
          description: The condition required to show the block to subscribers.
        condition_set_ids:
          type: array
          items:
            type: string
          description: >-
            An optional list of condition set UUIDs to gate this block behind
            dynamic content targeting. When provided, only subscribers matching
            the specified condition sets will see this block. Condition sets
            must belong to the same publication and be active.
        condition_set_operator:
          $ref: '#/components/schemas/type_posts:ConditionSetOperator'
          description: >-
            Instructs how to combine multiple condition sets. Defaults to "or"
            (subscriber can match any condition). Use "and" to show the block if
            the subscriber meets all conditions.
      title: VisibilitySettings
    type_posts:Link:
      type: object
      properties:
        href:
          type: string
          description: The URL of the link.
        target:
          type: string
          description: The target of the link (e.g., _blank).
      required:
        - href
      title: Link
    type_posts:ParagrahBlockTextSection:
      type: object
      properties:
        text:
          type: string
          description: The text content of the paragraph.
        styling:
          type: array
          items:
            type: string
          description: The styling of the text (e.g., bold, italic).
        link:
          $ref: '#/components/schemas/type_posts:Link'
          description: The link of the text.
      required:
        - text
      title: ParagrahBlockTextSection
    type_posts:TextAlignment:
      type: string
      enum:
        - left
        - center
        - right
      description: The text alignment of the header.
      title: TextAlignment
    type_posts:Sizes:
      type: string
      enum:
        - small
        - normal
        - large
      description: The sizes of the button.
      title: Sizes
    type_posts:HeadingLevel:
      type: string
      enum:
        - '1'
        - '2'
        - '3'
        - '4'
        - '5'
        - '6'
      description: The level of the header.
      title: HeadingLevel
    type_ids:ExternalRssFeedId:
      type: string
      description: The prefixed ID of the external RSS feed.
      title: ExternalRssFeedId
    type_posts:RssBlockLayout:
      type: string
      enum:
        - 1-col
        - 2-col
        - 3-col
        - 4-col
      description: The layout of the articles from the feed.
      title: RssBlockLayout
    type_posts:RssCtaStyle:
      type: string
      enum:
        - CTA button
        - CTA link
        - Title as link
        - Thumbnail as link
        - Title and thumbnail as link
      description: The style of the call to action.
      title: RssCtaStyle
    type_posts:RssCtaAlignment:
      type: string
      enum:
        - Left
        - Center
        - Right
      description: The alignment of the call to action.
      title: RssCtaAlignment
    type_posts:RssThumbnailPosition:
      type: string
      enum:
        - Above Title
        - Below Title
        - Left of content
        - Right of content
        - Alternating Horizontally
      description: The position of the thumbnail.
      title: RssThumbnailPosition
    type_posts:EmbeddableBlocks:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - paragraph
              description: 'Discriminator value: paragraph'
            visual_settings:
              $ref: '#/components/schemas/type_posts:VisualSettings'
              description: Optional styling for borders, spacing, colors, etc.
            visibility_settings:
              $ref: '#/components/schemas/type_posts:VisibilitySettings'
              description: >-
                Optional rules for when/where this block is shown, including
                dynamic content targeting via condition sets.
            plaintext:
              type: string
              description: The plaintext content of the paragraph.
            formattedText:
              type: array
              items:
                $ref: '#/components/schemas/type_posts:ParagrahBlockTextSection'
              description: The formatted content of the paragraph.
          required:
            - type
        - type: object
          properties:
            type:
              type: string
              enum:
                - image
              description: 'Discriminator value: image'
            visual_settings:
              $ref: '#/components/schemas/type_posts:VisualSettings'
              description: Optional styling for borders, spacing, colors, etc.
            visibility_settings:
              $ref: '#/components/schemas/type_posts:VisibilitySettings'
              description: >-
                Optional rules for when/where this block is shown, including
                dynamic content targeting via condition sets.
            imageUrl:
              type: string
              description: The URL of the image.
            url:
              type: string
              description: The URL that the image should link to.
            title:
              type: string
              description: The title of the image.
            alt_text:
              type: string
              description: Alternative text for the image.
            caption:
              type: string
              description: A caption for the image.
            imageAlignment:
              $ref: '#/components/schemas/type_posts:TextAlignment'
              description: The text alignment of the image.
            captionAlignment:
              $ref: '#/components/schemas/type_posts:TextAlignment'
              description: The text alignment of the caption.
            width:
              type: integer
              description: The width of the image. Should be between 1 and 100.
          required:
            - type
            - imageUrl
        - type: object
          properties:
            type:
              type: string
              enum:
                - button
              description: 'Discriminator value: button'
            visual_settings:
              $ref: '#/components/schemas/type_posts:VisualSettings'
              description: Optional styling for borders, spacing, colors, etc.
            visibility_settings:
              $ref: '#/components/schemas/type_posts:VisibilitySettings'
              description: >-
                Optional rules for when/where this block is shown, including
                dynamic content targeting via condition sets.
            href:
              type: string
              description: The URL the button should use.
            text:
              type: string
              description: The text content of the button.
            target:
              type: string
              description: The target of the button (e.g., _blank).
            alignment:
              $ref: '#/components/schemas/type_posts:TextAlignment'
              description: The text alignment of the button.
            size:
              $ref: '#/components/schemas/type_posts:Sizes'
              description: The size of the button (e.g., small, normal, large).
          required:
            - type
            - href
            - text
        - type: object
          properties:
            type:
              type: string
              enum:
                - heading
              description: 'Discriminator value: heading'
            visual_settings:
              $ref: '#/components/schemas/type_posts:VisualSettings'
              description: Optional styling for borders, spacing, colors, etc.
            visibility_settings:
              $ref: '#/components/schemas/type_posts:VisibilitySettings'
              description: >-
                Optional rules for when/where this block is shown, including
                dynamic content targeting via condition sets.
            level:
              $ref: '#/components/schemas/type_posts:HeadingLevel'
              description: The level of the header (e.g., 1, 2, 3, etc.).
            textAlignment:
              $ref: '#/components/schemas/type_posts:TextAlignment'
              description: The text alignment of the header (e.g., left, center, right).
            text:
              type: string
              description: The text content of the header.
            anchorHeader:
              type: boolean
              default: true
              description: Whether the header should be an anchor header.
            anchorIncludeInToc:
              type: boolean
              default: true
              description: Whether the header should be included in the table of contents.
          required:
            - type
            - level
            - text
        - type: object
          properties:
            type:
              type: string
              enum:
                - rss
              description: 'Discriminator value: rss'
            visual_settings:
              $ref: '#/components/schemas/type_posts:VisualSettings'
              description: Optional styling for borders, spacing, colors, etc.
            visibility_settings:
              $ref: '#/components/schemas/type_posts:VisibilitySettings'
              description: >-
                Optional rules for when/where this block is shown, including
                dynamic content targeting via condition sets.
            externalRssFeedId:
              $ref: '#/components/schemas/type_ids:ExternalRssFeedId'
              description: The ID of the external RSS feed.
            rssFeedUrl:
              type: string
              description: The URL of the RSS feed.
            articleLayout:
              $ref: '#/components/schemas/type_posts:RssBlockLayout'
              description: The layout of the articles from the feed.
            articlesToShow:
              type: integer
              description: The number of articles to show from the feed.
            showCta:
              type: boolean
              description: Whether to show a call to action.
            ctaText:
              type: string
              description: >-
                The text of the call to action. Applicable if ctaStyle is button
                or link.
            ctaStyle:
              $ref: '#/components/schemas/type_posts:RssCtaStyle'
              description: The style of the call to action.
            ctaAlignment:
              $ref: '#/components/schemas/type_posts:RssCtaAlignment'
              description: The alignment of the call to action.
            refreshOnSend:
              type: boolean
              description: >-
                Whether or not to refresh the contents from the RSS feed before
                sending out the email.
            showArticleTitle:
              type: boolean
              description: Whether to show the article title.
            showArticleThumbnail:
              type: boolean
              description: Whether to show the article thumbnail.
            thumbnailPosition:
              $ref: '#/components/schemas/type_posts:RssThumbnailPosition'
              description: The position of the thumbnail.
            showAuthor:
              type: boolean
              description: Whether to show the author.
            showPublishedDate:
              type: boolean
              description: Whether to show the date the article was published
            showCategories:
              type: boolean
              description: Whether to show the categories.
            showDescription:
              type: boolean
              description: Whether to show the article description.
            showContent:
              type: boolean
              description: Whether to show the article content.
          required:
            - type
        - type: object
          properties:
            type:
              type: string
              enum:
                - advertisement
              description: 'Discriminator value: advertisement'
            visual_settings:
              $ref: '#/components/schemas/type_posts:VisualSettings'
              description: Optional styling for borders, spacing, colors, etc.
            visibility_settings:
              $ref: '#/components/schemas/type_posts:VisibilitySettings'
              description: >-
                Optional rules for when/where this block is shown, including
                dynamic content targeting via condition sets.
            opportunity_id:
              type: string
              description: The ID of the Advertisement opportunity.
          required:
            - type
            - opportunity_id
      discriminator:
        propertyName: type
      description: A block in the post content that can be embedded within a column.
      title: EmbeddableBlocks
    type_posts:ColumnBlock:
      type: object
      properties:
        blocks:
          type: array
          items:
            $ref: '#/components/schemas/type_posts:EmbeddableBlocks'
          description: The blocks that make up the column.
      required:
        - blocks
      title: ColumnBlock
    type_posts:ListType:
      type: string
      enum:
        - ordered
        - unordered
      description: The type of list (e.g., ordered, unordered).
      title: ListType
    type_posts:TableCellData:
      type: object
      properties:
        text:
          type: string
          description: The text content of the cell.
        alignment:
          $ref: '#/components/schemas/type_posts:TextAlignment'
          description: The text alignment of the cell.
      required:
        - text
      title: TableCellData
    type_ids:PollId:
      type: string
      description: The prefixed ID of the poll.
      title: PollId
    type_posts:QuoteVariant:
      type: string
      enum:
        - block
        - inline
        - quotation
      description: The variant of the quote block.
      title: QuoteVariant
    type_ids:PaywallId:
      type: string
      description: The prefixed ID of the paywall.
      title: PaywallId
    type_posts:Block:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - paragraph
              description: 'Discriminator value: paragraph'
            visual_settings:
              $ref: '#/components/schemas/type_posts:VisualSettings'
              description: Optional styling for borders, spacing, colors, etc.
            visibility_settings:
              $ref: '#/components/schemas/type_posts:VisibilitySettings'
              description: >-
                Optional rules for when/where this block is shown, including
                dynamic content targeting via condition sets.
            plaintext:
              type: string
              description: The plaintext content of the paragraph.
            formattedText:
              type: array
              items:
                $ref: '#/components/schemas/type_posts:ParagrahBlockTextSection'
              description: The formatted content of the paragraph.
          required:
            - type
        - type: object
          properties:
            type:
              type: string
              enum:
                - image
              description: 'Discriminator value: image'
            visual_settings:
              $ref: '#/components/schemas/type_posts:VisualSettings'
              description: Optional styling for borders, spacing, colors, etc.
            visibility_settings:
              $ref: '#/components/schemas/type_posts:VisibilitySettings'
              description: >-
                Optional rules for when/where this block is shown, including
                dynamic content targeting via condition sets.
            imageUrl:
              type: string
              description: The URL of the image.
            url:
              type: string
              description: The URL that the image should link to.
            title:
              type: string
              description: The title of the image.
            alt_text:
              type: string
              description: Alternative text for the image.
            caption:
              type: string
              description: A caption for the image.
            imageAlignment:
              $ref: '#/components/schemas/type_posts:TextAlignment'
              description: The text alignment of the image.
            captionAlignment:
              $ref: '#/components/schemas/type_posts:TextAlignment'
              description: The text alignment of the caption.
            width:
              type: integer
              description: The width of the image. Should be between 1 and 100.
          required:
            - type
            - imageUrl
        - type: object
          properties:
            type:
              type: string
              enum:
                - button
              description: 'Discriminator value: button'
            visual_settings:
              $ref: '#/components/schemas/type_posts:VisualSettings'
              description: Optional styling for borders, spacing, colors, etc.
            visibility_settings:
              $ref: '#/components/schemas/type_posts:VisibilitySettings'
              description: >-
                Optional rules for when/where this block is shown, including
                dynamic content targeting via condition sets.
            href:
              type: string
              description: The URL the button should use.
            text:
              type: string
              description: The text content of the button.
            target:
              type: string
              description: The target of the button (e.g., _blank).
            alignment:
              $ref: '#/components/schemas/type_posts:TextAlignment'
              description: The text alignment of the button.
            size:
              $ref: '#/components/schemas/type_posts:Sizes'
              description: The size of the button (e.g., small, normal, large).
          required:
            - type
            - href
            - text
        - type: object
          properties:
            type:
              type: string
              enum:
                - heading
              description: 'Discriminator value: heading'
            visual_settings:
              $ref: '#/components/schemas/type_posts:VisualSettings'
              description: Optional styling for borders, spacing, colors, etc.
            visibility_settings:
              $ref: '#/components/schemas/type_posts:VisibilitySettings'
              description: >-
                Optional rules for when/where this block is shown, including
                dynamic content targeting via condition sets.
            level:
              $ref: '#/components/schemas/type_posts:HeadingLevel'
              description: The level of the header (e.g., 1, 2, 3, etc.).
            textAlignment:
              $ref: '#/components/schemas/type_posts:TextAlignment'
              description: The text alignment of the header (e.g., left, center, right).
            text:
              type: string
              description: The text content of the header.
            anchorHeader:
              type: boolean
              default: true
              description: Whether the header should be an anchor header.
            anchorIncludeInToc:
              type: boolean
              default: true
              description: Whether the header should be included in the table of contents.
          required:
            - type
            - level
            - text
        - type: object
          properties:
            type:
              type: string
              enum:
                - rss
              description: 'Discriminator value: rss'
            visual_settings:
              $ref: '#/components/schemas/type_posts:VisualSettings'
              description: Optional styling for borders, spacing, colors, etc.
            visibility_settings:
              $ref: '#/components/schemas/type_posts:VisibilitySettings'
              description: >-
                Optional rules for when/where this block is shown, including
                dynamic content targeting via condition sets.
            externalRssFeedId:
              $ref: '#/components/schemas/type_ids:ExternalRssFeedId'
              description: The ID of the external RSS feed.
            rssFeedUrl:
              type: string
              description: The URL of the RSS feed.
            articleLayout:
              $ref: '#/components/schemas/type_posts:RssBlockLayout'
              description: The layout of the articles from the feed.
            articlesToShow:
              type: integer
              description: The number of articles to show from the feed.
            showCta:
              type: boolean
              description: Whether to show a call to action.
            ctaText:
              type: string
              description: >-
                The text of the call to action. Applicable if ctaStyle is button
                or link.
            ctaStyle:
              $ref: '#/components/schemas/type_posts:RssCtaStyle'
              description: The style of the call to action.
            ctaAlignment:
              $ref: '#/components/schemas/type_posts:RssCtaAlignment'
              description: The alignment of the call to action.
            refreshOnSend:
              type: boolean
              description: >-
                Whether or not to refresh the contents from the RSS feed before
                sending out the email.
            showArticleTitle:
              type: boolean
              description: Whether to show the article title.
            showArticleThumbnail:
              type: boolean
              description: Whether to show the article thumbnail.
            thumbnailPosition:
              $ref: '#/components/schemas/type_posts:RssThumbnailPosition'
              description: The position of the thumbnail.
            showAuthor:
              type: boolean
              description: Whether to show the author.
            showPublishedDate:
              type: boolean
              description: Whether to show the date the article was published
            showCategories:
              type: boolean
              description: Whether to show the categories.
            showDescription:
              type: boolean
              description: Whether to show the article description.
            showContent:
              type: boolean
              description: Whether to show the article content.
          required:
            - type
        - type: object
          properties:
            type:
              type: string
              enum:
                - advertisement
              description: 'Discriminator value: advertisement'
            visual_settings:
              $ref: '#/components/schemas/type_posts:VisualSettings'
              description: Optional styling for borders, spacing, colors, etc.
            visibility_settings:
              $ref: '#/components/schemas/type_posts:VisibilitySettings'
              description: >-
                Optional rules for when/where this block is shown, including
                dynamic content targeting via condition sets.
            opportunity_id:
              type: string
              description: The ID of the Advertisement opportunity.
          required:
            - type
            - opportunity_id
        - type: object
          properties:
            type:
              type: string
              enum:
                - columns
              description: 'Discriminator value: columns'
            visual_settings:
              $ref: '#/components/schemas/type_posts:VisualSettings'
              description: Optional styling for borders, spacing, colors, etc.
            visibility_settings:
              $ref: '#/components/schemas/type_posts:VisibilitySettings'
              description: >-
                Optional rules for when/where this block is shown, including
                dynamic content targeting via condition sets.
            columns:
              type: array
              items:
                $ref: '#/components/schemas/type_posts:ColumnBlock'
              description: The blocks that make up the columns.
          required:
            - type
            - columns
        - type: object
          properties:
            type:
              type: string
              enum:
                - list
              description: 'Discriminator value: list'
            visual_settings:
              $ref: '#/components/schemas/type_posts:VisualSettings'
              description: Optional styling for borders, spacing, colors, etc.
            visibility_settings:
              $ref: '#/components/schemas/type_posts:VisibilitySettings'
              description: >-
                Optional rules for when/where this block is shown, including
                dynamic content targeting via condition sets.
            items:
              type: array
              items:
                type: string
              description: The items in the list.
            listType:
              $ref: '#/components/schemas/type_posts:ListType'
              description: The type of list (e.g., ordered, unordered).
            startNumber:
              type: integer
              description: >-
                The number to start the list at. Only applicable if listType is
                ordered.
          required:
            - type
            - items
        - type: object
          properties:
            type:
              type: string
              enum:
                - table
              description: 'Discriminator value: table'
            visual_settings:
              $ref: '#/components/schemas/type_posts:VisualSettings'
              description: Optional styling for borders, spacing, colors, etc.
            visibility_settings:
              $ref: '#/components/schemas/type_posts:VisibilitySettings'
              description: >-
                Optional rules for when/where this block is shown, including
                dynamic content targeting via condition sets.
            rows:
              type: array
              items:
                type: array
                items:
                  $ref: '#/components/schemas/type_posts:TableCellData'
              description: The rows of the table.
            headerRow:
              type: boolean
              default: true
              description: Whether the first row is a header row.
            headerColumn:
              type: boolean
              default: false
              description: Whether the first column is a header column.
          required:
            - type
            - rows
        - type: object
          properties:
            type:
              type: string
              enum:
                - html
              description: 'Discriminator value: html'
            visual_settings:
              $ref: '#/components/schemas/type_posts:VisualSettings'
              description: Optional styling for borders, spacing, colors, etc.
            visibility_settings:
              $ref: '#/components/schemas/type_posts:VisibilitySettings'
              description: >-
                Optional rules for when/where this block is shown, including
                dynamic content targeting via condition sets.
            html:
              type: string
              description: The raw HTML content.
          required:
            - type
            - html
        - type: object
          properties:
            type:
              type: string
              enum:
                - embed_link
              description: 'Discriminator value: embed_link'
            visual_settings:
              $ref: '#/components/schemas/type_posts:VisualSettings'
              description: Optional styling for borders, spacing, colors, etc.
            visibility_settings:
              $ref: '#/components/schemas/type_posts:VisibilitySettings'
              description: >-
                Optional rules for when/where this block is shown, including
                dynamic content targeting via condition sets.
            url:
              type: string
              description: The URL of the embed link.
          required:
            - type
            - url
        - type: object
          properties:
            type:
              type: string
              enum:
                - poll
              description: 'Discriminator value: poll'
            visual_settings:
              $ref: '#/components/schemas/type_posts:VisualSettings'
              description: Optional styling for borders, spacing, colors, etc.
            visibility_settings:
              $ref: '#/components/schemas/type_posts:VisibilitySettings'
              description: >-
                Optional rules for when/where this block is shown, including
                dynamic content targeting via condition sets.
            poll_id:
              $ref: '#/components/schemas/type_ids:PollId'
              description: The ID of the poll you wish to include.
            show_options_initially:
              type: boolean
              description: Whether to show the poll options initially. Defaults to false.
          required:
            - type
            - poll_id
        - type: object
          properties:
            type:
              type: string
              enum:
                - quote
              description: 'Discriminator value: quote'
            visual_settings:
              $ref: '#/components/schemas/type_posts:VisualSettings'
              description: Optional styling for borders, spacing, colors, etc.
            visibility_settings:
              $ref: '#/components/schemas/type_posts:VisibilitySettings'
              description: >-
                Optional rules for when/where this block is shown, including
                dynamic content targeting via condition sets.
            variant:
              $ref: '#/components/schemas/type_posts:QuoteVariant'
              description: The type of quote block. Defaults to "block".
            quote:
              type: string
              description: The text of the quote.
            alignment:
              $ref: '#/components/schemas/type_posts:TextAlignment'
              description: The text alignment of the quote. Defaults depend on the variant.
            author:
              type: string
              description: The author of the quote.
          required:
            - type
            - quote
        - type: object
          properties:
            type:
              type: string
              enum:
                - content_break
              description: 'Discriminator value: content_break'
          required:
            - type
        - type: object
          properties:
            type:
              type: string
              enum:
                - paywall_break
              description: 'Discriminator value: paywall_break'
            paywall_id:
              $ref: '#/components/schemas/type_ids:PaywallId'
              description: The ID of the paywall.
          required:
            - type
            - paywall_id
      discriminator:
        propertyName: type
      description: A block in the post content.
      title: Block
    type_ids:PostTemplateId:
      type: string
      description: The prefixed ID of the post template.
      title: PostTemplateId
    type_posts:PostPublishStatus:
      type: string
      enum:
        - draft
        - confirmed
      default: confirmed
      title: PostPublishStatus
    type_posts:PostEmailCaptureTypeOverride:
      type: string
      enum:
        - none
        - gated
        - popup
      title: PostEmailCaptureTypeOverride
    type_posts:PostSocialShare:
      type: string
      enum:
        - comments_and_likes_only
        - with_comments_and_likes
        - top
        - none
      title: PostSocialShare
    type_ids:SegmentId:
      type: string
      description: The prefixed ID of the segment.
      title: SegmentId
    type_posts:PostWebRecipients:
      type: object
      properties:
        tier_ids:
          type: array
          items:
            type: string
        include_segment_ids:
          type: array
          items:
            $ref: '#/components/schemas/type_ids:SegmentId'
        exclude_segment_ids:
          type: array
          items:
            $ref: '#/components/schemas/type_ids:SegmentId'
      title: PostWebRecipients
    type_posts:PostEmailRecipients:
      type: object
      properties:
        tier_ids:
          type: array
          items:
            type: string
        include_segment_ids:
          type: array
          items:
            $ref: '#/components/schemas/type_ids:SegmentId'
        exclude_segment_ids:
          type: array
          items:
            $ref: '#/components/schemas/type_ids:SegmentId'
      title: PostEmailRecipients
    type_posts:PostRecipients:
      type: object
      properties:
        web:
          $ref: '#/components/schemas/type_posts:PostWebRecipients'
        email:
          $ref: '#/components/schemas/type_posts:PostEmailRecipients'
      required:
        - web
        - email
      title: PostRecipients
    type_posts:PostEmailSettings:
      type: object
      properties:
        from_address:
          type: string
        custom_live_url:
          type: string
        display_title_in_email:
          type: boolean
        display_byline_in_email:
          type: boolean
        display_subtitle_in_email:
          type: boolean
        email_header_engagement_buttons:
          type: string
        email_header_social_share:
          type: string
        email_preview_text:
          type: string
        email_subject_line:
          type: string
      title: PostEmailSettings
    type_ids:PriceId:
      type: string
      description: The prefixed ID of the price.
      title: PriceId
    type_posts:PostWebSettings:
      type: object
      properties:
        display_thumbnail_on_web:
          type: boolean
        hide_from_feed:
          type: boolean
        paywall_break_price_id:
          $ref: '#/components/schemas/type_ids:PriceId'
        paywall_id:
          $ref: '#/components/schemas/type_ids:PaywallId'
        slug:
          type: string
      title: PostWebSettings
    type_posts:PostMetadata:
      type: object
      properties:
        default_description:
          type: string
        default_title:
          type: string
        og_description:
          type: string
        og_title:
          type: string
        twitter_description:
          type: string
        twitter_title:
          type: string
      title: PostMetadata
    type_ids:PostId:
      type: string
      description: The prefixed ID of the post.
      title: PostId
    type_:PostCreate:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:PostId'
          description: The prefixed post id
      required:
        - id
      title: PostCreate
    type_posts:PostsCreateResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_:PostCreate'
      required:
        - data
      title: PostsCreateResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts"

payload = {
    "title": "The Kitchen Sink Post (refactored version)",
    "blocks": [
        {
            "type": "heading",
            "level": "2",
            "text": "This is my block!!!",
            "anchorHeader": False,
            "anchorIncludeInToc": False,
            "textAlignment": "center"
        },
        {
            "type": "list",
            "items": ["a", "b", "c"],
            "listType": "ordered"
        },
        {
            "type": "list",
            "items": ["d", "e", "f"],
            "listType": "ordered",
            "startNumber": 4
        },
        {
            "type": "list",
            "items": ["g", "h", "i"],
            "listType": "unordered",
            "startNumber": 4
        },
        {
            "type": "table",
            "rows": [[
                    { "text": "A" },
                    {
                        "text": "B",
                        "alignment": "center"
                    },
                    {
                        "text": "C",
                        "alignment": "right"
                    }
                ], [
                    {
                        "text": "D",
                        "alignment": "right"
                    },
                    {
                        "text": "E",
                        "alignment": "center"
                    },
                    {
                        "text": "F",
                        "alignment": "left"
                    }
                ]],
            "headerColumn": True,
            "headerRow": True
        },
        {
            "type": "table",
            "rows": [[{ "text": "A" }, { "text": "B" }, { "text": "C" }], [{ "text": "D" }, { "text": "E" }, { "text": "F" }]]
        },
        {
            "type": "table",
            "rows": [[{ "text": "A" }, { "text": "B" }, { "text": "C" }], [{ "text": "D" }, { "text": "E" }, { "text": "F" }]],
            "headerRow": False
        },
        {
            "type": "columns",
            "columns": [{ "blocks": [
                        {
                            "type": "paragraph",
                            "plaintext": "Marble Column 1 {{email}}"
                        }
                    ] }, { "blocks": [
                        {
                            "type": "image",
                            "imageUrl": "https://cdn.britannica.com/89/164789-050-D6B5E2C7/Barack-Obama-2012.jpg",
                            "alt_text": "A picture of Barry Obama",
                            "caption": "One Cool President",
                            "captionAlignment": "center",
                            "imageAlignment": "right",
                            "title": "Barry O",
                            "url": "https://www.whitehouse.gov/",
                            "width": 75
                        }
                    ] }]
        },
        {
            "type": "advertisement",
            "opportunity_id": "d8dfa6be-24b5-4cad-8350-ae44366dbd4c"
        },
        {
            "type": "image",
            "imageUrl": "https://cdn.britannica.com/89/164789-050-D6B5E2C7/Barack-Obama-2012.jpg",
            "alt_text": "A picture of Barry Obama",
            "caption": "One Cool President",
            "captionAlignment": "center",
            "imageAlignment": "right",
            "title": "Barry O",
            "url": "https://www.whitehouse.gov/",
            "width": 75
        },
        {
            "type": "paragraph",
            "formattedText": [
                { "text": "This is going to be " },
                {
                    "text": "a really, really awesome time ",
                    "styling": ["bold"]
                },
                {
                    "text": "Are you ready for this?",
                    "styling": ["italic", "bold"]
                }
            ]
        },
        {
            "type": "button",
            "href": "/subscribe",
            "text": "Subscribe",
            "alignment": "center",
            "size": "large",
            "target": "_blank"
        },
        {
            "type": "button",
            "href": "/signup",
            "text": "Sign Up",
            "alignment": "right",
            "size": "small",
            "target": "_blank"
        },
        {
            "type": "button",
            "href": "/",
            "text": "View Posts",
            "target": "_blank"
        },
        {
            "type": "heading",
            "level": "4",
            "text": "This is my block!!!",
            "anchorHeader": True,
            "anchorIncludeInToc": True,
            "textAlignment": "right"
        }
    ],
    "subtitle": "Contains lots of examples of each block type and the various settings you could use",
    "post_template_id": "post_template_00000000-0000-0000-0000-000000000000",
    "scheduled_at": "2024-12-25T12:00:00Z",
    "custom_link_tracking_enabled": True,
    "email_capture_type_override": "none",
    "override_scheduled_at": "2022-10-26T14:01:16Z",
    "social_share": "comments_and_likes_only",
    "thumbnail_image_url": "https://images.squarespace-cdn.com/content/v1/56e4ca0540261d39b90e4b18/1605047208324-PONGEYKEAKTMM1LANHJ5/1ED706BF-A70B-4F26-B3D5-266B449DDA8A_1_105_c.jpeg",
    "recipients": {
        "web": { "tier_ids": ["premium"] },
        "email": {
            "tier_ids": ["premium", "free"],
            "include_segment_ids": ["seg_6426b403-39f5-42bd-86e9-9533fb0099e7"],
            "exclude_segment_ids": ["seg_e34b4085-aef6-449f-a699-7563f915f852"]
        }
    },
    "email_settings": {
        "from_address": "from_address",
        "custom_live_url": "https://beehiiv.com",
        "display_title_in_email": True,
        "display_byline_in_email": True,
        "display_subtitle_in_email": True,
        "email_header_engagement_buttons": "email_header_engagement_buttons",
        "email_header_social_share": "email_header_social_share",
        "email_preview_text": "email_preview_text",
        "email_subject_line": "email_subject_line"
    },
    "web_settings": {
        "display_thumbnail_on_web": True,
        "hide_from_feed": True,
        "slug": "and-this-is-gonna-rock"
    },
    "seo_settings": {
        "default_description": "default_description",
        "default_title": "default_title",
        "og_description": "OpenGraph description",
        "og_title": "Opengraph Title",
        "twitter_description": "Twitter Stuff",
        "twitter_title": "My Twitter Article"
    },
    "content_tags": ["Obama", "Care", "Rocks", "Healthcare"]
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"title":"The Kitchen Sink Post (refactored version)","blocks":[{"type":"heading","level":"2","text":"This is my block!!!","anchorHeader":false,"anchorIncludeInToc":false,"textAlignment":"center"},{"type":"list","items":["a","b","c"],"listType":"ordered"},{"type":"list","items":["d","e","f"],"listType":"ordered","startNumber":4},{"type":"list","items":["g","h","i"],"listType":"unordered","startNumber":4},{"type":"table","rows":[[{"text":"A"},{"text":"B","alignment":"center"},{"text":"C","alignment":"right"}],[{"text":"D","alignment":"right"},{"text":"E","alignment":"center"},{"text":"F","alignment":"left"}]],"headerColumn":true,"headerRow":true},{"type":"table","rows":[[{"text":"A"},{"text":"B"},{"text":"C"}],[{"text":"D"},{"text":"E"},{"text":"F"}]]},{"type":"table","rows":[[{"text":"A"},{"text":"B"},{"text":"C"}],[{"text":"D"},{"text":"E"},{"text":"F"}]],"headerRow":false},{"type":"columns","columns":[{"blocks":[{"type":"paragraph","plaintext":"Marble Column 1 {{email}}"}]},{"blocks":[{"type":"image","imageUrl":"https://cdn.britannica.com/89/164789-050-D6B5E2C7/Barack-Obama-2012.jpg","alt_text":"A picture of Barry Obama","caption":"One Cool President","captionAlignment":"center","imageAlignment":"right","title":"Barry O","url":"https://www.whitehouse.gov/","width":75}]}]},{"type":"advertisement","opportunity_id":"d8dfa6be-24b5-4cad-8350-ae44366dbd4c"},{"type":"image","imageUrl":"https://cdn.britannica.com/89/164789-050-D6B5E2C7/Barack-Obama-2012.jpg","alt_text":"A picture of Barry Obama","caption":"One Cool President","captionAlignment":"center","imageAlignment":"right","title":"Barry O","url":"https://www.whitehouse.gov/","width":75},{"type":"paragraph","formattedText":[{"text":"This is going to be "},{"text":"a really, really awesome time ","styling":["bold"]},{"text":"Are you ready for this?","styling":["italic","bold"]}]},{"type":"button","href":"/subscribe","text":"Subscribe","alignment":"center","size":"large","target":"_blank"},{"type":"button","href":"/signup","text":"Sign Up","alignment":"right","size":"small","target":"_blank"},{"type":"button","href":"/","text":"View Posts","target":"_blank"},{"type":"heading","level":"4","text":"This is my block!!!","anchorHeader":true,"anchorIncludeInToc":true,"textAlignment":"right"}],"subtitle":"Contains lots of examples of each block type and the various settings you could use","post_template_id":"post_template_00000000-0000-0000-0000-000000000000","scheduled_at":"2024-12-25T12:00:00Z","custom_link_tracking_enabled":true,"email_capture_type_override":"none","override_scheduled_at":"2022-10-26T14:01:16Z","social_share":"comments_and_likes_only","thumbnail_image_url":"https://images.squarespace-cdn.com/content/v1/56e4ca0540261d39b90e4b18/1605047208324-PONGEYKEAKTMM1LANHJ5/1ED706BF-A70B-4F26-B3D5-266B449DDA8A_1_105_c.jpeg","recipients":{"web":{"tier_ids":["premium"]},"email":{"tier_ids":["premium","free"],"include_segment_ids":["seg_6426b403-39f5-42bd-86e9-9533fb0099e7"],"exclude_segment_ids":["seg_e34b4085-aef6-449f-a699-7563f915f852"]}},"email_settings":{"from_address":"from_address","custom_live_url":"https://beehiiv.com","display_title_in_email":true,"display_byline_in_email":true,"display_subtitle_in_email":true,"email_header_engagement_buttons":"email_header_engagement_buttons","email_header_social_share":"email_header_social_share","email_preview_text":"email_preview_text","email_subject_line":"email_subject_line"},"web_settings":{"display_thumbnail_on_web":true,"hide_from_feed":true,"slug":"and-this-is-gonna-rock"},"seo_settings":{"default_description":"default_description","default_title":"default_title","og_description":"OpenGraph description","og_title":"Opengraph Title","twitter_description":"Twitter Stuff","twitter_title":"My Twitter Article"},"content_tags":["Obama","Care","Rocks","Healthcare"]}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts"

	payload := strings.NewReader("{\n  \"title\": \"The Kitchen Sink Post (refactored version)\",\n  \"blocks\": [\n    {\n      \"type\": \"heading\",\n      \"level\": \"2\",\n      \"text\": \"This is my block!!!\",\n      \"anchorHeader\": false,\n      \"anchorIncludeInToc\": false,\n      \"textAlignment\": \"center\"\n    },\n    {\n      \"type\": \"list\",\n      \"items\": [\n        \"a\",\n        \"b\",\n        \"c\"\n      ],\n      \"listType\": \"ordered\"\n    },\n    {\n      \"type\": \"list\",\n      \"items\": [\n        \"d\",\n        \"e\",\n        \"f\"\n      ],\n      \"listType\": \"ordered\",\n      \"startNumber\": 4\n    },\n    {\n      \"type\": \"list\",\n      \"items\": [\n        \"g\",\n        \"h\",\n        \"i\"\n      ],\n      \"listType\": \"unordered\",\n      \"startNumber\": 4\n    },\n    {\n      \"type\": \"table\",\n      \"rows\": [\n        [\n          {\n            \"text\": \"A\"\n          },\n          {\n            \"text\": \"B\",\n            \"alignment\": \"center\"\n          },\n          {\n            \"text\": \"C\",\n            \"alignment\": \"right\"\n          }\n        ],\n        [\n          {\n            \"text\": \"D\",\n            \"alignment\": \"right\"\n          },\n          {\n            \"text\": \"E\",\n            \"alignment\": \"center\"\n          },\n          {\n            \"text\": \"F\",\n            \"alignment\": \"left\"\n          }\n        ]\n      ],\n      \"headerColumn\": true,\n      \"headerRow\": true\n    },\n    {\n      \"type\": \"table\",\n      \"rows\": [\n        [\n          {\n            \"text\": \"A\"\n          },\n          {\n            \"text\": \"B\"\n          },\n          {\n            \"text\": \"C\"\n          }\n        ],\n        [\n          {\n            \"text\": \"D\"\n          },\n          {\n            \"text\": \"E\"\n          },\n          {\n            \"text\": \"F\"\n          }\n        ]\n      ]\n    },\n    {\n      \"type\": \"table\",\n      \"rows\": [\n        [\n          {\n            \"text\": \"A\"\n          },\n          {\n            \"text\": \"B\"\n          },\n          {\n            \"text\": \"C\"\n          }\n        ],\n        [\n          {\n            \"text\": \"D\"\n          },\n          {\n            \"text\": \"E\"\n          },\n          {\n            \"text\": \"F\"\n          }\n        ]\n      ],\n      \"headerRow\": false\n    },\n    {\n      \"type\": \"columns\",\n      \"columns\": [\n        {\n          \"blocks\": [\n            {\n              \"type\": \"paragraph\",\n              \"plaintext\": \"Marble Column 1 {{email}}\"\n            }\n          ]\n        },\n        {\n          \"blocks\": [\n            {\n              \"type\": \"image\",\n              \"imageUrl\": \"https://cdn.britannica.com/89/164789-050-D6B5E2C7/Barack-Obama-2012.jpg\",\n              \"alt_text\": \"A picture of Barry Obama\",\n              \"caption\": \"One Cool President\",\n              \"captionAlignment\": \"center\",\n              \"imageAlignment\": \"right\",\n              \"title\": \"Barry O\",\n              \"url\": \"https://www.whitehouse.gov/\",\n              \"width\": 75\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"type\": \"advertisement\",\n      \"opportunity_id\": \"d8dfa6be-24b5-4cad-8350-ae44366dbd4c\"\n    },\n    {\n      \"type\": \"image\",\n      \"imageUrl\": \"https://cdn.britannica.com/89/164789-050-D6B5E2C7/Barack-Obama-2012.jpg\",\n      \"alt_text\": \"A picture of Barry Obama\",\n      \"caption\": \"One Cool President\",\n      \"captionAlignment\": \"center\",\n      \"imageAlignment\": \"right\",\n      \"title\": \"Barry O\",\n      \"url\": \"https://www.whitehouse.gov/\",\n      \"width\": 75\n    },\n    {\n      \"type\": \"paragraph\",\n      \"formattedText\": [\n        {\n          \"text\": \"This is going to be \"\n        },\n        {\n          \"text\": \"a really, really awesome time \",\n          \"styling\": [\n            \"bold\"\n          ]\n        },\n        {\n          \"text\": \"Are you ready for this?\",\n          \"styling\": [\n            \"italic\",\n            \"bold\"\n          ]\n        }\n      ]\n    },\n    {\n      \"type\": \"button\",\n      \"href\": \"/subscribe\",\n      \"text\": \"Subscribe\",\n      \"alignment\": \"center\",\n      \"size\": \"large\",\n      \"target\": \"_blank\"\n    },\n    {\n      \"type\": \"button\",\n      \"href\": \"/signup\",\n      \"text\": \"Sign Up\",\n      \"alignment\": \"right\",\n      \"size\": \"small\",\n      \"target\": \"_blank\"\n    },\n    {\n      \"type\": \"button\",\n      \"href\": \"/\",\n      \"text\": \"View Posts\",\n      \"target\": \"_blank\"\n    },\n    {\n      \"type\": \"heading\",\n      \"level\": \"4\",\n      \"text\": \"This is my block!!!\",\n      \"anchorHeader\": true,\n      \"anchorIncludeInToc\": true,\n      \"textAlignment\": \"right\"\n    }\n  ],\n  \"subtitle\": \"Contains lots of examples of each block type and the various settings you could use\",\n  \"post_template_id\": \"post_template_00000000-0000-0000-0000-000000000000\",\n  \"scheduled_at\": \"2024-12-25T12:00:00Z\",\n  \"custom_link_tracking_enabled\": true,\n  \"email_capture_type_override\": \"none\",\n  \"override_scheduled_at\": \"2022-10-26T14:01:16Z\",\n  \"social_share\": \"comments_and_likes_only\",\n  \"thumbnail_image_url\": \"https://images.squarespace-cdn.com/content/v1/56e4ca0540261d39b90e4b18/1605047208324-PONGEYKEAKTMM1LANHJ5/1ED706BF-A70B-4F26-B3D5-266B449DDA8A_1_105_c.jpeg\",\n  \"recipients\": {\n    \"web\": {\n      \"tier_ids\": [\n        \"premium\"\n      ]\n    },\n    \"email\": {\n      \"tier_ids\": [\n        \"premium\",\n        \"free\"\n      ],\n      \"include_segment_ids\": [\n        \"seg_6426b403-39f5-42bd-86e9-9533fb0099e7\"\n      ],\n      \"exclude_segment_ids\": [\n        \"seg_e34b4085-aef6-449f-a699-7563f915f852\"\n      ]\n    }\n  },\n  \"email_settings\": {\n    \"from_address\": \"from_address\",\n    \"custom_live_url\": \"https://beehiiv.com\",\n    \"display_title_in_email\": true,\n    \"display_byline_in_email\": true,\n    \"display_subtitle_in_email\": true,\n    \"email_header_engagement_buttons\": \"email_header_engagement_buttons\",\n    \"email_header_social_share\": \"email_header_social_share\",\n    \"email_preview_text\": \"email_preview_text\",\n    \"email_subject_line\": \"email_subject_line\"\n  },\n  \"web_settings\": {\n    \"display_thumbnail_on_web\": true,\n    \"hide_from_feed\": true,\n    \"slug\": \"and-this-is-gonna-rock\"\n  },\n  \"seo_settings\": {\n    \"default_description\": \"default_description\",\n    \"default_title\": \"default_title\",\n    \"og_description\": \"OpenGraph description\",\n    \"og_title\": \"Opengraph Title\",\n    \"twitter_description\": \"Twitter Stuff\",\n    \"twitter_title\": \"My Twitter Article\"\n  },\n  \"content_tags\": [\n    \"Obama\",\n    \"Care\",\n    \"Rocks\",\n    \"Healthcare\"\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"title\": \"The Kitchen Sink Post (refactored version)\",\n  \"blocks\": [\n    {\n      \"type\": \"heading\",\n      \"level\": \"2\",\n      \"text\": \"This is my block!!!\",\n      \"anchorHeader\": false,\n      \"anchorIncludeInToc\": false,\n      \"textAlignment\": \"center\"\n    },\n    {\n      \"type\": \"list\",\n      \"items\": [\n        \"a\",\n        \"b\",\n        \"c\"\n      ],\n      \"listType\": \"ordered\"\n    },\n    {\n      \"type\": \"list\",\n      \"items\": [\n        \"d\",\n        \"e\",\n        \"f\"\n      ],\n      \"listType\": \"ordered\",\n      \"startNumber\": 4\n    },\n    {\n      \"type\": \"list\",\n      \"items\": [\n        \"g\",\n        \"h\",\n        \"i\"\n      ],\n      \"listType\": \"unordered\",\n      \"startNumber\": 4\n    },\n    {\n      \"type\": \"table\",\n      \"rows\": [\n        [\n          {\n            \"text\": \"A\"\n          },\n          {\n            \"text\": \"B\",\n            \"alignment\": \"center\"\n          },\n          {\n            \"text\": \"C\",\n            \"alignment\": \"right\"\n          }\n        ],\n        [\n          {\n            \"text\": \"D\",\n            \"alignment\": \"right\"\n          },\n          {\n            \"text\": \"E\",\n            \"alignment\": \"center\"\n          },\n          {\n            \"text\": \"F\",\n            \"alignment\": \"left\"\n          }\n        ]\n      ],\n      \"headerColumn\": true,\n      \"headerRow\": true\n    },\n    {\n      \"type\": \"table\",\n      \"rows\": [\n        [\n          {\n            \"text\": \"A\"\n          },\n          {\n            \"text\": \"B\"\n          },\n          {\n            \"text\": \"C\"\n          }\n        ],\n        [\n          {\n            \"text\": \"D\"\n          },\n          {\n            \"text\": \"E\"\n          },\n          {\n            \"text\": \"F\"\n          }\n        ]\n      ]\n    },\n    {\n      \"type\": \"table\",\n      \"rows\": [\n        [\n          {\n            \"text\": \"A\"\n          },\n          {\n            \"text\": \"B\"\n          },\n          {\n            \"text\": \"C\"\n          }\n        ],\n        [\n          {\n            \"text\": \"D\"\n          },\n          {\n            \"text\": \"E\"\n          },\n          {\n            \"text\": \"F\"\n          }\n        ]\n      ],\n      \"headerRow\": false\n    },\n    {\n      \"type\": \"columns\",\n      \"columns\": [\n        {\n          \"blocks\": [\n            {\n              \"type\": \"paragraph\",\n              \"plaintext\": \"Marble Column 1 {{email}}\"\n            }\n          ]\n        },\n        {\n          \"blocks\": [\n            {\n              \"type\": \"image\",\n              \"imageUrl\": \"https://cdn.britannica.com/89/164789-050-D6B5E2C7/Barack-Obama-2012.jpg\",\n              \"alt_text\": \"A picture of Barry Obama\",\n              \"caption\": \"One Cool President\",\n              \"captionAlignment\": \"center\",\n              \"imageAlignment\": \"right\",\n              \"title\": \"Barry O\",\n              \"url\": \"https://www.whitehouse.gov/\",\n              \"width\": 75\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"type\": \"advertisement\",\n      \"opportunity_id\": \"d8dfa6be-24b5-4cad-8350-ae44366dbd4c\"\n    },\n    {\n      \"type\": \"image\",\n      \"imageUrl\": \"https://cdn.britannica.com/89/164789-050-D6B5E2C7/Barack-Obama-2012.jpg\",\n      \"alt_text\": \"A picture of Barry Obama\",\n      \"caption\": \"One Cool President\",\n      \"captionAlignment\": \"center\",\n      \"imageAlignment\": \"right\",\n      \"title\": \"Barry O\",\n      \"url\": \"https://www.whitehouse.gov/\",\n      \"width\": 75\n    },\n    {\n      \"type\": \"paragraph\",\n      \"formattedText\": [\n        {\n          \"text\": \"This is going to be \"\n        },\n        {\n          \"text\": \"a really, really awesome time \",\n          \"styling\": [\n            \"bold\"\n          ]\n        },\n        {\n          \"text\": \"Are you ready for this?\",\n          \"styling\": [\n            \"italic\",\n            \"bold\"\n          ]\n        }\n      ]\n    },\n    {\n      \"type\": \"button\",\n      \"href\": \"/subscribe\",\n      \"text\": \"Subscribe\",\n      \"alignment\": \"center\",\n      \"size\": \"large\",\n      \"target\": \"_blank\"\n    },\n    {\n      \"type\": \"button\",\n      \"href\": \"/signup\",\n      \"text\": \"Sign Up\",\n      \"alignment\": \"right\",\n      \"size\": \"small\",\n      \"target\": \"_blank\"\n    },\n    {\n      \"type\": \"button\",\n      \"href\": \"/\",\n      \"text\": \"View Posts\",\n      \"target\": \"_blank\"\n    },\n    {\n      \"type\": \"heading\",\n      \"level\": \"4\",\n      \"text\": \"This is my block!!!\",\n      \"anchorHeader\": true,\n      \"anchorIncludeInToc\": true,\n      \"textAlignment\": \"right\"\n    }\n  ],\n  \"subtitle\": \"Contains lots of examples of each block type and the various settings you could use\",\n  \"post_template_id\": \"post_template_00000000-0000-0000-0000-000000000000\",\n  \"scheduled_at\": \"2024-12-25T12:00:00Z\",\n  \"custom_link_tracking_enabled\": true,\n  \"email_capture_type_override\": \"none\",\n  \"override_scheduled_at\": \"2022-10-26T14:01:16Z\",\n  \"social_share\": \"comments_and_likes_only\",\n  \"thumbnail_image_url\": \"https://images.squarespace-cdn.com/content/v1/56e4ca0540261d39b90e4b18/1605047208324-PONGEYKEAKTMM1LANHJ5/1ED706BF-A70B-4F26-B3D5-266B449DDA8A_1_105_c.jpeg\",\n  \"recipients\": {\n    \"web\": {\n      \"tier_ids\": [\n        \"premium\"\n      ]\n    },\n    \"email\": {\n      \"tier_ids\": [\n        \"premium\",\n        \"free\"\n      ],\n      \"include_segment_ids\": [\n        \"seg_6426b403-39f5-42bd-86e9-9533fb0099e7\"\n      ],\n      \"exclude_segment_ids\": [\n        \"seg_e34b4085-aef6-449f-a699-7563f915f852\"\n      ]\n    }\n  },\n  \"email_settings\": {\n    \"from_address\": \"from_address\",\n    \"custom_live_url\": \"https://beehiiv.com\",\n    \"display_title_in_email\": true,\n    \"display_byline_in_email\": true,\n    \"display_subtitle_in_email\": true,\n    \"email_header_engagement_buttons\": \"email_header_engagement_buttons\",\n    \"email_header_social_share\": \"email_header_social_share\",\n    \"email_preview_text\": \"email_preview_text\",\n    \"email_subject_line\": \"email_subject_line\"\n  },\n  \"web_settings\": {\n    \"display_thumbnail_on_web\": true,\n    \"hide_from_feed\": true,\n    \"slug\": \"and-this-is-gonna-rock\"\n  },\n  \"seo_settings\": {\n    \"default_description\": \"default_description\",\n    \"default_title\": \"default_title\",\n    \"og_description\": \"OpenGraph description\",\n    \"og_title\": \"Opengraph Title\",\n    \"twitter_description\": \"Twitter Stuff\",\n    \"twitter_title\": \"My Twitter Article\"\n  },\n  \"content_tags\": [\n    \"Obama\",\n    \"Care\",\n    \"Rocks\",\n    \"Healthcare\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"title\": \"The Kitchen Sink Post (refactored version)\",\n  \"blocks\": [\n    {\n      \"type\": \"heading\",\n      \"level\": \"2\",\n      \"text\": \"This is my block!!!\",\n      \"anchorHeader\": false,\n      \"anchorIncludeInToc\": false,\n      \"textAlignment\": \"center\"\n    },\n    {\n      \"type\": \"list\",\n      \"items\": [\n        \"a\",\n        \"b\",\n        \"c\"\n      ],\n      \"listType\": \"ordered\"\n    },\n    {\n      \"type\": \"list\",\n      \"items\": [\n        \"d\",\n        \"e\",\n        \"f\"\n      ],\n      \"listType\": \"ordered\",\n      \"startNumber\": 4\n    },\n    {\n      \"type\": \"list\",\n      \"items\": [\n        \"g\",\n        \"h\",\n        \"i\"\n      ],\n      \"listType\": \"unordered\",\n      \"startNumber\": 4\n    },\n    {\n      \"type\": \"table\",\n      \"rows\": [\n        [\n          {\n            \"text\": \"A\"\n          },\n          {\n            \"text\": \"B\",\n            \"alignment\": \"center\"\n          },\n          {\n            \"text\": \"C\",\n            \"alignment\": \"right\"\n          }\n        ],\n        [\n          {\n            \"text\": \"D\",\n            \"alignment\": \"right\"\n          },\n          {\n            \"text\": \"E\",\n            \"alignment\": \"center\"\n          },\n          {\n            \"text\": \"F\",\n            \"alignment\": \"left\"\n          }\n        ]\n      ],\n      \"headerColumn\": true,\n      \"headerRow\": true\n    },\n    {\n      \"type\": \"table\",\n      \"rows\": [\n        [\n          {\n            \"text\": \"A\"\n          },\n          {\n            \"text\": \"B\"\n          },\n          {\n            \"text\": \"C\"\n          }\n        ],\n        [\n          {\n            \"text\": \"D\"\n          },\n          {\n            \"text\": \"E\"\n          },\n          {\n            \"text\": \"F\"\n          }\n        ]\n      ]\n    },\n    {\n      \"type\": \"table\",\n      \"rows\": [\n        [\n          {\n            \"text\": \"A\"\n          },\n          {\n            \"text\": \"B\"\n          },\n          {\n            \"text\": \"C\"\n          }\n        ],\n        [\n          {\n            \"text\": \"D\"\n          },\n          {\n            \"text\": \"E\"\n          },\n          {\n            \"text\": \"F\"\n          }\n        ]\n      ],\n      \"headerRow\": false\n    },\n    {\n      \"type\": \"columns\",\n      \"columns\": [\n        {\n          \"blocks\": [\n            {\n              \"type\": \"paragraph\",\n              \"plaintext\": \"Marble Column 1 {{email}}\"\n            }\n          ]\n        },\n        {\n          \"blocks\": [\n            {\n              \"type\": \"image\",\n              \"imageUrl\": \"https://cdn.britannica.com/89/164789-050-D6B5E2C7/Barack-Obama-2012.jpg\",\n              \"alt_text\": \"A picture of Barry Obama\",\n              \"caption\": \"One Cool President\",\n              \"captionAlignment\": \"center\",\n              \"imageAlignment\": \"right\",\n              \"title\": \"Barry O\",\n              \"url\": \"https://www.whitehouse.gov/\",\n              \"width\": 75\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"type\": \"advertisement\",\n      \"opportunity_id\": \"d8dfa6be-24b5-4cad-8350-ae44366dbd4c\"\n    },\n    {\n      \"type\": \"image\",\n      \"imageUrl\": \"https://cdn.britannica.com/89/164789-050-D6B5E2C7/Barack-Obama-2012.jpg\",\n      \"alt_text\": \"A picture of Barry Obama\",\n      \"caption\": \"One Cool President\",\n      \"captionAlignment\": \"center\",\n      \"imageAlignment\": \"right\",\n      \"title\": \"Barry O\",\n      \"url\": \"https://www.whitehouse.gov/\",\n      \"width\": 75\n    },\n    {\n      \"type\": \"paragraph\",\n      \"formattedText\": [\n        {\n          \"text\": \"This is going to be \"\n        },\n        {\n          \"text\": \"a really, really awesome time \",\n          \"styling\": [\n            \"bold\"\n          ]\n        },\n        {\n          \"text\": \"Are you ready for this?\",\n          \"styling\": [\n            \"italic\",\n            \"bold\"\n          ]\n        }\n      ]\n    },\n    {\n      \"type\": \"button\",\n      \"href\": \"/subscribe\",\n      \"text\": \"Subscribe\",\n      \"alignment\": \"center\",\n      \"size\": \"large\",\n      \"target\": \"_blank\"\n    },\n    {\n      \"type\": \"button\",\n      \"href\": \"/signup\",\n      \"text\": \"Sign Up\",\n      \"alignment\": \"right\",\n      \"size\": \"small\",\n      \"target\": \"_blank\"\n    },\n    {\n      \"type\": \"button\",\n      \"href\": \"/\",\n      \"text\": \"View Posts\",\n      \"target\": \"_blank\"\n    },\n    {\n      \"type\": \"heading\",\n      \"level\": \"4\",\n      \"text\": \"This is my block!!!\",\n      \"anchorHeader\": true,\n      \"anchorIncludeInToc\": true,\n      \"textAlignment\": \"right\"\n    }\n  ],\n  \"subtitle\": \"Contains lots of examples of each block type and the various settings you could use\",\n  \"post_template_id\": \"post_template_00000000-0000-0000-0000-000000000000\",\n  \"scheduled_at\": \"2024-12-25T12:00:00Z\",\n  \"custom_link_tracking_enabled\": true,\n  \"email_capture_type_override\": \"none\",\n  \"override_scheduled_at\": \"2022-10-26T14:01:16Z\",\n  \"social_share\": \"comments_and_likes_only\",\n  \"thumbnail_image_url\": \"https://images.squarespace-cdn.com/content/v1/56e4ca0540261d39b90e4b18/1605047208324-PONGEYKEAKTMM1LANHJ5/1ED706BF-A70B-4F26-B3D5-266B449DDA8A_1_105_c.jpeg\",\n  \"recipients\": {\n    \"web\": {\n      \"tier_ids\": [\n        \"premium\"\n      ]\n    },\n    \"email\": {\n      \"tier_ids\": [\n        \"premium\",\n        \"free\"\n      ],\n      \"include_segment_ids\": [\n        \"seg_6426b403-39f5-42bd-86e9-9533fb0099e7\"\n      ],\n      \"exclude_segment_ids\": [\n        \"seg_e34b4085-aef6-449f-a699-7563f915f852\"\n      ]\n    }\n  },\n  \"email_settings\": {\n    \"from_address\": \"from_address\",\n    \"custom_live_url\": \"https://beehiiv.com\",\n    \"display_title_in_email\": true,\n    \"display_byline_in_email\": true,\n    \"display_subtitle_in_email\": true,\n    \"email_header_engagement_buttons\": \"email_header_engagement_buttons\",\n    \"email_header_social_share\": \"email_header_social_share\",\n    \"email_preview_text\": \"email_preview_text\",\n    \"email_subject_line\": \"email_subject_line\"\n  },\n  \"web_settings\": {\n    \"display_thumbnail_on_web\": true,\n    \"hide_from_feed\": true,\n    \"slug\": \"and-this-is-gonna-rock\"\n  },\n  \"seo_settings\": {\n    \"default_description\": \"default_description\",\n    \"default_title\": \"default_title\",\n    \"og_description\": \"OpenGraph description\",\n    \"og_title\": \"Opengraph Title\",\n    \"twitter_description\": \"Twitter Stuff\",\n    \"twitter_title\": \"My Twitter Article\"\n  },\n  \"content_tags\": [\n    \"Obama\",\n    \"Care\",\n    \"Rocks\",\n    \"Healthcare\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts', [
  'body' => '{
  "title": "The Kitchen Sink Post (refactored version)",
  "blocks": [
    {
      "type": "heading",
      "level": "2",
      "text": "This is my block!!!",
      "anchorHeader": false,
      "anchorIncludeInToc": false,
      "textAlignment": "center"
    },
    {
      "type": "list",
      "items": [
        "a",
        "b",
        "c"
      ],
      "listType": "ordered"
    },
    {
      "type": "list",
      "items": [
        "d",
        "e",
        "f"
      ],
      "listType": "ordered",
      "startNumber": 4
    },
    {
      "type": "list",
      "items": [
        "g",
        "h",
        "i"
      ],
      "listType": "unordered",
      "startNumber": 4
    },
    {
      "type": "table",
      "rows": [
        [
          {
            "text": "A"
          },
          {
            "text": "B",
            "alignment": "center"
          },
          {
            "text": "C",
            "alignment": "right"
          }
        ],
        [
          {
            "text": "D",
            "alignment": "right"
          },
          {
            "text": "E",
            "alignment": "center"
          },
          {
            "text": "F",
            "alignment": "left"
          }
        ]
      ],
      "headerColumn": true,
      "headerRow": true
    },
    {
      "type": "table",
      "rows": [
        [
          {
            "text": "A"
          },
          {
            "text": "B"
          },
          {
            "text": "C"
          }
        ],
        [
          {
            "text": "D"
          },
          {
            "text": "E"
          },
          {
            "text": "F"
          }
        ]
      ]
    },
    {
      "type": "table",
      "rows": [
        [
          {
            "text": "A"
          },
          {
            "text": "B"
          },
          {
            "text": "C"
          }
        ],
        [
          {
            "text": "D"
          },
          {
            "text": "E"
          },
          {
            "text": "F"
          }
        ]
      ],
      "headerRow": false
    },
    {
      "type": "columns",
      "columns": [
        {
          "blocks": [
            {
              "type": "paragraph",
              "plaintext": "Marble Column 1 {{email}}"
            }
          ]
        },
        {
          "blocks": [
            {
              "type": "image",
              "imageUrl": "https://cdn.britannica.com/89/164789-050-D6B5E2C7/Barack-Obama-2012.jpg",
              "alt_text": "A picture of Barry Obama",
              "caption": "One Cool President",
              "captionAlignment": "center",
              "imageAlignment": "right",
              "title": "Barry O",
              "url": "https://www.whitehouse.gov/",
              "width": 75
            }
          ]
        }
      ]
    },
    {
      "type": "advertisement",
      "opportunity_id": "d8dfa6be-24b5-4cad-8350-ae44366dbd4c"
    },
    {
      "type": "image",
      "imageUrl": "https://cdn.britannica.com/89/164789-050-D6B5E2C7/Barack-Obama-2012.jpg",
      "alt_text": "A picture of Barry Obama",
      "caption": "One Cool President",
      "captionAlignment": "center",
      "imageAlignment": "right",
      "title": "Barry O",
      "url": "https://www.whitehouse.gov/",
      "width": 75
    },
    {
      "type": "paragraph",
      "formattedText": [
        {
          "text": "This is going to be "
        },
        {
          "text": "a really, really awesome time ",
          "styling": [
            "bold"
          ]
        },
        {
          "text": "Are you ready for this?",
          "styling": [
            "italic",
            "bold"
          ]
        }
      ]
    },
    {
      "type": "button",
      "href": "/subscribe",
      "text": "Subscribe",
      "alignment": "center",
      "size": "large",
      "target": "_blank"
    },
    {
      "type": "button",
      "href": "/signup",
      "text": "Sign Up",
      "alignment": "right",
      "size": "small",
      "target": "_blank"
    },
    {
      "type": "button",
      "href": "/",
      "text": "View Posts",
      "target": "_blank"
    },
    {
      "type": "heading",
      "level": "4",
      "text": "This is my block!!!",
      "anchorHeader": true,
      "anchorIncludeInToc": true,
      "textAlignment": "right"
    }
  ],
  "subtitle": "Contains lots of examples of each block type and the various settings you could use",
  "post_template_id": "post_template_00000000-0000-0000-0000-000000000000",
  "scheduled_at": "2024-12-25T12:00:00Z",
  "custom_link_tracking_enabled": true,
  "email_capture_type_override": "none",
  "override_scheduled_at": "2022-10-26T14:01:16Z",
  "social_share": "comments_and_likes_only",
  "thumbnail_image_url": "https://images.squarespace-cdn.com/content/v1/56e4ca0540261d39b90e4b18/1605047208324-PONGEYKEAKTMM1LANHJ5/1ED706BF-A70B-4F26-B3D5-266B449DDA8A_1_105_c.jpeg",
  "recipients": {
    "web": {
      "tier_ids": [
        "premium"
      ]
    },
    "email": {
      "tier_ids": [
        "premium",
        "free"
      ],
      "include_segment_ids": [
        "seg_6426b403-39f5-42bd-86e9-9533fb0099e7"
      ],
      "exclude_segment_ids": [
        "seg_e34b4085-aef6-449f-a699-7563f915f852"
      ]
    }
  },
  "email_settings": {
    "from_address": "from_address",
    "custom_live_url": "https://beehiiv.com",
    "display_title_in_email": true,
    "display_byline_in_email": true,
    "display_subtitle_in_email": true,
    "email_header_engagement_buttons": "email_header_engagement_buttons",
    "email_header_social_share": "email_header_social_share",
    "email_preview_text": "email_preview_text",
    "email_subject_line": "email_subject_line"
  },
  "web_settings": {
    "display_thumbnail_on_web": true,
    "hide_from_feed": true,
    "slug": "and-this-is-gonna-rock"
  },
  "seo_settings": {
    "default_description": "default_description",
    "default_title": "default_title",
    "og_description": "OpenGraph description",
    "og_title": "Opengraph Title",
    "twitter_description": "Twitter Stuff",
    "twitter_title": "My Twitter Article"
  },
  "content_tags": [
    "Obama",
    "Care",
    "Rocks",
    "Healthcare"
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"title\": \"The Kitchen Sink Post (refactored version)\",\n  \"blocks\": [\n    {\n      \"type\": \"heading\",\n      \"level\": \"2\",\n      \"text\": \"This is my block!!!\",\n      \"anchorHeader\": false,\n      \"anchorIncludeInToc\": false,\n      \"textAlignment\": \"center\"\n    },\n    {\n      \"type\": \"list\",\n      \"items\": [\n        \"a\",\n        \"b\",\n        \"c\"\n      ],\n      \"listType\": \"ordered\"\n    },\n    {\n      \"type\": \"list\",\n      \"items\": [\n        \"d\",\n        \"e\",\n        \"f\"\n      ],\n      \"listType\": \"ordered\",\n      \"startNumber\": 4\n    },\n    {\n      \"type\": \"list\",\n      \"items\": [\n        \"g\",\n        \"h\",\n        \"i\"\n      ],\n      \"listType\": \"unordered\",\n      \"startNumber\": 4\n    },\n    {\n      \"type\": \"table\",\n      \"rows\": [\n        [\n          {\n            \"text\": \"A\"\n          },\n          {\n            \"text\": \"B\",\n            \"alignment\": \"center\"\n          },\n          {\n            \"text\": \"C\",\n            \"alignment\": \"right\"\n          }\n        ],\n        [\n          {\n            \"text\": \"D\",\n            \"alignment\": \"right\"\n          },\n          {\n            \"text\": \"E\",\n            \"alignment\": \"center\"\n          },\n          {\n            \"text\": \"F\",\n            \"alignment\": \"left\"\n          }\n        ]\n      ],\n      \"headerColumn\": true,\n      \"headerRow\": true\n    },\n    {\n      \"type\": \"table\",\n      \"rows\": [\n        [\n          {\n            \"text\": \"A\"\n          },\n          {\n            \"text\": \"B\"\n          },\n          {\n            \"text\": \"C\"\n          }\n        ],\n        [\n          {\n            \"text\": \"D\"\n          },\n          {\n            \"text\": \"E\"\n          },\n          {\n            \"text\": \"F\"\n          }\n        ]\n      ]\n    },\n    {\n      \"type\": \"table\",\n      \"rows\": [\n        [\n          {\n            \"text\": \"A\"\n          },\n          {\n            \"text\": \"B\"\n          },\n          {\n            \"text\": \"C\"\n          }\n        ],\n        [\n          {\n            \"text\": \"D\"\n          },\n          {\n            \"text\": \"E\"\n          },\n          {\n            \"text\": \"F\"\n          }\n        ]\n      ],\n      \"headerRow\": false\n    },\n    {\n      \"type\": \"columns\",\n      \"columns\": [\n        {\n          \"blocks\": [\n            {\n              \"type\": \"paragraph\",\n              \"plaintext\": \"Marble Column 1 {{email}}\"\n            }\n          ]\n        },\n        {\n          \"blocks\": [\n            {\n              \"type\": \"image\",\n              \"imageUrl\": \"https://cdn.britannica.com/89/164789-050-D6B5E2C7/Barack-Obama-2012.jpg\",\n              \"alt_text\": \"A picture of Barry Obama\",\n              \"caption\": \"One Cool President\",\n              \"captionAlignment\": \"center\",\n              \"imageAlignment\": \"right\",\n              \"title\": \"Barry O\",\n              \"url\": \"https://www.whitehouse.gov/\",\n              \"width\": 75\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"type\": \"advertisement\",\n      \"opportunity_id\": \"d8dfa6be-24b5-4cad-8350-ae44366dbd4c\"\n    },\n    {\n      \"type\": \"image\",\n      \"imageUrl\": \"https://cdn.britannica.com/89/164789-050-D6B5E2C7/Barack-Obama-2012.jpg\",\n      \"alt_text\": \"A picture of Barry Obama\",\n      \"caption\": \"One Cool President\",\n      \"captionAlignment\": \"center\",\n      \"imageAlignment\": \"right\",\n      \"title\": \"Barry O\",\n      \"url\": \"https://www.whitehouse.gov/\",\n      \"width\": 75\n    },\n    {\n      \"type\": \"paragraph\",\n      \"formattedText\": [\n        {\n          \"text\": \"This is going to be \"\n        },\n        {\n          \"text\": \"a really, really awesome time \",\n          \"styling\": [\n            \"bold\"\n          ]\n        },\n        {\n          \"text\": \"Are you ready for this?\",\n          \"styling\": [\n            \"italic\",\n            \"bold\"\n          ]\n        }\n      ]\n    },\n    {\n      \"type\": \"button\",\n      \"href\": \"/subscribe\",\n      \"text\": \"Subscribe\",\n      \"alignment\": \"center\",\n      \"size\": \"large\",\n      \"target\": \"_blank\"\n    },\n    {\n      \"type\": \"button\",\n      \"href\": \"/signup\",\n      \"text\": \"Sign Up\",\n      \"alignment\": \"right\",\n      \"size\": \"small\",\n      \"target\": \"_blank\"\n    },\n    {\n      \"type\": \"button\",\n      \"href\": \"/\",\n      \"text\": \"View Posts\",\n      \"target\": \"_blank\"\n    },\n    {\n      \"type\": \"heading\",\n      \"level\": \"4\",\n      \"text\": \"This is my block!!!\",\n      \"anchorHeader\": true,\n      \"anchorIncludeInToc\": true,\n      \"textAlignment\": \"right\"\n    }\n  ],\n  \"subtitle\": \"Contains lots of examples of each block type and the various settings you could use\",\n  \"post_template_id\": \"post_template_00000000-0000-0000-0000-000000000000\",\n  \"scheduled_at\": \"2024-12-25T12:00:00Z\",\n  \"custom_link_tracking_enabled\": true,\n  \"email_capture_type_override\": \"none\",\n  \"override_scheduled_at\": \"2022-10-26T14:01:16Z\",\n  \"social_share\": \"comments_and_likes_only\",\n  \"thumbnail_image_url\": \"https://images.squarespace-cdn.com/content/v1/56e4ca0540261d39b90e4b18/1605047208324-PONGEYKEAKTMM1LANHJ5/1ED706BF-A70B-4F26-B3D5-266B449DDA8A_1_105_c.jpeg\",\n  \"recipients\": {\n    \"web\": {\n      \"tier_ids\": [\n        \"premium\"\n      ]\n    },\n    \"email\": {\n      \"tier_ids\": [\n        \"premium\",\n        \"free\"\n      ],\n      \"include_segment_ids\": [\n        \"seg_6426b403-39f5-42bd-86e9-9533fb0099e7\"\n      ],\n      \"exclude_segment_ids\": [\n        \"seg_e34b4085-aef6-449f-a699-7563f915f852\"\n      ]\n    }\n  },\n  \"email_settings\": {\n    \"from_address\": \"from_address\",\n    \"custom_live_url\": \"https://beehiiv.com\",\n    \"display_title_in_email\": true,\n    \"display_byline_in_email\": true,\n    \"display_subtitle_in_email\": true,\n    \"email_header_engagement_buttons\": \"email_header_engagement_buttons\",\n    \"email_header_social_share\": \"email_header_social_share\",\n    \"email_preview_text\": \"email_preview_text\",\n    \"email_subject_line\": \"email_subject_line\"\n  },\n  \"web_settings\": {\n    \"display_thumbnail_on_web\": true,\n    \"hide_from_feed\": true,\n    \"slug\": \"and-this-is-gonna-rock\"\n  },\n  \"seo_settings\": {\n    \"default_description\": \"default_description\",\n    \"default_title\": \"default_title\",\n    \"og_description\": \"OpenGraph description\",\n    \"og_title\": \"Opengraph Title\",\n    \"twitter_description\": \"Twitter Stuff\",\n    \"twitter_title\": \"My Twitter Article\"\n  },\n  \"content_tags\": [\n    \"Obama\",\n    \"Care\",\n    \"Rocks\",\n    \"Healthcare\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "title": "The Kitchen Sink Post (refactored version)",
  "blocks": [
    [
      "type": "heading",
      "level": "2",
      "text": "This is my block!!!",
      "anchorHeader": false,
      "anchorIncludeInToc": false,
      "textAlignment": "center"
    ],
    [
      "type": "list",
      "items": ["a", "b", "c"],
      "listType": "ordered"
    ],
    [
      "type": "list",
      "items": ["d", "e", "f"],
      "listType": "ordered",
      "startNumber": 4
    ],
    [
      "type": "list",
      "items": ["g", "h", "i"],
      "listType": "unordered",
      "startNumber": 4
    ],
    [
      "type": "table",
      "rows": [[
          ["text": "A"],
          [
            "text": "B",
            "alignment": "center"
          ],
          [
            "text": "C",
            "alignment": "right"
          ]
        ], [
          [
            "text": "D",
            "alignment": "right"
          ],
          [
            "text": "E",
            "alignment": "center"
          ],
          [
            "text": "F",
            "alignment": "left"
          ]
        ]],
      "headerColumn": true,
      "headerRow": true
    ],
    [
      "type": "table",
      "rows": [[["text": "A"], ["text": "B"], ["text": "C"]], [["text": "D"], ["text": "E"], ["text": "F"]]]
    ],
    [
      "type": "table",
      "rows": [[["text": "A"], ["text": "B"], ["text": "C"]], [["text": "D"], ["text": "E"], ["text": "F"]]],
      "headerRow": false
    ],
    [
      "type": "columns",
      "columns": [["blocks": [
            [
              "type": "paragraph",
              "plaintext": "Marble Column 1 {{email}}"
            ]
          ]], ["blocks": [
            [
              "type": "image",
              "imageUrl": "https://cdn.britannica.com/89/164789-050-D6B5E2C7/Barack-Obama-2012.jpg",
              "alt_text": "A picture of Barry Obama",
              "caption": "One Cool President",
              "captionAlignment": "center",
              "imageAlignment": "right",
              "title": "Barry O",
              "url": "https://www.whitehouse.gov/",
              "width": 75
            ]
          ]]]
    ],
    [
      "type": "advertisement",
      "opportunity_id": "d8dfa6be-24b5-4cad-8350-ae44366dbd4c"
    ],
    [
      "type": "image",
      "imageUrl": "https://cdn.britannica.com/89/164789-050-D6B5E2C7/Barack-Obama-2012.jpg",
      "alt_text": "A picture of Barry Obama",
      "caption": "One Cool President",
      "captionAlignment": "center",
      "imageAlignment": "right",
      "title": "Barry O",
      "url": "https://www.whitehouse.gov/",
      "width": 75
    ],
    [
      "type": "paragraph",
      "formattedText": [
        ["text": "This is going to be "],
        [
          "text": "a really, really awesome time ",
          "styling": ["bold"]
        ],
        [
          "text": "Are you ready for this?",
          "styling": ["italic", "bold"]
        ]
      ]
    ],
    [
      "type": "button",
      "href": "/subscribe",
      "text": "Subscribe",
      "alignment": "center",
      "size": "large",
      "target": "_blank"
    ],
    [
      "type": "button",
      "href": "/signup",
      "text": "Sign Up",
      "alignment": "right",
      "size": "small",
      "target": "_blank"
    ],
    [
      "type": "button",
      "href": "/",
      "text": "View Posts",
      "target": "_blank"
    ],
    [
      "type": "heading",
      "level": "4",
      "text": "This is my block!!!",
      "anchorHeader": true,
      "anchorIncludeInToc": true,
      "textAlignment": "right"
    ]
  ],
  "subtitle": "Contains lots of examples of each block type and the various settings you could use",
  "post_template_id": "post_template_00000000-0000-0000-0000-000000000000",
  "scheduled_at": "2024-12-25T12:00:00Z",
  "custom_link_tracking_enabled": true,
  "email_capture_type_override": "none",
  "override_scheduled_at": "2022-10-26T14:01:16Z",
  "social_share": "comments_and_likes_only",
  "thumbnail_image_url": "https://images.squarespace-cdn.com/content/v1/56e4ca0540261d39b90e4b18/1605047208324-PONGEYKEAKTMM1LANHJ5/1ED706BF-A70B-4F26-B3D5-266B449DDA8A_1_105_c.jpeg",
  "recipients": [
    "web": ["tier_ids": ["premium"]],
    "email": [
      "tier_ids": ["premium", "free"],
      "include_segment_ids": ["seg_6426b403-39f5-42bd-86e9-9533fb0099e7"],
      "exclude_segment_ids": ["seg_e34b4085-aef6-449f-a699-7563f915f852"]
    ]
  ],
  "email_settings": [
    "from_address": "from_address",
    "custom_live_url": "https://beehiiv.com",
    "display_title_in_email": true,
    "display_byline_in_email": true,
    "display_subtitle_in_email": true,
    "email_header_engagement_buttons": "email_header_engagement_buttons",
    "email_header_social_share": "email_header_social_share",
    "email_preview_text": "email_preview_text",
    "email_subject_line": "email_subject_line"
  ],
  "web_settings": [
    "display_thumbnail_on_web": true,
    "hide_from_feed": true,
    "slug": "and-this-is-gonna-rock"
  ],
  "seo_settings": [
    "default_description": "default_description",
    "default_title": "default_title",
    "og_description": "OpenGraph description",
    "og_title": "Opengraph Title",
    "twitter_description": "Twitter Stuff",
    "twitter_title": "My Twitter Article"
  ],
  "content_tags": ["Obama", "Care", "Rocks", "Healthcare"]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# List posts <Badge intent="info" minimal outlined>OAuth Scope: posts:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/posts

Retrieve all posts belonging to a specific publication

Reference: https://developers.beehiiv.com/api-reference/posts/index

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/posts:
    get:
      operationId: index
      summary: >-
        List posts <Badge intent="info" minimal outlined>OAuth Scope:
        posts:read</Badge>
      description: Retrieve all posts belonging to a specific publication
      tags:
        - subpackage_posts
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: expand
          in: query
          description: >-
            Optionally expand the results by adding additional information.
            <br>`stats` - Adds statistics about the post(s).
            <br>`free_web_content` - Adds the web HTML rendered to a free
            reader. <br>`free_email_content` - Adds the email HTML rendered to a
            free reader. <br>`free_rss_content` - Adds the RSS feed HTML.
            <br>`premium_web_content` - Adds the web HTML rendered to a premium
            reader. <br>`premium_email_content` - Adds the email HTML rendered
            to a premium reader.
          required: false
          schema:
            type: array
            items:
              $ref: '#/components/schemas/type_posts:PostExpandField'
        - name: audience
          in: query
          description: Optionally filter the results by audience
          required: false
          schema:
            $ref: '#/components/schemas/type_posts:PostAudienceFilter'
        - name: platform
          in: query
          description: >-
            Optionally filter the results by platform.<br>`web` - Posts only
            published to web.<br>`email` - Posts only published to
            email.<br>`both` - Posts published to email and web.<br>`all` - Does
            not restrict results by platform.
          required: false
          schema:
            $ref: '#/components/schemas/type_posts:PostPlatformFilter'
        - name: status
          in: query
          description: >-
            Optionally filter the results by the status of the post.<br>`draft`
            - not been scheduled.<br>`confirmed` - The post will be active after
            the `scheduled_at`.<br>`archived` - The post is no longer
            active.<br>`all` - Does not restrict results by status.
          required: false
          schema:
            $ref: '#/components/schemas/type_posts:PostStatusFilter'
        - name: content_tags[]
          in: query
          description: >-
            Optionally filter posts by content_tags. Adding a content tag will
            return any post with that content tag associated to
            it.<br><br><b>Example</b>: Filtering for `content_tags:
            ["sales","closing"]` will return results of posts that have *either*
            `sales` or `closing` content_tags.
          required: false
          schema:
            type: array
            items:
              type: string
        - name: slugs[]
          in: query
          description: >-
            Optionally filter posts by their slugs. Adding a slug will return
            any post with that exact slug associated to
            it.<br><br><b>Example:</b> Filtering for `slugs:
            ["my-first-post","another-post"]` will return results of posts that
            have *either* `my-first-post` or `another-post` as their slug.
          required: false
          schema:
            type: array
            items:
              type: string
        - name: authors[]
          in: query
          description: >-
            Optionally filter posts by their authors. Adding an author name will
            return any post with that author associated to it
            (case-insensitive).<br><br><b>Example:</b> Filtering for `authors:
            ["John Doe","Jane Smith"]` will return results of posts that have
            *either* John Doe or Jane Smith as authors.
          required: false
          schema:
            type: array
            items:
              type: string
        - name: premium_tiers
          in: query
          description: >-
            Optionally filter posts by audience based on premium tiers.<br> This
            takes in an array of Display Names of the premium tiers.<br> It will
            also scope any expanded content output to the specified premium
            tiers.<br> Note: This is case insensitive.
          required: false
          schema:
            type: array
            items:
              type: string
        - name: limit
          in: query
          description: >-
            A limit on the number of objects to be returned. The limit can range
            between 1 and 100, and the default is 10.
          required: false
          schema:
            type: integer
        - name: page
          in: query
          description: >-
            Pagination returns the results in pages. Each page contains the
            number of results specified by the `limit` (default: 10).<br>If not
            specified, results 1-10 from page 1 will be returned.
          required: false
          schema:
            type: integer
        - name: order_by
          in: query
          description: >-
            The field that the results are sorted by. Defaults to created<br>
            `created` - The time in which the post was first created.<br>
            `publish_date` - The time the post was set to be published.<br>
            `displayed_date` - The time displayed in place of the
            `publish_date`. If no `displayed_date` was set, it will default to
            the `publish_date`
          required: false
          schema:
            $ref: '#/components/schemas/type_posts:PostOrderBy'
        - name: direction
          in: query
          description: >-
            The direction that the results are sorted in. Defaults to asc<br>
            `asc` - Ascending, sorts from smallest to largest.<br> `desc` -
            Descending, sorts from largest to smallest.
          required: false
          schema:
            $ref: '#/components/schemas/type_:RequestDirection'
        - name: hidden_from_feed
          in: query
          description: >-
            Optionally filter the results by the `hidden_from_feed` attribute of
            the post.<br>`all` - Does not restrict results by
            `hidden_from_feed`.<br>`true` - Only return posts hidden from the
            feed.<br>`false` - Only return posts that are visible on the feed.
          required: false
          schema:
            $ref: '#/components/schemas/type_posts:PostsListRequestHiddenFromFeed'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_posts:PostsListResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_posts:PostExpandField:
      type: string
      enum:
        - stats
        - free_web_content
        - free_email_content
        - free_rss_content
        - premium_web_content
        - premium_email_content
      title: PostExpandField
    type_posts:PostAudienceFilter:
      type: string
      enum:
        - free
        - premium
        - all
      default: all
      title: PostAudienceFilter
    type_posts:PostPlatformFilter:
      type: string
      enum:
        - web
        - email
        - both
        - all
      default: all
      title: PostPlatformFilter
    type_posts:PostStatusFilter:
      type: string
      enum:
        - draft
        - confirmed
        - archived
        - all
      default: all
      title: PostStatusFilter
    type_posts:PostOrderBy:
      type: string
      enum:
        - created
        - publish_date
        - displayed_date
      default: created
      title: PostOrderBy
    type_:RequestDirection:
      type: string
      enum:
        - asc
        - desc
      default: asc
      description: The direction of the request. Defaults to `asc`.
      title: RequestDirection
    type_posts:PostsListRequestHiddenFromFeed:
      type: string
      enum:
        - all
        - 'true'
        - 'false'
      default: all
      title: PostsListRequestHiddenFromFeed
    type_ids:PostId:
      type: string
      description: The prefixed ID of the post.
      title: PostId
    type_:PostStatus:
      type: string
      enum:
        - draft
        - confirmed
        - archived
      default: draft
      description: >-
        The status of the post.<br>`draft` - not been scheduled.<br>`confirmed`
        - The post will be active after the `scheduled_at`.<br>`archived` - The
        post is no longer active.
      title: PostStatus
    type_:PostAudience:
      type: string
      enum:
        - free
        - premium
        - both
      description: >-
        The audience that the post is available to on the web. Only applicable
        if the platform is `web` or `both`.
      title: PostAudience
    type_:PostPlatform:
      type: string
      enum:
        - web
        - email
        - both
      description: The platform that the post is or will be published to.
      title: PostPlatform
    type_:FreePostContent:
      type: object
      properties:
        web:
          type: string
          description: The web HTML rendered to a free or annonomous reader.
        email:
          type: string
          description: The email HTML rendered to a free reader.
        rss:
          type: string
          description: The HTML that is rendered in RSS feeds.
      description: The requested free post HTML. This HTML has paywalls enforced.
      title: FreePostContent
    type_:PremiumPostContent:
      type: object
      properties:
        web:
          type: string
          description: The website HTML rendered to a free reader
        email:
          type: string
          description: The email HTML rendered to a premium reader
      description: >-
        The requested premium post HTML. This HTML does not have paywalls
        enforced.
      title: PremiumPostContent
    type_:PostContent:
      type: object
      properties:
        free:
          $ref: '#/components/schemas/type_:FreePostContent'
          description: The requested free post HTML. This HTML has paywalls enforced.
        premium:
          $ref: '#/components/schemas/type_:PremiumPostContent'
          description: >-
            The requested premium post HTML. This HTML does not have paywalls
            enforced.
      description: >-
        Optional html content for a post. Retrievable by including any of
        `expand: [free_web_content, free_email_content, free_rss_content,
        premium_web_content, premium_email_content]` in the post request body.


        **Note:** Generating HTML is slow. We recommend only requesting the HTML
        versions you need at the time.
      title: PostContent
    type_:PostStatsEmail:
      type: object
      properties:
        recipients:
          type: integer
          default: 0
          description: Total number of email recipients
        delivered:
          type: integer
          default: 0
          description: Total number of emails delivered
        opens:
          type: integer
          default: 0
          description: Total number of email opens
        unique_opens:
          type: integer
          default: 0
          description: Total number of unique email opens
        open_rate:
          type: number
          format: double
          description: The percentage of emails that have been opened
        clicks:
          type: integer
          default: 0
          description: Total number of email clicks
        unique_clicks:
          type: integer
          default: 0
          description: Unique number of email clicks
        verified_clicks:
          type: integer
          default: 0
          description: >-
            Total number of verified human email clicks across all URLs in this
            post. Verified clicks have passed bot detection and are confirmed to
            be from real subscribers.
        unique_verified_clicks:
          type: integer
          default: 0
          description: >-
            Unique number of verified human email clicks across all URLs in this
            post. Only counts the first verified click per subscriber.
        click_rate:
          type: number
          format: double
          description: The percentage of emails that have been clicked
        unsubscribes:
          type: integer
          default: 0
          description: Total number of email unsubscribes
        spam_reports:
          type: integer
          default: 0
          description: The number of subscribers that reported this post email as spam
      description: >-
        Stats scoped only to email recipients. Not relevant for posts published
        only to web
      title: PostStatsEmail
    type_:PostStatsWeb:
      type: object
      properties:
        views:
          type: integer
          default: 0
          description: Total number of web views
        clicks:
          type: integer
          default: 0
          description: Total number of web clicks
      description: >-
        Stats scoped only to web views. Not relevant for posts published only to
        email
      title: PostStatsWeb
    type_:PostClickStatsEmail:
      type: object
      properties:
        clicks:
          type: integer
        unique_clicks:
          type: integer
        verified_clicks:
          type: integer
          description: >-
            Total number of verified human email clicks on this URL. Verified
            clicks have passed bot detection and are confirmed to be from real
            subscribers.
        unique_verified_clicks:
          type: integer
          description: >-
            Unique number of verified human email clicks on this URL. Only
            counts the first verified click per subscriber.
        click_through_rate:
          type: number
          format: double
          description: >-
            The percentage of email clicks on the URL compared to the total
            number of recipients
      description: >-
        URL stats scoped only to email recipients. Not relevant for posts
        published only to web
      title: PostClickStatsEmail
    type_:PostClickStatsWeb:
      type: object
      properties:
        clicks:
          type: integer
        unique_clicks:
          type: integer
        click_through_rate:
          type: number
          format: double
          description: >-
            The percentage of clicks on the URL compared to the total number of
            web views
      description: >-
        Stats scoped only to web views. Not relevant for posts published only to
        email
      title: PostClickStatsWeb
    type_:ClickStats:
      type: object
      properties:
        url:
          type: string
          description: The URL the stats are for
        base_url:
          type: string
          description: >-
            The canonical URL with all query parameters and fragments removed.
            Derived by stripping everything after the '?' and '#' characters.
            Preserves the protocol, host (including casing), port, and path
            exactly as they appear in the original URL. Guaranteed to be present
            whenever url is present, enabling grouping of clicks by destination
            regardless of tracking parameters.
        email:
          $ref: '#/components/schemas/type_:PostClickStatsEmail'
          description: >-
            URL stats scoped only to email recipients. Not relevant for posts
            published only to web
        web:
          $ref: '#/components/schemas/type_:PostClickStatsWeb'
          description: >-
            Stats scoped only to web views. Not relevant for posts published
            only to email
        total_clicks:
          type: integer
        total_unique_clicks:
          type: integer
        total_click_through_rate:
          type: number
          format: double
          description: >-
            The percentage of clicks on the URL compared to the total number of
            recipients and web views
      description: Details about specific URL's click stats from a post.
      title: ClickStats
    type_:PostStats:
      type: object
      properties:
        email:
          $ref: '#/components/schemas/type_:PostStatsEmail'
          description: >-
            Stats scoped only to email recipients. Not relevant for posts
            published only to web
        web:
          $ref: '#/components/schemas/type_:PostStatsWeb'
          description: >-
            Stats scoped only to web views. Not relevant for posts published
            only to email
        clicks:
          type: array
          items:
            $ref: '#/components/schemas/type_:ClickStats'
          description: An array of click statistics for each URL in the post
      description: >-
        Optional list of stats for a post. Retrievable by including `expand:
        [stats]` in the post request body. <br><br> **Note:** If a timeout
        occurs while aggregating stats, subsequent requests may return
        consolidated click metrics rather than individual raw click metrics.
      title: PostStats
    type_:Post:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:PostId'
          description: The prefixed post id
        subtitle:
          type: string
          description: The subtitle displayed in web views
        title:
          type: string
          description: The title displayed in web views
        authors:
          type: array
          items:
            type: string
          description: An array of author names
        created:
          type: integer
          description: >-
            The time the post was created. Measured in seconds since the Unix
            epoch
        status:
          $ref: '#/components/schemas/type_:PostStatus'
          description: >-
            The status of the post.<br>`draft` - not been
            scheduled.<br>`confirmed` - The post will be active after the
            `scheduled_at`.<br>`archived` - The post is no longer active.
        publish_date:
          type: integer
          description: >-
            The time the post was set to be published. Measured in seconds since
            the Unix epoch
        displayed_date:
          type: integer
          description: >-
            The time displayed in place of the `publish_date`. Measured in
            seconds since the Unix epoch
        split_tested:
          type: boolean
          description: >-
            A flag to indicate if a split test was done. Only applicable to
            email posts.
        subject_line:
          type: string
          description: >-
            The email subject line. In cases of A/B Testing, this will be
            adjusted to the winning subject line.
        preview_text:
          type: string
          description: The email preview text
        slug:
          type: string
          description: The web slug where this post can be accessed.
        thumbnail_url:
          type: string
          description: >-
            The URL of the thumbnail. Defaults to the Publication logo if not
            set.
        web_url:
          type: string
          description: >-
            The full URL where this post can be accessed on the web. Only
            applicable if the platform is `web` or `both`.
        audience:
          $ref: '#/components/schemas/type_:PostAudience'
          description: >-
            The audience that the post is available to on the web. Only
            applicable if the platform is `web` or `both`.
        platform:
          $ref: '#/components/schemas/type_:PostPlatform'
          description: The platform that the post is or will be published to.
        content_tags:
          type: array
          items:
            type: string
          description: All content tags that were associated with the post.
        meta_default_description:
          type: string
          description: >-
            Meta tag description for the post, called SEO Description in the
            admin UI
        meta_default_title:
          type: string
          description: meta tag title for the post, called SEO Title in the admin UI
        content:
          $ref: '#/components/schemas/type_:PostContent'
        stats:
          $ref: '#/components/schemas/type_:PostStats'
        hidden_from_feed:
          type: boolean
          default: false
          description: A flag to indicate if the post is hidden from the website feed.
        enforce_gated_content:
          type: boolean
          default: false
          description: >-
            A flag to indicate if the post enforces gated content for
            non-subscribers.
        email_capture_popup:
          type: boolean
          default: false
          description: A flag to indicate if popup email capture is enabled for this post.
      required:
        - id
        - subtitle
        - title
        - authors
        - created
        - status
        - split_tested
        - subject_line
        - preview_text
        - slug
        - thumbnail_url
        - web_url
        - audience
        - platform
        - content_tags
        - hidden_from_feed
        - enforce_gated_content
        - email_capture_popup
      title: Post
    type_posts:PostsListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/type_:Post'
        limit:
          type: integer
          description: >-
            The limit placed on the results. If no limit was specified in the
            request,this defaults to 10.
        page:
          type: integer
          default: 1
          description: >-
            The page number the results are from. If no page was specified in
            the request, this defaults to page 1.
        total_results:
          type: integer
          description: The total number of results from all pages.
        total_pages:
          type: integer
          description: The total number of pages.
      required:
        - data
        - limit
        - page
        - total_results
        - total_pages
      title: PostsListResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.posts.list("pub_00000000-0000-0000-0000-000000000000");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get aggregate stats <Badge intent="info" minimal outlined>OAuth Scope: posts:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/posts/aggregate_stats

Retrieve aggregate stats for all posts

Reference: https://developers.beehiiv.com/api-reference/posts/aggregate-stats

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/posts/aggregate_stats:
    get:
      operationId: aggregate-stats
      summary: >-
        Get aggregate stats <Badge intent="info" minimal outlined>OAuth Scope:
        posts:read</Badge>
      description: Retrieve aggregate stats for all posts
      tags:
        - subpackage_posts
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: audience
          in: query
          description: Optionally filter the results by audience
          required: false
          schema:
            $ref: '#/components/schemas/type_posts:PostAudienceFilter'
        - name: platform
          in: query
          description: >-
            Optionally filter the results by platform.<br>`web` - Posts only
            published to web.<br>`email` - Posts only published to
            email.<br>`both` - Posts published to email and web.<br>`all` - Does
            not restrict results by platform.
          required: false
          schema:
            $ref: '#/components/schemas/type_posts:PostPlatformFilter'
        - name: status
          in: query
          description: >-
            Optionally filter the results by the status of the post.<br>`draft`
            - not been scheduled.<br>`confirmed` - The post will be active after
            the `scheduled_at`.<br>`archived` - The post is no longer
            active.<br>`all` - Does not restrict results by status.
          required: false
          schema:
            $ref: '#/components/schemas/type_posts:PostStatusFilter'
        - name: content_tags[]
          in: query
          description: >-
            Optionally filter posts by content_tags. Adding a content tag will
            return any post with that content tag associated to it.<br>Example:
            Filtering for `content_tags: ["sales","closing"]` will return
            results of posts that have *either* sales or closing content_tags.
          required: false
          schema:
            type: array
            items:
              type: string
        - name: authors[]
          in: query
          description: >-
            Optionally filter posts by their authors. Adding an author name will
            return any post with that author associated to it
            (case-insensitive).<br><br><b>Example:</b> Filtering for `authors:
            ["John Doe","Jane Smith"]` will return results of posts that have
            *either* John Doe or Jane Smith as authors.
          required: false
          schema:
            type: array
            items:
              type: string
        - name: hidden_from_feed
          in: query
          description: >-
            Optionally filter the results by the `hidden_from_feed` attribute of
            the post.<br>`all` - Does not restrict results by
            `hidden_from_feed`.<br>`true` - Only return posts hidden from the
            feed.<br>`false` - Only return posts that are visible on the feed.
          required: false
          schema:
            $ref: '#/components/schemas/type_posts:PostsListRequestHiddenFromFeed'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_posts:PostsAggregateStatsResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_posts:PostAudienceFilter:
      type: string
      enum:
        - free
        - premium
        - all
      default: all
      title: PostAudienceFilter
    type_posts:PostPlatformFilter:
      type: string
      enum:
        - web
        - email
        - both
        - all
      default: all
      title: PostPlatformFilter
    type_posts:PostStatusFilter:
      type: string
      enum:
        - draft
        - confirmed
        - archived
        - all
      default: all
      title: PostStatusFilter
    type_posts:PostsListRequestHiddenFromFeed:
      type: string
      enum:
        - all
        - 'true'
        - 'false'
      default: all
      title: PostsListRequestHiddenFromFeed
    type_:PostStatsEmail:
      type: object
      properties:
        recipients:
          type: integer
          default: 0
          description: Total number of email recipients
        delivered:
          type: integer
          default: 0
          description: Total number of emails delivered
        opens:
          type: integer
          default: 0
          description: Total number of email opens
        unique_opens:
          type: integer
          default: 0
          description: Total number of unique email opens
        open_rate:
          type: number
          format: double
          description: The percentage of emails that have been opened
        clicks:
          type: integer
          default: 0
          description: Total number of email clicks
        unique_clicks:
          type: integer
          default: 0
          description: Unique number of email clicks
        verified_clicks:
          type: integer
          default: 0
          description: >-
            Total number of verified human email clicks across all URLs in this
            post. Verified clicks have passed bot detection and are confirmed to
            be from real subscribers.
        unique_verified_clicks:
          type: integer
          default: 0
          description: >-
            Unique number of verified human email clicks across all URLs in this
            post. Only counts the first verified click per subscriber.
        click_rate:
          type: number
          format: double
          description: The percentage of emails that have been clicked
        unsubscribes:
          type: integer
          default: 0
          description: Total number of email unsubscribes
        spam_reports:
          type: integer
          default: 0
          description: The number of subscribers that reported this post email as spam
      description: >-
        Stats scoped only to email recipients. Not relevant for posts published
        only to web
      title: PostStatsEmail
    type_:PostStatsWeb:
      type: object
      properties:
        views:
          type: integer
          default: 0
          description: Total number of web views
        clicks:
          type: integer
          default: 0
          description: Total number of web clicks
      description: >-
        Stats scoped only to web views. Not relevant for posts published only to
        email
      title: PostStatsWeb
    type_:PostClickStatsEmail:
      type: object
      properties:
        clicks:
          type: integer
        unique_clicks:
          type: integer
        verified_clicks:
          type: integer
          description: >-
            Total number of verified human email clicks on this URL. Verified
            clicks have passed bot detection and are confirmed to be from real
            subscribers.
        unique_verified_clicks:
          type: integer
          description: >-
            Unique number of verified human email clicks on this URL. Only
            counts the first verified click per subscriber.
        click_through_rate:
          type: number
          format: double
          description: >-
            The percentage of email clicks on the URL compared to the total
            number of recipients
      description: >-
        URL stats scoped only to email recipients. Not relevant for posts
        published only to web
      title: PostClickStatsEmail
    type_:PostClickStatsWeb:
      type: object
      properties:
        clicks:
          type: integer
        unique_clicks:
          type: integer
        click_through_rate:
          type: number
          format: double
          description: >-
            The percentage of clicks on the URL compared to the total number of
            web views
      description: >-
        Stats scoped only to web views. Not relevant for posts published only to
        email
      title: PostClickStatsWeb
    type_:ClickStats:
      type: object
      properties:
        url:
          type: string
          description: The URL the stats are for
        base_url:
          type: string
          description: >-
            The canonical URL with all query parameters and fragments removed.
            Derived by stripping everything after the '?' and '#' characters.
            Preserves the protocol, host (including casing), port, and path
            exactly as they appear in the original URL. Guaranteed to be present
            whenever url is present, enabling grouping of clicks by destination
            regardless of tracking parameters.
        email:
          $ref: '#/components/schemas/type_:PostClickStatsEmail'
          description: >-
            URL stats scoped only to email recipients. Not relevant for posts
            published only to web
        web:
          $ref: '#/components/schemas/type_:PostClickStatsWeb'
          description: >-
            Stats scoped only to web views. Not relevant for posts published
            only to email
        total_clicks:
          type: integer
        total_unique_clicks:
          type: integer
        total_click_through_rate:
          type: number
          format: double
          description: >-
            The percentage of clicks on the URL compared to the total number of
            recipients and web views
      description: Details about specific URL's click stats from a post.
      title: ClickStats
    type_:PostStats:
      type: object
      properties:
        email:
          $ref: '#/components/schemas/type_:PostStatsEmail'
          description: >-
            Stats scoped only to email recipients. Not relevant for posts
            published only to web
        web:
          $ref: '#/components/schemas/type_:PostStatsWeb'
          description: >-
            Stats scoped only to web views. Not relevant for posts published
            only to email
        clicks:
          type: array
          items:
            $ref: '#/components/schemas/type_:ClickStats'
          description: An array of click statistics for each URL in the post
      description: >-
        Optional list of stats for a post. Retrievable by including `expand:
        [stats]` in the post request body. <br><br> **Note:** If a timeout
        occurs while aggregating stats, subsequent requests may return
        consolidated click metrics rather than individual raw click metrics.
      title: PostStats
    type_posts:PostsAggregateStatsResponseStats:
      type: object
      properties:
        stats:
          $ref: '#/components/schemas/type_:PostStats'
      required:
        - stats
      title: PostsAggregateStatsResponseStats
    type_posts:PostsAggregateStatsResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_posts:PostsAggregateStatsResponseStats'
      required:
        - data
      title: PostsAggregateStatsResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/aggregate_stats"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/aggregate_stats';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/aggregate_stats"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/aggregate_stats")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/aggregate_stats")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/aggregate_stats', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/aggregate_stats");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/aggregate_stats")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get post <Badge intent="info" minimal outlined>OAuth Scope: posts:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/posts/{postId}

Retrieve a single Post belonging to a specific publication

Reference: https://developers.beehiiv.com/api-reference/posts/show

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/posts/{postId}:
    get:
      operationId: show
      summary: >-
        Get post <Badge intent="info" minimal outlined>OAuth Scope:
        posts:read</Badge>
      description: Retrieve a single Post belonging to a specific publication
      tags:
        - subpackage_posts
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: postId
          in: path
          description: The prefixed ID of the post object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PostId'
        - name: expand
          in: query
          description: >-
            Optionally expand the results by adding additional information.
            <br>`stats` - Adds statistics about the post(s).
            <br>`free_web_content` - Adds the web HTML rendered to a free
            reader. <br>`free_email_content` - Adds the email HTML rendered to a
            free reader. <br>`free_rss_content` - Adds the RSS feed HTML.
            <br>`premium_web_content` - Adds the web HTML rendered to a premium
            reader. <br>`premium_email_content` - Adds the email HTML rendered
            to a premium reader.
          required: false
          schema:
            type: array
            items:
              $ref: '#/components/schemas/type_posts:PostExpandField'
        - name: premium_tiers
          in: query
          description: >-
            Scope any expanded content output to the specified premium
            tiers.<br> This takes in an array of Display Names of the premium
            tiers.<br> Note: This is case insensitive.
          required: false
          schema:
            type: array
            items:
              type: string
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_posts:PostsGetResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:PostId:
      type: string
      description: The prefixed ID of the post.
      title: PostId
    type_posts:PostExpandField:
      type: string
      enum:
        - stats
        - free_web_content
        - free_email_content
        - free_rss_content
        - premium_web_content
        - premium_email_content
      title: PostExpandField
    type_:PostStatus:
      type: string
      enum:
        - draft
        - confirmed
        - archived
      default: draft
      description: >-
        The status of the post.<br>`draft` - not been scheduled.<br>`confirmed`
        - The post will be active after the `scheduled_at`.<br>`archived` - The
        post is no longer active.
      title: PostStatus
    type_:PostAudience:
      type: string
      enum:
        - free
        - premium
        - both
      description: >-
        The audience that the post is available to on the web. Only applicable
        if the platform is `web` or `both`.
      title: PostAudience
    type_:PostPlatform:
      type: string
      enum:
        - web
        - email
        - both
      description: The platform that the post is or will be published to.
      title: PostPlatform
    type_:FreePostContent:
      type: object
      properties:
        web:
          type: string
          description: The web HTML rendered to a free or annonomous reader.
        email:
          type: string
          description: The email HTML rendered to a free reader.
        rss:
          type: string
          description: The HTML that is rendered in RSS feeds.
      description: The requested free post HTML. This HTML has paywalls enforced.
      title: FreePostContent
    type_:PremiumPostContent:
      type: object
      properties:
        web:
          type: string
          description: The website HTML rendered to a free reader
        email:
          type: string
          description: The email HTML rendered to a premium reader
      description: >-
        The requested premium post HTML. This HTML does not have paywalls
        enforced.
      title: PremiumPostContent
    type_:PostContent:
      type: object
      properties:
        free:
          $ref: '#/components/schemas/type_:FreePostContent'
          description: The requested free post HTML. This HTML has paywalls enforced.
        premium:
          $ref: '#/components/schemas/type_:PremiumPostContent'
          description: >-
            The requested premium post HTML. This HTML does not have paywalls
            enforced.
      description: >-
        Optional html content for a post. Retrievable by including any of
        `expand: [free_web_content, free_email_content, free_rss_content,
        premium_web_content, premium_email_content]` in the post request body.


        **Note:** Generating HTML is slow. We recommend only requesting the HTML
        versions you need at the time.
      title: PostContent
    type_:PostStatsEmail:
      type: object
      properties:
        recipients:
          type: integer
          default: 0
          description: Total number of email recipients
        delivered:
          type: integer
          default: 0
          description: Total number of emails delivered
        opens:
          type: integer
          default: 0
          description: Total number of email opens
        unique_opens:
          type: integer
          default: 0
          description: Total number of unique email opens
        open_rate:
          type: number
          format: double
          description: The percentage of emails that have been opened
        clicks:
          type: integer
          default: 0
          description: Total number of email clicks
        unique_clicks:
          type: integer
          default: 0
          description: Unique number of email clicks
        verified_clicks:
          type: integer
          default: 0
          description: >-
            Total number of verified human email clicks across all URLs in this
            post. Verified clicks have passed bot detection and are confirmed to
            be from real subscribers.
        unique_verified_clicks:
          type: integer
          default: 0
          description: >-
            Unique number of verified human email clicks across all URLs in this
            post. Only counts the first verified click per subscriber.
        click_rate:
          type: number
          format: double
          description: The percentage of emails that have been clicked
        unsubscribes:
          type: integer
          default: 0
          description: Total number of email unsubscribes
        spam_reports:
          type: integer
          default: 0
          description: The number of subscribers that reported this post email as spam
      description: >-
        Stats scoped only to email recipients. Not relevant for posts published
        only to web
      title: PostStatsEmail
    type_:PostStatsWeb:
      type: object
      properties:
        views:
          type: integer
          default: 0
          description: Total number of web views
        clicks:
          type: integer
          default: 0
          description: Total number of web clicks
      description: >-
        Stats scoped only to web views. Not relevant for posts published only to
        email
      title: PostStatsWeb
    type_:PostClickStatsEmail:
      type: object
      properties:
        clicks:
          type: integer
        unique_clicks:
          type: integer
        verified_clicks:
          type: integer
          description: >-
            Total number of verified human email clicks on this URL. Verified
            clicks have passed bot detection and are confirmed to be from real
            subscribers.
        unique_verified_clicks:
          type: integer
          description: >-
            Unique number of verified human email clicks on this URL. Only
            counts the first verified click per subscriber.
        click_through_rate:
          type: number
          format: double
          description: >-
            The percentage of email clicks on the URL compared to the total
            number of recipients
      description: >-
        URL stats scoped only to email recipients. Not relevant for posts
        published only to web
      title: PostClickStatsEmail
    type_:PostClickStatsWeb:
      type: object
      properties:
        clicks:
          type: integer
        unique_clicks:
          type: integer
        click_through_rate:
          type: number
          format: double
          description: >-
            The percentage of clicks on the URL compared to the total number of
            web views
      description: >-
        Stats scoped only to web views. Not relevant for posts published only to
        email
      title: PostClickStatsWeb
    type_:ClickStats:
      type: object
      properties:
        url:
          type: string
          description: The URL the stats are for
        base_url:
          type: string
          description: >-
            The canonical URL with all query parameters and fragments removed.
            Derived by stripping everything after the '?' and '#' characters.
            Preserves the protocol, host (including casing), port, and path
            exactly as they appear in the original URL. Guaranteed to be present
            whenever url is present, enabling grouping of clicks by destination
            regardless of tracking parameters.
        email:
          $ref: '#/components/schemas/type_:PostClickStatsEmail'
          description: >-
            URL stats scoped only to email recipients. Not relevant for posts
            published only to web
        web:
          $ref: '#/components/schemas/type_:PostClickStatsWeb'
          description: >-
            Stats scoped only to web views. Not relevant for posts published
            only to email
        total_clicks:
          type: integer
        total_unique_clicks:
          type: integer
        total_click_through_rate:
          type: number
          format: double
          description: >-
            The percentage of clicks on the URL compared to the total number of
            recipients and web views
      description: Details about specific URL's click stats from a post.
      title: ClickStats
    type_:PostStats:
      type: object
      properties:
        email:
          $ref: '#/components/schemas/type_:PostStatsEmail'
          description: >-
            Stats scoped only to email recipients. Not relevant for posts
            published only to web
        web:
          $ref: '#/components/schemas/type_:PostStatsWeb'
          description: >-
            Stats scoped only to web views. Not relevant for posts published
            only to email
        clicks:
          type: array
          items:
            $ref: '#/components/schemas/type_:ClickStats'
          description: An array of click statistics for each URL in the post
      description: >-
        Optional list of stats for a post. Retrievable by including `expand:
        [stats]` in the post request body. <br><br> **Note:** If a timeout
        occurs while aggregating stats, subsequent requests may return
        consolidated click metrics rather than individual raw click metrics.
      title: PostStats
    type_:Post:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:PostId'
          description: The prefixed post id
        subtitle:
          type: string
          description: The subtitle displayed in web views
        title:
          type: string
          description: The title displayed in web views
        authors:
          type: array
          items:
            type: string
          description: An array of author names
        created:
          type: integer
          description: >-
            The time the post was created. Measured in seconds since the Unix
            epoch
        status:
          $ref: '#/components/schemas/type_:PostStatus'
          description: >-
            The status of the post.<br>`draft` - not been
            scheduled.<br>`confirmed` - The post will be active after the
            `scheduled_at`.<br>`archived` - The post is no longer active.
        publish_date:
          type: integer
          description: >-
            The time the post was set to be published. Measured in seconds since
            the Unix epoch
        displayed_date:
          type: integer
          description: >-
            The time displayed in place of the `publish_date`. Measured in
            seconds since the Unix epoch
        split_tested:
          type: boolean
          description: >-
            A flag to indicate if a split test was done. Only applicable to
            email posts.
        subject_line:
          type: string
          description: >-
            The email subject line. In cases of A/B Testing, this will be
            adjusted to the winning subject line.
        preview_text:
          type: string
          description: The email preview text
        slug:
          type: string
          description: The web slug where this post can be accessed.
        thumbnail_url:
          type: string
          description: >-
            The URL of the thumbnail. Defaults to the Publication logo if not
            set.
        web_url:
          type: string
          description: >-
            The full URL where this post can be accessed on the web. Only
            applicable if the platform is `web` or `both`.
        audience:
          $ref: '#/components/schemas/type_:PostAudience'
          description: >-
            The audience that the post is available to on the web. Only
            applicable if the platform is `web` or `both`.
        platform:
          $ref: '#/components/schemas/type_:PostPlatform'
          description: The platform that the post is or will be published to.
        content_tags:
          type: array
          items:
            type: string
          description: All content tags that were associated with the post.
        meta_default_description:
          type: string
          description: >-
            Meta tag description for the post, called SEO Description in the
            admin UI
        meta_default_title:
          type: string
          description: meta tag title for the post, called SEO Title in the admin UI
        content:
          $ref: '#/components/schemas/type_:PostContent'
        stats:
          $ref: '#/components/schemas/type_:PostStats'
        hidden_from_feed:
          type: boolean
          default: false
          description: A flag to indicate if the post is hidden from the website feed.
        enforce_gated_content:
          type: boolean
          default: false
          description: >-
            A flag to indicate if the post enforces gated content for
            non-subscribers.
        email_capture_popup:
          type: boolean
          default: false
          description: A flag to indicate if popup email capture is enabled for this post.
      required:
        - id
        - subtitle
        - title
        - authors
        - created
        - status
        - split_tested
        - subject_line
        - preview_text
        - slug
        - thumbnail_url
        - web_url
        - audience
        - platform
        - content_tags
        - hidden_from_feed
        - enforce_gated_content
        - email_capture_popup
      title: Post
    type_posts:PostsGetResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_:Post'
      required:
        - data
      title: PostsGetResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.posts.get("post_00000000-0000-0000-0000-000000000000", "pub_00000000-0000-0000-0000-000000000000");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/post_00000000-0000-0000-0000-000000000000"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/post_00000000-0000-0000-0000-000000000000"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/post_00000000-0000-0000-0000-000000000000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/post_00000000-0000-0000-0000-000000000000")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/post_00000000-0000-0000-0000-000000000000', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/post_00000000-0000-0000-0000-000000000000");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/post_00000000-0000-0000-0000-000000000000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Delete post <Badge intent="info" minimal outlined>OAuth Scope: posts:write</Badge>

DELETE https://api.beehiiv.com/v2/publications/{publicationId}/posts/{postId}

Delete or Archive a post. Any post that has been confirmed will have it's status changed to `archived`. Posts in the `draft` status will be permanently deleted.

Reference: https://developers.beehiiv.com/api-reference/posts/delete

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/posts/{postId}:
    delete:
      operationId: delete
      summary: >-
        Delete post <Badge intent="info" minimal outlined>OAuth Scope:
        posts:write</Badge>
      description: >-
        Delete or Archive a post. Any post that has been confirmed will have
        it's status changed to `archived`. Posts in the `draft` status will be
        permanently deleted.
      tags:
        - subpackage_posts
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: postId
          in: path
          description: The prefixed ID of the post object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PostId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '204':
          description: No Content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_posts:PostsDeleteResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:PostId:
      type: string
      description: The prefixed ID of the post.
      title: PostId
    type_posts:PostsDeleteResponse:
      type: object
      properties: {}
      title: PostsDeleteResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.posts.delete("post_00000000-0000-0000-0000-000000000000", "pub_00000000-0000-0000-0000-000000000000");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/post_00000000-0000-0000-0000-000000000000"

payload = {}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.delete(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/post_00000000-0000-0000-0000-000000000000"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("DELETE", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/post_00000000-0000-0000-0000-000000000000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/post_00000000-0000-0000-0000-000000000000")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/post_00000000-0000-0000-0000-000000000000', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/post_00000000-0000-0000-0000-000000000000");
var request = new RestRequest(Method.DELETE);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/posts/post_00000000-0000-0000-0000-000000000000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get post templates

GET https://api.beehiiv.com/v2/publications/{publicationId}/post_templates

Retrieve a list of post templates available for the publication.

Reference: https://developers.beehiiv.com/api-reference/post-templates/index

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/post_templates:
    get:
      operationId: index
      summary: Get post templates
      description: Retrieve a list of post templates available for the publication.
      tags:
        - subpackage_postTemplates
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: limit
          in: query
          description: >-
            A limit on the number of objects to be returned. The limit can range
            between 1 and 100, and the default is 10.
          required: false
          schema:
            type: integer
        - name: page
          in: query
          description: >-
            Pagination returns the results in pages. Each page contains the
            number of results specified by the `limit` (default: 10).<br>If not
            specified, results 1-10 from page 1 will be returned.
          required: false
          schema:
            type: integer
        - name: order
          in: query
          description: The direction of the request. Defaults to `asc`.
          required: false
          schema:
            $ref: '#/components/schemas/type_:RequestDirection'
        - name: order_by
          in: query
          description: The field to order by. Defaults to `created`.
          required: false
          schema:
            type: string
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_postTemplates:PostTemplatesGetResponse
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_:RequestDirection:
      type: string
      enum:
        - asc
        - desc
      default: asc
      description: The direction of the request. Defaults to `asc`.
      title: RequestDirection
    type_ids:PostTemplateId:
      type: string
      description: The prefixed ID of the post template.
      title: PostTemplateId
    type_postTemplates:PostTemplate:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:PostTemplateId'
          description: The prefixed ID of the post template.
        name:
          type: string
          description: The name of the post template.
      required:
        - id
        - name
      title: PostTemplate
    type_postTemplates:PostTemplatesGetResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/type_postTemplates:PostTemplate'
          description: A list of post templates available for this publication.
        limit:
          type: integer
          description: >-
            The limit placed on the results. If no limit was specified in the
            request, this defaults to 10.
        page:
          type: integer
          default: 1
          description: >-
            The page number the results are from. If no page was specified in
            the request, this defaults to page 1.
        total_results:
          type: integer
          description: The total number of results from all pages.
        total_pages:
          type: integer
          description: The total number of pages.
      required:
        - data
        - limit
        - page
        - total_results
        - total_pages
      title: PostTemplatesGetResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/post_templates"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/post_templates';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/post_templates"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/post_templates")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/post_templates")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/post_templates', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/post_templates");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/post_templates")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# List publications <Badge intent="info" minimal outlined>OAuth Scope: publications:read</Badge>

GET https://api.beehiiv.com/v2/publications

Retrieve all publications associated with your API key.

Reference: https://developers.beehiiv.com/api-reference/publications/index

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications:
    get:
      operationId: index
      summary: >-
        List publications <Badge intent="info" minimal outlined>OAuth Scope:
        publications:read</Badge>
      description: Retrieve all publications associated with your API key.
      tags:
        - subpackage_publications
      parameters:
        - name: expand
          in: query
          description: >-
            Optionally expand the results by adding additional information like
            subscription counts and engagement stats.
          required: false
          schema:
            type: array
            items:
              $ref: >-
                #/components/schemas/type_publications:PublicationsRequestExpandItem
        - name: limit
          in: query
          description: >-
            A limit on the number of objects to be returned. The limit can range
            between 1 and 100, and the default is 10.
          required: false
          schema:
            type: integer
        - name: page
          in: query
          description: >-
            Pagination returns the results in pages. Each page contains the
            number of results specified by the `limit` (default: 10).<br>If not
            specified, results 1-10 from page 1 will be returned.
          required: false
          schema:
            type: integer
        - name: direction
          in: query
          description: >-
            The direction that the results are sorted in. Defaults to asc<br>
            `asc` - Ascending, sorts from smallest to largest.<br> `desc` -
            Descending, sorts from largest to smallest.
          required: false
          schema:
            $ref: '#/components/schemas/type_:RequestDirection'
        - name: order_by
          in: query
          description: >-
            The field that the results are sorted by. Defaults to created<br>
            `created` - The time in which the publication was first created.<br>
            `name` - The name of the publication.
          required: false
          schema:
            $ref: >-
              #/components/schemas/type_publications:PublicationsListRequestOrderBy
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_publications:PublicationsListResponse
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_publications:PublicationsRequestExpandItem:
      type: string
      enum:
        - stats
        - stat_active_subscriptions
        - stat_active_premium_subscriptions
        - stat_active_free_subscriptions
        - stat_average_open_rate
        - stat_average_click_rate
        - stat_total_sent
        - stat_total_unique_opened
        - stat_total_clicked
      title: PublicationsRequestExpandItem
    type_:RequestDirection:
      type: string
      enum:
        - asc
        - desc
      default: asc
      description: The direction of the request. Defaults to `asc`.
      title: RequestDirection
    type_publications:PublicationsListRequestOrderBy:
      type: string
      enum:
        - created
        - name
      default: created
      title: PublicationsListRequestOrderBy
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_:ActiveSubscriptionCount:
      oneOf:
        - type: integer
        - type: boolean
      description: Total number of active free and premium subscriptions
      title: ActiveSubscriptionCount
    type_:ActivePremiumSubscriptionCount:
      oneOf:
        - type: integer
        - type: boolean
      description: Total number of active premium/paid subscriptions
      title: ActivePremiumSubscriptionCount
    type_:ActiveFreeSubscriptionCount:
      oneOf:
        - type: integer
        - type: boolean
      description: Total number of active free subscriptions
      title: ActiveFreeSubscriptionCount
    type_:AverageOpenRate:
      oneOf:
        - type: number
          format: double
        - type: boolean
      description: The publications historical average open rate
      title: AverageOpenRate
    type_:AverageClickRate:
      oneOf:
        - type: number
          format: double
        - type: boolean
      description: The publications historical average click through rate
      title: AverageClickRate
    type_:TotalEmailsSent:
      oneOf:
        - type: integer
        - type: boolean
      description: Total number of emails sent
      title: TotalEmailsSent
    type_:TotalUniqueOpens:
      oneOf:
        - type: integer
        - type: boolean
      description: >-
        Total number of uniquely opened emails. Only counts the first open for
        each subscriber.
      title: TotalUniqueOpens
    type_:TotalClicks:
      oneOf:
        - type: integer
        - type: boolean
      description: The total number of links clicked from emails.
      title: TotalClicks
    type_:PublicationStats:
      type: object
      properties:
        active_subscriptions:
          $ref: '#/components/schemas/type_:ActiveSubscriptionCount'
          description: Total number of active free and premium subscriptions
        active_premium_subscriptions:
          $ref: '#/components/schemas/type_:ActivePremiumSubscriptionCount'
          description: Total number of active premium/paid subscriptions
        active_free_subscriptions:
          $ref: '#/components/schemas/type_:ActiveFreeSubscriptionCount'
          description: Total number of active free subscriptions
        average_open_rate:
          $ref: '#/components/schemas/type_:AverageOpenRate'
          description: The publications historical average open rate
        average_click_rate:
          $ref: '#/components/schemas/type_:AverageClickRate'
          description: The publications historical average click through rate
        total_sent:
          $ref: '#/components/schemas/type_:TotalEmailsSent'
          description: Total number of emails sent
        total_unique_opened:
          $ref: '#/components/schemas/type_:TotalUniqueOpens'
          description: >-
            Total number of uniquely opened emails. Only counts the first open
            for each subscriber.
        total_clicked:
          $ref: '#/components/schemas/type_:TotalClicks'
          description: The total number of links clicked from emails.
      description: >-
        Optional list of stats for a publication. Retrievable by including an
        `expand` array in the publication request body. Add `"stats"` to the
        array to retrieve all, or add individual stats (prefaced with `stat_`)
        to only retrieve specific ones.


        Examples:

        {
          "expand": ["stats"]
        }


        {
          "expand": ["stat_active_subscriptions", "stat_average_click_rate"]
        }
      title: PublicationStats
    type_:Publication:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:PublicationId'
          description: A unique prefixed id of the publication
        name:
          type: string
          description: The name of the publication
        organization_name:
          type: string
          description: The name of the organization
        referral_program_enabled:
          type: boolean
          description: >-
            A boolean field indicating whether the referral program is active
            for this publication.
        created:
          type: number
          format: double
          description: >-
            The time that the publication was created. Measured in seconds since
            the Unix epoch
        stats:
          $ref: '#/components/schemas/type_:PublicationStats'
      required:
        - id
        - name
        - organization_name
        - referral_program_enabled
        - created
      title: Publication
    type_publications:PublicationsListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/type_:Publication'
        limit:
          type: integer
          description: >-
            The limit placed on the results. If no limit was specified in the
            request,this defaults to 10.
        page:
          type: integer
          default: 1
          description: >-
            The page number the results are from. If no page was specified in
            the request, this defaults to page 1.
        total_results:
          type: integer
          description: The total number of results from all pages.
        total_pages:
          type: integer
          description: The total number of pages.
      required:
        - data
        - limit
        - page
        - total_results
        - total_pages
      title: PublicationsListResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient, Beehiiv } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.publications.list({
    expand: Beehiiv.PublicationsListRequestExpandItem.Stats
});

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get publication <Badge intent="info" minimal outlined>OAuth Scope: publications:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}

Retrieve a single publication

Reference: https://developers.beehiiv.com/api-reference/publications/show

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}:
    get:
      operationId: show
      summary: >-
        Get publication <Badge intent="info" minimal outlined>OAuth Scope:
        publications:read</Badge>
      description: Retrieve a single publication
      tags:
        - subpackage_publications
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: expand
          in: query
          description: >-
            Optionally expand the results by adding additional information like
            subscription counts and engagement stats.
          required: false
          schema:
            type: array
            items:
              $ref: >-
                #/components/schemas/type_publications:PublicationsGetRequestExpandItem
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_publications:PublicationsGetResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_publications:PublicationsGetRequestExpandItem:
      type: string
      enum:
        - stats
        - stat_active_subscriptions
        - stat_active_premium_subscriptions
        - stat_active_free_subscriptions
        - stat_average_open_rate
        - stat_average_click_rate
        - stat_total_sent
        - stat_total_unique_opened
        - stat_total_clicked
      title: PublicationsGetRequestExpandItem
    type_:ActiveSubscriptionCount:
      oneOf:
        - type: integer
        - type: boolean
      description: Total number of active free and premium subscriptions
      title: ActiveSubscriptionCount
    type_:ActivePremiumSubscriptionCount:
      oneOf:
        - type: integer
        - type: boolean
      description: Total number of active premium/paid subscriptions
      title: ActivePremiumSubscriptionCount
    type_:ActiveFreeSubscriptionCount:
      oneOf:
        - type: integer
        - type: boolean
      description: Total number of active free subscriptions
      title: ActiveFreeSubscriptionCount
    type_:AverageOpenRate:
      oneOf:
        - type: number
          format: double
        - type: boolean
      description: The publications historical average open rate
      title: AverageOpenRate
    type_:AverageClickRate:
      oneOf:
        - type: number
          format: double
        - type: boolean
      description: The publications historical average click through rate
      title: AverageClickRate
    type_:TotalEmailsSent:
      oneOf:
        - type: integer
        - type: boolean
      description: Total number of emails sent
      title: TotalEmailsSent
    type_:TotalUniqueOpens:
      oneOf:
        - type: integer
        - type: boolean
      description: >-
        Total number of uniquely opened emails. Only counts the first open for
        each subscriber.
      title: TotalUniqueOpens
    type_:TotalClicks:
      oneOf:
        - type: integer
        - type: boolean
      description: The total number of links clicked from emails.
      title: TotalClicks
    type_:PublicationStats:
      type: object
      properties:
        active_subscriptions:
          $ref: '#/components/schemas/type_:ActiveSubscriptionCount'
          description: Total number of active free and premium subscriptions
        active_premium_subscriptions:
          $ref: '#/components/schemas/type_:ActivePremiumSubscriptionCount'
          description: Total number of active premium/paid subscriptions
        active_free_subscriptions:
          $ref: '#/components/schemas/type_:ActiveFreeSubscriptionCount'
          description: Total number of active free subscriptions
        average_open_rate:
          $ref: '#/components/schemas/type_:AverageOpenRate'
          description: The publications historical average open rate
        average_click_rate:
          $ref: '#/components/schemas/type_:AverageClickRate'
          description: The publications historical average click through rate
        total_sent:
          $ref: '#/components/schemas/type_:TotalEmailsSent'
          description: Total number of emails sent
        total_unique_opened:
          $ref: '#/components/schemas/type_:TotalUniqueOpens'
          description: >-
            Total number of uniquely opened emails. Only counts the first open
            for each subscriber.
        total_clicked:
          $ref: '#/components/schemas/type_:TotalClicks'
          description: The total number of links clicked from emails.
      description: >-
        Optional list of stats for a publication. Retrievable by including an
        `expand` array in the publication request body. Add `"stats"` to the
        array to retrieve all, or add individual stats (prefaced with `stat_`)
        to only retrieve specific ones.


        Examples:

        {
          "expand": ["stats"]
        }


        {
          "expand": ["stat_active_subscriptions", "stat_average_click_rate"]
        }
      title: PublicationStats
    type_:Publication:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:PublicationId'
          description: A unique prefixed id of the publication
        name:
          type: string
          description: The name of the publication
        organization_name:
          type: string
          description: The name of the organization
        referral_program_enabled:
          type: boolean
          description: >-
            A boolean field indicating whether the referral program is active
            for this publication.
        created:
          type: number
          format: double
          description: >-
            The time that the publication was created. Measured in seconds since
            the Unix epoch
        stats:
          $ref: '#/components/schemas/type_:PublicationStats'
      required:
        - id
        - name
        - organization_name
        - referral_program_enabled
        - created
      title: Publication
    type_publications:PublicationsGetResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_:Publication'
      required:
        - data
      title: PublicationsGetResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient, Beehiiv } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.publications.get("pub_ad76629e-4a39-43ad-8055-0ee89dc6db15", {
    expand: Beehiiv.PublicationsGetRequestExpandItem.Stats
});

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_ad76629e-4a39-43ad-8055-0ee89dc6db15"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_ad76629e-4a39-43ad-8055-0ee89dc6db15"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_ad76629e-4a39-43ad-8055-0ee89dc6db15")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_ad76629e-4a39-43ad-8055-0ee89dc6db15")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_ad76629e-4a39-43ad-8055-0ee89dc6db15', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_ad76629e-4a39-43ad-8055-0ee89dc6db15");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_ad76629e-4a39-43ad-8055-0ee89dc6db15")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get referral program <Badge intent="info" minimal outlined>OAuth Scope: referral_program:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/referral_program

Retrieve details about the publication's referral program, including milestones and rewards.

Reference: https://developers.beehiiv.com/api-reference/referral-program/show

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/referral_program:
    get:
      operationId: show
      summary: >-
        Get referral program <Badge intent="info" minimal outlined>OAuth Scope:
        referral_program:read</Badge>
      description: >-
        Retrieve details about the publication's referral program, including
        milestones and rewards.
      tags:
        - subpackage_referralProgram
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: limit
          in: query
          description: >-
            A limit on the number of objects to be returned. The limit can range
            between 1 and 100, and the default is 10.
          required: false
          schema:
            type: integer
        - name: page
          in: query
          description: >-
            Pagination returns the results in pages. Each page contains the
            number of results specified by the `limit` (default: 10).<br>If not
            specified, results 1-10 from page 1 will be returned.
          required: false
          schema:
            type: integer
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_referralProgram:ReferralProgramGetResponse
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:MilestoneId:
      type: string
      description: The prefixed ID of the milestone.
      title: MilestoneId
    type_ids:RewardId:
      type: string
      description: The prefixed ID of the reward.
      title: RewardId
    type_:MilestoneRewardType:
      type: string
      enum:
        - physical
        - promo_code
        - digital
        - premium_gift
      description: >-
        What type of reward this is.<br>`physical` - A product which must be
        sent to the subscriber.<br>`promo_code` - A code that is redeemable for
        goods or services.
      title: MilestoneRewardType
    type_:MilestoneReward:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:RewardId'
          description: A unique prefixed id of the reward.
        name:
          type: string
          description: The name given to the reward at creation.
        description:
          type: string
          description: The description given to the name at creation.
        image_url:
          type: string
          description: A URL of an image to be displayed with the reward.
        type:
          $ref: '#/components/schemas/type_:MilestoneRewardType'
          description: >-
            What type of reward this is.<br>`physical` - A product which must be
            sent to the subscriber.<br>`promo_code` - A code that is redeemable
            for goods or services.
      required:
        - id
        - name
        - description
        - image_url
        - type
      description: The reward object.
      title: MilestoneReward
    type_:Milestone:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:MilestoneId'
          description: A unique prefixed id of the milestone.
        auto_fulfill:
          type: boolean
          description: >-
            Only available with a promo code reward type. This indicates that an
            email will automatically be sent when the milestone is reached
            containing the reward promo code.
        num_referrals:
          type: integer
          description: The number of referrals needed to reach this milestone.
        reward:
          $ref: '#/components/schemas/type_:MilestoneReward'
      required:
        - id
        - auto_fulfill
        - num_referrals
        - reward
      description: The milestone object.
      title: Milestone
    type_referralProgram:ReferralProgramGetResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/type_:Milestone'
          description: >-
            A list of the milestones related to this publication's referral
            program.
        limit:
          type: integer
          description: >-
            The limit placed on the results. If no limit was specified in the
            request,this defaults to 10.
        page:
          type: integer
          default: 1
          description: >-
            The page number the results are from. If no page was specified in
            the request, this defaults to page 1.
        total_results:
          type: integer
          description: The total number of results from all pages.
        total_pages:
          type: integer
          description: The total number of pages.
      required:
        - data
        - limit
        - page
        - total_results
        - total_pages
      title: ReferralProgramGetResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.referralProgram.get("pub_00000000-0000-0000-0000-000000000000");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/referral_program"

payload = {}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/referral_program"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/referral_program")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/referral_program")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/referral_program', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/referral_program");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/referral_program")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# List segments <Badge intent="info" minimal outlined>OAuth Scope: segments:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/segments

Retrieve information about all segments belonging to a specific publication

Reference: https://developers.beehiiv.com/api-reference/segments/index

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/segments:
    get:
      operationId: index
      summary: >-
        List segments <Badge intent="info" minimal outlined>OAuth Scope:
        segments:read</Badge>
      description: >-
        Retrieve information about all segments belonging to a specific
        publication
      tags:
        - subpackage_segments
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: type
          in: query
          description: Optionally filter the results by the segment's type.
          required: false
          schema:
            $ref: '#/components/schemas/type_:SegmentType'
        - name: status
          in: query
          description: Optionally filter the results by the segment's status.
          required: false
          schema:
            $ref: '#/components/schemas/type_segments:SegmentRequestStatus'
        - name: limit
          in: query
          description: >-
            A limit on the number of objects to be returned. The limit can range
            between 1 and 100, and the default is 10.
          required: false
          schema:
            type: integer
        - name: page
          in: query
          description: >-
            Pagination returns the results in pages. Each page contains the
            number of results specified by the `limit` (default: 10).<br>If not
            specified, results 1-10 from page 1 will be returned.
          required: false
          schema:
            type: integer
        - name: order_by
          in: query
          description: >-
            The field that the results are sorted by. Defaults to created<br>
            `created` - The time in which the segment was first created.<br>
            `last_calculated` - The time that the segment last completed
            calculation. Measured in seconds since the Unix epoch.
          required: false
          schema:
            $ref: '#/components/schemas/type_segments:SegmentOrderBy'
        - name: direction
          in: query
          description: >-
            The direction that the results are sorted in. Defaults to asc<br>
            `asc` - Ascending, sorts from smallest to largest.<br> `desc` -
            Descending, sorts from largest to smallest.
          required: false
          schema:
            $ref: '#/components/schemas/type_:RequestDirection'
        - name: expand[]
          in: query
          description: >-
            Optionally expand the response to include additional data. <br>
            `stats` - Requests the most recently calculated statistics for a
            segment. <br> Segment stats are recalculated once daily around 7
            a.m. UTC for dynamic segments, but can be manually recalculated at
            any time in the dashboard. Manual and static segments only calculate
            once upon upload or creation.
          required: false
          schema:
            type: array
            items:
              $ref: '#/components/schemas/type_segments:SegmentsExpandItems'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_segments:SegmentsListResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_:SegmentType:
      type: string
      enum:
        - dynamic
        - static
        - manual
        - all
      default: all
      description: >-
        The type of segment.<br>`dynamic` - The segment is recalculated at set
        intervals.<br>`static` - The segment is calculated once at
        creation.<br>`manual` - The segment is not calculated at all. The
        results are created via CSV.
      title: SegmentType
    type_segments:SegmentRequestStatus:
      type: string
      enum:
        - pending
        - processing
        - completed
        - failed
        - all
      default: all
      title: SegmentRequestStatus
    type_segments:SegmentOrderBy:
      type: string
      enum:
        - created
        - last_calculated
      default: created
      title: SegmentOrderBy
    type_:RequestDirection:
      type: string
      enum:
        - asc
        - desc
      default: asc
      description: The direction of the request. Defaults to `asc`.
      title: RequestDirection
    type_segments:SegmentsExpandItems:
      type: string
      enum:
        - stats
      title: SegmentsExpandItems
    type_ids:SegmentId:
      type: string
      description: The prefixed ID of the segment.
      title: SegmentId
    type_:SegmentStatus:
      type: string
      enum:
        - pending
        - processing
        - completed
        - failed
      description: >-
        The status of the segment's most recent calculation.<br>`pending` - The
        segment has not been calculated yet.<br>`processing` - The calculation
        is in progress, and has not completed.<br>`completed` - The calculation
        was successful.<br>`failed` - Something went wrong during the
        calculation.
      title: SegmentStatus
    type_:SegmentStats:
      type: object
      properties:
        open_rate:
          type: number
          format: double
          description: The average open rate of the subscribers in the segment.
        total_sent:
          type: integer
          description: The total number of emails sent to the subscribers in the segment.
        percentage_premium_subscribers:
          type: number
          format: double
          description: >-
            The percentage of subscribers in this segment who are premium in any
            tier.
        percentage_subscribers_with_referrals:
          type: number
          format: double
          description: >-
            The percentage of subscribers in this segment who have referred at
            least one other subscriber.
        unique_emails_clicked:
          type: integer
          description: >-
            The total number of unique emails clicked by subscribers in the
            segment.
        total_delivered:
          type: integer
          description: The total number of emails delivered to subscribers in the segment.
        total_referrals:
          type: integer
          description: The total number of referrals from subscribers in the segment.
        unsubscribed_rate:
          type: number
          format: double
          description: The percentage of subscribers in this segment who have unsubscribed.
        total_subscribers:
          type: integer
          description: The total number of subscribers in the segment.
        clickthrough_rate:
          type: number
          format: double
          description: The average clickthrough rate of the subscribers in the segment.
        unsubscribed_count:
          type: integer
          description: The total number of subscribers in the segment who are unsubscribed.
        unique_emails_opened:
          type: integer
          description: >-
            The total number of unique emails opened by subscribers in the
            segment.
        premium_subscribers:
          type: integer
          description: The total number of premium subscribers in the segment.
        average_referrals_per_subscriber:
          type: number
          format: double
          description: The average number of referrals per subscriber in the segment.
      required:
        - open_rate
        - total_sent
        - percentage_premium_subscribers
        - percentage_subscribers_with_referrals
        - unique_emails_clicked
        - total_delivered
        - total_referrals
        - unsubscribed_rate
        - total_subscribers
        - clickthrough_rate
        - unsubscribed_count
        - unique_emails_opened
        - premium_subscribers
        - average_referrals_per_subscriber
      title: SegmentStats
    type_:Segment:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:SegmentId'
          description: The prefixed ID of the segment.
        name:
          type: string
          description: The name of the segment.
        type:
          $ref: '#/components/schemas/type_:SegmentType'
          description: >-
            The type of segment.<br>`dynamic` - The segment is recalculated at
            set intervals.<br>`static` - The segment is calculated once at
            creation.<br>`manual` - The segment is not calculated at all. The
            results are created via CSV.
        last_calculated:
          type: integer
          description: >-
            The time the Segment was last calculated. Measured in seconds since
            the Unix epoch
        total_results:
          type: integer
          description: >-
            The total number of subscriptions that belong in the segment from
            the last calculation.
        status:
          $ref: '#/components/schemas/type_:SegmentStatus'
          description: >-
            The status of the segment's most recent calculation.<br>`pending` -
            The segment has not been calculated yet.<br>`processing` - The
            calculation is in progress, and has not completed.<br>`completed` -
            The calculation was successful.<br>`failed` - Something went wrong
            during the calculation.
        active:
          type: boolean
          description: >-
            Dynamic segments are marked inactive if they haven't been used in a
            specific period of time. Inactive segments will not automatically be
            recalculated.
        stats:
          $ref: '#/components/schemas/type_:SegmentStats'
      required:
        - id
        - name
        - type
        - total_results
        - status
        - active
      description: The segment object. To expand results, see the results endpoint.
      title: Segment
    type_segments:SegmentsListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/type_:Segment'
          description: An array of all segments.
        limit:
          type: integer
          description: >-
            The limit placed on the results. If no limit was specified in the
            request,this defaults to 10.
        page:
          type: integer
          default: 1
          description: >-
            The page number the results are from. If no page was specified in
            the request, this defaults to page 1.
        total_results:
          type: integer
          description: The total number of results from all pages.
        total_pages:
          type: integer
          description: The total number of pages.
      required:
        - data
        - limit
        - page
        - total_results
        - total_pages
      title: SegmentsListResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.segments.list("pub_00000000-0000-0000-0000-000000000000");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get segment <Badge intent="info" minimal outlined>OAuth Scope: segments:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/segments/{segmentId}

Retrieve information about a specific segment belonging to a publication

Reference: https://developers.beehiiv.com/api-reference/segments/show

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/segments/{segmentId}:
    get:
      operationId: show
      summary: >-
        Get segment <Badge intent="info" minimal outlined>OAuth Scope:
        segments:read</Badge>
      description: Retrieve information about a specific segment belonging to a publication
      tags:
        - subpackage_segments
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: segmentId
          in: path
          description: The prefixed ID of the segment object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:SegmentId'
        - name: expand[]
          in: query
          description: >-
            Optionally expand the response to include additional data. <br>
            `stats` - Requests the most recently calculated statistics for a
            segment. <br> Segment stats are recalculated once daily around 7
            a.m. UTC for dynamic segments, but can be manually recalculated at
            any time in the dashboard. Manual and static segments only calculate
            once upon upload or creation.
          required: false
          schema:
            type: array
            items:
              $ref: '#/components/schemas/type_segments:SegmentsExpandItems'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_segments:SegmentShowResponse'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:SegmentId:
      type: string
      description: The prefixed ID of the segment.
      title: SegmentId
    type_segments:SegmentsExpandItems:
      type: string
      enum:
        - stats
      title: SegmentsExpandItems
    type_:SegmentType:
      type: string
      enum:
        - dynamic
        - static
        - manual
        - all
      default: all
      description: >-
        The type of segment.<br>`dynamic` - The segment is recalculated at set
        intervals.<br>`static` - The segment is calculated once at
        creation.<br>`manual` - The segment is not calculated at all. The
        results are created via CSV.
      title: SegmentType
    type_:SegmentStatus:
      type: string
      enum:
        - pending
        - processing
        - completed
        - failed
      description: >-
        The status of the segment's most recent calculation.<br>`pending` - The
        segment has not been calculated yet.<br>`processing` - The calculation
        is in progress, and has not completed.<br>`completed` - The calculation
        was successful.<br>`failed` - Something went wrong during the
        calculation.
      title: SegmentStatus
    type_:SegmentStats:
      type: object
      properties:
        open_rate:
          type: number
          format: double
          description: The average open rate of the subscribers in the segment.
        total_sent:
          type: integer
          description: The total number of emails sent to the subscribers in the segment.
        percentage_premium_subscribers:
          type: number
          format: double
          description: >-
            The percentage of subscribers in this segment who are premium in any
            tier.
        percentage_subscribers_with_referrals:
          type: number
          format: double
          description: >-
            The percentage of subscribers in this segment who have referred at
            least one other subscriber.
        unique_emails_clicked:
          type: integer
          description: >-
            The total number of unique emails clicked by subscribers in the
            segment.
        total_delivered:
          type: integer
          description: The total number of emails delivered to subscribers in the segment.
        total_referrals:
          type: integer
          description: The total number of referrals from subscribers in the segment.
        unsubscribed_rate:
          type: number
          format: double
          description: The percentage of subscribers in this segment who have unsubscribed.
        total_subscribers:
          type: integer
          description: The total number of subscribers in the segment.
        clickthrough_rate:
          type: number
          format: double
          description: The average clickthrough rate of the subscribers in the segment.
        unsubscribed_count:
          type: integer
          description: The total number of subscribers in the segment who are unsubscribed.
        unique_emails_opened:
          type: integer
          description: >-
            The total number of unique emails opened by subscribers in the
            segment.
        premium_subscribers:
          type: integer
          description: The total number of premium subscribers in the segment.
        average_referrals_per_subscriber:
          type: number
          format: double
          description: The average number of referrals per subscriber in the segment.
      required:
        - open_rate
        - total_sent
        - percentage_premium_subscribers
        - percentage_subscribers_with_referrals
        - unique_emails_clicked
        - total_delivered
        - total_referrals
        - unsubscribed_rate
        - total_subscribers
        - clickthrough_rate
        - unsubscribed_count
        - unique_emails_opened
        - premium_subscribers
        - average_referrals_per_subscriber
      title: SegmentStats
    type_:Segment:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:SegmentId'
          description: The prefixed ID of the segment.
        name:
          type: string
          description: The name of the segment.
        type:
          $ref: '#/components/schemas/type_:SegmentType'
          description: >-
            The type of segment.<br>`dynamic` - The segment is recalculated at
            set intervals.<br>`static` - The segment is calculated once at
            creation.<br>`manual` - The segment is not calculated at all. The
            results are created via CSV.
        last_calculated:
          type: integer
          description: >-
            The time the Segment was last calculated. Measured in seconds since
            the Unix epoch
        total_results:
          type: integer
          description: >-
            The total number of subscriptions that belong in the segment from
            the last calculation.
        status:
          $ref: '#/components/schemas/type_:SegmentStatus'
          description: >-
            The status of the segment's most recent calculation.<br>`pending` -
            The segment has not been calculated yet.<br>`processing` - The
            calculation is in progress, and has not completed.<br>`completed` -
            The calculation was successful.<br>`failed` - Something went wrong
            during the calculation.
        active:
          type: boolean
          description: >-
            Dynamic segments are marked inactive if they haven't been used in a
            specific period of time. Inactive segments will not automatically be
            recalculated.
        stats:
          $ref: '#/components/schemas/type_:SegmentStats'
      required:
        - id
        - name
        - type
        - total_results
        - status
        - active
      description: The segment object. To expand results, see the results endpoint.
      title: Segment
    type_segments:SegmentShowResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_:Segment'
      required:
        - data
      title: SegmentShowResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Recalculate segment <Badge intent="info" minimal outlined>OAuth Scope: segments:write</Badge>

PUT https://api.beehiiv.com/v2/publications/{publicationId}/segments/{segmentId}/recalculate

Recalculates a specific segment belonging to a publication

Reference: https://developers.beehiiv.com/api-reference/segments/recalculate

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/segments/{segmentId}/recalculate:
    put:
      operationId: recalculate
      summary: >-
        Recalculate segment <Badge intent="info" minimal outlined>OAuth Scope:
        segments:write</Badge>
      description: Recalculates a specific segment belonging to a publication
      tags:
        - subpackage_segments
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: segmentId
          in: path
          description: The prefixed ID of the segment object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:SegmentId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_segments:SegmentRecalculateResponse'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '422':
          description: Unprocessable Entity
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:SegmentId:
      type: string
      description: The prefixed ID of the segment.
      title: SegmentId
    type_segments:SegmentRecalculateResponse:
      type: object
      properties:
        message:
          type: string
      title: SegmentRecalculateResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/recalculate"

payload = {}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/recalculate';
const options = {
  method: 'PUT',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/recalculate"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("PUT", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/recalculate")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/recalculate")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/recalculate', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/recalculate");
var request = new RestRequest(Method.PUT);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/recalculate")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PUT"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# List segment subscribers <Badge intent="info" minimal outlined>OAuth Scope: segments:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/segments/{segmentId}/members

List all members in a segment with full subscription data. Each member is returned as a subscription  object containing complete subscriber information and their subscription details.  Supports optional expansions for stats, custom fields, tags, referrals, and premium tiers.
**Use this endpoint when you need detailed subscriber information.** If you only need subscriber IDs, use `/segments/{segmentId}/results` for a lighter-weight response.

Reference: https://developers.beehiiv.com/api-reference/segments/list-members

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/segments/{segmentId}/members:
    get:
      operationId: list-members
      summary: >-
        List segment subscribers <Badge intent="info" minimal outlined>OAuth
        Scope: segments:read</Badge>
      description: >-
        List all members in a segment with full subscription data. Each member
        is returned as a subscription  object containing complete subscriber
        information and their subscription details.  Supports optional
        expansions for stats, custom fields, tags, referrals, and premium tiers.

        **Use this endpoint when you need detailed subscriber information.** If
        you only need subscriber IDs, use `/segments/{segmentId}/results` for a
        lighter-weight response.
      tags:
        - subpackage_segments
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: segmentId
          in: path
          description: The prefixed ID of the segment object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:SegmentId'
        - name: limit
          in: query
          description: >-
            A limit on the number of objects to be returned. The limit can range
            between 1 and 100, and the default is 10.
          required: false
          schema:
            type: integer
        - name: page
          in: query
          description: >-
            Pagination returns the results in pages. Each page contains the
            number of results specified by the `limit` (default: 10).<br>If not
            specified, results 1-10 from page 1 will be returned.
          required: false
          schema:
            type: integer
        - name: expand[]
          in: query
          description: >-
            Optionally expand the response to include additional data. <br>
            `stats` - Returns statistics about the subscription(s). <br>
            `custom_fields` - Returns custom field values set on the
            subscription. <br> `referrals` - Returns referrals made by the
            subscription. <br> `tags` - Returns tags associated with the
            subscription. <br> `subscription_premium_tiers` - Returns premium
            tier(s) the subscription is subscribed to.
          required: false
          schema:
            type: array
            items:
              $ref: '#/components/schemas/type_segments:SegmentMembersExpandItems'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_segments:SegmentMembersResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:SegmentId:
      type: string
      description: The prefixed ID of the segment.
      title: SegmentId
    type_segments:SegmentMembersExpandItems:
      type: string
      enum:
        - stats
        - custom_fields
        - referrals
        - tags
        - subscription_premium_tiers
      title: SegmentMembersExpandItems
    type_ids:SubscriptionId:
      type: string
      description: The prefixed ID of the subscription.
      title: SubscriptionId
    type_:SubscriptionExpandedStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
        - paused
      description: >-
        The status of the subscription.<br>`validating` - The email address is
        being validated.<br>`invalid` - The email address is
        invalid.<br>`pending` - The email address is valid, but the subscription
        is pending double opt-in.<br>`active` - The email was valid and the
        subscription is active.<br>`inactive` - The subscription was made
        inactive, possibly due to an unsubscribe.<br>`needs_attention` - The
        subscription requires approval or denial.<br>`paused` - The subscriber
        has paused their subscription.
      title: SubscriptionExpandedStatus
    type_:SubscriptionExpandedSubscriptionTier:
      type: string
      enum:
        - free
        - premium
      description: The current tier of the subscription.
      title: SubscriptionExpandedSubscriptionTier
    type_:SubscriptionExpandedUtmChannel:
      type: string
      enum:
        - ''
        - website
        - import
        - embed
        - api
        - referral
        - recommendation
        - magic_link
        - boost
        - boost_send
        - boost_direct_link
        - integration
        - product
      description: The acquisition channel
      title: SubscriptionExpandedUtmChannel
    type_ids:TierId:
      type: string
      description: The prefixed ID of the tier.
      title: TierId
    type_:SubscriptionTierInfoStatus:
      type: string
      enum:
        - active
        - archived
      description: Returns whether or not the tier has any active prices.
      title: SubscriptionTierInfoStatus
    type_:SubscriptionTierInfo:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:TierId'
        name:
          type: string
        status:
          $ref: '#/components/schemas/type_:SubscriptionTierInfoStatus'
          description: Returns whether or not the tier has any active prices.
      required:
        - id
        - name
        - status
      title: SubscriptionTierInfo
    type_:SubscriptionTierList:
      type: array
      items:
        $ref: '#/components/schemas/type_:SubscriptionTierInfo'
      description: >-
        Optional list of tiers for a subscription. Retrievable by including
        `expand: [subscription_premium_tiers]` in the request body.
      title: SubscriptionTierList
    type_:CustomFieldType:
      type: string
      enum:
        - string
        - integer
        - boolean
        - date
        - datetime
        - list
        - double
      description: The type of value being stored in the custom field.
      title: CustomFieldType
    type_:CustomFieldDataType:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: boolean
        - type: array
          items:
            type: string
      title: CustomFieldDataType
    type_:CustomField:
      type: object
      properties:
        name:
          type: string
          description: The name of the existing custom field
        kind:
          $ref: '#/components/schemas/type_:CustomFieldType'
          description: The type of value being stored in the custom field.
        value:
          $ref: '#/components/schemas/type_:CustomFieldDataType'
          description: The value stored for the subscription
      title: CustomField
    type_:SubscriptionCustomFieldList:
      type: array
      items:
        $ref: '#/components/schemas/type_:CustomField'
      description: >-
        Optional list of custom fields for a subscription. Retrievable by
        including `expand: [custom_field]` in the request body.
      title: SubscriptionCustomFieldList
    type_:SubscriptionTags:
      type: array
      items:
        type: string
      description: >-
        Optional list of tags for a subscription. Retrievable by including
        `expand: [tags]` in the request body.

        Max limit of 100 unique tags per publication.
      title: SubscriptionTags
    type_:SubscriptionStats:
      type: object
      properties:
        emails_received:
          type: integer
          description: The total number of emails that have been sent to this subscriber
        open_rate:
          type: number
          format: double
          description: The percentage of emails that the subscriber has opened
        click_through_rate:
          type: number
          format: double
          description: The percentage of emails that the subscriber has clicked a link in
      description: >-
        Optional list of stats for a subscription. Retrievable by including
        `expand: [stats]` in the request body.
      title: SubscriptionStats
    type_:Subscription:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:SubscriptionId'
          description: The prefixed subscription id
        email:
          type: string
          format: email
        status:
          $ref: '#/components/schemas/type_:SubscriptionExpandedStatus'
          description: >-
            The status of the subscription.<br>`validating` - The email address
            is being validated.<br>`invalid` - The email address is
            invalid.<br>`pending` - The email address is valid, but the
            subscription is pending double opt-in.<br>`active` - The email was
            valid and the subscription is active.<br>`inactive` - The
            subscription was made inactive, possibly due to an
            unsubscribe.<br>`needs_attention` - The subscription requires
            approval or denial.
        created:
          type: integer
          description: >-
            The date the subscription was created. Measured in seconds since the
            Unix epoch
        subscription_tier:
          $ref: '#/components/schemas/type_:SubscriptionExpandedSubscriptionTier'
          description: The current tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: >-
            The current premium tiers of the subscription. Empty if the
            subscriber is not associated with any premium tiers.
        utm_source:
          type: string
          description: The acquisition source; where the subscriber came from
        utm_medium:
          type: string
          description: The acquisition medium; how the subscriber got to your publication
        utm_channel:
          $ref: '#/components/schemas/type_:SubscriptionExpandedUtmChannel'
          description: The acquisition channel
        utm_campaign:
          type: string
          description: The acquisition campaign
        utm_term:
          type: string
          description: The acquisition term; typically the keyword or search term
        utm_content:
          type: string
          description: >-
            The acquisition content; typically used for A/B testing or ad
            variations
        referring_site:
          type: string
          description: The website that the subscriber was referred from
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        subscription_premium_tiers:
          $ref: '#/components/schemas/type_:SubscriptionTierList'
        custom_fields:
          $ref: '#/components/schemas/type_:SubscriptionCustomFieldList'
        tags:
          $ref: '#/components/schemas/type_:SubscriptionTags'
        stats:
          $ref: '#/components/schemas/type_:SubscriptionStats'
      required:
        - id
        - email
        - status
        - created
        - subscription_tier
        - subscription_premium_tier_names
        - utm_source
        - utm_medium
        - utm_channel
        - utm_campaign
        - utm_term
        - utm_content
        - referring_site
        - referral_code
      description: The subscription object
      title: Subscription
    type_segments:SegmentMembersResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/type_:Subscription'
        limit:
          type: integer
          description: >-
            The limit placed on the results. If no limit was specified in the
            request,this defaults to 10.
        page:
          type: integer
          default: 1
          description: >-
            The page number the results are from. If no page was specified in
            the request, this defaults to page 1.
        total_results:
          type: integer
          description: The total number of results from all pages.
        total_pages:
          type: integer
          description: The total number of pages.
      required:
        - data
        - limit
        - page
        - total_results
        - total_pages
      title: SegmentMembersResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/members"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/members';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/members"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/members")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/members")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/members', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/members");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/members")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# List segment subscriber IDs <Badge intent="info" minimal outlined>OAuth Scope: segments:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/segments/{segmentId}/results

List subscriber IDs for a segment. Returns a lightweight array of subscription IDs only, without additional subscriber details.
**Use this endpoint when you only need subscriber IDs** (e.g., for counting, ID-based lookups, or  integrations with external systems). If you need full subscriber details (email, status, custom fields, etc.), use `/segments/{segmentId}/members` instead.

Reference: https://developers.beehiiv.com/api-reference/segments/expand-results

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/segments/{segmentId}/results:
    get:
      operationId: expand-results
      summary: >-
        List segment subscriber IDs <Badge intent="info" minimal outlined>OAuth
        Scope: segments:read</Badge>
      description: >-
        List subscriber IDs for a segment. Returns a lightweight array of
        subscription IDs only, without additional subscriber details.

        **Use this endpoint when you only need subscriber IDs** (e.g., for
        counting, ID-based lookups, or  integrations with external systems). If
        you need full subscriber details (email, status, custom fields, etc.),
        use `/segments/{segmentId}/members` instead.
      tags:
        - subpackage_segments
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: segmentId
          in: path
          description: The prefixed ID of the segment object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:SegmentId'
        - name: limit
          in: query
          description: >-
            A limit on the number of objects to be returned. The limit can range
            between 1 and 100, and the default is 10.
          required: false
          schema:
            type: integer
        - name: page
          in: query
          description: >-
            Pagination returns the results in pages. Each page contains the
            number of results specified by the `limit` (default: 10).<br>If not
            specified, results 1-10 from page 1 will be returned.
          required: false
          schema:
            type: integer
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_segments:SegmentsGetResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:SegmentId:
      type: string
      description: The prefixed ID of the segment.
      title: SegmentId
    type_segments:SegmentsGetResponse:
      type: object
      properties:
        data:
          type: array
          items:
            type: string
          description: An array of subscription ids
        limit:
          type: integer
          description: >-
            The limit placed on the results. If no limit was specified in the
            request,this defaults to 10.
        page:
          type: integer
          default: 1
          description: >-
            The page number the results are from. If no page was specified in
            the request, this defaults to page 1.
        total_results:
          type: integer
          description: The total number of results from all pages.
        total_pages:
          type: integer
          description: The total number of pages.
      required:
        - data
        - limit
        - page
        - total_results
        - total_pages
      title: SegmentsGetResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.segments.get("pub_00000000-0000-0000-0000-000000000000", "seg_00000000-0000-0000-0000-000000000000");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/results"

payload = {}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/results"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/results")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/results")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/results', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/results");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000/results")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Delete segment <Badge intent="info" minimal outlined>OAuth Scope: segments:write</Badge>

DELETE https://api.beehiiv.com/v2/publications/{publicationId}/segments/{segmentId}

Delete a segment. Deleting the segment does not effect the subscriptions in the segment.

Reference: https://developers.beehiiv.com/api-reference/segments/delete

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/segments/{segmentId}:
    delete:
      operationId: delete
      summary: >-
        Delete segment <Badge intent="info" minimal outlined>OAuth Scope:
        segments:write</Badge>
      description: >-
        Delete a segment. Deleting the segment does not effect the subscriptions
        in the segment.
      tags:
        - subpackage_segments
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: segmentId
          in: path
          description: The prefixed ID of the segment object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:SegmentId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '204':
          description: No Content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_segments:SegmentDeleteResponse'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:SegmentId:
      type: string
      description: The prefixed ID of the segment.
      title: SegmentId
    type_segments:SegmentDeleteResponse:
      type: object
      properties:
        message:
          type: string
      title: SegmentDeleteResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.segments.delete("pub_00000000-0000-0000-0000-000000000000", "seg_00000000-0000-0000-0000-000000000000");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000"

payload = {}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.delete(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("DELETE", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000");
var request = new RestRequest(Method.DELETE);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/segments/seg_00000000-0000-0000-0000-000000000000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Create subscription <Badge intent="info" minimal outlined>OAuth Scope: subscriptions:write</Badge>

POST https://api.beehiiv.com/v2/publications/{publicationId}/subscriptions
Content-Type: application/json

Create new subscriptions for a publication.

Reference: https://developers.beehiiv.com/api-reference/subscriptions/create

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/subscriptions:
    post:
      operationId: create
      summary: >-
        Create subscription <Badge intent="info" minimal outlined>OAuth Scope:
        subscriptions:write</Badge>
      description: Create new subscriptions for a publication.
      tags:
        - subpackage_subscriptions
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Subscription created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_subscriptions:SubscriptionResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/type_:SubscriptionRequest'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_:CustomFieldDataType:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: boolean
        - type: array
          items:
            type: string
      title: CustomFieldDataType
    type_:CustomFieldValue:
      type: object
      properties:
        name:
          type: string
          description: The name of the existing custom field
        value:
          $ref: '#/components/schemas/type_:CustomFieldDataType'
          description: The value stored for the subscription
      description: The object required for setting custom field values on a subscription
      title: CustomFieldValue
    type_:DoubleOptOverride:
      type: string
      description: Override publication double-opt settings for this subscription.
      title: DoubleOptOverride
    type_:SubscriptionsCreateRequestTier:
      type: string
      enum:
        - free
        - premium
      description: The tier for this subscription.
      title: SubscriptionsCreateRequestTier
    type_ids:OptionalStripeCustomerId:
      type: string
      description: The prefixed ID of the Stripe customer.
      title: OptionalStripeCustomerId
    type_:SubscriptionRequest:
      type: object
      properties:
        email:
          type: string
          description: The email address of the subscription.
        reactivate_existing:
          type: boolean
          default: false
          description: >-
            Whether or not to reactivate the subscription if they have already
            unsubscribed. This option should be used only if the subscriber is
            knowingly resubscribing.
        send_welcome_email:
          type: boolean
          default: false
        utm_source:
          type: string
          description: The source of the subscription.
        utm_medium:
          type: string
          description: The medium of the subscription
        utm_campaign:
          type: string
          description: The acquisition campaign of the subscription
        utm_term:
          type: string
          description: The acquisition term; typically the keyword or search term
        utm_content:
          type: string
          description: >-
            The acquisition content; typically used for A/B testing or ad
            variations
        referring_site:
          type: string
          description: The website that the subscriber was referred from
        referral_code:
          type: string
          description: >-
            This should be a subscribers referral_code. This gives referral
            credit for the new subscription.
        custom_fields:
          type: array
          items:
            $ref: '#/components/schemas/type_:CustomFieldValue'
          description: >-
            The custom fields must already exist for the publication. Any new
            custom fields here will be discarded.
        double_opt_override:
          $ref: '#/components/schemas/type_:DoubleOptOverride'
          description: >-
            Override the publication's default double opt-in settings for this
            subscription. Possible values are:

            - "on" — The subscriber will receive a double opt-in confirmation
            email and will need to confirm their subscription prior to being
            marked as active.

            - "off" — The subscriber will be marked as active immediately and
            will not receive a double opt-in confirmation email.

            - "not_set" — The publication's default double opt-in settings will
            be applied to this subscription.
        tier:
          $ref: '#/components/schemas/type_:SubscriptionsCreateRequestTier'
          description: The tier for this subscription.
        premium_tiers:
          type: array
          items:
            type: string
          description: >-
            An array of premium tier names to assign to this subscription. When
            provided, the subscription will be assigned to premium tiers
            matching these names. Can be combined with `premium_tier_ids` to
            include tiers from both (duplicates are removed). Takes precedence
            over the `tier` parameter.
        premium_tier_ids:
          type: array
          items:
            type: string
          description: >-
            An array of premium tier IDs to assign to this subscription. When
            provided, the subscription will be assigned to these specific
            premium tiers. Can be combined with `premium_tiers` to include tiers
            from both (duplicates are removed). Takes precedence over the `tier`
            parameter.
        stripe_customer_id:
          $ref: '#/components/schemas/type_ids:OptionalStripeCustomerId'
          description: The Stripe customer ID for this subscription.
        automation_ids:
          type: array
          items:
            type: string
          description: >-
            Enroll the subscriber into automations after their subscription has
            been created. Requires the automations to have an active *Add by
            API* trigger.
      required:
        - email
      title: SubscriptionRequest
    type_ids:SubscriptionId:
      type: string
      description: The prefixed ID of the subscription.
      title: SubscriptionId
    type_:SubscriptionExpandedStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
        - paused
      description: >-
        The status of the subscription.<br>`validating` - The email address is
        being validated.<br>`invalid` - The email address is
        invalid.<br>`pending` - The email address is valid, but the subscription
        is pending double opt-in.<br>`active` - The email was valid and the
        subscription is active.<br>`inactive` - The subscription was made
        inactive, possibly due to an unsubscribe.<br>`needs_attention` - The
        subscription requires approval or denial.<br>`paused` - The subscriber
        has paused their subscription.
      title: SubscriptionExpandedStatus
    type_:SubscriptionExpandedSubscriptionTier:
      type: string
      enum:
        - free
        - premium
      description: The current tier of the subscription.
      title: SubscriptionExpandedSubscriptionTier
    type_:SubscriptionExpandedUtmChannel:
      type: string
      enum:
        - ''
        - website
        - import
        - embed
        - api
        - referral
        - recommendation
        - magic_link
        - boost
        - boost_send
        - boost_direct_link
        - integration
        - product
      description: The acquisition channel
      title: SubscriptionExpandedUtmChannel
    type_ids:TierId:
      type: string
      description: The prefixed ID of the tier.
      title: TierId
    type_:SubscriptionTierInfoStatus:
      type: string
      enum:
        - active
        - archived
      description: Returns whether or not the tier has any active prices.
      title: SubscriptionTierInfoStatus
    type_:SubscriptionTierInfo:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:TierId'
        name:
          type: string
        status:
          $ref: '#/components/schemas/type_:SubscriptionTierInfoStatus'
          description: Returns whether or not the tier has any active prices.
      required:
        - id
        - name
        - status
      title: SubscriptionTierInfo
    type_:SubscriptionTierList:
      type: array
      items:
        $ref: '#/components/schemas/type_:SubscriptionTierInfo'
      description: >-
        Optional list of tiers for a subscription. Retrievable by including
        `expand: [subscription_premium_tiers]` in the request body.
      title: SubscriptionTierList
    type_:CustomFieldType:
      type: string
      enum:
        - string
        - integer
        - boolean
        - date
        - datetime
        - list
        - double
      description: The type of value being stored in the custom field.
      title: CustomFieldType
    type_:CustomField:
      type: object
      properties:
        name:
          type: string
          description: The name of the existing custom field
        kind:
          $ref: '#/components/schemas/type_:CustomFieldType'
          description: The type of value being stored in the custom field.
        value:
          $ref: '#/components/schemas/type_:CustomFieldDataType'
          description: The value stored for the subscription
      title: CustomField
    type_:SubscriptionCustomFieldList:
      type: array
      items:
        $ref: '#/components/schemas/type_:CustomField'
      description: >-
        Optional list of custom fields for a subscription. Retrievable by
        including `expand: [custom_field]` in the request body.
      title: SubscriptionCustomFieldList
    type_:SubscriptionTags:
      type: array
      items:
        type: string
      description: >-
        Optional list of tags for a subscription. Retrievable by including
        `expand: [tags]` in the request body.

        Max limit of 100 unique tags per publication.
      title: SubscriptionTags
    type_:SubscriptionStats:
      type: object
      properties:
        emails_received:
          type: integer
          description: The total number of emails that have been sent to this subscriber
        open_rate:
          type: number
          format: double
          description: The percentage of emails that the subscriber has opened
        click_through_rate:
          type: number
          format: double
          description: The percentage of emails that the subscriber has clicked a link in
      description: >-
        Optional list of stats for a subscription. Retrievable by including
        `expand: [stats]` in the request body.
      title: SubscriptionStats
    type_:Subscription:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:SubscriptionId'
          description: The prefixed subscription id
        email:
          type: string
          format: email
        status:
          $ref: '#/components/schemas/type_:SubscriptionExpandedStatus'
          description: >-
            The status of the subscription.<br>`validating` - The email address
            is being validated.<br>`invalid` - The email address is
            invalid.<br>`pending` - The email address is valid, but the
            subscription is pending double opt-in.<br>`active` - The email was
            valid and the subscription is active.<br>`inactive` - The
            subscription was made inactive, possibly due to an
            unsubscribe.<br>`needs_attention` - The subscription requires
            approval or denial.
        created:
          type: integer
          description: >-
            The date the subscription was created. Measured in seconds since the
            Unix epoch
        subscription_tier:
          $ref: '#/components/schemas/type_:SubscriptionExpandedSubscriptionTier'
          description: The current tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: >-
            The current premium tiers of the subscription. Empty if the
            subscriber is not associated with any premium tiers.
        utm_source:
          type: string
          description: The acquisition source; where the subscriber came from
        utm_medium:
          type: string
          description: The acquisition medium; how the subscriber got to your publication
        utm_channel:
          $ref: '#/components/schemas/type_:SubscriptionExpandedUtmChannel'
          description: The acquisition channel
        utm_campaign:
          type: string
          description: The acquisition campaign
        utm_term:
          type: string
          description: The acquisition term; typically the keyword or search term
        utm_content:
          type: string
          description: >-
            The acquisition content; typically used for A/B testing or ad
            variations
        referring_site:
          type: string
          description: The website that the subscriber was referred from
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        subscription_premium_tiers:
          $ref: '#/components/schemas/type_:SubscriptionTierList'
        custom_fields:
          $ref: '#/components/schemas/type_:SubscriptionCustomFieldList'
        tags:
          $ref: '#/components/schemas/type_:SubscriptionTags'
        stats:
          $ref: '#/components/schemas/type_:SubscriptionStats'
      required:
        - id
        - email
        - status
        - created
        - subscription_tier
        - subscription_premium_tier_names
        - utm_source
        - utm_medium
        - utm_channel
        - utm_campaign
        - utm_term
        - utm_content
        - referring_site
        - referral_code
      description: The subscription object
      title: Subscription
    type_subscriptions:SubscriptionResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_:Subscription'
      required:
        - data
      description: The response containing subscription data
      title: SubscriptionResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.subscriptions.create("pub_00000000-0000-0000-0000-000000000000", {
    email: "bruce.wayne@wayneenterprise.com",
    reactivateExisting: false,
    sendWelcomeEmail: false,
    utmSource: "WayneEnterprise",
    utmMedium: "organic",
    utmCampaign: "fall_2022_promotion",
    referringSite: "www.wayneenterprise.com/blog",
    customFields: [{
            name: "First Name",
            value: "Bruce"
        }, {
            name: "Last Name",
            value: "Wayne"
        }],
    stripeCustomerId: "stripe_customer_id"
});

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions"

payload = {
    "email": "bruce.wayne@wayneenterprise.com",
    "reactivate_existing": False,
    "send_welcome_email": False,
    "utm_source": "WayneEnterprise",
    "utm_medium": "organic",
    "utm_campaign": "fall_2022_promotion",
    "referring_site": "www.wayneenterprise.com/blog",
    "custom_fields": [
        {
            "name": "First Name",
            "value": "Bruce"
        },
        {
            "name": "Last Name",
            "value": "Wayne"
        }
    ],
    "stripe_customer_id": "cus_12345abcde"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions"

	payload := strings.NewReader("{\n  \"email\": \"bruce.wayne@wayneenterprise.com\",\n  \"reactivate_existing\": false,\n  \"send_welcome_email\": false,\n  \"utm_source\": \"WayneEnterprise\",\n  \"utm_medium\": \"organic\",\n  \"utm_campaign\": \"fall_2022_promotion\",\n  \"referring_site\": \"www.wayneenterprise.com/blog\",\n  \"custom_fields\": [\n    {\n      \"name\": \"First Name\",\n      \"value\": \"Bruce\"\n    },\n    {\n      \"name\": \"Last Name\",\n      \"value\": \"Wayne\"\n    }\n  ],\n  \"stripe_customer_id\": \"cus_12345abcde\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"email\": \"bruce.wayne@wayneenterprise.com\",\n  \"reactivate_existing\": false,\n  \"send_welcome_email\": false,\n  \"utm_source\": \"WayneEnterprise\",\n  \"utm_medium\": \"organic\",\n  \"utm_campaign\": \"fall_2022_promotion\",\n  \"referring_site\": \"www.wayneenterprise.com/blog\",\n  \"custom_fields\": [\n    {\n      \"name\": \"First Name\",\n      \"value\": \"Bruce\"\n    },\n    {\n      \"name\": \"Last Name\",\n      \"value\": \"Wayne\"\n    }\n  ],\n  \"stripe_customer_id\": \"cus_12345abcde\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"email\": \"bruce.wayne@wayneenterprise.com\",\n  \"reactivate_existing\": false,\n  \"send_welcome_email\": false,\n  \"utm_source\": \"WayneEnterprise\",\n  \"utm_medium\": \"organic\",\n  \"utm_campaign\": \"fall_2022_promotion\",\n  \"referring_site\": \"www.wayneenterprise.com/blog\",\n  \"custom_fields\": [\n    {\n      \"name\": \"First Name\",\n      \"value\": \"Bruce\"\n    },\n    {\n      \"name\": \"Last Name\",\n      \"value\": \"Wayne\"\n    }\n  ],\n  \"stripe_customer_id\": \"cus_12345abcde\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions', [
  'body' => '{
  "email": "bruce.wayne@wayneenterprise.com",
  "reactivate_existing": false,
  "send_welcome_email": false,
  "utm_source": "WayneEnterprise",
  "utm_medium": "organic",
  "utm_campaign": "fall_2022_promotion",
  "referring_site": "www.wayneenterprise.com/blog",
  "custom_fields": [
    {
      "name": "First Name",
      "value": "Bruce"
    },
    {
      "name": "Last Name",
      "value": "Wayne"
    }
  ],
  "stripe_customer_id": "cus_12345abcde"
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"email\": \"bruce.wayne@wayneenterprise.com\",\n  \"reactivate_existing\": false,\n  \"send_welcome_email\": false,\n  \"utm_source\": \"WayneEnterprise\",\n  \"utm_medium\": \"organic\",\n  \"utm_campaign\": \"fall_2022_promotion\",\n  \"referring_site\": \"www.wayneenterprise.com/blog\",\n  \"custom_fields\": [\n    {\n      \"name\": \"First Name\",\n      \"value\": \"Bruce\"\n    },\n    {\n      \"name\": \"Last Name\",\n      \"value\": \"Wayne\"\n    }\n  ],\n  \"stripe_customer_id\": \"cus_12345abcde\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "email": "bruce.wayne@wayneenterprise.com",
  "reactivate_existing": false,
  "send_welcome_email": false,
  "utm_source": "WayneEnterprise",
  "utm_medium": "organic",
  "utm_campaign": "fall_2022_promotion",
  "referring_site": "www.wayneenterprise.com/blog",
  "custom_fields": [
    [
      "name": "First Name",
      "value": "Bruce"
    ],
    [
      "name": "Last Name",
      "value": "Wayne"
    ]
  ],
  "stripe_customer_id": "cus_12345abcde"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# List subscriptions <Badge intent="info" minimal outlined>OAuth Scope: subscriptions:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/subscriptions

Retrieve all subscriptions belonging to a specific publication.

<Info> **New**: This endpoint now supports cursor-based pagination for better performance and consistency. Use the `cursor` parameter instead of `page` for new integrations. </Info>
<Warning> **Deprecation Notice**: Offset-based pagination (using `page` parameter) is deprecated and limited to 100 pages maximum. Please migrate to cursor-based pagination. See our [Pagination Guide](/welcome/pagination) for details. </Warning>

Reference: https://developers.beehiiv.com/api-reference/subscriptions/index

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/subscriptions:
    get:
      operationId: index
      summary: >-
        List subscriptions <Badge intent="info" minimal outlined>OAuth Scope:
        subscriptions:read</Badge>
      description: >-
        Retrieve all subscriptions belonging to a specific publication.


        <Info> **New**: This endpoint now supports cursor-based pagination for
        better performance and consistency. Use the `cursor` parameter instead
        of `page` for new integrations. </Info>

        <Warning> **Deprecation Notice**: Offset-based pagination (using `page`
        parameter) is deprecated and limited to 100 pages maximum. Please
        migrate to cursor-based pagination. See our [Pagination
        Guide](/welcome/pagination) for details. </Warning>
      tags:
        - subpackage_subscriptions
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: expand[]
          in: query
          description: >-
            Optional list of expandable objects.<br>`subscription_premium_tiers
            ` - Returns an array of tiers the subscription is associated
            with.<br>`referrals` - Returns an array of subscriptions with
            limited data - `id`, `email`, and `status`. These are the
            subscriptions that were referred by this subscription.<br>`stats` -
            Returns statistics about the subscription(s).<br>`custom_fields` -
            Returns an array of custom field values that have been set on the
            subscription.
          required: false
          schema:
            $ref: >-
              #/components/schemas/type_subscriptions:SubscriptionsListRequestExpandItem
        - name: status
          in: query
          description: Optionally filter the results by a status
          required: false
          schema:
            $ref: >-
              #/components/schemas/type_subscriptions:SubscriptionsListRequestStatus
        - name: tier
          in: query
          description: Optionally filter the results by a their tier
          required: false
          schema:
            $ref: >-
              #/components/schemas/type_subscriptions:SubscriptionsListRequestTier
        - name: premium_tiers[]
          in: query
          description: Optionally filter the results by one or multiple premium tiers
          required: false
          schema:
            type: string
        - name: premium_tier_ids[]
          in: query
          description: Optionally filter the results by one or multiple premium tier ids
          required: false
          schema:
            type: string
        - name: limit
          in: query
          description: >-
            A limit on the number of objects to be returned. The limit can range
            between 1 and 100, and the default is 10.
          required: false
          schema:
            type: integer
        - name: cursor
          in: query
          description: >-
            **Cursor-based pagination (recommended)**: Use this opaque cursor
            token to fetch the next page of results. When provided, pagination
            will use cursor-based method which is more efficient and consistent
            than offset-based pagination. See the [Pagination
            Guide](/welcome/pagination) for more details.
          required: false
          schema:
            type: string
        - name: page
          in: query
          description: >-
            **Offset-based pagination (deprecated)**: Page number for
            offset-based pagination. This method is deprecated and limited to
            100 pages maximum. Please migrate to cursor-based pagination using
            the `cursor` parameter. If not specified, results 1-10 from page 1
            will be returned. See the [Pagination Guide](/welcome/pagination)
            for migration guidance.
          required: false
          schema:
            type: integer
        - name: email
          in: query
          description: >-
            Optional email address to find a subscription.<br>This param must be
            an exact match and is case insensitive.
          required: false
          schema:
            type: string
        - name: order_by
          in: query
          description: >-
            The field that the results are sorted by. Defaults to created<br>
            `created` - The time in which the subscription was first
            created.<br>
          required: false
          schema:
            $ref: >-
              #/components/schemas/type_subscriptions:SubscriptionsListRequestOrderBy
        - name: direction
          in: query
          description: >-
            The direction that the results are sorted in. Defaults to asc<br>
            `asc` - Ascending, sorts from smallest to largest.<br> `desc` -
            Descending, sorts from largest to smallest.
          required: false
          schema:
            $ref: '#/components/schemas/type_:RequestDirection'
        - name: creation_date
          in: query
          description: >-
            Optional date entry (in the format YYYY/MM/DD) that filters returned
            subscriptions by their creation date.
          required: false
          schema:
            type: string
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_subscriptions:SubscriptionsListResponse
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_subscriptions:SubscriptionsListRequestExpandItem:
      type: string
      enum:
        - stats
        - custom_fields
        - referrals
      title: SubscriptionsListRequestExpandItem
    type_subscriptions:SubscriptionsListRequestStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - all
      default: all
      title: SubscriptionsListRequestStatus
    type_subscriptions:SubscriptionsListRequestTier:
      type: string
      enum:
        - free
        - premium
        - all
      default: all
      title: SubscriptionsListRequestTier
    type_subscriptions:SubscriptionsListRequestOrderBy:
      type: string
      enum:
        - created
      default: created
      title: SubscriptionsListRequestOrderBy
    type_:RequestDirection:
      type: string
      enum:
        - asc
        - desc
      default: asc
      description: The direction of the request. Defaults to `asc`.
      title: RequestDirection
    type_ids:SubscriptionId:
      type: string
      description: The prefixed ID of the subscription.
      title: SubscriptionId
    type_:SubscriptionExpandedStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
        - paused
      description: >-
        The status of the subscription.<br>`validating` - The email address is
        being validated.<br>`invalid` - The email address is
        invalid.<br>`pending` - The email address is valid, but the subscription
        is pending double opt-in.<br>`active` - The email was valid and the
        subscription is active.<br>`inactive` - The subscription was made
        inactive, possibly due to an unsubscribe.<br>`needs_attention` - The
        subscription requires approval or denial.<br>`paused` - The subscriber
        has paused their subscription.
      title: SubscriptionExpandedStatus
    type_:SubscriptionExpandedSubscriptionTier:
      type: string
      enum:
        - free
        - premium
      description: The current tier of the subscription.
      title: SubscriptionExpandedSubscriptionTier
    type_:SubscriptionExpandedUtmChannel:
      type: string
      enum:
        - ''
        - website
        - import
        - embed
        - api
        - referral
        - recommendation
        - magic_link
        - boost
        - boost_send
        - boost_direct_link
        - integration
        - product
      description: The acquisition channel
      title: SubscriptionExpandedUtmChannel
    type_ids:TierId:
      type: string
      description: The prefixed ID of the tier.
      title: TierId
    type_:SubscriptionTierInfoStatus:
      type: string
      enum:
        - active
        - archived
      description: Returns whether or not the tier has any active prices.
      title: SubscriptionTierInfoStatus
    type_:SubscriptionTierInfo:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:TierId'
        name:
          type: string
        status:
          $ref: '#/components/schemas/type_:SubscriptionTierInfoStatus'
          description: Returns whether or not the tier has any active prices.
      required:
        - id
        - name
        - status
      title: SubscriptionTierInfo
    type_:SubscriptionTierList:
      type: array
      items:
        $ref: '#/components/schemas/type_:SubscriptionTierInfo'
      description: >-
        Optional list of tiers for a subscription. Retrievable by including
        `expand: [subscription_premium_tiers]` in the request body.
      title: SubscriptionTierList
    type_:CustomFieldType:
      type: string
      enum:
        - string
        - integer
        - boolean
        - date
        - datetime
        - list
        - double
      description: The type of value being stored in the custom field.
      title: CustomFieldType
    type_:CustomFieldDataType:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: boolean
        - type: array
          items:
            type: string
      title: CustomFieldDataType
    type_:CustomField:
      type: object
      properties:
        name:
          type: string
          description: The name of the existing custom field
        kind:
          $ref: '#/components/schemas/type_:CustomFieldType'
          description: The type of value being stored in the custom field.
        value:
          $ref: '#/components/schemas/type_:CustomFieldDataType'
          description: The value stored for the subscription
      title: CustomField
    type_:SubscriptionCustomFieldList:
      type: array
      items:
        $ref: '#/components/schemas/type_:CustomField'
      description: >-
        Optional list of custom fields for a subscription. Retrievable by
        including `expand: [custom_field]` in the request body.
      title: SubscriptionCustomFieldList
    type_:SubscriptionTags:
      type: array
      items:
        type: string
      description: >-
        Optional list of tags for a subscription. Retrievable by including
        `expand: [tags]` in the request body.

        Max limit of 100 unique tags per publication.
      title: SubscriptionTags
    type_:SubscriptionStats:
      type: object
      properties:
        emails_received:
          type: integer
          description: The total number of emails that have been sent to this subscriber
        open_rate:
          type: number
          format: double
          description: The percentage of emails that the subscriber has opened
        click_through_rate:
          type: number
          format: double
          description: The percentage of emails that the subscriber has clicked a link in
      description: >-
        Optional list of stats for a subscription. Retrievable by including
        `expand: [stats]` in the request body.
      title: SubscriptionStats
    type_:Subscription:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:SubscriptionId'
          description: The prefixed subscription id
        email:
          type: string
          format: email
        status:
          $ref: '#/components/schemas/type_:SubscriptionExpandedStatus'
          description: >-
            The status of the subscription.<br>`validating` - The email address
            is being validated.<br>`invalid` - The email address is
            invalid.<br>`pending` - The email address is valid, but the
            subscription is pending double opt-in.<br>`active` - The email was
            valid and the subscription is active.<br>`inactive` - The
            subscription was made inactive, possibly due to an
            unsubscribe.<br>`needs_attention` - The subscription requires
            approval or denial.
        created:
          type: integer
          description: >-
            The date the subscription was created. Measured in seconds since the
            Unix epoch
        subscription_tier:
          $ref: '#/components/schemas/type_:SubscriptionExpandedSubscriptionTier'
          description: The current tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: >-
            The current premium tiers of the subscription. Empty if the
            subscriber is not associated with any premium tiers.
        utm_source:
          type: string
          description: The acquisition source; where the subscriber came from
        utm_medium:
          type: string
          description: The acquisition medium; how the subscriber got to your publication
        utm_channel:
          $ref: '#/components/schemas/type_:SubscriptionExpandedUtmChannel'
          description: The acquisition channel
        utm_campaign:
          type: string
          description: The acquisition campaign
        utm_term:
          type: string
          description: The acquisition term; typically the keyword or search term
        utm_content:
          type: string
          description: >-
            The acquisition content; typically used for A/B testing or ad
            variations
        referring_site:
          type: string
          description: The website that the subscriber was referred from
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        subscription_premium_tiers:
          $ref: '#/components/schemas/type_:SubscriptionTierList'
        custom_fields:
          $ref: '#/components/schemas/type_:SubscriptionCustomFieldList'
        tags:
          $ref: '#/components/schemas/type_:SubscriptionTags'
        stats:
          $ref: '#/components/schemas/type_:SubscriptionStats'
      required:
        - id
        - email
        - status
        - created
        - subscription_tier
        - subscription_premium_tier_names
        - utm_source
        - utm_medium
        - utm_channel
        - utm_campaign
        - utm_term
        - utm_content
        - referring_site
        - referral_code
      description: The subscription object
      title: Subscription
    type_subscriptions:SubscriptionsListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/type_:Subscription'
        limit:
          type: integer
          description: >-
            The limit placed on the results. If no limit was specified in the
            request, this defaults to 10.
        page:
          type: integer
          default: 1
          description: >-
            **Offset pagination only**: The page number the results are from.
            Only present when using deprecated offset-based pagination.
        total_pages:
          type: integer
          description: >-
            **Offset pagination only**: The total number of pages. Only present
            when using deprecated offset-based pagination.
        has_more:
          type: boolean
          description: >-
            **Cursor pagination only**: Indicates whether there are more results
            available after the current page. Only present when using
            cursor-based pagination.
        next_cursor:
          type: string
          description: >-
            **Cursor pagination only**: The cursor token to use for fetching the
            next page of results. This will be null if has_more is false. Only
            present when using cursor-based pagination.
        total_results:
          type: integer
          description: >-
            **Mixed pagination**: The total number of results from all pages.
            For offset-based pagination, this is always included.
      required:
        - data
      title: SubscriptionsListResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript Cursor-based pagination (recommended)
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.subscriptions.list("pub_00000000-0000-0000-0000-000000000000", {
    email: "clark@dailyplanet.com"
});

```

```python Cursor-based pagination (recommended)
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions"

querystring = {"limit":"10"}

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

```go Cursor-based pagination (recommended)
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions?limit=10"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Cursor-based pagination (recommended)
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions?limit=10")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java Cursor-based pagination (recommended)
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions?limit=10")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php Cursor-based pagination (recommended)
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions?limit=10', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp Cursor-based pagination (recommended)
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions?limit=10");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift Cursor-based pagination (recommended)
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions?limit=10")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

```typescript Cursor-based pagination (next page)
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.subscriptions.list("pub_00000000-0000-0000-0000-000000000000", {
    email: "clark@dailyplanet.com"
});

```

```python Cursor-based pagination (next page)
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions"

querystring = {"limit":"10","cursor":"eyJ0aW1lc3RhbXAiOiIyMDI0LTA3LTAyVDE3OjMwOjAwLjAwMDAwMFoifQ=="}

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

```go Cursor-based pagination (next page)
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions?limit=10&cursor=eyJ0aW1lc3RhbXAiOiIyMDI0LTA3LTAyVDE3OjMwOjAwLjAwMDAwMFoifQ%3D%3D"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Cursor-based pagination (next page)
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions?limit=10&cursor=eyJ0aW1lc3RhbXAiOiIyMDI0LTA3LTAyVDE3OjMwOjAwLjAwMDAwMFoifQ%3D%3D")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java Cursor-based pagination (next page)
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions?limit=10&cursor=eyJ0aW1lc3RhbXAiOiIyMDI0LTA3LTAyVDE3OjMwOjAwLjAwMDAwMFoifQ%3D%3D")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php Cursor-based pagination (next page)
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions?limit=10&cursor=eyJ0aW1lc3RhbXAiOiIyMDI0LTA3LTAyVDE3OjMwOjAwLjAwMDAwMFoifQ%3D%3D', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp Cursor-based pagination (next page)
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions?limit=10&cursor=eyJ0aW1lc3RhbXAiOiIyMDI0LTA3LTAyVDE3OjMwOjAwLjAwMDAwMFoifQ%3D%3D");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift Cursor-based pagination (next page)
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions?limit=10&cursor=eyJ0aW1lc3RhbXAiOiIyMDI0LTA3LTAyVDE3OjMwOjAwLjAwMDAwMFoifQ%3D%3D")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

```typescript Offset-based pagination (deprecated)
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.subscriptions.list("pub_00000000-0000-0000-0000-000000000000", {
    email: "clark@dailyplanet.com"
});

```

```python Offset-based pagination (deprecated)
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions"

querystring = {"email":"clark@dailyplanet.com","page":"1","limit":"10"}

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

```go Offset-based pagination (deprecated)
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions?email=clark%40dailyplanet.com&page=1&limit=10"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Offset-based pagination (deprecated)
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions?email=clark%40dailyplanet.com&page=1&limit=10")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java Offset-based pagination (deprecated)
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions?email=clark%40dailyplanet.com&page=1&limit=10")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php Offset-based pagination (deprecated)
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions?email=clark%40dailyplanet.com&page=1&limit=10', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp Offset-based pagination (deprecated)
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions?email=clark%40dailyplanet.com&page=1&limit=10");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift Offset-based pagination (deprecated)
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions?email=clark%40dailyplanet.com&page=1&limit=10")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get subscription by email <Badge intent="info" minimal outlined>OAuth Scope: subscriptions:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/subscriptions/by_email/{email}

<Info>Please note that this endpoint requires the email to be URL encoded. Please reference your language's documentation for the correct method of encoding.</Info> Retrieve a single subscription belonging to a specific email address in a specific publication.

Reference: https://developers.beehiiv.com/api-reference/subscriptions/get-by-email

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/subscriptions/by_email/{email}:
    get:
      operationId: get-by-email
      summary: >-
        Get subscription by email <Badge intent="info" minimal outlined>OAuth
        Scope: subscriptions:read</Badge>
      description: >-
        <Info>Please note that this endpoint requires the email to be URL
        encoded. Please reference your language's documentation for the correct
        method of encoding.</Info> Retrieve a single subscription belonging to a
        specific email address in a specific publication.
      tags:
        - subpackage_subscriptions
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: email
          in: path
          description: The ID of the subscriber object
          required: true
          schema:
            type: string
        - name: expand[]
          in: query
          description: >-
            Optional list of expandable objects.<br>`subscription_premium_tiers
            ` - Returns an array of tiers the subscription is associated
            with.<br>`referrals` - Returns an array of subscriptions with
            limited data - `id`, `email`, and `status`. These are the
            subscriptions that were referred by this subscription.<br>`stats` -
            Returns statistics about the subscription(s).<br>`custom_fields` -
            Returns an array of custom field values that have been set on the
            subscription. <br>`tags` - Returns an array of tags that have been
            set on the subscription.
          required: false
          schema:
            $ref: >-
              #/components/schemas/type_subscriptions:SubscriptionsGetRequestExpandItem
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_subscriptions:SubscriptionResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_subscriptions:SubscriptionsGetRequestExpandItem:
      type: string
      enum:
        - stats
        - custom_fields
        - referrals
        - tags
      title: SubscriptionsGetRequestExpandItem
    type_ids:SubscriptionId:
      type: string
      description: The prefixed ID of the subscription.
      title: SubscriptionId
    type_:SubscriptionExpandedStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
        - paused
      description: >-
        The status of the subscription.<br>`validating` - The email address is
        being validated.<br>`invalid` - The email address is
        invalid.<br>`pending` - The email address is valid, but the subscription
        is pending double opt-in.<br>`active` - The email was valid and the
        subscription is active.<br>`inactive` - The subscription was made
        inactive, possibly due to an unsubscribe.<br>`needs_attention` - The
        subscription requires approval or denial.<br>`paused` - The subscriber
        has paused their subscription.
      title: SubscriptionExpandedStatus
    type_:SubscriptionExpandedSubscriptionTier:
      type: string
      enum:
        - free
        - premium
      description: The current tier of the subscription.
      title: SubscriptionExpandedSubscriptionTier
    type_:SubscriptionExpandedUtmChannel:
      type: string
      enum:
        - ''
        - website
        - import
        - embed
        - api
        - referral
        - recommendation
        - magic_link
        - boost
        - boost_send
        - boost_direct_link
        - integration
        - product
      description: The acquisition channel
      title: SubscriptionExpandedUtmChannel
    type_ids:TierId:
      type: string
      description: The prefixed ID of the tier.
      title: TierId
    type_:SubscriptionTierInfoStatus:
      type: string
      enum:
        - active
        - archived
      description: Returns whether or not the tier has any active prices.
      title: SubscriptionTierInfoStatus
    type_:SubscriptionTierInfo:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:TierId'
        name:
          type: string
        status:
          $ref: '#/components/schemas/type_:SubscriptionTierInfoStatus'
          description: Returns whether or not the tier has any active prices.
      required:
        - id
        - name
        - status
      title: SubscriptionTierInfo
    type_:SubscriptionTierList:
      type: array
      items:
        $ref: '#/components/schemas/type_:SubscriptionTierInfo'
      description: >-
        Optional list of tiers for a subscription. Retrievable by including
        `expand: [subscription_premium_tiers]` in the request body.
      title: SubscriptionTierList
    type_:CustomFieldType:
      type: string
      enum:
        - string
        - integer
        - boolean
        - date
        - datetime
        - list
        - double
      description: The type of value being stored in the custom field.
      title: CustomFieldType
    type_:CustomFieldDataType:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: boolean
        - type: array
          items:
            type: string
      title: CustomFieldDataType
    type_:CustomField:
      type: object
      properties:
        name:
          type: string
          description: The name of the existing custom field
        kind:
          $ref: '#/components/schemas/type_:CustomFieldType'
          description: The type of value being stored in the custom field.
        value:
          $ref: '#/components/schemas/type_:CustomFieldDataType'
          description: The value stored for the subscription
      title: CustomField
    type_:SubscriptionCustomFieldList:
      type: array
      items:
        $ref: '#/components/schemas/type_:CustomField'
      description: >-
        Optional list of custom fields for a subscription. Retrievable by
        including `expand: [custom_field]` in the request body.
      title: SubscriptionCustomFieldList
    type_:SubscriptionTags:
      type: array
      items:
        type: string
      description: >-
        Optional list of tags for a subscription. Retrievable by including
        `expand: [tags]` in the request body.

        Max limit of 100 unique tags per publication.
      title: SubscriptionTags
    type_:SubscriptionStats:
      type: object
      properties:
        emails_received:
          type: integer
          description: The total number of emails that have been sent to this subscriber
        open_rate:
          type: number
          format: double
          description: The percentage of emails that the subscriber has opened
        click_through_rate:
          type: number
          format: double
          description: The percentage of emails that the subscriber has clicked a link in
      description: >-
        Optional list of stats for a subscription. Retrievable by including
        `expand: [stats]` in the request body.
      title: SubscriptionStats
    type_:Subscription:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:SubscriptionId'
          description: The prefixed subscription id
        email:
          type: string
          format: email
        status:
          $ref: '#/components/schemas/type_:SubscriptionExpandedStatus'
          description: >-
            The status of the subscription.<br>`validating` - The email address
            is being validated.<br>`invalid` - The email address is
            invalid.<br>`pending` - The email address is valid, but the
            subscription is pending double opt-in.<br>`active` - The email was
            valid and the subscription is active.<br>`inactive` - The
            subscription was made inactive, possibly due to an
            unsubscribe.<br>`needs_attention` - The subscription requires
            approval or denial.
        created:
          type: integer
          description: >-
            The date the subscription was created. Measured in seconds since the
            Unix epoch
        subscription_tier:
          $ref: '#/components/schemas/type_:SubscriptionExpandedSubscriptionTier'
          description: The current tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: >-
            The current premium tiers of the subscription. Empty if the
            subscriber is not associated with any premium tiers.
        utm_source:
          type: string
          description: The acquisition source; where the subscriber came from
        utm_medium:
          type: string
          description: The acquisition medium; how the subscriber got to your publication
        utm_channel:
          $ref: '#/components/schemas/type_:SubscriptionExpandedUtmChannel'
          description: The acquisition channel
        utm_campaign:
          type: string
          description: The acquisition campaign
        utm_term:
          type: string
          description: The acquisition term; typically the keyword or search term
        utm_content:
          type: string
          description: >-
            The acquisition content; typically used for A/B testing or ad
            variations
        referring_site:
          type: string
          description: The website that the subscriber was referred from
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        subscription_premium_tiers:
          $ref: '#/components/schemas/type_:SubscriptionTierList'
        custom_fields:
          $ref: '#/components/schemas/type_:SubscriptionCustomFieldList'
        tags:
          $ref: '#/components/schemas/type_:SubscriptionTags'
        stats:
          $ref: '#/components/schemas/type_:SubscriptionStats'
      required:
        - id
        - email
        - status
        - created
        - subscription_tier
        - subscription_premium_tier_names
        - utm_source
        - utm_medium
        - utm_channel
        - utm_campaign
        - utm_term
        - utm_content
        - referring_site
        - referral_code
      description: The subscription object
      title: Subscription
    type_subscriptions:SubscriptionResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_:Subscription'
      required:
        - data
      description: The response containing subscription data
      title: SubscriptionResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.subscriptions.get("pub_00000000-0000-0000-0000-000000000000", "work@example.com");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/by_email/work%40example.com"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/by_email/work%40example.com"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/by_email/work%40example.com")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/by_email/work%40example.com")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/by_email/work%40example.com', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/by_email/work%40example.com");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/by_email/work%40example.com")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get subscription by ID <Badge intent="info" minimal outlined>OAuth Scope: subscriptions:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/subscriptions/{subscriptionId}

<Info>In previous versions of the API, another endpoint existed to retrieve a subscription by the subscriber ID. This endpoint is now deprecated and will be removed in a future version of the API. Please use this endpoint instead. The subscription ID can be found by exporting a list of subscriptions either via the `Settings > Publications > Export Data` or by exporting a CSV in a segment.</Info> Retrieve a single subscription belonging to a specific publication.

Reference: https://developers.beehiiv.com/api-reference/subscriptions/get-by-id

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/subscriptions/{subscriptionId}:
    get:
      operationId: get-by-id
      summary: >-
        Get subscription by ID <Badge intent="info" minimal outlined>OAuth
        Scope: subscriptions:read</Badge>
      description: >-
        <Info>In previous versions of the API, another endpoint existed to
        retrieve a subscription by the subscriber ID. This endpoint is now
        deprecated and will be removed in a future version of the API. Please
        use this endpoint instead. The subscription ID can be found by exporting
        a list of subscriptions either via the `Settings > Publications > Export
        Data` or by exporting a CSV in a segment.</Info> Retrieve a single
        subscription belonging to a specific publication.
      tags:
        - subpackage_subscriptions
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: subscriptionId
          in: path
          description: The prefixed ID of the subscription object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:SubscriptionId'
        - name: expand[]
          in: query
          description: >-
            Optional list of expandable objects.<br>`subscription_premium_tiers`
            - Returns an array of tiers the subscription is associated
            with.<br>`referrals` - Returns an array of subscriptions with
            limited data - `id`, `email`, and `status`. These are the
            subscriptions that were referred by this subscription.<br>`stats` -
            Returns statistics about the subscription(s).<br>`custom_fields` -
            Returns an array of custom field values that have been set on the
            subscription. <br>`tags` - Returns an array of tags that have been
            set on the subscription.
          required: false
          schema:
            $ref: >-
              #/components/schemas/type_subscriptions:SubscriptionsGetRequestExpandItem
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_subscriptions:SubscriptionResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:SubscriptionId:
      type: string
      description: The prefixed ID of the subscription.
      title: SubscriptionId
    type_subscriptions:SubscriptionsGetRequestExpandItem:
      type: string
      enum:
        - stats
        - custom_fields
        - referrals
        - tags
      title: SubscriptionsGetRequestExpandItem
    type_:SubscriptionExpandedStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
        - paused
      description: >-
        The status of the subscription.<br>`validating` - The email address is
        being validated.<br>`invalid` - The email address is
        invalid.<br>`pending` - The email address is valid, but the subscription
        is pending double opt-in.<br>`active` - The email was valid and the
        subscription is active.<br>`inactive` - The subscription was made
        inactive, possibly due to an unsubscribe.<br>`needs_attention` - The
        subscription requires approval or denial.<br>`paused` - The subscriber
        has paused their subscription.
      title: SubscriptionExpandedStatus
    type_:SubscriptionExpandedSubscriptionTier:
      type: string
      enum:
        - free
        - premium
      description: The current tier of the subscription.
      title: SubscriptionExpandedSubscriptionTier
    type_:SubscriptionExpandedUtmChannel:
      type: string
      enum:
        - ''
        - website
        - import
        - embed
        - api
        - referral
        - recommendation
        - magic_link
        - boost
        - boost_send
        - boost_direct_link
        - integration
        - product
      description: The acquisition channel
      title: SubscriptionExpandedUtmChannel
    type_ids:TierId:
      type: string
      description: The prefixed ID of the tier.
      title: TierId
    type_:SubscriptionTierInfoStatus:
      type: string
      enum:
        - active
        - archived
      description: Returns whether or not the tier has any active prices.
      title: SubscriptionTierInfoStatus
    type_:SubscriptionTierInfo:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:TierId'
        name:
          type: string
        status:
          $ref: '#/components/schemas/type_:SubscriptionTierInfoStatus'
          description: Returns whether or not the tier has any active prices.
      required:
        - id
        - name
        - status
      title: SubscriptionTierInfo
    type_:SubscriptionTierList:
      type: array
      items:
        $ref: '#/components/schemas/type_:SubscriptionTierInfo'
      description: >-
        Optional list of tiers for a subscription. Retrievable by including
        `expand: [subscription_premium_tiers]` in the request body.
      title: SubscriptionTierList
    type_:CustomFieldType:
      type: string
      enum:
        - string
        - integer
        - boolean
        - date
        - datetime
        - list
        - double
      description: The type of value being stored in the custom field.
      title: CustomFieldType
    type_:CustomFieldDataType:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: boolean
        - type: array
          items:
            type: string
      title: CustomFieldDataType
    type_:CustomField:
      type: object
      properties:
        name:
          type: string
          description: The name of the existing custom field
        kind:
          $ref: '#/components/schemas/type_:CustomFieldType'
          description: The type of value being stored in the custom field.
        value:
          $ref: '#/components/schemas/type_:CustomFieldDataType'
          description: The value stored for the subscription
      title: CustomField
    type_:SubscriptionCustomFieldList:
      type: array
      items:
        $ref: '#/components/schemas/type_:CustomField'
      description: >-
        Optional list of custom fields for a subscription. Retrievable by
        including `expand: [custom_field]` in the request body.
      title: SubscriptionCustomFieldList
    type_:SubscriptionTags:
      type: array
      items:
        type: string
      description: >-
        Optional list of tags for a subscription. Retrievable by including
        `expand: [tags]` in the request body.

        Max limit of 100 unique tags per publication.
      title: SubscriptionTags
    type_:SubscriptionStats:
      type: object
      properties:
        emails_received:
          type: integer
          description: The total number of emails that have been sent to this subscriber
        open_rate:
          type: number
          format: double
          description: The percentage of emails that the subscriber has opened
        click_through_rate:
          type: number
          format: double
          description: The percentage of emails that the subscriber has clicked a link in
      description: >-
        Optional list of stats for a subscription. Retrievable by including
        `expand: [stats]` in the request body.
      title: SubscriptionStats
    type_:Subscription:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:SubscriptionId'
          description: The prefixed subscription id
        email:
          type: string
          format: email
        status:
          $ref: '#/components/schemas/type_:SubscriptionExpandedStatus'
          description: >-
            The status of the subscription.<br>`validating` - The email address
            is being validated.<br>`invalid` - The email address is
            invalid.<br>`pending` - The email address is valid, but the
            subscription is pending double opt-in.<br>`active` - The email was
            valid and the subscription is active.<br>`inactive` - The
            subscription was made inactive, possibly due to an
            unsubscribe.<br>`needs_attention` - The subscription requires
            approval or denial.
        created:
          type: integer
          description: >-
            The date the subscription was created. Measured in seconds since the
            Unix epoch
        subscription_tier:
          $ref: '#/components/schemas/type_:SubscriptionExpandedSubscriptionTier'
          description: The current tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: >-
            The current premium tiers of the subscription. Empty if the
            subscriber is not associated with any premium tiers.
        utm_source:
          type: string
          description: The acquisition source; where the subscriber came from
        utm_medium:
          type: string
          description: The acquisition medium; how the subscriber got to your publication
        utm_channel:
          $ref: '#/components/schemas/type_:SubscriptionExpandedUtmChannel'
          description: The acquisition channel
        utm_campaign:
          type: string
          description: The acquisition campaign
        utm_term:
          type: string
          description: The acquisition term; typically the keyword or search term
        utm_content:
          type: string
          description: >-
            The acquisition content; typically used for A/B testing or ad
            variations
        referring_site:
          type: string
          description: The website that the subscriber was referred from
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        subscription_premium_tiers:
          $ref: '#/components/schemas/type_:SubscriptionTierList'
        custom_fields:
          $ref: '#/components/schemas/type_:SubscriptionCustomFieldList'
        tags:
          $ref: '#/components/schemas/type_:SubscriptionTags'
        stats:
          $ref: '#/components/schemas/type_:SubscriptionStats'
      required:
        - id
        - email
        - status
        - created
        - subscription_tier
        - subscription_premium_tier_names
        - utm_source
        - utm_medium
        - utm_channel
        - utm_campaign
        - utm_term
        - utm_content
        - referring_site
        - referral_code
      description: The subscription object
      title: Subscription
    type_subscriptions:SubscriptionResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_:Subscription'
      required:
        - data
      description: The response containing subscription data
      title: SubscriptionResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Update subscription by ID <Badge intent="info" minimal outlined>OAuth Scope: subscriptions:write</Badge>

PUT https://api.beehiiv.com/v2/publications/{publicationId}/subscriptions/{subscriptionId}
Content-Type: application/json

Update a single subscription.

Reference: https://developers.beehiiv.com/api-reference/subscriptions/put

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/subscriptions/{subscriptionId}:
    put:
      operationId: put
      summary: >-
        Update subscription by ID <Badge intent="info" minimal outlined>OAuth
        Scope: subscriptions:write</Badge>
      description: Update a single subscription.
      tags:
        - subpackage_subscriptions
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: subscriptionId
          in: path
          description: The prefixed ID of the subscription object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:SubscriptionId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_subscriptions:SubscriptionResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                tier:
                  $ref: >-
                    #/components/schemas/type_bulkSubscriptionUpdates:SubscriptionsPutRequestSubscriptionsItemTier
                  description: Optional parameter to set the tier for this subscription.
                premium_tier_ids:
                  type: array
                  items:
                    type: string
                  description: >-
                    An array of premium tier IDs to assign to this subscription.
                    When provided, the subscription will be assigned to these
                    specific premium tiers. Can be combined with `premium_tiers`
                    to include tiers from both (duplicates are removed). Takes
                    precedence over the `tier` parameter.
                premium_tiers:
                  type: array
                  items:
                    type: string
                  description: >-
                    An array of premium tier names to assign to this
                    subscription. When provided, the subscription will be
                    assigned to premium tiers matching these names. Can be
                    combined with `premium_tier_ids` to include tiers from both
                    (duplicates are removed). Takes precedence over the `tier`
                    parameter.
                email:
                  type: string
                  description: The new email address for the subscription
                stripe_customer_id:
                  $ref: '#/components/schemas/type_ids:OptionalStripeCustomerId'
                  description: The Stripe Customer ID of the subscription (not required)
                unsubscribe:
                  type: boolean
                  description: >-
                    A boolean value specifying whether to unsubscribe this
                    subscription from the publication (not required)
                custom_fields:
                  type: array
                  items:
                    $ref: >-
                      #/components/schemas/type_bulkSubscriptionUpdates:SubscriptionsPutRequestSubscriptionsItemCustomFieldsItem
                  description: An array of custom field objects to update
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:SubscriptionId:
      type: string
      description: The prefixed ID of the subscription.
      title: SubscriptionId
    type_bulkSubscriptionUpdates:SubscriptionsPutRequestSubscriptionsItemTier:
      type: string
      enum:
        - free
        - premium
      description: The Tier of the Subscription (not required)
      title: SubscriptionsPutRequestSubscriptionsItemTier
    type_ids:OptionalStripeCustomerId:
      type: string
      description: The prefixed ID of the Stripe customer.
      title: OptionalStripeCustomerId
    type_:CustomFieldDataType:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: boolean
        - type: array
          items:
            type: string
      title: CustomFieldDataType
    type_bulkSubscriptionUpdates:SubscriptionsPutRequestSubscriptionsItemCustomFieldsItem:
      type: object
      properties:
        name:
          type: string
          description: The name of the existing custom field
        value:
          $ref: '#/components/schemas/type_:CustomFieldDataType'
          description: The value of the custom field
        delete:
          type: boolean
          description: >-
            A boolean value to specify whether to delete this custom field entry
            from the subscription
      title: SubscriptionsPutRequestSubscriptionsItemCustomFieldsItem
    type_:SubscriptionExpandedStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
        - paused
      description: >-
        The status of the subscription.<br>`validating` - The email address is
        being validated.<br>`invalid` - The email address is
        invalid.<br>`pending` - The email address is valid, but the subscription
        is pending double opt-in.<br>`active` - The email was valid and the
        subscription is active.<br>`inactive` - The subscription was made
        inactive, possibly due to an unsubscribe.<br>`needs_attention` - The
        subscription requires approval or denial.<br>`paused` - The subscriber
        has paused their subscription.
      title: SubscriptionExpandedStatus
    type_:SubscriptionExpandedSubscriptionTier:
      type: string
      enum:
        - free
        - premium
      description: The current tier of the subscription.
      title: SubscriptionExpandedSubscriptionTier
    type_:SubscriptionExpandedUtmChannel:
      type: string
      enum:
        - ''
        - website
        - import
        - embed
        - api
        - referral
        - recommendation
        - magic_link
        - boost
        - boost_send
        - boost_direct_link
        - integration
        - product
      description: The acquisition channel
      title: SubscriptionExpandedUtmChannel
    type_ids:TierId:
      type: string
      description: The prefixed ID of the tier.
      title: TierId
    type_:SubscriptionTierInfoStatus:
      type: string
      enum:
        - active
        - archived
      description: Returns whether or not the tier has any active prices.
      title: SubscriptionTierInfoStatus
    type_:SubscriptionTierInfo:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:TierId'
        name:
          type: string
        status:
          $ref: '#/components/schemas/type_:SubscriptionTierInfoStatus'
          description: Returns whether or not the tier has any active prices.
      required:
        - id
        - name
        - status
      title: SubscriptionTierInfo
    type_:SubscriptionTierList:
      type: array
      items:
        $ref: '#/components/schemas/type_:SubscriptionTierInfo'
      description: >-
        Optional list of tiers for a subscription. Retrievable by including
        `expand: [subscription_premium_tiers]` in the request body.
      title: SubscriptionTierList
    type_:CustomFieldType:
      type: string
      enum:
        - string
        - integer
        - boolean
        - date
        - datetime
        - list
        - double
      description: The type of value being stored in the custom field.
      title: CustomFieldType
    type_:CustomField:
      type: object
      properties:
        name:
          type: string
          description: The name of the existing custom field
        kind:
          $ref: '#/components/schemas/type_:CustomFieldType'
          description: The type of value being stored in the custom field.
        value:
          $ref: '#/components/schemas/type_:CustomFieldDataType'
          description: The value stored for the subscription
      title: CustomField
    type_:SubscriptionCustomFieldList:
      type: array
      items:
        $ref: '#/components/schemas/type_:CustomField'
      description: >-
        Optional list of custom fields for a subscription. Retrievable by
        including `expand: [custom_field]` in the request body.
      title: SubscriptionCustomFieldList
    type_:SubscriptionTags:
      type: array
      items:
        type: string
      description: >-
        Optional list of tags for a subscription. Retrievable by including
        `expand: [tags]` in the request body.

        Max limit of 100 unique tags per publication.
      title: SubscriptionTags
    type_:SubscriptionStats:
      type: object
      properties:
        emails_received:
          type: integer
          description: The total number of emails that have been sent to this subscriber
        open_rate:
          type: number
          format: double
          description: The percentage of emails that the subscriber has opened
        click_through_rate:
          type: number
          format: double
          description: The percentage of emails that the subscriber has clicked a link in
      description: >-
        Optional list of stats for a subscription. Retrievable by including
        `expand: [stats]` in the request body.
      title: SubscriptionStats
    type_:Subscription:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:SubscriptionId'
          description: The prefixed subscription id
        email:
          type: string
          format: email
        status:
          $ref: '#/components/schemas/type_:SubscriptionExpandedStatus'
          description: >-
            The status of the subscription.<br>`validating` - The email address
            is being validated.<br>`invalid` - The email address is
            invalid.<br>`pending` - The email address is valid, but the
            subscription is pending double opt-in.<br>`active` - The email was
            valid and the subscription is active.<br>`inactive` - The
            subscription was made inactive, possibly due to an
            unsubscribe.<br>`needs_attention` - The subscription requires
            approval or denial.
        created:
          type: integer
          description: >-
            The date the subscription was created. Measured in seconds since the
            Unix epoch
        subscription_tier:
          $ref: '#/components/schemas/type_:SubscriptionExpandedSubscriptionTier'
          description: The current tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: >-
            The current premium tiers of the subscription. Empty if the
            subscriber is not associated with any premium tiers.
        utm_source:
          type: string
          description: The acquisition source; where the subscriber came from
        utm_medium:
          type: string
          description: The acquisition medium; how the subscriber got to your publication
        utm_channel:
          $ref: '#/components/schemas/type_:SubscriptionExpandedUtmChannel'
          description: The acquisition channel
        utm_campaign:
          type: string
          description: The acquisition campaign
        utm_term:
          type: string
          description: The acquisition term; typically the keyword or search term
        utm_content:
          type: string
          description: >-
            The acquisition content; typically used for A/B testing or ad
            variations
        referring_site:
          type: string
          description: The website that the subscriber was referred from
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        subscription_premium_tiers:
          $ref: '#/components/schemas/type_:SubscriptionTierList'
        custom_fields:
          $ref: '#/components/schemas/type_:SubscriptionCustomFieldList'
        tags:
          $ref: '#/components/schemas/type_:SubscriptionTags'
        stats:
          $ref: '#/components/schemas/type_:SubscriptionStats'
      required:
        - id
        - email
        - status
        - created
        - subscription_tier
        - subscription_premium_tier_names
        - utm_source
        - utm_medium
        - utm_channel
        - utm_campaign
        - utm_term
        - utm_content
        - referring_site
        - referral_code
      description: The subscription object
      title: Subscription
    type_subscriptions:SubscriptionResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_:Subscription'
      required:
        - data
      description: The response containing subscription data
      title: SubscriptionResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.subscriptions.put("publicationId");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000"

payload = {
    "tier": "premium",
    "email": "newemail@example.com",
    "stripe_customer_id": "cus_12345abcde",
    "custom_fields": [
        {
            "name": "First Name",
            "value": "Bruce"
        },
        {
            "name": "Last Name",
            "value": "Wayne"
        }
    ]
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000"

	payload := strings.NewReader("{\n  \"tier\": \"premium\",\n  \"email\": \"newemail@example.com\",\n  \"stripe_customer_id\": \"cus_12345abcde\",\n  \"custom_fields\": [\n    {\n      \"name\": \"First Name\",\n      \"value\": \"Bruce\"\n    },\n    {\n      \"name\": \"Last Name\",\n      \"value\": \"Wayne\"\n    }\n  ]\n}")

	req, _ := http.NewRequest("PUT", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"tier\": \"premium\",\n  \"email\": \"newemail@example.com\",\n  \"stripe_customer_id\": \"cus_12345abcde\",\n  \"custom_fields\": [\n    {\n      \"name\": \"First Name\",\n      \"value\": \"Bruce\"\n    },\n    {\n      \"name\": \"Last Name\",\n      \"value\": \"Wayne\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"tier\": \"premium\",\n  \"email\": \"newemail@example.com\",\n  \"stripe_customer_id\": \"cus_12345abcde\",\n  \"custom_fields\": [\n    {\n      \"name\": \"First Name\",\n      \"value\": \"Bruce\"\n    },\n    {\n      \"name\": \"Last Name\",\n      \"value\": \"Wayne\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000', [
  'body' => '{
  "tier": "premium",
  "email": "newemail@example.com",
  "stripe_customer_id": "cus_12345abcde",
  "custom_fields": [
    {
      "name": "First Name",
      "value": "Bruce"
    },
    {
      "name": "Last Name",
      "value": "Wayne"
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000");
var request = new RestRequest(Method.PUT);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"tier\": \"premium\",\n  \"email\": \"newemail@example.com\",\n  \"stripe_customer_id\": \"cus_12345abcde\",\n  \"custom_fields\": [\n    {\n      \"name\": \"First Name\",\n      \"value\": \"Bruce\"\n    },\n    {\n      \"name\": \"Last Name\",\n      \"value\": \"Wayne\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "tier": "premium",
  "email": "newemail@example.com",
  "stripe_customer_id": "cus_12345abcde",
  "custom_fields": [
    [
      "name": "First Name",
      "value": "Bruce"
    ],
    [
      "name": "Last Name",
      "value": "Wayne"
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PUT"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Update subscription by email <Badge intent="info" minimal outlined>OAuth Scope: subscriptions:write</Badge>

PUT https://api.beehiiv.com/v2/publications/{publicationId}/subscriptions/by_email/{email}
Content-Type: application/json

Update a single subscription by email.

Reference: https://developers.beehiiv.com/api-reference/subscriptions/update-by-email

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/subscriptions/by_email/{email}:
    put:
      operationId: update-by-email
      summary: >-
        Update subscription by email <Badge intent="info" minimal outlined>OAuth
        Scope: subscriptions:write</Badge>
      description: Update a single subscription by email.
      tags:
        - subpackage_subscriptions
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: email
          in: path
          description: The email of the subscription object
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_subscriptions:SubscriptionResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                email:
                  type: string
                  description: The new email address for the subscription
                tier:
                  $ref: >-
                    #/components/schemas/type_bulkSubscriptionUpdates:SubscriptionsPutRequestSubscriptionsItemTier
                  description: Optional parameter to set the tier for this subscription.
                premium_tier_ids:
                  type: array
                  items:
                    type: string
                  description: >-
                    An array of premium tier IDs to assign to this subscription.
                    When provided, the subscription will be assigned to these
                    specific premium tiers. Can be combined with `premium_tiers`
                    to include tiers from both (duplicates are removed). Takes
                    precedence over the `tier` parameter.
                premium_tiers:
                  type: array
                  items:
                    type: string
                  description: >-
                    An array of premium tier names to assign to this
                    subscription. When provided, the subscription will be
                    assigned to premium tiers matching these names. Can be
                    combined with `premium_tier_ids` to include tiers from both
                    (duplicates are removed). Takes precedence over the `tier`
                    parameter.
                stripe_customer_id:
                  $ref: '#/components/schemas/type_ids:OptionalStripeCustomerId'
                  description: The Stripe Customer ID of the subscription (not required)
                unsubscribe:
                  type: boolean
                  description: >-
                    A boolean value specifying whether to unsubscribe this
                    subscription from the publication (not required)
                custom_fields:
                  type: array
                  items:
                    $ref: >-
                      #/components/schemas/type_bulkSubscriptionUpdates:SubscriptionsPutRequestSubscriptionsItemCustomFieldsItem
                  description: An array of custom field objects to update
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_bulkSubscriptionUpdates:SubscriptionsPutRequestSubscriptionsItemTier:
      type: string
      enum:
        - free
        - premium
      description: The Tier of the Subscription (not required)
      title: SubscriptionsPutRequestSubscriptionsItemTier
    type_ids:OptionalStripeCustomerId:
      type: string
      description: The prefixed ID of the Stripe customer.
      title: OptionalStripeCustomerId
    type_:CustomFieldDataType:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: boolean
        - type: array
          items:
            type: string
      title: CustomFieldDataType
    type_bulkSubscriptionUpdates:SubscriptionsPutRequestSubscriptionsItemCustomFieldsItem:
      type: object
      properties:
        name:
          type: string
          description: The name of the existing custom field
        value:
          $ref: '#/components/schemas/type_:CustomFieldDataType'
          description: The value of the custom field
        delete:
          type: boolean
          description: >-
            A boolean value to specify whether to delete this custom field entry
            from the subscription
      title: SubscriptionsPutRequestSubscriptionsItemCustomFieldsItem
    type_ids:SubscriptionId:
      type: string
      description: The prefixed ID of the subscription.
      title: SubscriptionId
    type_:SubscriptionExpandedStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
        - paused
      description: >-
        The status of the subscription.<br>`validating` - The email address is
        being validated.<br>`invalid` - The email address is
        invalid.<br>`pending` - The email address is valid, but the subscription
        is pending double opt-in.<br>`active` - The email was valid and the
        subscription is active.<br>`inactive` - The subscription was made
        inactive, possibly due to an unsubscribe.<br>`needs_attention` - The
        subscription requires approval or denial.<br>`paused` - The subscriber
        has paused their subscription.
      title: SubscriptionExpandedStatus
    type_:SubscriptionExpandedSubscriptionTier:
      type: string
      enum:
        - free
        - premium
      description: The current tier of the subscription.
      title: SubscriptionExpandedSubscriptionTier
    type_:SubscriptionExpandedUtmChannel:
      type: string
      enum:
        - ''
        - website
        - import
        - embed
        - api
        - referral
        - recommendation
        - magic_link
        - boost
        - boost_send
        - boost_direct_link
        - integration
        - product
      description: The acquisition channel
      title: SubscriptionExpandedUtmChannel
    type_ids:TierId:
      type: string
      description: The prefixed ID of the tier.
      title: TierId
    type_:SubscriptionTierInfoStatus:
      type: string
      enum:
        - active
        - archived
      description: Returns whether or not the tier has any active prices.
      title: SubscriptionTierInfoStatus
    type_:SubscriptionTierInfo:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:TierId'
        name:
          type: string
        status:
          $ref: '#/components/schemas/type_:SubscriptionTierInfoStatus'
          description: Returns whether or not the tier has any active prices.
      required:
        - id
        - name
        - status
      title: SubscriptionTierInfo
    type_:SubscriptionTierList:
      type: array
      items:
        $ref: '#/components/schemas/type_:SubscriptionTierInfo'
      description: >-
        Optional list of tiers for a subscription. Retrievable by including
        `expand: [subscription_premium_tiers]` in the request body.
      title: SubscriptionTierList
    type_:CustomFieldType:
      type: string
      enum:
        - string
        - integer
        - boolean
        - date
        - datetime
        - list
        - double
      description: The type of value being stored in the custom field.
      title: CustomFieldType
    type_:CustomField:
      type: object
      properties:
        name:
          type: string
          description: The name of the existing custom field
        kind:
          $ref: '#/components/schemas/type_:CustomFieldType'
          description: The type of value being stored in the custom field.
        value:
          $ref: '#/components/schemas/type_:CustomFieldDataType'
          description: The value stored for the subscription
      title: CustomField
    type_:SubscriptionCustomFieldList:
      type: array
      items:
        $ref: '#/components/schemas/type_:CustomField'
      description: >-
        Optional list of custom fields for a subscription. Retrievable by
        including `expand: [custom_field]` in the request body.
      title: SubscriptionCustomFieldList
    type_:SubscriptionTags:
      type: array
      items:
        type: string
      description: >-
        Optional list of tags for a subscription. Retrievable by including
        `expand: [tags]` in the request body.

        Max limit of 100 unique tags per publication.
      title: SubscriptionTags
    type_:SubscriptionStats:
      type: object
      properties:
        emails_received:
          type: integer
          description: The total number of emails that have been sent to this subscriber
        open_rate:
          type: number
          format: double
          description: The percentage of emails that the subscriber has opened
        click_through_rate:
          type: number
          format: double
          description: The percentage of emails that the subscriber has clicked a link in
      description: >-
        Optional list of stats for a subscription. Retrievable by including
        `expand: [stats]` in the request body.
      title: SubscriptionStats
    type_:Subscription:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:SubscriptionId'
          description: The prefixed subscription id
        email:
          type: string
          format: email
        status:
          $ref: '#/components/schemas/type_:SubscriptionExpandedStatus'
          description: >-
            The status of the subscription.<br>`validating` - The email address
            is being validated.<br>`invalid` - The email address is
            invalid.<br>`pending` - The email address is valid, but the
            subscription is pending double opt-in.<br>`active` - The email was
            valid and the subscription is active.<br>`inactive` - The
            subscription was made inactive, possibly due to an
            unsubscribe.<br>`needs_attention` - The subscription requires
            approval or denial.
        created:
          type: integer
          description: >-
            The date the subscription was created. Measured in seconds since the
            Unix epoch
        subscription_tier:
          $ref: '#/components/schemas/type_:SubscriptionExpandedSubscriptionTier'
          description: The current tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: >-
            The current premium tiers of the subscription. Empty if the
            subscriber is not associated with any premium tiers.
        utm_source:
          type: string
          description: The acquisition source; where the subscriber came from
        utm_medium:
          type: string
          description: The acquisition medium; how the subscriber got to your publication
        utm_channel:
          $ref: '#/components/schemas/type_:SubscriptionExpandedUtmChannel'
          description: The acquisition channel
        utm_campaign:
          type: string
          description: The acquisition campaign
        utm_term:
          type: string
          description: The acquisition term; typically the keyword or search term
        utm_content:
          type: string
          description: >-
            The acquisition content; typically used for A/B testing or ad
            variations
        referring_site:
          type: string
          description: The website that the subscriber was referred from
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        subscription_premium_tiers:
          $ref: '#/components/schemas/type_:SubscriptionTierList'
        custom_fields:
          $ref: '#/components/schemas/type_:SubscriptionCustomFieldList'
        tags:
          $ref: '#/components/schemas/type_:SubscriptionTags'
        stats:
          $ref: '#/components/schemas/type_:SubscriptionStats'
      required:
        - id
        - email
        - status
        - created
        - subscription_tier
        - subscription_premium_tier_names
        - utm_source
        - utm_medium
        - utm_channel
        - utm_campaign
        - utm_term
        - utm_content
        - referring_site
        - referral_code
      description: The subscription object
      title: Subscription
    type_subscriptions:SubscriptionResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_:Subscription'
      required:
        - data
      description: The response containing subscription data
      title: SubscriptionResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/by_email/example%40example.com"

payload = {
    "email": "newemail@example.com",
    "tier": "premium",
    "stripe_customer_id": "cus_12345abcde",
    "custom_fields": [
        {
            "name": "First Name",
            "value": "Bruce"
        },
        {
            "name": "Last Name",
            "value": "Wayne"
        }
    ]
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/by_email/example%40example.com';
const options = {
  method: 'PUT',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"email":"newemail@example.com","tier":"premium","stripe_customer_id":"cus_12345abcde","custom_fields":[{"name":"First Name","value":"Bruce"},{"name":"Last Name","value":"Wayne"}]}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/by_email/example%40example.com"

	payload := strings.NewReader("{\n  \"email\": \"newemail@example.com\",\n  \"tier\": \"premium\",\n  \"stripe_customer_id\": \"cus_12345abcde\",\n  \"custom_fields\": [\n    {\n      \"name\": \"First Name\",\n      \"value\": \"Bruce\"\n    },\n    {\n      \"name\": \"Last Name\",\n      \"value\": \"Wayne\"\n    }\n  ]\n}")

	req, _ := http.NewRequest("PUT", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/by_email/example%40example.com")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"email\": \"newemail@example.com\",\n  \"tier\": \"premium\",\n  \"stripe_customer_id\": \"cus_12345abcde\",\n  \"custom_fields\": [\n    {\n      \"name\": \"First Name\",\n      \"value\": \"Bruce\"\n    },\n    {\n      \"name\": \"Last Name\",\n      \"value\": \"Wayne\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/by_email/example%40example.com")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"email\": \"newemail@example.com\",\n  \"tier\": \"premium\",\n  \"stripe_customer_id\": \"cus_12345abcde\",\n  \"custom_fields\": [\n    {\n      \"name\": \"First Name\",\n      \"value\": \"Bruce\"\n    },\n    {\n      \"name\": \"Last Name\",\n      \"value\": \"Wayne\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/by_email/example%40example.com', [
  'body' => '{
  "email": "newemail@example.com",
  "tier": "premium",
  "stripe_customer_id": "cus_12345abcde",
  "custom_fields": [
    {
      "name": "First Name",
      "value": "Bruce"
    },
    {
      "name": "Last Name",
      "value": "Wayne"
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/by_email/example%40example.com");
var request = new RestRequest(Method.PUT);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"email\": \"newemail@example.com\",\n  \"tier\": \"premium\",\n  \"stripe_customer_id\": \"cus_12345abcde\",\n  \"custom_fields\": [\n    {\n      \"name\": \"First Name\",\n      \"value\": \"Bruce\"\n    },\n    {\n      \"name\": \"Last Name\",\n      \"value\": \"Wayne\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "email": "newemail@example.com",
  "tier": "premium",
  "stripe_customer_id": "cus_12345abcde",
  "custom_fields": [
    [
      "name": "First Name",
      "value": "Bruce"
    ],
    [
      "name": "Last Name",
      "value": "Wayne"
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/by_email/example%40example.com")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PUT"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Delete subscription <Badge intent="info" minimal outlined>OAuth Scope: subscriptions:write</Badge>

DELETE https://api.beehiiv.com/v2/publications/{publicationId}/subscriptions/{subscriptionId}

<Warning>This cannot be undone. All data associated with the subscription will also be deleted. We recommend unsubscribing when possible instead of deleting. If a premium subscription is deleted they will no longer be billed.</Warning> Deletes a subscription.

Reference: https://developers.beehiiv.com/api-reference/subscriptions/delete

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/subscriptions/{subscriptionId}:
    delete:
      operationId: delete
      summary: >-
        Delete subscription <Badge intent="info" minimal outlined>OAuth Scope:
        subscriptions:write</Badge>
      description: >-
        <Warning>This cannot be undone. All data associated with the
        subscription will also be deleted. We recommend unsubscribing when
        possible instead of deleting. If a premium subscription is deleted they
        will no longer be billed.</Warning> Deletes a subscription.
      tags:
        - subpackage_subscriptions
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: subscriptionId
          in: path
          description: The prefixed ID of the subscription object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:SubscriptionId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '204':
          description: No Content
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_subscriptions:SubscriptionDeleteResponse
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:SubscriptionId:
      type: string
      description: The prefixed ID of the subscription.
      title: SubscriptionId
    type_subscriptions:SubscriptionDeleteResponse:
      type: object
      properties:
        message:
          type: string
      title: SubscriptionDeleteResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.subscriptions.delete("sub_00000000-0000-0000-0000-000000000000", "pub_00000000-0000-0000-0000-000000000000");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000"

payload = {}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.delete(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("DELETE", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000");
var request = new RestRequest(Method.DELETE);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/subscriptions/sub_00000000-0000-0000-0000-000000000000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Add subscription tag <Badge intent="info" minimal outlined>OAuth Scope: subscriptions:write</Badge>

POST https://api.beehiiv.com/v2/publications/{publicationId}/subscriptions/{subscriptionId}/tags
Content-Type: application/json

Adds tags to a subscription. If the tag does not exist on the publication, it will be created automatically.

Reference: https://developers.beehiiv.com/api-reference/subscription-tags/create

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/subscriptions/{subscriptionId}/tags:
    post:
      operationId: create
      summary: >-
        Add subscription tag <Badge intent="info" minimal outlined>OAuth Scope:
        subscriptions:write</Badge>
      description: >-
        Adds tags to a subscription. If the tag does not exist on the
        publication, it will be created automatically.
      tags:
        - subpackage_subscriptionTags
      parameters:
        - name: publicationId
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: subscriptionId
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:SubscriptionId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/type_subscriptionTags:SubscriptionTagsCreateResponse
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                tags:
                  type: array
                  items:
                    type: string
                  description: Tags that can be used to group subscribers
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:SubscriptionId:
      type: string
      description: The prefixed ID of the subscription.
      title: SubscriptionId
    type_:SubscriptionExpandedStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
        - paused
      description: >-
        The status of the subscription.<br>`validating` - The email address is
        being validated.<br>`invalid` - The email address is
        invalid.<br>`pending` - The email address is valid, but the subscription
        is pending double opt-in.<br>`active` - The email was valid and the
        subscription is active.<br>`inactive` - The subscription was made
        inactive, possibly due to an unsubscribe.<br>`needs_attention` - The
        subscription requires approval or denial.<br>`paused` - The subscriber
        has paused their subscription.
      title: SubscriptionExpandedStatus
    type_:SubscriptionExpandedSubscriptionTier:
      type: string
      enum:
        - free
        - premium
      description: The current tier of the subscription.
      title: SubscriptionExpandedSubscriptionTier
    type_:SubscriptionExpandedUtmChannel:
      type: string
      enum:
        - ''
        - website
        - import
        - embed
        - api
        - referral
        - recommendation
        - magic_link
        - boost
        - boost_send
        - boost_direct_link
        - integration
        - product
      description: The acquisition channel
      title: SubscriptionExpandedUtmChannel
    type_ids:TierId:
      type: string
      description: The prefixed ID of the tier.
      title: TierId
    type_:SubscriptionTierInfoStatus:
      type: string
      enum:
        - active
        - archived
      description: Returns whether or not the tier has any active prices.
      title: SubscriptionTierInfoStatus
    type_:SubscriptionTierInfo:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:TierId'
        name:
          type: string
        status:
          $ref: '#/components/schemas/type_:SubscriptionTierInfoStatus'
          description: Returns whether or not the tier has any active prices.
      required:
        - id
        - name
        - status
      title: SubscriptionTierInfo
    type_:SubscriptionTierList:
      type: array
      items:
        $ref: '#/components/schemas/type_:SubscriptionTierInfo'
      description: >-
        Optional list of tiers for a subscription. Retrievable by including
        `expand: [subscription_premium_tiers]` in the request body.
      title: SubscriptionTierList
    type_:CustomFieldType:
      type: string
      enum:
        - string
        - integer
        - boolean
        - date
        - datetime
        - list
        - double
      description: The type of value being stored in the custom field.
      title: CustomFieldType
    type_:CustomFieldDataType:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: boolean
        - type: array
          items:
            type: string
      title: CustomFieldDataType
    type_:CustomField:
      type: object
      properties:
        name:
          type: string
          description: The name of the existing custom field
        kind:
          $ref: '#/components/schemas/type_:CustomFieldType'
          description: The type of value being stored in the custom field.
        value:
          $ref: '#/components/schemas/type_:CustomFieldDataType'
          description: The value stored for the subscription
      title: CustomField
    type_:SubscriptionCustomFieldList:
      type: array
      items:
        $ref: '#/components/schemas/type_:CustomField'
      description: >-
        Optional list of custom fields for a subscription. Retrievable by
        including `expand: [custom_field]` in the request body.
      title: SubscriptionCustomFieldList
    type_:SubscriptionTags:
      type: array
      items:
        type: string
      description: >-
        Optional list of tags for a subscription. Retrievable by including
        `expand: [tags]` in the request body.

        Max limit of 100 unique tags per publication.
      title: SubscriptionTags
    type_:SubscriptionStats:
      type: object
      properties:
        emails_received:
          type: integer
          description: The total number of emails that have been sent to this subscriber
        open_rate:
          type: number
          format: double
          description: The percentage of emails that the subscriber has opened
        click_through_rate:
          type: number
          format: double
          description: The percentage of emails that the subscriber has clicked a link in
      description: >-
        Optional list of stats for a subscription. Retrievable by including
        `expand: [stats]` in the request body.
      title: SubscriptionStats
    type_:Subscription:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:SubscriptionId'
          description: The prefixed subscription id
        email:
          type: string
          format: email
        status:
          $ref: '#/components/schemas/type_:SubscriptionExpandedStatus'
          description: >-
            The status of the subscription.<br>`validating` - The email address
            is being validated.<br>`invalid` - The email address is
            invalid.<br>`pending` - The email address is valid, but the
            subscription is pending double opt-in.<br>`active` - The email was
            valid and the subscription is active.<br>`inactive` - The
            subscription was made inactive, possibly due to an
            unsubscribe.<br>`needs_attention` - The subscription requires
            approval or denial.
        created:
          type: integer
          description: >-
            The date the subscription was created. Measured in seconds since the
            Unix epoch
        subscription_tier:
          $ref: '#/components/schemas/type_:SubscriptionExpandedSubscriptionTier'
          description: The current tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: >-
            The current premium tiers of the subscription. Empty if the
            subscriber is not associated with any premium tiers.
        utm_source:
          type: string
          description: The acquisition source; where the subscriber came from
        utm_medium:
          type: string
          description: The acquisition medium; how the subscriber got to your publication
        utm_channel:
          $ref: '#/components/schemas/type_:SubscriptionExpandedUtmChannel'
          description: The acquisition channel
        utm_campaign:
          type: string
          description: The acquisition campaign
        utm_term:
          type: string
          description: The acquisition term; typically the keyword or search term
        utm_content:
          type: string
          description: >-
            The acquisition content; typically used for A/B testing or ad
            variations
        referring_site:
          type: string
          description: The website that the subscriber was referred from
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        subscription_premium_tiers:
          $ref: '#/components/schemas/type_:SubscriptionTierList'
        custom_fields:
          $ref: '#/components/schemas/type_:SubscriptionCustomFieldList'
        tags:
          $ref: '#/components/schemas/type_:SubscriptionTags'
        stats:
          $ref: '#/components/schemas/type_:SubscriptionStats'
      required:
        - id
        - email
        - status
        - created
        - subscription_tier
        - subscription_premium_tier_names
        - utm_source
        - utm_medium
        - utm_channel
        - utm_campaign
        - utm_term
        - utm_content
        - referring_site
        - referral_code
      description: The subscription object
      title: Subscription
    type_subscriptionTags:SubscriptionTagsCreateResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_:Subscription'
      title: SubscriptionTagsCreateResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.subscriptionTags.create("publicationId", "subscriptionId");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/publicationId/subscriptions/subscriptionId/tags"

payload = { "tags": ["Premium", "Basic"] }
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/publicationId/subscriptions/subscriptionId/tags"

	payload := strings.NewReader("{\n  \"tags\": [\n    \"Premium\",\n    \"Basic\"\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/publicationId/subscriptions/subscriptionId/tags")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"tags\": [\n    \"Premium\",\n    \"Basic\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.beehiiv.com/v2/publications/publicationId/subscriptions/subscriptionId/tags")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"tags\": [\n    \"Premium\",\n    \"Basic\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.beehiiv.com/v2/publications/publicationId/subscriptions/subscriptionId/tags', [
  'body' => '{
  "tags": [
    "Premium",
    "Basic"
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/publicationId/subscriptions/subscriptionId/tags");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"tags\": [\n    \"Premium\",\n    \"Basic\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["tags": ["Premium", "Basic"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/publicationId/subscriptions/subscriptionId/tags")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Create a tier <Badge intent="info" minimal outlined>OAuth Scope: tiers:write</Badge>

POST https://api.beehiiv.com/v2/publications/{publicationId}/tiers
Content-Type: application/json

Create a new tier for a publication.

Reference: https://developers.beehiiv.com/api-reference/tiers/create

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/tiers:
    post:
      operationId: create
      summary: >-
        Create a tier <Badge intent="info" minimal outlined>OAuth Scope:
        tiers:write</Badge>
      description: Create a new tier for a publication.
      tags:
        - subpackage_tiers
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_tiers:TierResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                description:
                  type: string
                prices_attributes:
                  type: array
                  items:
                    $ref: '#/components/schemas/type_tiers:TierPricesAttributesItem'
              required:
                - name
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_tiers:TierPriceCurrency:
      type: string
      enum:
        - usd
        - aud
        - cad
        - eur
        - inr
        - brl
      title: TierPriceCurrency
    type_tiers:TierPriceInterval:
      type: string
      enum:
        - month
        - quarter
        - year
        - one_time
        - donation
      title: TierPriceInterval
    type_tiers:TierPricesAttributesItem:
      type: object
      properties:
        currency:
          $ref: '#/components/schemas/type_tiers:TierPriceCurrency'
        amount_cents:
          type: integer
        enabled:
          type: boolean
          default: true
        interval:
          $ref: '#/components/schemas/type_tiers:TierPriceInterval'
        interval_display:
          type: string
        cta:
          type: string
        features:
          type: array
          items:
            type: string
      required:
        - currency
        - amount_cents
        - interval
      title: TierPricesAttributesItem
    type_ids:TierId:
      type: string
      description: The prefixed ID of the tier.
      title: TierId
    type_tiers:TierStatus:
      type: string
      enum:
        - active
        - archived
      description: Returns whether or not the tier has any active prices.
      title: TierStatus
    type_tiers:TierStats:
      type: object
      properties:
        active_subscriptions:
          type: integer
          description: Total number of active subscriptions belonging to this tier.
      required:
        - active_subscriptions
      description: >-
        Optional list of stats for a tier. Retrievable by including `expand:
        [stats]` in the tier request body.
      title: TierStats
    type_ids:PriceId:
      type: string
      description: The prefixed ID of the price.
      title: PriceId
    type_tiers:TierPrice:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:PriceId'
        currency:
          $ref: '#/components/schemas/type_tiers:TierPriceCurrency'
        amount_cents:
          type: integer
        enabled:
          type: boolean
          default: true
        interval:
          $ref: '#/components/schemas/type_tiers:TierPriceInterval'
        denominator:
          type: string
        cta:
          type: string
          description: >-
            When using the external Stripe checkout, this text will be displayed
            on the button
        features:
          type: array
          items:
            type: string
      description: Price belonging to a Tier
      title: TierPrice
    type_tiers:Tier:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:TierId'
        name:
          type: string
        status:
          $ref: '#/components/schemas/type_tiers:TierStatus'
          description: Returns whether or not the tier has any active prices.
        description:
          type: string
          default: Super engaged readers
        stats:
          $ref: '#/components/schemas/type_tiers:TierStats'
        prices:
          type: array
          items:
            $ref: '#/components/schemas/type_tiers:TierPrice'
          description: >-
            Optional list of prices for a tier. Retrievable by including
            `expand: [prices]` in the tier request body.
      required:
        - id
        - name
        - status
      description: The subscription tier object.
      title: Tier
    type_tiers:TierResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_tiers:Tier'
      title: TierResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.tiers.postPublicationsPublicationIdTiers("pub_00000000-0000-0000-0000-000000000000", {
    name: "name"
});

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers"

payload = {
    "name": "Gold Tier",
    "description": "Our premium tier with exclusive benefits",
    "prices_attributes": [
        {
            "currency": "usd",
            "amount_cents": 500,
            "interval": "month",
            "enabled": True,
            "interval_display": "Monthly",
            "cta": "Subscribe Now",
            "features": ["Exclusive content", "Ad-free experience", "Priority support"]
        }
    ]
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers"

	payload := strings.NewReader("{\n  \"name\": \"Gold Tier\",\n  \"description\": \"Our premium tier with exclusive benefits\",\n  \"prices_attributes\": [\n    {\n      \"currency\": \"usd\",\n      \"amount_cents\": 500,\n      \"interval\": \"month\",\n      \"enabled\": true,\n      \"interval_display\": \"Monthly\",\n      \"cta\": \"Subscribe Now\",\n      \"features\": [\n        \"Exclusive content\",\n        \"Ad-free experience\",\n        \"Priority support\"\n      ]\n    }\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"Gold Tier\",\n  \"description\": \"Our premium tier with exclusive benefits\",\n  \"prices_attributes\": [\n    {\n      \"currency\": \"usd\",\n      \"amount_cents\": 500,\n      \"interval\": \"month\",\n      \"enabled\": true,\n      \"interval_display\": \"Monthly\",\n      \"cta\": \"Subscribe Now\",\n      \"features\": [\n        \"Exclusive content\",\n        \"Ad-free experience\",\n        \"Priority support\"\n      ]\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"Gold Tier\",\n  \"description\": \"Our premium tier with exclusive benefits\",\n  \"prices_attributes\": [\n    {\n      \"currency\": \"usd\",\n      \"amount_cents\": 500,\n      \"interval\": \"month\",\n      \"enabled\": true,\n      \"interval_display\": \"Monthly\",\n      \"cta\": \"Subscribe Now\",\n      \"features\": [\n        \"Exclusive content\",\n        \"Ad-free experience\",\n        \"Priority support\"\n      ]\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers', [
  'body' => '{
  "name": "Gold Tier",
  "description": "Our premium tier with exclusive benefits",
  "prices_attributes": [
    {
      "currency": "usd",
      "amount_cents": 500,
      "interval": "month",
      "enabled": true,
      "interval_display": "Monthly",
      "cta": "Subscribe Now",
      "features": [
        "Exclusive content",
        "Ad-free experience",
        "Priority support"
      ]
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"Gold Tier\",\n  \"description\": \"Our premium tier with exclusive benefits\",\n  \"prices_attributes\": [\n    {\n      \"currency\": \"usd\",\n      \"amount_cents\": 500,\n      \"interval\": \"month\",\n      \"enabled\": true,\n      \"interval_display\": \"Monthly\",\n      \"cta\": \"Subscribe Now\",\n      \"features\": [\n        \"Exclusive content\",\n        \"Ad-free experience\",\n        \"Priority support\"\n      ]\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "name": "Gold Tier",
  "description": "Our premium tier with exclusive benefits",
  "prices_attributes": [
    [
      "currency": "usd",
      "amount_cents": 500,
      "interval": "month",
      "enabled": true,
      "interval_display": "Monthly",
      "cta": "Subscribe Now",
      "features": ["Exclusive content", "Ad-free experience", "Priority support"]
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# List tiers <Badge intent="info" minimal outlined>OAuth Scope: tiers:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/tiers

Retrieve all tiers belonging to a specific publication

Reference: https://developers.beehiiv.com/api-reference/tiers/index

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/tiers:
    get:
      operationId: index
      summary: >-
        List tiers <Badge intent="info" minimal outlined>OAuth Scope:
        tiers:read</Badge>
      description: Retrieve all tiers belonging to a specific publication
      tags:
        - subpackage_tiers
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: expand[]
          in: query
          description: >-
            Optional list of expandable objects.<br>`stats` - Returns statistics
            about the tier(s).<br>`prices` - Returns prices for the tier(s).
          required: false
          schema:
            type: string
        - name: limit
          in: query
          description: >-
            A limit on the number of objects to be returned. The limit can range
            between 1 and 100, and the default is 10.
          required: false
          schema:
            type: integer
        - name: page
          in: query
          description: >-
            Pagination returns the results in pages. Each page contains the
            number of results specified by the `limit` (default: 10).<br>If not
            specified, results 1-10 from page 1 will be returned.
          required: false
          schema:
            type: integer
        - name: direction
          in: query
          description: >-
            The direction that the results are sorted in. Defaults to asc<br>
            `asc` - Ascending, sorts from smallest to largest.<br> `desc` -
            Descending, sorts from largest to smallest.
          required: false
          schema:
            $ref: '#/components/schemas/type_:RequestDirection'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_tiers:IndexTiersResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_:RequestDirection:
      type: string
      enum:
        - asc
        - desc
      default: asc
      description: The direction of the request. Defaults to `asc`.
      title: RequestDirection
    type_ids:TierId:
      type: string
      description: The prefixed ID of the tier.
      title: TierId
    type_tiers:TierStatus:
      type: string
      enum:
        - active
        - archived
      description: Returns whether or not the tier has any active prices.
      title: TierStatus
    type_tiers:TierStats:
      type: object
      properties:
        active_subscriptions:
          type: integer
          description: Total number of active subscriptions belonging to this tier.
      required:
        - active_subscriptions
      description: >-
        Optional list of stats for a tier. Retrievable by including `expand:
        [stats]` in the tier request body.
      title: TierStats
    type_ids:PriceId:
      type: string
      description: The prefixed ID of the price.
      title: PriceId
    type_tiers:TierPriceCurrency:
      type: string
      enum:
        - usd
        - aud
        - cad
        - eur
        - inr
        - brl
      title: TierPriceCurrency
    type_tiers:TierPriceInterval:
      type: string
      enum:
        - month
        - quarter
        - year
        - one_time
        - donation
      title: TierPriceInterval
    type_tiers:TierPrice:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:PriceId'
        currency:
          $ref: '#/components/schemas/type_tiers:TierPriceCurrency'
        amount_cents:
          type: integer
        enabled:
          type: boolean
          default: true
        interval:
          $ref: '#/components/schemas/type_tiers:TierPriceInterval'
        denominator:
          type: string
        cta:
          type: string
          description: >-
            When using the external Stripe checkout, this text will be displayed
            on the button
        features:
          type: array
          items:
            type: string
      description: Price belonging to a Tier
      title: TierPrice
    type_tiers:Tier:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:TierId'
        name:
          type: string
        status:
          $ref: '#/components/schemas/type_tiers:TierStatus'
          description: Returns whether or not the tier has any active prices.
        description:
          type: string
          default: Super engaged readers
        stats:
          $ref: '#/components/schemas/type_tiers:TierStats'
        prices:
          type: array
          items:
            $ref: '#/components/schemas/type_tiers:TierPrice'
          description: >-
            Optional list of prices for a tier. Retrievable by including
            `expand: [prices]` in the tier request body.
      required:
        - id
        - name
        - status
      description: The subscription tier object.
      title: Tier
    type_tiers:IndexTiersResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/type_tiers:Tier'
        limit:
          type: integer
          description: >-
            The limit placed on the results. If no limit was specified in the
            request,this defaults to 10.
        page:
          type: integer
          default: 1
          description: >-
            The page number the results are from. If no page was specified in
            the request, this defaults to page 1.
        total_results:
          type: integer
          description: The total number of results from all pages.
        total_pages:
          type: integer
          description: The total number of pages.
      required:
        - data
        - limit
        - page
        - total_results
        - total_pages
      title: IndexTiersResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.tiers.getPublicationsPublicationIdTiers("pub_00000000-0000-0000-0000-000000000000");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers"

payload = {}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get tier <Badge intent="info" minimal outlined>OAuth Scope: tiers:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/tiers/{tierId}

Retrieve a single tier belonging to a specific publication

Reference: https://developers.beehiiv.com/api-reference/tiers/show

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/tiers/{tierId}:
    get:
      operationId: show
      summary: >-
        Get tier <Badge intent="info" minimal outlined>OAuth Scope:
        tiers:read</Badge>
      description: Retrieve a single tier belonging to a specific publication
      tags:
        - subpackage_tiers
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: tierId
          in: path
          description: The prefixed ID of the tier object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:TierId'
        - name: expand[]
          in: query
          description: >-
            Optional list of expandable objects.<br>`stats` - Returns statistics
            about the tier(s).<br>`prices` - Returns prices for the tier(s).
          required: false
          schema:
            type: string
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_tiers:TierResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:TierId:
      type: string
      description: The prefixed ID of the tier.
      title: TierId
    type_tiers:TierStatus:
      type: string
      enum:
        - active
        - archived
      description: Returns whether or not the tier has any active prices.
      title: TierStatus
    type_tiers:TierStats:
      type: object
      properties:
        active_subscriptions:
          type: integer
          description: Total number of active subscriptions belonging to this tier.
      required:
        - active_subscriptions
      description: >-
        Optional list of stats for a tier. Retrievable by including `expand:
        [stats]` in the tier request body.
      title: TierStats
    type_ids:PriceId:
      type: string
      description: The prefixed ID of the price.
      title: PriceId
    type_tiers:TierPriceCurrency:
      type: string
      enum:
        - usd
        - aud
        - cad
        - eur
        - inr
        - brl
      title: TierPriceCurrency
    type_tiers:TierPriceInterval:
      type: string
      enum:
        - month
        - quarter
        - year
        - one_time
        - donation
      title: TierPriceInterval
    type_tiers:TierPrice:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:PriceId'
        currency:
          $ref: '#/components/schemas/type_tiers:TierPriceCurrency'
        amount_cents:
          type: integer
        enabled:
          type: boolean
          default: true
        interval:
          $ref: '#/components/schemas/type_tiers:TierPriceInterval'
        denominator:
          type: string
        cta:
          type: string
          description: >-
            When using the external Stripe checkout, this text will be displayed
            on the button
        features:
          type: array
          items:
            type: string
      description: Price belonging to a Tier
      title: TierPrice
    type_tiers:Tier:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:TierId'
        name:
          type: string
        status:
          $ref: '#/components/schemas/type_tiers:TierStatus'
          description: Returns whether or not the tier has any active prices.
        description:
          type: string
          default: Super engaged readers
        stats:
          $ref: '#/components/schemas/type_tiers:TierStats'
        prices:
          type: array
          items:
            $ref: '#/components/schemas/type_tiers:TierPrice'
          description: >-
            Optional list of prices for a tier. Retrievable by including
            `expand: [prices]` in the tier request body.
      required:
        - id
        - name
        - status
      description: The subscription tier object.
      title: Tier
    type_tiers:TierResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_tiers:Tier'
      title: TierResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.tiers.getPublicationsPublicationIdTiersTierId("pub_00000000-0000-0000-0000-000000000000", "tier_00000000-0000-0000-0000-000000000000");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers/tier_00000000-0000-0000-0000-000000000000"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers/tier_00000000-0000-0000-0000-000000000000"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers/tier_00000000-0000-0000-0000-000000000000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers/tier_00000000-0000-0000-0000-000000000000")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers/tier_00000000-0000-0000-0000-000000000000', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers/tier_00000000-0000-0000-0000-000000000000");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers/tier_00000000-0000-0000-0000-000000000000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Update a tier <Badge intent="info" minimal outlined>OAuth Scope: tiers:write</Badge>

PUT https://api.beehiiv.com/v2/publications/{publicationId}/tiers/{tierId}
Content-Type: application/json

Update an existing tier belonging to a specific publication

Reference: https://developers.beehiiv.com/api-reference/tiers/put

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/tiers/{tierId}:
    put:
      operationId: put
      summary: >-
        Update a tier <Badge intent="info" minimal outlined>OAuth Scope:
        tiers:write</Badge>
      description: Update an existing tier belonging to a specific publication
      tags:
        - subpackage_tiers
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: tierId
          in: path
          description: The prefixed ID of the tier object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:TierId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_tiers:TierResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                description:
                  type: string
                prices_attributes:
                  type: array
                  items:
                    $ref: '#/components/schemas/type_tiers:UpdateTierPriceRequest'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:TierId:
      type: string
      description: The prefixed ID of the tier.
      title: TierId
    type_ids:PriceId:
      type: string
      description: The prefixed ID of the price.
      title: PriceId
    type_tiers:TierPriceCurrency:
      type: string
      enum:
        - usd
        - aud
        - cad
        - eur
        - inr
        - brl
      title: TierPriceCurrency
    type_tiers:TierPriceInterval:
      type: string
      enum:
        - month
        - quarter
        - year
        - one_time
        - donation
      title: TierPriceInterval
    type_tiers:UpdateTierPriceRequest:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:PriceId'
          description: ID of the existing price.
        currency:
          $ref: '#/components/schemas/type_tiers:TierPriceCurrency'
        amount_cents:
          type: integer
        interval:
          $ref: '#/components/schemas/type_tiers:TierPriceInterval'
        interval_display:
          type: string
        cta:
          type: string
        features:
          type: array
          items:
            type: string
        delete:
          type: boolean
          default: false
          description: Optionally delete the price when updating the tier.
      required:
        - id
        - currency
        - amount_cents
        - interval
      title: UpdateTierPriceRequest
    type_tiers:TierStatus:
      type: string
      enum:
        - active
        - archived
      description: Returns whether or not the tier has any active prices.
      title: TierStatus
    type_tiers:TierStats:
      type: object
      properties:
        active_subscriptions:
          type: integer
          description: Total number of active subscriptions belonging to this tier.
      required:
        - active_subscriptions
      description: >-
        Optional list of stats for a tier. Retrievable by including `expand:
        [stats]` in the tier request body.
      title: TierStats
    type_tiers:TierPrice:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:PriceId'
        currency:
          $ref: '#/components/schemas/type_tiers:TierPriceCurrency'
        amount_cents:
          type: integer
        enabled:
          type: boolean
          default: true
        interval:
          $ref: '#/components/schemas/type_tiers:TierPriceInterval'
        denominator:
          type: string
        cta:
          type: string
          description: >-
            When using the external Stripe checkout, this text will be displayed
            on the button
        features:
          type: array
          items:
            type: string
      description: Price belonging to a Tier
      title: TierPrice
    type_tiers:Tier:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:TierId'
        name:
          type: string
        status:
          $ref: '#/components/schemas/type_tiers:TierStatus'
          description: Returns whether or not the tier has any active prices.
        description:
          type: string
          default: Super engaged readers
        stats:
          $ref: '#/components/schemas/type_tiers:TierStats'
        prices:
          type: array
          items:
            $ref: '#/components/schemas/type_tiers:TierPrice'
          description: >-
            Optional list of prices for a tier. Retrievable by including
            `expand: [prices]` in the tier request body.
      required:
        - id
        - name
        - status
      description: The subscription tier object.
      title: Tier
    type_tiers:TierResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_tiers:Tier'
      title: TierResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.tiers.putPublicationsPublicationIdTiersTierId("pub_00000000-0000-0000-0000-000000000000", "tier_00000000-0000-0000-0000-000000000000");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers/tier_00000000-0000-0000-0000-000000000000"

payload = {
    "name": "Gold",
    "description": "Our premium tier with exclusive benefits",
    "prices_attributes": [
        {
            "id": "price_00000000-0000-0000-0000-000000000000",
            "currency": "usd",
            "amount_cents": 500,
            "interval": "month",
            "interval_display": "Monthly",
            "cta": "Subscribe Now",
            "features": ["Exclusive content"],
            "delete": True
        }
    ]
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers/tier_00000000-0000-0000-0000-000000000000"

	payload := strings.NewReader("{\n  \"name\": \"Gold\",\n  \"description\": \"Our premium tier with exclusive benefits\",\n  \"prices_attributes\": [\n    {\n      \"id\": \"price_00000000-0000-0000-0000-000000000000\",\n      \"currency\": \"usd\",\n      \"amount_cents\": 500,\n      \"interval\": \"month\",\n      \"interval_display\": \"Monthly\",\n      \"cta\": \"Subscribe Now\",\n      \"features\": [\n        \"Exclusive content\"\n      ],\n      \"delete\": true\n    }\n  ]\n}")

	req, _ := http.NewRequest("PUT", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers/tier_00000000-0000-0000-0000-000000000000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"Gold\",\n  \"description\": \"Our premium tier with exclusive benefits\",\n  \"prices_attributes\": [\n    {\n      \"id\": \"price_00000000-0000-0000-0000-000000000000\",\n      \"currency\": \"usd\",\n      \"amount_cents\": 500,\n      \"interval\": \"month\",\n      \"interval_display\": \"Monthly\",\n      \"cta\": \"Subscribe Now\",\n      \"features\": [\n        \"Exclusive content\"\n      ],\n      \"delete\": true\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers/tier_00000000-0000-0000-0000-000000000000")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"Gold\",\n  \"description\": \"Our premium tier with exclusive benefits\",\n  \"prices_attributes\": [\n    {\n      \"id\": \"price_00000000-0000-0000-0000-000000000000\",\n      \"currency\": \"usd\",\n      \"amount_cents\": 500,\n      \"interval\": \"month\",\n      \"interval_display\": \"Monthly\",\n      \"cta\": \"Subscribe Now\",\n      \"features\": [\n        \"Exclusive content\"\n      ],\n      \"delete\": true\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers/tier_00000000-0000-0000-0000-000000000000', [
  'body' => '{
  "name": "Gold",
  "description": "Our premium tier with exclusive benefits",
  "prices_attributes": [
    {
      "id": "price_00000000-0000-0000-0000-000000000000",
      "currency": "usd",
      "amount_cents": 500,
      "interval": "month",
      "interval_display": "Monthly",
      "cta": "Subscribe Now",
      "features": [
        "Exclusive content"
      ],
      "delete": true
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers/tier_00000000-0000-0000-0000-000000000000");
var request = new RestRequest(Method.PUT);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"Gold\",\n  \"description\": \"Our premium tier with exclusive benefits\",\n  \"prices_attributes\": [\n    {\n      \"id\": \"price_00000000-0000-0000-0000-000000000000\",\n      \"currency\": \"usd\",\n      \"amount_cents\": 500,\n      \"interval\": \"month\",\n      \"interval_display\": \"Monthly\",\n      \"cta\": \"Subscribe Now\",\n      \"features\": [\n        \"Exclusive content\"\n      ],\n      \"delete\": true\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "name": "Gold",
  "description": "Our premium tier with exclusive benefits",
  "prices_attributes": [
    [
      "id": "price_00000000-0000-0000-0000-000000000000",
      "currency": "usd",
      "amount_cents": 500,
      "interval": "month",
      "interval_display": "Monthly",
      "cta": "Subscribe Now",
      "features": ["Exclusive content"],
      "delete": true
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/tiers/tier_00000000-0000-0000-0000-000000000000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PUT"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Create a webhook <Badge intent="info" minimal outlined>OAuth Scope: webhooks:write</Badge>

POST https://api.beehiiv.com/v2/publications/{publicationId}/webhooks
Content-Type: application/json

Create a new webhook for a given publication.

Reference: https://developers.beehiiv.com/api-reference/webhooks/create

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/webhooks:
    post:
      operationId: create
      summary: >-
        Create a webhook <Badge intent="info" minimal outlined>OAuth Scope:
        webhooks:write</Badge>
      description: Create a new webhook for a given publication.
      tags:
        - subpackage_webhooks
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Webhook created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_webhooks:WebhookResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                url:
                  type: string
                  format: uri
                  description: The webhook URL to send events to.
                event_types:
                  type: array
                  items:
                    $ref: '#/components/schemas/type_webhooks:WebhookEventType'
                  description: The types of events the webhook will receive.
                description:
                  type: string
                  description: A description of the webhook.
              required:
                - url
                - event_types
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_webhooks:WebhookEventType:
      type: string
      enum:
        - post.sent
        - post.updated
        - subscription.confirmed
        - subscription.created
        - subscription.downgraded
        - subscription.paused
        - subscription.resumed
        - subscription.tier.paused
        - subscription.tier.resumed
        - subscription.upgraded
        - subscription.tier.created
        - subscription.tier.deleted
        - subscription.deleted
        - survey.response_submitted
      title: WebhookEventType
    type_ids:EndpointId:
      type: string
      description: The prefixed ID of the endpoint.
      title: EndpointId
    type_webhooks:Webhook:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:EndpointId'
          description: The prefixed ID for the webhook.
        url:
          type: string
          format: uri
          description: The webhook URL to send events to.
        created:
          type: integer
          description: >-
            The date the webhook was created. Measured in seconds since the Unix
            epoch.
        updated:
          type: integer
          description: >-
            The date the webhook was last updated. Measured in seconds since the
            Unix epoch.
        event_types:
          type: array
          items:
            $ref: '#/components/schemas/type_webhooks:WebhookEventType'
          description: The types of events the webhook will receive.
        description:
          type: string
          description: The user-defined description for the webhook.
      required:
        - id
        - url
        - created
        - updated
        - event_types
        - description
      title: Webhook
    type_webhooks:WebhookResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_webhooks:Webhook'
      required:
        - data
      title: WebhookResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient, Beehiiv } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.webhooks.postWebhooks("pub_00000000-0000-0000-0000-000000000000", {
    url: "https://example.com/webhook",
    eventTypes: [Beehiiv.PostWebhooksRequestEventTypesItem.PostSent]
});

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks"

payload = {
    "url": "https://example.com/webhook",
    "event_types": ["post.sent"]
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks"

	payload := strings.NewReader("{\n  \"url\": \"https://example.com/webhook\",\n  \"event_types\": [\n    \"post.sent\"\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"url\": \"https://example.com/webhook\",\n  \"event_types\": [\n    \"post.sent\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"url\": \"https://example.com/webhook\",\n  \"event_types\": [\n    \"post.sent\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks', [
  'body' => '{
  "url": "https://example.com/webhook",
  "event_types": [
    "post.sent"
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"url\": \"https://example.com/webhook\",\n  \"event_types\": [\n    \"post.sent\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "url": "https://example.com/webhook",
  "event_types": ["post.sent"]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# List webhooks <Badge intent="info" minimal outlined>OAuth Scope: webhooks:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/webhooks

Retrieve all webhooks belonging to a specific publication.

Reference: https://developers.beehiiv.com/api-reference/webhooks/index

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/webhooks:
    get:
      operationId: index
      summary: >-
        List webhooks <Badge intent="info" minimal outlined>OAuth Scope:
        webhooks:read</Badge>
      description: Retrieve all webhooks belonging to a specific publication.
      tags:
        - subpackage_webhooks
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: limit
          in: query
          description: >-
            A limit on the number of objects to be returned. The limit can range
            between 1 and 100, and the default is 10.
          required: false
          schema:
            type: integer
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_webhooks:IndexWebhooksResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:EndpointId:
      type: string
      description: The prefixed ID of the endpoint.
      title: EndpointId
    type_webhooks:WebhookEventType:
      type: string
      enum:
        - post.sent
        - post.updated
        - subscription.confirmed
        - subscription.created
        - subscription.downgraded
        - subscription.paused
        - subscription.resumed
        - subscription.tier.paused
        - subscription.tier.resumed
        - subscription.upgraded
        - subscription.tier.created
        - subscription.tier.deleted
        - subscription.deleted
        - survey.response_submitted
      title: WebhookEventType
    type_webhooks:Webhook:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:EndpointId'
          description: The prefixed ID for the webhook.
        url:
          type: string
          format: uri
          description: The webhook URL to send events to.
        created:
          type: integer
          description: >-
            The date the webhook was created. Measured in seconds since the Unix
            epoch.
        updated:
          type: integer
          description: >-
            The date the webhook was last updated. Measured in seconds since the
            Unix epoch.
        event_types:
          type: array
          items:
            $ref: '#/components/schemas/type_webhooks:WebhookEventType'
          description: The types of events the webhook will receive.
        description:
          type: string
          description: The user-defined description for the webhook.
      required:
        - id
        - url
        - created
        - updated
        - event_types
        - description
      title: Webhook
    type_webhooks:IndexWebhooksResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/type_webhooks:Webhook'
      required:
        - data
      title: IndexWebhooksResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { BeehiivClient } from "beehiiv";

const client = new BeehiivClient({ token: "YOUR_TOKEN" });
await client.webhooks.getWebhooks("pub_00000000-0000-0000-0000-000000000000");

```

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get webhook <Badge intent="info" minimal outlined>OAuth Scope: webhooks:read</Badge>

GET https://api.beehiiv.com/v2/publications/{publicationId}/webhooks/{endpointId}

Retrieve a specific webhook belonging to a publication.

Reference: https://developers.beehiiv.com/api-reference/webhooks/show

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/webhooks/{endpointId}:
    get:
      operationId: show
      summary: >-
        Get webhook <Badge intent="info" minimal outlined>OAuth Scope:
        webhooks:read</Badge>
      description: Retrieve a specific webhook belonging to a publication.
      tags:
        - subpackage_webhooks
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: endpointId
          in: path
          description: The prefixed ID of the webhook object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:EndpointId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_webhooks:WebhookResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '422':
          description: Unprocessable Entity
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:EndpointId:
      type: string
      description: The prefixed ID of the endpoint.
      title: EndpointId
    type_webhooks:WebhookEventType:
      type: string
      enum:
        - post.sent
        - post.updated
        - subscription.confirmed
        - subscription.created
        - subscription.downgraded
        - subscription.paused
        - subscription.resumed
        - subscription.tier.paused
        - subscription.tier.resumed
        - subscription.upgraded
        - subscription.tier.created
        - subscription.tier.deleted
        - subscription.deleted
        - survey.response_submitted
      title: WebhookEventType
    type_webhooks:Webhook:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:EndpointId'
          description: The prefixed ID for the webhook.
        url:
          type: string
          format: uri
          description: The webhook URL to send events to.
        created:
          type: integer
          description: >-
            The date the webhook was created. Measured in seconds since the Unix
            epoch.
        updated:
          type: integer
          description: >-
            The date the webhook was last updated. Measured in seconds since the
            Unix epoch.
        event_types:
          type: array
          items:
            $ref: '#/components/schemas/type_webhooks:WebhookEventType'
          description: The types of events the webhook will receive.
        description:
          type: string
          description: The user-defined description for the webhook.
      required:
        - id
        - url
        - created
        - updated
        - event_types
        - description
      title: Webhook
    type_webhooks:WebhookResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_webhooks:Webhook'
      required:
        - data
      title: WebhookResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Update webhook <Badge intent="info" minimal outlined>OAuth Scope: webhooks:write</Badge>

PATCH https://api.beehiiv.com/v2/publications/{publicationId}/webhooks/{endpointId}
Content-Type: application/json

Update a webhook subscription for a publication.

Reference: https://developers.beehiiv.com/api-reference/webhooks/update

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/webhooks/{endpointId}:
    patch:
      operationId: update
      summary: >-
        Update webhook <Badge intent="info" minimal outlined>OAuth Scope:
        webhooks:write</Badge>
      description: Update a webhook subscription for a publication.
      tags:
        - subpackage_webhooks
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: endpointId
          in: path
          description: The prefixed ID of the webhook object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:EndpointId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_webhooks:WebhookResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                event_types:
                  type: array
                  items:
                    $ref: '#/components/schemas/type_webhooks:WebhookEventType'
                  description: The types of events the webhook will receive.
                description:
                  type: string
                  description: A description of the webhook.
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:EndpointId:
      type: string
      description: The prefixed ID of the endpoint.
      title: EndpointId
    type_webhooks:WebhookEventType:
      type: string
      enum:
        - post.sent
        - post.updated
        - subscription.confirmed
        - subscription.created
        - subscription.downgraded
        - subscription.paused
        - subscription.resumed
        - subscription.tier.paused
        - subscription.tier.resumed
        - subscription.upgraded
        - subscription.tier.created
        - subscription.tier.deleted
        - subscription.deleted
        - survey.response_submitted
      title: WebhookEventType
    type_webhooks:Webhook:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:EndpointId'
          description: The prefixed ID for the webhook.
        url:
          type: string
          format: uri
          description: The webhook URL to send events to.
        created:
          type: integer
          description: >-
            The date the webhook was created. Measured in seconds since the Unix
            epoch.
        updated:
          type: integer
          description: >-
            The date the webhook was last updated. Measured in seconds since the
            Unix epoch.
        event_types:
          type: array
          items:
            $ref: '#/components/schemas/type_webhooks:WebhookEventType'
          description: The types of events the webhook will receive.
        description:
          type: string
          description: The user-defined description for the webhook.
      required:
        - id
        - url
        - created
        - updated
        - event_types
        - description
      title: Webhook
    type_webhooks:WebhookResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_webhooks:Webhook'
      required:
        - data
      title: WebhookResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000"

payload = {
    "event_types": ["post.sent", "subscription.confirmed"],
    "description": "A webhook to receive new posts data and new subscription confirmations."
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000';
const options = {
  method: 'PATCH',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"event_types":["post.sent","subscription.confirmed"],"description":"A webhook to receive new posts data and new subscription confirmations."}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000"

	payload := strings.NewReader("{\n  \"event_types\": [\n    \"post.sent\",\n    \"subscription.confirmed\"\n  ],\n  \"description\": \"A webhook to receive new posts data and new subscription confirmations.\"\n}")

	req, _ := http.NewRequest("PATCH", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"event_types\": [\n    \"post.sent\",\n    \"subscription.confirmed\"\n  ],\n  \"description\": \"A webhook to receive new posts data and new subscription confirmations.\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"event_types\": [\n    \"post.sent\",\n    \"subscription.confirmed\"\n  ],\n  \"description\": \"A webhook to receive new posts data and new subscription confirmations.\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000', [
  'body' => '{
  "event_types": [
    "post.sent",
    "subscription.confirmed"
  ],
  "description": "A webhook to receive new posts data and new subscription confirmations."
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"event_types\": [\n    \"post.sent\",\n    \"subscription.confirmed\"\n  ],\n  \"description\": \"A webhook to receive new posts data and new subscription confirmations.\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "event_types": ["post.sent", "subscription.confirmed"],
  "description": "A webhook to receive new posts data and new subscription confirmations."
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Delete a webhook <Badge intent="info" minimal outlined>OAuth Scope: webhooks:write</Badge>

DELETE https://api.beehiiv.com/v2/publications/{publicationId}/webhooks/{endpointId}

Delete a webhook subscription from a publication.

Reference: https://developers.beehiiv.com/api-reference/webhooks/delete

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /publications/{publicationId}/webhooks/{endpointId}:
    delete:
      operationId: delete
      summary: >-
        Delete a webhook <Badge intent="info" minimal outlined>OAuth Scope:
        webhooks:write</Badge>
      description: Delete a webhook subscription from a publication.
      tags:
        - subpackage_webhooks
      parameters:
        - name: publicationId
          in: path
          description: The prefixed ID of the publication object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:PublicationId'
        - name: endpointId
          in: path
          description: The prefixed ID of the webhook object
          required: true
          schema:
            $ref: '#/components/schemas/type_ids:EndpointId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '204':
          description: No Content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_webhooks:WebhooksDeleteResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:EndpointId:
      type: string
      description: The prefixed ID of the endpoint.
      title: EndpointId
    type_webhooks:WebhooksDeleteResponse:
      type: object
      properties:
        message:
          type: string
      title: WebhooksDeleteResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000"

payload = {}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.delete(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000';
const options = {
  method: 'DELETE',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("DELETE", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000");
var request = new RestRequest(Method.DELETE);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/publications/pub_00000000-0000-0000-0000-000000000000/webhooks/ep_0000000000000000000000000000")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Identify workspace <Badge intent="info" minimal outlined>OAuth Scope: identify:read</Badge>

GET https://api.beehiiv.com/v2/workspaces/identify

Retrieve information about the workspace the OAuth or API token is associated with.

Reference: https://developers.beehiiv.com/api-reference/workspaces/identify

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /workspaces/identify:
    get:
      operationId: identify
      summary: >-
        Identify workspace <Badge intent="info" minimal outlined>OAuth Scope:
        identify:read</Badge>
      description: >-
        Retrieve information about the workspace the OAuth or API token is
        associated with.
      tags:
        - subpackage_workspaces
      parameters:
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_workspaces:WorkspaceIdentifyResponse'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_ids:WorkspaceId:
      type: string
      description: The prefixed ID of the workspace.
      title: WorkspaceId
    type_workspaces:WorkspaceIdentity:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:WorkspaceId'
          description: The prefixed ID of the workspace.
        name:
          type: string
          description: The name of the workspace.
        owner_email:
          type: string
          description: The email of the owner of the workspace.
      required:
        - id
        - name
        - owner_email
      title: WorkspaceIdentity
    type_workspaces:WorkspaceIdentifyResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/type_workspaces:WorkspaceIdentity'
      required:
        - data
      title: WorkspaceIdentifyResponse
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/workspaces/identify"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/workspaces/identify';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/workspaces/identify"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/workspaces/identify")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/workspaces/identify")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/workspaces/identify', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/workspaces/identify");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/workspaces/identify")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get publications by subscription email <Badge intent="info" minimal outlined>OAuth Scope: publications:read</Badge>

GET https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/{email}

Retrieve all publications in the workspace that have a subscription for the specified email address. The workspace is determined by the provided API key.

Reference: https://developers.beehiiv.com/api-reference/workspaces/publications-by-subscription-email

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: public_v2
  version: 1.0.0
paths:
  /workspaces/publications/by_subscription_email/{email}:
    get:
      operationId: publications-by-subscription-email
      summary: >-
        Get publications by subscription email <Badge intent="info" minimal
        outlined>OAuth Scope: publications:read</Badge>
      description: >-
        Retrieve all publications in the workspace that have a subscription for
        the specified email address. The workspace is determined by the provided
        API key.
      tags:
        - subpackage_workspaces
      parameters:
        - name: email
          in: path
          description: The email address to search for subscriptions
          required: true
          schema:
            type: string
        - name: expand
          in: query
          description: >-
            Optionally expand the results by adding additional information.
            <br>`subscription` - Returns the full Subscription object for the
            email address in each publication. <br>`publication` - Returns the
            full Publication object instead of just ID and name.
            <br>`subscription_custom_fields` - Returns custom field values
            nested within the subscription object. (Returns the subscription
            object regardless of whether `subscription` is requested.)
          required: false
          schema:
            type: array
            items:
              $ref: >-
                #/components/schemas/type_workspaces:PublicationsBySubscriptionEmailRequestExpandItem
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: >-
                    #/components/schemas/type_workspaces:PublicationsBySubscriptionEmailResponseItem
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '429':
          description: Rate Limit Exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:Error'
servers:
  - url: https://api.beehiiv.com/v2
components:
  schemas:
    type_workspaces:PublicationsBySubscriptionEmailRequestExpandItem:
      type: string
      enum:
        - subscription
        - publication
        - subscription_custom_fields
      title: PublicationsBySubscriptionEmailRequestExpandItem
    type_ids:PublicationId:
      type: string
      description: The prefixed ID of the publication.
      title: PublicationId
    type_ids:SubscriptionId:
      type: string
      description: The prefixed ID of the subscription.
      title: SubscriptionId
    type_:SubscriptionExpandedStatus:
      type: string
      enum:
        - validating
        - invalid
        - pending
        - active
        - inactive
        - needs_attention
        - paused
      description: >-
        The status of the subscription.<br>`validating` - The email address is
        being validated.<br>`invalid` - The email address is
        invalid.<br>`pending` - The email address is valid, but the subscription
        is pending double opt-in.<br>`active` - The email was valid and the
        subscription is active.<br>`inactive` - The subscription was made
        inactive, possibly due to an unsubscribe.<br>`needs_attention` - The
        subscription requires approval or denial.<br>`paused` - The subscriber
        has paused their subscription.
      title: SubscriptionExpandedStatus
    type_:ActiveSubscriptionCount:
      oneOf:
        - type: integer
        - type: boolean
      description: Total number of active free and premium subscriptions
      title: ActiveSubscriptionCount
    type_:ActivePremiumSubscriptionCount:
      oneOf:
        - type: integer
        - type: boolean
      description: Total number of active premium/paid subscriptions
      title: ActivePremiumSubscriptionCount
    type_:ActiveFreeSubscriptionCount:
      oneOf:
        - type: integer
        - type: boolean
      description: Total number of active free subscriptions
      title: ActiveFreeSubscriptionCount
    type_:AverageOpenRate:
      oneOf:
        - type: number
          format: double
        - type: boolean
      description: The publications historical average open rate
      title: AverageOpenRate
    type_:AverageClickRate:
      oneOf:
        - type: number
          format: double
        - type: boolean
      description: The publications historical average click through rate
      title: AverageClickRate
    type_:TotalEmailsSent:
      oneOf:
        - type: integer
        - type: boolean
      description: Total number of emails sent
      title: TotalEmailsSent
    type_:TotalUniqueOpens:
      oneOf:
        - type: integer
        - type: boolean
      description: >-
        Total number of uniquely opened emails. Only counts the first open for
        each subscriber.
      title: TotalUniqueOpens
    type_:TotalClicks:
      oneOf:
        - type: integer
        - type: boolean
      description: The total number of links clicked from emails.
      title: TotalClicks
    type_:PublicationStats:
      type: object
      properties:
        active_subscriptions:
          $ref: '#/components/schemas/type_:ActiveSubscriptionCount'
          description: Total number of active free and premium subscriptions
        active_premium_subscriptions:
          $ref: '#/components/schemas/type_:ActivePremiumSubscriptionCount'
          description: Total number of active premium/paid subscriptions
        active_free_subscriptions:
          $ref: '#/components/schemas/type_:ActiveFreeSubscriptionCount'
          description: Total number of active free subscriptions
        average_open_rate:
          $ref: '#/components/schemas/type_:AverageOpenRate'
          description: The publications historical average open rate
        average_click_rate:
          $ref: '#/components/schemas/type_:AverageClickRate'
          description: The publications historical average click through rate
        total_sent:
          $ref: '#/components/schemas/type_:TotalEmailsSent'
          description: Total number of emails sent
        total_unique_opened:
          $ref: '#/components/schemas/type_:TotalUniqueOpens'
          description: >-
            Total number of uniquely opened emails. Only counts the first open
            for each subscriber.
        total_clicked:
          $ref: '#/components/schemas/type_:TotalClicks'
          description: The total number of links clicked from emails.
      description: >-
        Optional list of stats for a publication. Retrievable by including an
        `expand` array in the publication request body. Add `"stats"` to the
        array to retrieve all, or add individual stats (prefaced with `stat_`)
        to only retrieve specific ones.


        Examples:

        {
          "expand": ["stats"]
        }


        {
          "expand": ["stat_active_subscriptions", "stat_average_click_rate"]
        }
      title: PublicationStats
    type_:Publication:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:PublicationId'
          description: A unique prefixed id of the publication
        name:
          type: string
          description: The name of the publication
        organization_name:
          type: string
          description: The name of the organization
        referral_program_enabled:
          type: boolean
          description: >-
            A boolean field indicating whether the referral program is active
            for this publication.
        created:
          type: number
          format: double
          description: >-
            The time that the publication was created. Measured in seconds since
            the Unix epoch
        stats:
          $ref: '#/components/schemas/type_:PublicationStats'
      required:
        - id
        - name
        - organization_name
        - referral_program_enabled
        - created
      title: Publication
    type_:SubscriptionExpandedSubscriptionTier:
      type: string
      enum:
        - free
        - premium
      description: The current tier of the subscription.
      title: SubscriptionExpandedSubscriptionTier
    type_:SubscriptionExpandedUtmChannel:
      type: string
      enum:
        - ''
        - website
        - import
        - embed
        - api
        - referral
        - recommendation
        - magic_link
        - boost
        - boost_send
        - boost_direct_link
        - integration
        - product
      description: The acquisition channel
      title: SubscriptionExpandedUtmChannel
    type_ids:TierId:
      type: string
      description: The prefixed ID of the tier.
      title: TierId
    type_:SubscriptionTierInfoStatus:
      type: string
      enum:
        - active
        - archived
      description: Returns whether or not the tier has any active prices.
      title: SubscriptionTierInfoStatus
    type_:SubscriptionTierInfo:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:TierId'
        name:
          type: string
        status:
          $ref: '#/components/schemas/type_:SubscriptionTierInfoStatus'
          description: Returns whether or not the tier has any active prices.
      required:
        - id
        - name
        - status
      title: SubscriptionTierInfo
    type_:SubscriptionTierList:
      type: array
      items:
        $ref: '#/components/schemas/type_:SubscriptionTierInfo'
      description: >-
        Optional list of tiers for a subscription. Retrievable by including
        `expand: [subscription_premium_tiers]` in the request body.
      title: SubscriptionTierList
    type_:CustomFieldType:
      type: string
      enum:
        - string
        - integer
        - boolean
        - date
        - datetime
        - list
        - double
      description: The type of value being stored in the custom field.
      title: CustomFieldType
    type_:CustomFieldDataType:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: boolean
        - type: array
          items:
            type: string
      title: CustomFieldDataType
    type_:CustomField:
      type: object
      properties:
        name:
          type: string
          description: The name of the existing custom field
        kind:
          $ref: '#/components/schemas/type_:CustomFieldType'
          description: The type of value being stored in the custom field.
        value:
          $ref: '#/components/schemas/type_:CustomFieldDataType'
          description: The value stored for the subscription
      title: CustomField
    type_:SubscriptionCustomFieldList:
      type: array
      items:
        $ref: '#/components/schemas/type_:CustomField'
      description: >-
        Optional list of custom fields for a subscription. Retrievable by
        including `expand: [custom_field]` in the request body.
      title: SubscriptionCustomFieldList
    type_:SubscriptionTags:
      type: array
      items:
        type: string
      description: >-
        Optional list of tags for a subscription. Retrievable by including
        `expand: [tags]` in the request body.

        Max limit of 100 unique tags per publication.
      title: SubscriptionTags
    type_:SubscriptionStats:
      type: object
      properties:
        emails_received:
          type: integer
          description: The total number of emails that have been sent to this subscriber
        open_rate:
          type: number
          format: double
          description: The percentage of emails that the subscriber has opened
        click_through_rate:
          type: number
          format: double
          description: The percentage of emails that the subscriber has clicked a link in
      description: >-
        Optional list of stats for a subscription. Retrievable by including
        `expand: [stats]` in the request body.
      title: SubscriptionStats
    type_:Subscription:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/type_ids:SubscriptionId'
          description: The prefixed subscription id
        email:
          type: string
          format: email
        status:
          $ref: '#/components/schemas/type_:SubscriptionExpandedStatus'
          description: >-
            The status of the subscription.<br>`validating` - The email address
            is being validated.<br>`invalid` - The email address is
            invalid.<br>`pending` - The email address is valid, but the
            subscription is pending double opt-in.<br>`active` - The email was
            valid and the subscription is active.<br>`inactive` - The
            subscription was made inactive, possibly due to an
            unsubscribe.<br>`needs_attention` - The subscription requires
            approval or denial.
        created:
          type: integer
          description: >-
            The date the subscription was created. Measured in seconds since the
            Unix epoch
        subscription_tier:
          $ref: '#/components/schemas/type_:SubscriptionExpandedSubscriptionTier'
          description: The current tier of the subscription.
        subscription_premium_tier_names:
          type: array
          items:
            type: string
          description: >-
            The current premium tiers of the subscription. Empty if the
            subscriber is not associated with any premium tiers.
        utm_source:
          type: string
          description: The acquisition source; where the subscriber came from
        utm_medium:
          type: string
          description: The acquisition medium; how the subscriber got to your publication
        utm_channel:
          $ref: '#/components/schemas/type_:SubscriptionExpandedUtmChannel'
          description: The acquisition channel
        utm_campaign:
          type: string
          description: The acquisition campaign
        utm_term:
          type: string
          description: The acquisition term; typically the keyword or search term
        utm_content:
          type: string
          description: >-
            The acquisition content; typically used for A/B testing or ad
            variations
        referring_site:
          type: string
          description: The website that the subscriber was referred from
        referral_code:
          type: string
          description: >-
            The code associated to this subscriber to refer others. When a new
            subscription is created with this referral code, credit for the
            referral goes to this subscription.
        subscription_premium_tiers:
          $ref: '#/components/schemas/type_:SubscriptionTierList'
        custom_fields:
          $ref: '#/components/schemas/type_:SubscriptionCustomFieldList'
        tags:
          $ref: '#/components/schemas/type_:SubscriptionTags'
        stats:
          $ref: '#/components/schemas/type_:SubscriptionStats'
      required:
        - id
        - email
        - status
        - created
        - subscription_tier
        - subscription_premium_tier_names
        - utm_source
        - utm_medium
        - utm_channel
        - utm_campaign
        - utm_term
        - utm_content
        - referring_site
        - referral_code
      description: The subscription object
      title: Subscription
    type_workspaces:PublicationsBySubscriptionEmailResponseItem:
      type: object
      properties:
        publication_id:
          $ref: '#/components/schemas/type_ids:PublicationId'
          description: The prefixed ID of the publication
        publication_name:
          type: string
          description: The name of the publication
        subscription_id:
          $ref: '#/components/schemas/type_ids:SubscriptionId'
          description: >-
            The prefixed ID of the subscription matching the email address for
            this publication
        status:
          $ref: '#/components/schemas/type_:SubscriptionExpandedStatus'
          description: >-
            The status of the subscription matching the email address for this
            publication
        publication:
          $ref: '#/components/schemas/type_:Publication'
          description: >-
            The full Publication object. Only present when `expand` includes
            `publication`.
        subscription:
          $ref: '#/components/schemas/type_:Subscription'
          description: >-
            The Subscription object matching the email address for this
            publication.  Only present when `expand` includes `subscription` or
            `subscription_custom_fields`.
      required:
        - publication_id
        - publication_name
        - subscription_id
        - status
      title: PublicationsBySubscriptionEmailResponseItem
    type_:ErrorDetail:
      type: object
      properties:
        message:
          type: string
        code:
          type: string
      required:
        - message
        - code
      title: ErrorDetail
    type_:Error:
      type: object
      properties:
        status:
          type: integer
        statusText:
          type: string
        errors:
          type: array
          items:
            $ref: '#/components/schemas/type_:ErrorDetail'
      required:
        - status
        - statusText
        - errors
      description: The top level error response.
      title: Error
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com"

querystring = {"expand":"[\"subscription\",\"publication\",\"subscription_custom_fields\"]"}

payload = {}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D';
const options = {
  method: 'GET',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

```python
import requests

url = "https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com"

querystring = {"expand":"[\"subscription\",\"publication\",\"subscription_custom_fields\"]"}

payload = {}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D';
const options = {
  method: 'GET',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

```python
import requests

url = "https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com"

querystring = {"expand":"[\"subscription\",\"publication\",\"subscription_custom_fields\"]"}

payload = {}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D';
const options = {
  method: 'GET',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.beehiiv.com/v2/workspaces/publications/by_subscription_email/bruce.wayne%40wayneenterprise.com?expand=%5B%22subscription%22%2C%22publication%22%2C%22subscription_custom_fields%22%5D")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

