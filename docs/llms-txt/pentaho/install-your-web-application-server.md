# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-your-linux-environment-for-a-manual-installation/install-your-web-application-server.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-your-windows-environment-for-a-manual-installation/install-your-web-application-server.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-your-linux-environment-for-a-manual-installation/install-your-web-application-server.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-your-windows-environment-for-a-manual-installation/install-your-web-application-server.md

# Install your web application server

If you want to install Pentaho on your own Tomcat web application server, you will first need to install that web application server. You must complete the installation yourself.

**Note:** If you already have a Tomcat web application server installed and you want to run the Pentaho Server on it, you can skip this task.

The Pentaho Server can be deployed on your own Tomcat web application server. Perform the following steps to install your web application server:

1. Check the [Components Reference](https://docs.pentaho.com/install/10.2-install/components-reference) to see which version of Tomcat is supported by Pentaho.
2. To download and install the web application software, use the instructions in the documentation for the web application server.

   We recommend that you install the web application server in the `pentaho\server\pentaho-server` directory.
3. Verify the web application server is installed correctly by starting it and viewing the default page.

   If the web application server does not start, troubleshoot it using the web application server's documentation before you continue with the Pentaho Server installation process.
4. Stop the web application server.
