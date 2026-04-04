# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/read-metadata-from-copybook/general-read-metadata-from-copybook.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/read-metadata-from-copybook/general-read-metadata-from-copybook.md

# General

* **Step name**: Specify the unique name of the step on the canvas. You can customize the name or leave it as the default.

![Read metadata from Copybook step](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-d2be7d975025adf74d693a2da9ec29bd0fe8221a%2FPDI_ReadMetadataFromCopybook_dialog.png?alt=media)

## **Schema**

These options define the location of the copybook definition file and include mapping options for the binary data files.

| Option                            | Description                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **COBOL Copybook file path**      | Specify the file path to the copybook definition file. You can enter any VFS or SFTP file path, or click **Browse** to open the system file browser. After selecting a file, click **Validate** to verify that the definition file can be accessed and parsed.                                                                                                                                              |
| **COBOL Copybook line structure** | <p>Specify the line structure of the definition file: - <strong>Standard columns (6 to 72)</strong></p><p>Select this option when the definition file contains line numbers. The first 6 columns of text from each line are ignored. Any data beyond column 72 is ignored.</p><ul><li><strong>Full line</strong></li></ul><p>Select this option when the definition file does not contain line numbers.</p> |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                             |

\## \*\*Binary format\*\*

Use these options to describe the binary format of the selected file:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Option</td><td>Description</td></tr><tr><td><strong>Source architecture</strong></td><td><p>Select the machine architecture of the binary data source files. The values are:- <strong>Big endian (mainframe)</strong></p><p>The most significant byte first and the least significant byte last.</p><ul><li><strong>Little endian</strong></li></ul><p>The least significant byte first and the most significant byte last.</p></td></tr><tr><td><strong>Source charset name</strong></td><td>Select the character encoding set for the binary data file. Mainframe EBCDIC is typically encoded using IBM037 or cp1047 character sets. For more information about character sets and their aliases, see <a href="https://docs.oracle.com/javase/8/docs/technotes/guides/intl/encoding.doc.html">Supported Encodings</a> in the Oracle® documentation.</td></tr><tr><td><strong>Packed decimal (COMP-3) convention</strong></td><td><p>Select how COMP-3 packed decimals are parsed when reading the binary data at runtime of the <a href="../copybook-input-pdi-step">Copybook Input</a> step.</p><ul><li><strong>Strict</strong></li></ul><p>Must follow the IBM S370FPD specification to avoid validation errors. Validation is performed to verify that all nibbles (half-bytes), except the sign nibble, are decimal digits (0-9). This is the default value.</p><pre><code>-   For signed packed decimals, the sign nibble must be C \(positive\) or D \(negative\).
-   For unsigned packed decimals, the sign nibble must be F.
</code></pre><ul><li><strong>Lenient</strong></li></ul><p>Validation is performed to verify that all nibbles contain decimal digits and the sign nibble contains a hexadecimal value of A-F. The sign nibble is only used to interpret a negative number if the value is D.</p><ul><li><strong>Lenient - unchecked</strong></li></ul><p>No validation is performed on the source bytes. The sign nibble may contain any hexadecimal value 0-F, and the last nibble is not included in the result. The sign nibble is only used to interpret a negative number if the value is D.</p><p><strong>Note:</strong> The selection of these options changes the output <code>field_record_type</code> field. See <a href="example-copybook-metadata">Example</a> below.</p></td></tr></tbody></table>

\## \*\*Output\*\*

Use this option to include the metadata of the parent group in the definition file.

* **Extract parent groups?:** Select this check box if you want to include parent group metadata in the output stream. Clear this check box to exclude parent group metadata from the output stream.
