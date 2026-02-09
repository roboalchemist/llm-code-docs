# Source: https://docs.apify.com/api/v2/actor-run-metamorph-post.md

# Metamorph run


```
POST 
https://api.apify.com/v2/actor-runs/:runId/metamorph
```


Transforms an Actor run into a run of another Actor with a new input.

This is useful if you want to use another Actor to finish the work of your current Actor run, without the need to create a completely new run and waiting for its finish.

For the users of your Actors, the metamorph operation is transparent, they will just see your Actor got the work done.

Internally, the system stops the Docker container corresponding to the Actor run and starts a new container using a different Docker image.

All the default storages are preserved and the new input is stored under the `INPUT-METAMORPH-1` key in the same default key-value store.

For more information, see the [Actor docs](https://docs.apify.com/platform/actors/development/programming-interface/metamorph).

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
