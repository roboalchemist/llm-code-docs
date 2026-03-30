# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/data-lineage/contribute-additional-step-and-job-entry-analyzers-to-the-pentaho-metaverse/different-types-of-step-analyzers/adding-analyzers-from-existing-pdi-plug-ins-non-osgi.md

# Adding analyzers from existing PDI plug-ins (non-OSGi)

You can add analyzers from existing PDI non-OSGi plug-ins. For examples of custom analyzers and external resource consumers, see [GitHub - pentaho/pentaho-metaverse](https://github.com/pentaho/pentaho-metaverse) for details.

When adding analyzers, you still need to [add a compile-time dependency](https://github.com/pentaho/documentation/blob/main/PDIA/9.3/PDI/Advanced%20Pentaho%20Data%20Integration%20topics/Advanced%20topics%20\(Pentaho%20Data%20Integration%20overview\)/Data%20lineage/Contribute%20additional%20step%20and%20job%20entry%20analyzers%20to%20the%20Pentaho%20Metaverse/Examples/Add%20dependencies=GUID-F1D87381-93E4-413D-8D69-9D21712C45D7=1=en=.md) to the `pentaho-metaverse-api` JAR file and you must also [create your StepAnalyzer class](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/data-lineage/contribute-additional-step-and-job-entry-analyzers-to-the-pentaho-metaverse/examples/create-a-class-which-implements-istepanalyzer).

The main difference is how you register your analyzer with the rest of the metaverse analyzers. Since this is not an OSGi bundle, the blueprint configuration is not an option. Instead, you have to create a **KettleLifecyclePlugin** which instantiates your analyzer class and registers it with **PentahoSystem**. The following examples illustrate registration to extract the lineage information from documents:

* Analyzer class example for the **CSV File Input** step: [pentaho-metaverse/CsvFileInputStepAnalyzer.java at master · pentaho/pentaho-metaverse](https://github.com/pentaho/pentaho-metaverse/blob/master/core/src/main/java/org/pentaho/metaverse/analyzer/kettle/step/csvfileinput/CsvFileInputStepAnalyzer.java)
* External resource consumer class example for the **CSV File Input** step: [pentaho-metaverse/CsvFileInputExternalResourceConsumer.java at master · pentaho/pentaho-metaverse](https://github.com/pentaho/pentaho-metaverse/blob/master/core/src/main/java/org/pentaho/metaverse/analyzer/kettle/step/csvfileinput/CsvFileInputExternalResourceConsumer.java)

The lifecycle listener is a new plug-in:

```java
import org.pentaho.di.core.annotations.LifecyclePlugin;
import org.pentaho.di.core.lifecycle.LifeEventHandler;
import org.pentaho.di.core.lifecycle.LifecycleListener;
import org.pentaho.platform.engine.core.system.PentahoSystem;
@LifecyclePlugin( id = "CsvFileInputPlugin", name = "CsvFileInputPlugin" )
public class CsvFileInputLifecycleListener implements LifecycleListener {
  CsvFileInputStepAnalyzer analyzer;
  CsvFileInputExternalResourceConsumer consumer;
  @Override public void onStart( LifeEventHandler lifeEventHandler ) {
    // instantiate a new analyzer
    analyzer = new CsvFileInputStepAnalyzer();
    // construct the external resource consumer for the files that it reads from
    consumer = new CsvFileInputExternalResourceConsumer();
    analyzer.setExternalResourceConsumer( consumer );
    // register the analyzer with PentahoSystem. this also adds it to the service reference list that contains ALL IStepAnalyzers registered
    PentahoSystem.registerObject( analyzer );
    // register the consumer with PentahoSystem. this also adds it to the service reference list that contains ALL IStepExternalResourceConsumers registered
    PentahoSystem.registerObject( consumer );
  }
  @Override public void onExit( LifeEventHandler lifeEventHandler ) {
  }
}
```
