# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/installation-and-upgrade-issues/not-able-to-login-or-run-transformations.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-and-upgrade-issues/not-able-to-login-or-run-transformations.md

# Not able to login or run transformations

If you have manually upgraded to 8.0 from a previous version of Pentaho that used a DI Server and are not able to login or run transformations perform one or both of the following steps:

1. Check the file size of the `pentaho-solutions/system/pentaho.xml` file.

   If the file size is 0 KB, then the file is corrupted and must be replaced.
2. To resolve this issue, copy the file from your 7.1 DI server to the 8.0 Pentaho Server.
