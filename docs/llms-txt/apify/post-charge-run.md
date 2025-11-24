# Source: https://docs.apify.com/api/v2/post-charge-run.md

# Charge events in run


```
POST 
https://api.apify.com/v2/actor-runs/:runId/charge
```


Clientshttps://docs.apify.com/api/client/python/reference/class/RunClientAsync#chargehttps://docs.apify.com/api/client/js/reference/class/RunClient#chargeCharge for events in the run of your https://docs.apify.com/platform/actors/running/actors-in-store#pay-per-event. The event you are charging for must be one of the configured events in your Actor. If the Actor is not set up as pay per event, or if the event is not configured, the endpoint will return an error. The endpoint must be called from the Actor run itself, with the same API token that the run was started with.

Learn more about pay-per-event pricing

For more details about pay-per-event (PPE) pricing, refer to our https://docs.apify.com/platform/actors/publishing/monetize/pay-per-event.md.

## Request

## Responses

* 201

The charge was successful. Note that you still have to make sure in your Actor that the total charge for the run respects the maximum value set by the user, as the API does not check this. Above the limit, the charges reported as successful in API will not be added to your payouts, but you will still bear the associated costs. Use the Apify charge manager or SDK to avoid having to deal with this manually.
