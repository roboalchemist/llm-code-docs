# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/installation-and-upgrade-issues/context-xml-changes-do-not-take-effect-after-deploying-a-war.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-and-upgrade-issues/context-xml-changes-do-not-take-effect-after-deploying-a-war.md

# Context XML changes do not take effect after deploying a WAR

With a manual installation, if you deploy a WAR with a custom `context.xml`, the `context.xml` file may not be overwritten.

The location and naming convention for this file are: `$CATALINA_HOME/conf/Catalina/*host*/*war name*.xml`. An example of this file path is `/tomcat/conf/Catalina/localhost/pentaho.xml`. If this file exists, you will have to delete it prior to deploying the `pentaho.war` if you have made any changes to `context.xml`.
