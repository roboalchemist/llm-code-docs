# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/network-security/securing-behind-proxy.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/data-center-edition/network-security/securing-behind-proxy.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/network-security/securing-behind-proxy.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/data-center-edition/network-security/securing-behind-proxy.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/network-security/securing-behind-proxy.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/data-center-edition/network-security/securing-behind-proxy.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/network-security/securing-behind-proxy.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/data-center-edition/network-security/securing-behind-proxy.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/network-security/securing-behind-proxy.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/network-security/securing-behind-proxy.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/network-security/securing-behind-proxy.md

# Securing behind a proxy

For most production instances, traffic encryption (and therefore HTTPS) is required. As SonarQube only supports plain HTTP for inbound traffic, a reverse proxy is necessary to terminate SSL/TLS encryption before SonarQube.

If you deploy SonarQube on Kubernetes, you’ll need an ingress controller. An ingress controller is a specialized load balancer for Kubernetes that acts as a reverse proxy and manages traffic routing to services within the Kubernetes cluster. See [#ingress](https://docs.sonarsource.com/sonarqube-server/on-kubernetes-or-openshift/customizing-helm-chart#ingress "mention").

### General guidelines <a href="#general-guidelines" id="general-guidelines"></a>

{% hint style="info" %}
For security reasons, we recommend only giving external access to the main port.
{% endhint %}

The reverse proxy should be configured to set the following standard headers:

* `X-Forwarded-Proto`
* `X-Forwarded-For`

This setting is mandatory if you use HTTPS or SAML authentication for SonarQube.

In the example below, where HTTPS is used from the client to the reverse proxy, the reverse proxy will set:

* `X-Forwarded-Proto` to `HTTPS`
* `X-Forwarded-For` to `<clientIpAddress>`

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/F4SbAEi70usdHWKwrWGv/1d3e46d9ae25e03394e72c7d0929c4fa1adc5155.png" alt="As SonarQube only supports plain HTTP for inbound traffic, a reverse proxy to support HTTPS"><figcaption></figcaption></figure>

In addition, the reverse proxy may be configured to forward the following custom headers:

* `SonarQube-Authentication-Token-Expiration`\
  This header is added to a web service response when using tokens to authenticate. Forwarding this header is not required for the SonarQube features to work properly.
* `Sonar-MD5`\
  This header is used to verify the integrity of the plugins downloaded by the scanner. You must forward this header to successfully execute analyses that use plugins.

For information about tokens, see [managing-tokens](https://docs.sonarsource.com/sonarqube-server/user-guide/managing-tokens "mention").

### Using Nginx proxy <a href="#using-nginx-proxy" id="using-nginx-proxy"></a>

Nginx configuration will vary based on your own application’s requirements and the way you intend to expose SonarQube to the outside world. If you need more details about Nginx, see [Nginx documentation](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/).

In the following, we assume that you’ve already installed Nginx, that you are using a Virtual Host for `www.somecompany.com` and that SonarQube is running and available on `http(s)://sonarhost:sonarport/`.

At this point, edit the Nginx configuration file:

* Include the code below to expose SonarQube at `http://www.somecompany.com/` or `https://www.somecompany.com/`

{% tabs %}
{% tab title="WITH HTTP" %}

```nginx
# the server directive is Nginx's virtual host directive
server {
  # port to listen on. Can also be set to an IP:PORT
  listen 80;
  # sets the domain[s] that this vhost server requests for
  server_name www.somecompany.com;
  location / {
    proxy_pass http://<sonarhost>:<sonarport>;
  }
}
```

{% endtab %}

{% tab title="WITH HTTPS" %}

```nginx
# the server directive is Nginx's virtual host directive
server { 
 # port to listen on. Can also be set to an IP:PORT 
 listen 443 ssl;
 ssl_certificate <path_to_your_certificate_file>;
 ssl_certificate_key <path_to_your_certificate_key_file>;
 location / {
   proxy_pass <address-of-your-sonarqube-instance-behind-proxy>;
   proxy_set_header Host $host;
   proxy_set_header X-Forwarded-For $remote_addr;
   proxy_set_header X-Forwarded-Proto https;
 }
}
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
You may need to increase the max URL length since SonarQube requests can have URLs longer than 2048.
{% endhint %}

### Using Apache proxy <a href="#using-apache-proxy" id="using-apache-proxy"></a>

Apache configuration is going to vary based on your own application’s requirements and the way you intend to expose SonarQube to the outside world. If you need more details about Apache HTTPd and mod\_proxy, see the [Apache documentation](https://httpd.apache.org).

In the following, we assume that you’ve already installed Apache 2 with module mod\_proxy, that SonarQube is running and available on `http://private_sonar_host:sonar_port/`, and that you want to configure a Virtual Host for `www.public_sonar.com`.

At this point, edit the HTTPd configuration file for the `www.public_sonar.com` virtual host:

* Include the following to expose SonarQube via `mod_proxy` at [`http://www.public_sonar.com/`](http://www.public_sonar.com/)

```apacheconf
ProxyRequests Off
ProxyPreserveHost On
<VirtualHost *:80>
  ServerName www.public_sonar.com
  ServerAdmin admin@somecompany.com
  ProxyPass / http://private_sonar_host:sonar_port/
  ProxyPassReverse / http://www.public_sonar.com/
  ErrorLog logs/somecompany/sonar/error.log
  CustomLog logs/somecompany/sonar/access.log common
</VirtualHost>
```

### Using F5 proxy <a href="#using-f5-proxy" id="using-f5-proxy"></a>

Use an iRule to insert the original client IP address in an `X-Forwarded-For` HTTP header (see also [F5 documentation](https://my.f5.com/manage/s/article/K4816#2)) as illustrated below.

```css-79elbk
when HTTP_REQUEST {
    HTTP::header insert X-Forwarded-For [IP::remote_addr]
    HTTP::header insert X-Forwarded-Proto "https"
}
```

### Using HAproxy <a href="#using-haproxy" id="using-haproxy"></a>

The example below shows the configuration of an HAproxy for a Data Center Edition (load balancer and reverse proxy at the same time).

```css-79elbk
frontend http-in
    bind *:80
    bind *:443 ssl crt /etc/ssl/private/<server_certificate>
    http-request redirect scheme https unless { ssl_fc }
    default_backend sonarqube_server
backend sonarqube_server
    balance roundrobin
    http-request set-header X-Forwarded-Proto https
    option httpchk GET /api/system/status
    http-check expect rstring UP|DB_MIGRATION_NEEDED|DB_MIGRATION_RUNNING
    default-server check maxconn 200
    server node1 <server_endpoint_1>
    server node2 <server_endpoint_2> 
```

### Using IIS on Windows <a href="#using-iis-on-windows" id="using-iis-on-windows"></a>

Using IIS on Windows, you can create a website that acts as a reverse proxy and access your SonarQube instance over SSL.

#### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

<details>

<summary>ISS enabled</summary>

Internet Information Services (IIS) must be enabled with the following extensions:

* The [Url Rewrite extension for IIS](https://www.iis.net/downloads/microsoft/url-rewrite)
* The [Application Based Routing extension for IIS](https://www.iis.net/downloads/microsoft/application-request-routing)

{% hint style="info" %}
To make sure the extensions are enabled, restart your IIS Manager after you install them.
{% endhint %}

In the example used below, IIS is enabled on the same machine as the SonarQube instance.

</details>

<details>

<summary>SSL certificate</summary>

You must provide a [self-signed SSL certificate, or a real one](https://learn.microsoft.com/en-us/iis/manage/configuring-security/how-to-set-up-ssl-on-iis#obtain-a-certificate) and import it (see [manage-tls-certificates](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/scanner-environment/manage-tls-certificates "mention")) to the Java truststore of the machine running the scanner.

</details>

<details>

<summary>Microsoft limit on HTTP requests</summary>

To accommodate potentially long query strings with the SonarQube web API, you can increase the Microsoft limit on HTTP requests by setting the following attributes to much larger values:

* `maxQueryString` (default is 2048) on `system.webServer`
* `maxQueryStringLength` on `system.web`

If you don’t, request filtering (`requestFiltering`) will be applied which can yield HTTP 404 errors. For example, this may cause projects to not appear on the projects dashboard.

To adjust both `maxQueryString` on `system.webServer` and `maxQueryStringLength` on `system.web`, add the following to your Microsoft’s `web.config` file for the associated IIS site using the Configuration Editor:

```css-79elbk
<system.webServer>
  <security>
    <requestFiltering>
      <requestLimits maxQueryString="32768"/>
    </requestFiltering>
  </security>
</system.webServer>
<system.web>
    <httpRuntime maxQueryStringLength="32768" maxUrlLength="65536"/>
</system.web>
```

See [Request Limits \<requestLimits> | Microsoft Learn](https://learn.microsoft.com/en-us/iis/configuration/system.webServer/security/requestFiltering/requestLimits/) for more information.

</details>

#### Step 1: Create an IIS website <a href="#step-1-create-an-iis-website" id="step-1-create-an-iis-website"></a>

1. In the IIS Manager, select *Your machine* > **Sites** > **Add Website…**
2. Under Site name, enter a name for your website.
3. Under **Content Directory** > **Physical path**, select a physical path for your website’s folder. Based on the default IIS website, we recommend creating a `%SystemDrive%\inetpub\wwwroot_sonarqube` folder and using it as a physical path.
4. In Binding, select **Type** > **https**.
5. For Host name, enter the hostname you will use to access SonarQube.
6. Under SSL certificate, select an SSL certificate.
7. Click **OK**.

#### Step 2: Configure your IIS website as a reverse proxy <a href="#step-2-configure-your-iis-website-as-a-reverse-proxy" id="step-2-configure-your-iis-website-as-a-reverse-proxy"></a>

Once you’ve created your website using the IIS Manager, you can use the URL Rewrite extension to use that website as a reverse proxy:

1. From the IIS Manager home page, select your website and open **URL Rewrite**.
2. Click **Add Rule(s)** to create a new rule.
3. Select **Reverse Proxy** from the list of templates.
4. Enter the destination server URL. It can be `localhost:9000` or a remote server.
5. Click **OK** to create the rule. The URL Rewrite page now displays a reverse proxy inbound rule.

#### Step 3: Add the HTTP\_X\_FORWARDED\_PROTO server variable <a href="#step-3-add-the-httpxforwardedproto-server-variable" id="step-3-add-the-httpxforwardedproto-server-variable"></a>

Using the URL Rewrite module, you can create a server variable to handle the `HTTP_X_FORWARDED_PROTO` header and pass it to SonarQube.

From the URL Rewrite page:

1. Click **View Server Variables**. This opens the **Allowed Server Variables** page.
2. To add a server variable, click **Add…**, enter **HTTP\_X\_FORWARDED\_PROTO** in the field and click **OK**. The server variable is now displayed on the **Allowed Server Variables** page.
3. Click **Back to Rules** to go to the **URL Rewrite rules list**.
4. Select the reverse proxy inbound rule for your website. Under **Inbound Rules**, click **Edit**.
5. Expand the **Server variables** section of the rule definition.
6. Add the **HTTP\_X\_FORWARDED\_PROTO** server variable and give it the value **https**.
7. Apply the changes.

SonarQube can now be accessed over SSL.

#### Step 4: If SAML authentication is used <a href="#step-4-if-saml-authentication-is-used" id="step-4-if-saml-authentication-is-used"></a>

For SAML through IIS, you must perform the following additional steps:

1. Make sure the host headers are preserved. This is set at the IIS server level, by executing the following command:

```sh
 %windir%\system32\inetsrv\appcmd.exe set config -section:system.webServer/proxy -preserveHostHeader:true /commit:apphost
```

You should then see an output that says something like:\
Applied configuration changes to section "system.webServer/proxy" for "MACHINE/WEBROOT/APPHOST" at configuration commit path "MACHINE/WEBROOT/APPHOST"

2. Disable the Reverse rewrite host in the response headers as follows:
   1. At the server level in IIS, go to **Application Request Routing** > **Server proxy settings**.
   2. Uncheck the box **Reverse rewrite host in response headers**.
   3. Apply the change.
   4. Restart IIS.

#### Step 5: Check that the connection is enabled <a href="#step-5-check-that-the-connection-is-enabled" id="step-5-check-that-the-connection-is-enabled"></a>

With your SonarQube instance and your IIS website running, open the IIS Manager and click the link under *Your website* > **Browse Website** > **Browse**, or enter the website’s URL in a browser. You should see the login or home page of your SonarQube instance.

#### Step 6: Additional optional configuration <a href="#step-6-additional-optional-configuration" id="step-6-additional-optional-configuration"></a>

You can configure your SonarQube instance to only accept traffic from your reverse proxy, by setting the `sonar.web.host` system property to `127.0.0.1`.

Another option is to use the Windows Firewall to only accept traffic from localhost.

For information about system properties setup, see [configuration-methods](https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties/configuration-methods "mention").

### Related pages <a href="#related-pages" id="related-pages"></a>

* [network-rules](https://docs.sonarsource.com/sonarqube-server/server-installation/network-security/network-rules "mention") (Developer and Enterprise editions)
* [network-rules](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/network-security/network-rules "mention") (Data Center Edition)
