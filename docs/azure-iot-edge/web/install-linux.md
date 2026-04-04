# Source: https://learn.microsoft.com/en-us/azure/iot-edge/how-to-provision-single-device-linux-symmetric

Create IoT Edge device on Linux using symmetric keys - Azure IoT Edge | Microsoft Learn [Skip to main content ][Skip to Ask Learn chat experience ]
This browser is no longer supported. 

Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support. 
[Download Microsoft Edge ][More info about Internet Explorer and Microsoft Edge ]Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents [Read in English ]Add Add to plan [Edit ]
#### Share via 
[Facebook ][x.com ][LinkedIn ][Email ]Print 
Note 

Access to this page requires authorization. You can try [signing in ]or [changing directories ]. 

Access to this page requires authorization. You can try [changing directories ]. 

# Create and provision an IoT Edge device on Linux using symmetric keys 
Feedback Summarize this article for me 
## In this article 

**Applies to: **IoT Edge 1.5 

Important 

IoT Edge 1.5 LTS is the [supported release ]. IoT Edge 1.4 LTS is end of life as of November 12, 2024. If you are on an earlier release, see [Update IoT Edge ]. 

This article provides end-to-end instructions for registering and provisioning a Linux IoT Edge device that includes installing IoT Edge. 

Each device that connects to an [IoT hub ]has a device ID that's used to track [cloud-to-device ]or [device-to-cloud ]communications. You configure a device with its connection information, which includes: 

- IoT hub hostname 

- Device ID 

- Authentication details to connect to IoT Hub 

The steps in this article walk through a process called *manual provisioning *, where you connect a single device to its IoT hub. For manual provisioning, you have two options for authenticating IoT Edge devices: 

- 
**Symmetric keys **: When you create a new device identity in IoT Hub, the service creates two keys. You place one of the keys on the device, and it presents the key to IoT Hub when authenticating. 

This authentication method is faster to get started, but not as secure. 

- 
**X.509 self-signed **: You create two X.509 identity certificates and place them on the device. When you create a new device identity in IoT Hub, you provide thumbprints from both certificates. When the device authenticates to IoT Hub, it presents one certificate and IoT Hub verifies that the certificate matches its thumbprint. 

This authentication method is more secure and recommended for production scenarios. 

This article covers using symmetric keys as your authentication method. If you want to use X.509 certificates, see [Create and provision an IoT Edge device on Linux using X.509 certificates ]. 

Note 

If you have many devices to set up and don't want to manually provision each one, use one of the following articles to learn how IoT Edge works with the IoT Hub device provisioning service: 

- [Create and provision IoT Edge devices at scale on Linux using X.509 certificates ]

- [Create and provision IoT Edge devices at scale with a TPM on Linux ]

- [Create and provision IoT Edge devices at scale on Linux using symmetric keys ]

## Prerequisites 

This article shows how to register your IoT Edge device and install IoT Edge (also called IoT Edge runtime) on your device. Make sure you have the device management tool of your choice, for example Azure CLI, and device requirements before you register and install your device. 

### Device management tools 

You can use the **Azure portal **, **Visual Studio Code **, or **Azure CLI **for the steps to register your device. Each utility has its own prerequisites or might need to be installed: 

- [Portal ]

- [Visual Studio Code ]

- [Azure CLI ]

A free or standard [IoT hub ]in your Azure subscription. 

- A free or standard [IoT hub ]in your Azure subscription 

- [Visual Studio Code ]

- [Azure IoT Edge ]extension. The *Azure IoT Edge tools for Visual Studio Code *extension is in [maintenance mode ]. 

- [Azure IoT Hub ]extension 

- 
A free or standard [IoT hub ]in your Azure subscription 

- 
[Azure CLI ]in your environment 

At a minimum, your Azure CLI version must be 2.0.70 or newer. Use `az --version `to validate. This version supports `az `extension commands and introduces the Knack command framework. 

### Device requirements 

An X64, ARM32, or ARM64 Linux device. 

Microsoft publishes installation packages for various operating systems. 

