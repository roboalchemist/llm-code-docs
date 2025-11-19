# Source: https://docs.apify.com/platform/actors/development/builds-and-runs/runs.md

# Runs

**Learn about Actor runs, how to start them, and how to manage them.**

***

When you start an Actor, you create a run. A run is a single execution of your Actor with a specific input in a Docker container.

## Starting an Actor

You can start an Actor in several ways:

* Manually from the https://console.apify.com/actors UI
* Via the https://docs.apify.com/api/v2/act-runs-post.md
* Using the https://docs.apify.com/platform/schedules.md provided by the Apify platform
* By one of the available https://docs.apify.com/platform/integrations.md

## Input and environment variables

The run receives input via the `INPUT` record of its default https://docs.apify.com/platform/storage/key-value-store.md. Environment variables are also passed to the run. For more information about environment variables check the https://docs.apify.com/platform/actors/development/programming-interface/environment-variables.md section.

## Run duration and timeout

Actor runs can be short or long-running. To prevent infinite runs, you can set a timeout. The timeout is specified in seconds, and the default timeout varies based on the template from which you create your Actor. If the run doesn't finish within the timeout, it's automatically stopped, and its status is set to `TIMED-OUT`.
