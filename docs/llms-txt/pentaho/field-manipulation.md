# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/data-lineage/contribute-additional-step-and-job-entry-analyzers-to-the-pentaho-metaverse/different-types-of-step-analyzers/field-manipulation.md

# Field manipulation

If the step you are writing a custom analyzer for is just a traditional step which manipulates data or fields to produce different outputs than inputs, then you should extend your step analyzer. An example of this kind of step analyzer would be [Strings Cut](https://github.com/pentaho/pentaho-metaverse/blob/master/core/src/main/java/org/pentaho/metaverse/analyzer/kettle/step/stringscut/StringsCutStepAnalyzer.java). It is much easier to understand the graph model when looking at it.

Below is the basic graph model for the Strings Cut step:

![Strings Cut Diagram](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-67d550e6e4a22cfcab65518d7a6f6d90d9afce8d%2Fstrings_cut.png?alt=media)

In this example, three fields are inputs into the step: `FirstName`, `LastName`, and `Middle Name`. Four fields are derived as the outputs: `FirstName`, `LastName`, `MI` (middle initial), and `Middle Name`. In the example below, the Strings Cut step uses just the `Middle Name` input field to create the `MI` output field from the first character.

![Strings Cut Dialog Box](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-d9929de5820123243d7d859f9a4a9163f2607060%2FStringCutDialog.png?alt=media)

Looking at the graph above, you can see that there are four 'derives' links corresponding to the four output fields. The `Middle Name` input field results in two derive links to both the `Middle Name` and the `MI` output fields. The base **StepAnalyzer** will create the inputs and outputs (fields and links) for you, but it is up to you to inform the base analyzer about the fields to use and which fields derive other fields.

Override the **getUsedFields** method to supply the fields used by the step. In the example above, the only input field used by the step is `Middle Name`.

```java
@Override
protected Set<StepField> getUsedFields( StringCutMeta meta ) {
  HashSet<StepField> usedFields = new HashSet<>();
  for ( String fieldInString : meta.getFieldInStream() ) {
    usedFields.addAll( createStepFields( fieldInString, getInputs() ) );
  }
  return usedFields;
}
```

To supply the non-passthrough derives links and operation information, override the **getChangeRecords** method. In the above example, the non-passthrough derived link from the `Middle Name` input field to the `MI` output field is created from this override method.

```java
@Override
public Set<ComponentDerivationRecord> getChangeRecords( StringCutMeta meta ) throws MetaverseAnalyzerException {
  Set<ComponentDerivationRecord> changeRecords = new HashSet<>();
  for ( int i = 0; i < meta.getFieldInStream().length; i++ ) {
    String fieldInString = meta.getFieldInStream()[i];
    String fieldOutString = meta.getFieldOutStream()[i];
    if ( fieldOutString == null || fieldOutString.length() < 1 ) {
      fieldOutString = fieldInString;
    }
 
    ComponentDerivationRecord changeRecord = new ComponentDerivationRecord( fieldInString, fieldOutString, ChangeType.DATA );
    String changeOperation = fieldInString + " -> [ substring [ " + meta.getCutFrom()[i] + ", "
        + meta.getCutTo()[i] + " ] ] -> " + fieldOutString;
    changeRecord.addOperation( new Operation( Operation.CALC_CATEGORY, ChangeType.DATA,
      DictionaryConst.PROPERTY_TRANSFORMS, changeOperation ) );
    changeRecords.add( changeRecord );
  }
  return changeRecords;
}
```

By default, the implementation determines if a field is a passthrough field or not. If this logic isn't sufficient for your step, then override the **isPassthrough** method like the StringsCutStepAnalyzer does. The default logic assumes that if there is an output field with an identical name as an input field, then it is a passthrough.

```java
/**
 * Determines if a field is considered a passthrough field or not. In this case, if we're not using the field, it's
 * a passthrough. If we are using the field, then it is only a passthrough if we're renaming the field on which we
 * perform the operation(s).
 *
 * @param originalFieldName The name of the incoming field
 * @return true if this field is a passthrough (i.e. no operations are performed on it), false otherwise
 */
@Override
protected boolean isPassthrough( StepField originalFieldName ) {
  String[] inFields = baseStepMeta.getFieldInStream();
  String origFieldName = originalFieldName.getFieldName();
  for ( int i = 0; i < inFields.length; i++ ) {
    if ( inFields[i].equals( origFieldName ) && Const.isEmpty( baseStepMeta.getFieldOutStream()[i] ) ) {
      return false;
    }
  }
  return true;
}
```