For the latest information about which operating systems are currently supported for production scenarios, see [Azure IoT Edge supported platforms ]. 

### Visual Studio Code extensions 

If you're using Visual Studio Code, there are helpful Azure IoT extensions that make the device creation and management process easier. 

Install both the Azure IoT Edge and Azure IoT Hub extensions: 

- 
[Azure IoT Edge ]. The *Azure IoT Edge tools for Visual Studio Code *extension is in [maintenance mode ]. 

- 
[Azure IoT Hub ]

## Register your device 

You can use the **Azure portal **, **Visual Studio Code **, or **Azure CLI **to register your device, depending on your preference. 

- [Portal ]

- [Visual Studio Code ]

- [Azure CLI ]

In your IoT hub in the Azure portal, IoT Edge devices are created and managed separately from IoT devices that aren't edge enabled. 

- 
Sign in to the [Azure portal ]and navigate to your IoT hub. 

- 
In the left pane, select **Devices **from the menu, then select **Add Device **. 

- 
On the **Create a device **page, provide the following information: 

- Create a descriptive Device ID, for example `my-edge-device-1 `(all lowercase). Copy this Device ID, as you use it later. 

- Check the **IoT Edge Device **checkbox. 

- Select **Symmetric key **as the authentication type. 

- Use the default settings to autogenerate authentication keys, which connect the new device to your hub. 

- 
Select **Save **. 

You should see your new device listed in your IoT hub. 

### Sign in to Azure 

You can use the Azure IoT extensions for Visual Studio Code to perform operations with your IoT hub. Make sure you install the Azure IoT extension prerequisites. 

Once Azure IoT Edge and Azure IoT Hub extensions are installed, you notice an Azure icon gets added to the left icon menu. You can sign in to your Azure account through Visual Studio Code by selecting the Azure icon and then select **Sign in to Azure **. 

### Register a new device with Visual Studio Code 

Registering a new device is akin to creating an IoT Edge device in the Azure portal. This virtual device is one of the *twins *, whereas the real world device is the other twin. Visual Studio Code can set up this virtual device for you through the following steps. 

- In the Visual Studio Code Explorer menu, expand the **Azure IoT Hub **section. 

- Select on the **... **in the **Azure IoT Hub **section header. If you don't see the ellipsis, select or hover over the header. 

- Select **Create IoT Edge Device **. 

- In the text box that opens, give your device an ID, for example `my-edge-device-1 `(all lowercase), then press enter. 

In the output console of Visual Studio Code, you see the result of the command: a JSON printout. The device information includes the **deviceId **that you provided and generates a **connectionString **that you can use to connect your physical device to your IoT hub. The output console also shows your keys and other device identifying information. 

You can now see your device listed under the **Azure IoT Hub **> **Devices **section of the Explorer menu. 

Note 

If your device isn't listed, you might need to choose your IoT hub from the link **Select IoT Hub **provided under **Azure IoT Hub **and then follow the prompts. The prompts ask you to choose your subscription first and then your IoT hub. This process lets Visual Studio Code know about your IoT hub (and all devices in it). Refresh Visual Studio Code and your device should show. 

Use the [az iot hub device-identity create ]command to create a new device identity in your IoT hub. Replace `device_id_here `with your own new and unique device ID, for example `my-edge-device-1 `(all lowercase). Replace `hub_name_here `with your existing IoT hub. 

This command includes three parameters: 

- 
`--device-id `or `-d `: Provide a descriptive name that's unique within your IoT hub. 

- 
`--hub-name `or `-n `: Provide the name of your IoT hub. 

- 
`--edge-enabled `or `--ee `: Declare that the device is an IoT Edge device. 

```
`az iot hub device-identity create --device-id device_id_here --hub-name hub_name_here --edge-enabled `
```

If your CLI says **The command requires the extension azure-iot. Do you want to install it now? **, then type `Y `and press `Enter `to initiate the download to create your device. 

Now that you have a device registered in IoT Hub, you can retrieve provisioning information used to complete the installation and provisioning of the [IoT Edge runtime ]in the next step. 

