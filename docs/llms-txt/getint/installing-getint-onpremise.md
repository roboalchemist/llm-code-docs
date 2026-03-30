# Source: https://docs.getint.io/getting-started-with-the-platform/deployment-options/on-premise-deployment/installing-getint-onpremise.md

# Installation

For those looking for enhanced performance, superior workflow management, efficient operations, and robust data security, On-Premise emerges as an exceptional solution. You’re in control of your data during any changes or updates, and it all happens within your custom server. This ensures that there are no other requests, except for the applications you are integrating. Thus, On-Premise offers a compelling blend of power and privacy.

### How to Install On-Premise <a href="#how-to-install-on-premise" id="how-to-install-on-premise"></a>

This detailed guide will cover all the necessary steps to install [getint.io](http://getint.io/) in your dedicated network.

#### Installation requirements <a href="#installation-requirements" id="installation-requirements"></a>

* Ubuntu / Debian / Redhat / Windows server / Docker - Server requirements
* **Root user** access
* Your Getint binary and License files. If you do not have them, please get in touch with us at [**support@getint.io**](mailto:support@getint.io)

#### Server requirements <a href="#server-requirements" id="server-requirements"></a>

| Minimum   | Recommended |
| --------- | ----------- |
| 2GB Ram   | 4GB Ram     |
| 1 vCPU    | 2 vCPU      |
| 60 GB HDD | 60 GB SSD   |

#### Installation steps <a href="#installation-steps" id="installation-steps"></a>

1. **Open your terminal and sign in to the machine as a root user.**
   * Use the SSH command and replace `youripaddress` with the hostname or IP address of the server:

| ssh root\@youripaddress |
| ----------------------- |

1. **Enter your password:**
   * You’ll be prompted to enter your password for the specified username
2. **Download Getint files:**
   * Getint will provide these. Use the command `wget` + the link to the files to download the installation package
   * Use the command `ls -al` to see the files in the current directory, and ensure the zip files are located there
3. **Extract the files**
   * Use the `unzip` command to extract Getint files in the directory. For instance, it should be like this: `unzip getint-1.58.zip`
   * Run `apt install unzip` to download an unzip tool if you don’t have one
4. **Switch to the Getint directory**
   * After the installation, switch the directory to the new Getint folder by running `cd getint`
   * Now enter `cd synchronizer` to open the Getint installation folder
5. **Make sure you have the necessary tools to run Getint**
   * Install Java if it isn’t available on your machine. Enter the command `apt install default-jre` and press **Y** then **Enter** when prompted. Press **ctrl + c** to return to the directory.
   * Make sure Java is now installed with the command `java --version`

{% hint style="warning" %}
Please note that we support Java versions 8 through 17.
{% endhint %}

1. **Running Getint**

* Use the command `./manager.sh start` to launch Getint. Press **ctrl + c** to close the logs and return to the directory
* Check if Getint is up and running in the background by using the command `ps -aux | grep getint`

1. **Accessing Getint**

* These are the credentials you can use to log into Getint via your browser:
  * Username: admin
  * Password: admin
* Open the browser and type the URL which is the machine’s IP address. Alternatively, if you have any domain name assigned to the machine on which Getint is installed, you can type that domain name
* Other commands you can use to manage your instance:
  * `./manager.sh stop` stops the integration, so you won’t be able to access it until you start it again
  * `./manager.sh restart` restarts the integration in case you have made some changes to the directory

Getint will start on port 80 by default. If port 80 is already in use, change it with the command `vim getint.env`

After switching ports, use the command `cat getint.env` to see the current port in use.

#### Video tutorial <a href="#video-tutorial" id="video-tutorial"></a>

Here’s a video tutorial that demonstrates how to install the On-Premise version.

{% embed url="<https://www.loom.com/share/8f018d0128fc45178d5b27346cba707a?sid=fd9f751c-6a9e-423f-bb11-b343c1293cbe>" %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvfdnR8QBDNRNmvHoH6lW%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=72cfc2d7-2f26-47ec-9eb6-1bdeacaf470f" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>

### **Docker - Docker-compose installation** <a href="#docker-docker-compose-installation" id="docker-docker-compose-installation"></a>

The initial steps are similar to installing Getint on your dedicated machine, but they have remarkable differences in how the app is installed and fully executed. Ultimately, it will depend on your server requirements.

As Docker is a separate tool, please ensure it is installed on your machine before running Getint. Otherwise, Getint won’t start, and your terminal will pop up an error.

1. **Open your terminal and sign in to the machine as a root user.**
   * Use the SSH command and replace `youripaddress` with the hostname or IP address of the server:

| ssh root\@youripaddress |
| ----------------------- |

1. **Enter your password:**
   * You’ll be prompted to enter your password for the specified username
2. **Download Getint files:**
   * Getint will provide these. Use the command `wget` + the link to the files to download the installation package
   * Use the command `ls -al` to see the files in the current directory, and ensure the zip files are located there
3. **Extract the files**
   * Run `apt install unzip` to download an unzip tool if you don’t have one
   * Use the `unzip` command to extract Getint files in the directory. For instance, it should be like this: `unzip getint-1.58.zip`
4. **Switch to the Getint directory**
   * After the installation, switch the directory to the new Getint folder by running `cd getint`
   * Now enter `cd synchronizer` to open the Getint installation folder
   * Use the command `cd docker`, and then `cd scripts`
5. **Installing docker if it isn't installed on your machine**
   * The installation path will depend on the tool you’re using. For example, we’re using Ubuntu 20, and the installation package is available here: [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/). However, if you’re using a different distribution, click on **Docker Engine**, then click on **Install**, and locate your distribution under this page. After the installation, use the command `docker version` to ensure the tool is installed

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjGAYIVZuO28CfzCOpSWY%2F912ba1c97c369e7ccb5bee2071a62ca3.png?alt=media&#x26;token=f54729ab-db24-420a-bd66-3d980a98dc5b" alt=""><figcaption></figcaption></figure>

1. **Installing docker-compose on your machine**
   * It is also necessary to have docker-compose as our installation will consist of the PostgreSQL database, Nginx, and the Getint app. After the installation, use the command `docker-compose version` to ensure the tool is installed
   * Docker-compose standalone is available here: [Install Compose standalone](https://docs.docker.com/compose/install/standalone/)
2. **Running Getint**
   * While in the scripts folder, enter the command `sh start.sh` to launch Getint
   * Ensure Getint is running in the background by using the command `docker container ls`
3. **Accessing Getint**
   * These are the credentials you can use to log into Getint via your browser:
     * Username: admin
     * Password: admin
   * Open the browser and type the URL which is the machine’s IP address. Alternatively, if you have any domain name assigned to the machine on which Getint is installed, you can type that domain name
   * Other commands you can use to manage your instance:
     * `sh stop.sh`
     * `sh restart.sh`

Getint will start on port 80 by default. If port 80 is already in use, change it with the command `vim ../docker-compose.yaml`

After switching ports, use the command `docker container ls` to see the current port in use.

#### **Video tutorial** <a href="#video-tutorial.1" id="video-tutorial.1"></a>

Here’s a video tutorial on how to Install Getint in a docker.

{% embed url="<https://www.loom.com/share/4beb603104b245cbbaacef013032ac7d?sid=cc553c61-a37d-4839-b2be-329ab722ff2f}>" %}

{% hint style="info" %}
Our amazing team at Getint is always here to support you throughout your integration journey. We specialize in providing the best possible customer experience. If you have any questions about the setup process, please open a ticket with us at our [Help Center](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team).
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
