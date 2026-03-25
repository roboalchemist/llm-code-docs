# Source: https://docs.pentaho.com/pba-metadata-editor/readme/a-conceptual-overview-of-relational-data-modeling-get-started-with-pentaho-metadata-editor.md

# Source: https://docs.pentaho.com/pba-metadata-editor/pdia-9.3-metadata-editor/get-started-with-pentaho-metadata-editor-cp/a-conceptual-overview-of-relational-data-modeling-get-started-with-pentaho-metadata-editor.md

# Source: https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/get-started-with-pentaho-metadata-editor-cp/a-conceptual-overview-of-relational-data-modeling-get-started-with-pentaho-metadata-editor.md

# A conceptual overview of relational data modeling

Metadata in Pentaho is based on relational data modeling, which maps the physical structure of your database into a logical business model. The goal of the relational data modeling in Pentaho is to simplify the experience of business users when they are creating reports.

The metadata business model is actually one major component in a Pentaho metadata domain. The domain encapsulates both the physical descriptions of your database objects and the logical model (the business model), the abstract representation of the database. The purpose of this page is to give a Pentaho metadata consumer a good idea of the relationships involved throughout a Pentaho domain, in order to fully leverage the power of the business models. This diagram depicts the business objects and relationships within the Pentaho metadata domain:

![](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-ea276135cbfcb718dad1568c92e7fce9473a592a%2F01_metadata_domain.png?alt=media)

In this diagram, both the relationship arrows in the legend as well as the color of the business objects are significant. Each independent business object has its own color; thus, connections, physical tables, business tables, physical columns, business columns and categories are the main business objects in a Pentaho domain. The two types of relationships depicted in the diagram are key to understanding Pentaho metadata. The "inherits from" relationship is a relationship between two different business objects where one will inherit metadata from the other, with the ability to override any of the inherited metadata properties. An example of this is that a business table inherits metadata from its associated physical table. The second relationship, the "same object" relationship, is one where the two business objects are actually one and the same, just represented in a different organization or duplicated for usability. This is the relationship between business columns in the abstract business layer, and business columns in the business view.

**Important:** Although the Pentaho Metadata Editor displays a checkbox for each of the permissions available in the Pentaho Server, only **Execute** is enforced.

## The Physical Layer

The physical layer of a Pentaho domain encompasses connections, physical tables and physical columns. These objects represent the database(s) you are trying to model and enrich with metadata. The physical layer is not considered part of the business model, because not all connections defined in the physical layer will be used in every business model.

Multiple business models can be created in one domain, but those models must have one and only one connection reference. This means that you cannot mix and match physical tables from two different connections in the same model yet. We realize that this prevents the model from supporting multiple data sources, as well as severely limits the Pentaho Metadata Editor's ability to allow table changes across connections, a feature necessary for moving from dev to production databases, for example. Fortunately, you can get around the latter with a bit of hand-editing XML. Note that these features are important to us and are early inclusions in the metadata roadmap.

## The Business View

The business view is the part of the business model that applications will operate against, and end-users will see. The business view is nothing more than "buckets" (called categories) for you to re-arrange and re-organize your business columns in a fashion that makes sense to the consumers of the data.

In the business view, you can create any number of categories and arrange your business columns in those categories however it best suits your business, mixing and matching columns that derived from different business tables, even adding business columns more than once to different categories. The only restriction to the business view is that you cannot add the same business column more than once to a single category.

## The Abstract Business Layer

The abstract business layer is the heavy lifter in the metadata business model. The business model encompasses the abstract business layer and the business view. In the abstract business layer, you have business tables, business columns, and business relationships.

You can create business tables for any physical table you have defined in the physical layer. You can also create more than one business table to reference the same physical table. The same rules apply for business columns. This can be useful in a multitude of scenarios, filtering security or even data at this level being one example. The business table keeps a reference to the physical table that it models, and this allows a metadata inheritance relationship between physical tables and business tables. If you define metadata on a physical table, the business table will inherit that metadata, unless and until the business table itself has overridden the inherited metadata. This concept operates on a metadata property to property basis, meaning that each property can be overridden individually.

The same relationship exists between physical columns and business columns. If you define metadata on a physical column, the business column will inherit that metadata, unless and until the business column itself has overridden the inherited metadata. Then there are relationships. Do not confuse the term relationships here with the relationships described in the domain diagram. The relationships described here are not represented in that diagram. These relationships are mappings that you define to describe the relational (or other) bonds between your business tables. One example may be a one to many relationship between a customer table and an orders table. The strength in metadata relationships is that you can identify relationships between columns or tables in the abstract business layer that may not be obvious in the physical layer. An example would be to compare budget, actual and sales numbers, using a formula-derived business column that is specific to your business rules.

## Incorporate Metadata

Each business object in the domain can have metadata associated with it, with the exception of categories. In Pentaho terminology, a collection of metadata properties is called a concept.

Each business object can have the following three levels of concepts:

* its own (self or child concept)
* a parent concept
* an inherited concept

All of the defined metadata properties from the three levels are available (to metadata-aware applications, end-users) on a business object. It is important to understand what the override hierarchy is, when more than one concept level has defined the same metadata property.

When a metadata property is set in the business object itself, and that same property is in play (either inherited or from a parent concept), the business object's self or child concept overrides all others. The next level in the hierarchy is the parent concept. So, for example, suppose the name property on a business object is not set on the object itself, but is inherited from its physical counterpart. In this instance, you set a parent concept on the business object with a name property defined in the parent concept. The parent concept's name property overrides the inherited name property. Ultimately, the inherited metadata properties are used if, and only if, the same property is not defined somewhere down the hierarchical chain, as part of a self concept or parent concept.

<br>
