# Source: https://www.aptible.com/docs/how-to-guides/observability-guides/elk.md

# How to set up a self-hosted Elasticsearch Log Drain with Logstash and Kibana (ELK)

> This guide will walk you through setting up a self-hosted Elasticsearch - Logstash - Kibana (ELK) stack on Aptible.

## Create an Elasticsearch database

Use the [`aptible db:create`](/reference/aptible-cli/cli-commands/cli-db-create) command to create a new [Elasticsearch](/core-concepts/managed-databases/supported-databases/elasticsearch) Database:

```
aptible db:create "$DB_HANDLE" --type elasticsearch
```

> 📘 Add the `--disk-size X` option to provision a larger-than-default Database.

## Set up a log drain

**Step 1:** In the Aptible dashboard, create a new [log drain](/core-concepts/observability/logs/log-drains/overview):

<img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk1.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=5af6301121eb961b304a3589b65a2207" alt="" data-og-width="1280" width="1280" data-og-height="883" height="883" data-path="images/elk1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk1.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=8ea1ab0e5d35ef28577a679aae927ab2 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk1.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=e7df183c28a5d894735d1e23352e3b0b 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk1.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=0582196e515125cde85877a9425fb6c2 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk1.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=eb0c0551e791bf86dea2055d90a86498 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk1.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=e52b919c79c73db80d0980b1bba0d8a2 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk1.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=d12dd4e7dee70602c6e2e0fc5da93354 2500w" />

**Step 2:** Select Elasticsearch as the destination

<img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk2.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=d0eba7c968929ecedf50582b6275fa8d" alt="" data-og-width="1280" width="1280" data-og-height="883" height="883" data-path="images/elk2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk2.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=75ed0f2197bde35a04d87a8db76ed801 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk2.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=2ff51e7d111f97622ae0a1723a8c40e3 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk2.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=9080b95badbe0d35cc4e62028605d2c6 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk2.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=b879232109855f596f80b0c761d95aae 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk2.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=f90e62e93dce82eb69c4a605b8d2c39e 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk2.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=bc948732faac0c5abd77a45754d5aa1a 2500w" />

**Step 3:** Save the Log Drain:

<img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk4.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=9bacc9bacede847b9c7fb9437575ce84" alt="" data-og-width="1280" width="1280" data-og-height="883" height="883" data-path="images/elk4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk4.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=118c9176c404a75fb221bc8db4062dff 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk4.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=addd38e4f4a4f2a40b78b8b06f2d4400 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk4.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=cc6f59f3441955ebcea8853c90e33044 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk4.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=a830f1ef59735af15d259302c667a811 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk4.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=d11774e73244c6c09755bc6a676f004f 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/elk4.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=a4e88f43ca446ae93a0e9d601d98d2a4 2500w" />

## Set up Kibana

Kibana is an open-source, browser-based analytics and search dashboard for Elasticsearch. Follow our [Running Kibana](/how-to-guides/observability-guides/setup-kibana) guide to deploying Kibana on Aptible.

## Set up Log Rotation

If you let logs accumulate in Elasticsearch, you'll need more and more RAM and disk space to store them. To avoid this, set up log archiving. We recommend archiving logs to S3. Follow the instructions in our [Elasticsearch Log Rotation](/how-to-guides/observability-guides/elasticsearch-log-rotation) guide.
