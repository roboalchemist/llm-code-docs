# Source: https://docs.apify.com/platform/actors/development/programming-interface/status-messages.md

# Status messages

**Learn how to use custom status messages to inform users about an Actor's progress.**

<!-- -->

***

Each Actor run has a status, represented by the `status` field. The following table describes the possible values:

| Status       | Type         | Description                                 |
| ------------ | ------------ | ------------------------------------------- |
| `READY`      | initial      | Started but not allocated to any worker yet |
| `RUNNING`    | transitional | Executing on a worker                       |
| `SUCCEEDED`  | terminal     | Finished successfully                       |
| `FAILED`     | terminal     | Run failed                                  |
| `TIMING-OUT` | transitional | Timing out now                              |
| `TIMED-OUT`  | terminal     | Timed out                                   |
| `ABORTING`   | transitional | Being aborted by user                       |
| `ABORTED`    | terminal     | Aborted by user                             |

## Status messages

In addition to the status, each Actor run has a status message (the `statusMessage` field). This message informs users about the Actor's current activity, enhancing the user experience.

![Status message](/assets/images/status-message-5a087d1952b6d9050f089ca946bffba5.png)

## Exit status message

When an Actor exits, the status message is set to either:

* A default text (e.g., *Actor finished with exit code 1*)
* A custom message (see the https://docs.apify.com/platform/actors/development/programming-interface/basic-commands.md#exit-actor method for details)

## Update status message

To keep users informed during the Actor's execution, update the status message periodically. Use the following code to set a status message:

* JavaScript
* Python


```
import { Actor } from 'apify';

await Actor.init();

// ...
await Actor.setStatusMessage('Crawled 45 of 100 pages');

await Actor.exit();
```


Update frequency

You can call the `setStatusMessage` function as often as needed. The SDK only invokes the API if the status changes, simplifying usage.


```
from apify import Actor

async def main():
    async with Actor:
        await Actor.set_status_message('Crawled 45 of 100 pages')
        # INFO  [Status message]: Crawled 45 of 100 pages
```
