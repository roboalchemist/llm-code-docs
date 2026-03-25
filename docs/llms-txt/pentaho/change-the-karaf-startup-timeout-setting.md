# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-server/advanced-topics/customize-the-pentaho-server/change-the-karaf-startup-timeout-setting.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/change-the-karaf-startup-timeout-setting.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/change-the-karaf-startup-timeout-setting.md

# Change the Karaf startup timeout setting

Upon start up, the system waits for Karaf to install all of its features before timing out. If you modify Karaf and it now takes longer to install during start up, you may need to extend the default timeout setting to allow Karaf more time to install. The current default timeout is: 120000 (milliseconds - about 2 minutes).

You can change this default timeout by editing the `server.properties` file.

1. Stop the Pentaho Server.
2. Navigate to the `/pentaho-server/pentah﻿o-s﻿olutions/system`﻿﻿﻿ directory.
3. Open the `server.properties` file with any text editor, and search for the **karafWaitForBoot** parameter.
4. Uncomment the line containing the parameter and set it to your desired wait time in milliseconds

   ```xml
   # This sets the amount of time the system will wait for karaf to install all of
   # it's features before timing out.  The default value is 2 minutes but can be
   # overridden here.
   #karafWaitForBoot = 120000
   ```
5. Save and close the file.
6. Restart the Pentaho Server
