# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/from-zip-file/starting-stopping-server/running-as-a-service.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/from-zip-file/starting-stopping-server/running-as-a-service.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/from-zip-file/starting-stopping-server/running-as-a-service.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/from-zip-file/starting-stopping-server/running-as-a-service.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/from-zip-file/starting-stopping-server/running-as-a-service.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/from-zip-file/starting-stopping-server/running-as-a-service.md

# Running as a service

### On Windows <a href="#on-windows" id="on-windows"></a>

#### Installing or uninstalling SonarQube as a service <a href="#installing-or-uninstalling-sonarqube-as-a-service" id="installing-or-uninstalling-sonarqube-as-a-service"></a>

```css-79elbk
> <sonarqubeHome>\bin\windows-x86-64\SonarService.bat install
> <sonarqubeHome>\bin\windows-x86-64\SonarService.bat uninstall
```

#### Starting the service <a href="#starting-the-service" id="starting-the-service"></a>

```css-79elbk
> <sonarqubeHome>\bin\windows-x86-64\SonarService.bat start
```

{% hint style="info" %}
By default, the service will use the Java executable available on the Windows PATH. This setting can be changed by setting the environmental variable `SONAR_JAVA_PATH`. See more in [advanced-setup](https://docs.sonarsource.com/sonarqube-server/server-installation/from-zip-file/advanced-setup "mention").
{% endhint %}

#### Stopping the service <a href="#stopping-the-service" id="stopping-the-service"></a>

```css-79elbk
> <sonarqubeHome>\bin\windows-x86-64\SonarService.bat stop
```

{% hint style="info" %}
This command does a graceful shutdown where no new analysis report processing can start, but the tasks in progress are allowed to finish. The time a stop will take depends on the processing time of the tasks in progress. You’ll need to end all SonarQube Server processes manually to force a stop.
{% endhint %}

#### Checking the service status <a href="#checking-the-service-status" id="checking-the-service-status"></a>

To check if the SonarQube service is running:

```css-79elbk
> <sonarqubeHome>\bin\windows-x86-64\SonarService.bat status
```

### On Linux with systemd <a href="#on-linux-with-systemd" id="on-linux-with-systemd"></a>

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

* Because the sonar-application jar name ends with the version of SonarQube, you will need to adjust the `ExecStart` command accordingly on install and at each upgrade.
* All SonarQube directories should be owned by the `sonarqube` user.
* If you have multiple Java versions, you will need to modify the `java` path in the `ExecStart` command. This also means `SONAR_JAVA_PATH` will not work with SonarQube as a service.
  {% endhint %}

Once your `sonarqube.service` file is created and properly configured, run:

```css-79elbk
sudo systemctl enable sonarqube.service
sudo systemctl start sonarqube.service
```

### On Linux with initd <a href="#on-linux-with-initd" id="on-linux-with-initd"></a>

The following has been tested on Ubuntu 20.04 and CentOS 6.2.

You cannot run SonarQube as `root` in \*nix systems. Ideally, you will have created a new account dedicated to the purpose of running SonarQube. Let’s suppose the user used to start the service is `sonarqube`. Then create the file`/etc/init.d/sonar` *based on* the following:

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

Register SonarQube at boot time (RedHat, CentOS, 64 bit):

```css-79elbk
sudo ln -s <sonarqubeHome>/bin/linux-x86-64/sonar.sh /usr/bin/sonar
sudo chmod 755 /etc/init.d/sonar
sudo chkconfig --add sonar
```

Register SonarQube at boot time (Ubuntu, 64 bit):

```css-79elbk
sudo ln -s <sonarqubeHome>/bin/linux-x86-64/sonar.sh /usr/bin/sonar
sudo chmod 755 /etc/init.d/sonar
sudo update-rc.d sonar defaults
```

Once registration is done, run:

```css-79elbk
sudo service sonar start
```
