# Source: https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent

Title: Proxy Agent | Fivetran database connection methods

URL Source: https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent

Markdown Content:
The Fivetran Proxy Agent enables Fivetran to securely connect to data sources that are not publicly accessible, such as databases in private networks or on-premises environments. The Proxy Agent runs inside your network and establishes an outbound-only connection to the Fivetran Managed SaaS. This design allows Fivetran to communicate with your database without opening inbound firewall ports or exposing the source to the public internet.

Each Proxy Agent is uniquely identified by an agent ID in its configuration file (`config.json`). Only _one_ Proxy Agent process can be active for a given agent ID at a time.

Do _not_ run multiple Proxy Agent processes using the same configuration file or agent ID. Doing so can disconnect the agent and cause connection sync failures and other unexpected behavior.

**Security and network communication**

The Proxy Agent establishes and maintains an outbound gRPC control connection to Fivetran over port `443`, secured with mutual TLS (mTLS). During normal operation, the agent may also open additional outbound TLS-encrypted connections over port `443` as needed. See the [list of IP addresses](https://fivetran.com/docs/using-fivetran/ips#fivetranproxyusers) that must be allowed in your firewall.

The Proxy Agent supports TLS 1.3 and earlier versions.

Proxy Agent versions prior to v1.1.0, bundled with High-Volume Agent version 6.1.0_79 and earlier, use WebSockets (over TLS) to communicate with the Fivetran Proxy Server.

**Region scope**

The Proxy Agent is configured for a specific destination region and can only handle connections that run in the same region. For example, if the Proxy Agent is configured for `us-east4`, and both BigQuery and Snowflake destinations run in that region, the Proxy Agent can be used for both connections.

* * *

System requirements[](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#systemrequirements)
-----------------------------------------------------------------------------------------------------------------------

Proxy Agent requires the following system resources:

*   **CPU:** Minimum 4 vCPUs with x86-64 processors
*   **Memory:** Minimum 5 GB of RAM
*   **Storage:** Minimum 2 GB allocated disk space for the executables and logs
*   **Java:** The Proxy Agent includes a bundled Java Runtime Environment (JRE) based on open-source Azul Zulu JDK. You do not need to install or purchase any additional Java licenses.

* * *

Supported connectors[](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#supportedconnectors)
-------------------------------------------------------------------------------------------------------------------------

You can use Proxy Agent with the following connectors:

*   [HVA Db2 for i](https://fivetran.com/docs/connectors/databases/hva-db2i)
*   [HVA Oracle](https://fivetran.com/docs/connectors/databases/oracle/hva-oracle)
*   [HVA SAP ECC on Oracle](https://fivetran.com/docs/connectors/databases/sap/high-volume-agent/hva-sap-ecc-oracle)
*   [HVA SQL Server](https://fivetran.com/docs/connectors/databases/sql-server/hva-sql-server)
*   [MariaDB](https://fivetran.com/docs/connectors/databases/mariadb)
*   [MongoDB](https://fivetran.com/docs/connectors/databases/mongodb)
*   [MySQL](https://fivetran.com/docs/connectors/databases/mysql)
*   [Oracle](https://fivetran.com/docs/connectors/databases/oracle/oracle-connector)
*   [PostgreSQL](https://fivetran.com/docs/connectors/databases/postgresql)
*   [SAP ERP on HANA](https://fivetran.com/docs/connectors/databases/sap/sap-erp-hana)
*   [SQL Server](https://fivetran.com/docs/connectors/databases/sql-server)

For the supported High-Volume Agent (HVA) connectors, this connection method requires the Proxy Agent to be installed on the HVA's host or on a host that has access to HVA. See the sample system architecture with Proxy Agent and HVA below.

![Image 1: Proxy Agent System Architecture](https://fivetran.com/static-assets-docs/_next/static/media/proxy-agent-system-architecture.7c63ee0c.webp)

For non-HVA connectors, the source communicates directly with the Proxy Agent.

![Image 2: Proxy Agent Non-HVA System Architecture](https://fivetran.com/static-assets-docs/_next/static/media/proxy-agent-non-hva-architecture.23017ba5.webp)

*   A Proxy Agent can support multiple connections. However, we recommend that you use a maximum of 30 connections per Proxy Agent.
*   A Proxy Agent can only be used for connections within a single Fivetran cloud processing region, but it can be used by any connection in your account that runs in that region. For example, a Proxy Agent configured for the `AZURE_EASTUS2` region cannot be used by a connection that runs in the `GCP_US_EAST4` region. In that case, you must use a separate Proxy Agent that is configured for the `GCP_US_EAST4` region.

* * *

Configure Proxy Agent[](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#configureproxyagent)
--------------------------------------------------------------------------------------------------------------------------

Follow the instructions below to configure a connection through the Proxy Agent.

Proxy Agents configured after June 10, 2025 must use the Proxy Agent bundled with High-Volume Agent version 6.1.0/79 or later.

### Certificate management options[](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#certificatemanagementoptions)

The Proxy Agent uses a client certificate and private key to authenticate to Fivetran. You can manage these credentials using one of the following methods:

*   **Embedded certificate method (default)**:Fivetran generates the client certificate and private key and embeds them directly inside the Proxy Agent configuration file (`config.json`). This is the simplest and recommended method for most deployments.

*   **KeyStore method (advanced)**:You store the Fivetran-generated client certificate and private key in a secure PKCS12 KeyStore file. This method is available in Proxy Agent version 1.1.4 or later, which is bundled with High-Volume Agent version 6.1.0_90 and later.

Using a KeyStore provides the following benefits:

    *   Encrypted, password-protected storage for the certificate and private key
    *   Separation of configuration (`config.json`) and sensitive credentials (certificate and private key)

Both methods require generating the Proxy Agent configuration file (`config.json`). If you plan to use the KeyStore method, you will extract the embedded certificate and private key from this file for use in your KeyStore. See [Configure Proxy Agent to use KeyStore](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#configureproxyagenttousekeystoreoptional).

### Generate Proxy Agent settings[](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#generateproxyagentsettings)

Follow the instructions below to generate the Proxy Agent configuration file (`config.json`), which contains the settings and authentication parameters required to establish secure communication between the Proxy Agent and Fivetran. This file is also required to install the Proxy Agent.

In Fivetran's setup form, do the following:

1.   In the **Connection Method** drop-down menu, select **Connect via proxy agent**.

2.   Click **Configure a new proxy agent**.

![Image 3: ConnectionMethodProxyAgent](https://fivetran.com/static-assets-docs/_next/static/media/ConnectionMethodProxyAgent.217f4951.webp)
3.   Proceed to the **Configure a new proxy agent** dialog.

4.   Download [High-Volume Agent](https://fivetran.com/dashboard/account/downloads) if you have not already. Then, select the **I've downloaded the agent** checkbox and click **Next**.

![Image 4: DownloadProxyAgent](https://fivetran.com/static-assets-docs/_next/static/media/DownloadProxyAgent.a59ec574.webp)
5.   Enter a name for your Proxy Agent and  click **Generate proxy agent config** to generate a Proxy Agent configuration file.

![Image 5: ConfigureProxyAgent](https://fivetran.com/static-assets-docs/_next/static/media/ConfigureProxyAgent.203f7e95.webp)
6.   Download the generated Proxy Agent configuration file (`config.json`) and save it in a location that is easy to access. You will need this file for the installation of the Proxy Agent.

The configuration file contains the settings and authentication parameters required to establish secure communication between the Proxy Agent and Fivetran. ![Image 6: DownloadProxyAgentConfig](https://fivetran.com/static-assets-docs/_next/static/media/DownloadProxyAgentConfig.037b7522.webp)
7.   Select the **I have downloaded the file** checkbox and click **Save** to finalize the Proxy Agent configuration.

8.   (Optional): If the Proxy Agent needs to forward traffic through an intermediate network proxy to reach Fivetran, add the following configuration to your `config.json` file:

Do not include `http://` or `https://` in the `<proxy_host>` value. ```
proxy_host: "<proxy_host>",
proxy_port: "<proxy_port>"
``` 

### Configure Proxy Agent to use KeyStore (optional)[](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#configureproxyagenttousekeystoreoptional)

If you are using the [**KeyStore method**](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#certificatemanagementoptions) for certificate management, follow the steps in this section. Skip this step if you are using the default **Embedded certificate method**.

Configure the Proxy Agent to use a KeyStore
**Prerequisites**:

*   Proxy Agent version 1.1.4 or later (bundled with High-Volume Agent version 6.1.0_90 and later).
*   On Linux, the Proxy Agent service runs as `root`.
*   On Windows, the Proxy Agent service runs under the `LocalSystem` account.
*   OpenSSL version 1.0.1 or later installed (which is required to convert PEM files into a PKCS12 KeyStore).

Perform the following steps to prepare and configure the KeyStore:

1.   Extract the certificate and private key from the generated `config.json` file into PEM files. Run the following commands in the directory where the `config.json` file is located:

Ensure you have `jq` installed on your system. If not, follow the instructions in the [jq installation guide](https://stedolan.github.io/jq/download/). ```
jq -r .client_cert < config.json > certificate.pem
jq -r .client_private_key < config.json > private_key.pem
``` 
2.   Convert the PEM certificate and private key into a PKCS12 KeyStore file.

OpenSSL is required to convert the PEM certificate and private key into a PKCS12 KeyStore file. Ensure that OpenSSL version 1.0.1 or later is installed. Earlier versions do not support the SHA-256 algorithms required for PKCS12 keystores. If OpenSSL is not installed already, install it using either your operating system’s package manager or by downloading the source from the [OpenSSL project website](https://www.openssl.org/source/). 
    *   **Linux**:

```
sudo openssl pkcs12 -export \
  -in certificate.pem \
  -inkey private_key.pem \
  -out keystore.p12 \
  -name orchestrator.fivetran.com \
  -passout pass:<your_secure_password>
``` 
    *   **Windows**:

```
openssl pkcs12 -export -in certificate.pem -inkey private_key.pem -out keystore.p12 -name orchestrator.fivetran.com -passout pass:<your_secure_password>
``` 

3.   Ensure the KeyStore file is readable by the account that runs the Proxy Agent service:

    *   On Linux, the Proxy Agent service runs as `root`. Creating the KeyStore file with `sudo` ensures that `root` can read the file.

    *   On Windows, the Proxy Agent service runs under the `LocalSystem` account.

Grant read access to the KeyStore file for `LocalSystem`. Replace `<path_to_keystore>` with the full path to your KeyStore file:

```
icacls <path_to_keystore> /grant:r "NT AUTHORITY\SYSTEM":R "BUILTIN\Administrators":F /C
``` 

4.   (Optional) Validate that the KeyStore was created correctly using the JRE bundled with the Proxy Agent:

    *   **Linux**:

```
$HVR_HOME/jre/bin/keytool -list -keystore keystore.p12 -storetype PKCS12 -storepass <your_secure_password>
``` 
    *   **Windows**:

```
%HVR_HOME%\jre\bin\keytool -list -keystore keystore.p12 -storetype PKCS12 -storepass <your_secure_password>
``` 
Expected output:

```
Keystore type: PKCS12
Keystore provider: SUN

Your keystore contains 1 entry

orchestrator.fivetran.com, Jan 15, 2025, PrivateKeyEntry,
Certificate fingerprint (SHA-256): AA:BB:CC:...
``` 

5.   Remove the embedded certificate fields from your configuration file. This ensures that the Proxy Agent relies only on the KeyStore for the certificate and private key.

For Windows EXE installations, the installer requires embedded certificates for validation. Do not remove the `client_cert` and `client_private_key` fields before installation. Remove these fields after the installation completes, as described in [Configure KeyStore settings for Windows EXE installation](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#configurekeystoresettingsforwindowsexeinstallation). 
Before (embedded certificates):

```
{
  "agent_id": "your_agent_id",
  "auth_token": "...",
  "orchestrator_host": "orchestrator.fivetran.com",
  "client_cert": "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----\n",
  "client_private_key": "-----BEGIN RSA PRIVATE KEY-----\n...\n-----END RSA PRIVATE KEY-----\n"
}
``` 
After (using KeyStore):

```
{
  "agent_id": "your_agent_id",
  "auth_token": "...",
  "orchestrator_host": "orchestrator.fivetran.com"
}
``` 

### Network configuration and validation[](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#networkconfigurationandvalidation)

Before installing the Proxy Agent, [safelist the hostnames of the Proxy Broker and the appropriate Proxy Server](https://fivetran.com/docs/using-fivetran/ips#fivetranproxyusers) in your firewall so that the Proxy Agent can connect to our server. After configuring your firewall, do the following to verify connectivity to Fivetran's Proxy Server on the machine on which the Proxy Agent will be installed.

Verify Connectivity to the Proxy Broker
*   **Using Telnet**:```
telnet orchestrator.fivetran.com 443
``` 
*   **Using Netcat**:```
nc orchestrator.fivetran.com 443 -v
``` 

Verify Connectivity to the Proxy Server
Replace `<proxy server hostname>` with the hostname [for the appropriate region](https://fivetran.com/docs/using-fivetran/ips#fivetranproxyusers):

*   **Using Telnet**:```
telnet primary.<proxy server hostname> 443
``` 
*   **Using Netcat**:```
nc primary.<proxy server hostname> 443 -v
``` 

### Install Proxy Agent[](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#installproxyagent)

Follow the Proxy Agent installation instructions for your operating system.

Install Proxy Agent on Windows using EXE file (Installer)
When installing the Proxy Agent as a service, the user who installs the Proxy Agent must have permission to manage Windows services. We recommend that you install the Proxy Agent as an Administrator user.

1.   Run the downloaded `.exe` file (for example, `fivetran-6.1.0_23-hub_and_agent-windows-x64-64bit_ga_patch-setup.exe`).

2.   In the installation wizard dialog, click **Next**.![Image 7](https://fivetran.com/static-assets-docs/_next/static/media/Welcome.02de292f.webp)

3.   Read the License Agreement, select **I accept the agreement** and click **Next**.![Image 8](https://fivetran.com/static-assets-docs/_next/static/media/LicenseAgreement.0cd7a459.webp)

4.   Specify the installation directories (for example, `C:\Fivetran\hvr_home`, `C:\Fivetran\hvr_config`, and `C:\Fivetran\hvr_tmp`) and click **Next**.

![Image 9](https://fivetran.com/static-assets-docs/_next/static/media/DestinationDirectories.826f9b92.webp)
5.   Specify the name for the program folder and click **Next**.

![Image 10](https://fivetran.com/static-assets-docs/_next/static/media/ProgramFolder.fa00865e.webp)
6.   Select the role of the installation:

    *   **Proxy Agent** to install only the Proxy Agent or
    *   **High-Volume Agent (HVA) and Proxy Agent** to install both the Proxy Agent and HVA.![Image 11](https://fivetran.com/static-assets-docs/_next/static/media/InstallationRoleProxyAgent.a9376b0c.webp)

7.   If you selected **High-Volume Agent (HVA) and Proxy Agent** in the previous step, enter value for the High-Volume Agent Listener Port and click **Next**.

![Image 12](https://fivetran.com/static-assets-docs/_next/static/media/AgentListenerPort.534be3ff.webp)
8.   Paste the Proxy Agent settings from the configuration file (`config.json`) you've [generated](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#generateproxyagentsettings) and click **Next**.

The configuration file contains the settings and authentication parameters required to establish secure communication between the Proxy Agent and Fivetran. ![Image 13](https://fivetran.com/static-assets-docs/_next/static/media/AgentProxySettings.5619f944.webp)
9.   Select **Local System account** for running the Proxy Agent service and click **Next**.

![Image 14](https://fivetran.com/static-assets-docs/_next/static/media/ServicesUserAccount_Local.d83671e5.webp)
10.   Select **Add HVR_HOME**, **HVR_CONFIG**, and **HVR_TMP** (if required) and click **Next**. _If you are only installing the Proxy Agent, we recommend that you skip this step._

This is to set the environment variables `HVR_HOME`, `HVR_CONFIG`, and `HVR_TMP` in your operating system. These variables point to the corresponding installation directories you've [created](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#installationdirectories) above. ![Image 15](https://fivetran.com/static-assets-docs/_next/static/media/AdditionalConfiguration_Agent.82a674d6.webp)
11.   Click **Next** to initiate the installation.

If you selected **High-Volume Agent (HVA) and Proxy Agent** in step 6, this will install both the Proxy Agent and High-Volume Agent under the same installation directory. ![Image 16](https://fivetran.com/static-assets-docs/_next/static/media/ReadytoInstall.4fc5fa6a.webp)
12.   Click **Finish** to start the Proxy Agent. Once installed, the Proxy Agent service appears running in Windows Services.

If you selected **High-Volume Agent (HVA) and Proxy Agent** in step 6, this will start both the Proxy Agent and High-Volume Agent services. ![Image 17](https://fivetran.com/static-assets-docs/_next/static/media/CompletedAgent.5d45232a.webp)
13.   (Optional) If you are using a KeyStore for [certificate management](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#certificatemanagementoptions), configure the Proxy Agent to load the KeyStore by setting the required JVM system properties.

Expand for instructions

#### Configure KeyStore settings for Windows EXE installation[](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#configurekeystoresettingsforwindowsexeinstallation)

The Windows EXE installer creates the Proxy Agent as a Windows service using `prunsrv.exe`. The installer requires embedded certificates during installation for validation. After installation completes, you must remove the embedded certificates from the Proxy Agent configuration and then configure the service to load credentials from the KeyStore.

    1.   Stop the Proxy Agent service:

```
net stop "Fivetran Proxy Agent"
``` 
    2.   Remove the embedded certificate fields from the Proxy Agent configuration file.

a. Open the `%HVR_CONFIG%\proxy\proxyagent.conf` file.

b. Remove the `client_cert` and `client_private_key` fields.

Before (embedded certificates):

```
{
"agent_id": "your_agent_id",
"auth_token": "...",
"orchestrator_host": "orchestrator.fivetran.com",
"client_cert": "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----\n",
"client_private_key": "-----BEGIN RSA PRIVATE KEY-----\n...\n-----END RSA PRIVATE KEY-----\n"
}
``` 
After (using KeyStore):

```
{
"agent_id": "your_agent_id",
"auth_token": "...",
"orchestrator_host": "orchestrator.fivetran.com"
}
``` 
c. Save the file after removing the fields.

    3.   Identify the actual service name created by the installer:

```
sc query | findstr /i "FivetranProxy"
``` 
Note the service name in the output. It has the format `FivetranProxyPrunsrv_<HASH>` (for example, `FivetranProxyPrunsrv_ABCD1234`).

    4.   Update the service to include the KeyStore JVM system properties:

```
"%HVR_HOME%\proxy\prunsrv.exe" //US//FivetranProxyPrunsrv_<HASH> ++JvmOptions "-Djavax.net.ssl.keyStore=<path_to_keystore>" ++JvmOptions "-Djavax.net.ssl.keyStorePassword=<your_secure_password>"
``` 
Replace:

        *   `FivetranProxyPrunsrv_<HASH>` with the service name you identified
        *   `<path_to_keystore>` with the full path to your KeyStore file
        *   `<your_secure_password>` with the KeyStore password

Using ++JvmOptions appends options without removing existing JVM configuration required by the Proxy Agent.

    5.   Start the Proxy Agent service:

```
net start "Fivetran Proxy Agent"
``` 
    6.   Check the Proxy Agent logs to confirm that the KeyStore was loaded successfully. By default, the log file is located at `%HVR_CONFIG%\proxy\log\agent-out.log`. Look for entries similar to:

```
INFO: Certificates not found in config, attempting to load from KeyStore
INFO: Using KeyStore from javax.net.ssl.keyStore: <path_to_keystore>
INFO: Successfully loaded certificates from KeyStore for alias: orchestrator.fivetran.com
``` 

Install Proxy Agent on Windows using ZIP file
Perform the following steps as an Administrator user.

1.   Configure the environment variables `HVR_HOME`, `HVR_CONFIG`, and `HVR_TMP` for your operating system using command `setx` or `set`. Each of these environment variables should be pointed to the installation directories - `hvr_home`, `hvr_config`, and `hvr_tmp`:

Environment variables set using `setx` command are available in the future command windows only and the environment variables set using `set` command are available in the current command window only. ```
setx HVR_HOME C:\fivetran\hvr_home
setx HVR_CONFIG C:\fivetran\hvr_config
setx HVR_TMP C:\fivetran\hvr_tmp
``` ```
set HVR_HOME=C:\fivetran\hvr_home
set HVR_CONFIG=C:\fivetran\hvr_config
set HVR_TMP=C:\fivetran\hvr_tmp
``` 
Also, add the executable directory path (for example, `C:\fivetran\hvr_home\bin`) to the environment variable `PATH`.

```
setx PATH "%PATH%;C:\fivetran\hvr_home\bin"
``` ```
set PATH=%PATH%;C:\fivetran\hvr_home\bin
``` 

Alternatively, environment variables can be configured using Windows GUI.
    1.   Navigate to **Control Panel ▶ System and Security ▶ System ▶ Advanced system settings**

Alternatively, use the command `sysdm.cpl` to open **System Properties**. 
    2.   In the **Advanced** tab, click **Environment Variables...**![Image 18](https://fivetran.com/static-assets-docs/_next/static/media/SystemProperties.eb6aa61e.webp)

    3.   In section **System variables**, click **New**.

        1.   Enter **Variable name** (for example, `HVR_HOME`) and **Variable value** (for example, `C:\fivetran\hvr_home`).

![Image 19](https://fivetran.com/static-assets-docs/_next/static/media/NewUserVariable.0bf260a8.webp)
        2.   Click **OK**.
        3.   Repeat the above steps for each environment variable.

    4.   Add the executable directory path to the environment variable `Path`.

        1.   In section **System variables** or **User Variables for**_user\_name_, from the list of variables, select **Path** and click **Edit...**.
        2.   Click **New** and enter the path for the Proxy Agent executable.

![Image 20](https://fivetran.com/static-assets-docs/_next/static/media/EditEnvVariable.c674d4e5.webp)
        3.   Click **OK**.

2.   Create the installation directory - `hvr_home` (for example, `C:\fivetran\hvr_home`):

```
md %HVR_HOME%
``` 

    *   Other directories (`hvr_config` and `hvr_tmp`) will be created automatically as needed.
    *   `hvr_home` is regarded a read-only directory.

3.   Extract the installation file (for example, **fivetran-6.1.0_23-hub_and_agent-windows-x64-64bit_ga_patch.zip**) into the `hvr_home` directory:

```
cd %HVR_HOME%
C:\fivetran\hvr_home>tar -xf C:\Users\Admin\Downloads\fivetran-6.1.0_23-hub_and_agent-windows-x64-64bit_ga_patch.zip
``` Alternatively, files can be extracted using the 'Extract All' option in Windows GUI.![Image 21](https://fivetran.com/static-assets-docs/_next/static/media/ExtractAll.303c70aa.webp) 
4.   Paste the Proxy Agent settings from the configuration file (`config.json`) you've [generated](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#generateproxyagentsettings) to the `proxyagent.conf` file located in the `HVR_CONFIG/proxy` directory.

The configuration file contains the settings and authentication parameters required to establish secure communication between the Proxy Agent and Fivetran. If the `proxyagent.conf` file is missing, create the file manually. 
5.   Run the following command to validate the Proxy Agent settings:

```
%HVR_HOME%/jre/bin/java -jar %HVR_HOME%/proxy/proxyagent.jar -v %HVR_CONFIG%/proxy/proxyagent.conf
``` 
6.   Create a `.bat` file (for example, `install_and_run_proxy_service.bat`) with the following contents.

```
FOR /F "delims=" %%i IN ('CALL "%HVR_HOME%/bin/hvr" hvrhubserversvc -s') DO SET HvrHubServerSvcOutput=%%i
 REM We use a normalized HVR_CONFIG path hash to guarantee a unique service name
 SET HubConfigHash=%HvrHubServerSvcOutput:~13,8%

 REM In the CLI below use "DomainName\UserName" for --ServiceUser and specify --ServicePassword parameter if needed
 REM Adjust the other parameters as necessary
 REM Ensure to have unique service name (in //IS//<ServiceName>) and display name 
 %HVR_HOME%/proxy/prunsrv.exe //IS//FivetranProxy_%HubConfigHash% ^
    --StartParams "%HVR_CONFIG%/proxy/proxyagent.conf" ^
    --ServiceUser "LocalSystem" ^
    --DisplayName "Fivetran Proxy Agent [%HubConfigHash%]" ^
    --Description "Fivetran Proxy Agent installed into %HVR_HOME%\proxy" ^
    --Jvm "%HVR_HOME%/jre/bin/server/jvm.dll" ^
    --JavaHome "%HVR_HOME%/jre" ^
    --Classpath "%HVR_HOME%/proxy/proxyagent.jar" ^
    --StartPath "%HVR_HOME%/proxy/" ^
    --Startup=auto ^
    --StartMode=jvm ^
    --StartClass=com.fivetran.proxy.agent.ProxyAgent ^
    --StartMethod=main ^
    --StopMode=jvm ^
    --StopClass=com.fivetran.proxy.agent.ProxyAgent ^
    --StopMethod=stop ^
    --JvmOptions "-XX:+HeapDumpOnOutOfMemoryError" ^
    --StdOutput "%HVR_CONFIG%/proxy/logs/agent-out.log" ^
    ++Environment "HVR_CONFIG=%HVR_CONFIG%" ^
    ++Environment "HVR_HOME=%HVR_HOME%" ^
    ++Environment "HVR_TMP=%HVR_TMP%"

  %HVR_HOME%/proxy/prunsrv.exe //ES//FivetranProxy_%HubConfigHash%
``` 
7.   Run the `.bat` file to configure and start the Proxy Agent:

```
install_and_run_proxy_service.bat
``` 
8.   (Optional) If you are using a KeyStore for [certificate management](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#certificatemanagementoptions), configure the Proxy Agent to load the KeyStore by setting the required JVM system properties.

Expand for instructions

#### Configure KeyStore settings for Windows ZIP installation[](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#configurekeystoresettingsforwindowszipinstallation)

    1.   Stop the Proxy Agent service:

```
%HVR_HOME%\bin\hvrproxy.bat stop
``` 
    2.   Update the Proxy Agent service definition to include the required JVM system properties for loading the KeyStore. Open the `install_and_run_proxy_service.bat` file you created earlier and modify the `--JvmOptions` line:

```
--JvmOptions "-XX:+HeapDumpOnOutOfMemoryError; -Djavax.net.ssl.keyStore=<path_to_keystore>; -Djavax.net.ssl.keyStorePassword=<your_secure_password>"
``` 
    3.   Rerun the updated install script to update the service definition:

```
install_and_run_proxy_service.bat
``` 
    4.   Start the Proxy Agent service:

```
%HVR_HOME%\bin\hvrproxy.bat start
``` 
    5.   Check the Proxy Agent logs to confirm that the KeyStore was loaded successfully. By default, the log file is located at `%HVR_CONFIG%\proxy\logs\agent-out.log`.

If you configured a custom log directory using the `log_folder_path` setting in `proxyagent.conf` (located in `%HVR_CONFIG%\proxy`), the logs are written to that directory instead, for example, `<log_folder_path>/agent-out.log`. 
Look for entries similar to:

```
INFO: Certificates not found in config, attempting to load from KeyStore
INFO: Using KeyStore from javax.net.ssl.keyStore: <path_to_keystore>
INFO: Successfully loaded certificates from KeyStore for alias: orchestrator.fivetran.com
``` 

Install Proxy Agent on Linux
Perform the installation steps as a regular user (for example, `fivetran`). Use `sudo` only for steps that create system users, modify files under `/etc`, or manage the `systemd` service.

The Proxy Agent service runs as `root`. The examples below use the `fivetran` home directory for installation paths. Ensure that the installation directories and files are readable by `root` so the service can access the binaries and configuration.

The commands to set the environment variables depend on the shell you use to interface with the operating system. This procedure lists examples that can be used in Bourne Shell (sh) and KornShell (ksh).

1.   Create a regular user account to set up the install directories and environment variables (for example, `fivetran`):

```
sudo useradd -m fivetran
``` 
2.   Switch to the `fivetran` user:

```
sudo su - fivetran
``` 
3.   Configure the environment variables `HVR_HOME`, `HVR_CONFIG`, and `HVR_TMP` for your operating system. Each of these environment variables should be pointed to the installation directories - `hvr_home`, `hvr_config`, and `hvr_tmp`.

```
export HVR_HOME=/home/fivetran/hvr_home 
export HVR_CONFIG=/home/fivetran/hvr_config
export HVR_TMP=/home/fivetran/hvr_tmp
``` 
Also, add the executable directory path to the environment variable `PATH`.

```
PATH=$PATH:$HVR_HOME/bin
``` 
4.   Add the environment and the executable directory path into the startup file (for example, `.profile`).

```
export HVR_HOME=/home/fivetran/hvr_home
export HVR_CONFIG=/home/fivetran/hvr_config
export HVR_TMP=/home/fivetran/hvr_tmp
export PATH=$PATH:$HVR_HOME/bin
``` 
5.   Create the installation directory - `hvr_home` using the following commands:

```
umask 022
``` ```
mkdir $HVR_HOME
``` `umask 022` is used so that the files and directories created in the following commands are readable by everyone (other Linux users and groups), but only writable by the owner. Other directories (`HVR_CONFIG` and `HVR_TMP`) will be created automatically as needed. The `HVR_HOME` directory is regarded as read-only. 
6.   Download the High-Volume Agent installation file from the **[Downloads](https://fivetran.com/dashboard/account/downloads)** page in your Fivetran dashboard. One way to do this is to copy the download URL and run the following `wget` command:

```
cd /tmp
wget "<download_url_from_fivetran>"
``` 
7.   Extract the installation file (for example, `fivetran-6.1.0_23-hub_and_agent-linux_glibc2.17-x64-64bit_ga.tar.gz`) into the `HVR_HOME` directory:

```
cd $HVR_HOME
``` ```
tar xzf /tmp/hvr-6.1.0_23-hub_and_agent-linux_glibc2.17-x64-64bit_ga.tar.gz
``` 
Once installed, the `jre` and `proxy` folders are created in your `HVR_HOME` directory.

8.   Create a new directory for the `proxyagent.conf` file in `hvr_config` (`/home/fivetran/hvr_config/proxy`). Paste the Proxy Agent settings from the configuration file (`config.json`) you've [generated](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#generateproxyagentsettings) to the `proxyagent.conf` file located in the newly created directory.

The configuration file contains the settings and authentication parameters required to establish secure communication between the Proxy Agent and Fivetran. 
9.   Run the following command to verify if the Linux machine is ready for the setup. The output of the command should be `systemd`.

```
ps -p 1 -o comm=
``` 
10.   Using `sudo`, update the `fivetran_proxy.service` file in the `/etc/systemd/system` directory with the correct path to the Java executable, `proxyagent.jar`, and `proxyagent.conf` files.

If missing, create the `fivetran_proxy.service` file manually. The contents of the file should be as follows:

```
[Unit]
Description=Fivetran Proxy Agent #<agent_id>

[Service]

Type=simple
Environment="HVR_HOME=/home/fivetran/hvr_home"
Environment="HVR_CONFIG=/home/fivetran/hvr_config"
Environment="HVR_TMP=/home/fivetran/hvr_tmp"

ExecStart=/home/fivetran/hvr_home/jre/bin/java \
  -XX:+HeapDumpOnOutOfMemoryError \
  -XX:HeapDumpPath=${HVR_CONFIG}/proxy/ \
  -jar ${HVR_HOME}/proxy/proxyagent.jar \
  /home/fivetran/hvr_config/proxy/proxyagent.conf

# Restart this service after a crash
Restart=always

# The number of seconds to wait before attempting a restart
RestartSec=5s

[Install]
WantedBy=multi-user.target
``` 
11.   Using `sudo`, execute the following commands to start the Proxy Agent service.

a. Enable the service:

```
sudo systemctl enable fivetran_proxy.service
``` 
b. Start the service:

```
sudo systemctl start fivetran_proxy.service
``` 
c. Verify the status of the service:

```
sudo systemctl status fivetran_proxy.service
``` 
12.   (Optional) If you are using a KeyStore for [certificate management](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#certificatemanagementoptions), configure the Proxy Agent to load the KeyStore by setting the required JVM system properties.

Expand for instructions

#### Configure KeyStore settings for Linux installation[](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#configurekeystoresettingsforlinuxinstallation)

    1.   Update the `systemd` service definition to include the required JVM system properties for loading the KeyStore. Edit the `/etc/systemd/system/fivetran_proxy.service` file and add the following line under the `[Service]` section:

```
Environment="JAVA_OPTS=-Djavax.net.ssl.keyStore=/path/to/keystore.p12 -Djavax.net.ssl.keyStorePassword=<your_secure_password>"
``` 
    2.   Reload the `systemd` daemon and restart the Proxy Agent service:

```
sudo systemctl daemon-reload
sudo systemctl restart fivetran_proxy.service
``` 
    3.   Check the Proxy Agent logs to confirm that the KeyStore was loaded successfully. By default, the log file is located at `$HVR_CONFIG/proxy/log/agent-out.log`.

If you configured a custom log directory using the `log_folder_path` setting in `proxyagent.conf` (located in `$HVR_CONFIG/proxy`), the logs are written to that directory instead (for example, `<log_folder_path>/agent-out.log`). 
Look for entries similar to:

```
INFO: Certificates not found in config, attempting to load from KeyStore
INFO: Using KeyStore from javax.net.ssl.keyStore: <path_to_keystore>
INFO: Successfully loaded certificates from KeyStore for alias: orchestrator.fivetran.com
``` 

#### Proxy Agent directory structure[](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#proxyagentdirectorystructure)

The following directories are created during the installation of the Proxy Agent. Each directory may contain files and subdirectories:

*   `hvr_home`: Contains executables and files essential for running the Proxy Agent.

Expand to see the directories and files in `hvr_home````
📁 hvr_home
│
├─ 📁 api        --  REST API documentation
│
├─ 📁 bin        --  Executable files and shared libraries (dynamic-link 
│                    libraries on Windows) for running the Proxy Agent
│
├─ 📁 dbms       --  Database-specific SQL files and templates
│
├─ 📁 etc        --  Configuration files and other miscellaneous files
│  │
│  ├─ 📁 cert    --  Bundled certificates, such as root CAs
│  │
│  ├─ 📁 snmp    --  SNMP MIB file
│  │
│  ├─ 📁 xml     --  DTD of XML-serialized data streams
│  │
│  ├─ 📄 constsqlexpr.pat            --  SQL expressions treated as constants to
│  │                                     optimize replication performance
│  │
│  ├─ 📄 hvrosaccess_example.conf    --  Sample configuration for allowing HVR to
│  │                                     run plugins from non-standard directories
│  │
│  └─ 📄 purge.manifest              --  Manifest file (see hvrstrip -m)
│
├─ 📁 examples       --  Sample channel definitions
│
├─ 📁 lib            --  Shared libraries and database drivers
│
├─ 📁 plugin         --  Plugins shipped (installed) with the Proxy Agent
│  │
│  ├─ 📁 agent
│  │
│  └─ 📁 transform
│
├─ 📁 plugin_examples    --  Sample plugins. To use a sample plugin, save
│  │                         it in the 'hvr_config/plugin' directory
│  ├─ 📁 agent
│  │
│  ├─ 📁 authentication
│  │
│  ├─ 📁 rewrite
│  │
│  └─ 📁 transform
│
├─ 📁 sbin           --  Manually created trusted executables
│
├─ 📁 script         --  Internal Proxy Agent script files
│
├─ 📁 www            --  HVR UI-related files
│
├─ 📄 hvr.3rdparty   --  License agreements, copyrights, versions, and notices
│                        for third-party software used by the Proxy Agent
│
├─ 📄 hvr.rel        --  Proxy Agent Release Notes
│
└─ 📄 hvr.ver        --  Proxy Agent version number
```  
*   `hvr_config`: Contains directories and files associated with the Proxy Agent configuration.

Expand to see the directories and files in `hvr_config````
📁 hvr_config    --  Directories and files for the Proxy Agent configuration
│
├─ 📁 etc        --  Configuration files for the Proxy Agent
│
├─ 📁 intermediate    --  Temporary files for Compare/Refresh jobs
│
├─ 📁 logs            --  Proxy Agent-level log files
│
├─ 📁 plugin          --  User-installed plugins (see 'hvr_home/plugin_examples/')
│  │
│  ├─ 📁 agent
│  │
│  └─ 📁 transform
│
├─ 📁 public    --  Log file retention information
│
├─ 📁 run       --  Runtime state, such as `.pid` files
│
└─ 📁 tmp       --  Temporary files (default, if HVR_TMP is not defined)
```  
*   `hvr_tmp` (optional): Contains temporary files associated with the Proxy Agent.

Making any changes to the `hvr_home` directory or its subdirectories is strictly prohibited. This directory must remain unchanged to ensure security and integrity during updates or upgrades. User-specific configurations and runtime data is stored in the `hvr_config` directory.

### Configure Proxy Agent recovery (recommended for Windows) [](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#configureproxyagentrecoveryrecommendedforwindows)

Expand for instructions
If your Proxy Agent is installed on a Windows system, you can set up a recovery configuration for the agent by performing the following steps:

This process is not required on Linux systems.

1.   Go to **Control Panel > Administrative Tools > Computer Management > Services and Applications > Services** or use the `services.msc` command to open the Services console.

2.   In the Services console, locate the Fivetran Proxy Agent service. Ensure the service description matches the installation directory.

3.   Right-click the service and select **Properties**.

4.   Go to the **Recovery** tab.

5.   Set your preferred recovery options for the failure scenario.

![Image 22](https://fivetran.com/static-assets-docs/_next/static/media/windows-service-recovery.f6b9846a.webp)

The [SC failure](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc742019(v=ws.11)) command-line utility is also available for more advanced configurations. This tool allows you to automate recovery actions directly through the command line.

* * *

Upgrade Proxy Agent[](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#upgradeproxyagent)
----------------------------------------------------------------------------------------------------------------------

Steps for upgrading the Proxy Agent depend on how it was installed.

Before upgrading the Proxy Agent, we _recommend_ making a copy of the Proxy Agent configuration file (`hvr_config/proxy/proxyagent.conf`) located on the Proxy Agent machine. Backing it up preserves the existing Proxy Agent configuration, including the certificates used to establish secure communication with Fivetran. This lets you quickly restore the configuration if you need to revert to an earlier Proxy Agent version after an upgrade or reinstall, without having to generate a new Proxy Agent configuration file.

Proxy Agent Installed on Windows using EXE file (Installer)
The Installer will automatically detect the existing Proxy Agent installation and upgrade it. Perform the following steps:

1.   Download the latest High-Volume Agent Installer from [the downloads page](https://fivetran.com/dashboard/account/downloads).

2.   Run the Installer.

Proxy Agent Installed on Windows using a ZIP file or on Linux (Installer)
The Proxy Agent installed using a ZIP file or on Linux requires manual upgrade steps. Perform the following steps:

1.   Download the latest High-Volume Agent for the desired operating system from [the downloads page](https://fivetran.com/dashboard/account/downloads).

2.   Uninstall the existing proxy agent using the [Uninstall Proxy Agent](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#uninstallproxyagent) instructions.

3.   Follow the instructions for installing the Proxy Agent using the appropriate section of [the installation instructions](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#installproxyagent).

* * *

Uninstall Proxy Agent[](https://fivetran.com/docs/connectors/databases/connection-options/proxy-agent#uninstallproxyagent)
--------------------------------------------------------------------------------------------------------------------------

Follow the instructions below to uninstall the Proxy Agent.

If you are uninstalling the Proxy Agent to perform an upgrade, we _recommend_ making a copy of the Proxy Agent configuration file (`hvr_config/proxy/proxyagent.conf`) located on the Proxy Agent machine. Backing it up preserves the existing Proxy Agent configuration, including the certificates used to establish secure communication with Fivetran. This lets you quickly restore the configuration if you need to revert to an earlier Proxy Agent version after an upgrade or reinstall, without having to generate a new Proxy Agent configuration file.

Uninstall Proxy Agent from Windows
The steps to uninstall the Proxy Agent depend on whether you used an EXE file (Installer) or a ZIP file to install it.

Ensure that no Windows Services management console applications (opened via `services.msc`) are running.

**Uninstall Proxy Agent that was installed using an EXE file**

1.   Navigate to the `uninstall` folder in the Proxy Agent installation directory `%HVR_HOME%` (for example, `C:\fivetran\hvr_home\uninstall`).

2.   Double-click the `uninstall.exe` file to initiate the uninstallation process.

**Uninstall Proxy Agent that was installed using a ZIP file**

1.   Create a `.bat` file (for example, `delete_proxy_agent_service.bat`) with the following contents:

```
FOR /F "delims=" %%i IN ('CALL "%HVR_HOME%/bin/hvr" hvrhubserversvc -s') DO SET HvrHubServerSvcOutput=%%i
   REM We use a normalized HVR_CONFIG path hash to guarantee a unique service name
   SET HubConfigHash=%HvrHubServerSvcOutput:~13,8%

   %HVR_HOME%/proxy/prunsrv.exe //DS//FivetranProxy_%HubConfigHash%
``` 
2.   Run the `.bat` file as an Administrator to remove all Proxy Agent service entries.

Uninstall Proxy Agent from Linux
1.   Stop the Proxy Agent service:

```
sudo systemctl stop fivetran_proxy.service
``` 
2.   Disable the service from auto-starting at boot:

```
sudo systemctl disable fivetran_proxy.service
``` 
3.   Remove the service configuration file:

```
sudo rm /etc/systemd/system/fivetran_proxy.service
``` 
4.   Reload the systemd manager configuration:

```
sudo systemctl daemon-reload
``` 
5.   Clear the systemd state for any failed services:

```
sudo systemctl reset-failed
``` 

Thanks for your feedback!

Was this page helpful?
