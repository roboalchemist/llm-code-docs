# Source: https://www.aptible.com/docs/how-to-guides/app-guides/how-to-scale-apps-services.md

# How to scale apps and services

Learn how to manually scale apps and services on Aptible

## Overview

[Apps](/core-concepts/apps/overview) can be scaled on a [Service](/core-concepts/apps/deploying-apps/services)-by-Service basis: any given Service for your App can be scaled independently of others.

## Using the Dashboard

* Within the Aptible Dashboard apps and services can be manually scaled by:

  * Navigating to the Environment in which your App lives

  * Selecting the **Apps** tab

  * Selecting the respective App

  * Selecting **Scale**

<img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scale-apps1.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=f9d711d789234e64a98a2b1ba408a388" alt="" data-og-width="2800" width="2800" data-og-height="2000" height="2000" data-path="images/scale-apps1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scale-apps1.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=c9645e6da1ca87768a91ed0b4eab3f7c 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scale-apps1.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=47b3c3602bd9c92629978ce082265fac 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scale-apps1.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=b444c90bff4742133877a6c1a32ab43e 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scale-apps1.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=d56cde924b4b16a7d37d7ddd0e8f79ea 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scale-apps1.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=cb953aaec22d49f61a3e0147dc334c09 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scale-apps1.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=7f08ef17bd1ca014113f76e1a8ac1731 2500w" />

## Using the CLI

Apps and services can be manually scaled via the Aptible CLI using the [`aptible apps:scale`](/reference/aptible-cli/cli-commands/cli-apps-scale) command.

## Using Terraform

Apps and services can be scaled programmatically via Aptible [Terraform Provider](https://registry.terraform.io/providers/aptible/aptible/latest/docs) by using the nested service element for the App resource:

```js  theme={null}
resource "aptible_app" "APP" {
    env_id = ENVIRONMENT_ID
    handle = "APP_HANDLE"
    service {
        process_type = "SERVICE_NAME1"
        container_count = 1
        container_memory_limit = 1024
    }
    service {
        process_type = "SERVICE_NAME2"
        container_count = 2
        container_memory_limit = 2048
    }
}
```
