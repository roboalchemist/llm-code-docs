# Source: https://redis.io/docs/latest/operate/rs/release-notes/index.html.md

# Source: https://redis.io/docs/latest/operate/rs/references/rest-api/index.html.md

# Source: https://redis.io/docs/latest/operate/rs/references/cli-utilities/redis-cli/index.html.md

# Source: https://redis.io/docs/latest/operate/rs/networking/port-configurations/index.html.md

# Source: https://redis.io/docs/latest/operate/rs/installing-upgrading/product-lifecycle/index.html.md

# Source: https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/hardware-requirements/index.html.md

# Source: https://redis.io/docs/latest/operate/rs/databases/connect/test-client-connectivity/index.html.md

# Source: https://redis.io/docs/latest/operate/rs/databases/connect/index.html.md

# Source: https://redis.io/docs/latest/operate/rs/index.html.md

# Source: https://redis.io/docs/latest/operate/redisinsight/install/index.html.md

# Source: https://redis.io/docs/latest/operate/rc/rc-quickstart/index.html.md

# Source: https://redis.io/docs/latest/operate/rc/databases/back-up-data/index.html.md

# Source: https://redis.io/docs/latest/operate/rc/index.html.md

# Source: https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/index.html.md

# Source: https://redis.io/docs/latest/operate/oss_and_stack/management/config/index.html.md

# Source: https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/index.html.md

# Source: https://redis.io/docs/latest/operate/kubernetes/index.html.md

# Source: https://redis.io/docs/latest/operate/index.html.md

# Source: https://redis.io/docs/latest/operate/rc/cloud-integrations/vercel/index.html.md

# Source: https://redis.io/docs/latest/integrate/riot/index.html.md

# Source: https://redis.io/docs/latest/integrate/redisvl/index.html.md

# Source: https://redis.io/docs/latest/integrate/redis-py/index.html.md

# Source: https://redis.io/docs/latest/integrate/redis-data-integration/index.html.md

# Source: https://redis.io/docs/latest/integrate/prometheus-with-redis-enterprise/prometheus-metrics-definitions/index.html.md

# Source: https://redis.io/docs/latest/integrate/index.html.md

# Source: https://redis.io/docs/latest/develop/use/patterns/distributed-locks/index.html.md

# Source: https://redis.io/docs/latest/develop/tools/redis-for-vscode/index.html.md

# Source: https://redis.io/docs/latest/develop/tools/insight/release-notes/index.html.md

# Source: https://redis.io/docs/latest/develop/tools/cli/index.html.md

# Source: https://redis.io/docs/latest/develop/reference/eviction/index.html.md

# Source: https://redis.io/docs/latest/develop/interact/search-and-query/indexing/index.html.md

# Source: https://redis.io/docs/latest/develop/interact/search-and-query/advanced-concepts/vectors/index.html.md

# Source: https://redis.io/docs/latest/develop/interact/search-and-query/index.html.md

# Source: https://redis.io/docs/latest/develop/data-types/index.html.md

# Source: https://redis.io/docs/latest/develop/clients/index.html.md

# Source: https://redis.io/docs/latest/develop/index.html.md

# Source: https://redis.io/docs/latest/commands/ttl/index.html.md

# Source: https://redis.io/docs/latest/commands/set/index.html.md

# Source: https://redis.io/docs/latest/commands/hset/index.html.md

# Source: https://redis.io/docs/latest/commands/get/index.html.md

# Source: https://redis.io/docs/latest/commands/expire/index.html.md

# Source: https://redis.io/docs/latest/commands/del/index.html.md

# Source: https://redis.io/docs/latest/commands/auth/index.html.md

# Source: https://redis.io/docs/latest/develop/get-started/index.html.md

# Source: https://redis.io/docs/latest/apis/index.html.md

# APIs

```json metadata
{
  "title": "APIs",
  "description": "An overview of Redis APIs for developers and operators",
  "categories": null,
  "tableOfContents": {"sections":[{"id":"apis-for-developers","title":"APIs for Developers","children":[{"id":"client-api","title":"Client API"},{"id":"programmability-apis","title":"Programmability APIs"}]},{"id":"apis-for-operators","title":"APIs for Operators","children":[{"id":"redis-cloud-api","title":"Redis Cloud API"},{"id":"redis-software-api","title":"Redis Software API"},{"id":"redis-enterprise-for-kubernetes-api","title":"Redis Enterprise for Kubernetes API"}]}]},
  "codeExamples": []
}
```




























Redis provides a number of APIs for developers and operators. The following sections provide you easy access to the client API, the several programmability APIs, the RESTFul management APIs and the Kubernetes resource definitions.

## APIs for Developers

### Client API

Redis comes with a wide range of commands that help you to develop real-time applications. You can find a complete overview of the Redis commands here:

- [Redis commands](https://redis.io/docs/latest/commands/)

As a developer, you will likely use one of our supported client libraries for connecting and executing commands.

- [Connect with Redis clients introduction](https://redis.io/docs/latest/develop/clients)

### Programmability APIs

The existing Redis commands cover most use cases, but if low latency is a critical requirement, you might need to extend Redis' server-side functionality.

Lua scripts have been available since early versions of Redis. With Lua, the script is provided by the client and cached on the server side, which implies the risk that different clients might use a different script version.

- [Redis Lua API reference](https://redis.io/docs/latest/develop/programmability/lua-api)
- [Scripting with Lua introduction](https://redis.io/docs/latest/develop/programmability/eval-intro)

The Redis functions feature, which became available in Redis 7, supersedes the use of Lua in prior versions of Redis. The client is still responsible for invoking the execution, but unlike the previous Lua scripts, functions can now be replicated and persisted.

- [Functions and scripting in Redis 7 and beyond](https://redis.io/docs/latest/develop/programmability/functions-intro)

If none of the previous methods fulfills your needs, then you can extend the functionality of Redis with new commands using the Redis Modules API. 

- [Redis Modules API introduction](https://redis.io/docs/latest/develop/reference/modules/)
- [Redis Modules API reference](https://redis.io/docs/latest/develop/reference/modules/modules-api-ref)

## APIs for Operators

### Redis Cloud API
Redis Cloud is a fully managed Database as a Service offering and the fastest way to deploy Redis at scale. You can programmatically manage your databases, accounts, access, and credentials using the Redis Cloud REST API.

- [Redis Cloud REST API introduction](https://redis.io/docs/latest/operate/rc/api/)
- [Redis Cloud REST API examples](https://redis.io/docs/latest/operate/rc/api/examples/)
- [Redis Cloud REST API reference](https://redis.io/docs/latest/operate/rc/api/api-reference)


### Redis Software API
If you have installed Redis Software, you can automate operations with the Redis Software REST API.

- [Redis Software REST API introduction](https://redis.io/docs/latest/operate/rs/references/rest-api/)
- [Redis Software REST API requests](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/)
- [Redis Software REST API objects](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/)


### Redis Enterprise for Kubernetes API

If you need to install Redis Enterprise on Kubernetes, then you can use the [Redis Enterprise for Kubernetes Operators](https://redis.io/docs/latest/operate/Kubernetes/). You can find the resource definitions here:

- [Redis Enterprise Cluster API](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_cluster_api)
- [Redis Enterprise Database API](https://redis.io/docs/latest/operate/kubernetes/reference/api/redis_enterprise_database_api)
