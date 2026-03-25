# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/how-to-enable-kerberos-authentication/use-kerberos-with-mongodb.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/secure-the-pentaho-system/big-data-security/how-to-enable-kerberos-authentication/use-kerberos-with-mongodb.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/how-to-enable-kerberos-authentication/use-kerberos-with-mongodb.md

# Use Kerberos with MongoDB

If you use Kerberos to authenticate access to your installation of MongoDB, with a little extra configuration, you can also use Kerberos to authenticate PDI client users who attempt the access MongoDB through a step in a transformation. When a user attempts to run a transformation that contains a step that connects to a MongoDB cluster to perform a function, the credentials in the step are matched against the credentials in the Kerberos administrative database on MongoDB. If the credentials match, the Kerberos Key Distribution Center (KDC) grants an authorization ticket and access is granted. If not, the user is not authenticated and the step does not run.

To set up Kerberos authentication to provide PDI client users with access to MongoDB you will need to perform several sets of tasks.

* [Complete MongoDB and Client Prerequisites](#complete-mongodb-and-client-prerequisites)
* [Add Users To Kerberos Database](#add-users-to-kerberos-database)
* [Set Up Kerberos Administrative Server and KDC to Start When the Server Starts](#set-up-kerberos-administrative-server-and-kdc-to-start-when-server-starts)
* [Configure Client-Side Nodes](#configure-client-side-nodes)
* [Test authentication with the PDI client using configuration fields](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/Administer/Secure%20the%20Pentaho%20system/Secure%20the%20Pentaho%20System/Big%20data%20security/Kerberos%20authentication%20versus%20secure%20impersonation/How%20to%20Enable%20Kerberos%20Authentication%20-%20Big%20Data%20Security%20Overview/Use%20Kerberos%20with%20MongoDB/Test%20authentication%20with%20the%20PDI%20client%20using%20Configure%20fields=GUID-A2AF85E3-6681-4667-97EC-8E813D6AD3ED=2=en=.md) or [Test authentication with the PDI client using a connection string](#test-authentication-with-the-pdi-client-using-a-connection-string)

## Complete MongoDB and client prerequisites

Make sure that you have completed the following tasks before you move to the next section.

* Make sure that you have installed and configured an Enterprise version MongoDB according to the instructions in the MongoDB installation guide at <http://docs.mongodb.org/manual/installation/>.
* Configure MongoDB to use Kerberos. Instructions for how to do that at <http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication/>.
* Install the current version of the PDI client on each client machine.
* Make sure each client machine can use a hostname to access MongoDB. You should also test to ensure that IP addresses resolve to hostnames using both forward and reverse lookups.

## Add users to Kerberos database

Add the user account credential to the Kerberos database for each PDI client user that should have access to MongoDB. You only need to do this once for each user.

1. Log in as root (or a privileged user), to the server that hosts the Kerberos database.
2. Add user identification to the Kerberos database by completing these steps.
   1. Open a **Terminal** window.
   2. Add the account username to the Kerberos database.

      The username should match the one used to create the user in MongoDB. See the "Create users" section of <http://docs.mongodb.org/manual/tutorial/control-access-to-mongodb-with-kerberos-authentication/> for more details.

      If successful, a message appears indicating that the user has been created.

      ```
      root@kdc1:~# kadmin.local -q "addprinc <username>"
      ...
      Principal "<user name>@DEV.LOCAL" created.
      ```
   3. Repeat for each user you want to add to the database.

## Set up Kerberos Administrative Server and KDC to start when server starts

It is a good practice to start the Kerberos Administrative Server and the KDC when the server boots. One way to do this is to set them up to run as a service. This is an optional, but recommended step.

1. If you have not done so already, log into the server that contains the Kerberos Administrative Server and the KDC.
2. Set the Kerberos Administrative Server to run as a service when the system starts. By default, the name of the Kerberos Administrative Server is kadmin. If you do not know how to do this, check the documentation for your operating system.
3. Set the KDC to run as a service when the system starts. By default, the name of the KDC is krb5kdc.

## Configure client-side nodes

After you have added users to the database and configured the Kerberos admin and KDC to start when the server starts, you are ready to configure each client-side node from which a user might access MongoDB. Client-side nodes should each have a copy of the PDI client already installed. Client-side configuration differs based on your operating system.

{% tabs %}
{% tab title="Configure Linux and Mac client nodes" %}

## Install JCE on Linux and Mac clients

This step is optional. The KDC configuration includes an AES-256 encryption setting. If you want to use this encryption strength, you will need to install the Java Cryptographic Extension (JCE) files.

1. Download the Java Cryptographic Extension (JCE) for the currently supported version of Java from the [Oracle site](https://www.oracle.com/java/technologies/javase-jce8-downloads.html).

   See **Components reference** in the **Try Pentaho Data Integration and Analytics** document for the currently supported version of Java.
2. Read the installation instructions that are included with the download.
3. Copy the JCE jars to the `java/lib/security` directory where PDI is installed on the Linux client machine.

## Download and install Kerberos client on Linux and Mac clients

Download and install a Kerberos client. Check your operating system's documentation for further details on how to do this.

## Modify Kerberos configuration file to reflect Realm, KDC, and admin server on Linux and Mac clients

Modify the Kerberos configuration file to reflect your Realm, KDC, and Admin Server.

1. Open the `krb5.conf` file. By default this file is located in `/etc/krb5.conf`, but it might appear somewhere else on your system.
2. Add your Realm, KDC, and Admin Server information. The information in-between the carats < > indicates where you should modify the code to match your specific environment.

   ```
   [libdefaults]
          default_realm = <correct default realm name>
   	clockskew = 300
   	v4_instance_resolve = false
   	v4_name_convert = {
   		host = {
   			rcmd = host
   			ftp = ftp
   		}
   		plain = {
   			something = something-else
   		}
   	}
   	
   [realms]
   	<correct default realm name>= {
   		kdc=<KDC IP Address, or resolvable Hostname>
   		admin_server=< Admin Server IP Address, or resolvable Hostname>
   	}
   	MY.REALM = {
   		kdc = MY.COMPUTER 
   	}
   	OTHER.REALM = {
   		v4_instance_convert = {
   			kerberos = kerberos
   			computer = computer.some.other.domain
   		}
   	}
   [domain_realm]
   	.my.domain = MY.REALM 
   ```
3. Save and close the configuration file.
4. Restart the computer.

## Specify the location of the Kerberos configuration file on Mac clients that run the PDI client

If you are configuring the PDI client to use Kerberos to authenticate MongoDB on a Mac client, you might need to manually specify where the Kerberos configuration file can be found. Do this if the version of the JRE that the PDI client uses is earlier than Java 1.70\_40, because the JRE attempts to find the Kerberos configuration file in a different location than the default.

1. Use **Finder** to navigate to `design-tools/data-integration/launcher/launcher.properties` file.
2. In the `launcher.properties` file, add a java parameter that indicates the realm and the KDC that you specified in the [Modify Kerberos Configuration File to Reflect Realm, KDC, and Admin Server](#modify-kerberos-configuration-file-to-reflect-realm-kdc-and-admin-server-on-windows-client) step. Make sure to set both of these properties.

   ```
   -Djava.security.krb5.realm=<Kerberos Realm>
   -Djava.secrutiy.krb5.kdc=&lt;Kerberos KDC>
   ```
3. If you need to set additional configuration properties for your Kerberos installation, see "Locating the `krb5.conf` Configuration File" section located in<http://docs.oracle.com/javase/7/docs/technotes/guides/security/jgss/tutorials/KerberosReq.html> for details.
4. Close and save the `launcher.properties` file.

## Specify the location of the Kerberos configuration file on Mac clients that run PRD

If you are configuring the PRD to use Kerberos to authenticate MongoDB on a Mac, you will need to manually specify where the Kerberos configuration file can be found. You must do this if the version of the JRE that the PRD uses is earlier than Java 1.7.0\_40, because it attempts to find the Kerberos configuration file in a different location than the default.

1. Use **Finder** to navigate to the `Pentaho Report Designer.app` file which is in the `design-tools` directory. Right-click and select **Show Package Contents**.
2. Navigate to the **Contents** > **Java**.
3. Open `launcher.properties`. Do not use the `launcher.properties` file that is in the root of the `app` directory.
4. In the `launcher.properties` file, add a java parameter that indicates the realm and the KDC that you specified in the **Modify Kerberos Configuration File to Reflect Realm, KDC, and Admin Server** step. Make sure to set both of these properties.

   ```
   -Djava.security.krb5.realm=<Kerberos Realm>
   -Djava.secrutiy.krb5.kdc=&lt;Kerberos KDC
   ```
5. If you need to set additional configuration properties for your Kerberos installation, see Locating the krb5.conf Configuration File section located in<http://docs.oracle.com/javase/7/docs/technotes/guides/security/jgss/tutorials/KerberosReq.html> for details.
6. Close and save the `launcher.properties` file.

## Synchronize clock on Linux client

Synchronize the clock on the Linux client with the clock on MongoDB host. This is important because if the clocks are too far apart, then when authentication is attempted, Kerberos will not consider the tickets that are granted to be valid and the user will not be authenticated. The times on the Linux client clock and the MongoDB host clock must not be greater than the range you entered for the **clockskew** variable in `krb5.conf` file when you completed the steps in the previous task, *Modify Kerberos configuration file to reflect Realm, KDC, and admin server on Linux and Mac clients*.

Consult your operating system's documentation for information on how to properly set your clock.

## Obtain Kerberos ticket on Linux client

To obtain a Kerberos ticket, complete these steps.

1. Open a **Terminal** window and type `kinit` at the prompt.
2. When prompted for a password, enter it.

   The prompt appears again.
3. To ensure that the Kerberos ticket was granted, type `klist` at the prompt.

   Authentication information appears.
   {% endtab %}

{% tab title="Configure Windows client nodes" %}

## Install JCE on Windows client

This step is optional. The KDC configuration includes an AES-256 encryption setting. If you want to use this encryption strength, you will need to install the Java Cryptographic Extension (JCE) files.

1. Download the Java Cryptographic Extension (JCE) for the currently supported version of Java from the [Oracle site](https://www.oracle.com/java/technologies/javase-jce8-downloads.html).

   See **Components reference** in the **Try Pentaho Data Integration and Analytics** document for the currently supported version of Java.
2. Read the installation instructions that are included with the download.
3. Copy the JCE jars to the `java\lib\security` directory where PDI is installed.

## Download and install Kerberos client on Windows client

Download and install a Kerberos client. We recommend that you use the Heimdal implementation of Kerberos, which can be found here: <https://www.secure-endpoints.com/heimdal/>.

## Modify Kerberos configuration file to reflect Realm, KDC, and admin server on Windows client

You will need to modify the Kerberos configuration file to reflect the appropriate realm, KDC, and Admin Server.

1. Open the `krb5.conf` file. By default this file is located in `c:\Program Data\Kerberos`. This location might be different on your system.
2. Add the appropriate realm, KDC, and admin server information. An example of where to add the data appears below.

   ```
   [libdefaults]
          default_realm = <correct default realm name>
   	clockskew = 300
   	v4_instance_resolve = false
   	v4_name_convert = {
   		host = {
   			rcmd = host
   			ftp = ftp
   		}
   		plain = {
   			something = something-else
   		}
   	}
   	
   [realms]
   	<correct default realm name>= {
   		kdc=<KDC IP Address, or resolvable Hostname>
   		admin_server=< Admin Server IP Address, or resolvable Hostname>
   	}
   	MY.REALM = {
   		kdc = MY.COMPUTER 
   	}
   	OTHER.REALM = {
   		v4_instance_convert = {
   			kerberos = kerberos
   			computer = computer.some.other.domain
   		}
   	}
   [domain_realm]
   	.my.domain = MY.REALM 
   ```
3. Save and close the configuration file.
4. Make a copy of the configuration file and place it in the `c:\Windows` directory. Rename the file `krb5.ini`.
5. Restart the computer.

## Synchronize clock on Windows client

Synchronize the clock on the Windows client with the clock on the MongoDB host. This is important because if the clocks are too far apart, then when authentication is attempted, Kerberos will not consider the tickets that are granted to be valid and the user will not be authenticated. The times on the Windows client clock and the MongoDB host's clock must not be greater than the range you entered for the **clockskew** variable in `krb5.conf` file when you completed the steps in the previous task, *Modify Kerberos Configuration File to Reflect Realm, KDC, and Admin Server on Windows Client*.

Consult your operating system's documentation for information on how to properly set your clock.

## Obtain Kerberos ticket on Windows client

To obtain a Kerberos ticket, complete these steps.

1. Open a **Command Prompt** window and type `kinit` at the prompt.
2. When prompted for a password, enter it.

   The prompt appears again.
3. To ensure that the Kerberos ticket was granted, type `klist` at the prompt.

   Authentication information appears.
   {% endtab %}
   {% endtabs %}

## Test authentication with the PDI client

Use one of the following options to test authentication with the PDI client.

{% tabs %}
{% tab title="Use configuration fields" %}
To test the authentication from within the PDI client , create a transformation that contains a MongoDB Input that connects to MongoDB using configuration fields.

Verify that you have the permission to read a database and the corresponding collections on the instance of MongoDB you want to connect to.

1. Start the PDI client.
2. Create a new transformation.
3. Drag the MongoDB Input step to the canvas and open the step.
4. Click **Configure Fields**.
5. Enter the host name of the MongoDB instance and port for MongoDB.
6. In the username field, indicate the Kerberos principal, using this format: `<primary>/<instance>@KERBEROS_REALM`. Be sure to include the forward slash. Also note that the Kerberos Realm is case sensitive. Check with your administrator if you do not know your Kerberos principal.
7. Leave the **password** field blank.
8. Click the **Authenticate using Kerberos** checkbox.
9. Click the **Input options** tab, then enter the name of a database on MongoDB to which you have read permissions.
10. Click the **Get Collections** button. You should be able to see the databases you have read access to, as well as the collections in the drop-down lists.
11. Click the **Preview** button. If you see data, then you know that Kerberos is working properly.
    {% endtab %}

{% tab title="Use a connection string" %}
To test the authentication from within the PDI client , create a transformation that contains a MongoDB Input that connects to MongoDB using a connection string.

Verify that you have the permission to read a database and the corresponding collections on the instance of MongoDB you want to connect to.

1. Start the PDI client.
2. Create a new transformation.
3. Drag the MongoDB Input step to the canvas and open the step.
4. Click **Connection String**.
5. Enter the host name of the MongoDB instance and port for MongoDB.
6. Provide the connection string to authenticate using Kerberos. For example: `mongodb://<service-principal>@<hostname>:<port>/?authSource=$external&authMechanism=GSSAPI`
7. Click **Test** to make sure the connection is successful.
8. Click the **Input options** tab, then enter the name of a database on MongoDB to which you have read permissions.
9. Click the **Get Collections** button. You should be able to see the databases you have read access to, as well as the collections in the drop-down lists.
10. Click **Preview**. If you see data, then you know that Kerberos is working properly.
    {% endtab %}
    {% endtabs %}
