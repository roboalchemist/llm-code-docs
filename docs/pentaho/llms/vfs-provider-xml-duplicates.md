# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp/pentaho-server-issues/vfs-provider-xml-duplicates.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/pentaho-server-issues/vfs-provider-xml-duplicates.md

# VFS provider XML duplicates

The `vfs-provider.xml` configuration file may be present in other application JARs that you have deployed to your Java application server. Having multiple instances of this file will cause classpath errors.

To resolve this issue, merge the multiple files into one canonical edition.
