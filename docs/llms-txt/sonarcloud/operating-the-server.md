# Source: https://docs.sonarsource.com/sonarqube-server/8.9/setup-and-upgrade/configure-and-operate-a-server/operating-the-server.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/setup-and-upgrade/configure-and-operate-a-server/operating-the-server.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/setup-and-upgrade/configure-and-operate-a-server/operating-the-server.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/setup-and-upgrade/configure-and-operate-a-server/operating-the-server.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/setup-and-upgrade/configure-and-operate-a-server/operating-the-server.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/setup-and-upgrade/configure-and-operate-a-server/operating-the-server.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/configure-and-operate-a-server/operating-the-server.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/setup-and-upgrade/configure-and-operate-a-server/operating-the-server.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/configure-and-operate-a-server/operating-the-server.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/configure-and-operate-a-server/operating-the-server.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/operating-the-server.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/operating-the-server.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/operating-the-server.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/operating-the-server.md

# Operating the server

### Running SonarQube Server as a service on Windows <a href="#running-sonarqube-as-a-service-on-windows" id="running-sonarqube-as-a-service-on-windows"></a>

#### Install or uninstall SonarQube as a service <a href="#install-or-uninstall-sonarqube-as-a-service" id="install-or-uninstall-sonarqube-as-a-service"></a>

```css-79elbk
> <sonarqubeHome>\bin\windows-x86-64\SonarService.bat install
> <sonarqubeHome>\bin\windows-x86-64\SonarService.bat uninstall
```

#### Start or stop the service <a href="#start-or-stop-the-service" id="start-or-stop-the-service"></a>

```css-79elbk
> <sonarqubeHome>\bin\windows-x86-64\SonarService.bat start
```

{% hint style="info" %}
By default, the service will use the Java executable available on the Windows PATH. This setting can be changed by setting the environmental variable `SONAR_JAVA_PATH`. See more in [installing-sonarqube-from-zip-file](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/install-the-server/installing-sonarqube-from-zip-file "mention").
{% endhint %}

```css-79elbk
> <sonarqubeHome>\bin\windows-x86-64\SonarService.bat stop
```

{% hint style="info" %}
`> <sonarqubeHome>\bin\windows-x86-64\SonarService.bat stop` does a graceful shutdown where no new analysis report processing can start, but the tasks in progress are allowed to finish. The time a stop will take depends on the processing time of the tasks in progress. You’ll need to end all SonarQube Server processes manually to force a stop.
{% endhint %}

#### Service status <a href="#service-status" id="service-status"></a>

Check if the SonarQube service is running:

```css-79elbk
> <sonarqubeHome>\bin\windows-x86-64\SonarService.bat status
```

### Running SonarQube Server manually on Linux <a href="#running-sonarqube-manually-on-linux" id="running-sonarqube-manually-on-linux"></a>

#### Start or stop the instance <a href="#start-or-stop-the-instance" id="start-or-stop-the-instance"></a>

```sh
Start:
<sonarqubeHome>/bin/linux-x86-64/sonar.sh start

Graceful shutdown:
<sonarqubeHome>/bin/linux-x86-64/sonar.sh stop

Hard stop:
<sonarqubeHome>/bin/linux-x86-64/sonar.sh force-stop
```

{% hint style="info" %}
Stop does a graceful shutdown where no new analysis report processing can start, but the tasks in progress are allowed to finish. The time a stop will take depends on the processing time of the tasks in progress. Use force stop for a hard stop.
{% endhint %}

### Running SonarQube Server as a service on Linux with systemd <a href="#running-sonarqube-as-service-linux-systemd" id="running-sonarqube-as-service-linux-systemd"></a>

On a Unix system using systemd, you can install SonarQube as a service. You cannot run SonarQube as root in Unix systems. Ideally, you will have created a new account dedicated to the purpose of running SonarQube. Let’s suppose:

* The user used to start the service is `sonarqube`
* The group used to start the service is `sonarqube`
* The Java Virtual Machine is installed in `/opt/java/`
* SonarQube has been unzipped into `/opt/sonarqube/`