## View registered devices and retrieve provisioning information 

Devices that use symmetric key authentication need their connection strings to complete installation and provisioning of the IoT Edge runtime. The connection string gets generated for your IoT Edge device when you create the device. For Visual Studio Code and Azure CLI, the connection string is in the JSON output. If you use the Azure portal to create your device, you can find the connection string from the device itself. When you select your device in your IoT hub, it's listed as `Primary connection string `on the device page. 

- [Portal ]

- [Visual Studio Code ]

- [Azure CLI ]

The edge-enabled devices that connect to your IoT hub are listed on the **Devices **page of your IoT hub. If you have multiple devices, you can filter the list by selecting the type **Iot Edge Devices **, then select **Apply **. 

When you're ready to set up your device, you need the connection string that links your physical device with its identity in the IoT hub. Devices that authenticate with symmetric keys have their connection strings available to copy in the portal. To find your connection string in the portal: 

- From the **Devices **page, select the IoT Edge device ID from the list. 

- Copy the value of either **Primary Connection String **or **Secondary Connection String **. Either key works. 

All the devices that connect to your IoT hub are listed in the **Azure IoT Hub **section of the Visual Studio Code Explorer. IoT Edge devices are distinguishable from non-Edge devices because they have a different icon and you see the **$edgeAgent **and **$edgeHub **modules are deployed to each IoT Edge device. 

When you're ready to set up your device, you need the connection string that links your physical device with its identity in the IoT hub. Here's how to get your connection string from Visual Studio Code. 

- 
Right-click on the ID (name) of your device in the **Azure IoT Hub **section. 

- 
Select **Copy Device Connection String **. 

The connection string is copied to your clipboard. 

You can also select **Get Device Info **from the right-click menu to see all the device info, including the connection string, in the output window. 

To see all devices in your IoT hub, use the [az iot hub device-identity list ]command. Replace `hub_name_here `with your own IoT hub name. 

```
`az iot hub device-identity list --hub-name hub_name_here `
```

Any device that is registered as an IoT Edge device has the property **capabilities.iotEdge **set to **true **. You see a lot of other metadata as JSON output as well, including your device IDs. 

When you're ready to set up your device, you need its connection string that links your physical device with its identity in the IoT hub. Use the following [az iot hub device-identity connection-string show ]command to return the connection string for a single device. Replace `[device_id] `and `[hub_name] `with your own values. The value for the `device-identity `parameter is case-sensitive. 

```
`az iot hub device-identity connection-string show --device-id [device_id] --hub-name [hub_name] `
```

You should see JSON output in the console, similar to the following example: 

```
`{
  "connectionString": "HostName=[hub_name].azure-devices.net;DeviceId=[device_id];SharedAccessKey=[device_key]"
} `
```

Tip 

The `connection-string show `command was introduced in version 0.9.8 of the Azure IoT extension, replacing the deprecated `show-connection-string `command. If you get an error running this command, make sure your extension version is updated to 0.9.8 or later. For more information and the latest updates, see [Microsoft Azure IoT extension for Azure CLI ]. 

When copying the connection string to use on a device, don't include the quotation marks around the connection string. 

## Install IoT Edge 

In this section, you prepare your Linux virtual machine or physical device for IoT Edge. Then, you install IoT Edge. 

Run the following commands to add the package repository and then add the Microsoft package signing key to your list of trusted keys. 

Important 

On June 30, 2022, Raspberry Pi OS Stretch was retired from the Tier 1 OS support list. To avoid potential security vulnerabilities, update your host OS to Bullseye. 

For [tier 2 supported platform operating systems ], installation packages are made available at [Azure IoT Edge releases ]. See the installation steps in [Offline or specific version installation (optional) ]. 

- [Ubuntu ]

- [Debian ]

- [Red Hat Enterprise Linux ]

- [Ubuntu Core snaps ]

Installing can be done with a few commands. Open a terminal and run the following commands: 

- 
**24.04 **: 

