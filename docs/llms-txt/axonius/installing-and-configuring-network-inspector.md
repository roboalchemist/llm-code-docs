# Source: https://docs.axonius.com/docs/installing-and-configuring-network-inspector.md

# Installing and Configuring the Network Inspector

This topic details the Axonius Network Inspector device installation and configuration steps.

## Installation and Configuration Steps

1. Place the device on a flat, stable surface.
2. Plug in the power cable and then power on the device.
3. Connect a monitor and keyboard to the device and verify that the system is initializing.
4. Connect a laptop directly to the **Management** port of the device using an Ethernet cable with an RJ-45 connector.
5. Configure your laptop to the following IP and subnet: **`192.168.0.2/ 255.255.255.0`**.
6. Verify that the green link LED lights up on the Management NIC card.
7. On your laptop, open a browser and enter the management address:  **`https://192.168.0.1:8080`**. The Login page appears in the browser.
8. Log in to the application using the username and password that you received from your account manager.

After a successful login, the **Setup Wizard** is displayed.

<Image align="center" alt="Setup Wizard" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/deployment/Setup_Wizard.png" className="border" />

9. Enter the **Customer Name**, **Site**, and **Location**.
10. In the **Management NIC** section, select the management IP address assignment method: **DHCP** or **Manual** (default). If you select **Manual**, then:
    a. Either leave the default IP address as-is or specify a new IP address and subnet (recommended) in CIDR format (for example: 192.168.0.0/24). Keep a record of the IP address that you assigned.
    b. Enter the **Gateway** address.
11. In the **NTP Servers** section, select the NTP servers assignment method: **Use default NTP servers** (default) or specify **Custom** servers. If you select **Custom**, then either leave the pre-configured server as-is or specify one or more NTP servers.
12. In the **iDRAC NIC** section, select the iDRAC IP address assignment method: **DHCP** (default) or **Manual**. If you select **Manual**, then:
    a. Enter the IP address and subnet in CIDR format.
    b. Enter the Gateway IP address.
13. Click **Save**.  A confirmation page shows the configuration changes that you made.

<Image align="center" alt="Confirm_changes.png" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Confirm_changes.png" className="border" />

13. Click **Apply**.
    The changes are applied. It takes approximately 2 minutes for the updates to take effect, while the **Applying Changes** page is shown.

<Image align="center" alt="Applying_changes.png" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Applying_changes.png" className="border" />

When the configuration is completed, the **Success** page is shown.

<Image align="center" alt="Success.png" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Success.png" className="border" />