Then create the file `/etc/systemd/system/sonarqube.service` *based on* the following:

```css-79elbk
[Unit]
Description=SonarQube service
After=syslog.target network.target

[Service]
Type=simple
User=sonarqube
Group=sonarqube
PermissionsStartOnly=true
ExecStart=/bin/nohup /opt/java/bin/java -Xms32m -Xmx32m -Djava.net.preferIPv4Stack=true -jar /opt/sonarqube/lib/sonar-application-25.1.0.102122.jar
StandardOutput=journal
LimitNOFILE=131072
LimitNPROC=8192
TimeoutStartSec=5
Restart=always
SuccessExitStatus=143

[Install]
WantedBy=multi-user.target
```

{% hint style="info" %}

* Because the sonar-application jar name ends with the version of SonarQube Server, you will need to adjust the `ExecStart` command accordingly on install and at each upgrade.
* All SonarQube Server directories should be owned by the `sonarqube` user.
* If you have multiple Java versions, you will need to modify the `java` path in the `ExecStart` command. This also means `SONAR_JAVA_PATH` will not work with SonarQube Server as a service.
  {% endhint %}

Once your `sonarqube.service` file is created and properly configured, run:

```css-79elbk
sudo systemctl enable sonarqube.service
sudo systemctl start sonarqube.service
```

### Running SonarQube Server as a service on Linux with initd <a href="#running-sonarqube-as-service-linux-initd" id="running-sonarqube-as-service-linux-initd"></a>

The following has been tested on Ubuntu 20.04 and CentOS 6.2.

You cannot run SonarQube Server as `root` in \*nix systems. Ideally, you will have created a new account dedicated to the purpose of running SonarQube Server. Let’s suppose the user used to start the service is `sonarqube`. Then create the file`/etc/init.d/sonar` *based on* the following:

```css-79elbk
#!/bin/sh
#
# rc file for SonarQube
#
# chkconfig: 345 96 10
# description: SonarQube system (www.sonarsource.org)
#
### BEGIN INIT INFO
# Provides: sonar
# Required-Start: $network
# Required-Stop: $network
# Default-Start: 3 4 5
# Default-Stop: 0 1 2 6
# Short-Description: SonarQube system (www.sonarsource.org)
# Description: SonarQube system (www.sonarsource.org)
### END INIT INFO
 
su sonarqube -c "/usr/bin/sonar $*"
```

Register SonarQube Server at boot time (RedHat, CentOS, 64 bit):

```css-79elbk
sudo ln -s <sonarqubeHome>/bin/linux-x86-64/sonar.sh /usr/bin/sonar
sudo chmod 755 /etc/init.d/sonar
sudo chkconfig --add sonar
```

Register SonarQube Server at boot time (Ubuntu, 64 bit):

```css-79elbk
sudo ln -s <sonarqubeHome>/bin/linux-x86-64/sonar.sh /usr/bin/sonar
sudo chmod 755 /etc/init.d/sonar
sudo update-rc.d sonar defaults
```

Once registration is done, run:

```css-79elbk
sudo service sonar start
```

### Securing SonarQube Server behind a proxy <a href="#securing-the-server-behind-a-proxy" id="securing-the-server-behind-a-proxy"></a>

This section helps you configure SonarQube Server if you want to run it behind a proxy. This can be done for security concerns or to consolidate multiple disparate applications. To run SonarQube Server over HTTPS, see the HTTPS Configuration section below.

{% hint style="warning" %}
For security reasons, we recommend only giving external access to the main port.
{% endhint %}

#### Using an Apache Proxy <a href="#using-an-apache-proxy" id="using-an-apache-proxy"></a>

We assume that you’ve already installed Apache 2 with module mod\_proxy, that SonarQube Server is running and available on `http://private_sonar_host:sonar_port/`, and that you want to configure a Virtual Host for `www.public_sonar.com`.

At this point, edit the HTTPd configuration file for the `www.public_sonar.com` virtual host. Include the following to expose SonarQube Server via `mod_proxy` at `http://www.public_sonar.com/`

