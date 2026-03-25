# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/copybook-input-pdi-step/before-you-begin-copybook-input-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/copybook-input-pdi-step/before-you-begin-copybook-input-step.md

# Before you begin

Review these prerequisites before using the Copybook Input step.

* For PDI to process binary data files, you must first download both the copybook definition file and the binary data files from the mainframe environment. For example, you can use FTP or an SFTP server to download the files to a staging area accessible from PDI. You can also use a [SFTP VFS](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/parameters/vfs-properties) path to connect to and read data directly from the mainframe at runtime.
* The binary data file must remain in binary format when used as input to this step. If you are using FTP to download the files, ensure that the data file is not converted to ASCII.
* This step works with Fixed Length COBOL records only. Variable record types such as `VB`, `VBS`, `OCCURS DEPENDING ON` are not supported.
* Your mainframe administrator can provide more details about the environment-specific copybook file definitions and structures this step requires for reading binary data.
