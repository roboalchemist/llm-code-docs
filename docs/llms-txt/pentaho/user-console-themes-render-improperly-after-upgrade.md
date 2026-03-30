# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/installation-and-upgrade-issues/user-console-themes-render-improperly-after-upgrade.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-and-upgrade-issues/user-console-themes-render-improperly-after-upgrade.md

# User Console themes render improperly after upgrade

There are two possible causes for improperly rendered User Console themes:

* If you are seeing unusual rendering problems in the User Console shortly after performing a Pentaho Server upgrade, the problem may be related to old JavaScript files being held in the browser cache:

  To fix this problem, clear your web browser's cache, then reload the Pentaho User Console.
* If the login page appears blank with all input fields left-justified:

  To fix this problem, stop the Pentaho Server. Navigate to the `pentaho/server/pentaho-server/pentaho-solutions/system` directory and open the `pentaho.xml` file with any text editor. Edit the **\<default-theme>** parameter so that only lower-case letters are used in the parameter value (for example, `ruby`, `crystal`, or `sapphire`). Save and close the file. Start the Pentaho Server.
