# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/data-lineage/contribute-additional-step-and-job-entry-analyzers-to-the-pentaho-metaverse/different-types-of-step-analyzers/external-resource.md

# External resource

If you are writing a custom analyzer for a step which reads or writes data from an external source like a file, extend **ExternalResourceStepAnalyzer**. An example analyzer that extends this is [TextFileOutputStepAnalyzer](https://github.com/pentaho/pentaho-metaverse/blob/master/core/src/main/java/org/pentaho/metaverse/analyzer/kettle/step/textfileoutput/TextFileOutputStepAnalyzer.java).

![Text File Output Step Analyzer Diagram](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-8018d6f41b10ba9b6ab44d0a2304d23ef11aa0ec%2Fexternalresourcegraph.png?alt=media)

Above is a typical file-based output step graph diagram (CSV would be very similar). This kind of step analyzer is different in that it creates resource nodes for fields and files which it touches (the yellow boxes). To accomplish this in a custom step analyzer, there are a few steps you must take. First, you must implement the abstract methods defined in**ExternalResourceStepAnalyzer**:

```java
@Override
public String getResourceInputNodeType() {
  return null;
}
 
@Override
public String getResourceOutputNodeType() {
  return DictionaryConst.NODE_TYPE_FILE_FIELD;
}
 
@Override
public boolean isOutput() {
  return true;
}
 
@Override
public boolean isInput() {
  return false;
}
 
@Override
public IMetaverseNode createResourceNode( IExternalResourceInfo resource ) throws MetaverseException {
  return createFileNode( resource.getName(), descriptor );
}
```

Next, you need to create a class which implements **IStepExternalResourceConsumer**. You will want to extend the base class **BaseStepExternalResourceConsumer** to help make your job a bit easier. External Resource Consumers are used in two places: once when the execution profiles are generated to determine what resources are read from/written to, and once by the step analyzers. In your `blueprint.xml` file, you will need to define the bean, publish the service, and inject the bean into your step analyzer:

```xml
<!-- Define the bean for the step analyzer, inject the external resource consumer -->
<bean id="TextFileOutputStepAnalyzer"
      class="org.pentaho.metaverse.analyzer.kettle.step.textfileoutput.TextFileOutputStepAnalyzer">
  <property name="externalResourceConsumer" ref="textFileOutputERC"/>
</bean>


<!--
  Define our analyzer as a service. This will allow it to be automatically added to the reference-list ultimately used
  by the TransformationAnalyzer to determine if there is a custom analyzer for a particular BaseStepMeta impl
  (TableInputMeta in this case).
-->
<service id="textFileOutputStepAnalyzerService"
         interface="org.pentaho.metaverse.api.analyzer.kettle.step.IStepAnalyzer"
         ref="TextFileOutputStepAnalyzer"/>


<!-- Define the external resource consumer bean -->
<bean id="textFileOutputERC" scope="singleton"
      class="org.pentaho.metaverse.analyzer.kettle.step.textfileoutput.TextFileOutputExternalResourceConsumer"/>


<!--
  Define the external resource consumer as a service so it will get added to the reference-list of all IStepExternalResourceConsumer's.
-->
<service id="textFileOutputERCService"
         interface="org.pentaho.metaverse.api.analyzer.kettle.step.IStepExternalResourceConsumer"
         ref="textFileOutputERC"/>
```

The custom logic portions of the **TextFileOutputStepAnalyzer** are in the fields it uses, and this logic determines the fields which are actually written to the file.

```java
@Override
protected Set<StepField> getUsedFields( TextFileOutputMeta meta ) {
  Set<StepField> usedFields = new HashSet<>();
  // we only "use" one field IF we are getting the file to write to from a field in the stream
  if ( meta.isFileNameInField() ) {
    usedFields.addAll( createStepFields( meta.getFileNameField(), getInputs() ) );
  }
  return usedFields;
}
 
 
@Override
public Set<String> getOutputResourceFields( TextFileOutputMeta meta ) {
  // TextFileOutput doesn't force you to write all input fields out to the file, you can pick which ones you want.
  // The default impl of this method assumes you want all inputs.
  Set<String> fields = new HashSet<>();
  TextFileField[] outputFields = meta.getOutputFields();
  for ( int i = 0; i < outputFields.length; i++ ) {
    TextFileField outputField = outputFields[ i ];
    fields.add( outputField.getName() );
  }
  return fields;
}
```
