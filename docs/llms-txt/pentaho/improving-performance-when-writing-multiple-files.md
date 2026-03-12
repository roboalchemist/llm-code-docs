# Source: https://docs.pentaho.com/pdia-data-integration/data-integration-issues/improving-performance-when-writing-multiple-files.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-issues/improving-performance-when-writing-multiple-files.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-issues/improving-performance-when-writing-multiple-files.md

# Improving performance when writing multiple files

You can use the two following Kettle properties to tune how the Text File Output and the Hadoop File Output steps work in a transformation.

* **KETTLE\_FILE\_OUTPUT\_MAX\_STREAM\_COUNT**

  This property limits the number of files that can be opened simultaneously by the step. The property only works when the **"Accept file name from field?"** option (in the **File** tab) is selected. In this scenario, each row coming into the step has a column containing the file name to which the remaining data in the row is to be written. If each row has a different file name, then the step will open a new file for each row. Once data is written to the file referenced in the row, the file is left open in case the next row references the same file. Leaving the file open prevents the step from aborting. If the transformation is processing many rows and each row has a different file name, then many files will be opened and there is a possibility of exhausting the number of open files allowed by the OS. To avoid this problem, use **KETTLE\_FILE\_OUTPUT\_MAX\_STREAM\_COUNT** to define the maximum number of files the step can have open. Once the step reaches the maximum number of open files, it closes one of the open files before opening another. If the file that was closed is referenced in a later row, a different file will be closed and the referenced file will be reopened for append. Setting this parameter to `0` allows for an unlimited number of open files. The default is: 1024
* **KETTLE\_FILE\_OUTPUT\_MAX\_STREAM\_LIFE**

  This property defines the maximum number of milliseconds between flushes of all files opened by the step. The property is most useful when the **"Accept file name from field?"** option (in the **File** tab) is selected. Since the output written to each file is buffered, if many small files are opened and written to, there is a possibility that a large amount of buffered data could exhaust the system memory. Setting this property forces the buffered file data to be periodically flushed, reducing the amount of system memory used by the step. Setting this value to `0` prevents the file streams from being periodically flushed. The default value is: 0

To edit the Kettle properties file, follow the steps in: [Set Kettle variables in the PDI client](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/variables/kettle-variables/set-kettle-variables-in-the-pdi-client).
