# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-your-linux-environment-for-a-manual-installation/set-environment-variables.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-your-windows-environment-for-a-manual-installation/set-environment-variables.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/prepare-your-linux-environment-for-an-archive-install/set-environment-variables.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/prepare-your-windows-environment-for-an-archive-install/set-environment-variables.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/prepare-your-linux-environment-for-an-archive-install/set-environment-variables.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/prepare-your-windows-environment-for-an-archive-install/set-environment-variables.md

# Set environment variables

If you do not set the **HOME** environment variables, Pentaho does not start correctly. Complete the steps in this topic to ensure that you have set the **HOME** environment variables properly.

1. Set the path of the **PENTAHO\_JAVA\_HOME** variable to the path of your Java installation, as shown:

   `SET PENTAHO_JAVA_HOME=C:\Program Files\Java\jdk11.x.x.x`
2. (Optional) If you are using a JRE, then also set the **JRE\_HOME** home environment variable.
3. Log off and log on again, then verify the variables have been properly set by using a command similar to the following example:

   `ECHO %PENTAHO_JAVA_HOME%`
