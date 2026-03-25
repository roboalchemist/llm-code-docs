# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/installation-and-upgrade-issues/jboss-fails-to-start/jboss-fails-to-start-after-manually-unpacking-pentaho-war.md

# JBoss fails to start after manually unpacking Pentaho WAR

If you unpack the WAR file to any other folder name, including `pentaho` without the `.war` extension, JBoss will fail to deploy the WAR without any meaningful warnings.

You must also name the resultant folder `pentaho.war` when manually unpacking the `pentaho.war` file.
