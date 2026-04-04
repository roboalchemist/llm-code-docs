# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/data-lineage/contribute-additional-step-and-job-entry-analyzers-to-the-pentaho-metaverse/different-types-of-step-analyzers/connection-based-external-resource.md

# Connection-based external resource

If the step you are writing a custom analyzer for is using a connection like a database connection, then you should extend **ConnectionExternalResourceStepAnalyzer**. An example of this type of analyzer is [TableOutputStepAnalyzer](https://github.com/pentaho/pentaho-metaverse/blob/master/core/src/main/java/org/pentaho/metaverse/analyzer/kettle/step/tableoutput/TableOutputStepAnalyzer.java). Connection-based analyzers are just a more specific type of step analyzer than the external resource step analyzers. It is an external resource analyzer which also has a connection analyzer and understands the concept of a table.

All **IStepAnalyzers** can optionally support the notion of a property called **connectionAnalyzer**. A connection analyzer is a specific type of analyzer. Its job is to build the relationships and nodes for an external connection. Some examples of connection analyzers are for traditional databases, noSQL databases, HDFS, etc. The metaverse exposes two **IDatabaseConnection** analyzers for reuse in external bundles (like the one outlined here). You can inject either **stepDatabaseConnectionAnalyzer** or **jobEntryConnectionAnalyzer** into your analyzer by grabbing hold of a reference to the exposed service (see below). If you need a custom **connectionAnalyzer**, you can implement your own and use that in your bundle.

```java
<!--
  If you are defining your resource in a separate bundle, grab a reference to the IDatabaseConnectionAnalyzer
  for steps provided by the core pentaho-metaverse bundle.
  This will be injected into analyzer (TableOutputStepAnalyzer)
-->
<reference id="stepDatabaseConnectionAnalyzerRef"
           interface="org.pentaho.metaverse.api.analyzer.kettle.IDatabaseConnectionAnalyzer"
           component-name="stepDatabaseConnectionAnalyzer"
           availability="mandatory"/>
 
<!--
  Declare our sample analyzer(TableOutputStepAnalyzer) bean. Inject the stepDatabaseConnectionAnalyzer so it can
  use the same one that the TableOutputStepAnalyzer uses.
-->
<bean id="tableOutputStepAnalyzer" class="org.pentaho.metaverse.analyzer.kettle.step.tableoutput.TableOutputStepAnalyzer">
  <property name="connectionAnalyzer" ref="stepDatabaseConnectionAnalyzerRef"/>
  <property name="externalResourceConsumer" ref="tableOutputERC"/>
</bean>
 
<!--
  Define our analyzer as a service. This will allow it to be automatically added to the reference-list ultimately used
  by the TransformationAnalyzer to determine if there is a custom analyzer for a particular BaseStepMeta impl
  (TableOutputMeta in this case).
-->
<service id="tableOutputStepAnalyzerService"
         interface="org.pentaho.metaverse.api.analyzer.kettle.step.IStepAnalyzer"
         ref="tableOutputStepAnalyzer"/>
 
 
<!-- Configure the TableOutputExternalResourceConsumer and service  -->
<bean id="tableOutputERC" scope="singleton"
      class="org.pentaho.metaverse.analyzer.kettle.step.tableoutput.TableOutputExternalResourceConsumer"/>
<service id="tableOutputERCService"
         interface="org.pentaho.metaverse.api.analyzer.kettle.step.IStepExternalResourceConsumer"
         ref="tableOutputERC"/>
```
