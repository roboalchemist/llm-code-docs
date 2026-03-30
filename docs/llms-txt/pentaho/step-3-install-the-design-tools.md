# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/installation-of-the-pentaho-design-tools/install-the-ba-design-tools/perform-a-manual-installation-of-the-ba-design-tools/step-3-install-the-design-tools.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-of-the-pentaho-design-tools/step-3-install-the-design-tools.md

# Step 3: Install the design tools

To install design tool files that you unpacked in [Step 2: Unpack the files](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-of-the-pentaho-design-tools/step-2-unpack-the-files), you must create a directory for each design tool and then move the design tool files into that directory.

Complete the following steps to move the design tool files into the appropriate directories.

1. Create a directory for installing the design tools that has permissions to read, write, and execute commands.

   For example, you can create the `Pentaho/design-tools` directory.

   **Note:** For publishing reports, models, and schemas created with the design tools, it is a best practice to install the design tools in a directory on a workstation or server that is on the same network as the Pentaho Server.
2. In the `design-tools` directory, create a directory for each design tool, as shown in the following table.

   The following table lists the design tools and the file path for each design tool directory.

| Design tool            | Directory file path                                                                                                                                                                                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Aggregation Designer` | `pentaho/design-tools/aggregation-designer`                                                                                                                                                                                                                   |
| `Metadata Editor`      | `pentaho/design-tools/metadata-editor`                                                                                                                                                                                                                        |
| `Report Designer`      | `pentaho/design-tools/report-designer`**Notes:** If you plan to use HIVE as data source for building your model or report, you must also move the files that you unpacked from the `prd-ee-10.2.0.0-<build number>-hadoop-addon.zip` file into the directory. |
| `Schema Workbench`     | `pentaho/design-tools/schema-workbench`                                                                                                                                                                                                                       |

3\. Move the design tool files that you unpacked in \[Step 2: Unpack the files]\(Step%202%20Unpack%20the%20files.md) into the appropriate \`design-tools\` directories.

4. (Optional) If you plan to use HIVE as data source for building your model or report, complete the following substeps to move the additional files that you unpacked in [Step 2: Unpack the files](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-of-the-pentaho-design-tools/step-2-unpack-the-files).
   1. Move the contents of the `pme-ee-10.2.0.0-<build number>-hadoop-addon.zip` file into the `pentaho/design-tools/metadata-editor` directory.
   2. Move the contents of the `prd-ee-10.2.0.0-<build number>-hadoop-addon.zip` file into the `pentaho/design-tools/report-designer` directory.
