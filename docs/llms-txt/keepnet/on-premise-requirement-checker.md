# Source: https://doc.keepnetlabs.com/next-generation-product/miscellaneous/on-premise-requirement-checker.md

# On-Premise Requirement Checker

## **On-premise Requirement Checker**

This section provides a detailed explanation of the On-premise Requirement Checker (OPRC) to ensure that the installation and configuration process of the platform will be easy.

## **Download the OPRC**

This tool allows you to easily verify that your system meets the platform requirements before installation to speed up the process. You can download and install the OPRC tool to the server using this link.

## **OPRC Setup**

Once the OPRC has been downloaded to the servers where the platform will be installed, only a few steps are necessary to assess and configure the required settings.

* Run the setup file as administrator.
* Click the **Next** button.
* Leave the **Installation Folder** as the default option. Select **Everyone** and click the **Next** button.
* Click the **Next** button to complete the installation.

Once the installation is complete, you will find a shortcut on the desktop to run the application.

### **Configurations**

When the application is launched, you can evaluate and adjust the following elements under the **Configurations** heading.

#### **LDAP Configuration**

The platform needs to provide a connection to the **Active Directory** server located in the client's internal network in order to integrate the active directory over LDAP to fetch and synchronize users to the platform.

The following components are used to ensure the connection has been established:

<table data-header-hidden><thead><tr><th width="159">Name</th><th width="582.7312641937926">Function</th><th data-hidden></th></tr></thead><tbody><tr><td>Server IP or Hostname</td><td>Active Directory server IP or hostname information. If a different port is preferred for the connection, use <strong>IP:PORT</strong> format.</td><td></td></tr><tr><td>Username</td><td>Domain username used to login to the active directory server. It should be specified as <strong>Domain\Username.</strong></td><td></td></tr><tr><td>Password</td><td>Password of the user to login to the active directory server.</td><td></td></tr><tr><td>Test Configuration</td><td>Confirm the configuration.</td><td></td></tr></tbody></table>

{% hint style="info" %}
If the configuration test results in an error, go to the Output tab for details of the problem.
{% endhint %}

#### **Proxy Configuration**

A proxy server may be required to successfully use the platform if the customer wish the on-premise server to go through the internet over their proxy server. The following components are used to establish the proxy server connection to the internet.

<table data-header-hidden><thead><tr><th width="163"></th><th width="586.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Server IP or Hostname</td><td>Proxy Server’s IP or Hostname</td><td></td></tr><tr><td>Server Port</td><td>Port used to connect to the proxy server</td><td></td></tr><tr><td>Authentication</td><td>If authentication is required for connections to the proxy server, this option should be enabled.</td><td></td></tr><tr><td>Username</td><td>If authentication is required for connection to the proxy server, provide the name of the authorized user.</td><td></td></tr><tr><td>Password</td><td>If authentication is required for connection to the proxy server, provide the password of the authorized user.</td><td></td></tr><tr><td>Test Configuration</td><td>Confirm the configuration.</td><td></td></tr></tbody></table>

{% hint style="info" %}
In order to use the [Phishing Simulator](https://keepnetlabs.com/products/phishing-simulator) product, the ability to send anonymous emails must be enabled.
{% endhint %}

{% hint style="info" %}
If the test results in an error, go to the Output tab for details of the problem.
{% endhint %}

### **Database Configuration**

The platform database must have a connection to the server. The necessary components for two popular server types are provided below.

#### **Microsoft SQL Server**

This step is not necessary if the Next Generation Product has been installed.

<table data-header-hidden><thead><tr><th width="163"></th><th width="584.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Server IP or Hostname</td><td>IP or hostname of the Microsoft SQL server. If a different port is preferred for the connection, use IP:PORT format.</td><td></td></tr><tr><td>Database Name</td><td>Name of the database where the product is going to be installed</td><td></td></tr><tr><td>Username</td><td>If a SQL authentication method is required for connection to</td><td></td></tr><tr><td></td><td>Microsoft SQL server, provide the name of the authorized user.</td><td></td></tr><tr><td>Password</td><td>If a SQL authentication method is required for connection to Microsoft SQL server, provide the password of the authorized user.</td><td></td></tr><tr><td>Windows Authentication</td><td>If the Windows authentication method is used for connection to Microsoft SQL server, this option should be enabled. This should be the user who activates the OPRC tool.</td><td></td></tr><tr><td>Test Configuration</td><td>Confirm the configuration</td><td></td></tr></tbody></table>

{% hint style="info" %}
If the test results in an error, go to the Output tab for details of the problem.
{% endhint %}

#### **PostgreSQL Server**

This step is not necessary if the Current UI (legacy interface) has been installed.

<table data-header-hidden><thead><tr><th width="160"></th><th width="584.1428571428571"></th><th data-hidden></th></tr></thead><tbody><tr><td>Server IP or Hostname</td><td>IP or Hostname of the PostgreSQL server</td><td></td></tr><tr><td>Port</td><td>Port used to connect to the PostgreSQL server</td><td></td></tr><tr><td>Database Name</td><td>Name of the database where the product is installed</td><td></td></tr><tr><td>Username</td><td>If a SQL authentication method is required for connection to the PostgreSQL server, provide the name of the authorized user.</td><td></td></tr><tr><td>Password</td><td>If a SQL authentication method is required for connection to the PostgreSQL server, provide the password of the authorized user.</td><td></td></tr><tr><td>Test Configuration</td><td>Confirm the configuration</td><td></td></tr></tbody></table>

{% hint style="info" %}
If the test results in an error, go to the Output tab for details of the problem.
{% endhint %}

### **Current UI and New UI Tabs**

The OPRC will check the hardware and software settings to ensure that the requirements are met for the successful use of the platform.

* A “✓” icon indicates that the platform can be installed and implemented.
* An “✘” icon indicates that an element must be revised.

### **Output**

The Output tab provides an explanation of how to revise any settings required to ensure successful use of the platform.

## FAQ

### Q: What should I do when all requirements are completed?

A: You can contact with the support team for further installation process by sharing that all requirements are completed and checked with the tool.
