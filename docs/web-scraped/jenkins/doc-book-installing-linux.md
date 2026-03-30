# Source: https://www.jenkins.io/doc/book/installing/linux/

Title: Linux

URL Source: https://www.jenkins.io/doc/book/installing/linux/

Markdown Content:
Table of Contents

*   [Prerequisites](https://www.jenkins.io/doc/book/installing/linux/#prerequisites)
*   [Debian/Ubuntu](https://www.jenkins.io/doc/book/installing/linux/#debianubuntu)
    *   [Installation of Java](https://www.jenkins.io/doc/book/installing/linux/#debian-java)
    *   [Long Term Support release](https://www.jenkins.io/doc/book/installing/linux/#debian-stable)
    *   [Weekly release](https://www.jenkins.io/doc/book/installing/linux/#debian-weekly)

*   [Fedora](https://www.jenkins.io/doc/book/installing/linux/#fedora)
    *   [Long Term Support release](https://www.jenkins.io/doc/book/installing/linux/#fedora-stable)
    *   [Weekly release](https://www.jenkins.io/doc/book/installing/linux/#fedora-weekly)
    *   [Start Jenkins](https://www.jenkins.io/doc/book/installing/linux/#start-jenkins)

*   [Red Hat Enterprise Linux and derivatives](https://www.jenkins.io/doc/book/installing/linux/#red-hat-centos)
    *   [Long Term Support release](https://www.jenkins.io/doc/book/installing/linux/#red-hat-stable)
    *   [Weekly release](https://www.jenkins.io/doc/book/installing/linux/#red-hat-weekly)
    *   [Start Jenkins](https://www.jenkins.io/doc/book/installing/linux/#start-jenkins-2)

*   [Post-installation setup wizard](https://www.jenkins.io/doc/book/installing/linux/#setup-wizard)
    *   [Unlocking Jenkins](https://www.jenkins.io/doc/book/installing/linux/#unlocking-jenkins)
    *   [Customizing Jenkins with plugins](https://www.jenkins.io/doc/book/installing/linux/#customizing-jenkins-with-plugins)
    *   [Creating the first administrator user](https://www.jenkins.io/doc/book/installing/linux/#creating-the-first-administrator-user)

Jenkins installers are available for several Linux distributions.

*   [Debian/Ubuntu](https://www.jenkins.io/doc/book/installing/linux/#debianubuntu)

*   [Fedora](https://www.jenkins.io/doc/book/installing/linux/#fedora)

*   [Red Hat Enterprise Linux and derivatives](https://www.jenkins.io/doc/book/installing/linux/#red-hat-centos)

[](https://www.jenkins.io/doc/book/installing/linux/#debianubuntu)Debian/Ubuntu[](https://www.jenkins.io/doc/book/installing/linux/#debianubuntu)
-------------------------------------------------------------------------------------------------------------------------------------------------

On Debian and Debian-based distributions like Ubuntu, you can install Jenkins through `apt`.

How to Install Jenkins on Ubuntu 24.04

You need to choose either the Jenkins Long Term Support release or the Jenkins weekly release.

### [](https://www.jenkins.io/doc/book/installing/linux/#debian-java)Installation of Java[](https://www.jenkins.io/doc/book/installing/linux/#debian-java)

Jenkins requires Java to run, yet not all Linux distributions include Java by default. Additionally, [not all Java versions are compatible](https://www.jenkins.io/doc/book/platform-information/support-policy-java/) with Jenkins.

There are multiple Java implementations that you can use. [OpenJDK](https://openjdk.java.net/) is the most popular one at the moment, we will use it in this guide.

Update the Debian apt repositories, install OpenJDK 21, and check the installation using the following commands:

```
sudo apt update
sudo apt install fontconfig openjdk-21-jre
java -version
```

bash

If the installation was successful, you should see an output similar to the following:

```
openjdk 21.0.8 2025-07-15
OpenJDK Runtime Environment (build 21.0.8+9-Debian-1)
OpenJDK 64-Bit Server VM (build 21.0.8+9-Debian-1, mixed mode, sharing)
```

bash

On Debian/Ubuntu, it is strongly recommended to install Java **before** Jenkins. If Jenkins is installed first and Java is added later, the Jenkins service may fail to start with:

`jenkins: failed to find a valid Java installation`
bash

Installing Java first ensures the environment is fully initialized and avoids this issue. After completing the Java installation, continue with the Jenkins installation steps below.

### [](https://www.jenkins.io/doc/book/installing/linux/#debian-stable)Long Term Support release[](https://www.jenkins.io/doc/book/installing/linux/#debian-stable)

```
sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2026.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update
sudo apt install jenkins
```

bash

### [](https://www.jenkins.io/doc/book/installing/linux/#debian-weekly)Weekly release[](https://www.jenkins.io/doc/book/installing/linux/#debian-weekly)

A new release is produced weekly to deliver bug fixes and features to users and plugin developers. It can be installed from the [`debian` apt repository](https://pkg.jenkins.io/debian/).

```
sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian/jenkins.io-2026.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update
sudo apt install jenkins
```

bash

Beginning with Jenkins 2.335 and Jenkins 2.332.1, the package is configured with `systemd` rather than the older System V `init`. More information is available in ["Managing systemd services"](https://www.jenkins.io/doc/book/system-administration/systemd-services/).

The package installation will:

*   Setup Jenkins as a daemon launched on start. Run `systemctl cat jenkins` for more details.

*   Create a ‘jenkins’ user to run this service.

*   Direct console log output to `systemd-journald`. Run `journalctl -u jenkins.service` if you are troubleshooting Jenkins.

*   Populate `/lib/systemd/system/jenkins.service` with configuration parameters for the launch, e.g `JENKINS_HOME`

*   Set Jenkins to listen on port 8080. Access this port with your browser to start configuration.

If Jenkins fails to start because a port is in use, run `systemctl edit jenkins` and add the following:

```
[Service]
Environment="JENKINS_PORT=8081"
```

Here, "8081" was chosen but you can put another port available.

Why use `apt` and not `apt-get` or another command? The apt command has been available since 2014. It has a command structure that is similar to `apt-get` but was created to be a more pleasant experience for typical users. Simple software management tasks like install, search and remove are easier with `apt`.

[](https://www.jenkins.io/doc/book/installing/linux/#fedora)Fedora[](https://www.jenkins.io/doc/book/installing/linux/#fedora)
------------------------------------------------------------------------------------------------------------------------------

You can install Jenkins through `dnf`. You need to add the Jenkins repository from the Jenkins website to the package manager first.

### [](https://www.jenkins.io/doc/book/installing/linux/#fedora-stable)Long Term Support release[](https://www.jenkins.io/doc/book/installing/linux/#fedora-stable)

A [LTS (Long-Term Support) release](https://www.jenkins.io/download/lts/) is chosen every 12 weeks from the stream of regular releases as the stable release for that time period. It can be installed from the [`rpm-stable`](https://pkg.jenkins.io/rpm-stable/) yum repository.

```
sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/rpm-stable/jenkins.repo
sudo dnf upgrade
# Add required dependencies for the Jenkins package
sudo dnf install fontconfig java-21-openjdk
sudo dnf install jenkins
sudo systemctl daemon-reload
```

bash

### [](https://www.jenkins.io/doc/book/installing/linux/#fedora-weekly)Weekly release[](https://www.jenkins.io/doc/book/installing/linux/#fedora-weekly)

A new release is produced weekly to deliver bug fixes and features to users and plugin developers. It can be installed from the [`rpm`](https://pkg.jenkins.io/rpm/) yum repository.

```
sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/rpm/jenkins.repo
sudo dnf upgrade
# Add required dependencies for the jenkins package
sudo dnf install fontconfig java-21-openjdk
sudo dnf install jenkins
```

bash

### [](https://www.jenkins.io/doc/book/installing/linux/#start-jenkins)Start Jenkins[](https://www.jenkins.io/doc/book/installing/linux/#start-jenkins)

You can enable the Jenkins service to start at boot with the command:

`sudo systemctl enable jenkins`
bash

You can start the Jenkins service with the command:

`sudo systemctl start jenkins`
bash

You can check the status of the Jenkins service using the command:

`sudo systemctl status jenkins`
bash

If everything has been set up correctly, you should see output similar to this:

```
Loaded: loaded (/lib/systemd/system/jenkins.service; enabled; vendor preset: enabled)
Active: active (running) since Tue 2018-11-13 16:19:01 +03; 4min 57s ago
```

bash

If you have a firewall installed, you must add Jenkins as an exception. You must change `YOURPORT` in the script below to the port you want to use. Port `8080` is the most common.

```
YOURPORT=8080
PERM="--permanent"
SERV="$PERM --service=jenkins"

firewall-cmd $PERM --new-service=jenkins
firewall-cmd $SERV --set-short="Jenkins ports"
firewall-cmd $SERV --set-description="Jenkins port exceptions"
firewall-cmd $SERV --add-port=$YOURPORT/tcp
firewall-cmd $PERM --add-service=jenkins
firewall-cmd --zone=public --add-service=http --permanent
firewall-cmd --reload
```

bash

[](https://www.jenkins.io/doc/book/installing/linux/#red-hat-centos)Red Hat Enterprise Linux and derivatives[](https://www.jenkins.io/doc/book/installing/linux/#red-hat-centos)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can install Jenkins through `yum` on Red Hat Enterprise Linux, AlmaLinux, Rocky Linux, Oracle Linux, CentOS, and other Red Hat based distributions.

How To Install Jenkins on Rocky Linux 9

You need to choose either the Jenkins Long Term Support release or the Jenkins weekly release.

### [](https://www.jenkins.io/doc/book/installing/linux/#red-hat-stable)Long Term Support release[](https://www.jenkins.io/doc/book/installing/linux/#red-hat-stable)

A [LTS (Long-Term Support) release](https://www.jenkins.io/download/lts/) is chosen every 12 weeks from the stream of regular releases as the stable release for that time period. It can be installed from the [`rpm-stable`](https://pkg.jenkins.io/rpm-stable/) yum repository.

```
sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/rpm-stable/jenkins.repo
sudo yum upgrade
# Add required dependencies for the jenkins package
sudo yum install fontconfig java-21-openjdk
sudo yum install jenkins
sudo systemctl daemon-reload
```

bash

### [](https://www.jenkins.io/doc/book/installing/linux/#red-hat-weekly)Weekly release[](https://www.jenkins.io/doc/book/installing/linux/#red-hat-weekly)

A new release is produced weekly to deliver bug fixes and features to users and plugin developers. It can be installed from the [`rpm`](https://pkg.jenkins.io/rpm/) yum repository.

```
sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/rpm/jenkins.repo
sudo yum upgrade
# Add required dependencies for the jenkins package
sudo yum install fontconfig java-21-openjdk
sudo yum install jenkins
```

bash

### [](https://www.jenkins.io/doc/book/installing/linux/#start-jenkins-2)Start Jenkins[](https://www.jenkins.io/doc/book/installing/linux/#start-jenkins-2)

You can enable the Jenkins service to start at boot with the command:

`sudo systemctl enable jenkins`
bash

You can start the Jenkins service with the command:

`sudo systemctl start jenkins`
bash

You can check the status of the Jenkins service using the command:

`sudo systemctl status jenkins`
bash

If everything has been set up correctly, you should see an output like this:

```
Loaded: loaded (/lib/systemd/system/jenkins.service; enabled; vendor preset: enabled)
Active: active (running) since Tue 2023-06-22 16:19:01 +03; 4min 57s ago
...
```

bash

If you have a firewall installed, you must add Jenkins as an exception. You must change `YOURPORT` in the script below to the port you want to use. Port `8080` is the most common.

```
YOURPORT=8080
PERM="--permanent"
SERV="$PERM --service=jenkins"

firewall-cmd $PERM --new-service=jenkins
firewall-cmd $SERV --set-short="Jenkins ports"
firewall-cmd $SERV --set-description="Jenkins port exceptions"
firewall-cmd $SERV --add-port=$YOURPORT/tcp
firewall-cmd $PERM --add-service=jenkins
firewall-cmd --zone=public --add-service=http --permanent
firewall-cmd --reload
```

bash

[](https://www.jenkins.io/doc/book/installing/linux/#setup-wizard)Post-installation setup wizard[](https://www.jenkins.io/doc/book/installing/linux/#setup-wizard)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

After downloading, installing, and running Jenkins using one of the procedures above (except when installing with the Jenkins Operator), the post-installation setup wizard begins.

The setup wizard takes you through a few quick one-time steps to unlock Jenkins, customize it with plugins, and create the first administrator user through which you can continue accessing Jenkins.

### [](https://www.jenkins.io/doc/book/installing/linux/#unlocking-jenkins)Unlocking Jenkins[](https://www.jenkins.io/doc/book/installing/linux/#unlocking-jenkins)

When you first access a new Jenkins controller, you are asked to unlock it using an automatically-generated password.

1.   Browse to `http://localhost:8080` (or whichever port you configured for Jenkins when installing it) and wait until the **Unlock Jenkins** page appears.

![Image 1: Unlock Jenkins page](https://www.jenkins.io/doc/book/resources/tutorials/setup-jenkins-01-unlock-jenkins-page.jpg)

2.   From the Jenkins console log output, copy the automatically generated alphanumeric password (between the 2 sets of asterisks).

![Image 2: Copying initial admin password](https://www.jenkins.io/doc/book/resources/tutorials/setup-jenkins-02-copying-initial-admin-password.png)

**Note:**

    *   The command: `sudo cat /var/lib/jenkins/secrets/initialAdminPassword` will print the password at console.

    *   If you are running Jenkins in Docker using the official `jenkins/jenkins` image you can use `sudo docker exec ${CONTAINER_ID or CONTAINER_NAME} cat /var/jenkins_home/secrets/initialAdminPassword` to print the password in the console without having to open an interactive shell inside the container.

3.   On the **Unlock Jenkins** page, paste this password into the **Administrator password** field and click **Continue**.

**Note:**

    *   The Jenkins console log indicates the location (in the Jenkins home directory) where this password can also be obtained. This password must be entered in the setup wizard on new Jenkins installations before you can access Jenkins’s main UI. This password also serves as the default administrator account’s password (with username "admin") if you happen to skip the subsequent user-creation step in the setup wizard.

### [](https://www.jenkins.io/doc/book/installing/linux/#customizing-jenkins-with-plugins)Customizing Jenkins with plugins[](https://www.jenkins.io/doc/book/installing/linux/#customizing-jenkins-with-plugins)

After [unlocking Jenkins](https://www.jenkins.io/doc/book/installing/linux/#unlocking-jenkins), the **Customize Jenkins** page appears. Here you can install any number of useful plugins as part of your initial setup.

Click one of the two options shown:

*   **Install suggested plugins** - to install the recommended set of plugins, which are based on most common use cases.

*   **Select plugins to install** - to choose which set of plugins to initially install. When you first access the plugin selection page, the suggested plugins are selected by default.

If you are not sure what plugins you need, choose **Install suggested plugins**. You can install or remove additional Jenkins plugins later via the [**Manage Jenkins**](https://www.jenkins.io/doc/book/managing)>[**Plugins**](https://www.jenkins.io/doc/book/managing/plugins/) page in Jenkins.

The setup wizard shows the progression of Jenkins being configured and your chosen set of Jenkins plugins being installed. This process may take a few minutes to complete.

### [](https://www.jenkins.io/doc/book/installing/linux/#creating-the-first-administrator-user)Creating the first administrator user[](https://www.jenkins.io/doc/book/installing/linux/#creating-the-first-administrator-user)

Finally, after [customizing Jenkins with plugins](https://www.jenkins.io/doc/book/installing/linux/#customizing-jenkins-with-plugins), Jenkins asks you to create your first administrator user.

1.   When the **Create First Admin User** page appears, specify the details for your administrator user in the respective fields and click **Save and Finish**.

2.   When the **Jenkins is ready** page appears, click **Start using Jenkins**.

**Notes:**

    *   This page may display **Jenkins is almost ready!** instead and if so, click **Restart**.

    *   If the page does not automatically refresh after a minute, use your web browser to refresh the page manually.

3.   If required, log in to Jenkins using the credentials of the user you just created and you are ready to start using Jenkins!

Please submit your feedback about this page through this [quick form](https://www.jenkins.io/doc/feedback-form/).

Alternatively, if you don't wish to complete the quick form, you can simply indicate if you found this page helpful?

See existing feedback [here](https://docs.google.com/spreadsheets/d/1IIdpVs39JDYKg0sLQIv-MNO928qcGApAIfdW5ohfD78).
