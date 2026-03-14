# Source: https://plivo.com/docs/sip-trunking/interconnection-guides/freeswitch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

#  Freeswitch

> Configure FreeSwitch with Zentrunk — regular and secure SIP trunking

<Tabs>
  <Tab title="Regular Trunking">
    # Zentrunk & Freeswitch - Regular Trunking

    ## Overview

    This documentation provides a basic configuration to get FreeSwitch up and running with Plivo as the external SIP gateway. This documentation was written using a Debian Jessie GNU/Linux System running FreeSwitch 1.6.6.

    To get started with Zentrunk using FreeSwitch you would need to do the following:

    1. [Install FreeSwitch on your environment](/sip-trunking/interconnection-guides/freeswitch/#installation-of-freeswitch).
    2. [Create a Trunk on Zentrunk using Plivo Console](/sip-trunking/#create-an-outbound-trunk).
    3. [Configure an Outbound Trunk](/sip-trunking/interconnection-guides/freeswitch/#configuring-an-outbound-trunk).
    4. [Configure the Inbound Trunk](/sip-trunking/interconnection-guides/freeswitch/#configuring-an-inbound-trunk).

    ## Installation of Freeswitch

    On your Debian system, execute the following commands in the terminal:

    1. Update the Package Manager.

    ```sh  theme={null}
    apt-get update && apt-get install -y curl
    ```

    2. Add the Public Key of FreeSwitch package to local Package Manager.

    ```sh  theme={null}
    curl https://files.freeswitch.org/repo/deb/debian/freeswitch_archive_g0.pub | apt-key add -
    ```

    3. Add the FreeSwitch repository URL to the source list of local Package Manager.

    ```sh  theme={null}
    echo "deb http://files.freeswitch.org/repo/deb/freeswitch-1.6/ jessie main" > /etc/apt/sources.list.d/freeswitch.list
    ```

    4. Install the FreeSwitch package.

    ```sh  theme={null}
    apt-get update && apt-get install -y freeswitch-all freeswitch-all-dbg gdb
    ```

    To install Freeswitch on CentOS, follow the instructions given [here](https://freeswitch.org/confluence/display/FREESWITCH/Installation)

    To install Freeswitch on Windows, follow the instructions given [here](https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/Installation/Windows-Install_1966780/)

    ## Configuring an Outbound Trunk

    To configure Freeswitch to connect to your Plivo Zentrunk, locate the root configuration of FreeSwitch on your machine. These locations vary from platform to platform.

    * For Debian Jessie GNU/Linux System, the root configuration is present at **/etc/freeswitch/**.
    * For Windows, the root configuration is located at **C:\Program Files\FreeSWITCH\conf**.

    For Linux systems, it could be either of the following depending on your installation:

    * **/usr/local/freeswitch/conf**
    * **/opt/freeswitch/conf**

    With the root configuration directory located, you must complete the following configurations:

    1. Create a new SIP Profile.
    2. Create a Dial Plan.

    ### Step 1: Sip Profile

    1. Create a new file named "zentrunk.xml" at **/etc/freeswitch/sip\_profiles/external/**.
    2. In zentrunk.xml, create a new gateway with your Plivo Zentrunk details (refer the below given images to get your Plivo Trunk details).

    ```xml  theme={null}
    <include>
      <gateway name="Plivo-outbound">
        <param name="username" value="Username for TestAuthGroup"/>
        <param name="password" value="Password for TestAuthGroup" />
        <param name="proxy" value="Termination SIP Domain of your Plivo Trunk"/>
        <param name="register" value="false"/>
      </gateway>
    </include>
    ```

    #### Termination SIP Domain of your Plivo Trunk:

    <Frame>
            <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/Trunk4.png?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=b86ea3cad3d63f6417e549c7c8bd59ee" alt="" width="1440" height="703" data-path="images/Trunk4.png" />
    </Frame>

    #### TestAuthGroup Credentials:

    <Frame>
            <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/AuthGroup3.png?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=c57d88c2a1837699b3f43b5f6a4b25ed" alt="" width="1440" height="568" data-path="images/AuthGroup3.png" />
    </Frame>

    ### Step 2: Dialplan

    Next, you should setup a Dial Plan to use the Plivo SIP Profile created in Step 1.

    * Create a new file named "02\_zentrunk.xml" at **/etc/freeswitch/dialplan/default/**. If you already have a dialplan prefixed by 02, you can choose the another number.

    ```xml  theme={null}
    <extension name="plivo">
      <condition field="destination_number" expression="^(\d{11})$">
    	<action application="set" data="effective_caller_id_number=${outbound_caller_id_number}"/>
    	<action application="bridge" data="sofia/gateway/Plivo-outbound/$1"/>
      </condition>
    </extension>
    ```

    The above dial plan has defined an extension for 11 digit US numbers like +1-(222)-(222)-2222. The **outbound\_caller\_id\_number** field is inherited from **vars.xml** which would be set as the caller ID while making outbound calls. This extension is set to bridge to your SIP Profile "Plivo-outbound".

    ### Step 3: Reload Configurations

    1. Load the fs\_cli utility. Execute **fs\_cli** in your terminal.
    2. Reload the dialplan. Execute **reloadxml**.
    3. Add the new SIP Profile, Execute **sofia profile external rescan**

    ## Test your setup

    FreeSwitch instances have default users and SIP passwords preconfigured. To prevent being hacked, we recommend you change the default password.

    Open **vars.xml** located at **/etc/freeswitch/** and edit the following line:

    ```xml  theme={null}
    <X-PRE-PROCESS cmd="set" data="default_password=set your password here"/>
    ```

    This change is applicable to all users under **/etc/freeswitch/directory/default/**. If you want to change the password per user, then navigate to **/etc/freeswitch/directory/default/** and edit 1000.xml (or any user of your choice).

    ```xml  theme={null}
    <param name="password" value="set your password here"/>
    ```

    Execute **reloadxml** in fs\_cli utility after making changes to users xml.

    **Note:** Freeswitch has to be restarted if any changes were made to **vars.xml**.

    ### Make an outbound call

    When the account is successfully enabled on X-Lite, it is ready to make calls. Enter any valid 11 digit US number in your X-Lite and hit on the call button. This call would hit your freeswitch server first, then go through Plivo Zentrunk and finally reach the destination number.

    To know more about configuring X-lite for outbound calls, check the [X-lite configuration guide](/sip-trunking/interconnection-guides/configuring-x-lite/)

    ## Configuring an Inbound Trunk

    To configure the Freeswitch to connect to your Plivo inbound Zentrunk, first locate the root configuration of FreeSwitch on your machine. These locations vary from platform to platform.

    * For Debian Jessie GNU/Linux System, the root configuration is present at **/etc/freeswitch/**.
    * For Windows, the root configuration is located at **C:\Program Files\FreeSWITCH\conf**.

    For Linux systems, it could be either of the following depending on your installation -

    * **/usr/local/freeswitch/conf**
    * **/opt/freeswitch/conf**

    With the root configuration directory located, there are three major configurations that needs to done:

    1. Create a Dial Plan.
    2. Create a User
    3. Change access control list

    ### Step 1: Dialplan

    Create a new file named "03\_zentrunk.xml" at **/etc/freeswitch/dialplan/default/**. If you already have a dialplan prefixed by 03, you can choose the another number. Use the XML Under the context =public

    ```xml  theme={null}
    <extension name="inboundbridge" continue="true">
     		<condition field="destination_number" expression="^(\+)?your_destination_number$">
            <action application="log" data=" Pleasewait we are connecting to plivo inbound NMS"/>
    	    <action application="set" data="bypass_media=true"/>
        	<action application="export" data="sip_from_uri=${sip_from_uri}"/>
            <action application="bridge" data="user/1000"/>
      	</condition>
    </extension>
    ```

    Values to be replaced:

    ```xml  theme={null}
    ^your_destination_number$= The destination number on which you want to receive the incoming call
    ```

    ### Step 2: Access control list

    Open the file  acl.conf.xml  at autoload\_configs/acl.conf.xml. We will have to Whitelist Plivo outbound SIP IP found in [zentrunk](/sip-trunking/) page.

    ### Step 3: Create a User

    Open the file found at freeswitch/directory/default/1000.xml Use the below XML as a reference to edit the user 1000.

    ```xml  theme={null}
    <include>
      <user id="1000">
        <params>
          <param name="password" value="${default_password}"/>
          <param name="vm-password" value="1000"/>
        </params>
        <variables>
            <variable name="to_allow" value="domestic,international,local"/>
            <variable name="accountcode" value="1000"/>
            <variable name="user_context" value="default"/>
            <variable name="effective_caller_id_name" value="Extension 1000"/>
            <variable name="effective_caller_id_number" value="1000"/>
            <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
            <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
            <variable name="callergroup" value="techsupport"/>
         </variables>
          </user>
    </include>
    ```

    <Note>
      **Note:** User ID & Authorization name will be \`1000\` and Value of Default password will be \`1234\`.
    </Note>

    FreeSwitch instances have default users and SIP passwords preconfigured. To prevent being hacked, we recommend you change the default password.\
    Open **vars.xml** located at **/etc/freeswitch/** and edit the following line:

    ```xml  theme={null}
    <X-PRE-PROCESS cmd="set" data="default_password=set your password here"/>
    ```

    This change is applicable to all users under **/etc/freeswitch/directory/default/**. If you want to change the password per user, navigate to **/etc/freeswitch/directory/default/** and edit 1000.xml (or any user of your choice).

    ```xml  theme={null}
    <param name="password" value="set your password here"/>
    ```

    Execute **reloadxml** in fs\_cli utility after making changes to users xml.

    <Note>
      **Note:** Freeswitch has to be restarted if any changes were made to \`vars.xml\`.
    </Note>

    ### Step4: Reload Configurations

    1. Load the fs\_cli utility. Execute **fs\_cli** in your terminal.
    2. Reload the the changes made to the XML's. Execute **reloadxml**.
    3. Reload the ACL file. Execute **reloadacl**.
    4. Reload the dialplan Execute **Reload mod\_dialplan\_xml**.
    5. Restart the service . Execute **Service freeswitch restart**.

    ### Receive an inbound call

    When the account is successfully enabled on X-Lite, it is ready to receive calls. Dial the number provided in the "your\_destination\_number\$" field and the calls will first hit the Plivo inbound zentrunk and then go through your FreeSWITCH to reach your endpoint.

    To know more about configuring X-lite for Inbound calls, check the [X-lite configuration guide](/sip-trunking/interconnection-guides/configuring-x-lite/)
  </Tab>

  <Tab title="Secure Trunking">
    # FreeSwitch using Secure Trunking for Outbound calling

    ## Overview

    This documentation provides configuration for secure and reliable data transfer between your SIP device and Zentrunk infrastructure. This documentation was written using a Debian 9 Stretch GNU/Linux system running FreeSwitch latest release version.

    To get started with Zentrunk Secure Trunking using FreeSwitch you would need to do the following:

    ## Installation of FreeSwitch

    On your Debian 9 Stretch system, execute the following commands in the terminal:

    1. Update the Package Manager.

    ```
    apt-get update && apt-get install -y gnupg2 wget
    ```

    2. Add the Public Key of FreeSwitch package to local Package Manager.

    ```
    wget -O - https://files.freeswitch.org/repo/deb/debian-release/fsstretch-archive-keyring.asc | apt-key add -
    ```

    3. Add the FreeSwitch repository URL to the source list of local Package Manager.

    ```
    echo "deb http://files.freeswitch.org/repo/deb/debian-release/ stretch main" > /etc/apt/sources.list.d/freeswitch.list
    ```

    ```
    echo "deb-src http://files.freeswitch.org/repo/deb/debian-release/ stretch main" >> /etc/apt/sources.list.d/freeswitch.list
    ```

    4. Install the FreeSwitch package.

    ```
    apt-get update && apt-get install -y freeswitch-meta-all
    ```

    ## Configuring a Secure Outbound Trunk (TLS and SRTP)

    To configure FreeSwitch to connect to your Plivo Secure Zentrunk, locate the root configuration of FreeSwitch on your machine. For Debian 9 Stretch GNU/Linux System, the root configuration is present at **/etc/freeswitch/**.

    With the root configuration directory located at **/etc/freeswitch/**, you must complete the following configurations:

    1. Create a new SIP Profile.
    2. Create a Dial Plan.

    ### Step 1: Creating a SIP Profile Gateway

    1. Create a new file named “zentrunk.xml” at /etc/freeswitch/sip\_profiles/external/.

    ```
    touch /etc/freeswitch/sip_profiles/external/zentrunk.xml
    ```

    2. In zentrunk.xml, create a new gateway with your Plivo Secure Zentrunk details (refer the below given images to get your Plivo Trunk details).

    ```
    vim /etc/freeswitch/sip_profiles/external/zentrunk.xml
    ```

    ```xml  theme={null}
    <include>
      <gateway name="Plivo">
        <param name="tls-version" value="tlsv1"/>
        <param name="register-transport" value="tls"/>
        <param name="username" value="Username for TestAuthGroup" />
        <param name="password" value="Password for TestAuthGroup" />
        <param name="caller-id-in-from" value="true"/>
        <param name="proxy" value="Termination SIP Domain of your Plivo Trunk"/>
        <param name="register" value="false"/>
      </gateway>
    </include>
    ```

    **Termination SIP domain of your Plivo Outbound Trunk:**

    <Frame>
            <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/Trunk4.png?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=b86ea3cad3d63f6417e549c7c8bd59ee" alt="" width="1440" height="703" data-path="images/Trunk4.png" />
    </Frame>

    **Create the AUTH GROUP Credentials:**

    <Frame>
            <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/AuthGroup3.png?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=c57d88c2a1837699b3f43b5f6a4b25ed" alt="" width="1440" height="568" data-path="images/AuthGroup3.png" />
    </Frame>

    ### Step 2: Dialplan

    FreeSwitch creates a certain set of default dialplan xml files post installation which are not relevant for setup. Please ensure a SIP profile has been created before proceeding to create a dial plan.

    1. FreeSwitch creates a set of default xml configuration files during installation that we won’t need. We are removing them with the following commands:

    ```
    rm -rf  /etc/freeswitch/dialplan/default/
    ```

    ```
    rm -rf /etc/freeswitch/dialplan/skinny-patterns*
    ```

    ```
    rm /etc/freeswitch/dialplan/features.xml
    ```

    2. Replace the public dialplan /etc/freeswitch/dialplan/public.xml with the following xml:

    ```
    vim /etc/freeswitch/dialplan/public.xml
    ```

    ```xml  theme={null}
    <?xml version="1.0" encoding="utf-8"?>
    <include>
        <context name="public">
            <extension name="Plivo-Secure">
                <condition field="destination_number" expression="^(\d+)$">
                    <action application="set" data="proxy_media=false"/>
                    <action application="set" data="bypass_media=false"/>
                    <action application="export" data="nolocal:rtp_secure_media=true:AES_CM_128_HMAC_SHA1_80"/>
                    <action application="set" data="dialed_number=$1"/>
                    <action application="log" data="INFO Processing for plivo Secure ${dialed_number}"/>
                    <action application="bridge" data="sofia/gateway/Plivo/$1"/>
                </condition>
            </extension>
        </context>
    </include>
    ```

    ### Step 3 : Generate SSL Certificate

    You could generate the certificate as described here

    **1 - Generate the CA (Root) Certificate**

    To use TLS/SSL you need at least two certificates: the root (CA) certificate and a certificate for every server. There is a script at

    ```
    _/{prefix}/freeswitch/bin/gentls_cert _or within the source tarball _{tarball}/scripts/gentls_cert
    ```

    that helps generate these files. Assuming that the DNS name of your FreeSWITCH PBX is pbx.mydomain.tld, with

    ```
    /usr/bin/gentls_cert setup -cn pbx.mydomain.tld -alt DNS:pbx.mydomain.tld -org mydomain.tld
    ```

    This will create CA certificate and key along with in /etc/freeswitch/tls/CA directory and certificate in the /etc/freeswitch/tls folder.

    ```
    Output: 
    root@ip-x.x.x.x:/etc/freeswitch/dialplan#  /usr/bin/gentls_cert setup -cn pbx.freeswitch.org -alt DNS:pbx.freeswitch.org -org freeswitch.org
    Creating new CA...
    Generating a RSA private key
    ...................................................................
    writing new private key to '/etc/freeswitch/tls/CA/cakey.pem'
    DONE
    ```

    <Note>
      **Note:** The name given for -cn and -alt should be the same as the DNS name of your FreeSwitch installation and used as the registrar name on the phone (at least on Polycom devices). ] You can change the "DAYS=2190" line in the gentls\_cert file to make the certificate valid for a longer time. However making it too long has some wrap around problem, it appears.
    </Note>

    **2 - Generate the Server Certificate**

    ```
    /usr/bin/gentls_cert create_server -cn pbx.freeswitch.org -alt DNS:pbx.freeswitch.org -org freeswitch.org
    ```

    ```
    Output:
    root@ip-x.x.x.x:/etc/freeswitch/dialplan# /usr/bin/gentls_cert create_server -cn pbx.freeswitch.org -alt DNS:pbx.freeswitch.org -org freeswitch.org
    Generating new certificate...
    --------------------------------------------------------
    CN: "pbx.freeswitch.org"
    ORG_NAME: "freeswitch.org"
    ALT_NAME: "DNS:pbx.freeswitch.org"
    Certificate filename "agent.pem"
    [Is this OK? (y/N)]
    y
    Generating a RSA private key
    .............................................................................................
    writing new private key to '/tmp/fs-ca-15020-20190920094519.key'
    Signature ok
    subject=CN = pbx.freeswitch.org, O = freeswitch.org
    Getting CA Private Key
    DONE
    ```

    This creates the server certificate at /etc/freeswitch/tls/agent.pem. This file contains the certificate and the private key. It should contain the domain name in the common and alternate name. If you need to generate certificates for other servers use the -out flag for gentls\_cert to specify the output certificate/key file name and copy this to the remote server.

    In order for the new certificate to take effect (the only way for FreeSWITCH to use it), FreeSWITCH must be restarted.

    <Note>
      **Note**: The name given for -cn and -alt should be the same as the DNS name of your FreeSwitch installation and used as the registrar name on the phone (required for Polycom devices and Eyebeam softphone).
    </Note>

    **Verify your certificate**

    You can review your certificate details with the following command:

    ```
    openssl x509 -noout -inform pem -text -in /etc/freeswitch/tls/agent.pem
    ```

    ```
    cd /etc/freeswitch/tls
    ```

    ```
    chmod 640 agent.pem cafile.pem
    ```

    FreeSwitch only requires the agent.pem file to act as a TLS server. It contains the certificate and the key).

    <Note>
      **Note**: It is extremely important that your agent.pem (and optionally cafile.pem) have read permissions for the user FreeSwitch will run as.
    </Note>

    For example, if you are starting FreeSwitch with the following option\_ -u freeswitch,\_ you have to give read permissions to the “freeswitch” user with the following command:

    ```
    chown root.freeswitch agent.pem cafile.pem
    ```

    ```
    chmod 640 agent.pem cacert.pem
    ```

    **3 - Enable TLS**

    ```sh  theme={null}
    $ vim /etc/freeswitch/vars.xml :

    _<X-PRE-PROCESS cmd="set" data="external_ssl_enable=true"/>_
    ```

    ```sh  theme={null}
    $ vim /etc/freeswitch/sip_profiles/external.xml :

    _<param name="tls-cert-dir" value="/etc/freeswitch/tls/"/>_
    ```

    ### Step 4: Restart FreeSwitch

    You have to restart FreeSwitch for the changes to take effect

    ```
    service freeswitch start
    ```

    To check freeswitch running status:

    ```
    service freeswitch status
    ```

    ## Test your setup

    FreeSwitch instances have default users and SIP passwords preconfigured. To prevent any intrusion, we highly recommend you to change the default password.

    Open vars.xml located at /etc/freeswitch/ and edit the following line:

    ```
    <X-PRE-PROCESS cmd="set" data="default_password=set your password here"/>
    ```

    This change is applicable for all users under /etc/freeswitch/directory/default/. If you want to change the password per user, then navigate to /etc/freeswitch/directory/default/ and edit 1000.xml (or any user of your choice).

    ```
    vim /etc/freeswitch/directory/default/1000.xml
    ```

    ```xml  theme={null}
    <param name="password" value="set your password here"/>
    <variable name="user_context" value="public"/>
    <variable name="effective_caller_id_name" value="Extension 1000"/>
    <variable name="effective_caller_id_number" value="Your Caller ID"/>
    ```

    Execute reloadxml in fs\_cli utility after making changes to any user’s xml.

    ```
    fs_cli -x “reloadxml”
    ```

    ### Make an Outbound Call

    When the account is successfully enabled on X-Lite, it is ready to make calls. Enter any valid 11 digit US number in your X-Lite and click on the call button. This call would go to your freeswitch server first, then through Plivo Secure Zentrunk and finally reach the destination number.

    To know more about configuring X-lite for outbound calls, check the [X-lite configuration guide](/sip-trunking/interconnection-guides/configuring-x-lite/)
  </Tab>
</Tabs>
