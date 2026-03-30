# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-your-linux-environment-for-a-manual-installation/advanced-linux-considerations/systems-without-video-cards.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/prepare-your-linux-environment-for-an-archive-install/advanced-linux-considerations/systems-without-video-cards.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/prepare-your-linux-environment-for-an-archive-install/advanced-linux-considerations/systems-without-video-cards.md

# Systems without video cards

The **java.awt.headless** parameter enables systems without video output and/or human input hardware to execute operations that require them. To set this application server option to be applied at every Pentaho Server startup, you will need to modify the startup scripts for either the Pentaho Server or your Java application server.

Prior to starting the Pentaho Server the first time, add the **-Djava.awt.headless=true** parameter to the list of **CATALINA\_OPTS** parameters.

**Note:** The startup process will fail if an environment variable setting is not valid or is incorrect. When modifying any environment variable in the startup file, make sure its setting is valid and correct.

The entire line should look like this:

```

export CATALINA_OPTS="-Djava.awt.headless=true -Xms4096m -Xmx6144m -XX:MaxPermSize=256m -Dsun.rmi.dgc.client.gcInterval=3600000 -Dsun.rmi.dgc.server.gcInterval=3600000"

```

If you intend to create a Pentaho Server service control script, you must add this same parameter to that script's **CATALINA\_OPTS** line.
