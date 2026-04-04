# Source: https://sap.github.io/cloud-sdk/docs/java/features/odata/vdm-generator

Title: Generate a Typed OData Client With the OData Generator | SAP Cloud SDK

URL Source: https://sap.github.io/cloud-sdk/docs/java/features/odata/vdm-generator

Markdown Content:
The OData Generator allows for generating Java classes from the metadata of an OData service. These classes which are referred to as _typed OData client_ provide type-safe access to the service.

Localisation

The generator is designed to generate source code in english. You may also generate a client based on other languages in the EDMX file. However, languages that use non-latin characters, specifically languages that read from right to left or that don't have capitalisation, may not be supported.

In general, there are two ways to use the generator:

*   Via the dedicated maven plugin (via `pom.xml` and CLI)
*   By instantiating and invoking it at runtime

The maven plugin is usually the recommended way as it integrates nicely with most project setups and makes configuration easy. However, the other two approaches are available and all are documented below.

For all three the required input is an `EDMX` file holding the service metadata.

OData v2 and OData v4

Please be aware that OData v2 and OData v4 service definitions are not interchangeable. There is a dedicated generator for each protocol version and it only accepts service definitions for that version.

Custom Data Types

The OData VDM generator does support all data types per the [OData specification](https://www.odata.org/documentation/odata-version-2-0/json-format/). If your OData service metadata uses a data type not listed in the standard, please alter your metadata to use a compatible data type from the specification instead.

For example, a non-standard `Edm.Float` type can be substituted by `Edm.Single` type from the OData specification.

Using the OData Generator[​](https://sap.github.io/cloud-sdk/docs/java/features/odata/vdm-generator#using-the-odata-generator "Direct link to Using the OData Generator")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Regardless of how the generator is invoked the generated code requires some dependencies to be present. Therefore, it is required to ensure the following dependencies are present in your project:

*   OData v2
*   OData v4

`<dependency>    <groupId>com.sap.cloud.sdk.datamodel</groupId>    <artifactId>odata-v4-core</artifactId></dependency><dependency>    <groupId>org.projectlombok</groupId>    <artifactId>lombok</artifactId>    <scope>provided</scope></dependency>`

Lombok Dependency

Lombok is used by the generated typed OData client classes, that is why they are needed but only with the scope _provided_. Furthermore, some common IDEs (e.g. IntelliJ, Eclipse) require plugins to recognize these annotations. See the note on [missing accessors](https://sap.github.io/cloud-sdk/docs/java/troubleshooting-frequent-problems#compilation-failures-in-generated-odata-vdm-classes)

### Using the OData Generator Maven Plugin[​](https://sap.github.io/cloud-sdk/docs/java/features/odata/vdm-generator#using-the-odata-generator-maven-plugin "Direct link to Using the OData Generator Maven Plugin")

The maven plugin is most useful if you would like to use the generated code within a maven project. Use it by adding it to your `application/pom.xml` file under the `<plugin>` section:

*   OData v2
*   OData v4

`<plugin>    <groupId>com.sap.cloud.sdk.datamodel</groupId>    <artifactId>odata-v4-generator-maven-plugin</artifactId>    <!-- Please use the latest version here-->    <version>5.XX.X</version>    <executions>        <execution>            <id>generate-consumption</id>            <phase>generate-sources</phase>            <goals>                <goal>generate</goal>            </goals>            <configuration>                <inputDirectory>${project.basedir}/edmx</inputDirectory>                <outputDirectory>${project.build.directory}/vdm</outputDirectory>                <deleteOutputDirectory>true</deleteOutputDirectory>                <packageName>com.mycompany.vdm</packageName>                <defaultBasePath>odata/v4/</defaultBasePath>                <compileScope>COMPILE</compileScope>                <serviceMethodsPerEntitySet>true</serviceMethodsPerEntitySet>                <!-- (Optional) You can add a custom copyright header:		        <copyrightHeader>Copyright (c) this year, my company</copyrightHeader>		        Or use the SAP copyright header:		        <sapCopyrightHeader>true</sapCopyrightHeader>		        -->            </configuration>        </execution>    </executions></plugin>`

Adapt the `<inputDirectory>` to point to the location of your service definitions. A full list of parameters is [available here](https://sap.github.io/cloud-sdk/docs/java/features/odata/vdm-generator#available-parameters).

Now maven will run the generator within the `process-sources` phase which is executed before `compile`. The `<compileScope>` option instructs maven to add the generated code as sources for the compile phase.

caution

Usually, you will have to override the generated service path in the code. By default, the generator will use the `namespace` value of the `<schema>` tag as the service name. The URL path will be built as `default-base-path` + `service-name`. If your service definition does not contain this value or the value does not match what is needed in the URL then you need to override the service path in the code. Use the `.withServicePath("/path/to/my/service")` option on the service class.

### Using the Plugin from the Command Line[​](https://sap.github.io/cloud-sdk/docs/java/features/odata/vdm-generator#using-the-plugin-from-the-command-line "Direct link to Using the Plugin from the Command Line")

The maven plugin can also be invoked without a project from the command line using `-D` parameter flags, for example:

*   OData v2
*   OData v4

`mvn com.sap.cloud.sdk.datamodel:odata-v4-generator-maven-plugin:5.XX.X:generate -Dodatav4.generate.inputDirectory=foo -Dodatav4.generate.outputDirectory=bar`

See the full list of parameters [here](https://github.com/SAP/cloud-sdk-java/blob/main/datamodel/odata-v4/odata-v4-generator-maven-plugin/src/main/java/com/sap/cloud/sdk/datamodel/odatav4/generator/DataModelGeneratorMojo.java).

### Generate Clients Programmatically[​](https://sap.github.io/cloud-sdk/docs/java/features/odata/vdm-generator#generate-clients-programmatically "Direct link to Generate Clients Programmatically")

*   OData v2
*   OData v4

1.   Please include the `odata-v4-generator` artifact as a dependency in your project. Choose a module and location from which you intend to invoke the generator and add the following dependency to the appropriate `pom.xml`. `<dependency>    <groupId>com.sap.cloud.sdk.datamodel</groupId>    <artifactId>odata-v4-generator</artifactId> </dependency>` 

1.   Copy the following code which will later invoke the generator:

`final Path inputDirectory = Paths.get("application/src/main/resources/");final Path outputDirectory = Paths.get("application/src/main/java/");final Path serviceNameMapping = inputDirectory.resolve("serviceNameMappings.properties");new DataModelGenerator()    .withInputDirectory(inputDirectory.toFile())    .withOutputDirectory(outputDirectory.toFile())    .withServiceNameMapping(serviceNameMapping.toFile())    .pojosOnly(false)    .withNameSource(NameSource.NAME)    .withPackageName("org.example")    .withDefaultBasePath("/my/path/")    .serviceMethodsPerEntitySet()    .execute();` 
2.   Adapt the input & output directory as well as the package name according to your setup. A full list of parameters is [available here](https://sap.github.io/cloud-sdk/docs/java/features/odata/vdm-generator#available-parameters). Place your EDMX file within the input folder and run the generator.

This should give you the generated classes in the desired folder. You can now proceed with using them to build requests.

In case you run into issues with the above process:

*   Double-check your service and file names
*   Check that the folders are set up correctly
*   The service name mappings meet your expectations

caution

Usually, you will have to override the generated service path in the code. By default, the generator will use the `namespace` value of the `<schema>` tag as the service name. The URL path will be built as `default-base-path` + `service-name`. If your service definition does not contain this value or the value does not match what is needed in the URL then you need to override the service path in the code. Use the `.withServicePath("/path/to/my/service")` option on the service class.

Available Parameters[​](https://sap.github.io/cloud-sdk/docs/java/features/odata/vdm-generator#available-parameters "Direct link to Available Parameters")
----------------------------------------------------------------------------------------------------------------------------------------------------------

The following parameters are available on the generator for both OData protocol versions:

*   Maven Plugin
*   Java

| Parameter | Default | Description |
| --- | --- | --- |
| `<compileScope>` | `NONE` | Adds the generated sources to the compilation or test phase |
| `<copyrightHeader>` | `null` | Copyright header to be added at the top of generated files |
| `<deleteOutputDirectory>` | `False` | Target directory is deleted before code generation |
| `<defaultBasePath>` | - | Base path of the exposed API |
| `<includeEntitySets>` | - | Only generate classes for specific entity sets |
| `<includeFunctionImports>` | - | Only generate classes for specific function imports |
| `<inputDirectory>` | `input` | Location of the metadata files |
| `<namingStrategy>` | - | Fully-qualified Java class to be used as the naming strategy |
| `<nameSource>` | `LABEL` | Source for entity and property names (either `LABEL` or `NAME`) |
| `<outputDirectory>` | `output` | Output directory for generated sources |
| `<overwriteFiles>` | `False` | Overwrite existing files |
| `<packageName>` | - | Package name for the generated sources |
| `<sapCopyrightHeader>` | `False` | Add the SAP copyright header (overrides `copyrightHeader`) |
| `<serviceNameMappingFile>` | - | Determine service names from a given mapping file |
| `<serviceMethodsPerEntitySet>` | `False` | Generate service methods per each entity set for one entity type |
| `<keepExistingSignatures>`[^1] | `False` | Try to avoid API breaking changes by sticking to existing generated method[^2] signatures |

[^1] Feature is in experimental state.

[^2] The _keep existing signatures_ switch only works if the output directory already contains a generated client library.

More information is also available in the Javadoc of the generator implementation ([OData v2](https://sap.github.io/cloud-sdk/java-api/v5/com/sap/cloud/sdk/datamodel/odata/generator/DataModelGenerator.html), [OData v4](https://sap.github.io/cloud-sdk/java-api/v5/com/sap/cloud/sdk/datamodel/odatav4/generator/DataModelGenerator.html)).

### Available Naming Strategies[​](https://sap.github.io/cloud-sdk/docs/java/features/odata/vdm-generator#available-naming-strategies "Direct link to Available Naming Strategies")

The SAP Cloud SDK offers two different naming strategies that can be used out-of-the-box:

*   `com.sap.cloud.sdk.datamodel.odata.utility.S4HanaNamingStrategy` (default)
*   `com.sap.cloud.sdk.datamodel.odata.utility.SimpleNamingStrategy`

While both strategies, of course, generate syntactically valid Java names, the `S4HanaNamingStrategy` tries to make the names as aligned with common Java coding convention as possible. This is achieved by stripping away common pre- and suffixes used in SAP service specifications, such as the prefix `SAP_` or the suffix `Type`. Furthermore, some names are even extended by, for example, adding the prefix `to` to indicate a navigation property.

In contrast to that, the `SimpleNamingStrategy` performs only the bare minimum of modifications to convert the specified names into valid Java syntax.