```
`wget https://packages.microsoft.com/config/ubuntu/24.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb `
```

- 
**22.04 **: 

```
`wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb `
```

- 
**20.04 **: 

```
`wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb `
```

Installing with APT can be done with a few commands. Open a terminal and run the following commands: 

- 
**12 - Bookworm (arm32v7) **: 

```
`curl https://packages.microsoft.com/config/debian/12/packages-microsoft-prod.deb > ./packages-microsoft-prod.deb
sudo apt install ./packages-microsoft-prod.deb `
```

- 
**11 - Bullseye (arm32v7) **: 

```
`curl https://packages.microsoft.com/config/debian/11/packages-microsoft-prod.deb > ./packages-microsoft-prod.deb
sudo apt install ./packages-microsoft-prod.deb `
```

Tip 

If you gave the "root" account a password during the OS install, you don't need 'sudo' and can run the previous command by starting with 'apt'. 

Installing can be done with a few commands. Open a terminal and run the following commands: 

- 
**9.x (amd64) **: 

```
`wget https://packages.microsoft.com/config/rhel/9.0/packages-microsoft-prod.rpm -O packages-microsoft-prod.rpm
  sudo yum localinstall packages-microsoft-prod.rpm
  rm packages-microsoft-prod.rpm `
```

- 
**8.x (amd64) **: 

```
`wget https://packages.microsoft.com/config/rhel/8/packages-microsoft-prod.rpm -O packages-microsoft-prod.rpm
  sudo yum localinstall packages-microsoft-prod.rpm
  rm packages-microsoft-prod.rpm `
```

You install IoT Edge runtime from the snap store in a later step. Continue to the next section. 

For more information about operating system versions, see [Azure IoT Edge supported platforms ]. 

Note 

Azure IoT Edge software packages are subject to the license terms located in each package ( `usr/share/doc/{package-name} `or the `LICENSE `directory). Read the license terms before using a package. Your installation and use of a package constitutes your acceptance of these terms. If you don't agree with the license terms, don't use that package. 

### Install a container engine 

Azure IoT Edge relies on an [OCI ]-compatible container runtime. For production scenarios, we recommend that you use the Moby engine. The Moby engine is the container engine officially supported with IoT Edge. Docker CE/EE container images are compatible with the Moby runtime. If you're using Ubuntu Core snaps, the Docker snap is serviced by Canonical and supported for production scenarios. 

- [Ubuntu ]

- [Debian ]

- [Red Hat Enterprise Linux ]

- [Ubuntu Core snaps ]

Install the Moby engine. 

```
`sudo apt-get update; \
  sudo apt-get install moby-engine `
```

Install the Moby engine. 

```
`sudo apt-get update; \
  sudo apt-get install moby-engine `
```

Install the Moby engine and CLI. 

```
`sudo yum install moby-engine moby-cli `
```

Tip 

If you get errors when you install the Moby container engine, verify your Linux kernel for Moby compatibility. Some embedded device manufacturers ship device images that contain custom Linux kernels without the features required for container engine compatibility. Run the following command, which uses the [check-config script ]provided by Moby, to check your kernel configuration: 

```
`curl -ssl https://raw.githubusercontent.com/moby/moby/master/contrib/check-config.sh -o check-config.sh
chmod +x check-config.sh
./check-config.sh `
```

In the output of the script, check that all items under `Generally Necessary `and `Network Drivers `are enabled. If you're missing features, enable them by rebuilding your kernel from source and selecting the associated modules for inclusion in the appropriate kernel .config. Similarly, if you're using a kernel configuration generator like `defconfig `or `menuconfig `, find and enable the respective features and rebuild your kernel accordingly. After you deploy your newly modified kernel, run the check-config script again to verify that all the required features were successfully enabled. 

IoT Edge has dependencies on Docker and IoT Identity Service. Install the dependencies using the following commands: 

```
`sudo snap install docker
sudo snap install azure-iot-identity `
```

The Docker snap is serviced by Canonical and supported for production scenarios. 

By default, the container engine doesn't set container log size limits. Over time, this situation can lead to the device filling up with logs and running out of disk space. However, you can configure your log to show locally, though it's optional. To learn more about logging configuration, see [Prepare to deploy your IoT Edge solution in production ]. 

The following steps show you how to configure your container to use [`local `logging driver ]as the logging mechanism. 

- [Ubuntu / Debian / RHEL ]

- [Ubuntu Core snaps ]

- 
Create or edit the existing Docker [daemon's config file ]

```
`sudo nano /etc/docker/daemon.json `
```

- 
Set the default logging driver to the `local `logging driver as shown in the example. 

```
`{
      "log-driver": "local"
   } `
