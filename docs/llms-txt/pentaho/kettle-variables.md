# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/variables/kettle-variables.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/variables/kettle-variables.md

# Kettle Variables

Kettle variables provide a way to store small pieces of information dynamically in a narrower scope than environment variables. A Kettle variable is local to Kettle, and can be scoped down to the job or transformation in which it is set, or up to a related job. The Set Variable and Set Session Variables steps in a transformation allow you to specify the related job that you want to limit the scope to (for example, the parent job, grandparent job, or the root job).

Kettle variables configure various PDI-specific options such as the location of the shared object file for transformations and jobs or the log size limit.&#x20;

You can set variables using the following methods:

* [Set Kettle variables in the PDI client](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/variables/kettle-variables/set-kettle-variables-in-the-pdi-client)
* [Set Kettle variables manually](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/variables/kettle-variables/set-kettle-variables-manually)
* [Set Kettle or Java environment variables in the Pentaho MapReduce job entry](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/variables/kettle-variables/set-kettle-or-java-environment-variables-in-the-pentaho-mapreduce-job-entry)
* [Set the LAZY\_REPOSITORY variable in the PDI client](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/variables/kettle-variables/set-the-lazy_repository-variable-in-the-pdi-client)

If you are running a [Pentaho MapReduce](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/pentaho-mapreduce) job, you can also set Kettle and environment variables in the Pentaho MapReduce job entry.
