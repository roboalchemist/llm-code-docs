# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/how-to-enable-kerberos-authentication/set-up-kerberos-for-pentaho.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/secure-the-pentaho-system/big-data-security/how-to-enable-kerberos-authentication/set-up-kerberos-for-pentaho.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/how-to-enable-kerberos-authentication/set-up-kerberos-for-pentaho.md

# Set Up Kerberos for Pentaho

How you can set up Kerberos on a machine that the Pentaho Server can access to connect to Big Data clusters depends on your operating system.

## Configure Kerberos

{% tabs %}
{% tab title="Configure Kerberos on Linux" %}
To configure Linux computers, complete these tasks.

### Configure JCE

The KDC configuration uses an “unlimited” AES-256 encryption setting by default for the Java Cryptographic Extension (JCE) files. However, the import and export control rules about cryptographic software vary by country. If you must change this encryption to remain in compliance, then you can adjust the strength by updating the security property.

**Note:** You may need to consult your export/import control counsel to determine the exact cryptographic policy for your location.

Perform the following steps if you must configure JCE:

1. Open the `pentaho/java/conf/security/java.security` file in any text editor.
2. Locate the # Cryptographic Jurisdiction Policy defaults section and set the `crypto.policy` as shown:

   `crypto.policy=limited`
3. Save the file and close the text editor.

### Modify the Kerberos configuration file

Perform the following steps to modify your Kerberos configuration file:

1. Open the `krb5.conf` file with any text editor.

   The default location is the `/etc` directory.
2. Add your realm, KDC, and Admin Server information as shown in the following example:

   ```
   [libdefaults]
          default_realm = <YOUR_REALM.COM>
   ...

   [realms]
   <YOUR_REALM.COM>= {
   kdc=<KDC IP Address, or resolvable Hostname>
   admin_server=<Admin Server IP Address, or resolvable Hostname>
   ...
   }
   [domain_realm]
   <.your_realm.com> = <YOUR_REALM.COM>
   <your_realm.com> = <YOUR_REALM.COM>
   ```
3. Save and close the configuration file.
4. Restart the computer.

### Synchronize clocks

Synchronize the clock on the Linux client with the clock on the Hadoop cluster. If the timestamp on the client requests differs too much from the clock on the cluster, Kerberos will not authenticate the user. Consult your operating system's documentation for information on setting your systems clock.

### Obtain Kerberos ticket

To obtain a Kerberos ticket, complete these steps.

1. Open a Terminal window and type `kinit` at the prompt.
2. Enter a password when prompted.
3. Make sure that the Kerberos ticket was granted by typing `klist` at the prompt.

   The authentication information appears.
   {% endtab %}

{% tab title="Configure Kerberos for Windows" %}

To configure Kerberos on Windows computers, complete these tasks.

### Configure JCE

The KDC configuration uses an “unlimited” AES-256 encryption setting by default for the Java Cryptographic Extension (JCE) files. However, the import and export control rules about cryptographic software vary by country. If you must change this encryption to remain in compliance, then you can adjust the strength by updating the security property.

**Note:** You may need to consult your export/import control counsel to determine the exact cryptographic policy for your location.

Perform the following steps if you must configure JCE:

1. Open the `pentaho\java\conf\security\java.security` file in any text editor.
2. Locate the # Cryptographic Jurisdiction Policy defaults section and set the `crypto.policy` as shown:

   `crypto.policy=limited`
3. Save the file and close the text editor.

### Download and install Kerberos

Download and install a Kerberos server. We recommend that you use the Heimdal implementation of Kerberos, which can be found here: <https://www.secure-endpoints.com/heimdal/>.

### Modify the Kerberos configuration file

Perform the following steps to modify your Kerberos configuration file:

1. Open the `krb5.conf` file with any text editor. The default location is the `C:\ProgramData\Kerberos` directory.
2. Add your realm, KDC, and Admin Server information as shown in the following example:

   ```
   [libdefaults]
          default_realm = <YOUR_REALM.COM>
   ...

   [realms]
   <YOUR_REALM.COM>= {
   kdc=<KDC IP Address, or resolvable Hostname>
   admin_server=<Admin Server IP Address, or resolvable Hostname>
   ...
   }
   [domain_realm]
   <.your_realm.com> = <YOUR_REALM.COM>
   <your_realm.com> = <YOUR_REALM.COM>
   ```
3. Save and close the configuration file.
4. Make a copy of the configuration file and place it in the `c:\Windows` directory. Rename the file `krb5.ini`.
5. Restart the computer.

### Synchronize clocks

Synchronize the clock on the Windows client with the clock on the Hadoop cluster. If the timestamp on the client requests differs too much from the clock on the cluster, Kerberos will not authenticate the user. Consult your operating system's documentation for information on setting your systems clock. The times on the Windows clock and the Hadoop cluster clock must not be greater than the range you entered for the clockskew variable in `krb5.conf` file. Consult your operating system's documentation for information on setting your systems clock.

### Obtain Kerberos ticket

To obtain a Kerberos ticket, complete these steps.

1. Open a Command Prompt window and type `kinit` at the prompt.
2. Enter a password when prompted.
3. Make sure that the Kerberos ticket was granted by typing `klist` at the prompt.

   The authentication information appears.

   **Note:** If you are using the Heimdal version of Kerberos, the `klist` command output should not have the `Current LoginId is ...` prompt.
   {% endtab %}
   {% endtabs %}

## Set up user accounts and network access for all OS

Ensure that user accounts and network access has been granted. Specific tasks include:

* Ensure the ports you plan to use are open between the cluster and computers running Pentaho components, like the Pentaho Server, Spoon, PRD, and PME.
* Make sure each server can use a hostname to access each computer on the cluster. Test to ensure that IP addresses resolve to hostnames using both forward and reverse lookups.
* Add user account credentials for each Pentaho user needing access to the cluster through the Kerberos database.
* Make sure the UID and GID for the user that you are running your jobs as on the matches the user UID and GID of that user for every computer of the cluster.

## Next step

See the **Install Pentaho Data Integration and Analytics** document to continue configurating your cluster connection with Pentaho.
