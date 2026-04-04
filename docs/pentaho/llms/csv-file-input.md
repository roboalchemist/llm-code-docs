# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/csv-file-input.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/csv-file-input.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/csv-file-input.md

# CSV File Input

The CSV File Input step reads data from delimited text files into a PDI transformation. While this step is called CSV File Input, you can also use CSV File Input with many other separator types, such as pipes, tabs, and semicolons.

**Note:** The semicolon (;) is set as the default separator type for this step.

**Note:** The options for this step are a subset of the [Text File Input](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/text-file-input-cp) step. This step differs from the Text File Input step in the following ways:

* **NIO**

  Non-blocking I/O is used for native system calls to read the file faster, but is limited to local files. It does not support VFS.
* **Parallel Running**

  If you configure this step to run in multiple copies (or in a clustered mode) and you enable parallel running, each copy will read a separate block of a single file. You can distribute the reading of a file to several threads or even several slave nodes in a clustered transformation.
* **Lazy Conversion**

  Leave the **Lazy Conversion** checkbox selected only if you are reading data from many fields in a file and you want most of the data to pass through the transformation, not be manipulated. For example, data might be passed through a transformation to a text file or database. Lazy conversion can prevent PDI from performing unnecessary work on the data, such as converting data into objects like strings, dates, or numbers. If you are transforming most of the data in a file, and not passing the data through, clear the **Lazy Conversion** checkbox.

An example of a simple CSV input transformation (`CSV Input - Reading customer data.ktr`) can be found in the `data-integration/samples/transformations` directory.
