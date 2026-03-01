# Source: https://docs.curator.interworks.com/setup/ssl/windows_ssl_iis_deprecated.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Windows SSL (IIS)

> Legacy SSL configuration for deprecated Windows IIS installations

<Danger>Curator no longer supports IIS on new installations.</Danger>

The information below is for use only for existing installs.  It is *highly* recommended that you reinstall with Apache for
stability, please see our
[Windows Apache Installation](/setup/installation/windows_installation)
documentation for steps on how to achieve the best Curator experience for Windows.

## Enabling SSL

1. In IIS Manager, on the left-hand pane, select the server (note: not the site).

2. On the server Home page double-click **Server Certificates** (in the center pane).

3. On the right-hand pane click the `Complete Certificate Request` link.

4. Follow the steps below in the Complete Certificate Request wizard, then click **OK**:

   **File name containing the certificate authority's response:** Your .cer file

   **Friendly name:** Give your cert a name!  Recommended format: `curator-cert-[expiration-date]`

   **Select a certificate store for the new certificate:** Select *Web Hosting*.

5. In IIS Manager, on the left-hand pane, select the site that is running Curator.

6. On the right-hand pane under *Edit Site*, click **Bindings...**.

7. In the Bindings window, click **Add**

8. Follow the steps below in the  Add Site Bindings window, then click **OK**:

   **Type** Select https.

   **IP address** Select the IP address of the site (or select All Unassigned).

   **Port** Type port 443

   **SSL certificate** 	Select the new SSL cert you created in step #4

9. On the right-hand pane click **Restart**
