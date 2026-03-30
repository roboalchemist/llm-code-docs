# Source: https://ebean.io/docs/features/draftable

Title: Documentation / Features / Draftable

URL Source: https://ebean.io/docs/features/draftable

Markdown Content:
Overview
--------

Draftable is a feature that uses a second set of tables to hold a 'draft' version of the object graph separately from the 'live'. Typically the draft objects are edited and go through an approval process before being published.

To implement this feature, all @Draftable and @DraftElement beans have a second draft table that closely resembles the live table but commonly will have additional columns to support an approval workflow for publishing.

Publishing is a function that takes underlying rows from the draft tables and copies them to the matching live table. In this way, the application can easily maintain a 'draft' version and 'live' version of the entities.

Mapping
-------

* * *

#### ENTITY MAPPING

#### @Draftable

`@Draftable` is an annotation put on entity beans that should support draftable features.

The @Draftable annotation put on 'top level' (or root level) entity beans and @DraftableElement is put on related child entity beans which are considered part of the same graph.

Publishing a `@Draftable` bean will publish the 'top level' @Draftable entity beans along with any of its related child @DraftableElement beans.

#### @DraftableElement

`@DraftableElement` is an annotation put on entity beans that are part of a draftable object graph but not 'top level' beans. The publish() and draftRestore() functions act on a draftable bean and all it's associated draftableElement beans as a single unit (published/restored as a unit).

* * *

#### PROPERTY MAPPING

#### @DraftOnly

`@DraftOnly` is an annotation put on properties that exist on the draft table only - these properties do not exist on the associated live table. For example, annotation properties that are on the draft to support approval workflow (workflow status, when publish timestamp etc).

#### @DraftDirty

`@DraftDirty` is an annotation that can be put on a boolean property of a @Draftable entity bean. This property only exists on the draft table and it's value is automatically set to true when the draft bean is saved and automatically set to false when the draft bean is published. The property is expected to be used to identify (query) draft beans that should be published.

Currently a change to a @DraftableElement does not set the dirty flag on the 'owning' @Draftable bean and instead this would need to be done manually in this case if required.

#### @DraftReset

`@DraftReset` is an annotation that can be put on a property of a @Draftable entity bean. The value of this property is automatically set to null on the draft bean after it has been published. For example, the property is could contain comments or timestamp values related to the approval workflow (and after a bean is publish these are 'reset' to null on the draft bean).

Query As Draft
--------------

A normal Query builds the object graph from the 'live' tables. You can specify the query to run `asDraft()` and then it will build the object graph using the draft tables. This can be used to `PREVIEW` the currently editing state of the object graphs.

// Get the 'draft' object graph
Document documentDraft =
    Ebean.find(Document.class)
      .setId(docId)
      .asDraft()
      .findOne();

// Get the 'draft' documents
List<Document> draftDocuments =
    Ebean.find(Document.class)
      .where()
        .eq("dirty", true)
        .ge("whenPublish", now)
      .asDraft()
      .findList();

Note: The `asDraft` query state is propagated to any lazy loading or query joins.

Note: Any `asDraft` query does not use the L2 cache (Only queries for live beans can use L2 cache).

Publish
-------

`Publish` is the function that takes the values from draft object graph and applies them to the matching live object graph. The publish function cascades from a top level @Draftable entity bean to any related @DraftableElement entity beans.

#### @OneToMany

A `@OneToMany` relationship to a @DraftableElement effectively has save and delete cascade turned on automatically. The cascade save/delete is used internally to publish the object graph.

#### @ManyToMany

A `@ManyToMany` relationship to a @Draftable bean effectively has save and delete cascade turned on automatically to maintain the relationship.

Database database = DB.getDefault();

// publish a single bean (from draft to live)
// returning the 'live' bean
Document liveDoc = database.publish(Document.class, docId);

// publish using a query
Query<Link> pubQuery = database.find(Link.class)
  .where().idIn(ids)
  .order().asc("id");

// publish returning the resulting 'live' beans
List<Link> pubList = database.publish(pubQuery);

Draft Restore
-------------

`DraftRestore` is the function that takes the values from the live object graph and applies them back to the matching draft object graph. You can consider it the opposite of a publish().

Database database = DB.getDefault();

// Restore a single draft bean
database.draftRestore(Document.class, docId);

Query<Document> restoreQuery = database.find(Document.class)
  .where().idIn(ids)
  .order().asc("id");

// Restore all the beans matching a query
database.draftRestore(restoreQuery);

Example Application
-------------------

An example application is available at [example-draftable](https://github.com/ebean-orm/example-draftable) .

L2 Cache
--------

Only live beans and queries can use the L2 cache. Similarly only save/delete of live beans invalidate parts of the L2 cache. All queries for draft beans do not use the L2 cache and save/delete of draft beans do not invalidate any part of the L2 cache.
