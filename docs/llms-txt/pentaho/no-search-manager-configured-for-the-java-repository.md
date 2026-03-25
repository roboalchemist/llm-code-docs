# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/installation-and-upgrade-issues/no-search-manager-configured-for-the-java-repository.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-and-upgrade-issues/no-search-manager-configured-for-the-java-repository.md

# No search manager configured for the Java repository

If you see a `Javax.jcr.RepositoryException:no search manager configured for this workspace` error message in your Pentaho Server log, then there was an error in the PDI upgrade process. Specifically, the `SearchIndex` XML nodes were not properly modified.

To fix this problem, refer to [Post-upgrade tasks](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp) and closely follow the instructions for modifying repository configuration files.
