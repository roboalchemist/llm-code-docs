# Source: https://learn.microsoft.com/en-us/azure/iot-edge/troubleshoot

Troubleshoot Azure IoT Edge | Microsoft Learn [Skip to main content ][Skip to Ask Learn chat experience ]
This browser is no longer supported. 

Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support. 
[Download Microsoft Edge ][More info about Internet Explorer and Microsoft Edge ]Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents [Read in English ]Add Add to plan [Edit ]
#### Share via 
[Facebook ][x.com ][LinkedIn ][Email ]Print 
Note 

Access to this page requires authorization. You can try [signing in ]or [changing directories ]. 

Access to this page requires authorization. You can try [changing directories ]. 

# Troubleshoot your IoT Edge device 
Feedback Summarize this article for me 
## In this article 

**Applies to: **IoT Edge 1.5 

Important 

IoT Edge 1.5 LTS is the [supported release ]. IoT Edge 1.4 LTS is end of life as of November 12, 2024. If you are on an earlier release, see [Update IoT Edge ]. 

If you experience issues running Azure IoT Edge in your environment, use this article as a guide for troubleshooting and diagnostics. 

## Run the 'check' command 

Your first step when troubleshooting IoT Edge should be to use the `check `command, which runs a collection of configuration and connectivity tests for common issues. The `check `command is available in [release 1.0.7 ]and later. 

Note 

The troubleshooting tool can't run connectivity checks if the IoT Edge device is behind a proxy server. 

You can run the `check `command as follows, or include the `--help `flag to see a complete list of options: 

```
`sudo iotedge check `
```

The troubleshooting tool runs many checks that are sorted into these three categories: 

- *Configuration checks *examine details that could prevent IoT Edge devices from connecting to the cloud, including issues with the config file and the container engine. 

- *Connection checks *verify that the IoT Edge runtime can access ports on the host device and that all the IoT Edge components can connect to the IoT Hub. This set of checks returns errors if the IoT Edge device is behind a proxy. 

- *Production readiness checks *look for recommended production best practices, such as the state of device certificate authority (CA) certificates and module log file configuration. 

The IoT Edge check tool uses a container to run its diagnostics. The container image, `mcr.microsoft.com/azureiotedge-diagnostics:latest `, is available through the [Microsoft Artifact Registry ](MAR). If you need to run a check on a device without direct access to the internet, your devices need access to the container image. 

In a scenario using nested IoT Edge devices, you can get access to the diagnostics image on downstream devices by routing the image pull through the parent devices. 

```
`sudo iotedge check --diagnostics-image-name <parent_device_fqdn_or_ip>:<port_for_api_proxy_module>/azureiotedge-diagnostics:1.2 `
```

For information about each of the diagnostic checks this tool runs, including what to do if you get an error or warning, see [Built-in troubleshooting functionality ]. 

## Gather debug information with 'support-bundle' command 

When you need to gather logs from an IoT Edge device, the most convenient way is to use the `support-bundle `command. By default, this command collects module, IoT Edge security manager and container engine logs, `iotedge check `JSON output, and other useful debug information. It compresses them into a single file for easy sharing. The `support-bundle `command is available in [release 1.0.9 ]and later. 

Run the `support-bundle `command with the `--since `flag to specify how long from the past you want to get logs. For example `6h `gets logs since the last six hours, `6d `since the last six days, `6m `since the last six minutes and so on. Include the `--help `flag to see a complete list of options. 

```
`sudo iotedge support-bundle --since 6h `
```

By default, the `support-bundle `command creates a zip file called **support_bundle.zip **in the directory where the command is called. Use the flag `--output `to specify a different path or file name for the output. 

For more information about the command, view its help information. 

```
`iotedge support-bundle --help `
```

You can also use the built-in direct method call [UploadSupportBundle ]to upload the output of the support-bundle command to Azure Blob Storage. 

Warning 

Output from the `support-bundle `command can contain host, device names, module names, and information logged by your modules. Be aware of this inclusion if sharing the output in a public forum. 

## Review metrics collected from the runtime 

The IoT Edge runtime modules produce metrics to help you monitor and understand the health of your IoT Edge devices. Add the **metrics-collector **module to your deployments to handle collecting these metrics and sending them to the cloud for easier monitoring. 

For more information, see [Collect and transport metrics ]. 

