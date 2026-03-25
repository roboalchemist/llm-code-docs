# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/prepare-jboss-web-application-servers/step-1-increase-the-amount-of-time-jboss-allows-for-pentaho-server-deployment.md

# Step 1: Increase the amount of time JBoss allows for Pentaho Server deployment

By default, JBoss allows up to one minute for a web application to be deployed; otherwise, an error occurs. Because the Pentaho Server deployment requires more than one minute, manually edit the `standalone.xml` file to increase the deployment time.

1. Use a text editor to open the `<your jboss installation directory>/standalone/configuration/standalone.xml` file
2. Find the **deployment-scanner** tag, add the **deployment-timeout** attribute, then set the attribute equal to *3600*.

   **Note:** If you are installing the Pentaho Server on a VM, you might want to increase the **deployment-timeout** attribute's value to give the Pentaho Server more time to deploy.

   ```xml

   <deployment-scanner scan-interval="5000" relative-to="jboss.server.base.dir" path="deployments" scan-enabled="true" deployment-timeout="3600"/>
   ```
3. Save and close the file.