```css-79elbk
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

Apache configuration is going to vary based on your own application’s requirements and the way you intend to expose SonarQube Server to the outside world. If you need more details about Apache HTTPd and mod\_proxy, please see [https://httpd.apache.org](http://httpd.apache.org/).

#### Using Nginx <a href="#using-nginx" id="using-nginx"></a>

We assume that you’ve already installed Nginx, that you are using a Virtual Host for `www.somecompany.com` and that SonarQube Server is running and available on `http://sonarhost:sonarport/`.

At this point, edit the Nginx configuration file. Include the following to expose SonarQube Server at `http://www.somecompany.com/`:

```css-79elbk
# the server directive is Nginx's virtual host directive
server {
  # port to listen on. Can also be set to an IP:PORT
  listen 80;
  # sets the domain[s] that this vhost server requests for
  server_name www.somecompany.com;
  location / {
    proxy_pass http://sonarhost:sonarport;
  }
}
```

Nginx configuration will vary based on your own application’s requirements and the way you intend to expose SonarQube Server to the outside world. If you need more details about Nginx, please see <https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/>.

Note that you may need to increase the max URL length since SonarQube Server requests can have URLs longer than 2048.

#### Using IIS on Windows <a href="#using-iis-on-windows" id="using-iis-on-windows"></a>

Using IIS on Windows, you can create a website that acts as a reverse proxy and access your SonarQube Server instance over SSL.

{% hint style="warning" %}
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
{% endhint %}

**Prerequisites**