## Check your IoT Edge version 

If you're running an older version of IoT Edge, then upgrading might resolve your issue. The `iotedge check `tool checks that the IoT Edge security daemon is the latest version, but doesn't check the versions of the IoT Edge hub and agent modules. To check the version of the runtime modules on your device, use the commands `iotedge logs edgeAgent `and `iotedge logs edgeHub `. The version number is declared in the logs when the module starts up. 

For instructions on how to update your device, see [Update IoT Edge ]. 

## Verify the installation of IoT Edge on your devices 

You can verify the installation of IoT Edge on your devices by [monitoring the edgeAgent module twin ]. 

To get the latest edgeAgent module twin, run the following command from [Azure Cloud Shell ]: 

```
`az iot hub module-twin show --device-id <edge_device_id> --module-id '$edgeAgent' --hub-name <iot_hub_name> `
```

This command outputs all the edgeAgent [reported properties ]. Here are some helpful ones monitor the status of the device: 

- runtime status 

- runtime start time 

- runtime last exit time 

- runtime restart count 

## Check the status of the IoT Edge security manager and its logs 

The [IoT Edge security manager ]is responsible for operations like initializing the IoT Edge system at startup and provisioning devices. If IoT Edge isn't starting, the security manager logs can provide useful information. 

- 
View the status of the IoT Edge system services: 

```
`sudo iotedge system status `
```

- 
View the logs of the IoT Edge system services: 

```
`sudo iotedge system logs -- -f `
```

- 
Enable debug-level logs to view more detailed logs of the IoT Edge system services: 

- 
Enable debug-level logs. 

```
`sudo iotedge system set-log-level debug
sudo iotedge system restart `
```

- 
Switch back to the default info-level logs after debugging. 

```
`sudo iotedge system set-log-level info
sudo iotedge system restart `
```

## Check container logs for issues 

Once the IoT Edge security daemon is running, look at the logs of the containers to detect issues. Start with your deployed containers, then look at the containers that make up the IoT Edge runtime: edgeAgent and edgeHub. The IoT Edge agent logs typically provide info on the lifecycle of each container. The IoT Edge hub logs provide info on messaging and routing. 

You can retrieve the container logs from several places: 

- 
On the IoT Edge device, run the following command to view logs: 

```
`iotedge logs <container name> `
```

- 
On the Azure portal, use the built-in troubleshoot tool. For more information, see [Troubleshoot IoT Edge devices from the Azure portal ]. 

- 
Use the [UploadModuleLogs direct method ]to upload the logs of a module to Azure Blob Storage. 

## Clean up container logs 

By default the Moby container engine doesn't set container log size limits. Over time extensive logs can lead to the device filling up with logs and running out of disk space. If large container logs are affecting your IoT Edge device performance, use the following command to force-remove the container along with its related logs. 

If you're still troubleshooting, wait until after you inspect the container logs to take this step. 

Warning 

If you force remove the edgeHub container while it has an undelivered message backlog and no [host storage ]configured, the undelivered messages are lost. 

```
`docker rm --force <container name> `
```

For more information about ongoing logs maintenance and production scenarios, see [Set up default logging driver ]. 

## View the messages going through the IoT Edge hub 

You can view the messages going through the IoT Edge hub and gather insights from verbose logs from the runtime containers. To turn on verbose logs on these containers, set the `RuntimeLogLevel `environment variable in the deployment manifest. 

To view messages going through the IoT Edge hub, set the `RuntimeLogLevel `environment variable to `debug `for the edgeHub module. 

Both the edgeHub and edgeAgent modules have this runtime log environment variable, with the default value set to `info `. This environment variable can take the following values: 

- fatal 

- error 

- warning 

- info 

- debug 

- verbose 

You can also check the messages being sent between IoT Hub and IoT devices. View these messages by using the [Azure IoT Hub extension for Visual Studio Code ]. For more information, see [Handy tool when you develop with Azure IoT ]. 

## Restart containers 

After investigating the logs and messages for information, you can try restarting containers. 

On the IoT Edge device, use the following commands to restart modules: 

```
`iotedge restart <container name> `
```

Restart the IoT Edge runtime containers: 

```
`iotedge restart edgeAgent && iotedge restart edgeHub `
```

