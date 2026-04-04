# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-9.3-schema-workbench/pentaho-schema-workbench-cp.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-10.2-schema-workbench/pentaho-schema-workbench-cp.md

# Pentaho Schema Workbench 10.2

With a physical multidimensional data model in place, you must create a logical model that maps to it. A Mondrian schema is essentially an XML file that performs this mapping, thereby defining a multidimensional database structure. You can create Mondrian schemas using the Pentaho Schema Workbench.

In a very basic scenario, you will create a Mondrian schema with one cube that consists of a single fact table and a few dimensions, each with a single hierarchy consisting of a handful of levels. More complex schemas may involve multiple virtual cubes, and instead of mapping directly to the single fact table at the center of a star schema, they might map to views or inline tables instead.

All of the Mondrian XML elements are documented in this section in both a single quick reference list and a full individual reference piece for each element. Primarily you will be using Pentaho Schema Workbench to create Mondrian schemas graphically, though you can do advanced schema design through the Data Source Wizard in the User Console or through Schema Workbench later on.

For information on using Pentaho Schema Workbench, see the following topics:&#x20;

* [Get started with the Schema Workbench](https://docs.pentaho.com/pba-schema-workbench/pdia-10.2-schema-workbench/get-started-with-the-schema-workbench)
* [Work with Mondrian schema](https://docs.pentaho.com/pba-schema-workbench/pdia-10.2-schema-workbench/work-with-mondrian-schema)
* [Adapt Mondrian schemas to work with Analyzer](https://docs.pentaho.com/pba-schema-workbench/pdia-10.2-schema-workbench/adapt-mondrian-schemas-to-work-with-analyzer)
* [Localization and internationalization of analysis schemas](https://docs.pentaho.com/pba-schema-workbench/pdia-10.2-schema-workbench/localization-and-internationalization-of-schema-workbench-analysis-schemas)
