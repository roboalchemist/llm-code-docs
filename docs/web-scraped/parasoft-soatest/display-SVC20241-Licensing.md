# Source: https://docs.parasoft.com/display/SVC20241/Licensing?src=contextnavpagetreemode

Title: Licensing - SOAtest and Virtualize with CTP 2024.1

URL Source: https://docs.parasoft.com/display/SVC20241/Licensing?src=contextnavpagetreemode

Markdown Content:
This section describes how to license the desktop instance of SOAtest and Virtualize.For information about licensing the web archive (WAR) deployment of the server, see[Licensing the Server](https://docs.parasoft.com/display/SVC20241/Licensing+Virtualize+Server).

In this section:

Network Licenses
----------------

You can configure SOAtest and Virtualize to use a license served from Parasoft DTP or a standalone instance of Parasoft License Server.Contact your system administrator for information about which type of license you should use.

DTP License
-----------

You can use a license from DTP or license configuration settings from a DTP Project. Your Parasoft DTP administrators should verify that the product and version you are licensing appears in the DTP License Server. Administrators can refer to the DTP documentation for information about updating the tools database. Refer to [Connecting to DTP](https://docs.parasoft.com/display/SVC20241/Connecting+to+DTP) for additional information.

1.   Choose**Parasoft > Preferences**and click on the **DTP** category.
2.   Enable the **Enable** option and specify the DTP URL, including the `https://` protocol, in the **Base URL** field.Note that DTP does not support `http://` connections. If DTP is deployed to a location other than the root of the host server, the URL should include a context path (a relative path from the host name; f or example:`https://server.company.com:8443/contextPath`). This may be the case if your organization uses a reverse proxy.Refer to the DTP documentation on [https://docs.parasoft.com](https://docs.parasoft.com/) for additional information about reverse proxy server configuration and context path configuration.
3.   Enter your DTP login credentials in the **User name**and **Password**fields.
4.   Click**Test Connection** to verify that the settings are correct.
5.   If you are going to use a license configuration associated with a specific DTP project, click **Configure**in the Project section and choose a project, then click **OK**.
6.   Click **Apply** and click the **Configure...**link in the**License**section.
7.   If you have multiple Parasoft products installed, open the tab for the Parasoft product you want to license (for example, Jtest, SOAtest, Virtualize).
8.   Enable the **Network**option and click the**Configure...**link.

9.   Enable the **Use configured DTP settings** option. If you are going to use a license configuration associated with a specific DTP project, enable the **Use License Server settings from DTP project**to use the license configuration associated with the project selected in step 5 instead.
10.   Click**OK**to close the dialog.
11.   Choose the product edition from the **Edition** menu. Contact your Parasoft administrator for assistance selecting an edition or custom edition features.
12.   You can enable the **Borrow** option and specify a length of time for which SOAtest and Virtualize will consume a license token. Licenses can be borrowed from 1 hour to 14 days.Refer to the DTP documentation for additional information about borrowing licenses.

13.   **Apply** to save your settings.

License Server
--------------

You can connect to License Server to retrieve a license token, even if you are connected to a separate instance of DTP.

1.   Choose**Parasoft > Preferences**and click on the **License** category.
2.   If you have multiple Parasoft products installed, open the tab for the Parasoft product you want to license (for example, Jtest, SOAtest, Virtualize).
3.   Enable the **Network**option and click the**Configure...**link.

4.   Enable the**Use the following License Server** option and specify the License Server URL, including the `https://` protocol, in the **Base URL** field.Note that License Server does not support `http://` connections. If License Server is deployed to a location other than the root of the host server, the URL should include a context path (a relative path from the host name; f or example:`https://server.company.com:8443/contextPath`). This may be the case if your organization uses a reverse proxy.Refer to the DTP documentation on [https://docs.parasoft.com](https://docs.parasoft.com/) for additional information about reverse proxy server configuration and context path configuration.
5.   If the License Server requires authentication, enable the **Enable Authentication** option and enter your credentials in the**User name** and **Password**fields.
6.   Click **Test Connection** to verify your settings and click **OK** to save your changes.
7.   Choose the product edition from the **Edition** menu. Contact your Parasoft administrator for assistance selecting an edition or custom edition features.
8.   You can enable the **Borrow** option and specify a length of time for which SOAtest and Virtualize will consume a license token. Licenses can be borrowed from 1 hour to 14 days.Refer to the License Server documentation for additional information about borrowing licenses.

9.   Click **Apply** to save your settings.

Connecting to DTP or License Server Via a Proxy
-----------------------------------------------

If a proxy server is required to connect to the DTP server or License Server, configure the proxy settings by going to **Window**>**Preferences**to open the Preferences dialog and selecting **General**>**Network Connections**, then configuring the appropriate proxy settings to connect to the server.

Deactivating License
--------------------

You can deactivate/activate licenses by choosing **Parasoft > Deactivate License/Active License**.

You can also configure the license to automatically deactivate after 30 minutes of inactivity:

1.   Go to **Parasoft > Preferences**and click the **License** category.
2.   Enable the **Start deactivated, release automatically when idle** option.
3.   Click **Apply** to save your changes.

When the license is deactivated:

*   Parasoft views are disabled and results are cleared from the Quality Tasks view.
*   The license token is released in DTP or License Server.

Licensed views are restored and the Quality Tasks view will display available results when the license is reactivated.

Waiting for a License in Command Line Mode
------------------------------------------

You can configure SOAtest and Virtualize to wait for a license token if a requested token is not currently available by specifying the`license.wait.for.tokens.time` option when using the command line interface.

For additional information, see the following pages:

*   [Settings](https://docs.parasoft.com/display/SVC20241/Additional+Preference+Settings#AdditionalPreferenceSettings-Localsettings) in Virtualize
*   [Configuring Settings](https://docs.parasoft.com/display/SVC20241/Configuring+Settings) in SOAtest
*   [Testing from the Command Line Interface - soatestcli](https://docs.parasoft.com/display/SVC20241/Testing+from+the+Command+Line+Interface+-+soatestcli)

Stabilizing the Machine ID
--------------------------

Changes in the network environment may affect the interface that is used to compute your machine ID, resulting in machine ID instability. You can use the `PARASOFT_SUPPORT_NET_INTERFACES`environment variable to specify a stable interface and prevent the machine ID from floating.

1.   Set up the PARASOFT_SUPPORT_NET_INTERFACES environment variable according to your operating system.
2.   Set the variable value to a stable ethernet network interface. Do not use virtual, temporary, or loopback interfaces.
    *   Windows: Set the value to the MAC address of your network card, for example:

`SET``PARASOFT_SUPPORT_NET_INTERFACES=00-10-D9-27``-AC``-85` 
    *   Linux/macOS: Set the value to one of the network interfaces from the "inet" or "inet6" family, for example:

`export``PARASOFT_SUPPORT_NET_INTERFACES=eth1` 

Using a Local License
---------------------

Local licenses do not request a license token from a server on the network. Instead, they are locked to a specific machine. You will need to provide your machine ID to your Parasoft representative, who will send you a license password. The machine ID appears in the Parasoft license configuration screen.

1.   Choose**Parasoft > Preferences**to and select the**License**category.
2.   If you have multiple Parasoft products installed, open the tab for the Parasoft product you want to license (for example, Jtest, SOAtest).
3.   Enable the**Local**option.
4.   If you have not already done so, note the machine ID in the **Machine id** field and send it to your Parasoft representative to obtain a license password. You can also run a command using the command line interface to print the machine ID to the console. Without a license, the following message will appear:`Error: No valid license (MachineId: WIN32-12345678)`.
5.   Enter your license password from Parasoft and click**Apply**. The License preferences page will display the features that you are licensed to use, and the expiration date for your license.
6.   Click**OK**to set and save your license.

Additional Licensing Considerations for SOAtest Server
------------------------------------------------------

If you are using the combined SOAtest/Virtualize distribution, a Virtualize license is required to run SOAtest Server. In some instances, you may only have a license for SOAtest, for example if you are updating to a paid license from the Free License. Contact your Parasoft representative for additional information about licensing options.

Manually Configuring the License
--------------------------------

You can create SOAtest and Virtualize configuration file and specify your license settings. See [Configuring Settings](https://docs.parasoft.com/display/SVC20241/Configuring+Settings) (SOAtest) and [Settings](https://docs.parasoft.com/display/SVC20241/Additional+Preference+Settings#AdditionalPreferenceSettings-Localsettings) (Virtualize)for details on creating and configuring the file.

Importing and Exporting License Configuration Settings
------------------------------------------------------

You can export your configuration settings to a _.properties_ file and share with team members. See [Configuring Settings](https://docs.parasoft.com/display/SVC20241/Configuring+Settings) or [Settings](https://docs.parasoft.com/display/SVC20241/Additional+Preference+Settings#AdditionalPreferenceSettings-Localsettings) for details.

Configuring SOAVirt WAR License from CTP
----------------------------------------

Once the registration of the Virtualize server is complete you will be redirected to the server detail page.

1.   Click the ellipses ( **...** ) menu in the upper-right corner and select **Configure License**. This option is only applicable to war file deployment servers.

![Image 1](https://docs.parasoft.com/download/attachments/195706182/image-2021-06-30-15-17-26-957.png?version=1&modificationDate=1711559549036&api=v2)

You will see the Configure License screen asking for either a**Local**or **Network**license. For more information go to [Licensing the Server](https://docs.parasoft.com/display/SVC20241/Licensing+Virtualize+Server).
2.   From the Configure License screen, generate a **Local**with the provided machine ID and enter it in the text box.

![Image 2](https://docs.parasoft.com/download/attachments/195706182/image-2021-06-30-15-17-08-926.png?version=1&modificationDate=1711559549072&api=v2)
3.   Or enter the**Network**license server information and set the desired**Virtualize**and**SOAtest**editions.

![Image 3](https://docs.parasoft.com/download/attachments/195706182/image-2021-06-30-15-16-26-578.png?version=1&modificationDate=1711559549114&api=v2)

4.   Choose features, if**Custom Edition** is selected.

![Image 4](https://docs.parasoft.com/download/attachments/195706182/image-2021-06-30-15-16-54-138.png?version=1&modificationDate=1711559549179&api=v2)
