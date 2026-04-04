# after
{
 someReference {
    name
  }
}
```

*   In our Mutation API, we renamed the following:
    
    *   `transaction` is now `transactionAsync`
        
    *   `transactionAwaitable` is now `transaction`
        

note:

A bit confusing, yes, but we found that `transactionAwaitable` (which executed the transaction and responded with the result) was much more useful than the old `transaction`, which fired off a job and then it was up to the developer to poll for the `transactionStatus`. The name "transactionAwaitable" was a poorly thought out name, and we've taken the opportunity of a breaking version to fix this.

## Analytics → Events

We’ve renamed the `/analytics` entrypoint to `/events`

```
import { sendEvent, getEventCount } from 'basehub/analytics'
import { sendEvent, getEvents } from 'basehub/events'
```

That should be all!