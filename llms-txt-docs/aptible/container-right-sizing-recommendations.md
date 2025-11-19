# Source: https://www.aptible.com/docs/core-concepts/scaling/container-right-sizing-recommendations.md

# Container Right-Sizing Recommendations

> Learn about using the in-app Container Right-Sizing Recommendations for performance and optimization

<Frame>
    <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scaling-recs.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=3101638da52d36dcb085e8a996aad852" alt="" data-og-width="2240" width="2240" data-og-height="1260" height="1260" data-path="images/scaling-recs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scaling-recs.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=b3634f2733c3de4ede2388c0e05998d9 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scaling-recs.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=dc2b7c394a1abca7dbd607d867987147 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scaling-recs.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=48a94aa3e899e669e51c8458083a91ae 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scaling-recs.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=4d21eddcd6f1c6c6d514a731a76edb32 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scaling-recs.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=8d87bbba0e0325ca5a94b5db15defdcf 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scaling-recs.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=753cb444f03df0ea1668e4c782edcb4d 2500w" />
</Frame>

# Overview

Container Right-Sizing Recommendations are shown in the Aptible Dashboard for App Services and Databases. For each resource, one of the following scaling recommendations will show:

* Rightsized, indicating optimal performance and cost efficiency

* Scale Up, recommending increased resources to meet growing demand

* Scale Down, recommending a reduction to avoid overspending

* Auto-scaling, indicating that vertical scaling is happening automatically

Recommendations are updated daily based on the last two weeks of data, and provide vertical scaling recommendations for optimal container size and profile. Use the auto-fill button to apply recommended changes with a single click!

To begin using this feature, navigate to the App Services or Database index page in the Aptible Dashboard and find the `Scaling Recs` column. Additionally, you will find a banner on the App Service and Database Scale pages where Aptible also provides the recommendation.

# How does Aptible make manual vertical scale right-sizing recommendations?

Here are the key details of how the recommendations are generated:

* Aptible looks at the App and Database metrics within the last **14 days**

* There are two primary metrics:

  * CPU usage: **95th percentile** within the time window

  * RAM usage: **max RSS value** within the time window

* For specific databases, Aptible will modify the current RAM usage:

  * When PostgreSQL, MySQL, MongoDB: make a recommendation based on **30% of max RSS value** within the time window

  * When Elasticsearch, Influxdb: make a recommendation based on **50% of max RSS
    value** within the time window

* Then, Aptible finds the most optimial [Container Profile](https://www.aptible.com/docs/core-concepts/scaling/container-profiles) and size that fits within the
  CPU and RAM usage:

  * If the recommended cost savings is less than \$150/mo, Aptible won't offer the
    recommendation

  * If the recommended container size change is a single step down (e.g.
    downgrade from 4GB to 2GB), Aptible won't offer the recommendation

# Why does Aptible increase the RAM usage for certain databases?

For some databases, the maintainers recommend having greater capacity than what
is currently being used.  Therefore, Aptible has unique logic that allows those databases to
adhere to their recommendations. We have a section specifically about [Understanding Memory Utilization](https://www.aptible.com/docs/core-concepts/scaling/memory-limits#understanding-memory-utilization) where you can learn more.

Because Aptible does not have knowledge of how these databases are being used, we have
to make best guesses and use the most common use cases to set sane defaults for the
databases we offer as well as our right-sizing recommendations.

### PostgreSQL

We set the manual recommendations to scale based on **30% of the max RSS
value** within the time window. This means if a PostgreSQL database uses more than 30% of the available memory, Aptible will recommend a scale-up and, conversely, scaling down.

We make this recommendation based on setting the `shared_buffers` to 25% of the
total RAM, which is the [recommended starting value](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-SHARED-BUFFERS):

> If you have a dedicated database server with 1GB or more of RAM, a reasonable starting value for shared\_buffers is 25% of the memory in your system.

Other References:

* [https://www.geeksforgeeks.org/postgresql-memory-management/](https://www.geeksforgeeks.org/postgresql-memory-management/)

* [https://www.enterprisedb.com/postgres-tutorials/how-tune-postgresql-memory](https://www.enterprisedb.com/postgres-tutorials/how-tune-postgresql-memory)

### MySQL

We set the manual recommendations to scale based on **30% of the max RSS
value** within the time window.

We make this recommendation based on setting the `innodb_buffer_pool_size` to
50% of the total RAM.

From the MySQL[ docs](https://dev.mysql.com/doc/refman/8.4/en/innodb-parameters.html#sysvar_innodb_buffer_pool_size):

> A larger buffer pool requires less disk I/O to access the same table data more than once. On a dedicated database server, you might set the buffer pool size to 80% of the machine's physical memory size.

### MongoDB

We set the manual recommendations to scale based on **30% of the max RSS
value** within the time window.

We make this recommendation based on the [default WiredTiger internal cache set
to 50% of total RAM - 1GB](https://www.mongodb.com/docs/manual/administration/production-notes/#allocate-sufficient-ram-and-cpu):

> With WiredTiger, MongoDB utilizes both the WiredTiger internal cache and the filesystem cache. The default WiredTiger internal cache size is the larger of either: 50% of (RAM - 1 GB), or 256 MB.

### ElasticSearch

We set the manual recommendations to scale based on **50% of the max RSS
value** within the time window.

We make this recommendation based on [setting the heap size 50% of total RAM](https://www.elastic.co/guide/en/elasticsearch/guide/master/heap-sizing.html#_give_less_than_half_your_memory_to_lucene):

> The standard recommendation is to give 50% of the available memory to Elasticsearch heap, while leaving the other 50% free. It won’t go unused; Lucene will happily gobble up whatever is left over.

Other References:

* [https://www.elastic.co/guide/en/elasticsearch/reference/current/advanced-configuration.html#set-jvm-heap-size](https://www.elastic.co/guide/en/elasticsearch/reference/current/advanced-configuration.html#set-jvm-heap-size)
