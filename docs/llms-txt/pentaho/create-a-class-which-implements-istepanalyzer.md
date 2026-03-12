# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/data-lineage/contribute-additional-step-and-job-entry-analyzers-to-the-pentaho-metaverse/examples/create-a-class-which-implements-istepanalyzer.md

# Create a class which implements IStepAnalyzer

At a minimum, you will need to create a java class which implements the IStepAnalyzer interface (for a job entry analyzer, you would implement IJobEntryAnalyzer). The IStepAnalyzer interface only requires that you implement the **analyzer** and **getSupportedSteps** methods. It is fairly black-box and does not do much to make the developer's life much easier. Step analyzers follow a common pattern:

* Model the step itself in the graph as a node.
* Link all stream fields which are inputs into the step to that node, if any.
* Determine the outputs of the step, if any, then create and link those nodes to the step node.
* Add links to the fields which the step actually uses, if any.
* Add links from the input fields to the output fields.

Virtually, all implementations would benefit by extending the common base class **StepAnalyzer** which provides a common implementation for all of those common tasks. Below, is a simple [implementation of a step analyzer for the Dummy step](https://github.com/pentaho/pentaho-metaverse/blob/master/sample/src/main/java/org/pentaho/metaverse/sample/DummyStepAnalyzer.java). There is nothing special about this step which warrants a custom step analyzer, but for the purpose of this document we will add a custom property to the step node. This is done in the **customAnalyzer** method:

```java
public class DummyStepAnalyzer extends StepAnalyzer<DummyTransMeta> {
  @Override
  protected Set<StepField> getUsedFields( DummyTransMeta meta ) {
    // no incoming fields are used by the Dummy step
    return null;
  }
  @Override
  protected void customAnalyze( DummyTransMeta meta, IMetaverseNode rootNode ) throws MetaverseAnalyzerException {
    // add any custom properties or relationships here
    rootNode.setProperty( "do_nothing", true );
  }
  @Override
  public Set<Class<? extends BaseStepMeta>> getSupportedSteps() {
    Set<Class<? extends BaseStepMeta>> supportedSteps = new HashSet<>();
    supportedSteps.add( DummyTransMeta.class );
    return supportedSteps;
  }
}
```
