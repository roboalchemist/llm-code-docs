# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/data-lineage/contribute-additional-step-and-job-entry-analyzers-to-the-pentaho-metaverse/different-types-of-step-analyzers.md

# Different types of step analyzers

In the process of implementing custom step analyzers, we discovered a few generic patterns based on the type of step.

* First, there are the traditional steps which just take some input fields, manipulate them in some fashion, and then output them.
* The second type are the input and output steps. These steps use an external resource (file, database, web service, etc) to read or write data.
* The last is a more specific type of the second, and one which requires a logical connection to an external resource, typically a database or noSQL data store.

These patterns are the basis for the three main base classes you might consider extending when implementing a custom step analyzer.
