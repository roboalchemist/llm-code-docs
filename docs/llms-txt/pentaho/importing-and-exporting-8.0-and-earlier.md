# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp/pentaho-repository-issues/importing-and-exporting-8.0-and-earlier.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/pentaho-repository-issues/importing-and-exporting-8.0-and-earlier.md

# Importing and exporting PDI content with Pentaho 8.0 and earlier

When you export the contents of the repository from Pentaho version 8.0 or earlier and import them into a later version, an error occurs. This error may occur because you are attempting to export/import the entire repository, which may include items from repository locations that have restricted access in later versions of Pentaho.

Here's how you can resolve this error: To import or export PDI content that was created in Pentaho 8.0 or earlier, select specific content and not the entire repository. If you are working with multiple selections, export each one separately.

Also note that you do not need to export your Ops Mart content because it is automatically included and updated for each new version of Pentaho.