You can also restart modules remotely from the Azure portal. For more information, see [Troubleshoot IoT Edge devices from the Azure portal ]. 

## Check your firewall and port configuration rules 

Azure IoT Edge allows communication from an on-premises server to Azure cloud using supported IoT Hub protocols. For more information, see [Choose a device communication protocol ]. For enhanced security, communication channels between Azure IoT Edge and Azure IoT Hub are always configured to be Outbound. This configuration is based on the [Service Assisted Communication pattern ], which minimizes the attack surface for a malicious entity to explore. Inbound communication is only required for [specific scenarios ]where Azure IoT Hub needs to push messages to the Azure IoT Edge device. Cloud-to-device messages are protected using secure TLS channels and can be further secured using X.509 certificates and TPM device modules. The Azure IoT Edge Security Manager governs how this communication can be established. For more information, see [Azure IoT Edge security manager ]. 

While IoT Edge provides enhanced configuration for securing Azure IoT Edge runtime and deployed modules, it's still dependent on the underlying machine and network configuration. Hence, it's imperative to ensure proper network and firewall rules are set up for secure edge to cloud communication. The following table can be used as a guideline when configuration firewall rules for the underlying servers where Azure IoT Edge runtime is hosted: 
Protocol Port Incoming Outgoing Guidance MQTT 8883 BLOCKED (Default) BLOCKED (Default) 
- Configure Outgoing (Outbound) to be Open when using MQTT as the communication protocol. 

- IoT Edge doesn't support port 1883 for MQTT. 

- Incoming (Inbound) connections should be blocked. 
AMQP 5671 BLOCKED (Default) OPEN (Default) 
- Default communication protocol for IoT Edge. 

- Must be configured to be Open if Azure IoT Edge isn't configured for other supported protocols or AMQP is the desired communication protocol. 

- IoT Edge doesn't support port 5672 for AMQP. 

- Block this port when Azure IoT Edge uses a different IoT Hub supported protocol. 

- Incoming (Inbound) connections should be blocked. 
HTTPS 443 BLOCKED (Default) OPEN (Default) 
- Configure Outgoing (Outbound) to be Open on 443 for IoT Edge provisioning. This configuration is required when using manual scripts or Azure IoT Device Provisioning Service (DPS). 

- [Incoming (Inbound) connection ]should be Open only for specific scenarios: 
- If you have a transparent gateway with downstream devices that can send method requests. In this case, port 443 doesn't need to be open to external networks to connect to IoT Hub or provide IoT Hub services through Azure IoT Edge. Thus the incoming rule could be restricted to only open Incoming (Inbound) from the internal network. 

- For Client to Device (C2D) scenarios. 

- IoT Edge doesn't support port 80 for HTTP. 

- If non-HTTP protocols (for example, AMQP or MQTT) can't be configured in the enterprise; the messages can be sent over WebSockets. Port 443 is used for WebSocket communication in that case. 

## Last resort: stop and recreate all containers 

Sometimes, a system might require significant special modification to work with existing networking or operating system constraints. For example, a system could require a different data disk mount and proxy settings. If you tried all previous steps and still get container failures, the docker system caches or persisted network settings might not up to date with the latest reconfiguration. In this case, the last resort option is to use [`docker prune `]get a clean start from scratch. 

The following command stops the IoT Edge system (and thus all containers), uses the "all" and "volume" option for `docker prune `to remove all containers and volumes. Review the warning that the command issues and confirm with `y `when ready. 

```
`sudo iotedge system stop
docker system prune --all --volumes `
```

```
`WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all volumes not used by at least one container
  - all images without at least one container associated to them
  - all build cache

Are you sure you want to continue? [y/N] `
```

Start the system again. To be safe, apply any potentially remaining configuration and start the system with one command. 

```
`sudo iotedge config apply `
```

Wait a few minutes and check again. 

```
`sudo iotedge list `
```

## Next steps 

Do you think that you found a bug in the IoT Edge platform? [Submit an issue ]so that we can continue to improve. 

If you have more questions, create a [Support request ]for help. 

## Feedback 

Was this page helpful? 
Yes No No 
Need help with this topic? 

Want to try using Ask Learn to clarify or guide you through this topic? 
Ask Learn Ask Learn Suggest a fix? 
## Additional resources 

- Last updated on 2025-05-05 

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

- © Microsoft 2026