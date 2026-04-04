# Source: https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite

Title: Install and run the Azurite emulator for Azure Storage

URL Source: https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite

Markdown Content:
Using the Azurite emulator allows developers to fast-track cloud-based application and tool development without the need for internet connectivity.

This article provides instructions for installing and running Azurite, as well as configuring it for local development. For more information about using Azurite, see [Use the Azurite emulator for local Azure Storage development](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite).

Azurite supersedes the [Azure Storage Emulator](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-emulator), and continues to be updated to support the latest versions of Azure Storage APIs.

Azurite can be installed and run using various methods, including npm, Docker, and Visual Studio Code. This video shows you how to install and run the Azurite emulator.

The steps in the video are also described in the following sections. Select any of these tabs to view specific instructions relevant to your environment.

*   [Visual Studio](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#tabpanel_1_visual-studio-code)
*   [npm](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#tabpanel_1_npm)
*   [Docker Hub](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#tabpanel_1_docker-hub)
*   [GitHub](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#tabpanel_1_github)

Azurite is automatically available with [Visual Studio 2022](https://visualstudio.microsoft.com/vs/). The Azurite executable is updated as part of new Visual Studio version releases. If you're running an earlier version of Visual Studio, you can install Azurite by using either Node Package Manager (npm), DockerHub, or by cloning the Azurite GitHub repository.

Select any of the following tabs to view specific instructions relevant to your environment.

*   [Visual Studio](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#tabpanel_2_visual-studio-code)
*   [npm](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#tabpanel_2_npm)
*   [Docker Hub](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#tabpanel_2_docker-hub)
*   [GitHub](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#tabpanel_2_github)

To use Azurite with most project types in Visual Studio, you first need to run the Azurite executable. Once the executable is running, Azurite listens for connection requests from the application. To learn more, see [Running Azurite from the command line](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#running-azurite-from-the-command-line).

For **Azure Functions** projects and **ASP.NET** projects, you can choose to configure the project to start Azurite automatically. This configuration is done during the project setup. While this project configuration starts Azurite automatically, Visual Studio doesn't expose detailed Azurite configuration options. To customize detailed Azurite configuration options, [run the Azurite executable](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#running-azurite-from-the-command-line) before launching Visual Studio.

To learn more about configuring **Azure Functions** projects and **ASP.NET** projects to start Azurite automatically, see the following guidance:

*   [Running Azurite from an Azure Functions project](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#running-azurite-from-an-azure-functions-project)
*   [Running Azurite from an ASP.NET project](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#running-azurite-from-an-aspnet-project)

The following table shows the location of the Azurite executable for different versions of Visual Studio running on a Windows machine:

| Visual Studio version | Azurite executable location |
| --- | --- |
| Visual Studio Community 2022 | `C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\Extensions\Microsoft\Azure Storage Emulator` |
| Visual Studio Professional 2022 | `C:\Program Files\Microsoft Visual Studio\2022\Professional\Common7\IDE\Extensions\Microsoft\Azure Storage Emulator` |
| Visual Studio Enterprise 2022 | `C:\Program Files\Microsoft Visual Studio\2022\Enterprise\Common7\IDE\Extensions\Microsoft\Azure Storage Emulator` |

You can find the Azurite executable file in the extensions folder of your Visual Studio installation, as detailed in the [Azurite executable file location table](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#azurite-executable-file-location).

Navigate to the appropriate location and start `azurite.exe`. After you run the executable file, Azurite listens for connections.

[![Image 1: Screen capture of Azurite command-line output.](https://learn.microsoft.com/en-us/azure/storage/common/media/storage-use-azurite/azurite-command-line-output-visual-studio-sml.png)](https://learn.microsoft.com/en-us/azure/storage/common/media/storage-use-azurite/azurite-command-line-output-visual-studio.png#lightbox)

To learn more about available command line options to configure Azurite, see [Command line options](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#command-line-options).

In Visual Studio 2022, create an **Azure Functions** project. While setting the project options, mark the box labeled **Use Azurite for runtime storage account**.

[![Image 2: A screenshot showing how to set Azurite to be the runtime storage account for an Azure Functions project.](https://learn.microsoft.com/en-us/azure/storage/common/media/storage-use-azurite/azurite-azure-functions-sml.png)](https://learn.microsoft.com/en-us/azure/storage/common/media/storage-use-azurite/azurite-azure-functions.png#lightbox)

After you create the project, Azurite starts automatically. The location of the Azurite executable file is detailed in the [Azurite executable file location table](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#azurite-executable-file-location). The output looks similar to the following screenshot:

[![Image 3: A screenshot showing output after setting Azurite to be the runtime storage account for an Azure Functions project.](https://learn.microsoft.com/en-us/azure/storage/common/media/storage-use-azurite/azurite-azure-functions-output-sml.png)](https://learn.microsoft.com/en-us/azure/storage/common/media/storage-use-azurite/azurite-azure-functions-output.png#lightbox)

This configuration option can be changed later by modifying the project's **Connected Services** dependencies.

In Visual Studio 2022, create an **ASP.NET Core Web App** project. Then, open the **Connected Services** dialog box, select **Add a service dependency**, and then select **Storage Azurite emulator**.

[![Image 4: A screenshot showing how to add Azurite as a dependency to an ASP.NET project.](https://learn.microsoft.com/en-us/azure/storage/common/media/storage-use-azurite/azurite-aspnet-connect-sml.png)](https://learn.microsoft.com/en-us/azure/storage/common/media/storage-use-azurite/azurite-aspnet-connect.png#lightbox)

In the **Configure Storage Azurite emulator** dialog box, set the **Connection string name** field to `StorageConnectionString`, and then select **Finish**.

[![Image 5: A screenshot showing how to configure a connection string to use Azurite with an ASP.NET project.](https://learn.microsoft.com/en-us/azure/storage/common/media/storage-use-azurite/azurite-aspnet-connection-string-sml.png)](https://learn.microsoft.com/en-us/azure/storage/common/media/storage-use-azurite/azurite-aspnet-connection-string.png#lightbox)

When the configuration completes, select **Close**, and the Azurite emulator starts automatically. The location of the Azurite executable file is detailed in the [Azurite executable file location table](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#azurite-executable-file-location). The output looks similar to the following screenshot:

[![Image 6: A screenshot showing output after connecting an ASP.NET project to the Azurite emulator.](https://learn.microsoft.com/en-us/azure/storage/common/media/storage-use-azurite/azurite-aspnet-output.png)](https://learn.microsoft.com/en-us/azure/storage/common/media/storage-use-azurite/azurite-aspnet-output.png#lightbox)

This configuration option can be changed later by modifying the project's **Connected Services** dependencies.

This section details the command line switches available when launching Azurite.

**Optional** - Get command-line help by using the `-h` or `--help` switch.

```
azurite -h
azurite --help
```

*   [Blob Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#tabpanel_3_blob-storage)
*   [Queue Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#tabpanel_3_queue-storage)
*   [Table Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#tabpanel_3_table-storage)

**Optional** - By default, Azurite listens to 127.0.0.1 as the local server. Use the `--blobHost` switch to set the address to your requirements.

Accept requests on the local machine only:

```
azurite --blobHost 127.0.0.1
```

Allow remote requests:

```
azurite --blobHost 0.0.0.0
```

Caution

Allowing remote requests might make your system vulnerable to external attacks.

*   [Blob Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#tabpanel_4_blob-storage)
*   [Queue Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#tabpanel_4_queue-storage)
*   [Table Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#tabpanel_4_table-storage)

**Optional** - By default, Azurite listens for the Blob service on port 10000. Use the `--blobPort` switch to specify the listening port that you require.

Note

After using a customized port, you need to update the connection string or corresponding configuration in your Azure Storage tools or SDKs.

Customize the Blob service listening port:

```
azurite --blobPort 8888
```

Let the system auto select an available port:

```
azurite --blobPort 0
```

The port in use is displayed during Azurite startup.

**Optional** - Azurite stores data to the local disk during execution. Use the `-l` or `--location` switch to specify a path as the workspace location. By default, the current process working directory is used. Note the lowercase 'l'.

```
azurite -l c:\azurite
azurite --location c:\azurite
```

**Optional** - By default, the access log is displayed in the console window. Disable the display of the access log by using the `-s` or `--silent` switch.

```
azurite -s
azurite --silent
```

**Optional** - The debug log includes detailed information on every request and exception stack trace. Enable the debug log by providing a valid local file path to the `-d` or `--debug` switch.

```
azurite -d path/debug.log
azurite --debug path/debug.log
```

**Optional** - By default, Azurite applies strict mode to block unsupported request headers and parameters. Disable strict mode by using the `-L` or `--loose` switch. Note the capital 'L'.

```
azurite -L
azurite --loose
```

**Optional** - Display the installed Azurite version number by using the `-v` or `--version` switch.

```
azurite -v
azurite --version
```

**Optional** - By default, Azurite uses the HTTP protocol. You can enable HTTPS mode by providing a path to a Privacy Enhanced Mail (.pem) or [Personal Information Exchange (.pfx)](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/personal-information-exchange---pfx--files) certificate file to the `--cert` switch. HTTPS is required to connect to Azurite using [OAuth authentication](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite#oauth-configuration).

When `--cert` is provided for a PEM file, you must provide a corresponding `--key` switch.

```
azurite --cert path/server.pem --key path/key.pem
```

When `--cert` is provided for a PFX file, you must provide a corresponding `--pwd` switch.

```
azurite --cert path/server.pfx --pwd pfxpassword
```

For detailed information on generating PEM and PFX files, see [HTTPS Setup](https://github.com/Azure/Azurite/blob/master/README.md#https-setup).

**Optional** - Enable OAuth authentication for Azurite by using the `--oauth` switch.

```
azurite --oauth basic --cert path/server.pem --key path/key.pem
```

Note

OAuth requires an HTTPS endpoint. Make sure HTTPS is enabled by providing `--cert` switch along with the `--oauth` switch.

Azurite supports basic authentication by specifying the `basic` parameter to the `--oauth` switch. Azurite performs basic authentication, like validating the incoming bearer token, checking the issuer, audience, and expiry. Azurite doesn't check the token signature or permissions. To learn more about authorization, see [Connect to Azurite with SDKs and tools](https://learn.microsoft.com/en-us/azure/storage/common/storage-connect-azurite?toc=/azure/storage/blobs/toc.json&bc=/azure/storage/blobs/breadcrumb/toc.json).

**Optional** - When starting up, Azurite checks that the requested API version is valid. The following command skips the API version check:

```
azurite --skipApiVersionCheck
```

**Optional**. When you use the fully qualified domain name instead of the IP in request Uri host, Azurite parses the storage account name from request URI host by default. You can force the parsing of the storage account name from request URI path by using `--disableProductStyleUrl`:

```
azurite --disableProductStyleUrl
```

**Optional**. By default, blob and queue metadata is persisted to disk and content is persisted to extent files. Table storage persists all data to disk. You can disable persisting any data to disk and only store data in-memory. In the in-memory persistence scenario, if the Azurite process is terminated, all data is lost. The default persistence behavior can be overridden using the following option:

```
azurite --inMemoryPersistence
```

This setting is rejected when the SQL-based metadata implementation is enabled (via `AZURITE_DB`), or when the `--location` option is specified.

**Optional**. By default, the in-memory extent store (for blob and queue content) is limited to 50% of the total memory on the host machine. The total is evaluated using `os.totalmem()`. This limit can be overridden using the following option:

```
azurite --extentMemoryLimit <megabytes>
```

There's no restriction on the value specified for this option. However, virtual memory might be used if the limit exceeds the amount of available physical memory as provided by the operating system. A high limit might eventually lead to out of memory errors or reduced performance. This option is rejected when `--inMemoryPersistence` isn't specified.

To learn more, see [Use in-memory storage](https://github.com/Azure/Azurite#use-in-memory-storage).

**Optional**. By default, Azurite collects telemetry data to help improve the product. Use the `--disableTelemetry` option to disable telemetry data collection for the current Azurite execution, like following command:

```
azurite --disableTelemetry
```

*   [Connect to Azurite with SDKs and tools](https://learn.microsoft.com/en-us/azure/storage/common/storage-connect-azurite?toc=/azure/storage/blobs/toc.json&bc=/azure/storage/blobs/breadcrumb/toc.json) explains how to connect to Azurite using various Azure Storage SDKs and tools.
*   [Configure Azure Storage connection strings](https://learn.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string?toc=/azure/storage/blobs/toc.json&bc=/azure/storage/blobs/breadcrumb/toc.json) explains how to assemble a valid Azure Storage connection string.
*   [Use Azurite to run automated tests](https://learn.microsoft.com/en-us/azure/storage/blobs/use-azurite-to-run-automated-tests?toc=/azure/storage/blobs/toc.json&bc=/azure/storage/blobs/breadcrumb/toc.json) describes how to write automated tests using the Azurite storage emulator.
*   [Use the Azure Storage Emulator for development and testing](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-emulator?toc=/azure/storage/blobs/toc.json&bc=/azure/storage/blobs/breadcrumb/toc.json) documents the legacy Azure Storage Emulator, which is superseded by Azurite.
