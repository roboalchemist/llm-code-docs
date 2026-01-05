# Source: https://learn.microsoft.com/en-us/azure/iot-edge/how-to-update-iot-edge

Update IoT Edge version on devices | Microsoft Learn [Skip to main content ][Skip to Ask Learn chat experience ]
This browser is no longer supported. 

Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support. 
[Download Microsoft Edge ][More info about Internet Explorer and Microsoft Edge ]Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents [Read in English ]Add Add to plan [Edit ]
#### Share via 
[Facebook ][x.com ][LinkedIn ][Email ]Print 
Note 

Access to this page requires authorization. You can try [signing in ]or [changing directories ]. 

Access to this page requires authorization. You can try [changing directories ]. 

# Update IoT Edge 
Feedback Summarize this article for me 
## In this article 

**Applies to: **IoT Edge 1.5 IoT Edge 1.4 

Important 

IoT Edge 1.5 LTS is the [supported release ]. IoT Edge 1.4 LTS is end of life as of November 12, 2024. 

As the IoT Edge service releases new versions, update your IoT Edge devices for the latest features and security improvements. This article provides information about how to update your IoT Edge devices when a new version is available. 

Two logical components of an IoT Edge device need to be updated if you want to move to a newer version. 

- 
*Security subsystem *- It runs on the device, handles security-based tasks, and starts the modules when the device starts. The *security subsystem *can only be updated from the device itself. 

- 
*IoT Edge runtime *- The IoT Edge runtime is made up of the IoT Edge hub ( `edgeHub `) and IoT Edge agent ( `edgeAgent `) modules. Depending on how you structure your deployment, the *runtime *can be updated from either the device or remotely. 

## How to update 

Use the sections of this article to update both the security subsystem and runtime containers on a device. 

### Patch releases 

When you upgrade between *patch *releases, for example 1.5.1 to 1.5.2, the update order isn't important. You can upgrade the security subsystem or the runtime containers before or after the other. To update between patch releases: 

- [Update the security subsystem ]

- [Update the runtime containers ]

- [Verify versions match ]

You can [troubleshoot ]the upgrade process at any time. 

### Major or minor releases 

When you upgrade between major or minor releases, for example from 1.4 to 1.5, update both the security subsystem and the runtime containers. Before a release, we test the security subsystem and the runtime container version combination. To update between major or minor product releases: 

- 
On the device, stop IoT Edge using the command `sudo systemctl stop iotedge `and [uninstall ]. 

- 
On the device, upgrade your container engine, either [Docker ]or [Moby ]. 

- 
On the device, [install IoT Edge ]. 

If you're importing an old configuration using `iotedge config import `, then modify the [agent.config] image of the generated `/etc/aziot/config.toml `file to use the 1.5 image for edgeAgent. 

For more information, see [Configure IoT Edge device settings ]. 

- 
In IoT Hub, [update the module deployment ]to reference the newest system modules. 

- 
On the device, start the IoT Edge using `sudo iotedge config apply `. 

You can [troubleshoot ]the upgrade process at any time. 

## Update the security subsystem 

The IoT Edge security subsystem includes a set of native components that need to be updated using the package manager on the IoT Edge device. 

Check the version of the security subsystem running on your device by using the command `iotedge version `. If you're using IoT Edge for Linux on Windows, you need to SSH into the Linux virtual machine to check the version. 

- [Ubuntu / Debian ]

- [Red Hat Enterprise Linux ]

- [Linux on Windows ]

- [Windows ]

On Linux x64 devices, use `apt-get `or your appropriate package manager to update the security subsystem to the latest version. 

Update `apt `: 

```
`sudo apt-get update `
```

Note 

For instructions to get the latest repository configuration from Microsoft see the preliminary steps to [Install IoT Edge ]. 

Check to see which versions of IoT Edge are available: 

```
`apt list -a aziot-edge `
```

Update IoT Edge: 

```
`sudo apt-get install aziot-edge `
```

Running `apt-get install aziot-edge `upgrades the security subsystem and installs the [identity service ], `aziot-identity-service `, as a required dependency. 

Check to see which versions of IoT Edge are available. 

```
`yum list aziot-edge `
```

If you want to update to the most recent version of IoT Edge, use the following command, which also updates the [identity service ]to the latest version: 

```
`sudo yum install aziot-edge `
```

For information about IoT Edge for Linux on Windows updates, see [EFLOW Updates ]. 

Note 

Currently, there is no support for IoT Edge running on Windows devices in Windows containers. Use a Linux container to run IoT Edge on Windows. 

Then, reapply configuration to ensure system is fully updated. 

```
`sudo iotedge config apply `
```

## Update the runtime containers 

The way that you update the IoT Edge agent and IoT Edge hub containers depends on whether you use rolling tags (like 1.5) or specific tags (like 1.5.1) in your deployment. 

Check the version of the IoT Edge agent and IoT Edge hub modules currently on your device using the commands `iotedge logs edgeAgent `or `iotedge logs edgeHub `. If you're using IoT Edge for Linux on Windows, you need to SSH into the Linux virtual machine to check the runtime module versions. 

