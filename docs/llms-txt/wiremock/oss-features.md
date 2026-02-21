# Source: https://docs.wiremock.io/ide-integrations/jetbrains/oss-features.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Support for WireMock OSS

> Features supporting the OSS (non-WireMock Cloud) side of WireMock

## Create WireMock stubs

### Create basic WireMock stub from scratch

If a JSON file is placed in the **mappings** folder or contains the `"mappings"` key, the plugin recognizes it as a WireMock stub file and provides appropriate coding assistance.

1. In the **Project** tool window, right-click a folder (or press <kbd>⌘Сmd</kbd><kbd>N</kbd> or <kbd>Alt</kbd><kbd>Insert</kbd>) and select **New | File**.
2. In the **New File** dialog that opens, enter a name of the file. For example, you can enter `mappings/my-stub.json`, and the plugin will create the **mappings** folder and place the new file within it.
3. Start typing a key to get suggestions for applicable keys and their quick documentation.

<img src="https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/mappings_property_completion.png?fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=d244a1a9070d1a057bfb3e22f6a4e913" alt="WireMock Coding Assistance" data-og-width="1364" width="1364" data-og-height="836" height="836" data-path="images/ides/jetbrains/mappings_property_completion.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/mappings_property_completion.png?w=280&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=c7482549790dd20309aa922b1dd647a6 280w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/mappings_property_completion.png?w=560&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=f110c7d00096e947b477847287822bd7 560w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/mappings_property_completion.png?w=840&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=8da3e4006b717add4ca0f9fd86a0bf4e 840w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/mappings_property_completion.png?w=1100&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=5f91a59cbccd2869bde5eee0788250be 1100w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/mappings_property_completion.png?w=1650&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=713d35bfe03d255e2cebf475aeb092b1 1650w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/mappings_property_completion.png?w=2500&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=f3b9dd5aaf0b299af3a292462105030b 2500w" />

### Create WireMock stubs from Endpoints tool window

1. Open the **Endpoints** tool window (**View | Tool Windows | Endpoints**).
2. Right-click an endpoint and select **Generate WireMock Stubs**.

<img src="https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/generate_stubs_from_endpoints.png?fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=c4cdd73259c7fe7299fefe5778ced77e" width="550" alt="Creating WireMock stub from Endpoints" data-og-width="980" data-og-height="624" data-path="images/ides/jetbrains/generate_stubs_from_endpoints.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/generate_stubs_from_endpoints.png?w=280&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=4f8b4a516179d854fb4ab69eb6aab453 280w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/generate_stubs_from_endpoints.png?w=560&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=cf635b99bd641cf8a4769feb29588db2 560w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/generate_stubs_from_endpoints.png?w=840&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=6c6476e8962e88054ada7273d8f1be9a 840w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/generate_stubs_from_endpoints.png?w=1100&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=7ec7b88bfd7fd3123fc27fd79ffbd2ad 1100w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/generate_stubs_from_endpoints.png?w=1650&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=f359dac819733b465b1b8292869bcea7 1650w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/generate_stubs_from_endpoints.png?w=2500&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=28079e32d48ee2668041a2388e91e608 2500w" />