```

- 
Restart the container engine for the changes to take effect. 

```
`sudo systemctl restart docker `
```

Currently, the `local `logging driver setting isn't supported for the Docker snap. 

### Install the IoT Edge runtime 

The IoT Edge service provides and maintains security standards on the IoT Edge device. The service starts on every boot and bootstraps the device by starting the rest of the IoT Edge runtime. 

Note 

Beginning with version 1.2, the [Azure IoT identity service ]handles identity provisioning and management for IoT Edge and for other device components that need to communicate with IoT Hub. 

The steps in this section represent the typical process to install the latest IoT Edge version on a device that has internet connection. If you need to install a specific version, like a prerelease version, or need to install while offline, follow the **Offline or specific version installation **steps later in this article. 

Tip 

If you already have an IoT Edge device running an older version and want to upgrade to the latest release, use the steps in [Update IoT Edge ]. Later versions are sufficiently different from previous versions of IoT Edge that specific steps are necessary to upgrade. 

- [Ubuntu ]

- [Debian ]

- [Red Hat Enterprise Linux ]

- [Ubuntu Core snaps ]

Install the latest version of IoT Edge and the IoT identity service package (if you're not already [up-to-date ]): 

- 
**22.04 **: 

```
`sudo apt-get update; \
   sudo apt-get install aziot-edge `
```

- 
**20.04 **: 

```
`sudo apt-get update; \
   sudo apt-get install aziot-edge `
```

Install the latest version of IoT Edge and the IoT identity service package (if you're not already [up-to-date ]): 

```
`sudo apt-get update; \
  sudo apt-get install aziot-edge `
