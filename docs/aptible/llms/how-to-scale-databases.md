# Source: https://www.aptible.com/docs/how-to-guides/database-guides/how-to-scale-databases.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to scale databases

> Learn how to scale databases on Aptible

## Overview

Aptible [Databases](/core-concepts/managed-databases/managing-databases/overview) can be manually scaled with minimal downtime (typically less than 1 minute). There are several elements of databases that can be scaled, such as CPU, RAM, IOPS, and throughput. See [Database Scaling](/core-concepts/scaling/database-scaling) for more information.

## Using the Aptible Dashboard

Databases can be scaled within the Aptible Dashboard by:

* Navigating to the Environment in which your Database lives in

* Selecting the **Databases** tab

* Selecting the respective Database

* Selecting **Scale**

<img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scale-databases1.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=0bfef33c650941ff9e030c749b671464" alt="" data-og-width="2800" width="2800" data-og-height="2228" height="2228" data-path="images/scale-databases1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scale-databases1.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=5c0b185728158cdd8ffc3c806d215cd3 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scale-databases1.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=00d55000e8fc9c2abd5374848421f81d 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scale-databases1.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=6f52e4ea25b90da920157bfbe8612432 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scale-databases1.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=31976efd5e4fa3635750dbd90321c80b 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scale-databases1.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=0542adc2f5532e841315faa281bf1186 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scale-databases1.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=b2f76ec14e172d256ecf613fc59b58f8 2500w" />

## Using the CLI

Databases can be scaled via the Aptible CLI using the [`aptible db:restart`](/reference/aptible-cli/cli-commands/cli-db-restart) command.

## Using Terraform

Databases can be programmatically scaled using the Aptible [Terraform Provider](https://registry.terraform.io/providers/aptible/aptible/latest/docs) using the `terraform_aptible_database` resource:

```js  theme={null}
 resource "aptible_database" "DATABASE" {
    env_id = ENVIRONMENT_ID
    handle = "DATABASE_HANDLE"
    database_type = "redis"
    container_size = 512
    disk_size = 10
}
```
