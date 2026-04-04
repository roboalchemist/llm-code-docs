# Source: https://render.com/docs/valkey-faq.md

# FAQ: Valkey on Render — New Render Key Value instances run Valkey instead of Redis®.

Render has adopted *Valkey* in place of Redis®<sup>\*</sup> for all newly created instances of [Render Key Value](key-value).

*Existing Redis instances continue operating as usual.* [See details below.](#what-will-happen-to-my-existing-redis-instances)

## FAQ

### What is Valkey?

[Valkey](https://valkey.io/) is an open-source key-value store that began as a fork of Redis version 7.2.4. For most applications and frameworks that connect to a Redis instance, Valkey is a drop-in replacement.

Valkey and Redis are completely independent projects that might diverge further over time.

### Why has Render adopted Valkey for new Key Value instances?

In 2024, the Redis project moved from the BSD 3-clause license to the [Redis Source Available License](https://redis.io/blog/redis-adopts-dual-source-available-licensing/). This change imposed restrictions on offering Redis as a managed service (and also led to the creation of the Valkey project).

Valkey immediately gained strong community backing, and it has established itself as the leading open-source Redis-compatible datastore. After comparing it against other available options, we believe Valkey provides the best combination of capabilities, compatibility, and community support for Render customers.

### How do I create a Valkey instance?

When you create a new Render Key Value instance, that instance automatically runs Valkey. The creation process is largely identical to the previous process for creating Redis instances.

In a `render.yaml` [Blueprint file](infrastructure-as-code), the values `keyvalue` and `redis` are equivalent for a service's [`type`](blueprint-spec#type) field: when used to create a new service, both values provision a Render Key Value instance that runs Valkey.

### What will happen to my existing Redis instances?

Existing Redis instances will continue operating as usual, with the following platform changes:

- *Redis instances will no longer receive version updates.*

  They will remain on version 6.2.14 indefinitely.

- *You cannot create _new_ Redis instances, with one exception:*

  [Preview environments](preview-environments) can create Redis instances as needed to accurately replicate your existing instances.

### Do I need to migrate my existing Redis instances to Valkey?

*No, but you're welcome to.* For the vast majority of Render users, Valkey is a drop-in replacement for Redis.

### Are there any changes to pricing?

*No.* Render Key Value instance types remain unchanged in both specs and pricing. The only difference is that new instances run Valkey instead of Redis.

Redis is a registered trademark of Redis Ltd. Any rights therein are reserved to Redis Ltd. Any use by Render Inc is for referential purposes only and does not indicate any sponsorship, endorsement or affiliation between Redis and Render Inc.