# Source: https://sap.github.io/cloud-sdk/docs/java/getting-started

Title: Getting Started | SAP Cloud SDK

URL Source: https://sap.github.io/cloud-sdk/docs/java/getting-started

Published Time: Fri, 27 Feb 2026 15:35:45 GMT

Markdown Content:
[![Image 1: maven central](https://maven-badges.sml.io/sonatype-central/com.sap.cloud.sdk/sdk-bom/badge.svg)](https://maven-badges.sml.io/sonatype-central/com.sap.cloud.sdk/sdk-bom)

Introduction[​](https://sap.github.io/cloud-sdk/docs/java/getting-started#introduction "Direct link to Introduction")
---------------------------------------------------------------------------------------------------------------------

To get started with the SAP Cloud SDK for Java you can either create a new project or integrate the SAP Cloud SDK into your existing one. You will need an installation of Java and Maven.

Java version compatibility

The SAP Cloud SDK is compatible with Java 17 Long-Term-Support (LTS). Newer Java versions may work as well depending on your setup but are not yet tested by us. Note that the SAP Business Technology Platform Cloud Foundry environment can be configured to run with Java 17.

To start with a clean, new project you can use the Spring Boot Archetye as described below. Alternatively, you can follow [these instructions](https://sap.github.io/cloud-sdk/docs/java/getting-started#integrate-the-cloud-sdk-for-java-into-your-project) to integrate the SAP Cloud SDK into your existing setup.

Generating a Project from a Maven Archetype[​](https://sap.github.io/cloud-sdk/docs/java/getting-started#generating-a-project-from-a-maven-archetype "Direct link to Generating a Project from a Maven Archetype")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The SAP Cloud SDK provides an archetype based on [Spring 6](https://spring.io/).

Run:

`mvn archetype:generate "-DarchetypeGroupId=com.sap.cloud.sdk.archetypes" \    "-DarchetypeArtifactId=spring-boot3" \    "-DarchetypeVersion=RELEASE"`

Maven will ask you to provide the following:

*   `groupId` - usually serves as your organization identifier, i.e. `foo.bar.cloud.app`
*   `artifactId` - it's your application's name, i.e. `mydreamapp`
*   `version` - we recommend keeping `1.0-SNAPSHOT` if you're just starting
*   `package` - by default this equals to `groupId`. Change it only if you know what you're doing

After providing all the interactive values to the CLI it will generate your first SAP Cloud SDK based application:

`[INFO] Scanning for projects...[INFO][INFO] ------------------< org.apache.maven:standalone-pom >-------------------[INFO] Building Maven Stub Project (No POM) 1[INFO] --------------------------------[ pom ]---------------------------------[INFO][INFO] >>> archetype:3.2.1:generate (default-cli) > generate-sources @ standalone-pom >>>[INFO][INFO] <<< archetype:3.2.1:generate (default-cli) < generate-sources @ standalone-pom <<<[INFO][INFO][INFO] --- archetype:3.2.1:generate (default-cli) @ standalone-pom ---[INFO] Generating project in Interactive mode[INFO] ....[INFO] ....Define value for property 'artifactId' (should match expression '[^_]+'): mydreamapp[INFO] Using property: gitignore = .gitignoreDefine value for property 'groupId': foo.bar.cloud.app[INFO] Using property: artifactId = mydreamappDefine value for property 'version' 1.0-SNAPSHOT: :Define value for property 'package' foo.bar.cloud.app: :Confirm properties configuration:artifactId: mydreamappgitignore: .gitignoregroupId: foo.bar.cloud.appartifactId: mydreamappversion: 1.0-SNAPSHOTpackage: foo.bar.cloud.app Y: :[INFO] ----------------------------------------------------------------------------[INFO] Using following parameters for creating project from Archetype: scp-cf-spring-jakarta:RELEASE[INFO] ----------------------------------------------------------------------------[INFO] Parameter: groupId, Value: foo.bar.cloud.app[INFO] Parameter: artifactId, Value: mydreamapp[INFO] Parameter: version, Value: 1.0-SNAPSHOT[INFO] Parameter: package, Value: foo.bar.cloud.app[INFO] Parameter: packageInPathFormat, Value: foo/bar/cloud/app[INFO] Parameter: package, Value: foo.bar.cloud.app[INFO] Parameter: gitignore, Value: .gitignore[INFO] Parameter: groupId, Value: foo.bar.cloud.app[INFO] Parameter: artifactId, Value: mydreamapp[INFO] Parameter: version, Value: 1.0-SNAPSHOT[INFO] Project created from Archetype in dir: /home/user/dev/temp/mydreamapp[INFO] ------------------------------------------------------------------------[INFO] BUILD SUCCESS[INFO] ------------------------------------------------------------------------[INFO] Total time:  20.616 s[INFO] Finished at: 2023-09-07T13:12:09+02:00[INFO] ------------------------------------------------------------------------`

**Congratulations! You've just set up a brand-new application with the SAP Cloud SDK for Java.**

tip

To change the Java version modify the `<java.version>` property in the root `pom.xml`.

### Run App Locally[​](https://sap.github.io/cloud-sdk/docs/java/getting-started#run-app-locally "Direct link to Run App Locally")

Applications created with our SAP Cloud SDK Archetypes give you the possibility to run locally on your development machine.

`mvn clean installcd application/mvn spring-boot:run -D"spring-boot.run.profiles"=local`

### Deploy to Cloud Foundry[​](https://sap.github.io/cloud-sdk/docs/java/getting-started#deploy-to-cloud-foundry "Direct link to Deploy to Cloud Foundry")

Assuming you have installed the [Cloud Foundry CLI](https://docs.cloudfoundry.org/cf-cli/) and are logged into your BTP account you can deploy the app via:

`cf push`

Authentication & Authorization

Please note that the starter project does not come with any authentication or authorization checks enabled by default. This enables you to get started quickly and run locally without further configuration.

However, we recommend securing your application as early as possible in the development process. The archetypes already come preconfigured for typical authorization scenarios. Following [this guide](https://developers.sap.com/tutorials/s4sdk-secure-cloudfoundry.html) you can secure your newly created application in just a few steps.

Integrate the SAP Cloud SDK for Java Into Your Project[​](https://sap.github.io/cloud-sdk/docs/java/getting-started#integrate-the-sap-cloud-sdk-for-java-into-your-project "Direct link to Integrate the SAP Cloud SDK for Java Into Your Project")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Adding Dependencies[​](https://sap.github.io/cloud-sdk/docs/java/getting-started#adding-dependencies "Direct link to Adding Dependencies")

To get started with an existing project include the _SAP Cloud SDK BOM_ in the _dependency management_ section of your project:

`<dependencyManagement>    <dependencies>        <dependency>            <groupId>com.sap.cloud.sdk</groupId>            <artifactId>sdk-bom</artifactId>            <version>use-latest-version-here</version>            <type>pom</type>            <scope>import</scope>        </dependency>    </dependencies></dependencyManagement>`

Include the essential Cloud SDK dependencies in the _dependencies_ section of your project:

`<dependency>    <groupId>com.sap.cloud.sdk</groupId>    <artifactId>sdk-core</artifactId></dependency>`

If you want to connect to an **SAP S/4HANA** system via the **OData** protocol, you should checkout our convenient [OData code generator](https://sap.github.io/cloud-sdk/docs/java/features/odata/vdm-generator). By downloading the OData service specifications for either type of **SAP S/4HANA** system ([**SAP S/4HANA Cloud**](https://api.sap.com/package/SAPS4HANACloud?section=Artifacts) or [**SAP S/4HANA On-premise**](https://api.sap.com/package/S4HANAOPAPI?section=Artifacts)) you can generate your own set of classes. Similarly the SAP Cloud SDK offers a [code generator for Open API](https://sap.github.io/cloud-sdk/docs/java/features/rest/generate-rest-client) protocol.

In case you have a **CAP application** which uses **multitenancy** features and/or a **protected backend** your service will need the following dependency:

`<dependency>  <groupId>com.sap.cds</groupId>  <artifactId>cds-integration-cloud-sdk</artifactId></dependency>`

### Framework Integration[​](https://sap.github.io/cloud-sdk/docs/java/getting-started#framework-integration "Direct link to Framework Integration")

In general, the SAP Cloud SDK for Java integrates natively into the [Spring Boot](https://spring.io/projects/spring-boot) framework.

In particular the [SAP Cloud SDK provides listeners](https://sap.github.io/cloud-sdk/docs/java/features/multi-tenancy/thread-context) that can extract tenant and principal information from an incoming request. To ensure these listeners are present, please configure your project accordingly.

Please ensure that the application is annotated to scan for components of the SAP Cloud SDK:

`@ComponentScan({"com.sap.cloud.sdk", <your.own.package>})@ServletComponentScan({"com.sap.cloud.sdk", <your.own.package>})`

Also, please check [the Spring version](https://mvnrepository.com/artifact/com.sap.cloud.sdk/sdk-bom/latest) declared in the SAP Cloud SDK BOM doesn't clash with your version of Spring.

SAP Cloud SDK Modules Bill-of-Material

By default, the SAP Cloud SDK archetypes reference the SAP Cloud SDK Bill-of-Material `sdk-bom`, which manages dependency versions for all SAP Cloud SDK modules and transitive dependencies. If you face dependency conflicts, you can instead try using the SAP Cloud SDK Modules Bill-of-Material `sdk-modules-bom` in the `dependencyManagement` section of your Maven POM file.

Next Steps[​](https://sap.github.io/cloud-sdk/docs/java/getting-started#next-steps "Direct link to Next Steps")
---------------------------------------------------------------------------------------------------------------

*   [Deploy your application to BTP Cloud Foundry](https://developers.sap.com/tutorials/s4sdk-cloud-foundry-sample-application.html)
*   [Call an OData Service on S/4HANA Cloud or On-Premise](https://developers.sap.com/tutorials/s4sdk-odata-service-cloud-foundry.html)
*   [Add resilience to your application](https://developers.sap.com/tutorials/s4sdk-resilience.html)
*   [Secure your application to prevent unauthorized access](https://developers.sap.com/tutorials/s4sdk-secure-cloudfoundry.html)

Further Resources[​](https://sap.github.io/cloud-sdk/docs/java/getting-started#further-resources "Direct link to Further Resources")
------------------------------------------------------------------------------------------------------------------------------------

*   Check our latest [release notes](https://sap.github.io/cloud-sdk/docs/java/release-notes)
*   Get [support](https://github.com/SAP/cloud-sdk-java/issues/new/choose) if you have questions or experience any issues
