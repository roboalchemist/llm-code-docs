# Source: https://www.aptible.com/docs/how-to-guides/observability-guides/access-operation-logs.md

# How to access operation logs

> For all operations performed, Aptible collects operation logs. These logs are retained only for active resources and can be viewed in the following ways.

## Using the Dashboard

* Within the resource summary by:

  * Navigating to the respective resource

  * Selecting the **Activity** tab<img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/operation-logs1.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=748098a440a51de685946976802b205d" alt="" data-og-width="2800" width="2800" data-og-height="2000" height="2000" data-path="images/operation-logs1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/operation-logs1.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=9d04c7002f3837083495df2fe07246db 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/operation-logs1.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=7518108263f213fb35e92d84fd1d08dc 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/operation-logs1.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=4a5f256fafb322117eb7dc63bd3b824e 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/operation-logs1.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=96d030f0386fba0f54ca7f2533309702 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/operation-logs1.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=c9fb3840bd00ad4d422fec39ee18c430 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/operation-logs1.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=26fe2c3d31819af0dfaa38f90f18df54 2500w" />

  * Selecting **Logs**
* Within the **Activity** dashboard by:

  * Navigating to the **Activity** page

  * Selecting the **Logs** button for the respective operation

    * Note: This page only shows operations performed in the last 7 days.

## Using the CLI

* By using the [aptible operation:logs](/reference/aptible-cli/cli-commands/cli-operation-logs) command

  * Note: This command only shows operations performed in the last 90 days.
* For actively running operations, by using

  * [`aptible logs`](/core-concepts/observability/logs/overview) to stream all logs for an app or database
