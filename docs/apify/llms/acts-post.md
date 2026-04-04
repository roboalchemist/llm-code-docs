# Source: https://docs.apify.com/api/v2/acts-post.md

# Create Actor


```
POST 
https://api.apify.com/v2/acts
```


Creates a new Actor with settings specified in an Actor object passed as JSON in the POST payload. The response is the full Actor object as returned by the  endpoint.

The HTTP request must have the `Content-Type: application/json` HTTP header!

The Actor needs to define at least one version of the source code. For more information, see .

If you want to make your Actor [public](https://docs.apify.com/platform/actors/publishing) using `isPublic: true`, you will need to provide the Actor's `title` and the `categories` under which that Actor will be classified in Apify Store. For this, it's best to use the [constants from our apify-shared-js package](https://github.com/apify/apify-shared-js/blob/2d43ebc41ece9ad31cd6525bd523fb86939bf860/packages/consts/src/consts.ts#L452-L471).

## Request

## Responses

* 201
* 400

**Response Headers**

* **Location**

Bad request - invalid input parameters or request body.
