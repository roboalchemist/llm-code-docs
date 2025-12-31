# Source: https://firebase.google.com/docs/firestore/using-console.md.txt

<br />

You can perform the following actions onCloud Firestorewhen using the[Firebase console](https://console.firebase.google.com/project/_/firestore/data):

- View, add, edit, and delete data.
- Create and updateCloud FirestoreSecurity Rules.
- Manage indexes.
- Monitor usage.

## View data

You can view all yourCloud Firestoredata in the Firebase console. From theCloud Firestore[**Data**tab](https://console.firebase.google.com/project/_/firestore/data), click on a document or collection to open the data nested within that item.

### Open a specific path

To open a document or collection at a specific path, use the**Edit path** buttoncreate:

![Click the Edit Path button to open a specific document or collection.](https://firebase.google.com/docs/firestore/images/edit-path.png)

### Filter documents in a collection

To filter the documents listed in a collection, use the**Filter list** buttonfilter_list.

![Click the Filter list button to filter the documents listed.](https://firebase.google.com/docs/firestore/images/filter-ui.png)

### Non-existent ancestor documents

A document can exist even if one or more its ancestors don't exist. For example, the document at path`/mycoll/mydoc/mysubcoll/mysubdoc`can exist even if the ancestor document`/mycoll/mydoc`does not. TheCloud Firestoredata viewer displays non-existent ancestor document as follows:

- In a collection's list of documents, the document IDs of non-existent ancestor documents are*italicized*.
- In a non-existent ancestor document's information panel, the data viewer points out that the document does not exist.

![Non-existent ancestor document in the console.](https://firebase.google.com/docs/firestore/images/non-existent-ancestor.png)
| **Warning:** Even though non-existent ancestor documents appear in the console, they do not appear in queries and snapshots. You must create the document to include it in query results.

## Query data

You can query for documents in the***Query builder*** tab of theCloud FirestoreData page.

1. [Go to theCloud FirestoreData page](https://console.firebase.google.com/project/_/firestore/data)

2. Click the**Query builder**tab.

3. Select a[query scope](https://firebase.google.com/docs/firestore/query-data/index-overview#query_scopes).

   Select***Collection***to query a single collection. In the text field, enter a path to a collection.

   Select***Collection group*** to query all collections with the same ID. In the***Collection group***field, enter a collection group ID.

   The table will automatically display documents from the specified collection or collection group.
4. Click***Add to query*** to filter the returned set of documents. By default, the Query Builder adds a`WHERE`clause. You can modify this clause using the dropdowns and text fields or change to one of the other available clauses. To continue building more complex queries, click***Add to query***.

   To remove a query clause, click it's remove buttoncancel. To remove all query clauses, click***Clear***.
   | **Note:** Queries must meetCloud Firestorerequirements and limitations for queries. Otherwise, the query fails and the page returns an error that describes why the query failed.
5. Click***Run***to retrieve results from your database.

### Query requirements and limitations

As you use the Query Builder, keep in mind the following requirements and limitations for queries.

- All queries must be supported by one or more indexes. If the database cannot find an index to support the query, it will return an error that contains a link to build the required index.

- `ORDER BY`clauses must match the fields in the`WHERE`clauses and come in the same order. By default, results are ordered by document ID. If you filter by any other field with anything other than an equality (`==`), add an`ORDER BY`clause for that field.

- Range (`<`,`<=`,`>`,`>=`) and not equals (`!=`,`not-in`) query clauses must all filter on the same field.

For additional limitations, see[Query limitations](https://firebase.google.com/docs/firestore/query-data/queries#query_limitations).

## Manage data

InCloud Firestore, you store data in documents and organize your documents into collections. Before you start adding data, learn more about the[Cloud Firestoredata model](https://firebase.google.com/docs/firestore/data-model).

You can add, edit, and delete documents and collections from the Firebase console. To manage your data, open the[**Data**tab](https://console.firebase.google.com/project/_/firestore/data)in the**Cloud Firestore**section:
| **Note:** Read, write, and delete operations performed in the console count towards yourCloud Firestoreusage. Some console activities, like viewing a document containing multiple fields, may generate several operations.

### Add data

1. Click**Add collection** , then enter your collection name and click**Next**.
2. Enter a specific document ID or click**Auto ID**, then add fields for the data in your document.
3. Click**Save**. Your new collection and document appear in the data viewer.
4. To add more documents to the collection, click**Add document**.

### Edit data

1. Click on a collection to view its documents, then click on a document to view its fields and subcollections.
2. Click on a field to edit its value. To add fields or subcollections to the selected document, click**Add field** or**Add collection**.

### Delete data

To delete a collection:

1. Select the collection you want to delete.
2. Click the menu icon at the top of the documents column, then click**Delete collection**.

![Click Delete collection from the menu in the documents column](https://firebase.google.com/docs/firestore/images/delete-collection.png)

To delete a document or all of its fields:

1. Select the document you want to delete.
2. Click the menu icon at the top of the document details column. Select**Delete document** or**Delete document fields**.

Deleting a document deletes all of the nested data in that document, including any subcollections. However, deleting a document's fields does not delete its subcollections.

![Click Delete document or Delete document fields from the context menu in the document details column](https://firebase.google.com/docs/firestore/images/delete-document.png)

To delete a specific field in a document:

1. Select the document to view its fields.
2. Click the delete icon beside the field you want to delete.

![Click the delete icon to remove a field from a document](https://firebase.google.com/docs/firestore/images/delete-field.png)

## ManageCloud FirestoreSecurity Rules

To add, edit, and deleteCloud FirestoreSecurity Rulesfrom the Firebase console, go to the[**Rules**tab](https://console.firebase.google.com/project/_/firestore/rules)in the**Cloud Firestore** section. Learn more about[setting up and customizing rules](https://firebase.google.com/docs/firestore/security/get-started).

## Manage indexes

To create new indexes for your queries and manage existing indexes from the Firebase console, go to the[**Indexes**tab](https://console.firebase.google.com/project/_/firestore/indexes)in the**Cloud Firestore** section. Learn more about[managing indexes](https://firebase.google.com/docs/firestore/query-data/indexing).

## Monitor usage

To monitor yourCloud Firestoreusage, open theCloud Firestore[**Usage**tab](https://console.firebase.google.com/project/_/firestore/usage)in the Firebase Console. Use the dashboard to gauge your usage over different time periods.