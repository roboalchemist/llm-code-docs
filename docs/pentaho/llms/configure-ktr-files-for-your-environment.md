# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/work-with-the-streamlined-data-refinery/install-and-configure-the-streamlined-data-refinery/configure-ktr-files-for-your-environment.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/install-and-configure-the-streamlined-data-refinery/configure-ktr-files-for-your-environment.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/install-and-configure-the-streamlined-data-refinery/configure-ktr-files-for-your-environment.md

# Configure KTR files for your environment

If you are not using Postgres and a default installation, you will need to configure a few of the sample KTR files in Spoon to use the SDR form.

1. Click **File** > **Open** and navigate to find the `SDR_data.ktr` in this directory: `pentaho/server/pentaho-server/pentaho-solutions/system/SDR/endpoints/kettle`.
   1. Right-click on the Set Local Variables step to edit, and enter the URL for your Pentaho Server.
   2. Click **OK**.
2. In the same transformation, right-click on the Call\_ML\_SDR job and select **Open Referenced Object** > **Job** to open the `_ML_SDR.job`.
   1. Right-click to edit the Create Table step to point to your staging database.
   2. Click **OK**.
3. Right-click to edit the Publish Model step and, if requested, enter your user id and password for the Pentaho Server.
   1. Click **Test Connection**.
   2. Click **OK**.
4. Open the `_ML_SDR_REFINERY.ktr`.
   1. Right-click to edit the Out to Staging DB step.
   2. Select your staging database from the drop-down menu.
5. Save all of these files and exit out of the PDI client.
6. Restart the Pentaho Server.
