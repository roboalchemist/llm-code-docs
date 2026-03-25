# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/installation-and-upgrade-issues/pentaho-server-does-not-start-when-installed-on-a-virtual-machine.md

# Pentaho Server does not start when installed on a virtual machine

The Pentaho Server does not start when installed on a Virtual Machine and deployed on the JBoss web application server.

To fix this problem, increase the amount of time JBoss allows for application deployment to 240 seconds or longer. For information on how to increase the amount of time, see [Step 1: Increase the amount of time JBoss allows for Pentaho Server deployment](https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/prepare-jboss-web-application-servers/step-1-increase-the-amount-of-time-jboss-allows-for-pentaho-server-deployment).
