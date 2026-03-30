# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/s3-file-output-cp/big-data-warning.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/s3-file-output-cp/big-data-warning.md

# Big Data warning

Because data cannot be appended to S3 using an ‘append mode,’ and the data to send to S3 is generated in memory, an `Out Of Memory Exception` (OOME) error may occur followed by the `java.io.IOException: Read end dead` exception error when the transformation attempts to close the file.

You can use one of the following actions to avoid these errors:

* Increase the **Java Heap Space** (**Xmx**) setting for Spoon (see the **Install Pentaho Data Integration and Analytics** document).
* Set the kettle property `s3.vfs.useTempFileOnUploadData=Y`.

Using the latter method, the system can now generate a temporary file with data and upload it to Amazon S3. In most cases, the user has enough free space to store the temporary file and write permissions on the default temporary-file directory.

When the S3 File Output step generates a file, the S3 VFS system uploads the file to S3 using a multi-part upload.The default size of the parts is 5 MB to avoid the 20 seconds inactivity timeout for the part uploads. A new variable, *s3.vfs.partSize*, has been added to the to the kettle.property file enabling you to change the default to improve perform ance in your environment. The value range is from 5MB to 1GB in the format `XMB` and `XGB`, Where `X` is a whole number or a one decimal place number such as 5 or 5.5.
