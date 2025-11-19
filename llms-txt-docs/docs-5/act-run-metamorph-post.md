# Source: https://docs.apify.com/api/v2/act-run-metamorph-post.md

# Metamorph run


```
POST 
https://api.apify.com/v2/acts/:actorId/runs/:runId/metamorph
```


deprecated

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

**\[DEPRECATED]** API endpoints related to run of the Actor were moved under new namespace .Transforms an Actor run into a run of another Actor with a new input.

This is useful if you want to use another Actor to finish the work of your current Actor run, without the need to create a completely new run and waiting for its finish. For the users of your Actors, the metamorph operation is transparent, they will just see your Actor got the work done.

There is a limit on how many times you can metamorph a single run. You can check the limit in https://docs.apify.com/platform/limits#actor-limits.

Internally, the system stops the Docker container corresponding to the Actor run and starts a new container using a different Docker image. All the default storages are preserved and the new input is stored under the `INPUT-METAMORPH-1` key in the same default key-value store.

For more information, see the https://docs.apify.com/platform/actors/development/programming-interface/metamorph.

## Request

## Responses

* 200

**Response Headers**

