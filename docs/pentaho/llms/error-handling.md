# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/general-user-defined-java-class/class-code-user-defined-java-class/error-handling.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/general-user-defined-java-class/class-code-user-defined-java-class/error-handling.md

# Error handling

If you want PDI to handle errors that may occur while running your class in a transformation, you must implement for your own error handling code. Before adding any error handling code, right-click on the User Defined Java Class step in the PDI client canvas and select **Error Handling** in the menu that appears. The resulting Step error handling settings dialog box contains options for specifying an error target step and associated field names that you will use to implement error handling in your defined code.

The following try code block from the `User Defined Java Class – Lambda Examples.ktr` in the `data-intregation/samples/transformations` directory contains an example of such error handling:

```java
try {

Object     numList = strsList.stream()
                        .map( new ToInteger() )
                     .sorted( new ReverseCase() )
                     .collect( Collectors.toList() );

    get( Fields.Out, "reverseOrder" ).setValue( row, numList.toString() );

} catch (NumberFormatException ex) {
    // Number List contains a value that cannot be converteds to an Integer.
    rowInError = true;
    errMsg = ex.getMessage();
    errCnt = errCnt + 1;
}

if ( !rowInError ) {
    putRow( data.outputRowMeta, row );
} else {
    // Output errors to the error hop. Right click on step and choose "Error Handling..."
    putError(data.outputRowMeta, row, errCnt, errMsg, "Not allowed", "DEC_0");
}
```

The try in the code sample above tests to see if `numList` contains valid numbers. If the list contains a number that is not valid, `putError` is used to handle the error and direct it to the wlog: ErrorPath step in the sample transformation. The ErrorPath step is also specified in the **Target steps** tab of the User Define Java Class step.
