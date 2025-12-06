# Source: https://docs.vespa.ai/en/writing/batch-delete.html.md

# Batch delete

 

Options for batch deleting documents:

1. Use [vespa feed](../clients/vespa-cli.html#documents):
```
$ vespa feed -t my-endpoint deletes.json
```
2. Find documents using a query, delete, repeat. Pseudocode:
```
while True; do
   query and read document ids, if empty exit
   delete document ids using[/document/v1](../reference/api/document-v1.html#delete)wait a sec # optional, add wait to reduce load while deleting
```
3. Use a [document selection](../schemas/documents.html#document-expiry) to expire documents. This deletes all documents _not_ matching the expression. It is possible to use parent documents and imported fields for expiry of a document set. The content node will iterate over the corpus and delete documents (that are later compacted out):
```
```
<documents garbage-collection="true">
    <document type="mytype"
              mode="index"
              selection="mytype.version > 4" />
</documents>
```
```
4. Use [/document/v1](../reference/api/document-v1.html#delete) to delete documents identified by a [document selection](../reference/writing/document-selector-language.html) - example dropping all documents from the _my\_doctype_ schema. The _cluster_ value is the ID of the content cluster in _services.xml_, e.g., `<content id="my_cluster" version="1.0">`:
```
$ curl -X DELETE \
  "$ENDPOINT/document/v1/my_namespace/my_doctype/docid?selection=true&cluster=my_cluster"
```
5. It is possible to drop a schema, with all its content, by removing the mapping to the content cluster. To understand what is happening, here is the status before the procedure: 

## Example

This is an end-to-end example on how to track number of documents, and delete a subset using a [selection string](../reference/writing/document-selector-language.html).

### Feed sample documents

Feed a batch of documents, e.g. using the [vector-search](https://github.com/vespa-cloud/vector-search) sample application:

```
$ vespa feed <(python3 feed.py 100000 3)
```

See number of documents for a node using the [content.proton.documentdb.documents.total](../reference/operations/metrics/searchnode.html#content_proton_documentdb_documents_total) metric (here 100,000):

```
$ docker exec vespa curl -s http://localhost:19092/prometheus/v1/values | grep ^content.proton.documentdb.documents.total

  content_proton_documentdb_documents_total_max{metrictype="standard",instance="searchnode",documenttype="vector",clustername="vectors",vespa_service="vespa_searchnode",} 100000.0 1695383025000

  content_proton_documentdb_documents_total_last{metrictype="standard",instance="searchnode",documenttype="vector",clustername="vectors",vespa_service="vespa_searchnode",} 100000.0 1695383025000
```

Using the metric above is useful while feeding this example. Another alternative is [visiting](visiting.html) all documents to print the ID:

```
$ vespa visit --field-set "[id]" | wc -l
  100000
```

At this point, there are 100,000 document in the index.

### Define selection

Define the subset of documents to delete - e.g. by age or other criteria. In this example, select random 1%. Do a test run:

```
$ vespa visit --field-set "[id]" --selection 'id.hash().abs() % 100 == 0' | wc -l
    1016
```

Hence, the selection string `id.hash().abs() % 100 == 0` hits 1,016 documents.

### Delete documents

Delete documents, see the number of documents deleted in the response:

```
$ curl -X DELETE \
  "http://localhost:8080/document/v1/mynamespace/vector/docid?selection=id.hash%28%29.abs%28%29+%25+100+%3D%3D+0&cluster=vectors"

  {
      "pathId":"/document/v1/mynamespace/vector/docid",
      "documentCount":1016
  }
```

In case of a large result set, a continuation token might be returned in the response, too:

```
"continuation": "AAAAEAAAA"
```

If so, add the token and redo the request:

```
$ curl -X DELETE \
  "http://localhost:8080/document/v1/mynamespace/vector/docid?selection=id.hash%28%29.abs%28%29+%25+100+%3D%3D+0&cluster=vectors&continuation=AAAAEAAAA"
```

Repeat as long as there are tokens in the output. The token changes in every response.

### Validate

Check that all documents matching the selection criterion are deleted:

```
$ vespa visit --selection 'id.hash().abs() % 100 == 0' --field-set "[id]" | wc -l
  0
```

List remaining documents:

```
$ vespa visit --field-set "[id]" | wc -l
  98984
```

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [Example](#example)
- [Feed sample documents](#feed-sample-documents)
- [Define selection](#define-selection)
- [Delete documents](#delete-documents)
- [Validate](#validate)

