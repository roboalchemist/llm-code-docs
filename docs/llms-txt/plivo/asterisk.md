# Source: https://plivo.com/docs/sip-trunking/interconnection-guides/asterisk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Asterisk

> Configure Asterisk with Zentrunk — regular and secure SIP trunking

<Tabs>
  <Tab title="Regular Trunking">
    # Zentrunk & Asterisk - Regular Trunking

    ## Overview

    Zentrunk is a SIP Trunking service from Plivo that allows you to connect with fixed and mobile phones in over 200 countries. Connect your cloud or on-premise communication infrastructure to Plivo’s Zentrunk SIP Trunking service to connect to your customers easily.

    This documentation provides a basic configuration to get Asterisk up and running with Plivo as the external SIP gateway.

    To get started with Zentrunk using Asterisk you would need to do the following:

    1. [Install Asterisk on your environment](/sip-trunking/interconnection-guides/asterisk/#installation-of-freeswitch).
    2. [Create a Trunk on Zentrunk using Plivo Console](/sip-trunking/#create-an-outbound-trunk).
    3. [Configure an Outbound Trunk](/sip-trunking/interconnection-guides/asterisk/#configuring-an-outbound-trunk).
    4. [Configure the Inbound Trunk](/sip-trunking/interconnection-guides/asterisk/#configuring-an-inbound-trunk).

    ## Installation of Asterisk

    For installing Asterisk, follow the instructions below:

    * For Debian systems execute the following commands in the terminal.

      1. `apt-get update`
      2. `apt-get upgrade`
      3. `apt-get install asterisk`

    * Follow the instructions given [here](https://www.voip-info.org/wiki/view/Asterisk+11+Installation+on+CentOS+6) to install Asterisk on CentOS.

    ## Create a Trunk on Zentrunk

    You can create a trunk using Plivo Console. For more information on creating a Trunk on Plivo Console, see below links:

    * [Create an Outbound Trunk](/sip-trunking/#create-an-outbound-trunk)
    * [Create an Inbound Trunk](/sip-trunking/#create-an-inbound-trunk)

    ## Configuring Asterisk for Outbound Trunk

    To configure the asterisk to connect to your Plivo Zentrunk, locate the root configuration of Asterisk on your machine. These locations vary from platform to platform.

    In this case (Debian Jessie GNU/Linux System), the root configuration is present at /etc/asterisk/.

    With the root configuration directory located, there are two major configurations that need to do -

    1. Create a new SIP Channel
    2. Create a Dial Plan.
    3. Reload the configuration

    ### Step 1: SIP Channel

    Create a new channel named "plivo-phone" at /etc/asterisk/sip.conf. This channel will be used in X-Lite to connect to asterisk. Also, create another channel called “plivo-trunk” which will connect to your Plivo Trunk.

    ```shell  theme={null}
    [plivo-phone]
    type=friend
    context=Zentrunk
    host=dynamic
    secret=password1234

    [zentrunk]
    type=peer
    context=Plivo
    host=Termination SIP Domain of your Plivo Trunk
    secret=Password for TestAuthGroup
    username=Username for TestAuthGroup
    ```

    A "plivo-phone" channel is created with the following attributes.

    * Type=friend - Creates a user and peer connection
    * Context=Zentrunk - Context is the identifier for a dialplan that will be loaded from extensions.conf. The sip.conf identifies and allows connections to the asterisk server. The context in the identifier allows the execution of call flow when a call is received from XLite.
    * Host=dynamic - XLite can be connected from anywhere
    * Secret=password1234 - Password to be used in X-Lite

    The "zentrunk" channel is created with the following attributes.

    * Type=peer - Creates a peer connection
    * Context=Plivo - Context is the identifier for a dialplan that will be loaded from extensions.conf. The sip.conf identifies and allows connections to the asterisk server. The context in the identifier allows the execution of call flow when a call is received from XLite.
    * Host=Termination SIP Domain of your Plivo Trunk
    * Secret=Password for TestAuthGroup
    * Username=Username for TestAuthGroup

    ### Step 2: Dialplan

    Next, you should set up a Dial Plan. A Dial Plan tells Asterisk what to do when a call has to be placed. The "Content" attribute in the SIP channel connects a channel with a dialplan. Add a dialplan named “Zentrunk” in extensions.conf under /etc/asterisk/directory.

    ```shell  theme={null}
    [Zentrunk]
    exten => _1XXXX.,1,Set(CALLERID(all)="Your Plivo Number" <Your Plivo Number>)
    exten => _1XXXX.,n,Dial(SIP/zentrunk/${EXTEN})
    exten => _1XXXX.,n,Hangup()
    ```

    The above dial plan has defined an extension for a number starting with the digit 1. When a call is made from X-Lite to a number that starts with 1, it hits the asterisk server first. The dialplan that satisfies this pattern matching get loaded, in this case, the above plan. The caller ID is set to your Plivo Number and the SIP INVITE is sent to "Zentrunk" channel which forwards the invite to Plivo Trunk from where the outbound call is placed.

    ### Step 3: Reload Configurations

    1. Load the asterisk client.
    2. Execute the following command in your terminal:
       ```shell  theme={null}
       asterisk -rvvvv
       ```
    3. Reload the sip channel, and then execute the following command:
       ```shell  theme={null}
       sip reload
       ```
    4. Reload the dialplan, and then execute the following command:
       ```shell  theme={null}
       dialplan reload.
       ```

    ## Configuring Asterisk for Inbound Trunk

    To configure your asterisk to connect to your Plivo Zentrunk, locate the root configuration of Asterisk on your machine. These locations vary from platform to platform.

    In this case (Debian Jessie GNU/Linux System), the root configuration is present at /etc/asterisk/.

    With the root configuration directory located, there are three major configurations that you need to do -

    1. Create a new SIP Channel
    2. Create a Dial Plan.
    3. Create a Sip Driver.
    4. Reload the configuration

    ### Step 1: Create a new SIP Channel

    Create a new channel named "6001" at /etc/asterisk/sip.conf. This channel will be used in X-Lite to connect to asterisk.

    ```shell  theme={null}
    [general]
    context=incoming

    [6001]
    type=friend
    context=from-internal
    host=dynamic
    secret=1234
    disallow=all
    allow=ulaw
    ```

    A 6001 channel is created with the following attributes.

    <Note>
      **Note:** Use 6001 as your user in X-lite.
    </Note>

    * Type=friend - Creates a user and peer connection .
    * Context=incoming - Context is the identifier for a dialplan that will be loaded from extensions.conf. The sip.conf identifies and allows connections to the asterisk server. The context in the identifier allows the execution of call flow when a call is received from XLite.
    * Host=dynamic - XLite can be connected from anywhere
    * Secret=1234 - Password to be used in X-Lite

    ### Step 2: Dialplan

    Next, you should set up a Dial Plan. A Dial Plan tells Asterisk what to do when a call is received .The "Content" attribute in the SIP channel connects a channel with a dialplan. Add a dialplan named “incoming” in extensions.conf under /etc/asterisk/directory.

    ```shell  theme={null}
    [incoming]
    exten => _X.,1,Wait(1)
    exten => _X.,n,Dial(SIP/6001)
    ```

    The above dial plan has defined an extension for a SIP enpoint named 6001. When a call is made to your inbound number, it hits the Plivo first and then it is forwarded to your asterisk server .Once the dialplan is loaded and the call is placed to the soft phone registered as 6001 in your asterik

    ### Step 3: Create a SIP Driver

    Create a new SIP driver named “6001” at /etc/asterisk/pjsip.conf with the below information.

    <Note>
      **Note:** Make sure that the secret in the sip.conf file and the password of pjsip.conf is the same.
    </Note>

    ```shell  theme={null}
    [transport-udp]
    type=transport
    protocol=udp
    bind=0.0.0.0

    [6001]
    type=endpoint
    context=from-internal
    disallow=all
    allow=ulaw
    auth=6001
    aors=6001

    [6001]
    type=auth
    auth_type=userpass
    password=1234
    username=6001

    [6001]
    type=aor
    max_contacts=1
    ```

    ### Step 4: Reload Configurations

    1. Load the asterisk client.
    2. Execute the following command in your terminal:
       ```shell  theme={null}
       asterisk -rvvvv
       ```
    3. Reload the sip channel, and then execute the following command:
       ```shell  theme={null}
       sip reload
       ```
    4. Reload the dialplan, and then execute the following command:
       ```shell  theme={null}
       dialplan reload
       ```
  </Tab>

  <Tab title="Secure Trunking">
    # Secure Trunking using chan\_pjsip

    ## Overview

    In this section, we will guide you through the steps to configure Asterisk to implement secure trunking for outbound calling. To configure the asterisk using **chan\_pjsip** to connect to your Plivo Zentrunk, locate the root configuration of Asterisk on your machine. These locations vary from platform to platform. In this case (**Debian Jessie GNU/Linux System**), the root configuration is present at */etc/asterisk*.

    With the root configuration directory located, two major configurations need to be done-

    1. Create an *endpoint* for Trunk
    2. Create a Dial Plan
    3. Reload the configuration / Restart Asterisk

    ## Step 1: Create an endpoint for Trunk

    Create a new endpoint named **zentrunk\_endpoint\_out** at */etc/asterisk/pjsip.conf*. You can use this endpoint to connect Zentrunk.

    ### pjsip.conf

    **Endpoint to connect Zentrunk**

    ```conf  theme={null}
    [zentrunk_endpoint_out]
    type=endpoint
    transport=transport-udp
    aors=zentrunk_aor
    disallow=all
    allow=ulaw
    outbound_auth=zentrunk_auth

    [zentrunk_aor]
    type=aor
    contact=sip:xxxxxxxxxxxxxxxx.zt.plivo.com:5060

    [zentrunk_auth]
    type=auth
    auth_type=userpass
    password=mitesh123
    username=mitesh

    [transport-udp]
    type=transport
    protocol=udp
    bind=0.0.0.0:5060
    ```

    * **\[zentrunk\_endpoint\_out]**: This is an endpoint definition.

    * **\[zentrunk\_aor]**: This defines the Address of Record to be used by endpoint - `zentrunk_endpoint_out`. This tells Asterisk where an endpoint can be contacted. For that you will need to configure `contact` with the url which will point to Zentrunk as below:

      ```conf  theme={null}
      contact=sip:<"TERMINATION SIP DOMAIN" of your ZENTRUNK's Outbound Trunk> :5060
      ```

    * **\[zentrunk\_auth]**: This defines authentication for `zentrunk_endpoint_out`. When the Trunk challenges for the INVITE from Asterisk, this section will be used to authenticate.

    * \[**transport-udp**]: The endpoint `zentrunk_endpoint_out` will use transport mentioned under this section.

    To test outbound calls using the above mentioned Trunk Configuration you may need an internal phone extension. For that, you may configure phone extension `6001` as mentioned below in pjsip.conf itself.

    **Internal extension / phone configuration**

    ```conf  theme={null}
    [6001]
    type=endpoint
    context=Zentrunk
    disallow=all
    allow=ulaw
    auth=6001
    aors=6001

    [6001]
    type=auth
    auth_type=userpass
    password=password1234
    username=6001

    [6001]
    type=aor
    max_contacts=1
    ```

    You can register any SIP enabled phone with `username: 6001` and `password: password1234`

    ## Step 2: Dialplan

    Next, you should set-up a dialplan. Below mentioned dial plan will dial out to ZENTRUNK using `zentrunk_endpoint_out` when 6001 (the SIP phone registered with username 6001) dial a number. Note that we have mentioned context=Zentrunk under endpoint 6001.

    Add below dial plan in **extensions.conf** under directory /etc/asterisk.

    ### extensions.conf

    ```conf  theme={null}
    [Zentrunk]
    exten => _X.,1,Set(CALLERID(all)="Your Plivo Number" <Your Plivo Number>)
    exten => _X.,n,Dial(PJSIP/${EXTEN}@zentrunk_endpoint_out)
    exten => _X.,n,Hangup()
    ```

    ## Step 3: Reload Configurations

    1. Execute the following command in your terminal to connect to the asterisk CLI:

    ```sh  theme={null}
    Asterisk -rvvvv
    ```

    2. Execute the below command to reload chan\_pjsip:

    ```sh  theme={null}
    pjsip reload
    ```

    3. Reload dialplan using below command:

    ```sh  theme={null}
    dialplan reload
    ```

    <Note>
      **Caution**: Configuration for **transport type** sections can't be reloaded during run-time without a full module unload and load. You need to restart Asterisk completely for your transport changes to take effect. We have one transport type section in the above configuration that is `transport-udp`. To restart asterisk please follow the below step.
    </Note>

    ## Restart Asterisk

    Execute the below command from the Linux command line to restart Asterisk.

    ```sh  theme={null}
    systemctl restart asterisk
    ```
  </Tab>
</Tabs>
