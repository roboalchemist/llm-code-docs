# Source: https://docs.apify.com/platform/limits.md

# Limits

**Learn the Apify platform's resource capability and limitations such as max memory, disk size and number of Actors and tasks per user.**

***

The tables below demonstrate the Apify platform's default resource limits. For API limits such as rate limits and max payload size, see the [API documentation](https://docs.apify.com/api/v2.md#rate-limiting).

> If needed, the limits shown below can be increased on paid accounts. For details, contact us at **[hello@apify.com](mailto:hello@apify.com)** or using the chat in [Apify Console](https://console.apify.com/) under the "Help & Resources → Contact Support".

## Actor runtime limits

| Description                                 | Limit for plan        |           |            |          |
| ------------------------------------------- | --------------------- | --------- | ---------- | -------- |
|                                             | Free                  | Starter   | Scale      | Business |
| Build memory size                           | 4,096 MB              |           |            |          |
| Run minimum memory                          | 128 MB                | 128 MB    |            |          |
| Run maximum memory                          | 8,192 MB              | 32,768 MB |            |          |
| Maximum combined memory of all running jobs | 8,192 MB              | 32,768 MB | 131,072 MB |          |
| Build timeout                               | 1800 secs             |           |            |          |
| Build/run disk size                         | 2× job memory limit   |           |            |          |
| Memory per CPU core                         | 4,096 MB              |           |            |          |
| Maximum log size                            | 10,485,760 characters |           |            |          |
| Maximum number of metamorphs                | 10 metamorphs per run |           |            |          |

## Apify platform limits

| Description                                                            | Limit for plan |         |       |          |
| ---------------------------------------------------------------------- | -------------- | ------- | ----- | -------- |
|                                                                        | Free           | Starter | Scale | Business |
| Maximum number of dataset columns for tabular formats (XLSX, CSV, ...) | 2000 columns   |         |       |          |
| Maximum size of Actor input schema                                     | 500 kB         |         |       |          |
| Maximum number of Actors per user                                      | 100            |         |       |          |
| Maximum number of tasks per user                                       | 1000           |         |       |          |
| Maximum number of schedules per user                                   | 100            |         |       |          |
| Maximum number of webhooks per user                                    | 100            |         |       |          |
| Maximum number of Actors per schedule                                  | 10             |         |       |          |
| Maximum number of tasks per schedule                                   | 10             |         |       |          |
| Maximum number of concurrent Actor runs per user                       | 25             | 32      | 128   | 256      |

## Usage limit

The Apify platform also introduces usage limits based on the billing plan to protect users from accidental overspending. To learn more about usage limits, head over to the [Limits](https://docs.apify.com/platform/console/billing.md#limits) section of our docs.

View these limits and adjust your maximum usage limit in [Apify Console](https://console.apify.com/billing#/limits):

![](/assets/images/usage-limits-2b0ebb13462f1d8122148611409b965a.png "Apify Security Whitepaper")
