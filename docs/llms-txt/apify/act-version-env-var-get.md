# Source: https://docs.apify.com/api/v2/act-version-env-var-get.md

# Get environment variable


```
GET 
https://api.apify.com/v2/acts/:actorId/versions/:versionNumber/env-vars/:envVarName
```


Clientshttps://docs.apify.com/api/client/python/reference/class/ActorEnvVarClientAsync#getGets a  that contains all the details about a specific environment variable of an Actor.

If `isSecret` is set to `true`, then `value` will never be returned.

## Request

## Responses

* 200

**Response Headers**

