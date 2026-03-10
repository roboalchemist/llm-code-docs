# Source: https://www.elastic.co/docs/deploy-manage/api-keys

﻿---
title: Elastic API keys
description: API keys are security mechanisms used to authenticate and authorize access to your deployments and Elasticsearch resources. They ensure that only authorized...
url: https://www.elastic.co/docs/deploy-manage/api-keys
products:
  - Elastic Cloud Enterprise
  - Elastic Cloud Hosted
  - Elastic Cloud Serverless
  - Elastic Cloud on Kubernetes
  - Elastic Stack
  - Elasticsearch
  - Kibana
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Cloud Hosted: Generally available
  - Elastic Cloud on Kubernetes: Generally available
  - Elastic Cloud Enterprise: Generally available
  - Self-managed Elastic deployments: Generally available
---

# Elastic API keys
API keys are security mechanisms used to authenticate and authorize access to your deployments and Elasticsearch resources.
They ensure that only authorized users or applications interact with these resources through [Elastic APIs](https://www.elastic.co/docs/api/).
For example, if you extract data from an Elasticsearch cluster on a daily basis, you might create an API key tied to your credentials, configure it with minimum access, and then put the API credentials into a cron job. Or you might create API keys to automate ingestion of new data from remote sources, without a live user interaction.
Depending on the APIs you want to use, the API keys to create are different, and managed at different locations:
- **[Elasticsearch API keys](https://www.elastic.co/docs/deploy-manage/api-keys/elasticsearch-api-keys)**, to use [Elasticsearch](https://www.elastic.co/docs/api/doc/elasticsearch/) and [Kibana](https://www.elastic.co/docs/api/doc/kibana/) APIs, and to manage remote cluster connections.
- **[Serverless project API keys](https://www.elastic.co/docs/deploy-manage/api-keys/serverless-project-api-keys)**, to use [Elasticsearch](https://www.elastic.co/docs/api/doc/elasticsearch-serverless/) and [Kibana](https://www.elastic.co/docs/api/doc/serverless/) serverless APIs.
- **[Elastic Cloud API keys](https://www.elastic.co/docs/deploy-manage/api-keys/elastic-cloud-api-keys)**, to manage your Elastic Cloud organization, Elastic Cloud Hosted deployments, and serverless projects using the [Elastic Cloud](https://www.elastic.co/docs/api/doc/cloud/) and [Elastic Cloud serverless](https://www.elastic.co/docs/api/doc/elastic-cloud-serverless/) APIs.
- **[Elastic Cloud Enterprise API keys](https://www.elastic.co/docs/deploy-manage/api-keys/elastic-cloud-enterprise-api-keys)**, to manage your Elastic Cloud Enterprise platform and deployments using the [Elastic Cloud Enterprise](https://www.elastic.co/docs/api/doc/cloud-enterprise/) API.