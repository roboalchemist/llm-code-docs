# Source: https://docs.pentaho.com/install/9.3-install/relational-data-modeling-in-pentaho/the-physical-layer.md

# Source: https://docs.pentaho.com/install/10.2-install/relational-data-modeling-in-pentaho/the-physical-layer.md

# The Physical Layer

The physical layer of a Pentaho domain encompasses connections, physical tables and physical columns. These objects represent the database(s) you are trying to model and enrich with metadata. The physical layer is not considered part of the business model, because not all connections defined in the physical layer will be used in every business model.

Multiple business models can be created in one domain, but those models must have one and only one connection reference. This means that you cannot mix and match physical tables from two different connections in the same model yet. We realize that this prevents the model from supporting multiple data sources, as well as severely limits the Pentaho Metadata Editor's ability to allow table changes across connections, a feature necessary for moving from dev to production databases, for example. Fortunately, you can get around the latter with a bit of hand-editing XML. Note that these features are important to us and are early inclusions in the metadata roadmap.
