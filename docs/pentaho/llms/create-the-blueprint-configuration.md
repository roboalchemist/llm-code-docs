# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/data-lineage/contribute-additional-step-and-job-entry-analyzers-to-the-pentaho-metaverse/examples/create-the-blueprint-configuration.md

# Create the Blueprint configuration

[Blueprint](http://aries.apache.org/modules/blueprint.html) provides a dependency injection framework for OSGi. The metaverse has two injection points. It has a reference list of all services registered in the container for both the IStepAnalyzer interfaces and theIJobEntryAnalyzer interfaces. When the container detects a new service which provides an implementation of one of those interfaces, the metaverse sees it and adds it to its set of known analyzers. The next time a step which implements the particular class you care about, such as DummyTransMeta in our example, is analyzed, your new **StepAnalyzers** will be used and your override methods will be called.

Create a `blueprint.xml` file in `src/main/resources/OSGI-INF/blueprint/` folder. (Create the folders, if needed.)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<blueprint xmlns="http://www.osgi.org/xmlns/blueprint/v1.0.0"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="
             http://www.osgi.org/xmlns/blueprint/v1.0.0 http://www.osgi.org/xmlns/blueprint/v1.0.0/blueprint.xsd
             ">

	<!-- Define a bean for our new step analyzer -->
	<bean id="dummyStepAnalyzer"/>

	<!--
  	  Define our analyzer as a service. This will allow it to be automatically added to the reference-list ultimately used
  	  by the TransformationAnalyzer to determine if there is a custom analyzer for a particular BaseStepMeta impl
  	  (DummyTransMeta in this case).
	-->
	<service id="dummyStepAnalyzerService"
         interface="org.pentaho.metaverse.api.analyzer.kettle.step.IStepAnalyzer"
         ref="dummyStepAnalyzer"/>


</blueprint>
```
