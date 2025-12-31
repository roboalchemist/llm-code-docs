# Source: https://docs.vespa.ai/en/basics/writing.html.md

# Writing

 

This is an introduction to writing data into Vespa.

## Documents

Once you have added one or more schemas to an application, and have added `<document-api>`in services.xml to the container cluster you want to handle writes, you can send writes following those schemas. A document is written as a JSON map containing a value for each field:

```
```
{
    "put": "id:my-namespace:my-documenttype::my-id-string",
    "fields": {
        "myTextField": "Hello world!",
        "myNumericAttribute": 13.8,
        "myEmbedding": [0.3, 1.45, 1.03]
    }
}
```
```

Each document has an id, which has two parts which can be decided freely:

- The **namespace**, which is just a string used to avoid name collisions if you have multiple kinds of clients deciding ids and not used for any other purpose 
- The **id string**, which can be any string you want, for example a product id or a url

Fields can remain empty; you do not need to set a value for every field defined in the document type.

You can find complete information on the document format in the[document JSON format reference](../reference/schemas/document-json-format.html).

## Writing documents

Documents are written to your application instances _write endpoint_, using the [document/v1](../writing/document-v1-api-guide.html) HTTP API. You can use the API directly, or use one of the clients provided by Vespa:

- **Command line, with [Vespa CLI](../clients/vespa-cli.html)**: `vespa feed mydoc.json/mydocs.jsonl` to feed one or many documents to Vespa.
- **Python, with [PyVespa](https://vespa-engine.github.io/pyvespa/):**`application.feed_iterable(...)`
- **Java, with the [Java Feed Client](../clients/vespa-feed-client.html):**`myFeedClient.put(id, json, params)`

Documents can also be removed, retrieved, and updated using the same API and clients.

## Updating documents

Documents can be fully replaced by a new version by writing them again, but you can also update any individual fields of existing documents. This is especially useful for updating attribute fields such as e.g. behavior signals or prices at high throughput, without impacting other fields and indexes.

Updates are sent in the same ways as document puts, it's just the format that's different:

```
```
{
    "update": "id:my-namespace:my-documenttype::my-id-string",
    "fields": {
        "myTextField": {
            "assign": "Some new value"
        }
    }
}
```
```

Updates can also increment numerical values, add to arrays and tensor etc., read more in the[partial update guide](../writing/partial-updates.html).

## Writes are streamed and realtime

Write operations to Vespa are streamed (using HTTP/2), and processed asynchronously. There is no need for a separate batch API to feed with the maximal throughput a system can handle, servers will push back by responding more slowly when they are close to saturation, and clients use this signal to back off, allowing them to dynamically converge at the maximal throughput a system can handle.

The write operations to Vespa are always applied in real time: When a write operation is asynchronously acknowledged, the write operation is persisted, fully processed and the result is visible in all subsequent queries. Vespa achieves this by a unique index design, combining in-memory mutable structures with and (for full-text) disk-backed posting lists.

Read more in the [feed sizing doc](../performance/sizing-feeding.html).

## The document API can also return documents

In addition to supporting writes, the document/v1 HTTP API can also return single documents by id (get), and stream any selection of a document corpus (visit). Visiting is used for background and one-time jobs such as backup and scraping content for offline machine learning. It is designed to have minimal impact on the running system rather than returning with low latency. Read more in[the document/v1 guide](../writing/document-v1-api-guide.html#data-dump).

  

#### Next: [Querying](querying.html)

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [Documents](#documents)
- [Writing documents](#writing-documents)
- [Updating documents](#updating-documents)
- [Writes are streamed and realtime](#writes-are-streamed-and-realtime)
- [The document API can also return documents](#the-document-api-can-also-return-documents)

