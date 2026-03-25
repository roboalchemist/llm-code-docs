# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/options-user-defined-java-class/info-steps-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/options-user-defined-java-class/info-steps-tab.md

# Info steps tab

![Info steps tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-1903cfacbea153ee808e54387d9eace50ea8c1e4%2FPDITransStep_UserDefinedJavaClass_InfoStepsTab.png?alt=media)

As the `GetRow()` method returns the first row from any input stream (either input stream or info stream), the **Info steps** table is used when the `rowMeta` input and `rowMeta` information vary.

Read or get all the data values from the information stream before calling the `getRow()` method, as shown in the following code example:

```java
if (first){
 first = false;
 
 /* TODO: Your code here. (Using info fields)
 
 FieldHelper infoField = get(Fields.Info, "info_field_name");
 
 RowSet infoStream = findInfoRowSet("info_stream_tag");
 
 Object[] infoRow = null;
 
 int infoRowCount = 0;
 
 // Read all rows from info step before calling getRow() method, which returns first row from any
 // input rowset. As rowMeta for info and input steps varies getRow() can lead to errors.
 while((infoRow = getRowFrom(infoStream)) != null){
 
   // do something with info data
   infoRowCount++;
 }
 */
}
 
Object[] r = getRow();
 
if (r == null) {
       setOutputDone();
       return false;
}
```
