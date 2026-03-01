# Source: https://docs.curator.interworks.com/setup/authentication/active_directory.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Active Directory

> A guide to setting up Active Directory authentication for Curator.

## Web Server Setup (Apache)

1. Find the **`curator.conf`** file (default location is `C:\InterWorks\Curator\curator.conf`).

2. Un-comment the lines (by deleting the `#` at the front of the line) starting at
   `LoadModule authnz_sspi_module modules/mod_authnz_sspi.so` and ending at `</Location>`.  See example below:

   ```conf  theme={null}
   # Uncomment the lines below for AD automatic login
   LoadModule authnz_sspi_module modules/mod_authnz_sspi.so
   <Location />
       AuthName "Curator"
       AuthType SSPI
       SSPIAuth On
       SSPIAuthoritative On
       <RequireAll>
           <RequireAny>
               Require valid-user
           </RequireAny>
           <RequireNone>
               Require user "ANONYMOUS LOGON"
           </RequireNone>
       </RequireAll>
   </Location>
   ```

3. After the configuration file has been edited and saved, restart the webserver.

## Curator Setup

After you have completed the Curator installation and the Web Server Setup steps above, you can enable Active
Directory/Kerberos on Curator.

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Security** > **Authentication Settings** section from the left-hand menu.
3. Change the "Authentication Type" to  **Active Directory / Kerberos**.