```

Install the latest version of IoT Edge and the IoT identity service package (if you're not already [up-to-date ]): 

```
`sudo yum install aziot-edge `
```

Install IoT Edge from the snap store: 

```
`sudo snap install azure-iot-edge `
```

### Connect snaps 

By default, snaps are dependency-free, untrusted, and strictly confined. Hence, snaps must be connected to other snaps and system resources after installation. Use the following commands to connect the IoT Identity Service and IoT Edge snaps to each other and to system resources. To get started, snaps need to be manually connected. For production deployments, they can be configured to automatically connect to reduce the provisioning workload. 

```
`#------------------------
#  IoT Identity Service
#------------------------

# Connect the Identity Service snap to the logging system
# and grant permission to query system info

sudo snap connect azure-iot-identity:log-observe
sudo snap connect azure-iot-identity:mount-observe
sudo snap connect azure-iot-identity:system-observe
sudo snap connect azure-iot-identity:hostname-control

# If using a TPM, enable TPM access

sudo snap connect azure-iot-identity:tpm

#------------
#  IoT Edge
#------------

# Connect to your /home directory to enable writing support bundles

sudo snap connect azure-iot-edge:home

# Connect to logging and grant permission to query system info

sudo snap connect azure-iot-edge:log-observe
sudo snap connect azure-iot-edge:mount-observe
sudo snap connect azure-iot-edge:system-observe
sudo snap connect azure-iot-edge:hostname-control
# Allow IoT Edge to connect to the /var/run/iotedge folder and use sockets

sudo snap connect azure-iot-edge:run-iotedge

# Connect IoT Edge to Docker

sudo snap connect azure-iot-edge:docker docker:docker-daemon `
```

## Provision the device with its cloud identity 

Now that the container engine and the IoT Edge runtime are installed on your device, you're ready to set up the device with its cloud identity and authentication information. 

- [Ubuntu / Debian / RHEL ]

- [Ubuntu Core snaps ]

You can configure your IoT Edge device with symmetric key authentication using the following command: 

```
`sudo iotedge config mp --connection-string 'PASTE_DEVICE_CONNECTION_STRING_HERE' `
```

This `iotedge config mp `command creates a configuration file on the device and enters your connection string in the configuration file. 

- 
Apply the configuration changes. 

```
`sudo iotedge config apply `
```

- 
To view the configuration file, you can open it: 

```
`sudo nano /etc/aziot/config.toml `
```

- 
Create a **config.toml **file in your home directory and configure your IoT Edge device with a symmetric key authentication for the snap. 

```
`sudo nano ~/config.toml `
```

- 
You can manually provision with a connection string using the following provisioning settings: 

```
`[provisioning]
source = "manual"
connection_string = "REPLACE_WITH_DEVICE_CONNECTION_STRING" `
```

For more information about provisioning configuration settings, see [Configure IoT Edge device settings ]. 

- 
Set the configuration for IoT Edge and the Identity Service using the following command: 

```
`sudo snap set azure-iot-edge raw-config="$(cat ~/config.toml)" `
```

## Deploy modules 

To deploy your IoT Edge modules, go to your IoT hub in the Azure portal, then: 

- 
Select **Devices **from the IoT Hub menu. 

- 
Select your device to open its page. 

- 
Select the **Set Modules **tab. 

- 
Since we want to deploy the IoT Edge default modules (edgeAgent and edgeHub), we don't need to add any modules to this pane, so select **Review + create **at the bottom. 

- 
You see the JSON confirmation of your modules. Select **Create **to deploy the modules. 

For more information, see [Deploy a module ]. 

## Verify successful configuration 

Verify that the runtime was successfully installed and configured on your IoT Edge device. 

Tip 

You need elevated privileges to run `iotedge `commands. Once you sign out of your machine and sign back in the first time after installing the IoT Edge runtime, your permissions are automatically updated. Until then, use `sudo `in front of the commands. 

- 
Check to see that the IoT Edge system service is running. 

```
`sudo iotedge system status `
```

A successful status response shows the `aziot `services as running or ready. 

- 
If you need to troubleshoot the service, retrieve the service logs. 

```
`sudo iotedge system logs `
```

- 
Use the `check `tool to verify configuration and connection status of the device. 

```
`sudo iotedge check `
```

You can expect a range of responses that might include **OK **(green), **Warning **(yellow), or **Error **(red). For troubleshooting common errors, see [Solutions to common issues for Azure IoT Edge ]. 

[]

Tip 

Always use `sudo `to run the check tool, even after your permissions are updated. The tool needs elevated privileges to access the config file to verify configuration status. 

Note 

On a newly provisioned device, you might see an error related to IoT Edge Hub: 

**Ã production readiness: Edge Hub's storage directory is persisted on the host filesystem - Error ****Could not check current state of edgeHub container **

This error is expected on a newly provisioned device because the IoT Edge Hub module isn't yet running. Be sure your IoT Edge modules were deployed in the previous steps. Deployment resolves this error. 

Alternatively, you might see a status code as `417 -- The device's deployment configuration is not set `. Once your modules are deployed, this status changes. 

- 
When the service starts for the first time, you should only see the **edgeAgent **module running. The edgeAgent module runs by default and helps to install and start any other modules that you deploy to your device. 

Check that your device and modules are deployed and running, by viewing your device page in the Azure portal. 

[]

Once your modules are deployed and running, list them in your device or virtual machine with the following command: 

```
`sudo iotedge list `
```

## Offline or specific version installation (optional) 

The steps in this section are for scenarios not covered by the standard installation steps. These scenarios might include: 

- Installing IoT Edge while offline 

- Installing a release candidate version 

Use the steps in this section if you want to install a [specific version of the Azure IoT Edge runtime ]that isn't available through your package manager. The Microsoft package list only contains a limited set of recent versions and their subversions, so these steps are for anyone who wants to install an older version or a release candidate version. 

If you're using Ubuntu snaps, you can download a snap and install it offline. For more information, see [Download snaps and install offline ]. 

