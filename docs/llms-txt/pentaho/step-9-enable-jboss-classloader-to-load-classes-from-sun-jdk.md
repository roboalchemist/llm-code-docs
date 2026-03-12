# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/install-jdbc-driver-as-a-module-in-jboss/step-9-enable-jboss-classloader-to-load-classes-from-sun-jdk.md

# Step 9: Enable JBoss classloader to load classes from Sun JDK

JBoss allows a specific set of packages from the JDK to load by default. To configure the Pentaho platform in JBoss, add this list of packages.

1. Locate the `pentaho/server/pentaho-server/<your jboss installation directory>/modules/system/layers/base/sun/jdk/main` directory.
2. Open the `module.xml` file with any text editor.
3. Add these three lines below the list of packages in the `module.xml`.

   ```
   <path name="sun/net/www/protocol/jar"/>
   <path name="sun/net/www/protocol/jar/JarURLConnection"/>
   <path name="com/sun/org/apache/xerces/internal/jaxp/datatype"/>

   ```
4. Save and close the `module.xml` file.
5. Navigate to the `...modules/system/layers/base/sun/jdk/main/service-loader-resources/META-INF/services` directory.
6. Find and remove this driver: **java.sql.Driver.driver**
