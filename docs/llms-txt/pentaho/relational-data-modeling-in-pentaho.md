# Source: https://docs.pentaho.com/install/relational-data-modeling-in-pentaho.md

# Source: https://docs.pentaho.com/install/9.3-install/relational-data-modeling-in-pentaho.md

# Source: https://docs.pentaho.com/install/10.2-install/relational-data-modeling-in-pentaho.md

# Relational Data Modeling in Pentaho

Pentaho allows you to build metadata domains and relational data models. A Pentaho metadata model maps the physical structure of your database into a logical business model.

These mappings are stored in a centralized metadata repository and allow administrators to:

* Create business-language definitions for complex or cryptic database tables
* Decrease the cost and impact associated with low level database changes
* Set security parameters limiting user's report access to data
* Drive formatting on text, date, and numeric data improving report maintenance
* Localize the information to the user's regional settings

The goal of the relational data modeling in Pentaho is to simplify the experience of business users when they are creating reports.

The metadata business model is actually one major component in a Pentaho metadata domain. The domain encapsulates both the physical descriptions of your database objects and the logical model (the business model), the abstract representation of the database. The purpose of this page is to give a Pentaho metadata consumer a good idea of the relationships involved throughout a Pentaho domain, in order to fully leverage the power of the business models. This diagram depicts the business objects and relationships within the Pentaho metadata domain:

![](https://3897443520-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F7HOrU4JuCmIFVNup2Gxd%2Fuploads%2Fgit-blob-ea276135cbfcb718dad1568c92e7fce9473a592a%2F01_metadata_domain.png?alt=media)

In this diagram, both the relationship arrows in the legend as well as the color of the business objects are significant. Each independent business object has its own color; thus, connections, physical tables, business tables, physical columns, business columns and categories are the main business objects in a Pentaho domain. The two types of relationships depicted in the diagram are key to understanding Pentaho metadata. The "inherits from" relationship is a relationship between two different business objects where one will inherit metadata from the other, with the ability to override any of the inherited metadata properties. An example of this is that a business table inherits metadata from its associated physical table. The second relationship, the "same object" relationship, is one where the two business objects are actually one and the same, just represented in a different organization or duplicated for usability. This is the relationship between business columns in the abstract business layer, and business columns in the business view.

**Important:** Although the Pentaho Metadata Editor displays a checkbox for each of the permissions available in the Pentaho Server, only **Execute** is enforced.