Using curl commands, you can target the component files directly from the IoT Edge GitHub repository. 

- 
Navigate to the [Azure IoT Edge releases ], and find the release version that you want to target. 

- 
Expand the **Assets **section for that version. 

- 
Every release should have new files for IoT Edge and the identity service. If you're going to install IoT Edge on an offline device, download these files ahead of time. Otherwise, use the following commands to update those components. 

- 
Find the **aziot-identity-service **file that matches your IoT Edge device's architecture. Right-click on the file link and copy the link address. 

- 
Use the copied link in the following command to install that version of the identity service: 

- [Ubuntu / Debian ]

- [Red Hat Enterprise Linux ]

- [Ubuntu Core snaps ]

```
`curl -L <identity service link> -o aziot-identity-service.deb && sudo apt-get install ./aziot-identity-service.deb `
```

```
`curl -L <identity service link> -o aziot-identity-service.rpm && sudo yum localinstall ./aziot-identity-service.rpm `
```

If you're using Ubuntu snaps, you can download a snap package and install it offline. For more information, see [Download snaps and install offline ]. 

- 
Find the **aziot-edge **file that matches your IoT Edge device's architecture. Right-click on the file link and copy the link address. 

- 
Use the copied link in the following command to install that version of IoT Edge. 

- [Ubuntu / Debian ]

- [Red Hat Enterprise Linux ]

- [Ubuntu Core snaps ]

```
`curl -L <iotedge link> -o aziot-edge.deb && sudo apt-get install ./aziot-edge.deb `
```

```
`curl -L <iotedge link> -o aziot-edge.rpm && sudo yum localinstall ./aziot-edge.rpm `
```

If you're using Ubuntu snaps, you can download a snap package and install it offline. For more information, see [Download snaps and install offline ]. 

## Uninstall IoT Edge 

If you want to remove the IoT Edge installation from your device, use the following commands. 

Remove the IoT Edge runtime. 

- [Ubuntu / Debian ]

- [Red Hat Enterprise Linux ]

- [Ubuntu Core snaps ]

```
`sudo apt-get autoremove --purge aziot-edge `
```

Leave out the `--purge `flag if you plan to reinstall IoT Edge and use the same configuration information in the future. The `--purge `flag deletes all the files associated with IoT Edge, including your configuration files. 

```
`sudo yum remove aziot-edge `
```

Remove the IoT Edge runtime: 

```
`sudo snap remove azure-iot-edge `
```

Remove Azure Identity Service: 

```
`sudo snap remove azure-iot-identity `
```

When the IoT Edge runtime is removed, any containers that it created are stopped but still exist on your device. View all containers to see which ones remain. 

```
`sudo docker ps -a `
```

Delete the containers from your device, including the two runtime containers. 

```
`sudo docker rm -f <container ID> `
```

Finally, remove the container runtime from your device. 

- [Ubuntu / Debian ]

- [Red Hat Enterprise Linux ]

- [Ubuntu Core snaps ]

```
`sudo apt-get autoremove --purge moby-engine `
```

```
`sudo yum remove moby-cli
sudo yum remove moby-engine `
```

```
`sudo snap remove docker `
```

## Next steps 

Continue to [deploy IoT Edge modules ]to learn how to deploy modules onto your device. 

## Feedback 

Was this page helpful? 
Yes No No 
Need help with this topic? 

Want to try using Ask Learn to clarify or guide you through this topic? 
Ask Learn Ask Learn Suggest a fix? 
## Additional resources 

- Last updated on 2025-04-29 

### In this article 

Was this page helpful? 
Yes No No 
Need help with this topic? 

Want to try using Ask Learn to clarify or guide you through this topic? 
Ask Learn Ask Learn Suggest a fix? [en-us ][Your Privacy Choices ]Theme 
- Light 

- Dark 

- High contrast 

- 

- [AI Disclaimer ]

- [Previous Versions ]

- [Blog ]

- [Contribute ]

- [Privacy ]

- [Terms of Use ]

- [Trademarks ]

- © Microsoft 2025