* Internet Information Services (IIS) enabled. In the following example, IIS is enabled on the same machine as the SonarQube instance.
* The [Url Rewrite extension for IIS](https://www.iis.net/downloads/microsoft/url-rewrite)
* The [Application Based Routing extension for IIS](https://www.iis.net/downloads/microsoft/application-request-routing)
* [A self-signed SSL certificate, or a real one](https://learn.microsoft.com/en-us/iis/manage/configuring-security/how-to-set-up-ssl-on-iis#obtain-a-certificate)\
  Note that you must import the certificate to the Java truststore of the machine running the scanner. See [manage-tls-certificates](https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/scanners/scanner-environment/manage-tls-certificates "mention").

{% hint style="info" %}
To make sure the extensions are enabled, restart your IIS Manager after you install them.
{% endhint %}

**Creating an IIS website**

1. In the IIS Manager, select *Your machine* > **Sites** > **Add Website…**
2. Under **Site name**, enter a name for your website.
3. Under **Content Directory** > **Physical path**, select a physical path for your website’s folder. Based on the default IIS website, we recommend creating a `%SystemDrive%\inetpub\wwwroot_sonarqube` folder and using it as a physical path.
4. In **Binding**, select **Type** > **https**.
5. For **Host name**, enter the hostname you will use to access SonarQube.
6. Under **SSL certificate**, select an SSL certificate.
7. Click **OK**.

**Using your IIS website as a reverse proxy**

Once you’ve created your website using the IIS Manager, you can use the URL Rewrite extension to use that website as a reverse proxy.

1. From the IIS Manager home page, select your website and open **URL Rewrite**.
2. Click **Add Rule(s)** to create a new rule.
3. Select **Reverse Proxy** from the list of templates.
4. Enter the destination server URL. It can be `localhost:9000` or a remote server.
5. Click **OK** to create the rule.

The URL Rewrite page now displays a reverse proxy inbound rule.

**Adding the HTTP\_X\_FORWARDED\_PROTO server variable**

Using the URL Rewrite module, you can create a server variable to handle the `HTTP_X_FORWARDED_PROTO` header and pass it to SonarQube. See the HTTPS Configuration section on this page for more information on that server variable.

From the URL Rewrite page:

1. Click **View Server Variables**. This opens the **Allowed Server Variables** page.
2. To add a server variable, click **Add…**, enter `HTTP_X_FORWARDED_PROTO` in the field and click **OK**. The server variable is now displayed on the **Allowed Server Variables** page.
3. Click **Back to Rules** to go to the URL Rewrite rules list.
4. Select the reverse proxy inbound rule for your website. Under **Inbound Rules**, click **Edit**.
5. Expand the **Server variables** section of the rule definition.
6. Add the `HTTP_X_FORWARDED_PROTO` server variable and give it the value **https**.
7. Apply the changes.

SonarQube can now be accessed over SSL.

**If SAML authentication is used**

For SAML through IIS, you must perform the following additional steps:

1. Make sure the host headers are preserved. This is set at the IIS server level, by executing the following command:\
   `%windir%\system32\inetsrv\appcmd.exe set config -section:system.webServer/proxy -preserveHostHeader:true /commit:apphost`\
   You should then see an output that says something like:\
   `Applied configuration changes to section "system.webServer/proxy" for "MACHINE/WEBROOT/APPHOST" at configuration commit path "MACHINE/WEBROOT/APPHOST"`
2. Disable the Reverse rewrite host in the response headers as follows:
   * At the server level in IIS, go to **Application Request Routing > Server proxy settings**.
   * Uncheck the box **Reverse rewrite host in response headers**.
   * Apply the change.
   * Restart IIS.

**Checking that the connection is enabled**

With your SonarQube instance and your IIS website running, open the IIS Manager and click the link under *Your website* > **Browse Website** > **Browse**, or enter the website’s URL in a browser. You should see the login or home page of your SonarQube instance.

**Next steps**

You can configure your SonarQube instance to only accept traffic from your reverse proxy, by adding the following line to the `sonar.properties` file:

`sonar.web.host=127.0.0.1`

Another option is to use the Windows Firewall to only accept traffic from localhost.

**Resources**

The setup described here is inspired by this [Configure SSL for SonarQube on Windows](https://jessehouwing.net/sonarqube-configure-ssl-on-windows/) blog post.

#### HTTPS configuration <a href="#https-configuration" id="https-configuration"></a>

```css-79elbk
# the server directive is Nginx's virtual host directive
server { 
 # port to listen on. Can also be set to an IP:PORT 
 listen 443 ssl;
 ssl_certificate ${path_to_your_certificate_file};
 ssl_certificate_key ${path_to_your_certificate_key_file};
 location / {
   proxy_pass ${address_of_your_sonarqube_instance_behind_proxy};
   proxy_set_header Host $host;
   proxy_set_header X-Forwarded-For $remote_addr;
   proxy_set_header X-Forwarded-Proto https;
 }
}
```

#### Forward SonarQube Server custom headers <a href="#forward-sonarqube-server-custom-headers" id="forward-sonarqube-server-custom-headers"></a>

SonarQube Server adds custom HTTP headers. The reverse proxy should be configured to forward the following headers:

* `SonarQube-Authentication-Token-Expiration`\
  This header is added to a web service response when using tokens to authenticate (see [managing-tokens](https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/managing-tokens "mention")). Forwarding this header is not required for the SonarQube Server features to work properly.
* `Sonar-MD5`\
  This header is used to verify the integrity of the plugins downloaded by the scanner. You must forward this header to successfully execute analyses that use plugins.

### Secure your network <a href="#secure-your-network" id="secure-your-network"></a>

To further lock down the communication in between the reverse proxy and SonarQube Server, you can define the following network rules:

|                                             |                  |                  |                     |             |
| ------------------------------------------- | ---------------- | ---------------- | ------------------- | ----------- |
| <p><strong>Protocol</strong></p><p><br></p> | **Source**       | **Destination**  | **Port**            | **default** |
| TCP                                         | Reverse Proxy    | SonarQube Server | `sonar.web.port`    | 9000        |
| TCP                                         | SonarQube Server | SonarQube Server | `sonar.search.port` | 9001        |
| TCP                                         | SonarQube Server | SonarQube Server | `sonar.es.port`     | random      |

You can further segment your network configuration if you specify a frontend network and keep Elasticsearch restricted to the loopback NiC.

|               |                     |                       |             |
| ------------- | ------------------- | --------------------- | ----------- |
| **Network**   | **Parameter**       | **Description**       | **default** |
| Frontend      | `sonar.web.host`    | Frontend HTTP Network | 0.0.0.0     |
| Elasticsearch | `sonar.search.host` | Elasticsearch Network | 127.0.0.1   |
