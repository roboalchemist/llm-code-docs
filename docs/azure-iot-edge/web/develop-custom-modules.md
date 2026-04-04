# Source: https://learn.microsoft.com/en-us/azure/iot-edge/how-to-develop-csharp-module

Develop Azure IoT Edge modules using Visual Studio Code tutorial | Microsoft Learn [Skip to main content ][Skip to Ask Learn chat experience ]
This browser is no longer supported. 

Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support. 
[Download Microsoft Edge ][More info about Internet Explorer and Microsoft Edge ]Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents [Read in English ]Add Add to plan [Edit ]
#### Share via 
[Facebook ][x.com ][LinkedIn ][Email ]Print 
Note 

Access to this page requires authorization. You can try [signing in ]or [changing directories ]. 

Access to this page requires authorization. You can try [changing directories ]. 

# Tutorial: Develop IoT Edge modules using Visual Studio Code 
Feedback Summarize this article for me 
## In this article 

**Applies to: **IoT Edge 1.5 

Important 

IoT Edge 1.5 LTS is the [supported release ]. IoT Edge 1.4 LTS is end of life as of November 12, 2024. If you are on an earlier release, see [Update IoT Edge ]. 

This tutorial shows how to develop and deploy your code to an IoT Edge device. Azure IoT Edge modules enable you to deploy code that runs your business logic directly on your IoT Edge device. In the [Deploy code to a Linux device ]quickstart, you set up an IoT Edge device and deployed a module from the Azure Marketplace. 

This article describes the steps for two IoT Edge development tools: 

- **Azure IoT Edge Dev Tool **command-line (CLI), which is preferred for development. 

- **Azure IoT Edge tools for Visual Studio Code **extension, which is in [maintenance mode ]. 

Use the tool selector button at the beginning of this article to choose your tool. 

In this tutorial, you learn how to: 

- Set up your development machine 

- Use the IoT Edge tools to create a new project 

- Build your project as a [Docker container ]and store it in an Azure container registry 

- Deploy your code to an IoT Edge device 

The IoT Edge module you create in this tutorial filters the temperature data your device generates. It sends messages upstream only if the temperature is above a set threshold. This kind of analysis at the edge helps reduce the amount of data sent to and stored in the cloud. 

## Prerequisites 

A development machine: 

- Use your own computer or a virtual machine. 

- Make sure your development machine supports [nested virtualization ]to run a container engine. 

- You can use most operating systems that run a container engine to develop IoT Edge modules for Linux devices. This tutorial uses a Windows computer, but it also points out known differences on macOS or Linux. 

- Install [Visual Studio Code ]

- Install the [Azure CLI ]. 

An Azure IoT Edge device: 

- Run IoT Edge on a separate device. Keeping the development machine and IoT Edge device separate simulates a real deployment scenario and helps keep the concepts clear. Use the quickstart article [Deploy code to a Linux Device ]to create an IoT Edge device in Azure or the [Azure Resource Manager template to deploy an IoT Edge-enabled VM ]. 

Cloud resources: 

- Use a free or standard-tier [Azure IoT Hub ]. 

If you don't have an Azure account, create a [free account ]before you begin. 

Tip 

For guidance on interactive debugging in Visual Studio Code or Visual Studio 2022: 

- [Debug Azure IoT Edge modules using Visual Studio Code ]

- [Use Visual Studio 2022 to develop and debug modules for Azure IoT Edge ]

This tutorial covers development steps for Visual Studio Code. 

## Key concepts 

This tutorial walks through developing an IoT Edge module. An *IoT Edge module *is a container with executable code. You can deploy one or more modules to an IoT Edge device. Modules do specific tasks like ingesting data from sensors, cleaning and analyzing data, or sending messages to an IoT Hub. For more information, see [Understand Azure IoT Edge modules ]. 

When you develop IoT Edge modules, you should understand the difference between the development machine and the target IoT Edge device where the module deploys. The container you build to hold your module code must match the operating system (OS) of the target device. For example, the most common scenario is developing a module on a Windows computer to target a Linux device running IoT Edge. In that case, the container operating system is Linux. As you go through this tutorial, keep in mind the difference between the *development machine OS *and the *container OS *. 

Tip 

If you're using [IoT Edge for Linux on Windows ], the target device in your scenario is the Linux virtual machine, not the Windows host. 

This tutorial targets devices running IoT Edge with Linux containers. Use your preferred operating system as long as your development machine runs Linux containers. Visual Studio Code is recommended for developing with Linux containers, so this tutorial uses it. You can use Visual Studio as well, although there are differences in support between the two tools. 

The following table lists supported development scenarios for Linux containers in Visual Studio Code and Visual Studio. 
Visual Studio Code Visual Studio 2019/2022 **Linux device architecture **Linux AMD64 
Linux ARM32v7 
Linux ARM64 Linux AMD64 
Linux ARM32 
Linux ARM64 **Azure services **Azure Functions 
Azure Stream Analytics 
Azure Machine Learning **Languages **C 
C# 
Java 
Node.js 
Python C 
C# **More information **[Azure IoT Edge for Visual Studio Code ][Azure IoT Edge Tools for Visual Studio 2019 ]
[Azure IoT Edge Tools for Visual Studio 2022 ]
## Install container engine 

IoT Edge modules are packaged as containers, so you need a [Docker compatible container management system ]on your development machine to build and manage them. Docker Desktop is a popular choice for development because it has strong feature support. Docker Desktop on Windows lets you switch between Linux containers and Windows containers, so you can develop modules for different types of IoT Edge devices. 

Use the Docker documentation to install Docker on your development machine: 

- 
[Install Docker Desktop for Windows ]. When you install Docker Desktop for Windows, you're asked whether you want to use Linux or Windows containers. You can change this setting at any time. This tutorial uses Linux containers because the modules target Linux devices. For more information, see [Switch between Windows and Linux containers ]. 

- 
[Install Docker Desktop for Mac ]

- 
Read [About Docker CE ]for installation information on several Linux platforms. For the Windows Subsystem for Linux (WSL), install Docker Desktop for Windows. 

## Set up tools 

Install the Python-based [Azure IoT Edge Dev Tool ]to create your IoT Edge solution. You have two options: 

- Use the preferred prebuilt [IoT Edge Dev Container ]. 

- Install the tool using the [iotedgedev development setup ]. 

Important 

The **Azure IoT Edge tools for Visual Studio Code **extension is in [maintenance mode ]. The preferred development tool is the command-line (CLI) **Azure IoT Edge Dev Tool **. 

Use the IoT extensions for Visual Studio Code to develop IoT Edge modules. These extensions offer project templates, automate the creation of the deployment manifest, and let you monitor and manage IoT Edge devices. In this section, you install Visual Studio Code and the IoT extension, then set up your Azure account to manage IoT Hub resources from within Visual Studio Code. 

- Install [Azure IoT Edge ]extension. 

- Install [Azure IoT Hub ]extension. 

- After you install the extensions, open the command palette by selecting **View > Command Palette **. 

- In the command palette, search for and select **Azure IoT Hub: Select IoT Hub **. Follow the prompts to select your Azure subscription and IoT Hub. 

