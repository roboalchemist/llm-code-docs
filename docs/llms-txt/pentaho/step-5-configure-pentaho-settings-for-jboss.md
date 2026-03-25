# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/prepare-jboss-web-application-servers/step-5-configure-pentaho-settings-for-jboss.md

# Step 5: Configure Pentaho settings for JBoss

Before you deploy the Pentaho Server, update the Pentaho configuration settings for JBoss.

1. Edit `/pentaho-solutions/system/karaf/etc/config.properties` to **add \_\_redirect** to the **bootdelegation** property, as shown in the following example:

   ```
   org.osgi.framework.bootdelegation =__redirected,
       com.sun.*, \
       javax.transaction, \
       javax.transaction.*, \
       javax.xml.crypto, \
       javax.xml.crypto.*, \
       jdk.nashorn.*, \
       sun.*, \
       jdk.internal.reflect, \
       jdk.internal.reflect.*, \
       org.apache.karaf.jaas.boot, \
       org.apache.karaf.jaas.boot.principal
   ```
2. Edit `/pentaho-solutions/system/karaf/etc/custom.properties` to change **org.apache.xerces.\*; version\\=”2.9.1”** to: **org.apache.xerces.\*; version\\=”2.11.0”**
3. Optionally, you can add JBoss logging.

   We recommend completing the steps in the [Adding JBoss logging](https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/prepare-jboss-web-application-servers/step-5-configure-pentaho-settings-for-jboss/add-jboss-logging) article, and then running the appropriate script for starting your server.
