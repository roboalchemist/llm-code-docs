# Source: https://render.com/docs/deploy-elasticsearch.md

# Deploy Elasticsearch

Elasticsearch is a popular open source search server used to index and query documents efficiently over a simple HTTP interface. [Render Disks](disks) make it effortless to deploy production-grade Elasticsearch on Render.

This guide shows how to deploy a single node Elasticsearch instance as a [private service](private-services) that is only exposed to other Render services in your account, and can't be accessed over the Internet. Let's get started!

## One-Click Deploy

Click *Deploy to Render* below and follow the prompts to set up a single node Elasticsearch instance on Render.

<deploy-to-render repo="https://github.com/render-examples/elasticsearch">
</deploy-to-render>

## Manual Deploy

1. Fork `render-examples/elasticsearch` on [GitHub](https://github.com/render-examples/elasticsearch) or [GitLab](https://gitlab.com/render-examples/elasticsearch).

2. Create a new *Private Service* on Render, and give Render permission to access your new repo.

3. Set the *Language* field to `Docker` and add the following environment variables:

   | Key              | Value               |
   | ---------------- | ------------------- |
   | `ES_JAVA_OPTS`   | `-Xms256m -Xmx256m` |
   | `discovery.type` | `single-node`       |

   If you upgrade your instance type to increase memory, remember to change the `ES_JAVA_OPTS` environment variable to [at most 50%](https://www.elastic.co/guide/en/elasticsearch/reference/current/heap-size.html) of the new limit.
   Elasticsearch generally needs more memory than is available with our Starter Plan, especially for production use.

4. Add a Disk under *Advanced* with the following values:

   |                |                                                      |
   | -------------- | ---------------------------------------------------- |
   | *Mount Path* | `/usr/share/elasticsearch/data`                      |
   | *Size*       | `10 GB` Feel free to change this to suit your needs. |

That's it! Save your private service to bring up Elasticsearch which will take a few minutes to start. Future deploy should be much faster.

Your Elasticsearch instance will be available on your private service URL as soon as the deploy is live. The URL should look like `elastic:9200`.

[image: Elastic]

You can then open the shell in your service dashboard to interact with Elasticsearch using the private service name and port.

```bash
[elasticsearch@elastic-fk6lt ~]$ curl elastic:9200
{
  "name" : "srv-bkv1tdfn59aidtakhgj0-756c7b77bc-fk6lt",
  "cluster_name" : "docker-cluster",
  "cluster_uuid" : "QRHHttswQPqcm5i9PKhBIA",
  "version" : {
    "number" : "7.3.0",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "508c38a",
    "build_date" : "2019-06-20T15:54:18.811730Z",
    "build_snapshot" : false,
    "lucene_version" : "8.0.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

You can also connect to Elasticsearch from your application using the name and port for your new service. Learn more about [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html).