The new stub file is saved as a [scratch](https://www.jetbrains.com/help/idea/scratches.html) under **Scratches and Consoles | WireMock Stubs**.

### Create WireMock stubs from OpenAPI specification

1. Open an OpenAPI specification file.
2. Click <img src="https://resources.jetbrains.com/help/img/idea/2025.3/app-client.expui.gutter.run.svg" style={{display: 'inline-block', margin: 'inherit'}} /> and select **Generate WireMock Stubs**.

<img src="https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/generate_stubs_from_openapi_spec.png?fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=0bfb3e1f4e4791e778d095428e76fe67" width="550" alt="Creating WireMock stub from OpenAPI Specs" data-og-width="812" data-og-height="516" data-path="images/ides/jetbrains/generate_stubs_from_openapi_spec.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/generate_stubs_from_openapi_spec.png?w=280&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=c42601bfa9afc75511460a3295f491f0 280w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/generate_stubs_from_openapi_spec.png?w=560&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=9e0d7858e91303ec4f840453417d65b0 560w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/generate_stubs_from_openapi_spec.png?w=840&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=3164fb369b6f803defa68ffb4191cdac 840w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/generate_stubs_from_openapi_spec.png?w=1100&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=117eedcd0980661ce651e68564b93001 1100w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/generate_stubs_from_openapi_spec.png?w=1650&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=3693ee66ee46b8c0c07b875619b7326a 1650w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/generate_stubs_from_openapi_spec.png?w=2500&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=c03d9b9febde96db3936d936073e5abd 2500w" />

The new stub file is saved as a [scratch](https://www.jetbrains.com/help/idea/scratches.html) under **Scratches and Consoles | WireMock Stubs**.

## Run WireMock server

1. Open your stub file.
2. Click <img src="https://resources.jetbrains.com/help/img/idea/2025.3/app-client.expui.webReferences.server.svg" alt="Run WireMock" style={{display: 'inline-block', margin: 'inherit'}} /> in the upper-right part of the editor.

<img src="https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/run-wiremock-server.png?fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=097393e79874f5c4b1ffc94786a9a537" width="550" alt="Run WireMock server" data-og-width="1054" data-og-height="416" data-path="images/ides/jetbrains/run-wiremock-server.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/run-wiremock-server.png?w=280&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=c9d3f6ff041841987ca9f5416feaa044 280w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/run-wiremock-server.png?w=560&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=6564a073c1fad0c42f2967b5b8b367cb 560w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/run-wiremock-server.png?w=840&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=ab923f7b0e946da46b51a9dc93d60f1e 840w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/run-wiremock-server.png?w=1100&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=2eb74bcc0d742ed8ff4377976010ccdd 1100w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/run-wiremock-server.png?w=1650&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=294e05c2a0c4e4c6e3218ef7c0fe3c60 1650w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/run-wiremock-server.png?w=2500&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=8c540fa3bab98cfc74c333bd2cf34556 2500w" />

This will start the WireMock server, and you can see it running in the **Services** tool window (**View | Tool Windows | Services** or press <kbd>⌘Сmd</kbd><kbd>8</kbd> or <kbd>Alt</kbd><kbd>8</kbd>).

<img src="https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/running-wiremock-server-services-tool-window.png?fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=7a5ec31980249b1d5c1a28617dc78c50" alt="A running WireMock server in the Services tool window" data-og-width="1864" width="1864" data-og-height="682" height="682" data-path="images/ides/jetbrains/running-wiremock-server-services-tool-window.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/running-wiremock-server-services-tool-window.png?w=280&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=43088c71ec3aadc4c9eae7f945b66a04 280w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/running-wiremock-server-services-tool-window.png?w=560&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=c076b43390b4357065b6cc5c4362062d 560w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/running-wiremock-server-services-tool-window.png?w=840&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=3fe723e2d40bf50cac94c194ae266e22 840w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/running-wiremock-server-services-tool-window.png?w=1100&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=f8892665e8081fd5577856aa7401061a 1100w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/running-wiremock-server-services-tool-window.png?w=1650&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=27e1db268c30f1a22ce72f7867478548 1650w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/running-wiremock-server-services-tool-window.png?w=2500&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=f9b03437b1174973d963dd3a7ba6d410 2500w" />

To customize how IntelliJ IDEA starts the WireMock server, you can [modify the WireMock run configuration](#wiremock-run-configuration) or create a new one.

## Send HTTP requests

Use the IntelliJ IDEA [HTTP Client](https://www.jetbrains.com/help/idea/http-client-in-product-code-editor.html) to send HTTP request to the WireMock server and preview responses.

1. [Run your WireMock server.](#run-wiremock-server)
2. Open your stub JSON file.
3. Place the caret at your endpoint URL, press <kbd>⌥Option</kbd><kbd>↩Enter</kbd> or <kbd>Alt</kbd><kbd>↩Enter</kbd> (**Show Context Actions**), and select **Generate request in HTTP Client**.

You can view the stub response in the **Services** tool window.

<img src="https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-send-http-request.gif?s=71c826f93d028aad0a97a6ee688da964" width="900" alt="WireMock send HTTP request" data-og-width="1268" data-og-height="1010" data-path="images/ides/jetbrains/wiremock-send-http-request.gif" data-optimize="true" data-opv="3" />

## Enable support for Handlebars templates

IntelliJ IDEA provides coding assistance for templating language used in WireMock response templates. To use this feature, you need the [Handlebars/Mustache](https://plugins.jetbrains.com/plugin/6884-handlebars-mustache) plugin to be installed and enabled.

1. Open your stub JSON file.
2. In the upper-right part of the editor, click <img src="https://resources.jetbrains.com/help/img/idea/2025.3/handlebarsJson.svg" style={{display: 'inline-block', margin: 'inherit'}} /> (**Use Handlebars Templates**). If the [Handlebars/Mustache](https://plugins.jetbrains.com/plugin/6884-handlebars-mustache) plugin is not installed, the action will install it.

This will make IntelliJ IDEA treat JSON files placed in the `__files` directory as response templates and provide appropriate Handlebars coding assistance including completion for [Handlebars helpers](https://wiremock.org/docs/response-templating/#handlebars-helpers).

<img src="https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/enable-support-for-handlebars-templates.png?fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=732352d5623f45163036b6e9b29f50ea" alt="Enable support for Handlebars templates" data-og-width="1538" width="1538" data-og-height="1194" height="1194" data-path="images/ides/jetbrains/enable-support-for-handlebars-templates.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/enable-support-for-handlebars-templates.png?w=280&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=f20eb3a7e6be6ae1e0fcd055c0dea356 280w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/enable-support-for-handlebars-templates.png?w=560&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=b47d1c7289b7959109e2b006bb3ae680 560w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/enable-support-for-handlebars-templates.png?w=840&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=a263d832564b9dd266aabc0ad7db13d4 840w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/enable-support-for-handlebars-templates.png?w=1100&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=b2c6775f1b69b7a6debc610a000f25c6 1100w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/enable-support-for-handlebars-templates.png?w=1650&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=ddab1f59009d526e0b6e4014d8f866e3 1650w, https://mintcdn.com/wiremockinc/aVMhpBIMjELNN2Qr/images/ides/jetbrains/enable-support-for-handlebars-templates.png?w=2500&fit=max&auto=format&n=aVMhpBIMjELNN2Qr&q=85&s=fd50fe3cc43a4736acd4a2c52c8cb6fc 2500w" />

## WireMock run configuration

<Info>Create: Run | Edit Configurations | + | WireMock</Info>

IntelliJ IDEA comes with a dedicated **WireMock** run configuration, which allows you to customize how to start the WireMock server.

<img src="https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-run-configuration.png?fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=b3ca80cc341e1dac470e24f5c89985ec" alt="WireMock run configuration" data-og-width="1568" width="1568" data-og-height="1212" height="1212" data-path="images/ides/jetbrains/wiremock-run-configuration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-run-configuration.png?w=280&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=92eeef2d9d9e4e84d6ed2afc8b8eeceb 280w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-run-configuration.png?w=560&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=6258a176ee561717d721ba6a8d666c32 560w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-run-configuration.png?w=840&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=40ec4693d04a6373327d3c25d186d177 840w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-run-configuration.png?w=1100&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=fae6999a1f8c65606ff098f62eb0847e 1100w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-run-configuration.png?w=1650&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=43d7d3e2ebb891e79c1e6a27e0ccd02f 1650w, https://mintcdn.com/wiremockinc/X5ETVmm7Bk8h2cuW/images/ides/jetbrains/wiremock-run-configuration.png?w=2500&fit=max&auto=format&n=X5ETVmm7Bk8h2cuW&q=85&s=8863dd20c383449910809ee91fbc9ec2 2500w" />

### Main parameters

* **Name**: Specify a name for the run configuration.
* **Stubs file**: Location of the JSON file with WireMock stubs to run.
* **Server port**: HTTP port number for the WireMock server. Enter `0` to dynamically determine a port.

### Modify options

* **Verbose output**: Turn on verbose logging to stdout (equivalent for the `--verbose` option).
* **Enable global Handlebars templating**: Render all response definitions using Handlebars templates by passing the `--global-response-templating` [WireMock command line option](https://wiremock.org/docs/standalone/java-jar/#command-line-options).
* **JRE**: Select a JRE if you wish to run WireMock in a different runtime environment than JBR.

### Logs

Specify which log files generated while running the application should be displayed in the console on the dedicated tabs of the [Run](https://www.jetbrains.com/help/idea/2025.3/run-tool-window.html) tool window.

### Before launch

Select tasks to be performed before starting the selected run/debug configuration.
