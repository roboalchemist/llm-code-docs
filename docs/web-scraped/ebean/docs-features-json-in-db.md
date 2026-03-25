# Source: https://ebean.io/docs/features/json-in-db

Title: Read Auditing | Ebean

URL Source: https://ebean.io/docs/features/json-in-db

Markdown Content:
Overview
--------

Postgres and Oracle have extensive support with JSON stored in the database. Both provide a lot of support for writing queries using document path expressions.

Ebean provides mapping support via `@DbJson` and `@DbJsonB` to map JSON documents to various database types including Postgres JSON, JSONB types as well as standard Varchar, Clob and Blob types. The mapping can be used with all supported databases and Postgres and Oracle provide support for including JSON expressions in query where clauses.

Both Postgres and Oracle support writing queries with JSON expressions and Ebean exposes the most common query expressions.:

Mapping
-------

For all databases JSON documents can be mapped on entity beans and saved and loaded from the database.

### @DbJsonB

In your entity bean you can annotate a property with `@DbJsonB` and that indicates that the property maps to a JSONB database type. For non-Postgres databases this maps to a database Clob.

@Entity
@Table(name="p_doc")
public class SimpleDoc extends Model {

  @Id
  Long id;
  ...

  @DbJsonB
  Map<String,Object> content;

  // Ordinary bean - use Jackson object mapper
  @DbJsonB
  PlainBean plainBean;

### @DbJson

In your entity bean you can annotate a property with `@DbJson` and that indicates that the property maps to a JSON database type. For non-Postgres databases this maps to a database Clob.

@Entity
@Table(name="p_doc")
public class SimpleDoc extends Model {

  @Id
  Long id;
  ...

  @DbJson
  Map<String,Object> content;

  // Ordinary bean - use Jackson object mapper
  @DbJson
  PlainBean plainBean;

Save and Find
-------------

You put JSON content into the content property and save it and fetch is as normal.

String rawJson = "{\"docName\":\"My document\", \"docScore\":234, \"title\":\"Some title\"}";

// get the JSON into a map using Jackson or similar tool.
// Ebean has EJson which using Jackson core which can be used
// to parse JSON content
Map<String, Object> content = EJson.parseObject(rawJson);

SimpleDoc doc = new SimpleDoc();
doc.setName("doc1");
doc.setContent(content);

// save to db
doc.save();

// fetch from db
SimpleDoc doc1 = SimpleDoc.find.byId(doc.getId());

assertEquals("My document", doc1.getContent().get("docName"));

Query expressions
-----------------

`Postgres` and `Oracle` provide expressions such that you can use a `path` expression to test is a given path `EXISTS` or test the value at a path.

Ebean `ExpressionList` has expressions for:

/**
 * Path exists - for the given path in a JSON document.
 */
ExpressionList<T> jsonExists(String propertyName, String path);

/**
 * Path does not exist - for the given path in a JSON document.
 */
ExpressionList<T> jsonNotExists(String propertyName, String path);

/**
 * Equal to expression for the value at the given path in the JSON document.
 */
ExpressionList<T> jsonEqualTo(String propertyName, String path, Object value);

/**
 * Not Equal to - for the given path in a JSON document.
 */
ExpressionList<T> jsonNotEqualTo(String propertyName, String path, Object val);

/**
 * Greater than - for the given path in a JSON document.
 */
ExpressionList<T> jsonGreaterThan(String propertyName, String path, Object val);

/**
 * Greater than or equal to - for the given path in a JSON document.
 */
ExpressionList<T> jsonGreaterOrEqual(String propertyName, String path, Object val);

/**
 * Less than - for the given path in a JSON document.
 */
ExpressionList<T> jsonLessThan(String propertyName, String path, Object val);

/**
 * Less than or equal to - for the given path in a JSON document.
 */
ExpressionList<T> jsonLessOrEqualTo(String propertyName, String path, Object val);

Postgres expressions
--------------------

Ebean uses Postgres `->>` and `#>>` operators to support the JSON expressions.

### Exists expression

For Postgres Ebean's `jsonExists()``jsonNotExists()` expression result in the path value using `->>` or `#>>` and `IS NULL` and `IS NOT NULL`.

List<SimpleDoc> list = new QSimpleDoc().query()
.where()
.jsonExists("content", "path.other")
.findList();

The function can then be used in an Ebean query like:

select t0.id c0, ...
where (t0.content #>> '{path,other}') is not null

### Value expressions

For Postgres Ebean's value expressions such as `jsonEqualTo()`, `jsonGreaterThan()` etc use the `->>` or `#>>` operator depending on the path and then cast the result depending on the value testing against. That is, if the value tested is a Integer or Long the DB path expression is cast to `::INTEGER` and there is similar casting for `::DECIMAL` and `::BOOLEAN`.

List<SimpleDoc> list = new QSimpleDoc().query()
  .where()
  .jsonEqualTo("content", "path.other", 34)
  .findList();

select t0.id c0, ...
where (t0.content #>> '{path,other}')::INTEGER = ?

Oracle expressions
------------------

Ebean uses Oracles `json_exists` and `json_value` functions to support Ebean's JSON expressions.

### Exists expression

For Oracle Ebean's jsonExists() expression uses the Oracle `json_exists` function.

List<SimpleDoc> list = new QSimpleDoc().query()
  .where()
  .jsonExists("content", "path.other")
  .findList();

The function can then be used in an Ebean query like:

select t0.id c0, ...
where json_exists(t0.content, '$.path.other')

### Value expressions

For Oracle Ebean's value's jsonEqualTo() jsonGreaterThan() etc use the Oracle `json_value` function.

List<SimpleDoc> list = new QSimpleDoc().query()
  .where()
  .jsonEqualTo("content", "path.other", 34)
  .findList();

select t0.id c0, ...
where json_value(t0.content, '$.path.other') = ?

Raw expression
--------------

If the provided expressions do not match what is required you can use `raw()` expressions.

List<SimpleDoc> docs = SimpleDoc.find.where()
  // pass a raw expression through - property names are translated to
  // db columns but everything else is passed through to the DB
  .raw("content#>'{docName}' ? 'rob doc'")
  .findList();
