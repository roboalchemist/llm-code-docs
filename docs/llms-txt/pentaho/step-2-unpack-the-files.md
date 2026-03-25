# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/installation-of-the-pentaho-design-tools/install-the-ba-design-tools/perform-a-manual-installation-of-the-ba-design-tools/step-2-unpack-the-files.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-of-the-pentaho-design-tools/install-the-pdi-tools-and-plugins/step-2-unpack-the-files.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-of-the-pentaho-design-tools/step-2-unpack-the-files.md

# Step 2: Unpack the files

Unpack the compressed Pentaho Business Analytics design tool files that you downloaded in [Step 1: Download files](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-of-the-pentaho-design-tools/step-1-download-files) so that you can move the files into the appropriate directories for installation.

**Note:** If you plan to use HIVE as data source for building your model or report, unpack the Metadata Editor and Report Designer Hadoop add-on files after you unpack the Metadata Editor and Report Designer design tools.

1. Locate the files that you downloaded in [Step 1: Download files](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-of-the-pentaho-design-tools/step-1-download-files).
2. Unpack the following files into a temporary directory.

   **CAUTION:**

   Do not use Unarchiver 3.3 to unpack files because Unarchiver 3.3 might corrupt the plugin file names.

   The following table lists the file to unpack for each design tool.

| Design tool            | File to unpack                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Aggregation Designer` | `pad-ee-10.2.0.0-<build number>.zip`                                                                                                                                                                                                                                                                                                                                                |
| `Metadata Editor`      | `pme-ee-10.2.0.0-<build number>.zip`**Note:** If you plan to use HIVE as data source for building your model or report, you must also unpack `pme-ee-10.2.0.0-<build number>-hadoop-addon.zip`.                                                                                                                                                                                     |
| `Report Designer`      | <p><code>prd-ee-10.2.0.0-\<build number>.zip</code><strong>Notes:</strong></p><ul><li>If you plan to use HIVE as data source for building your model or report, you must also unpack <code>prd-ee-10.2.0.0-\<build number>-hadoop-addon.zip</code>.</li><li>For <code>prd-ee</code> Mac OS users, the unique file is included as part of the <code>prd-ee</code> package.</li></ul> |
| `Schema Workbench`     | `psw-ee-10.2.0.0-<build number>.zip`                                                                                                                                                                                                                                                                                                                                                |