- Open the explorer section of Visual Studio Code by selecting the icon in the activity bar or by selecting **View > Explorer **. 

- At the bottom of the explorer section, expand the collapsed **Azure IoT Hub / Devices **menu. You see the devices and IoT Edge devices associated with the IoT Hub that you selected through the command palette. 

### Install language specific tools 

Install tools specific to the language you're developing in: 

- [C# ]

- [C ]

- [Java ]

- [Node.js ]

- [Python ]

- [.NET Core SDK ]

- [C# Visual Studio Code extension ]

- [C/C++ Visual Studio Code extension ]

- Installing the Azure IoT C SDK isn't required for this tutorial, but can provide helpful functionality like IntelliSense and reading program definitions. For installation information, see [Azure IoT C SDKs and Libraries ]. 

- [Java SE Development Kit 11 ]and [Maven ]. You need to [set the `JAVA_HOME `environment variable ]to point to your JDK installation. 

- [Maven ]

- [Java Extension Pack for Visual Studio Code ]

Tip 

The Java and Maven installation processes add environment variables to your system. Restart any open Visual Studio Code terminal, PowerShell, or command prompt instances after you finish installation. This step makes sure these utilities recognize the Java and Maven commands. 

- [Node.js ]. 

- [Yeoman ]

- [Azure IoT Edge Node.js Module Generator ]. 

To develop an IoT Edge module in Python, install these extra prerequisites on your development machine: 

- [Python ]and [Pip ]. 

- [Cookiecutter ]. 

- [Python extension for Visual Studio Code ]. 

Note 

Make sure your `bin `folder is on your path for your platform. Typically, it's `~/.local/ `for UNIX and macOS, or `%APPDATA%\Python `on Windows. 

## Create a container registry 

In this tutorial, you use the [Azure IoT Edge ]and [Azure IoT Hub ]extensions to build a module and create a container image from the files. Then you push this image to a registry that stores and manages your images. Finally, you deploy your image from your registry to run on your IoT Edge device. 

Important 

The Azure IoT Edge Visual Studio Code extension is in [maintenance mode ]. 

You can use any Docker-compatible registry to hold your container images. Two popular Docker registry services are [Azure Container Registry ]and [Docker Hub ]. This tutorial uses Azure Container Registry. 

If you don't already have a container registry, follow these steps to create a new one in Azure: 

- 
In the [Azure portal ], select **Create a resource **> **Containers **> **Container Registry **. 

- 
Provide the following required values to create your container registry: 
Field Value Subscription Select a subscription from the drop-down list. Resource group Use the same resource group for all of the test resources that you create during the IoT Edge quickstarts and tutorials; for example, **IoTEdgeResources **. Registry name Provide a unique name. Location Choose a location close to you. SKU Select **Basic **. 

- 
Select **Review + create **, then **Create **. 

- 
Select your new container registry from the **Resources **section of your Azure portal home page to open it. 

- 
In the left pane of your container registry, select **Access keys **from the menu located under **Settings **. 

[]

- 
Enable **Admin user **with the toggle button and view the **Username **and **Password **for your container registry. 

- 
Copy the values for **Login server **, **Username **, and **password **and save them somewhere convenient. You use these values throughout this tutorial to provide access to the container registry. 

## Create a new module project 

The Azure IoT Edge extension offers project templates for all supported IoT Edge module languages in Visual Studio Code. These templates include all the files and code you need to deploy a working module to test IoT Edge, or give you a starting point to customize the template with your own business logic. 

### Create a project template 

The [IoT Edge Dev Tool ]simplifies Azure IoT Edge development, with commands driven by environment variables. It helps you get started with IoT Edge development using the IoT Edge Dev Container and IoT Edge solution scaffolding that includes a default module and all the required configuration files. 

- 
Create a directory for your solution at the path you want. Change to your `iotedgesolution `directory. 

```
`mkdir c:\dev\iotedgesolution
cd c:\dev\iotedgesolution `
```

- 
Use the `iotedgedev solution init `command to create a solution and set up your Azure IoT Hub in the development language of your choice: 

- [C# ]

- [C ]

- [Java ]

- [Node.js ]

- [Python ]

```
`iotedgedev solution init --template csharp `
```

```
`iotedgedev solution init --template c `
```

```
`iotedgedev solution init --template java `
```

```
`iotedgedev solution init --template nodejs `
```

```
`iotedgedev solution init --template python `
```

The `iotedgedev solution init `command prompts you to complete several steps, including: 

- Authenticate to Azure 

- Choose an Azure subscription 

- Choose or create a resource group 

- Choose or create an Azure IoT Hub 

- Choose or create an Azure IoT Edge device 

Use Visual Studio Code and the [Azure IoT Edge ]extension. Start by creating a solution, then generate the first module in that solution. Each solution can include multiple modules. 

- Select **View > Command Palette **. 

- In the command palette, enter and run the command **Azure IoT Edge: New IoT Edge Solution **. 

- Browse to the folder where you want to create the new solution, then select **Select folder **. 

- Enter a name for your solution. 

- Select a module template for your preferred development language to be the first module in the solution. 

- Enter a name for your module. Choose a name that's unique within your container registry. 

- Enter the name of the module's image repository. Visual Studio Code autopopulates the module name with **localhost:5000/<your module name> **. Replace it with your own registry information. Use **localhost **if you use a local Docker registry for testing. If you use Azure Container Registry, use **Login server **from your registry's settings. The sign-in server looks like ***<registry name> *.azurecr.io **. Only replace the **localhost:5000 **part of the string, so that the final result looks like **< *registry name *>.azurecr.io/ *<your module name> ***. 

Visual Studio Code takes the information you provided, creates an IoT Edge solution, and then loads it in a new window. 

After you create the solution, these main files are in the solution: 

- 
The **.vscode **folder includes the configuration file **launch.json **. 

- 
The **modules **folder has subfolders for each module. In each subfolder, the module.json file controls how modules are built and deployed. 

- 
The **.env **file lists your environment variables. The environment variable for the container registry is **localhost:5000 **by default. 

- 
Two module deployment files, **deployment.template.json **and **deployment.debug.template.json **, list the modules to deploy to your device. By default, the list includes the IoT Edge system modules (edgeAgent and edgeHub) and sample modules such as: 

- **filtermodule **is a sample module that implements a simple filter function. 

- **SimulatedTemperatureSensor **module simulates data you can use for testing. For more information about how deployment manifests work, see [Learn how to use deployment manifests to deploy modules and establish routes ]. For more information about how the simulated temperature module works, see the [SimulatedTemperatureSensor.csproj source code ]. 

Note 

The exact modules installed can depend on your language of choice. 

### Set IoT Edge runtime version 

The latest stable IoT Edge system module version is 1.5. Set your system modules to version 1.5. 

- 
In Visual Studio Code, open the **deployment.template.json **deployment manifest file. The [deployment manifest ]is a JSON document that describes the modules to be configured on the targeted IoT Edge device. 

- 
Change the runtime version for the system runtime module images `edgeAgent `and `edgeHub `. For example, if you want to use the IoT Edge runtime version 1.5, change the following lines in the deployment manifest file: 

```
`"systemModules": {
    "edgeAgent": {

        "image": "mcr.microsoft.com/azureiotedge-agent:1.5",

    "edgeHub": {

        "image": "mcr.microsoft.com/azureiotedge-hub:1.5", `
```

### Provide your registry credentials to the IoT Edge agent 

The environment file stores the credentials for your container registry and shares them with the IoT Edge runtime. The runtime needs these credentials to pull your container images to the IoT Edge device. 

The IoT Edge extension tries to pull your container registry credentials from Azure and populate them in the environment file. 

Note 

The environment file is only created if you provide an image repository for the module. If you accepted the localhost defaults to test and debug locally, then you don't need to declare environment variables. 

Check if your credentials exist. If not, add them now: 

- 
If Azure Container Registry is your registry, set an Azure Container Registry username and password. Get these values from your container registry's **Settings **> **Access keys **menu in the Azure portal. 

- 
Open the **.env **file in your module solution. 

- 
Add the **username **and **password **values that you copied from your Azure container registry. For example: 

```
`CONTAINER_REGISTRY_SERVER="myacr.azurecr.io"
CONTAINER_REGISTRY_USERNAME="myacr"
CONTAINER_REGISTRY_PASSWORD="<registry_password>" `
```

- 
Save your changes to the **.env **file. 

Note 

This tutorial uses administrator credentials for Azure Container Registry that are convenient for development and test scenarios. When you're ready for production scenarios, we recommend a least-privileged authentication option like service principals or repository-scoped tokens. For more information, see [Manage access to your container registry ]. 

### Target architecture 

Select the architecture you're targeting with each solution, because that affects how the container is built and runs. The default is Linux AMD64. For this tutorial, use an Ubuntu virtual machine as the IoT Edge device and keep the default **amd64 **. 

If you need to change the target architecture for your solution, follow these steps. 

- Open the command palette and search for **Azure IoT Edge: Set Default Target Platform for Edge Solution **, or select the shortcut icon in the sidebar at the bottom of the window. 

- In the command palette, select the target architecture from the list of options. 

- [C# ]

- [C, Java, Node.js, Python ]

The target architecture is set when you create the container image in a later step. 

- 
Open or create **settings.json **in the **.vscode **directory of your solution. 

- 
Change the `platform `value to `amd64 `, `arm32v7 `, `arm64v8 `, or `windows-amd64 `. For example: 

```
`{
    "azure-iot-edge.defaultPlatform": {
        "platform": "amd64",
        "alias": null
    }
} `
```

### Update module with custom code 

Each template includes sample code that takes simulated sensor data from the **SimulatedTemperatureSensor **module and routes it to the IoT Hub. The sample module receives messages and passes them on. The pipeline functionality shows an important concept in IoT Edge: how modules communicate with each other. 

Each module can have multiple *input *and *output *queues declared in its code. The IoT Edge hub running on the device routes messages from the output of one module to the input of one or more modules. The specific code for declaring inputs and outputs varies between languages, but the concept is the same for all modules. For more information about routing between modules, see [Declare routes ]. 

- [C# ]

- [C ]

- [Java ]

- [Node.js ]

- [Python ]

The sample C# code that comes with the project template uses the [ModuleClient class ]from the IoT Hub SDK for .NET. 

- 
In the Visual Studio Code explorer, open **modules > filtermodule > ModuleBackgroundService.cs **. 

- 
Before the `filtermodule `namespace, add three `using `statements for types that are used later: 

```
`using System.Collections.Generic;     // For KeyValuePair<>
using Microsoft.Azure.Devices.Shared; // For TwinCollection
using Newtonsoft.Json;                // For JsonConvert `
```

- 
Add the `temperatureThreshold `variable to the `ModuleBackgroundService `class. This variable sets the value that the measured temperature must exceed for the data to be sent to the IoT Hub. 

```
`static int temperatureThreshold { get; set; } = 25; `
```

- 
Add the `MessageBody `, `Machine `, and `Ambient `classes. These classes define the expected schema for the body of incoming messages. 

```
`class MessageBody
{
    public Machine machine {get;set;}
    public Ambient ambient {get; set;}
    public string timeCreated {get; set;}
}
class Machine
{
    public double temperature {get; set;}
    public double pressure {get; set;}
}
class Ambient
{
    public double temperature {get; set;}
    public int humidity {get; set;}
} `
```

- 
Find the `ExecuteAsync `function. This function creates and configures a `ModuleClient `object that allows the module to connect to the local Azure IoT Edge runtime to send and receive messages. After creating the `ModuleClient `, the code reads the `temperatureThreshold `value from the module twin's desired properties. The code registers a callback to receive messages from an IoT Edge hub via an endpoint called `input1 `. 

Replace the call to the `ProcessMessageAsync `method with a new one that updates the name of the endpoint and the method that's called when input arrives. Also, add a `SetDesiredPropertyUpdateCallbackAsync `method for updates to the desired properties. To make this change, replace the last line of the `ExecuteAsync `method with the following code: 

```
`// Register a callback for messages that are received by the module.
// await _moduleClient.SetInputMessageHandlerAsync("input1", PipeMessage, cancellationToken);

// Read the TemperatureThreshold value from the module twin's desired properties
var moduleTwin = await _moduleClient.GetTwinAsync();
await OnDesiredPropertiesUpdate(moduleTwin.Properties.Desired, _moduleClient);

// Attach a callback for updates to the module twin's desired properties.
await _moduleClient.SetDesiredPropertyUpdateCallbackAsync(OnDesiredPropertiesUpdate, null);

// Register a callback for messages that are received by the module. Messages received on the inputFromSensor endpoint are sent to the FilterMessages method.
await _moduleClient.SetInputMessageHandlerAsync("inputFromSensor", FilterMessages, _moduleClient); `
```

- 
Add the `OnDesiredPropertiesUpdate `method to the `ModuleBackgroundService `class. This method receives updates on the desired properties from the module twin, and updates the `temperatureThreshold `variable to match. All modules have their own module twin, which lets you configure the code that's running inside a module directly from the cloud. 

```
`static Task OnDesiredPropertiesUpdate(TwinCollection desiredProperties, object userContext)
{
    try
    {
        Console.WriteLine("Desired property change:");
        Console.WriteLine(JsonConvert.SerializeObject(desiredProperties));

        if (desiredProperties["TemperatureThreshold"]!=null)
            temperatureThreshold = desiredProperties["TemperatureThreshold"];

    }
    catch (AggregateException ex)
    {
        foreach (Exception exception in ex.InnerExceptions)
        {
            Console.WriteLine();
            Console.WriteLine("Error when receiving desired property: {0}", exception);
        }
    }
    catch (Exception ex)
    {
        Console.WriteLine();
        Console.WriteLine("Error when receiving desired property: {0}", ex.Message);
    }
    return Task.CompletedTask;
} `
```

- 
Add the `FilterMessages `method. This method is called whenever the module receives a message from the IoT Edge hub. It filters out messages that report temperatures below the temperature threshold set via the module twin. It also adds the `MessageType `property to the message with the value set to `Alert `: 

```
`async Task<MessageResponse> FilterMessages(Message message, object userContext)
{
    var counterValue = Interlocked.Increment(ref _counter);
    try
    {
        ModuleClient moduleClient = (ModuleClient)userContext;
        var messageBytes = message.GetBytes();
        var messageString = Encoding.UTF8.GetString(messageBytes);
        Console.WriteLine($"Received message {counterValue}: [{messageString}]");

        // Get the message body.
        var messageBody = JsonConvert.DeserializeObject<MessageBody>(messageString);

        if (messageBody != null && messageBody.machine.temperature > temperatureThreshold)
        {
            Console.WriteLine($"Machine temperature {messageBody.machine.temperature} " +
                $"exceeds threshold {temperatureThreshold}");
            using (var filteredMessage = new Message(messageBytes))
            {
                foreach (KeyValuePair<string, string> prop in message.Properties)
                {
                    filteredMessage.Properties.Add(prop.Key, prop.Value);
                }

                filteredMessage.Properties.Add("MessageType", "Alert");
                await moduleClient.SendEventAsync("output1", filteredMessage);
            }
        }

        // Indicate that the message treatment is completed.
        return MessageResponse.Completed;
    }
    catch (AggregateException ex)
    {
        foreach (Exception exception in ex.InnerExceptions)
        {
            Console.WriteLine();
            Console.WriteLine("Error in sample: {0}", exception);
        }
        // Indicate that the message treatment is not completed.
        var moduleClient = (ModuleClient)userContext;
        return MessageResponse.Abandoned;
    }
    catch (Exception ex)
    {
        Console.WriteLine();
        Console.WriteLine("Error in sample: {0}", ex.Message);
        // Indicate that the message treatment is not completed.
        ModuleClient moduleClient = (ModuleClient)userContext;
        return MessageResponse.Abandoned;
    }
} `
```

- 
Save the **ModuleBackgroundService.cs **file. 

- 
In the Visual Studio Code explorer, open the **deployment.template.json **file in your IoT Edge solution workspace. 

- 
Since we changed the name of the endpoint that the module listens on, we also need to update the routes in the deployment manifest so that the **edgeHub **sends messages to the new endpoint. 

Find the `routes `section in the **$edgeHub **module twin. Update the `sensorTofiltermodule `route to replace `input1 `with `inputFromSensor `: 

```
`"sensorTofiltermodule": "FROM /messages/modules/tempSensor/outputs/temperatureOutput INTO BrokeredEndpoint(\"/modules/filtermodule/inputs/inputFromSensor\")" `
```

- 
Add the **filtermodule **module twin to the deployment manifest. Insert the following JSON content at the bottom of the `modulesContent `section, after the **$edgeHub **module twin: 

```
`"filtermodule": {
       "properties.desired":{
           "TemperatureThreshold":25
       }
   } `
```

- 
Save the **deployment.template.json **file. 

- 
The data from the sensor in this scenario comes in JSON format. To filter messages in JSON format, import a JSON library for C. This tutorial uses Parson. 

- 
Download the [Parson GitHub repository ]. Copy the **parson.c **and **parson.h **files into the **filtermodule **folder. 

- 
Open **modules > filtermodule > CMakeLists.txt **. At the top of the file, import the Parson files as a library called **my_parson **: 

```
`add_library(my_parson
    parson.c
    parson.h
) `
```

- 
Add `my_parson `to the list of libraries in the `target_link_libraries `function of CMakeLists.txt. 

- 
Save the **CMakeLists.txt **file. 

- 
Open **modules > filtermodule > main.c **. At the bottom of the list of `include `statements, add a new one to include `parson.h `for JSON support: 

```
`#include "parson.h" `
```

- 
In the **main.c **file, add a global variable called `temperatureThreshold `after the `include `section. This variable sets the value that the measured temperature must exceed in order for the data to be sent to IoT Hub: 

```
`static double temperatureThreshold = 25; `
```

- 
Find the `CreateMessageInstance `function in **main.c **. Replace the inner `if-else `statement with the following code that adds a few lines of functionality: 

```
`if ((messageInstance->messageHandle = IoTHubMessage_Clone(message)) == NULL)
{
    free(messageInstance);
    messageInstance = NULL;
}
else
{
    messageInstance->messageTrackingId = messagesReceivedByInput1Queue;
    MAP_HANDLE propMap = IoTHubMessage_Properties(messageInstance->messageHandle);
    if (Map_AddOrUpdate(propMap, "MessageType", "Alert") != MAP_OK)
    {
       printf("ERROR: Map_AddOrUpdate Failed!\r\n");
    }
} `
```

The new lines of code in the `else `statement add a new property to the message, which labels the message as an alert. This code labels all messages as alerts, because we'll add functionality that only sends messages to IoT Hub if they report high temperatures. 

- 
Replace the entire `InputQueue1Callback `function with the following code. This function implements the actual messaging filter. When a message is received, it checks whether the reported temperature exceeds the threshold. If it does, then it forwards the message through its output queue. If not, then it ignores the message: 

```
`static unsigned char *bytearray_to_str(const unsigned char *buffer, size_t len)
{
    unsigned char *ret = (unsigned char *)malloc(len + 1);
    memcpy(ret, buffer, len);
    ret[len] = '\0';
    return ret;
}

static IOTHUBMESSAGE_DISPOSITION_RESULT InputQueue1Callback(IOTHUB_MESSAGE_HANDLE message, void* userContextCallback)
{
    IOTHUBMESSAGE_DISPOSITION_RESULT result;
    IOTHUB_CLIENT_RESULT clientResult;
    IOTHUB_MODULE_CLIENT_LL_HANDLE iotHubModuleClientHandle = (IOTHUB_MODULE_CLIENT_LL_HANDLE)userContextCallback;

    unsigned const char* messageBody;
    size_t contentSize;

    if (IoTHubMessage_GetByteArray(message, &messageBody, &contentSize) == IOTHUB_MESSAGE_OK)
    {
        messageBody = bytearray_to_str(messageBody, contentSize);
    } else
    {
        messageBody = "<null>";
    }

    printf("Received Message [%zu]\r\n Data: [%s]\r\n",
            messagesReceivedByInput1Queue, messageBody);

    // Check if the message reports temperatures higher than the threshold
    JSON_Value *root_value = json_parse_string(messageBody);
    JSON_Object *root_object = json_value_get_object(root_value);
    double temperature;
    if (json_object_dotget_value(root_object, "machine.temperature") != NULL && (temperature = json_object_dotget_number(root_object, "machine.temperature")) > temperatureThreshold)
    {
        printf("Machine temperature %f exceeds threshold %f\r\n", temperature, temperatureThreshold);
        // This message should be sent to next stop in the pipeline, namely "output1".  What happens at "output1" is determined
        // by the configuration of the Edge routing table setup.
        MESSAGE_INSTANCE *messageInstance = CreateMessageInstance(message);
        if (NULL == messageInstance)
        {
            result = IOTHUBMESSAGE_ABANDONED;
        }
        else
        {
            printf("Sending message (%zu) to the next stage in pipeline\n", messagesReceivedByInput1Queue);

            clientResult = IoTHubModuleClient_LL_SendEventToOutputAsync(iotHubModuleClientHandle, messageInstance->messageHandle, "output1", SendConfirmationCallback, (void *)messageInstance);
            if (clientResult != IOTHUB_CLIENT_OK)
            {
                IoTHubMessage_Destroy(messageInstance->messageHandle);
                free(messageInstance);
                printf("IoTHubModuleClient_LL_SendEventToOutputAsync failed on sending msg#=%zu, err=%d\n", messagesReceivedByInput1Queue, clientResult);
                result = IOTHUBMESSAGE_ABANDONED;
            }
            else
            {
                result = IOTHUBMESSAGE_ACCEPTED;
            }
        }
    }
    else
    {
        printf("Not sending message (%zu) to the next stage in pipeline.\r\n", messagesReceivedByInput1Queue);
        result = IOTHUBMESSAGE_ACCEPTED;
    }

    messagesReceivedByInput1Queue++;
    return result;
} `
```

- 
Add a `moduleTwinCallback `function. This method receives updates on the desired properties from the module twin, and updates the `temperatureThreshold `variable to match. All modules have their own module twin, which lets you configure the code running inside a module directly from the cloud: 

```
`static void moduleTwinCallback(DEVICE_TWIN_UPDATE_STATE update_state, const unsigned char* payLoad, size_t size, void* userContextCallback)
{
    printf("\r\nTwin callback called with (state=%s, size=%zu):\r\n%s\r\n",
        MU_ENUM_TO_STRING(DEVICE_TWIN_UPDATE_STATE, update_state), size, payLoad);
    JSON_Value *root_value = json_parse_string(payLoad);
    JSON_Object *root_object = json_value_get_object(root_value);
    if (json_object_dotget_value(root_object, "desired.TemperatureThreshold") != NULL) {
        temperatureThreshold = json_object_dotget_number(root_object, "desired.TemperatureThreshold");
    }
    if (json_object_get_value(root_object, "TemperatureThreshold") != NULL) {
        temperatureThreshold = json_object_get_number(root_object, "TemperatureThreshold");
    }
} `
```

- 
Find the `SetupCallbacksForModule `function. Replace the function with the following code that adds an `else if `statement to check if the module twin is updated: 

```
`static int SetupCallbacksForModule(IOTHUB_MODULE_CLIENT_LL_HANDLE iotHubModuleClientHandle)
{
    int ret;

    if (IoTHubModuleClient_LL_SetInputMessageCallback(iotHubModuleClientHandle, "input1", InputQueue1Callback, (void*)iotHubModuleClientHandle) != IOTHUB_CLIENT_OK)
    {
        printf("ERROR: IoTHubModuleClient_LL_SetInputMessageCallback(\"input1\")..........FAILED!\r\n");
        ret = MU_FAILURE;
    }
    else if (IoTHubModuleClient_LL_SetModuleTwinCallback(iotHubModuleClientHandle, moduleTwinCallback, (void*)iotHubModuleClientHandle) != IOTHUB_CLIENT_OK)
    {
        printf("ERROR: IoTHubModuleClient_LL_SetModuleTwinCallback(default)..........FAILED!\r\n");
        ret = MU_FAILURE;
    }
    else
    {
        ret = 0;
    }

    return ret;
} `
```

- 
Save the **main.c **file. 

- 
In the Visual Studio Code explorer, open the **deployment.template.json **file in your IoT Edge solution workspace. 

- 
Add the **filtermodule **module twin to the deployment manifest. Insert the following JSON content at the bottom of the `moduleContent `section, after the `$edgeHub `module twin: 

```
`"filtermodule": {
    "properties.desired":{
        "TemperatureThreshold":25
    }
} `
```

- 
Save the **deployment.template.json **file. 

- 
In the Visual Studio Code explorer, open **modules > filtermodule > src > main > java > com > edgemodule > App.java **. 

- 
Add the following code at the top of the file to import new referenced classes. 

```
`import java.io.StringReader;
import java.util.concurrent.atomic.AtomicLong;
import java.util.HashMap;
import java.util.Map;

import javax.json.Json;
import javax.json.JsonObject;
import javax.json.JsonReader;

import com.microsoft.azure.sdk.iot.device.DeviceTwin.Pair;
import com.microsoft.azure.sdk.iot.device.DeviceTwin.Property;
import com.microsoft.azure.sdk.iot.device.DeviceTwin.TwinPropertyCallBack; `
```

- 
Add the following definition into the `App `class. This variable sets a temperature threshold. The measured machine temperature isn't reported to IoT Hub until it exceeds this value: 

```
`private static final String TEMP_THRESHOLD = "TemperatureThreshold";
private static AtomicLong tempThreshold = new AtomicLong(25); `
```

- 
Replace the execute method of `MessageCallbackMqtt `with the following code. This method is called whenever the module receives an MQTT message from the IoT Edge hub. It filters out messages that report temperatures below the temperature threshold set via the module twin: 

```
`protected static class MessageCallbackMqtt implements MessageCallback {
    private int counter = 0;
    @Override
    public IotHubMessageResult execute(Message msg, Object context) {
        this.counter += 1;

        String msgString = new String(msg.getBytes(), Message.DEFAULT_IOTHUB_MESSAGE_CHARSET);
        System.out.println(
               String.format("Received message %d: %s",
                        this.counter, msgString));
        if (context instanceof ModuleClient) {
            try (JsonReader jsonReader = Json.createReader(new StringReader(msgString))) {
                final JsonObject msgObject = jsonReader.readObject();
                double temperature = msgObject.getJsonObject("machine").getJsonNumber("temperature").doubleValue();
                long threshold = App.tempThreshold.get();
                if (temperature >= threshold) {
                    ModuleClient client = (ModuleClient) context;
                    System.out.println(
                        String.format("Temperature above threshold %d. Sending message: %s",
                        threshold, msgString));
                    client.sendEventAsync(msg, eventCallback, msg, App.OUTPUT_NAME);
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        return IotHubMessageResult.COMPLETE;
    }
} `
```

- 
Add the following two static inner classes into the `App `class. These classes update the `tempThreshold `variable when the module twin's desired property changes. All modules have their own module twin, which lets you configure the code that's running inside a module directly from the cloud: 

```
`protected static class DeviceTwinStatusCallBack implements IotHubEventCallback {
    @Override
    public void execute(IotHubStatusCode status, Object context) {
        System.out.println("IoT Hub responded to device twin operation with status " + status.name());
    }
}

protected static class OnProperty implements TwinPropertyCallBack {
    @Override
    public void TwinPropertyCallBack(Property property, Object context) {
        if (!property.getIsReported()) {
            if (property.getKey().equals(App.TEMP_THRESHOLD)) {
                try {
                    long threshold = Math.round((double) property.getValue());
                    App.tempThreshold.set(threshold);
                } catch (Exception e) {
                    System.out.println("Failed to set TemperatureThread with exception");
                    e.printStackTrace();
                }
            }
        }
    }
} `
```

- 
Add the following lines to the `main `method after `client.open() `to subscribe the module twin updates: 

```
`client.startTwin(new DeviceTwinStatusCallBack(), null, new OnProperty(), null);
Map<Property, Pair<TwinPropertyCallBack, Object>> onDesiredPropertyChange = new HashMap<Property, Pair<TwinPropertyCallBack, Object>>() {
    {
        put(new Property(App.TEMP_THRESHOLD, null), new Pair<TwinPropertyCallBack, Object>(new OnProperty(), null));
    }
};
client.subscribeToTwinDesiredProperties(onDesiredPropertyChange);
client.getTwin(); `
```

- 
Save the **App.java **file. 

- 
In the Visual Studio Code explorer, open the **deployment.template.json **file in your IoT Edge solution workspace. 

- 
Add the **filtermodule **module twin to the deployment manifest. Insert the following JSON content at the bottom of the `moduleContent `section, after the **$edgeHub **module twin: 

```
`"filtermodule": {
      "properties.desired":{
          "TemperatureThreshold":25
      }
  } `
```

- 
Save the **deployment.template.json **file. 

- 
In the Visual Studio Code explorer, open **modules > filtermodule > app.js **. 

- 
Add a temperature threshold variable to the beginning of **app.js **. The temperature threshold sets the value that the measured temperature must exceed in order for the data to be sent to IoT Hub: 

```
`var temperatureThreshold = 25; `
```

- 
Replace the entire `PipeMessage `function with the `FilterMessage `function. 

```
`// This function filters out messages that report temperatures below the temperature threshold.
// It also adds the MessageType property to the message with the value set to Alert.
function filterMessage(client, inputName, msg) {
    client.complete(msg, printResultFor('Receiving message'));
    if (inputName === 'input1') {
        var message = msg.getBytes().toString('utf8');
        var messageBody = JSON.parse(message);
        if (messageBody && messageBody.machine && messageBody.machine.temperature && messageBody.machine.temperature > temperatureThreshold) {
            console.log(`Machine temperature ${messageBody.machine.temperature} exceeds threshold ${temperatureThreshold}`);
            var outputMsg = new Message(message);
            outputMsg.properties.add('MessageType', 'Alert');
            client.sendOutputEvent('output1', outputMsg, printResultFor('Sending received message'));
        }
    }
} `
```

- 
Replace the function name `pipeMessage `with `filterMessage `in the `client.on() `call: 

```
`client.on('inputMessage', function (inputName, msg) {
    filterMessage(client, inputName, msg);
    }); `
```

- 
Copy the following code into the `client.open() `function callback, after `client.on() `inside the `else `statement. This function is invoked when the desired properties are updated: 

```
`client.getTwin(function (err, twin) {
    if (err) {
        console.error('Error getting twin: ' + err.message);
    } else {
        twin.on('properties.desired', function(delta) {
            if (delta.TemperatureThreshold) {
                temperatureThreshold = delta.TemperatureThreshold;
            }
        });
    }
}); `
```

- 
Save the **app.js **file. 

- 
In the Visual Studio Code explorer, open the **deployment.template.json **file in your IoT Edge solution workspace. 

- 
Add the **filtermodule **module twin to the deployment manifest. Insert the following JSON content at the bottom of the `moduleContent `section, after the `$edgeHub `module twin: 

```
`"filtermodule": {
      "properties.desired":{
          "TemperatureThreshold":25
      }
  } `
```

- 
Save the **deployment.template.json **file. 

In this section, add the code that expands the **filtermodule **to analyze the messages before sending them. You add code that filters messages where the reported machine temperature is within the acceptable limits. 

- 
In the Visual Studio Code explorer, open **modules > filtermodule > main.py **. 

- 
At the top of the **main.py **file, import the **json **library: 

```
`import json `
```

- 
Add global definitions for the **TEMPERATURE_THRESHOLD **, **RECEIVED_MESSAGES **and **TWIN_CALLBACKS **variables. The temperature threshold sets the value that the measured machine temperature must exceed for the data to be sent to the IoT Hub: 

```
`# global counters
TEMPERATURE_THRESHOLD = 25
TWIN_CALLBACKS = 0
RECEIVED_MESSAGES = 0 `
```

- 
Replace the `create_client `function with the following code: 

```
`def create_client():
    client = IoTHubModuleClient.create_from_edge_environment()

    # Define function for handling received messages
    async def receive_message_handler(message):
        global RECEIVED_MESSAGES
        print("Message received")
        size = len(message.data)
        message_text = message.data.decode('utf-8')
        print("    Data: <<<{data}>>> & Size={size}".format(data=message.data, size=size))
        print("    Properties: {}".format(message.custom_properties))
        RECEIVED_MESSAGES += 1
        print("Total messages received: {}".format(RECEIVED_MESSAGES))

        if message.input_name == "input1":
            message_json = json.loads(message_text)
            if "machine" in message_json and "temperature" in message_json["machine"] and message_json["machine"]["temperature"] > TEMPERATURE_THRESHOLD:
                message.custom_properties["MessageType"] = "Alert"
                print("ALERT: Machine temperature {temp} exceeds threshold {threshold}".format(
                    temp=message_json["machine"]["temperature"], threshold=TEMPERATURE_THRESHOLD
                ))
                await client.send_message_to_output(message, "output1")

    # Define function for handling received twin patches
    async def receive_twin_patch_handler(twin_patch):
        global TEMPERATURE_THRESHOLD
        global TWIN_CALLBACKS
        print("Twin Patch received")
        print("     {}".format(twin_patch))
        if "TemperatureThreshold" in twin_patch:
            TEMPERATURE_THRESHOLD = twin_patch["TemperatureThreshold"]
        TWIN_CALLBACKS += 1
        print("Total calls confirmed: {}".format(TWIN_CALLBACKS))

    try:
        # Set handler on the client
        client.on_message_received = receive_message_handler
        client.on_twin_desired_properties_patch_received = receive_twin_patch_handler
    except:
        # Cleanup if failure occurs
        client.shutdown()
        raise

    return client `
```

- 
Save the **main.py **file. 

- 
In the Visual Studio Code explorer, open the **deployment.template.json **file in your IoT Edge solution workspace. 

- 
Add the **filtermodule **module twin to the deployment manifest. Insert the following JSON content at the bottom of the `modulesContent `section, after the **$edgeHub **module twin: 

```
`"filtermodule": {
        "properties.desired":{
            "TemperatureThreshold":25
        }
    } `
```

- 
Save the **deployment.template.json **file. 

## Build and push your solution 

You updated the module code and the deployment template to help understand some key deployment concepts. Now, you're ready to build your module container image and push it to your container registry. 

In Visual Studio Code, open the **deployment.template.json **deployment manifest file. The [deployment manifest ]describes the modules to be configured on the targeted IoT Edge device. Before deployment, you must update your Azure Container Registry credentials and your module images with the proper `createOptions `values. For more information about `createOptions `values, see [How to configure container create options for IoT Edge modules ]. 

If you use an Azure Container Registry to store your module image, add your credentials to the `modulesContent > edgeAgent > settings > registryCredentials `section in **deployment.template.json **. Replace `myacr `with your own registry name and provide your password and login server address. For example: 

```
`"registryCredentials": {
    "myacr": {
        "username": "myacr",
        "password": "<your_acr_password>",
        "address": "myacr.azurecr.io"
    }
} `
```

Add or replace the following stringified content to the `createOptions `value for each system ( **edgeHub **and * **edgeAgent **) and custom module ( **filtermodule **and **tempSensor **) listed. Change the values if necessary: 

```
`"createOptions": "{\"HostConfig\":{\"PortBindings\":{\"5671/tcp\":[{\"HostPort\":\"5671\"}],\"8883/tcp\":[{\"HostPort\":\"8883\"}],\"443/tcp\":[{\"HostPort\":\"443\"}]}}}" `
```

For example, the `filtermodule `configuration should be similar to: 

```
`"filtermodule": {
"version": "1.0",
"type": "docker",
"status": "running",
"restartPolicy": "always",
"settings": {
   "image": "myacr.azurecr.io/filtermodule:0.0.1-amd64",
   "createOptions": "{\"HostConfig\":{\"PortBindings\":{\"5671/tcp\":[{\"HostPort\":\"5671\"}],\"8883/tcp\":[{\"HostPort\":\"8883\"}],\"443/tcp\":[{\"HostPort\":\"443\"}]}}}"
} `
```

#### Build module Docker image 

Open the Visual Studio Code integrated terminal by selecting **Terminal > New Terminal **. 

- [C# ]

- [C, Java, Node.js, Python ]

Use the `dotnet publish `command to build the container image for Linux and amd64 architecture. Change directory to the **filtermodule **directory in your project and run the `dotnet publish `command. 

```
`dotnet publish --os linux --arch x64 /t:PublishContainer `
```

Currently, the **iotedgedev **tool template targets .NET 7.0. If you want to target a different version of .NET, you can edit the **filtermodule.csproj **file and change the `TargetFramework `and `PackageReference `values. For example to target .NET 8.0, your **filtermodule.csproj **file should look like this: 

```
`<Project Sdk="Microsoft.NET.Sdk.Worker">
    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <Nullable>enable</Nullable>
        <ImplicitUsings>enable</ImplicitUsings>
    </PropertyGroup>
    <ItemGroup>
        <PackageReference Include="Microsoft.Azure.Devices.Client" Version="1.42.0" />
        <PackageReference Include="Microsoft.Extensions.Hosting" Version="8.0.0" />
    </ItemGroup>
</Project> `
```

Tag the docker image with your container registry information, version, and architecture. Replace `myacr `with your own registry name: 

```
`docker tag filtermodule myacr.azurecr.io/filtermodule:0.0.1-amd64 `
```

Use the module's Dockerfile to [build ]and tag the module Docker image: 

```
`docker build --rm -f "<DockerFilePath>" -t <ImageNameAndTag> "<ContextPath>" `
```

For example, to build the image for the local registry or an Azure container registry, run the following commands: 

```
`# Build and tag the image for the local registry

docker build --rm -f "./modules/filtermodule/Dockerfile.amd64.debug" -t localhost:5000/filtermodule:0.0.1-amd64 "./modules/filtermodule"

# Or build and tag the image for an Azure Container Registry. Replace myacr with your own registry name.

docker build --rm -f "./modules/filtermodule/Dockerfile.amd64.debug" -t myacr.azurecr.io/filtermodule:0.0.1-amd64 "./modules/filtermodule" `
```

#### Push module Docker image 

Provide your container registry credentials to Docker so that it can push your container image to storage in the registry. 

- 
Sign in to Docker with the Azure Container Registry (ACR) credentials: 

```
`docker login -u <ACR username> -p <ACR password> <ACR login server> `
```

You might receive a security warning recommending the use of `--password-stdin `. While that's a recommended best practice for production scenarios, it's outside the scope of this tutorial. For more information, see the [docker login ]reference. 

- 
Sign in to the Azure Container Registry. You must [install Azure CLI ]to use the `az `command. This command asks for your user name and password found in your container registry in **Settings > Access keys **: 

```
`az acr login -n <ACR registry name> `
```

Tip 

If you are logged out at any point in this tutorial, repeat the Docker and Azure Container Registry sign-in steps to continue. 

- 
[Push ]your module image to the local registry or a container registry: 

```
`docker push <ImageName> `
```

For example: 

```
`# Push the Docker image to the local registry

docker push localhost:5000/filtermodule:0.0.1-amd64

# Or push the Docker image to an Azure Container Registry. Replace myacr with your Azure Container Registry name.

az acr login --name myacr
docker push myacr.azurecr.io/filtermodule:0.0.1-amd64 `
```

#### Update the deployment template 

Update the deployment template **deployment.template.json **with the container registry image location. For example, if you're using an Azure Container Registry **myacr.azurecr.io **and your image is **filtermodule:0.0.1-amd64 **, update the `filtermodule `configuration to: 

```
`"filtermodule": {
    "version": "1.0",
    "type": "docker",
    "status": "running",
    "restartPolicy": "always",
    "settings": {
        "image": "myacr.azurecr.io/filtermodule:0.0.1-amd64",
        "createOptions": "{\"HostConfig\":{\"PortBindings\":{\"5671/tcp\":[{\"HostPort\":\"5671\"}],\"8883/tcp\":[{\"HostPort\":\"8883\"}],\"443/tcp\":[{\"HostPort\":\"443\"}]}}}"
    }
} `
```

In the Visual Studio Code explorer, right-click the **deployment.template.json **file and select **Build and Push IoT Edge Solution **. 

The build and push command starts three operations. First, it creates a new folder in the solution called **config **that holds the full deployment manifest, built out of information in the deployment template and other solution files. Second, it runs `docker build `to build the container image based on the appropriate dockerfile for your target architecture. Then, it runs `docker push `to push the image repository to your container registry. 

This process might take several minutes the first time, but it's faster the next time you run the commands. 

#### Optional: Update the module and image 

If you make changes to your module code, you must rebuild and push the module image to your container registry. Use the steps in this section to update the build and container image. You can skip this section if you didn't make any changes to your module code. 

Open the **deployment.amd64.json **file in newly created config folder. The filename reflects the target architecture, so it's different if you chose a different architecture. 

Notice that the two parameters that had placeholders now contain their proper values. The `registryCredentials `section has your registry username and password pulled from the **.env **file. The `filtermodule `has the full image repository with the name, version, and architecture tag from the **module.json **file. 

- 
Open the **module.json **file in the **filtermodule **folder. 

- 
Change the version number for the module image. For example, increment the patch version number to `"version": "0.0.2" `as if you made a small fix in the module code. 

Tip 

Module versions enable version control, and allow you to test changes on a small set of devices before you deploy updates to production. If you don't increment the module version before building and pushing, then you overwrite the repository in your container registry. 

- 
Save your changes to the **module.json **file. 

Build and push the updated image with a **0.0.2 **version tag. For example, to build and push the image for the local registry or an Azure container registry, use the following commands: 

- [C# ]

- [C, Java, Node.js, Python ]

```
`# Build the container image for Linux and amd64 architecture.

dotnet publish --os linux --arch x64

# For local registry:
# Tag the image with version 0.0.2, x64 architecture, and the local registry.

docker tag filtermodule localhost:5000/filtermodule:0.0.2-amd64

# For Azure Container Registry:
# Tag the image with version 0.0.2, x64 architecture, and your container registry information. Replace **myacr** with your own registry name.

docker tag filtermodule myacr.azurecr.io/filtermodule:0.0.2-amd64 `
```

```
`# Build and push the 0.0.2 image for the local registry

docker build --rm -f "./modules/filtermodule/Dockerfile.amd64.debug" -t localhost:5000/filtermodule:0.0.2-amd64 "./modules/filtermodule"

docker push localhost:5000/filtermodule:0.0.2-amd64

# Or build and push the 0.0.2 image for an Azure Container Registry. Replace myacr with your own registry name.

docker build --rm -f "./modules/filtermodule/Dockerfile.amd64.debug" -t myacr.azurecr.io/filtermodule:0.0.2-amd64 "./modules/filtermodule"

docker push myacr.azurecr.io/filtermodule:0.0.2-amd64 `
```

Right-click the **deployment.template.json **file again, and select **Build and Push IoT Edge Solution **again. 

Open the **deployment.amd64.json **file again. Notice the build system doesn't create a new file when you run the build and push command again. Rather, the same file updates to reflect the changes. The **filtermodule **image now points to the 0.0.2 version of the container. 

To further verify what the build and push command did, go to the [Azure portal ]and navigate to your container registry. In your container registry, select **Repositories **then **filtermodule **. Verify that both versions of the image push to the registry. 

[]

### Troubleshoot 

If you encounter errors when building and pushing your module image, it often has to do with Docker configuration on your development machine. Use the following checks to review your configuration: 

- Did you run the `docker login `command using the credentials that you copied from your container registry? These credentials are different than the ones that you use to sign in to Azure. 

- Is your container repository correct? Does it have your correct container registry name and your correct module name? Open the **module.json **file in the **filtermodule **folder to check. The repository value should be similar to **<registry name>.azurecr.io/filtermodule **. 

- If you used a different name than **filtermodule **for your module, is that name consistent throughout the solution? 

- Is your machine running the same type of containers that you're building? This tutorial is for Linux IoT Edge devices, so Visual Studio Code should say **amd64 **or **arm32v7 **in the side bar, and Docker Desktop should be running Linux containers. 

## Deploy modules to device 

You verified that there are built container images stored in your container registry, so it's time to deploy them to a device. Make sure that your IoT Edge device is up and running. 

Use the IoT Edge Azure [CLI set-modules ]command to deploy the modules to the Azure IoT Hub. For example, to deploy the modules defined in the **deployment.template.json **file to the IoT Hub **my-iot-hub **for the IoT Edge device **my-device **, use the following command. Replace the **hub-name **, **device-id **, and **login **IoT Hub connection string values with your own. 

```
`az iot edge set-modules --hub-name my-iot-hub --device-id my-device --content ./deployment.template.json --login "HostName=my-iot-hub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=<SharedAccessKey>" `
```

Tip 

Find your IoT Hub connection string, including the shared access key, in the Azure portal. Go to your IoT Hub, and select **Security settings > Shared access policies > iothubowner **. 

- 
In the Visual Studio Code explorer, under the **Azure IoT Hub **section, expand **Devices **to see your list of IoT devices. 

- 
Right-click the IoT Edge device that you want to deploy to, then select **Create Deployment for Single Device **. 

- 
In the file explorer, navigate into the **config **folder then select the **deployment.amd64.json **file. 

Don't use the deployment.template.json file, which doesn't have the container registry credentials or module image values in it. If you target a Linux ARM32 device, the deployment manifest's name is **deployment.arm32v7.json **. 

- 
Under your device, expand **Modules **to see a list of deployed and running modules. Select the refresh button. You should see the new **tempSensor **and **filtermodule **modules running on your device. 

It can take a few minutes for the modules to start. The IoT Edge runtime receives its new deployment manifest, pulls down the module images from the container runtime, then starts each new module. 

## View messages from device 

The sample module code gets messages through its input queue and sends them through its output queue. The deployment manifest sets up routes that send messages to **filtermodule **from **tempSensor **, and then forward messages from **filtermodule **to IoT Hub. The Azure IoT Edge and Azure IoT Hub extensions let you see messages as they arrive at IoT Hub from your device. 

- 
In the Visual Studio Code explorer, select the IoT Edge device you want to monitor, then select **Start Monitoring Built-in Event Endpoint **. 

- 
Watch the output window in Visual Studio Code to see messages arrive at your IoT Hub. 

## View changes on device 

To see what's happening on your device, use the commands in this section to inspect the IoT Edge runtime and modules running on your device. 

These commands are for your IoT Edge device, not your development machine. If you're using a virtual machine for your IoT Edge device, connect to it now. In Azure, go to the virtual machine's overview page and select **Connect **to access the secure shell connection. 

- 
View all modules deployed to your device, and check their status: 

```
`iotedge list `
```

You see four modules: the two IoT Edge runtime modules, **tempSensor **, and **filtermodule **. All four should be listed as running. 

- 
Inspect the logs for a specific module: 

```
`iotedge logs <module name> `
```

Module names are case-sensitive. 

The **tempSensor **and **filtermodule **logs show the messages they're processing. The **edgeAgent **module starts the other modules, so its logs have information about the deployment manifest. If a module isn't listed or isn't running, check the edgeAgent logs for errors. The **edgeHub **module manages communication between the modules and IoT Hub. If the modules are running but messages aren't arriving at your IoT Hub, check the **edgeHub **logs for errors. 

## Clean up resources 

If you want to continue to the next recommended article, keep the resources and configurations you created and reuse them. You can also keep using the same IoT Edge device as a test device. Otherwise, to avoid charges, delete the local configuration and the Azure resources you used in this article. 

### Delete Azure resources 

Deleting Azure resources and resource groups is irreversible. Make sure that you don't accidentally delete the wrong resource group or resources. If you created the IoT Hub inside an existing resource group that has resources that you want to keep, delete only the IoT Hub resource itself, not the resource group. 

To delete the resources: 

- Sign in to the [Azure portal ], and then select **Resource groups **. 

- Select the name of the resource group that contains your IoT Edge test resources. 

- Review the list of resources that your resource group contains. If you want to delete all of them, you can select **Delete resource group **. If you want to delete only some of them, you can select each resource to delete them individually. 

## Next steps 

In this tutorial, you set up Visual Studio Code on your development machine and deploy your first IoT Edge module with code that filters raw data generated by your IoT Edge device. 

Continue to the next tutorials to learn how Azure IoT Edge lets you deploy Azure cloud services to process and analyze data at the edge. 

[Debug Azure IoT Edge modules ][Functions ][Stream Analytics ][Custom Vision Service ]

## Feedback 

Was this page helpful? 
Yes No No 
Need help with this topic? 

Want to try using Ask Learn to clarify or guide you through this topic? 
Ask Learn Ask Learn Suggest a fix? 
## Additional resources 

- Last updated on 2025-11-03 

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