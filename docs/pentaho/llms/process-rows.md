# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/general-user-defined-java-class/class-code-user-defined-java-class/process-rows.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/general-user-defined-java-class/class-code-user-defined-java-class/process-rows.md

# Process rows

The **Processor** code defines the `processRow()` method, which is the heart of the step. This method is called by the transformation in a tight loop and will continue until false is returned.

**Note:** `getRow()` method must be called before the first `get(Fieds.in, FIELD_NAME)` that helps to avoid situations with unexpected fields ordering in the data obtained from the previous step (such as Mapping input specification).

A very simple example that calculates `firstname+" "+lastname` and stores it into a `nameField` is shown in the following example **Processor** code block:

```java
String firstnameField;
String lastnameField;
String nameField;
 
public boolean processRow(StepMetaInterface smi, StepDataInterface sdi) throws KettleException
{
    // Let's look up parameters only once for performance reason.
    //
    if (first) {
      firstnameField = getParameter("FIRSTNAME_FIELD");
      lastnameField = getParameter("LASTNAME_FIELD");
      nameField = getParameter("NAME_FIELD");
      first=false;
    }
 
    // First, get a row from the default input hop
    //
    Object[] r = getRow();
 
    // If the row object is null, we are done processing.
    //
    if (r == null) {
      setOutputDone();
      return false;
    }
 
    // It is always safest to call createOutputRow() to ensure that your output row's Object[] is large
    // enough to handle any new fields you are creating in this step.
    //
    Object[] outputRow = createOutputRow(r, data.outputRowMeta.size());
 
    String firstname = get(Fields.In, firstnameField).getString(r);
    String lastname = get(Fields.In, lastnameField).getString(r);
 
    // Set the value in the output field
    //
    String name = firstname+" "+lastname;
    get(Fields.Out, nameField).setValue(outputRow, name);
 
    // putRow will send the row on to the default output hop.
    //
    putRow(data.outputRowMeta, outputRow);
 
    return true;
```
