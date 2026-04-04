# Source: https://docs.api7.ai/apisix/key-concepts/consumer-groups.md

# Consumer Groups

In this document, you will learn the basic concept of consumer groups in APISIX and their common use cases. You will be introduced to a few relevant concepts, including how to pass consumer group information to upstream and consumer group access restriction.

Explore additional resources at the end of the document for more information on related topics.

## Overview[â](#overview "Direct link to Overview")

In APISIX, a *consumer group* corresponds to a group of [consumers](https://docs.api7.ai/apisix/key-concepts/consumers.md) sharing the same [plugin](https://docs.api7.ai/apisix/key-concepts/plugins.md) configurations, such as access control and rate limiting policies. Consumers can be added to a consumer group by referring to the consumer group ID in their configurations. This allows for easier management of APIs and helps to reduce redundancies in consumer configurations.

A few sample use cases of consumer groups are:

* Implementing API monetization with different pricing models
* Implementing [role-based access control (RBAC)](https://en.wikipedia.org/wiki/Role-based_access_control) for different roles, such as admins, developers, and guests
* Grouping consumers based on other shared functionalities

The following diagram illustrates the concept of consumer groups with an API monetization example that has three consumers, `John`, `Jane`, and `Bot`. John and Jane are human consumers in the **basic plan** that share a lower API quota, and the bot is in the **premium plan** with a higher API quota:

![Consumer groups of basic plan and premium plan](https://static.api7.ai/uploads/2024/12/12/VMcONfw0_consumer_groups.svg)

By using consumer groups, you do not need to repetitively configure [`limit-count`](https://docs.api7.ai/hub/limit-count.md) on each consumer.

## Passing Consumer Group Information to Upstream[â](#passing-consumer-group-information-to-upstream "Direct link to Passing Consumer Group Information to Upstream")

Similar to [passing consumer information to upstream](https://docs.api7.ai/apisix/key-concepts/consumers.md#passing-consumer-information-to-upstream), you can use [`proxy-rewrite`](https://docs.api7.ai/hub/proxy-rewrite.md) plugin on consumer groups to include the needed information in the header:

```
{
  "plugins":{
    ...,
    "proxy-rewrite":{
      "headers":{
        "set":{
          "X-Consumer-Group-ID":"$consumer_group_id"
        }
      }
    }
  }
}
```

## Consumer Group Access Restriction[â](#consumer-group-access-restriction "Direct link to Consumer Group Access Restriction")

You can control request access to your API by imposing restrictions based on consumer group ID, HTTP methods, or other parameters in the `consumer-restriction` plugin.

For example, if you want to strictly restrict the HTTP method for a consumer group called `cg-data-uploading` to use PUT, you can update the plugin's configuration as follows:

```
{
  "plugins":{
    ...,
    "consumer-restriction":{
      "type":"consumer_group_id",
      "allowed_by_methods":[
        {
          "user":"cg-data-uploading",
          "methods":["PUT"]
        }
      ]
    }
  }
}
```

The [`consumer-restriction`](https://docs.api7.ai/hub/consumer-restriction.md) plugin can also be used with [consumers](https://docs.api7.ai/apisix/key-concepts/consumers.md), [routes](https://docs.api7.ai/apisix/key-concepts/routes.md), [services](https://docs.api7.ai/apisix/key-concepts/services.md), and [consumer groups](https://docs.api7.ai/apisix/key-concepts/consumer-groups.md).

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts

  <!-- -->

  * [Consumers](https://docs.api7.ai/apisix/key-concepts/consumers.md)
  * [Credentials](https://docs.api7.ai/apisix/key-concepts/credentials.md)

* Admin API - [Consumer Groups](https://docs.api7.ai/apisix/reference/admin-api/.md#tag/Consumer-Group)
