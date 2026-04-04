# Source: https://kreya.app/docs/getting-started.md

# Getting Started

Follow these steps to call your first API using Kreya.

## Download and install Kreya[​](#download-and-install-kreya "Direct link to Download and install Kreya")

You can download Kreya by visiting the [download page](/downloads.md).

* macOS
* Windows
* Linux

Download the dmg file and open it. Drag the `Kreya.app` file into your Applications folder.

Download the MSI file and run it, which should automatically install Kreya. Should you receive a Windows Defender Smart Screen warning, click on "More info" and then "Run anyway". This may happen because Windows doesn't trust the Kreya code signature enough yet.

*Kreya uses [Microsoft Edge WebView2](https://docs.microsoft.com/en-us/microsoft-edge/webview2/), which will be installed when you run the MSI (if it is not already installed).*

The simplest option to install Kreya on Linux is via Snapcraft. Head over to <https://snapcraft.io/kreya>, select your Linux distribution and follow the guide.

Alternatively, you may install Kreya by downloading the tarball. Note that both `libgtk-4-1` and `libwebkitgtk-6.0-4` dependencies are required. Install them manually if they aren't present on your system.

## Using the example project[​](#using-the-example-project "Direct link to Using the example project")

If you just want to try Kreya a bit, the example project is a good start.

![The initial launch screen](/assets/ideal-img/launch-screen.41c7606.400.png)

To send your first request, select an operation in the list and simply hit 'Send'. That's it! You already made your first API call with Kreya.

![Sending a request with the example project](/assets/ideal-img/send-request-example-project.51d6b47.400.png)

## Manually creating a project[​](#manually-creating-a-project "Direct link to Manually creating a project")

If you want to create your own project, launch Kreya and click the `Create project...` button, after which you will see the following dialog:

![The create project dialog](/assets/ideal-img/create-project.cd67466.400.png)

1. Since Kreya is file-based, you need to select a location for the Kreya project.
2. Choose a name for your project.
3. Enter the directory name. It will be created inside the directory you chose in step 1. All project files will be stored inside this directory.
4. Ensure that the full path of the project matches your intentions.
5. By clicking `Create`, Kreya creates and opens the project.

### For gRPC: Adding protobuf definitions[​](#for-grpc-adding-protobuf-definitions "Direct link to For gRPC: Adding protobuf definitions")

If you to use gRPC, select "gRPC" in the first step.

To create gRPC requests, you need to add protobuf definitions, otherwise Kreya cannot know the available services and request/response types. You can do this via the initial project setup screen or later by adding an [Importer](/docs/importers.md) if you choose to skip this step.

![Adding a gRPC importer via the initial project setup](/assets/ideal-img/initial-grpc-project-setup.3647b8e.400.png)

Select an importer type, enter the necessary information and click 'Next'. If you want to try Kreya and you don't have any protobuf files at hand, enter `https://example-api.kreya.app:9090`. Kreya will automatically generate an operation for each service method of your gRPC service.

In the following screen, enter the API URL which will be prefilled for all operations.

### For GraphQL: Adding GraphQL schemas[​](#for-graphql-adding-graphql-schemas "Direct link to For GraphQL: Adding GraphQL schemas")

If you do not want to use GraphQL or do not have a GraphQL schema or introspectable endpoint at hand, skip this step. You can always add an [Importer](/docs/importers.md) later on.

![Adding a GraphQL schema importer via the initial project setup](/assets/ideal-img/initial-graphql-project-setup.4ce1a26.400.png)

Select an importer type, enter the necessary information and click 'Next'. If you want to try Kreya and you don't have any GraphQL schemas at hand, select `GraphQL schema introspection` importer and enter `https://example-api.kreya.app/graphql` as the endpoint. Kreya will automatically introspect your GraphQL schema and provide autocomplete for queries, mutations and subscriptions.

In the following screen, enter the API URL which will be prefilled for all operations.

### For REST: Adding OpenAPI definitions[​](#for-rest-adding-openapi-definitions "Direct link to For REST: Adding OpenAPI definitions")

If you do not want to use REST or do not have an OpenAPI definition at hand, skip this step. You can always add an [Importer](/docs/importers.md) later on.

![Adding a REST importer via the initial project setup](/assets/ideal-img/initial-rest-project-setup.789e79a.400.png)

Select an importer type, enter the necessary information and click 'Next'. If you want to try Kreya and you don't have any OpenAPI definitions at hand, enter `https://example-api.kreya.app/swagger/v1/swagger.json`. Kreya will automatically generate operations for your REST service.

In the following screen, enter the API URL which will be prefilled for all operations.

### Sending your first request[​](#sending-your-first-request "Direct link to Sending your first request")

All done! If necessary, click on the settings tab and enter your service URL in the `Endpoint` input field. Then, send your first operation by clicking on the 'Send' button.

![Operation with a selected settings tab and a filled endpoint field](/assets/ideal-img/entering-endpoint.980006a.400.png)

## Good to know[​](#good-to-know "Direct link to Good to know")

Kreya has a range of features that make your life easier. Be sure to try out the [Environment](/docs/environments.md), [Authentication](/docs/authentication.md), [Default Settings](/docs/default-settings.md) and all the other features!
