# Source: https://docs.axonius.com/docs/configuring-the-axonius-platform.md

# Configuring the Axonius Platform

Once the virtual appliance has been installed, complete the following configuration steps:

1. Set the IP address.
2. Log in and signup.
3. Connect adapters.

## 1. Setting the IP Address

<Callout icon="📘" theme="info">
  Note

  If installing on AWS, Azure, GCP (or any public cloud platform) the IP address is set automatically. Therefore you can skip this step.
</Callout>

Once the virtual appliance has been installed, the VMware console window can be used to configure a static IP address – or to view the dynamically assigned IP address if DHCP is being used. Do not set an IP address in the range of  172.17.x.x.

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(358).png" />

<Callout icon="📘" theme="info">
  Note

  IPv6 is supported but disabled by default. Please contact your Axonius representative for more information.
</Callout>

Log in to the system using the console with username **netconfig** and password **netconfig**
NOTE: the netconfig user is NOT accessible via ssh.

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(359).png" />

Follow the wizard for assigning an IP to the machine using a static IP address or DHCP.

1. From the interface list, enter the required interface number.
   * ESX default Interface naming convention – eth0, eth1, etc.
   * Linux default Interface naming convention – ens33, ens34, etc.
2. Enter interface type:
   * "DHCP" for dynamic IP
   * "static" for static IP configuration
3. If you selected "DHCP" for dynamic IP, you can find the dynamically assigned IP by using the SSH credentials below and executing the "ifconfig" command.
    

## 2. Logging in and Signing up

### Logging in to the Web UI

Make sure you open a new ticket with the Axonius Technical Support team to request an updated license file.

After you have configured the IP address,

1. Browse to the machine using a web browser. For example, https\://\\

2. If this does not work, wait 10 minutes and then verify that firewall access to the machine is accessible via port 443.

3. The **License Required** dialog opens and the system asks you to upload your license file.

<Image align="center" alt="LicenseRequired-empty.png" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/LicenseRequired-empty.png" />

4. Click to upload your file, or drag the file to the dialog.

5. Click **Apply**. The system begins the extraction and installation process.

<Image align="center" alt="LicenseRequired-InProgress.png" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/LicenseRequired-InProgress.png" />

6. The license is verified and the Axonius system is decrypted and installed. This can take several minutes.

Once the  decryption and installation process is complete, the Axonius Machine opens:

<Image align="center" alt="LicenseRequired-SelectPrimaryNode.png" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/LicenseRequired-SelectPrimaryNode.png" />

**To connect your Primary Axonius Node**

1. From the **Node Type** select **Primary Node**.
2. Click **Continue**. The system begins to install, this might take a few minutes.
3. The browser opens on the Axonius Signup page.

<Image align="center" alt="SignUpNEw.png" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SignUpNEw.png" />

As part of the initial Axonius signup, you need to to configure the admin user  by providing the following information:

* Email address - the address that will be used by Axonius as a communication channel
* Password – set and confirm the admin password
  To save the admin user configuration, click the **Get Started** button.

<Callout icon="📘" theme="info">
  Note

  You can add two-factor authentication in [Authentication](/docs/managing-password-settings) settings.
</Callout>

To add a new Compute Node refer to [Working with Additional Axonius Compute Nodes](/docs/connecting-additional-axonius-nodes).

## 3 Connecting Adapters

After accessing Axonius through a browser, proceed to connect the relevant adapters.
For each adapter that will be used, please provide the relevant access credentials. The details will vary by adapter, but will include some combination of the following:

* IP Addresses
* Usernames
* Passwords
* Key Files
* Any other credentials needed to access the adapters being used

To learn about connecting adapters, see the [Adapter page](/docs/adapters-screen).

<Callout icon="📘" theme="info">
  Note

  Some adapters require additional steps to gain the relevant connection details, such as generating API keys or other steps. To understand the required actions for connecting each adapter, open its connection documentation page. For more details, see [Adapters List](/docs/adapters-list).
</Callout>