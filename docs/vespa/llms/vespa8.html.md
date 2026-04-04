# Source: https://docs.vespa.ai/en/reference/release-notes/vespa8.html.md

# Vespa 8 Release Notes

 

This document lists the changes between Vespa major versions 7 and 8. As documented in [Vespa versions](../../learn/releases.html#versions), new functionality in Vespa is introduced in minor versions, while major versions are used to mark releases breaking compatibility. As Vespa 8 does not introduce any new functionality, it is as safe and mature as the versions of Vespa 7 preceding it. No further releases will be made of Vespa 7, except possible critical security fixes.

## Overview

The compatibility breaking changes in Vespa 8 fall into these categories:

- [Changes to default behaviour](#changed-defaults)
- [Application package structure and settings](#application-package-changes) - deprecated settings and constructs in e.g. _schemas_ and _services.xml_ are removed.
- [Java APIs](#java-api-changes) - deprecated APIs are removed or revoked from Vespa's [public API](https://javadoc.io/doc/com.yahoo.vespa/annotations/latest/com/yahoo/api/annotations/PublicApi.html) surface.
- [Container runtime environment](#container-runtime) - incompatible changes to the Java build and runtime environments.
- [HTTP API changes](#removed-http-api-parameters)
- [Removed command line tools](#removed-command-line-tools)
- [Removed or renamed metrics](#removed-or-renamed-metrics)
- [Changes to the document selection language](#document-selection-exact-type-matching)
- [Security related changes](#security)
- [Operating system support](#operating-system)
- [Other changes](#other-changes), not covered by any of the above categories.

To ensure their applications are compatible with Vespa 8, application owners must:

- Review the list of [changes to defaults](#changed-defaults) and add the necessary options if you want to preserve behavior from Vespa 7.
- Make sure there are no deprecation warnings when compiling against Vespa 7.
- Review the [application package changes](#application-package-changes) and make sure there are no deployment warnings when deploying on Vespa 7.
- Review the list of [HTTP API changes](#removed-http-api-parameters) and update any clients of the application.
- Review the remaining sections of this document, and update the application and its environment accordingly.

Usage of deprecated Java APIs produce warnings during compilation, while _deployment warnings_ are produced for application package deprecations and most changes to the container runtime environment. In hosted Vespa or Vespa Cloud, deployment warnings are shown in the application's console view. However, for other types of changes, there is no way to emit deprecation warnings, so these are only described in this document and other Vespa documentation.

The following sections lists all the changes from Vespa 7 to Vespa 8 in detail.

## Changed defaults

These changes may break clients, and impact both performance and user experience. Applications that are in production and relies on these defaults should make configuration changes to keep the existing behavior when upgrading to Vespa 8. This can be done on Vespa 7, _before_ upgrading - using [bucket tests](../../applications/testing.html#feature-switches-and-bucket-tests) can be useful.

The following defaults have changed:

| Change | Configuration required to avoid change on Vespa 8 |
| --- | --- |
| The default [simple query language](../querying/simple-query-language.html) (for end users) is changed from `all` to [weakAnd](../../ranking/wand.html#weakand). 
 **Note:** This might increase recall, and increase latency significantly if document corpus is large.
 | Explicitly pass [model.type](../api/query.html#model.type)=all in queries or set this parameter in the relevant [query profiles](../../querying/query-profiles.html): `<field name="model.type">all</field>`. |
| The default grammar in [YQL userInput](../querying/yql.html#userinput) is changed from `all` to [weakAnd](../../ranking/wand.html#weakand). 
 **Note:** This might increase recall, and increase latency significantly if document corpus is large.
 | Prefix `userInput` in YQL by `{grammar: "all"}`. |
| The value of the services.xml [legacy flag v7-geo-positions](../querying/default-result-format.html#geo-position-rendering) changes from true to false. See the [Vespa 8 geo migration guide](vespa8-geo-migration-guide). | Add to services.xml: `
        <legacy> <v7-geo-positions>true</v7-geo-positions> </legacy>
      ` |
| Fields of type `map`[changes JSON rendering](../querying/default-result-format.html#inconsistent-map-rendering) in search results. | Add overrides in your query profile(s) for the `renderer.json.jsonMaps` parameter. |
| Fields of type `weightedset`[changes JSON rendering](../querying/default-result-format.html#inconsistent-weightedset-rendering) in search results. | Add overrides in your query profile(s) for the `renderer.json.jsonWsets` parameter. |
| Expressions used as summary features, are no longer rendered wrapped in `rankingExpression()`. | Specify configuration in your rank profile as shown in [this example](../querying/default-result-format.html#summary-features-wrapped-in-rankingexpression). |
| Fields of type `raw` are now presented as a base64 encoded string in summary, the same way as in json feed format. Earlier, you needed to add `raw-as-base64-in-summary` in your schema file to get this behavior. | If you have fields of type "raw" and you must have the old summary behavior for them in search results, add the line   
`raw-as-base64-in-summary : false`  
 in your schema definition. |
| The default tensor format in responses has changed from 'long' to 'short': Tensors in query results, document API responses, and stateless model evaluation are rendered in the short form appropriate for their type (if any), documented [here](../schemas/document-json-format.html#tensor). | 

**Queries**: Pass [presentation.format.tensors](../api/query.html#presentation.format.tensors)=long in queries, or set it parameter in the relevant [query profiles](../../querying/query-profiles.html).

**Document/v1**: Pass the parameter `format.tensors=long` in requests.

**Stateless model evaluation**: Pass the parameter `format.tensors=long` in requests.

 |
| The default fieldset when getting or visiting documents is now `[document]` in all cases, meaning you only get those fields that are declared in the "document" block of the schema (generated fields are not included). This was already the default for the `/document/v1` API when fetching or visiting documents of a single known document type. Now it is also the default when visiting at the root level, for the command line tools `vespa-visit` and `vespa-get`, and if you use the programmatic `documentapi` from java to fetch documents. | In most cases there is no difference between `[all]` and `[document]` fieldsets - so no action is needed. If the old behavior is needed you can: 
- For the command line tools, specify the fieldset as `-l "[all]"` to include generated fields. 
- For `/document/v1` specify `[all]` as the value for the `fieldSet` parameter. 
- If using `documentapi` from java, add the line   
`params.setFieldSet("[all]");`  
 to modify your `VisitorParameters` value , or   
`params = params.withFieldSet("[all]");`  
 to modify your `DocumentOperationParameters` value. 

 If you run document processors to generate fields and want those returned, it may be more useful to declare a fieldset with just those fields you actually want as output instead. |
| Vespa will now limit the number of groups and hits in [grouping query results](../../querying/grouping.html) when `max` is not specified explicitly in grouping expressions. The default value is determined by [grouping.defaultMaxGroups](../api/query.html#grouping.defaultmaxgroups)/ [grouping.defaultMaxHits](../api/query.html#grouping.defaultmaxhits). The parameter [grouping.globalMaxGroups](../api/query.html#grouping.globalmaxgroups) must now be overridden in query profiles to allow grouping expressions that may return unbounded or large results. | 
- [grouping.defaultMaxGroups](../api/query.html#grouping.defaultmaxgroups) changed from `-1` to `10`. 
- [grouping.defaultMaxHits](../api/query.html#grouping.defaultmaxhits) changed from `-1` to `10`. 
- [grouping.globalMaxGroups](../api/query.html#grouping.globalmaxgroups) changed from `-1` to `10000`. 
- [grouping.defaultPrecisionFactor](../api/query.html#grouping.defaultprecisionfactor) changed from `1.0` to `2.0`. 

 |
| Vespa [access logs](../../operations/access-logging.html) are compressed with [zstd](https://github.com/facebook/zstd). | Add a config override under `<container>` in `services.xml`:   

```
<config name="container.core.access-log">
        <fileHandler>
          <compressionFormat>GZIP<compressionFormat>
```
 |

## Application package changes

### Removed settings from schemas

The following settings are removed from [schema](../schemas/schemas.html):

| Name | Replacement |
| --- | --- |
| attribute: huge | None. Setting _huge_ on an attribute doesn't have any effect, the code is rewritten to support it by default. |
| [compression](../schemas/schemas.html#compression) | 

None. Document compression is not needed, as compression is always enabled.

 |
| body (inside a field definition) | 

None. Deprecated since before Vespa 7, had no effect in Vespa 7.

 |
| header (inside a field definition) | 

None. Deprecated since before Vespa 7, had no effect in Vespa 7.

 |
| field type weightedset\<float\> | Because floating-point types are inherently imprecise they are badly suited as keys in maps and sets. If you feel the need for such data consider using something like: 
```
struct weightedfloat {
                 field value type float {}
                 field weight type int {}
             }
             field myfield type array<weightedfloat> {
                 ...
```
 |
| field type map\<float,anything\> | Using "float" as the key in a map is no longer supported, see `weightedset<float>` above. |
| field type weightedset\<double\> | Using "double" as the key in a set is no longer supported, see `weightedset<float>` above. |
| field type map\<double,anything\> | Using "double" as the key in a map is no longer supported, see `weightedset<float>` above. |
| field type weightedset\<uri\> | Using complex types as the key in a set is no longer supported, see `weightedset<float>` above. |
| field type map\<uri,anything\> | Using complex types as the key in a map is no longer supported, see `weightedset<float>` above. |
| Old syntax for array types like "string[]" | Write as `array<string>` instead. |
| Rank functions must have different names in a rank-profile | Only the last of two functions with the same name would be used. Remove or rename the first one. |
| Conflicting sorting settings are now rejected | Only keep the last of the conflicting settings. |
| A summary-field may only be added once in a document-summary block | Remove duplicates. |
| Schema and document should have the same name | Change name of the schema, so it is equal to the contained document. |

### TensorFlow import

Vespa 8 removes support for direct import of [TensorFlow models](../../ranking/tensorflow). [ONNX](https://onnx.ai/) is now the preferred ML model format, and works both for [ranking](../../ranking/onnx) and [stateless model evaluation](../../ranking/stateless-model-evaluation.html). ONNX contains tools to convert models from TensorFlow to ONNX, but Vespa will no longer provide this.

### Changed semantics in services.xml

The following elements and attributes in services.xml have new semantics:

| Name | Description |
| --- | --- |
| \<nodes\>\<redundancy\> | It is now an error to configure a number of nodes (per group) that is smaller than the configured redundancy. It used to generate an application-level warning, with the redundancy implicitly reduced. Remove any \<nodes\> override in the non-prod environments, as the node count is automatically adjusted. |

### Removed constructs from services.xml

The following elements and attributes are removed from services.xml:

| Parent element | Removed construct | Description |
| --- | --- | --- |
| \<admin\> | \<filedistribution\> | Configuring up/download rates is not supported |
| \<configserver\> | Use [configservers](../applications/services/admin.html#configservers) element instead |
| \<config\> | _namespace_ attribute | The namespace must be included in the _name_ attribute. |
| \<myArray _operation="append"\>_ syntax | Previously used to append items to config arrays. Use [item](../applications/config-files.html#configuring-arrays) instead. |
| \<container\> | _jetty_ attribute | Removed, had no effect on Vespa 7. |
| \<nodes\> jvm attributes | JVM attributes _jvmargs, allocated-memory, jvm-options, jvm-gc-options_ renamed and moved to [JVM](../applications/services/container.html#jvm) subelement |
| \<client\> | Previously used for setting up client providers. Use a [request handler](../../applications/request-handlers.html) instead. |
| \<handler\>\<clientBinding\> | Client bindings are no longer supported. |
| \<content\> | \<dispatch\> | Removed due to removal of _vespa-dispatch-bin_, [details.](#vespa-dispatch-bin-process-is-removed) |
| \<tuning\>\<dispatch\>\<min-group-coverage\> | Use [min-active-docs-coverage](../applications/services/content.html#min-active-docs-coverage) instead. |
| \<tuning\>\<dispatch\>\<use-local-node\> | Ignored, the local node will automatically be preferred when appropriate. |
| \<engine\>\<proton\>\<tuning\>\<searchnode\>\<flushstrategy\>\<native\>\<transactionlog\>\<maxentries\> | Use [maxsize](../applications/services/content.html#flushstrategy-native-transactionlog-maxsize) instead. Vespa 7 documentation: The maximum number of entries in the [transaction log](../../content/proton.html#transaction-log) for a document type before running flush, default 1000000 (1 M). |
| \<engine\>\<proton\>\<tuning\>\<searchnode\>\<summary\>\<store\>\<logstore\>\<chunk\>\<maxentries\> | Use [maxsize](../applications/services/content.html#summary-store-logstore-chunk-maxsize) instead. Vespa 7 documentation: Maximum number of documents in a chunk. See _summary.log.chunk.maxentries_. |
| \<services\> (root) | \<jdisc\> | Use [container](../applications/services/container.html) instead. |
| \<service\> | Running generic services is no longer supported. |
| \<clients\> | Client load types are deprecated and ignored. |

### _application/_ folder support removed

Application package content (_services.xml_, the _schemas/_ folder, etc.) is supposed to be put at the root level in the application zip, such that the unzipped application package has _./services.xml_, etc.

But it used to be that the application package content could be placed inside an _application_ directory. This support is removed on Vespa 8.

### _searchdefinitions/_ folder is deprecated

Search definition schemas should now be placed in the _schemas/_ folder. The old folder will still work on Vespa 8, but causes a deprecation warning upon deployment.

## Java API changes

### Removed Java packages

| Package | Description |
| --- | --- |
| _com.yahoo.docproc.util_ | Removed |
| _com.yahoo.jdisc.test_ | No longer [public API](https://javadoc.io/doc/com.yahoo.vespa/annotations/latest/com/yahoo/api/annotations/PublicApi.html) |
| _com.yahoo.log.event_ | No longer [public API](https://javadoc.io/doc/com.yahoo.vespa/annotations/latest/com/yahoo/api/annotations/PublicApi.html) |
| _com.yahoo.statistics_ | Removed |
| _com.yahoo.vespa.curator_ | No longer [public API](https://javadoc.io/doc/com.yahoo.vespa/annotations/latest/com/yahoo/api/annotations/PublicApi.html) |
| _com.yahoo.documentapi.messagebus.loadtypes_ | Load types are no longer supported. Use corresponding method overloads without _LoadType_ or _LoadTypeSet_ parameters instead. |

### Removed Java Classes and methods

Classes and methods that were marked as deprecated in Vespa 7 are removed. If deprecation warnings are emitted for Vespa APIs when building the application, these must be fixed before migrating to Vespa 8. The sections below contain only the most notable changes.

The following classes are no longer public API and have been moved to Vespa internal packages:

| Package | Class | Migration advice |
| --- | --- | --- |
| _com.yahoo.config.subscription_ | All classes, except [_ConfigGetter_](https://javadoc.io/doc/com.yahoo.vespa/config/latest/com/yahoo/config/subscription/ConfigGetter.html) | Config should be [injected](../../applications/configuring-components.html#use-config-in-code) to your component class constructor. |
| _com.yahoo.docproc_ | _DocprocExecutor_ | For unit tests, follow the steps in the [document-processing](https://github.com/vespa-engine/sample-apps/blob/master/examples/document-processing/src/test/java/ai/vespa/example/album/ProductTypeRefinerDocProcTest.java) sample app. If you need a _DocumentTypeManager_ in production code, it can be directly [injected](../../applications/dependency-injection.html) to your component class constructor. |
| _DocprocService_ |
| _DocumentOperationWrapper_ | No replacement - if needed, contact the Vespa team for advice. |
| _HandledProcessingException_ |
| _ProcessingEndpoint_ |
| _TransientFailureException_ |
| _com.yahoo.log_ | _VespaFormatter_ | No replacement. |

The following methods are removed:

| Method | Migration advice |
| --- | --- |
| _com.yahoo.documentapi.DocumentAccess.createDefault()_ | Container components can have a _DocumentAccess_ injected via their constructor. For use outside the container, e.g. in a custom command line tool, use the new method _createForNonContainer()_. |
| _com.yahoo.log.LogSetup.getLogHandler()_ | No replacement. |

### Breaking changes to Java APIs

The Javadoc of the deprecated types/members should document the replacement API. The below list is not exhaustive - some smaller and trivial changes are not listed.

| Type(s) | Description |
| --- | --- |
| _com.yahoo.processing_ | Removed use of Guava's _ListenableFuture_ in type signatures. Replacement uses _CompletableFuture_. |
| _com.yahoo.search.handler.HttpSearchResponse.waitableRender()_ | Removed use of Guava's _ListenableFuture_ in type signature. The method is replaced with _asyncRender()_. |
| _com.yahoo.jdisc.handler_ | Removed use of Guava's _ListenableFuture_ in type signatures. Replacement uses _CompletableFuture_ |
| _com.yahoo.searchlib.rankingexpression.rule_ | Removed use of Guava collection types in type signatures. |
| _com.yahoo.search.rendering.JsonRenderer_ | Removed use of Jackson types from class signature. |
| _com.yahoo.jdisc.Container_ | Removed use of Guice types from class signature. |
| _com.yahoo.vdslib.VisitorStatistics_ | Removed all _set/getSecondPass_-related methods. |
| _com.yahoo.documentapi_ | Removed all methods taking in a _com.yahoo.documentapi.messagebus.DocumentProtocol.Priority_ argument. Explicit operation priorities are deprecated and should not be set by the client. |

### Removed support for built-in XML factories

The Jdisc container has historically supported injection of built-in providers for the following XML factories:

- _javax.xml.datatype.DatatypeFactory_
- _javax.xml.parsers.DocumentBuilderFactory_ and _SAXParserFactory_
- _javax.xml.stream.XMLEventFactory_, _XMLInputFactory_ and _XMLOutputFactory_
- _javax.xml.transform.TransformerFactory_
- _javax.xml.validation.SchemaFactory_
- _javax.xml.xpath.XPathFactory_

These are now removed. Please check for more recent alternatives if you need this type of XML processing.

### Deprecated Java APIs

A few redundant APIs have been deprecated because they have replacements that provide the same, or better, functionality. We advise you switch to the replacement to reduce future maintenance cost.

| Type(s) | Replacement |
| --- | --- |
| _com.yahoo.container.jdisc.LoggingRequestHandler_ | Use _com.yahoo.container.jdisc.ThreadedHttpRequestHandler_ instead. |
| _com.yahoo.log.LogLevel_ | Use _java.util.logging.Level_ instead. |

## Container Runtime Environment

### JDK version

Vespa 8 upgrades the JDK version from 11 to 17. To ensure full compatibility, all container components should be rebuilt with JDK 17 before being deployed on Vespa 8.

### Changes to provided maven artifacts

[Guava](https://search.maven.org/artifact/com.google.guava/guava) has been upgraded from version 20.0 to 27.1. If you are using APIs that have been removed from the library since version 20, your code must be updated. In most cases, it should be trivial to find replacement APIs in Java's standard library.

The following Maven artifacts are no longer provided runtime to user application plugins by the Jdisc container:

| Artifact | Notes |
| --- | --- |
| [_com.fasterxml.jackson.jaxrs:jackson-jaxrs-base_](https://search.maven.org/artifact/com.fasterxml.jackson.jaxrs/jackson-jaxrs-base) | JSON input/output handling for JAX-RS implementations, e.g. Jersey |
| [_com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider_](https://search.maven.org/artifact/com.fasterxml.jackson.jaxrs/jackson-jaxrs-json-provider) |
| [_com.fasterxml.jackson.module:jackson-module-jaxb-annotations_](https://search.maven.org/artifact/com.fasterxml.jackson.module/jackson-module-jaxb-annotations) | Jackson data binding with JAXB annotations. |
| [_com.google.code.findbugs:jsr305_](https://search.maven.org/artifact/com.google.code.findbugs/jsr305) | Annotations in package _javax.annotation[.\*]_, e.g. _Nullable_ and _Nonnnull_. |
| [_com.google.inject.extensions:guice-assistedinject_](https://search.maven.org/artifact/com.google.inject.extensions/guice-assistedinject) | Guice extensions.  
 For component injection see [Depending on another component](../../applications/dependency-injection.html#depending-on-another-component) |
| [_com.google.inject.extensions:guice-multibindings_](https://search.maven.org/artifact/com.google.inject.extensions/guice-multibindings) | Guice extensions. |
| [_javax.annotation:javax.annotation-api_](https://search.maven.org/artifact/javax.annotation/javax.annotation-api) | Annotations in package _javax.annotation[.\*]_, e.g. _ManagedBean_ and _Resource_. |
| [_javax.validation:validation-api_](https://search.maven.org/artifact/javax.validation/validation-api) | Javax bean validation, used by Jersey 2. |
| [_org.eclipse.jetty:\*_](https://search.maven.org/search?q=g:org.eclipse.jetty) | The Eclipse Jetty Project. |
| [_org.apache.felix:org.apache.felix.framework_](https://search.maven.org/artifact/org.apache.felix/org.apache.felix.framework) | Felix OSGi framework. |
| _org.apache.felix:org.apache.felix.log_ | Felix OSGi framework. |
| [_org.apache.felix:org.apache.felix.main_](https://search.maven.org/artifact/org.apache.felix/org.apache.felix.main) | Felix OSGi framework. |
| [_org.bouncycastle:bcpkix-jdk15on_](https://search.maven.org/artifact/org.bouncycastle/bcpkix-jdk15on) | Bouncy Castle crypto API. |
| [_org.bouncycastle:bcprov-jdk15on_](https://search.maven.org/artifact/org.bouncycastle/bcprov-jdk15on) | Bouncy Castle crypto provider. |
| _org.glassfish.\*:\*_ | Jersey 2. All related artifacts are removed. |
| [_org.json:json_](https://search.maven.org/artifact/org.json/json) | See [vespa-engine/vespa#14762](https://github.com/vespa-engine/vespa/issues/14762) |
| [_org.javassist:javassist_](https://search.maven.org/artifact/org.javassist/javassist) | Bytecode manipulation, used by Jersey 2. |
| [_org.jvnet.mimepull:mimepull_](https://search.maven.org/artifact/org.jvnet.mimepull/mimepull) | MIME Streaming Extension, used by Jersey 2. |
| [_org.lz4:lz4-java_](https://search.maven.org/artifact/org.lz4/lz4-java) | Compression library. |

Make sure your application OSGi bundle embeds the required artifacts from the above list. An artifact can be embedded by adding it in scope _compile_ to the _dependencies_ section in pom.xml. Typically, these artifacts have until now been used in scope _provided_. Use `mvn dependency:tree` to check whether any of the listed artifacts are directly or transitively included as dependencies.

As always, remove any dependencies that are not required by your project. Consult the Maven documentation on[Dependency Exclusions](https://maven.apache.org/guides/introduction/introduction-to-optional-and-excludes-dependencies.html#dependency-exclusions) for how to remove a transitively included dependency.

An example adding _org.json:json_ as a compile scoped dependency:
```
<dependencies>
  ...
  <dependency>
    <groupId>org.json</groupId>
    <artifactId>json</artifactId>
    <version>20211205</version>
    <scope>compile</scope>
  </dependency>
  ...
</dependencies>
```

## Removed HTTP API parameters

The following HTTP API parameters are removed from the [query API](../api/query.html):

| Standard API path | Parameter name | Replacement |
| --- | --- | --- |
| /search/ | _pos.ll_ | add a[geoLocation](../querying/yql.html#geolocation)item to the query |
| /search/ | _pos.radius_ | add a[geoLocation](../querying/yql.html#geolocation)item to the query |
| /search/ | _pos.attribute_ | add a [geoLocation](../querying/yql.html#geolocation) item to the query |
| /search/ | _pos.bb_ | Support for restricting search by a bounding box, using the `pos.bb` query parameter, has been removed - add a [geoLocation](../querying/yql.html#geolocation) item to the query |

## Removed command line tools

### vespa-http-client

The `vespa-http-client` command line tool is removed on Vespa 8 and is replaced by the new [vespa-feed-client](../../clients/vespa-feed-client.html). The new client uses [HTTP/2](../../performance/http2.html) and the [Document v1 API](../../writing/document-v1-api-guide.html).

The underlying rest API used by the vespa-http-client will still be available and supported on Vespa 8. You can therefore continue to use an old client distributed with Vespa 7 to feed to a Vespa 8 installation. Note that there will not be released any updates for vespa-http-client after the initial Vespa 8 release, while fixes and security updates to the rest API implementation will continue as part of Vespa 8. We strongly recommend that you migrate away from vespa-http-client in a timely manner.

## Removed or renamed metrics

The following metrics are renamed:

| Old Name | New name | Description |
| --- | --- | --- |
| _vds.filestor.alldisks.\*_ | vds.filestor.\* | _alldisks_ has been removed from the metric name. |
| _vds.visitor.\*.sum.\*_ | vds.visitor.\*.\* | _sum_ has been removed from the metric name. |
| _vds.filestor.\*.sum.\*_ | vds.filestor.\*.\* | _sum_ has been removed from the metric name. |
| _vds.distributor.\*.sum.\*_ | vds.distributor.\*.\* | _sum_ has been removed from the metric name. |

The following metrics are removed:

| Name | Description |
| --- | --- |
| _http.status.401.rate_ | Use _http.status.4xx.rate_ with dimension _statusCode_==401 |
| _http.status.403.rate_ | Use _http.status.4xx.rate_ with dimension _statusCode_==403 |
| _content.proton.documentdb.matching.query\_collateral\_time.\*_ | Use _content.proton.documentdb.matching.query\_setup\_time.\*_ instead |
| _content.proton.documentdb.matching.rank\_profile.query\_collateral\_time.\*_ | Use _content.proton.documentdb.matching.rank\_profile.query\_setup\_time.\*_ instead |
| _vds.visitor.allthreads.averagevisitorlifetime~~.sum~~.average_ | Use .sum/.count instead |
| _vds.visitor.allthreads.averagequeuewait~~.sum~~.average_ | Use .sum/.count instead |
| _vds.visitor.allthreads.queuesize~~.sum~~.average_ | Use .sum/.count instead |
| _vds.visitor.allthreads.completed~~.sum~~.average_ | Use .sum/.count instead |
| _vds.visitor.allthreads.averagemessagesendtime~~.sum~~.average_ | Use .sum/.count instead |
| _vds.visitor.allthreads.averageprocessingtime~~.sum~~.average_ | Use .sum/.count instead |
| _vds.filestor~~.alldisks~~.queuesize.average_ | Use .sum/.count instead |
| _vds.filestor~~.alldisks~~.averagequeuewait.average_ | Use .sum/.count instead |
| _vds.filestor~~.alldisks~~.allthreads.put~~.sum~~.latency.average_ | Use .sum/.count instead |
| _vds.filestor~~.alldisks~~.allthreads.remove~~.sum~~.latency.average_ | Use .sum/.count instead |
| _vds.filestor~~.alldisks~~.allthreads.get~~.sum~~.latency.average_ | Use .sum/.count instead |
| _vds.filestor~~.alldisks~~.allthreads.update~~.sum~~.latency.average_ | Use .sum/.count instead |
| _vds.filestor~~.alldisks~~.allthreads.createiterator~~.sum~~.latency.average_ | Use .sum/.count instead |
| _vds.filestor~~.alldisks~~.allthreads.visit~~.sum~~.latency.average_ | Use .sum/.count instead |
| _vds.filestor~~.alldisks~~.allthreads.remove\_location~~.sum~~.latency.average_ | Use .sum/.count instead |
| _vds.filestor~~.alldisks~~.allthreads.deletebuckets~~.sum~~.latency.average_ | Use .sum/.count instead |
| _vds.distributor.puts~~.sum~~.latency.average_ | Use .sum/.count instead |
| _vds.distributor.removes~~.sum~~.latency.average_ | Use .sum/.count instead |
| _vds.distributor.updates~~.sum~~.latency.average_ | Use .sum/.count instead |
| _vds.distributor.gets~~.sum~~.latency.average_ | Use .sum/.count instead |
| _vds.distributor.visitor~~.sum~~.latency.average_ | Use .sum/.count instead |

## Exact matching of document types in selection language

The [document selection language](../writing/document-selector-language.html) now uses _exact_ matching for document types rather than _inheritance_ ("is-a") matching.

Example with two minimal document schemas:

- `document my_doc_type {}`
- `document my_extended_doc_type inherits my_doc_type {}`

Previously, the selection expression `my_doc_type` would match both a document instance of type `my_doc_type` _and_ `my_extended_doc_type`. It will now _only_ match a document of type `my_doc_type`.

## Security

### Strict mode enabled by default

_Strict mode_ for request filtering in the jdisc container is enabled by default in Vespa 8. See documentation on the [strict-mode](../applications/services/http.html#filtering) attribute in services.xml for details.

### Request headers controlling remote host/port in access log

The jdisc container will use the _X-Forwarded-For_ and _X-Forwarded-Port_ request headers to set the remote host and port respectively in the access log. The following request headers will no longer be handled by default:

- y-ra
- yahooremoteip
- client-ip
- y-rp

## Operating system support for Vespa artifacts

### RPMs

The supported OS for Vespa RPMs changes from [CentOS Linux 7](https://www.centos.org/centos-linux/) to [CentOS Stream 8](https://www.centos.org/centos-stream/) for Vespa 8. RPMs will still be built and distributed on [Fedora Copr](https://copr.fedorainfracloud.org/coprs/g/vespa/vespa/). If you install Vespa RPMs you will have to upgrade your OS to [CentOS Stream 8](https://www.centos.org/centos-stream/).

### OCI containers (Docker containers)

The base image used in our OCI containers changes from [docker.io/centos:7](https://hub.docker.com/_/centos) to [quay.io/centos/centos:stream8](https://quay.io/repository/centos/centos?tab=tags) for Vespa 8. This means that the container image is built and tested on systems running kernel version _4.18.0_ (current kernel for CentOS Stream 8). If you use Vespa's container image, you should upgrade the hosts running the containers to the same or a newer kernel version.

## Other changes

### Unknown rank profiles

Queries that specify a rank profile which does not exist in all the schemas being queried will now fail instead of falling back to using the `default` profile. Queries to multiple schemas must use a rank profile that exists in all of them, which can be ensured by [inheriting](/en/schemas/inheritance-in-schemas.html) a common schema.

### Unknown summary classes

Queries that specify a non-existent [summary class](../../querying/document-summaries.html) will now fail, instead of being rendered empty. Queries to multiple schemas must use a summary class that exists in all of them, which can be ensured by [inheriting](/en/schemas/inheritance-in-schemas.html) a common schema.

### The "qrserver" service name

Vespa containers are in general using "container" as their service name. However, a container cluster that has declared neither [document-processing](../applications/services/docproc.html) nor [document-api](../applications/services/container.html#document-api) used to be named "qrserver". On Vespa 8 all container clusters uses the service name "container". This affects the output of all metrics APIs, as well as the Vespa log output.

### Container access logs

The folder for container access logs has been moved from `$VESPA_HOME/logs/vespa/qrs/` to `$VESPA_HOME/logs/vespa/access/`.

The default compression format has changed from gzip to zstd, see [changed defaults](#changed-defaults).

### ONNX output in summary features

When defining an ONNX model output in summary features, Vespa 8 ensures that the summary feature name is `onnx` rather than `onnxModel` as in previous version.

### Changes in rankfeatures

Vespa can calculate and return all [rank-features](../api/query.html#ranking.listfeatures) in the `rankfeatures` summary field. Vespa 8 contains some changes to this list:

- `now` is removed
- `bm25(field)` is added
- `matches(field)` is added

### The "storage" message bus routing policy is removed

The "storage" routing policy was removed in early Vespa 7, and clients specifying it have been forwarded to the content routing policy for backwards compatibility. The forwarding is removed on Vespa 8 and clients needs be updated.

Replace all usages of the "storage" policy with "content", which behaves identically.

### vespa-dispatch-bin process is removed

The dispatch functionality is moved into the Vespa Container and the _vespa-dispatch-bin_ process is removed. As this is not a public interface, the default was switched to **not** using vespa-dispatch-bin in Vespa-7.109.10. The process was removed in subsequent Vespa releases:

| [Dispatch](../../querying/query-api.html) | Content cluster | dynamically allocated in 19100 - 19899 range | $VESPA\_HOME/sbin/vespa-dispatch-bin | Dispatcher, communicates between container and content nodes. Can be multi-level in a hierarchy |

Rolling upgrade note: A rolling upgrade over Vespa-7.109.10 should work with no extra steps.

### YQL format

- When Vespa outputs an YQL statement, it will now not end the string by a semicolon. Terminating statements with semicolon continue to be optional and legal input. 
- [Annotations](../querying/yql.html#annotations) are not enclosed in `[]` brackets (still valid input). 
- The annotation name is not quoted (still valid input). 

Example Vespa 7 / Vespa 8:

```
where text contains ([{"distance": 5}]near("a", "b"));
where text contains ({distance: 5}near("a", "b"))
```

### Upgrade procedure
The [upgrade procedure](/en/operations/self-managed/live-upgrade.html) has been simplified in Vespa 8 (when upgrading from Vespa 7 to Vespa 8 or between Vespa 8 versions). When upgrading from Vespa 7.x to Vespa 7.y replace item 3[Upgrade config servers](/en/operations/self-managed/live-upgrade.html#upgrade-config-server)in the [upgrade procedure](/en/operations/self-managed/live-upgrade.html) with this procedure:
- When upgrading the config servers, the nodes of the application cannot receive config until they are upgraded themselves. We need to set all of them in standalone mode before continuing by running this command on each node: 
```
$ vespa-configproxy-cmd -m setmode memorycache
```
 Each node will automatically reattach itself when it is upgraded. 
- Install the new Vespa version on the config servers and [restart](/en/operations/self-managed/admin-procedures.html#vespa-start-stop-restart) them one by one. Wait until it is up again, look in vespa log for "Changing health status code from 'initializing' to 'up'" or use [health checks](/en/operations/self-managed/configuration-server.html#troubleshooting). 
- Redeploy and activate the application: 
```
$[vespa deploy](/en/clients/vespa-cli.html#deployment)
```

 Copyright © 2026 - [Cookie Preferences](#)

### On this page:

- [Overview](#compatibility-overview)
- [Changed defaults](#changed-defaults)
- [Application package changes](#application-package-changes)
- [Removed settings from schemas](#removed-settings-from-schemas)
- [TensorFlow import](#tensorflow-import)
- [Changed semantics in services.xml](#changed-semantics-in-services-xml)
- [Removed constructs from services.xml](#removed-constructs-from-services-xml)
- [Java API changes](#java-api-changes)
- [Removed Java packages](#removed-java-packages)
- [Removed Java Classes and methods](#removed-java-classes-and-methods)
- [Breaking changes to Java APIs](#changed-java-apis)
- [Removed support for built-in XML factories](#built-in-xml-factories)
- [Deprecated Java APIs](#deprecated-java-apis)
- [Container Runtime Environment](#container-runtime)
- [JDK version](#jdk-version)
- [Changes to provided maven artifacts](#provided-maven-artifacts)
- [Removed HTTP API parameters](#removed-http-api-parameters)
- [Removed command line tools](#removed-command-line-tools)
- [vespa-http-client](#vespa-http-client)
- [Removed or renamed metrics](#removed-or-renamed-metrics)
- [Exact matching of document types in selection language](#document-selection-exact-type-matching)
- [Security](#security)
- [Strict mode enabled by default](#strict-mode)
- [Request headers controlling remote host/port in access log](#request-headers-for-remote-in-access-log)
- [Operating system support for Vespa artifacts](#operating-system)
- [RPMs](#supported-rpm-os)
- [OCI containers (Docker containers)](#supported-container-os)
- [Other changes](#other-changes)
- [Unknown rank profiles](#unknown-rank-profiles)
- [Unknown summary classes](#unknown-summary-classes)
- [The "qrserver" service name](#qrserver-service-name)
- [Container access logs](#container-access-logs)
- [ONNX output in summary features](#onnx-in-summary-features)
- [Changes in rankfeatures](#rankfeatures)
- [The "storage" message bus routing policy is removed](#storage-routing-policy)
- [vespa-dispatch-bin process is removed](#vespa-dispatch-bin-process-is-removed)
- [YQL format](#yql-format)
- [Upgrade procedure](#upgrade-procedure)

