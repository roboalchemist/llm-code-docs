# Source: https://docs.pentaho.com/install/9.3-install/relational-data-modeling-in-pentaho/incorporate-metadata.md

# Source: https://docs.pentaho.com/install/10.2-install/relational-data-modeling-in-pentaho/incorporate-metadata.md

# Incorporate Metadata

Each business object in the domain can have metadata associated with it, with the exception of categories. In Pentaho terminology, a collection of metadata properties is called a concept.

Each business object can have the following three levels of concepts:

* its own (self or child concept)
* a parent concept
* an inherited concept

All of the defined metadata properties from the three levels are available (to metadata-aware applications, end-users) on a business object. It is important to understand what the override hierarchy is, when more than one concept level has defined the same metadata property.

When a metadata property is set in the business object itself, and that same property is in play (either inherited or from a parent concept), the business object's self or child concept overrides all others. The next level in the hierarchy is the parent concept. So, for example, suppose the name property on a business object is not set on the object itself, but is inherited from its physical counterpart. In this instance, you set a parent concept on the business object with a name property defined in the parent concept. The parent concept's name property overrides the inherited name property. Ultimately, the inherited metadata properties are used if, and only if, the same property is not defined somewhere down the hierarchical chain, as part of a self concept or parent concept.
