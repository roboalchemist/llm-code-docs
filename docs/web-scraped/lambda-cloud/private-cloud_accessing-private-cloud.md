# Accessing your Lambda Private Cloud cluster -

Source: https://docs.lambda.ai/private-cloud/accessing-private-cloud/

---

[security ](../../tags/#tag:security)
# Accessing your Lambda Private Cloud cluster [# ](#accessing-your-lambda-private-cloud-cluster)

## Introduction [# ](#introduction)

[Lambda Private Cloud ](https://lambda.ai/service/gpu-cloud/private-cloud)clusters use Fortinet FortiGate firewall appliances to enable secure VPN access. To access your Private Cloud cluster through the firewall, you must first install and configure FortiClient VPN (FortiClient). 

## Download and install FortiClient [# ](#download-and-install-forticlient)

Download and install the appropriate FortiClient package for your computer: 

- [Download for Windows ](https://links.fortinet.com/forticlient/win/vpnagent)
- [Download for MacOS ](https://links.fortinet.com/forticlient/mac/vpnagent)
- [Download for Ubuntu ](https://links.fortinet.com/forticlient/deb/vpnagent)(and other `.deb`-based distributions) 
- [Download for Red Hat ](https://links.fortinet.com/forticlient/rhel/vpnagent)(and other `.rpm`-based distributions) 
FortiClient for other devices, including ARM64 systems, can be downloaded from Fortinet's [product downloads ](https://www.fortinet.com/support/product-downloads#vpn)page. 

## Configure the VPN connection [# ](#configure-the-vpn-connection)

Next, you'll configure FortiClient using the credentials provided in your 1Password vault, which looks like: 

[![Screenshot of a 1Password vault for Private Cloud](../../assets/images/private-cloud/1password-vault.png)](../../assets/images/private-cloud/1password-vault.png)

- 
Open FortiClient. 

- 
Click **Configure VPN **. 

- 
In the **New VPN Connection **window, enter the following settings: 

  - **VPN **: Select **SSL-VPN **. 
  - **Connection Name **: Enter a descriptive name for the VPN connection. 
  - (Optional) **Description **: Enter a description for the VPN connection. 
  - **Remote Gateway **: Enter the VPN URL from your 1Password vault. Omit the port number. 
  - Select the **Customize port **checkbox and enter the VPN URL port number. 
  - Clear the **Enable Single Sign On (SSO) for VPN Tunnel **checkbox. 
  - **Client Certificate **: Select **None **. 
  - **Authentication **: Select **Prompt on login **. 
  - Clear the **Enable Dual-stack IPv4/IPv6 address **checkbox. 
Your configuration should look like this: 

[![Screenshot of a FortiClient VPN connection configured for Private Cloud](../../assets/images/private-cloud/forticlient-new-vpn-connection.png)](../../assets/images/private-cloud/forticlient-new-vpn-connection.png)

- 
Click **Save **. 

- 
In the main window, select the VPN connection you just created from the dropdown menu: 

[![Screenshot of the FortiClient main window](../../assets/images/private-cloud/forticlient-main-window.png)](../../assets/images/private-cloud/forticlient-main-window.png)

- 
Enter the **Username **and **Password **provided in your 1Password vault. 

- 
Click **Connect **. 

You're asked to confirm that you want to connect to the VPN: 

[![Screenshot of prompt to accept or deny certificate](../../assets/images/private-cloud/forticlient-cert-confirmation.png)](../../assets/images/private-cloud/forticlient-cert-confirmation.png)

- 
Verify that the certificate fingerprint matches the fingerprint shown in your 1Password vault. Then, click **Accept **. 

You're connected to your Private Cloud cluster when FortiClient shows the VPN connection is active: 

[![Screenshot of FortiClient connect to Private Cloud VPN](../../assets/images/private-cloud/forticlient-vpn-connected.png)](../../assets/images/private-cloud/forticlient-vpn-connected.png)

## Next steps [# ](#next-steps)

- [Learn about Lambda Private Cloud clusters ](https://lambda.ai/service/gpu-cloud/private-cloud). 
- [Learn about Lambda 1-Click Clusters ](https://lambda.ai/service/gpu-cloud/1-click-clusters).