[]

### Understand IoT Edge tags 

The IoT Edge agent and IoT Edge hub images are tagged with the IoT Edge version that they're associated with. There are two different ways to use tags with the runtime images: 

- 
**Rolling tags **- Use only the first two values of the version number to get the latest image that matches those digits. For example, 1.5 is updated whenever there's a new release to point to the latest 1.5.x version. If the container runtime on your IoT Edge device pulls the image again, the runtime modules are updated to the latest version. Deployments from the Azure portal default to rolling tags. *This approach is suggested for development purposes. *

- 
**Specific tags **- Use all three values of the version number to explicitly set the image version. For example, 1.5.0 won't change after its initial release. You can declare a new version number in the deployment manifest when you're ready to update. *This approach is suggested for production purposes. *

### Update a rolling tag image 

If you use rolling tags in your deployment (for example, mcr.microsoft.com/azureiotedge-hub: **1.5 **) then you need to force the container runtime on your device to pull the latest version of the image. 

Delete the local version of the image from your IoT Edge device. On Windows machines, uninstalling the security subsystem also removes the runtime images, so you don't need to take this step again. 

```
`docker rmi mcr.microsoft.com/azureiotedge-hub:1.5
docker rmi mcr.microsoft.com/azureiotedge-agent:1.5 `
```

You may need to use the force `-f `flag to remove the images. 

The IoT Edge service pulls the latest versions of the runtime images and automatically starts them on your device again. 

### Update a specific tag image 

If you use specific tags in your deployment (for example, mcr.microsoft.com/azureiotedge-hub: **1.5 **) then all you need to do is update the tag in your deployment manifest and apply the changes to your device. 

- 
In the IoT Hub in the Azure portal, select your IoT Edge device, and select **Set Modules **. 

- 
On the **Modules **tab, select **Runtime Settings **. 

- 
In **Runtime Settings **, update the **Image URI **value in the **Edge Agent **section with the desired version. For example, `mcr.microsoft.com/azureiotedge-agent:1.5 `Don't select **Apply **yet. 

- 
Select the **Edge Hub **tab and update the **Image URI **value with the same desired version. For example, `mcr.microsoft.com/azureiotedge-hub:1.5 `. 

- 
Select **Apply **to save changes. 

- 
Select **Review + create **, review the deployment as seen in the JSON file, and select **Create **. 

## Update partner module URIs 

If you use partner modules, update your module deployments with image URIs provided by the partner. Contact the [IoT Edge module publisher ]to obtain the updated container image URI. Update your device configurations with the new image URI provided by the publisher. 

- Sign in to the [Azure portal ]and navigate to your IoT Hub. 

- On the left pane, select **Devices **under the **Device management **menu. 

- Select the IoT Edge device that uses the partner module from the list. 

- On the upper bar, select **Set Modules **. 

- Choose the IoT Edge partner module that you want to update with the new image URI. 

- Update the **Image URI **value with the new image URI provided by the publisher. 

- Select **Apply **to save changes. 

- Select **Review + create **, review the deployment as seen in the JSON file, and select **Create **. 

## Verify versions match 

- 
On your device, use `iotedge version `to check the security subsystem version. The output includes the major, minor, and revision version numbers. For example, *iotedge 1.5.13 *. 

- 
In your device deployment runtime settings, verify the *edgeHub *and *edgeAgent *image URI versions match the major and minor version of the security subsystem. If the security subsystem version is 1.5.15, the image versions would be 1.5. For example, *mcr.microsoft.com/azureiotedge-hub:1.5 *and *mcr.microsoft.com/azureiotedge-agent:1.5 *. 

Note 

Update the IoT Edge security subsystem and runtime containers to the same supported release version. While mismatched versions are supported, we haven't tested all version combinations. 

To find the latest version of Azure IoT Edge, see [Azure IoT Edge releases ]. 

## Troubleshooting 

You can view logs of your system at any time by running the following commands from your device. 

- 
Start troubleshooting using the [check ]command. It runs a collection of configuration and connectivity tests for common issues. 

```
`sudo iotedge check --verbose `
```

- 
To view the status of the IoT Edge system, run: 

```
`sudo iotedge system status `
```

- 
To view host component logs, run: 

```
`sudo iotedge system logs `
```

- 
To check for recurring issues reported with edgeAgent and edgeHub, run: 

Be sure to replace `<module> `with your own module name. If there are no issues, you see no output. 

```
`sudo iotedge logs <module> `
```

For more information, see [Troubleshoot your IoT Edge device ]. 

## Next steps 

View the latest [Azure IoT Edge releases ]. 

Stay up-to-date with recent updates and announcements in the [Internet of Things blog ]

## Feedback 

Was this page helpful? 
Yes No No 
Need help with this topic? 

Want to try using Ask Learn to clarify or guide you through this topic? 
Ask Learn Ask Learn Suggest a fix? 
## Additional resources 

- Last updated on 2025-01-23 

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