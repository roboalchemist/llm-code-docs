# Source: https://cdk8s.io/docs/latest/reference/cdk8s/java/

Title: Java - cdk8s

URL Source: https://cdk8s.io/docs/latest/reference/cdk8s/java/

Markdown Content:
Skip to content
cdk8s
Java
Initializing search
 cdk8s-team/cdk8s
What is cdk8s?
Getting started
Basics
cdk8s+
CLI
API Reference
cdk8s
TypeScript
Python
Java
Go
cdk8s-plus-31
cdk8s-plus-32
cdk8s-plus-33
Examples
Ecosystem Interoperability
Migrating from 1.x
Support
Changelog
Roadmap
Contribution guide
Media
On this page
Constructs
ApiObject
App
Chart
Helm
Include
Structs
ApiObjectMetadata
ApiObjectMetadataDefinitionOptions
ApiObjectProps
AppProps
ChartProps
CronOptions
GroupVersionKind
HelmProps
IncludeProps
NameOptions
OwnerReference
SizeConversionOptions
TimeConversionOptions
Classes
ApiObjectMetadataDefinition
Cron
DependencyGraph
DependencyVertex
Duration
ImplicitTokenResolver
JsonPatch
Lazy
LazyResolver
Names
NumberStringUnionResolver
ResolutionContext
Size
Testing
Yaml
Protocols
IAnyProducer
IResolver
Enums
SizeRoundingBehavior
YamlOutputType
cdk8s (Java) ¶
Constructs ¶
ApiObject ¶
Initializers ¶
import org.cdk8s.ApiObject;

ApiObject.Builder.create(Construct scope, java.lang.String id)
    .apiVersion(java.lang.String)
    .kind(java.lang.String)
//  .metadata(ApiObjectMetadata)
    .build();

Name	Type	Description
scope	software.constructs.Construct	the construct scope.
id	java.lang.String	namespace.
apiVersion	java.lang.String	API version.
kind	java.lang.String	Resource kind.
metadata	ApiObjectMetadata	Object metadata.
scopeRequired ¶
Type: software.constructs.Construct

the construct scope.

idRequired ¶
Type: java.lang.String

namespace.

apiVersionRequired ¶
Type: java.lang.String

API version.

kindRequired ¶
Type: java.lang.String

Resource kind.

metadataOptional ¶
Type: ApiObjectMetadata

Object metadata.

If name is not specified, an app-unique name will be allocated by the framework based on the path of the construct within thes construct tree.

Methods ¶
Name	Description
toString	Returns a string representation of this construct.
with	Applies one or more mixins to this construct.
addDependency	Create a dependency between this ApiObject and other constructs.
addJsonPatch	Applies a set of RFC-6902 JSON-Patch operations to the manifest synthesized for this API object.
toJson	Renders the object to Kubernetes JSON.
toString ¶
public java.lang.String toString()


Returns a string representation of this construct.

with ¶
public IConstruct with(IMixin... mixins)


Applies one or more mixins to this construct.

Mixins are applied in order. The list of constructs is captured at the start of the call, so constructs added by a mixin will not be visited. Use multiple with() calls if subsequent mixins should apply to added constructs.

mixinsRequired ¶
Type: software.constructs.IMixin…

The mixins to apply.

addDependency ¶
public void addDependency(IConstruct... dependencies)


Create a dependency between this ApiObject and other constructs.

These can be other ApiObjects, Charts, or custom.

dependenciesRequired ¶
Type: software.constructs.IConstruct…

the dependencies to add.

addJsonPatch ¶
public void addJsonPatch(JsonPatch... ops)


Applies a set of RFC-6902 JSON-Patch operations to the manifest synthesized for this API object.

Example

// Example automatically generated from non-compiling source. May contain errors.
kubePod.addJsonPatch(JsonPatch.replace("/spec/enableServiceLinks", true));

opsRequired ¶
Type: JsonPatch…

The JSON-Patch operations to apply.

toJson ¶
public java.lang.Object toJson()


Renders the object to Kubernetes JSON.

To disable sorting of dictionary keys in output object set the CDK8S_DISABLE_SORT environment variable to any non-empty value.

Static Functions ¶
Name	Description
isConstruct	Checks if x is a construct.
isApiObject	Return whether the given object is an ApiObject.
of	Returns the ApiObject named Resource which is a child of the given construct.
isConstruct ¶
import org.cdk8s.ApiObject;

ApiObject.isConstruct(java.lang.Object x)


Checks if x is a construct.

Use this method instead of instanceof to properly detect Construct instances, even when the construct library is symlinked.

Explanation: in JavaScript, multiple copies of the constructs library on disk are seen as independent, completely different libraries. As a consequence, the class Construct in each copy of the constructs library is seen as a different class, and an instance of one class will not test as instanceof the other class. npm install will not create installations like this, but users may manually symlink construct libraries together or use a monorepo tool: in those cases, multiple copies of the constructs library can be accidentally installed, and instanceof will behave unpredictably. It is safest to avoid using instanceof, and using this type-testing method instead.

xRequired ¶
Type: java.lang.Object

Any object.

isApiObject ¶
import org.cdk8s.ApiObject;

ApiObject.isApiObject(java.lang.Object o)


Return whether the given object is an ApiObject.

We do attribute detection since we can’t reliably use ‘instanceof’.

oRequired ¶
Type: java.lang.Object

The object to check.

of ¶
import org.cdk8s.ApiObject;

ApiObject.of(IConstruct c)


Returns the ApiObject named Resource which is a child of the given construct.

If c is an ApiObject, it is returned directly. Throws an exception if the construct does not have a child named Default or if this child is not an ApiObject.

cRequired ¶
Type: software.constructs.IConstruct

The higher-level construct.

Properties ¶
Name	Type	Description
node	software.constructs.Node	The tree node.
apiGroup	java.lang.String	The group portion of the API version (e.g. authorization.k8s.io).
apiVersion	java.lang.String	The object’s API version (e.g. authorization.k8s.io/v1).
chart	Chart	The chart in which this object is defined.
kind	java.lang.String	The object kind.
metadata	ApiObjectMetadataDefinition	Metadata associated with this API object.
name	java.lang.String	The name of the API object.
nodeRequired ¶
public Node getNode();

Type: software.constructs.Node

The tree node.

apiGroupRequired ¶
public java.lang.String getApiGroup();

Type: java.lang.String

The group portion of the API version (e.g. authorization.k8s.io).

apiVersionRequired ¶
public java.lang.String getApiVersion();

Type: java.lang.String

The object’s API version (e.g. authorization.k8s.io/v1).

chartRequired ¶
public Chart getChart();

Type: Chart

The chart in which this object is defined.

kindRequired ¶
public java.lang.String getKind();

Type: java.lang.String

The object kind.

metadataRequired ¶
public ApiObjectMetadataDefinition getMetadata();

Type: ApiObjectMetadataDefinition

Metadata associated with this API object.

nameRequired ¶
public java.lang.String getName();

Type: java.lang.String

The name of the API object.

If a name is specified in metadata.name this will be the name returned. Otherwise, a name will be generated by calling Chart.of(this).generatedObjectName(this), which by default uses the construct path to generate a DNS-compatible name for the resource.

App ¶

Represents a cdk8s application.

Initializers ¶
import org.cdk8s.App;

App.Builder.create()
//  .outdir(java.lang.String)
//  .outputFileExtension(java.lang.String)
//  .recordConstructMetadata(java.lang.Boolean)
//  .resolvers(java.util.List<IResolver>)
//  .yamlOutputType(YamlOutputType)
    .build();

Name	Type	Description
outdir	java.lang.String	The directory to output Kubernetes manifests.
outputFileExtension	java.lang.String	The file extension to use for rendered YAML files.
recordConstructMetadata	java.lang.Boolean	When set to true, the output directory will contain a construct-metadata.json file that holds construct related metadata on every resource in the app.
resolvers	java.util.List<IResolver>	A list of resolvers that can be used to replace property values before they are written to the manifest file.
yamlOutputType	YamlOutputType	How to divide the YAML output into files.
outdirOptional ¶
Type: java.lang.String
Default: CDK8S_OUTDIR if defined, otherwise “dist”

The directory to output Kubernetes manifests.

If you synthesize your application using cdk8s synth, you must also pass this value to the CLI using the --output option or the output property in the cdk8s.yaml configuration file. Otherwise, the CLI will not know about the output directory, and synthesis will fail.

This property is intended for internal and testing use.

outputFileExtensionOptional ¶
Type: java.lang.String
Default: .k8s.yaml

The file extension to use for rendered YAML files.

recordConstructMetadataOptional ¶
Type: java.lang.Boolean
Default: false

When set to true, the output directory will contain a construct-metadata.json file that holds construct related metadata on every resource in the app.

resolversOptional ¶
Type: java.util.List<IResolver>
Default: no resolvers.

A list of resolvers that can be used to replace property values before they are written to the manifest file.

When multiple resolvers are passed, they are invoked by order in the list, and only the first one that applies (e.g calls context.replaceValue) is invoked.

https://cdk8s.io/docs/latest/basics/app/#resolvers

yamlOutputTypeOptional ¶
Type: YamlOutputType
Default: YamlOutputType.FILE_PER_CHART

How to divide the YAML output into files.

Methods ¶
Name	Description
toString	Returns a string representation of this construct.
with	Applies one or more mixins to this construct.
synth	Synthesizes all manifests to the output directory.
synthYaml	Synthesizes the app into a YAML string.
toString ¶
public java.lang.String toString()


Returns a string representation of this construct.

with ¶
public IConstruct with(IMixin... mixins)


Applies one or more mixins to this construct.

Mixins are applied in order. The list of constructs is captured at the start of the call, so constructs added by a mixin will not be visited. Use multiple with() calls if subsequent mixins should apply to added constructs.

mixinsRequired ¶
Type: software.constructs.IMixin…

The mixins to apply.

synth ¶
public void synth()


Synthesizes all manifests to the output directory.

synthYaml ¶
public java.lang.String synthYaml()


Synthesizes the app into a YAML string.

Static Functions ¶
Name	Description
isConstruct	Checks if x is a construct.
of	No description.
isConstruct ¶
import org.cdk8s.App;

App.isConstruct(java.lang.Object x)


Checks if x is a construct.

Use this method instead of instanceof to properly detect Construct instances, even when the construct library is symlinked.

Explanation: in JavaScript, multiple copies of the constructs library on disk are seen as independent, completely different libraries. As a consequence, the class Construct in each copy of the constructs library is seen as a different class, and an instance of one class will not test as instanceof the other class. npm install will not create installations like this, but users may manually symlink construct libraries together or use a monorepo tool: in those cases, multiple copies of the constructs library can be accidentally installed, and instanceof will behave unpredictably. It is safest to avoid using instanceof, and using this type-testing method instead.

xRequired ¶
Type: java.lang.Object

Any object.

of ¶
import org.cdk8s.App;

App.of(IConstruct c)

cRequired ¶
Type: software.constructs.IConstruct
Properties ¶
Name	Type	Description
node	software.constructs.Node	The tree node.
charts	java.util.List<Chart>	Returns all the charts in this app, sorted topologically.
outdir	java.lang.String	The output directory into which manifests will be synthesized.
outputFileExtension	java.lang.String	The file extension to use for rendered YAML files.
resolvers	java.util.List<IResolver>	Resolvers used by this app.
yamlOutputType	YamlOutputType	How to divide the YAML output into files.
nodeRequired ¶
public Node getNode();

Type: software.constructs.Node

The tree node.

chartsRequired ¶
public java.util.List<Chart> getCharts();

Type: java.util.List<Chart>

Returns all the charts in this app, sorted topologically.

outdirRequired ¶
public java.lang.String getOutdir();

Type: java.lang.String

The output directory into which manifests will be synthesized.

outputFileExtensionRequired ¶
public java.lang.String getOutputFileExtension();

Type: java.lang.String
Default: .k8s.yaml

The file extension to use for rendered YAML files.

resolversRequired ¶
public java.util.List<IResolver> getResolvers();

Type: java.util.List<IResolver>

Resolvers used by this app.

This includes both custom resolvers passed by the resolvers property, as well as built-in resolvers.

yamlOutputTypeRequired ¶
public YamlOutputType getYamlOutputType();

Type: YamlOutputType
Default: YamlOutputType.FILE_PER_CHART

How to divide the YAML output into files.

Chart ¶
Initializers ¶
import org.cdk8s.Chart;

Chart.Builder.create(Construct scope, java.lang.String id)
//  .disableResourceNameHashes(java.lang.Boolean)
//  .labels(java.util.Map<java.lang.String, java.lang.String>)
//  .namespace(java.lang.String)
    .build();

Name	Type	Description
scope	software.constructs.Construct	No description.
id	java.lang.String	No description.
disableResourceNameHashes	java.lang.Boolean	The autogenerated resource name by default is suffixed with a stable hash of the construct path.
labels	java.util.Map	Labels to apply to all resources in this chart.
namespace	java.lang.String	The default namespace for all objects defined in this chart (directly or indirectly).
scopeRequired ¶
Type: software.constructs.Construct
idRequired ¶
Type: java.lang.String
disableResourceNameHashesOptional ¶
Type: java.lang.Boolean
Default: false

The autogenerated resource name by default is suffixed with a stable hash of the construct path.

Setting this property to true drops the hash suffix.

labelsOptional ¶
Type: java.util.Map
Default: no common labels

Labels to apply to all resources in this chart.

namespaceOptional ¶
Type: java.lang.String
Default: no namespace is synthesized (usually this implies “default”)

The default namespace for all objects defined in this chart (directly or indirectly).

This namespace will only apply to objects that don’t have a namespace explicitly defined for them.

Methods ¶
Name	Description
toString	Returns a string representation of this construct.
with	Applies one or more mixins to this construct.
addDependency	Create a dependency between this Chart and other constructs.
generateObjectName	Generates a app-unique name for an object given it’s construct node path.
toJson	Renders this chart to a set of Kubernetes JSON resources.
toString ¶
public java.lang.String toString()


Returns a string representation of this construct.

with ¶
public IConstruct with(IMixin... mixins)


Applies one or more mixins to this construct.

Mixins are applied in order. The list of constructs is captured at the start of the call, so constructs added by a mixin will not be visited. Use multiple with() calls if subsequent mixins should apply to added constructs.

mixinsRequired ¶
Type: software.constructs.IMixin…

The mixins to apply.

addDependency ¶
public void addDependency(IConstruct... dependencies)


Create a dependency between this Chart and other constructs.

These can be other ApiObjects, Charts, or custom.

dependenciesRequired ¶
Type: software.constructs.IConstruct…

the dependencies to add.

generateObjectName ¶
public java.lang.String generateObjectName(ApiObject apiObject)


Generates a app-unique name for an object given it’s construct node path.

Different resource types may have different constraints on names (metadata.name). The previous version of the name generator was compatible with DNS_SUBDOMAIN but not with DNS_LABEL.

For example, Deployment names must comply with DNS_SUBDOMAIN while Service names must comply with DNS_LABEL.

Since there is no formal specification for this, the default name generation scheme for kubernetes objects in cdk8s was changed to DNS_LABEL, since it’s the common denominator for all kubernetes resources (supposedly).

You can override this method if you wish to customize object names at the chart level.

apiObjectRequired ¶
Type: ApiObject

The API object to generate a name for.

toJson ¶
public java.util.List<java.lang.Object> toJson()


Renders this chart to a set of Kubernetes JSON resources.

Static Functions ¶
Name	Description
isConstruct	Checks if x is a construct.
isChart	Return whether the given object is a Chart.
of	Finds the chart in which a node is defined.
isConstruct ¶
import org.cdk8s.Chart;

Chart.isConstruct(java.lang.Object x)


Checks if x is a construct.

Use this method instead of instanceof to properly detect Construct instances, even when the construct library is symlinked.

Explanation: in JavaScript, multiple copies of the constructs library on disk are seen as independent, completely different libraries. As a consequence, the class Construct in each copy of the constructs library is seen as a different class, and an instance of one class will not test as instanceof the other class. npm install will not create installations like this, but users may manually symlink construct libraries together or use a monorepo tool: in those cases, multiple copies of the constructs library can be accidentally installed, and instanceof will behave unpredictably. It is safest to avoid using instanceof, and using this type-testing method instead.

xRequired ¶
Type: java.lang.Object

Any object.

isChart ¶
import org.cdk8s.Chart;

Chart.isChart(java.lang.Object x)


Return whether the given object is a Chart.

We do attribute detection since we can’t reliably use ‘instanceof’.

xRequired ¶
Type: java.lang.Object
of ¶
import org.cdk8s.Chart;

Chart.of(IConstruct c)


Finds the chart in which a node is defined.

cRequired ¶
Type: software.constructs.IConstruct

a construct node.

Properties ¶
Name	Type	Description
node	software.constructs.Node	The tree node.
apiObjects	java.util.List<ApiObject>	Returns all the included API objects.
labels	java.util.Map	Labels applied to all resources in this chart.
namespace	java.lang.String	The default namespace for all objects in this chart.
nodeRequired ¶
public Node getNode();

Type: software.constructs.Node

The tree node.

apiObjectsRequired ¶
public java.util.List<ApiObject> getApiObjects();

Type: java.util.List<ApiObject>

Returns all the included API objects.

labelsRequired ¶
public java.util.Map<java.lang.String, java.lang.String> getLabels();

Type: java.util.Map

Labels applied to all resources in this chart.

This is an immutable copy.

namespaceOptional ¶
public java.lang.String getNamespace();

Type: java.lang.String

The default namespace for all objects in this chart.

Helm ¶

Represents a Helm deployment.

Use this construct to import an existing Helm chart and incorporate it into your constructs.

Initializers ¶
import org.cdk8s.Helm;

Helm.Builder.create(Construct scope, java.lang.String id)
    .chart(java.lang.String)
//  .helmExecutable(java.lang.String)
//  .helmFlags(java.util.List<java.lang.String>)
//  .namespace(java.lang.String)
//  .releaseName(java.lang.String)
//  .repo(java.lang.String)
//  .values(java.util.Map<java.lang.String, java.lang.Object>)
//  .version(java.lang.String)
    .build();

Name	Type	Description
scope	software.constructs.Construct	No description.
id	java.lang.String	No description.
chart	java.lang.String	The chart name to use. It can be a chart from a helm repository or a local directory.
helmExecutable	java.lang.String	The local helm executable to use in order to create the manifest the chart.
helmFlags	java.util.List	Additional flags to add to the helm execution.
namespace	java.lang.String	Scope all resources in to a given namespace.
releaseName	java.lang.String	The release name.
repo	java.lang.String	Chart repository url where to locate the requested chart.
values	java.util.Map	Values to pass to the chart.
version	java.lang.String	Version constraint for the chart version to use.
scopeRequired ¶
Type: software.constructs.Construct
idRequired ¶
Type: java.lang.String
chartRequired ¶
Type: java.lang.String

The chart name to use. It can be a chart from a helm repository or a local directory.

This name is passed to helm template and has all the relevant semantics.

Example

"bitnami/redis";

helmExecutableOptional ¶
Type: java.lang.String
Default: “helm”

The local helm executable to use in order to create the manifest the chart.

helmFlagsOptional ¶
Type: java.util.List
Default: []

Additional flags to add to the helm execution.

namespaceOptional ¶
Type: java.lang.String

Scope all resources in to a given namespace.

releaseNameOptional ¶
Type: java.lang.String
Default: if unspecified, a name will be allocated based on the construct path

The release name.

https://helm.sh/docs/intro/using_helm/#three-big-concepts

repoOptional ¶
Type: java.lang.String

Chart repository url where to locate the requested chart.

valuesOptional ¶
Type: java.util.Map
Default: If no values are specified, chart will use the defaults.

Values to pass to the chart.

versionOptional ¶
Type: java.lang.String

Version constraint for the chart version to use.

This constraint can be a specific tag (e.g. 1.1.1) or it may reference a valid range (e.g. ^2.0.0). If this is not specified, the latest version is used

This name is passed to helm template --version and has all the relevant semantics.

Example

"^2.0.0";

Methods ¶
Name	Description
toString	Returns a string representation of this construct.
with	Applies one or more mixins to this construct.
toString ¶
public java.lang.String toString()


Returns a string representation of this construct.

with ¶
public IConstruct with(IMixin... mixins)


Applies one or more mixins to this construct.

Mixins are applied in order. The list of constructs is captured at the start of the call, so constructs added by a mixin will not be visited. Use multiple with() calls if subsequent mixins should apply to added constructs.

mixinsRequired ¶
Type: software.constructs.IMixin…

The mixins to apply.

Static Functions ¶
Name	Description
isConstruct	Checks if x is a construct.
isConstruct ¶
import org.cdk8s.Helm;

Helm.isConstruct(java.lang.Object x)


Checks if x is a construct.

Use this method instead of instanceof to properly detect Construct instances, even when the construct library is symlinked.

Explanation: in JavaScript, multiple copies of the constructs library on disk are seen as independent, completely different libraries. As a consequence, the class Construct in each copy of the constructs library is seen as a different class, and an instance of one class will not test as instanceof the other class. npm install will not create installations like this, but users may manually symlink construct libraries together or use a monorepo tool: in those cases, multiple copies of the constructs library can be accidentally installed, and instanceof will behave unpredictably. It is safest to avoid using instanceof, and using this type-testing method instead.

xRequired ¶
Type: java.lang.Object

Any object.

Properties ¶
Name	Type	Description
node	software.constructs.Node	The tree node.
apiObjects	java.util.List<ApiObject>	Returns all the included API objects.
releaseName	java.lang.String	The helm release name.
nodeRequired ¶
public Node getNode();

Type: software.constructs.Node

The tree node.

apiObjectsRequired ¶
public java.util.List<ApiObject> getApiObjects();

Type: java.util.List<ApiObject>

Returns all the included API objects.

releaseNameRequired ¶
public java.lang.String getReleaseName();

Type: java.lang.String

The helm release name.

Include ¶

Reads a YAML manifest from a file or a URL and defines all resources as API objects within the defined scope.

The names (metadata.name) of imported resources will be preserved as-is from the manifest.

Initializers ¶
import org.cdk8s.Include;

Include.Builder.create(Construct scope, java.lang.String id)
    .url(java.lang.String)
    .build();

Name	Type	Description
scope	software.constructs.Construct	No description.
id	java.lang.String	No description.
url	java.lang.String	Local file path or URL which includes a Kubernetes YAML manifest.
scopeRequired ¶
Type: software.constructs.Construct
idRequired ¶
Type: java.lang.String
urlRequired ¶
Type: java.lang.String

Local file path or URL which includes a Kubernetes YAML manifest.

Example

// Example automatically generated from non-compiling source. May contain errors.
mymanifest.getYaml();

Methods ¶
Name	Description
toString	Returns a string representation of this construct.
with	Applies one or more mixins to this construct.
toString ¶
public java.lang.String toString()


Returns a string representation of this construct.

with ¶
public IConstruct with(IMixin... mixins)


Applies one or more mixins to this construct.

Mixins are applied in order. The list of constructs is captured at the start of the call, so constructs added by a mixin will not be visited. Use multiple with() calls if subsequent mixins should apply to added constructs.

mixinsRequired ¶
Type: software.constructs.IMixin…

The mixins to apply.

Static Functions ¶
Name	Description
isConstruct	Checks if x is a construct.
isConstruct ¶
import org.cdk8s.Include;

Include.isConstruct(java.lang.Object x)


Checks if x is a construct.

Use this method instead of instanceof to properly detect Construct instances, even when the construct library is symlinked.

Explanation: in JavaScript, multiple copies of the constructs library on disk are seen as independent, completely different libraries. As a consequence, the class Construct in each copy of the constructs library is seen as a different class, and an instance of one class will not test as instanceof the other class. npm install will not create installations like this, but users may manually symlink construct libraries together or use a monorepo tool: in those cases, multiple copies of the constructs library can be accidentally installed, and instanceof will behave unpredictably. It is safest to avoid using instanceof, and using this type-testing method instead.

xRequired ¶
Type: java.lang.Object

Any object.

Properties ¶
Name	Type	Description
node	software.constructs.Node	The tree node.
apiObjects	java.util.List<ApiObject>	Returns all the included API objects.
nodeRequired ¶
public Node getNode();

Type: software.constructs.Node

The tree node.

apiObjectsRequired ¶
public java.util.List<ApiObject> getApiObjects();

Type: java.util.List<ApiObject>

Returns all the included API objects.

Structs ¶
ApiObjectMetadata ¶

Metadata associated with this object.

Initializer ¶
import org.cdk8s.ApiObjectMetadata;

ApiObjectMetadata.builder()
//  .annotations(java.util.Map<java.lang.String, java.lang.String>)
//  .finalizers(java.util.List<java.lang.String>)
//  .labels(java.util.Map<java.lang.String, java.lang.String>)
//  .name(java.lang.String)
//  .namespace(java.lang.String)
//  .ownerReferences(java.util.List<OwnerReference>)
    .build();

Properties ¶
Name	Type	Description
annotations	java.util.Map	Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata.
finalizers	java.util.List	Namespaced keys that tell Kubernetes to wait until specific conditions are met before it fully deletes resources marked for deletion.
labels	java.util.Map	Map of string keys and values that can be used to organize and categorize (scope and select) objects.
name	java.lang.String	The unique, namespace-global, name of this object inside the Kubernetes cluster.
namespace	java.lang.String	Namespace defines the space within each name must be unique.
ownerReferences	java.util.List<OwnerReference>	List of objects depended by this object.
annotationsOptional ¶
public java.util.Map<java.lang.String, java.lang.String> getAnnotations();

Type: java.util.Map
Default: No annotations.

Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata.

They are not queryable and should be preserved when modifying objects.

http://kubernetes.io/docs/user-guide/annotations

finalizersOptional ¶
public java.util.List<java.lang.String> getFinalizers();

Type: java.util.List
Default: No finalizers.

Namespaced keys that tell Kubernetes to wait until specific conditions are met before it fully deletes resources marked for deletion.

Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.

https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/

labelsOptional ¶
public java.util.Map<java.lang.String, java.lang.String> getLabels();

Type: java.util.Map
Default: No labels.

Map of string keys and values that can be used to organize and categorize (scope and select) objects.

May match selectors of replication controllers and services.

http://kubernetes.io/docs/user-guide/labels

nameOptional ¶
public java.lang.String getName();

Type: java.lang.String
Default: an app-unique name generated by the chart

The unique, namespace-global, name of this object inside the Kubernetes cluster.

Normally, you shouldn’t specify names for objects and let the CDK generate a name for you that is application-unique. The names CDK generates are composed from the construct path components, separated by dots and a suffix that is based on a hash of the entire path, to ensure uniqueness.

You can supply custom name allocation logic by overriding the chart.generateObjectName method.

If you use an explicit name here, bear in mind that this reduces the composability of your construct because it won’t be possible to include more than one instance in any app. Therefore it is highly recommended to leave this unspecified.

namespaceOptional ¶
public java.lang.String getNamespace();

Type: java.lang.String
Default: undefined (will be assigned to the ‘default’ namespace)

Namespace defines the space within each name must be unique.

An empty namespace is equivalent to the “default” namespace, but “default” is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty. Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces

ownerReferencesOptional ¶
public java.util.List<OwnerReference> getOwnerReferences();

Type: java.util.List<OwnerReference>
Default: automatically set by Kubernetes

List of objects depended by this object.

If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.

Kubernetes sets the value of this field automatically for objects that are dependents of other objects like ReplicaSets, DaemonSets, Deployments, Jobs and CronJobs, and ReplicationControllers. You can also configure these relationships manually by changing the value of this field. However, you usually don’t need to and can allow Kubernetes to automatically manage the relationships.

https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/

ApiObjectMetadataDefinitionOptions ¶

Options for ApiObjectMetadataDefinition.

Initializer ¶
import org.cdk8s.ApiObjectMetadataDefinitionOptions;

ApiObjectMetadataDefinitionOptions.builder()
//  .annotations(java.util.Map<java.lang.String, java.lang.String>)
//  .finalizers(java.util.List<java.lang.String>)
//  .labels(java.util.Map<java.lang.String, java.lang.String>)
//  .name(java.lang.String)
//  .namespace(java.lang.String)
//  .ownerReferences(java.util.List<OwnerReference>)
    .apiObject(ApiObject)
    .build();

Properties ¶
Name	Type	Description
annotations	java.util.Map	Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata.
finalizers	java.util.List	Namespaced keys that tell Kubernetes to wait until specific conditions are met before it fully deletes resources marked for deletion.
labels	java.util.Map	Map of string keys and values that can be used to organize and categorize (scope and select) objects.
name	java.lang.String	The unique, namespace-global, name of this object inside the Kubernetes cluster.
namespace	java.lang.String	Namespace defines the space within each name must be unique.
ownerReferences	java.util.List<OwnerReference>	List of objects depended by this object.
apiObject	ApiObject	Which ApiObject instance is the metadata attached to.
annotationsOptional ¶
public java.util.Map<java.lang.String, java.lang.String> getAnnotations();

Type: java.util.Map
Default: No annotations.

Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata.

They are not queryable and should be preserved when modifying objects.

http://kubernetes.io/docs/user-guide/annotations

finalizersOptional ¶
public java.util.List<java.lang.String> getFinalizers();

Type: java.util.List
Default: No finalizers.

Namespaced keys that tell Kubernetes to wait until specific conditions are met before it fully deletes resources marked for deletion.

Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.

https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/

labelsOptional ¶
public java.util.Map<java.lang.String, java.lang.String> getLabels();

Type: java.util.Map
Default: No labels.

Map of string keys and values that can be used to organize and categorize (scope and select) objects.

May match selectors of replication controllers and services.

http://kubernetes.io/docs/user-guide/labels

nameOptional ¶
public java.lang.String getName();

Type: java.lang.String
Default: an app-unique name generated by the chart

The unique, namespace-global, name of this object inside the Kubernetes cluster.

Normally, you shouldn’t specify names for objects and let the CDK generate a name for you that is application-unique. The names CDK generates are composed from the construct path components, separated by dots and a suffix that is based on a hash of the entire path, to ensure uniqueness.

You can supply custom name allocation logic by overriding the chart.generateObjectName method.

If you use an explicit name here, bear in mind that this reduces the composability of your construct because it won’t be possible to include more than one instance in any app. Therefore it is highly recommended to leave this unspecified.

namespaceOptional ¶
public java.lang.String getNamespace();

Type: java.lang.String
Default: undefined (will be assigned to the ‘default’ namespace)

Namespace defines the space within each name must be unique.

An empty namespace is equivalent to the “default” namespace, but “default” is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty. Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces

ownerReferencesOptional ¶
public java.util.List<OwnerReference> getOwnerReferences();

Type: java.util.List<OwnerReference>
Default: automatically set by Kubernetes

List of objects depended by this object.

If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.

Kubernetes sets the value of this field automatically for objects that are dependents of other objects like ReplicaSets, DaemonSets, Deployments, Jobs and CronJobs, and ReplicationControllers. You can also configure these relationships manually by changing the value of this field. However, you usually don’t need to and can allow Kubernetes to automatically manage the relationships.

https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/

apiObjectRequired ¶
public ApiObject getApiObject();

Type: ApiObject

Which ApiObject instance is the metadata attached to.

ApiObjectProps ¶

Options for defining API objects.

Initializer ¶
import org.cdk8s.ApiObjectProps;

ApiObjectProps.builder()
    .apiVersion(java.lang.String)
    .kind(java.lang.String)
//  .metadata(ApiObjectMetadata)
    .build();

Properties ¶
Name	Type	Description
apiVersion	java.lang.String	API version.
kind	java.lang.String	Resource kind.
metadata	ApiObjectMetadata	Object metadata.
apiVersionRequired ¶
public java.lang.String getApiVersion();

Type: java.lang.String

API version.

kindRequired ¶
public java.lang.String getKind();

Type: java.lang.String

Resource kind.

metadataOptional ¶
public ApiObjectMetadata getMetadata();

Type: ApiObjectMetadata

Object metadata.

If name is not specified, an app-unique name will be allocated by the framework based on the path of the construct within thes construct tree.

AppProps ¶
Initializer ¶
import org.cdk8s.AppProps;

AppProps.builder()
//  .outdir(java.lang.String)
//  .outputFileExtension(java.lang.String)
//  .recordConstructMetadata(java.lang.Boolean)
//  .resolvers(java.util.List<IResolver>)
//  .yamlOutputType(YamlOutputType)
    .build();

Properties ¶
Name	Type	Description
outdir	java.lang.String	The directory to output Kubernetes manifests.
outputFileExtension	java.lang.String	The file extension to use for rendered YAML files.
recordConstructMetadata	java.lang.Boolean	When set to true, the output directory will contain a construct-metadata.json file that holds construct related metadata on every resource in the app.
resolvers	java.util.List<IResolver>	A list of resolvers that can be used to replace property values before they are written to the manifest file.
yamlOutputType	YamlOutputType	How to divide the YAML output into files.
outdirOptional ¶
public java.lang.String getOutdir();

Type: java.lang.String
Default: CDK8S_OUTDIR if defined, otherwise “dist”

The directory to output Kubernetes manifests.

If you synthesize your application using cdk8s synth, you must also pass this value to the CLI using the --output option or the output property in the cdk8s.yaml configuration file. Otherwise, the CLI will not know about the output directory, and synthesis will fail.

This property is intended for internal and testing use.

outputFileExtensionOptional ¶
public java.lang.String getOutputFileExtension();

Type: java.lang.String
Default: .k8s.yaml

The file extension to use for rendered YAML files.

recordConstructMetadataOptional ¶
public java.lang.Boolean getRecordConstructMetadata();

Type: java.lang.Boolean
Default: false

When set to true, the output directory will contain a construct-metadata.json file that holds construct related metadata on every resource in the app.

resolversOptional ¶
public java.util.List<IResolver> getResolvers();

Type: java.util.List<IResolver>
Default: no resolvers.

A list of resolvers that can be used to replace property values before they are written to the manifest file.

When multiple resolvers are passed, they are invoked by order in the list, and only the first one that applies (e.g calls context.replaceValue) is invoked.

https://cdk8s.io/docs/latest/basics/app/#resolvers

yamlOutputTypeOptional ¶
public YamlOutputType getYamlOutputType();

Type: YamlOutputType
Default: YamlOutputType.FILE_PER_CHART

How to divide the YAML output into files.

ChartProps ¶
Initializer ¶
import org.cdk8s.ChartProps;

ChartProps.builder()
//  .disableResourceNameHashes(java.lang.Boolean)
//  .labels(java.util.Map<java.lang.String, java.lang.String>)
//  .namespace(java.lang.String)
    .build();

Properties ¶
Name	Type	Description
disableResourceNameHashes	java.lang.Boolean	The autogenerated resource name by default is suffixed with a stable hash of the construct path.
labels	java.util.Map	Labels to apply to all resources in this chart.
namespace	java.lang.String	The default namespace for all objects defined in this chart (directly or indirectly).
disableResourceNameHashesOptional ¶
public java.lang.Boolean getDisableResourceNameHashes();

Type: java.lang.Boolean
Default: false

The autogenerated resource name by default is suffixed with a stable hash of the construct path.

Setting this property to true drops the hash suffix.

labelsOptional ¶
public java.util.Map<java.lang.String, java.lang.String> getLabels();

Type: java.util.Map
Default: no common labels

Labels to apply to all resources in this chart.

namespaceOptional ¶
public java.lang.String getNamespace();

Type: java.lang.String
Default: no namespace is synthesized (usually this implies “default”)

The default namespace for all objects defined in this chart (directly or indirectly).

This namespace will only apply to objects that don’t have a namespace explicitly defined for them.

CronOptions ¶

Options to configure a cron expression.

All fields are strings so you can use complex expressions. Absence of a field implies ‘*’

Initializer ¶
import org.cdk8s.CronOptions;

CronOptions.builder()
//  .day(java.lang.String)
//  .hour(java.lang.String)
//  .minute(java.lang.String)
//  .month(java.lang.String)
//  .weekDay(java.lang.String)
    .build();

Properties ¶
Name	Type	Description
day	java.lang.String	The day of the month to run this rule at.
hour	java.lang.String	The hour to run this rule at.
minute	java.lang.String	The minute to run this rule at.
month	java.lang.String	The month to run this rule at.
weekDay	java.lang.String	The day of the week to run this rule at.
dayOptional ¶
public java.lang.String getDay();

Type: java.lang.String
Default: Every day of the month

The day of the month to run this rule at.

hourOptional ¶
public java.lang.String getHour();

Type: java.lang.String
Default: Every hour

The hour to run this rule at.

minuteOptional ¶
public java.lang.String getMinute();

Type: java.lang.String
Default: Every minute

The minute to run this rule at.

monthOptional ¶
public java.lang.String getMonth();

Type: java.lang.String
Default: Every month

The month to run this rule at.

weekDayOptional ¶
public java.lang.String getWeekDay();

Type: java.lang.String
Default: Any day of the week

The day of the week to run this rule at.

GroupVersionKind ¶
Initializer ¶
import org.cdk8s.GroupVersionKind;

GroupVersionKind.builder()
    .apiVersion(java.lang.String)
    .kind(java.lang.String)
    .build();

Properties ¶
Name	Type	Description
apiVersion	java.lang.String	The object’s API version (e.g. authorization.k8s.io/v1).
kind	java.lang.String	The object kind.
apiVersionRequired ¶
public java.lang.String getApiVersion();

Type: java.lang.String

The object’s API version (e.g. authorization.k8s.io/v1).

kindRequired ¶
public java.lang.String getKind();

Type: java.lang.String

The object kind.

HelmProps ¶

Options for Helm.

Initializer ¶
import org.cdk8s.HelmProps;

HelmProps.builder()
    .chart(java.lang.String)
//  .helmExecutable(java.lang.String)
//  .helmFlags(java.util.List<java.lang.String>)
//  .namespace(java.lang.String)
//  .releaseName(java.lang.String)
//  .repo(java.lang.String)
//  .values(java.util.Map<java.lang.String, java.lang.Object>)
//  .version(java.lang.String)
    .build();

Properties ¶
Name	Type	Description
chart	java.lang.String	The chart name to use. It can be a chart from a helm repository or a local directory.
helmExecutable	java.lang.String	The local helm executable to use in order to create the manifest the chart.
helmFlags	java.util.List	Additional flags to add to the helm execution.
namespace	java.lang.String	Scope all resources in to a given namespace.
releaseName	java.lang.String	The release name.
repo	java.lang.String	Chart repository url where to locate the requested chart.
values	java.util.Map	Values to pass to the chart.
version	java.lang.String	Version constraint for the chart version to use.
chartRequired ¶
public java.lang.String getChart();

Type: java.lang.String

The chart name to use. It can be a chart from a helm repository or a local directory.

This name is passed to helm template and has all the relevant semantics.

Example

"bitnami/redis";

helmExecutableOptional ¶
public java.lang.String getHelmExecutable();

Type: java.lang.String
Default: “helm”

The local helm executable to use in order to create the manifest the chart.

helmFlagsOptional ¶
public java.util.List<java.lang.String> getHelmFlags();

Type: java.util.List
Default: []

Additional flags to add to the helm execution.

namespaceOptional ¶
public java.lang.String getNamespace();

Type: java.lang.String

Scope all resources in to a given namespace.

releaseNameOptional ¶
public java.lang.String getReleaseName();

Type: java.lang.String
Default: if unspecified, a name will be allocated based on the construct path

The release name.

https://helm.sh/docs/intro/using_helm/#three-big-concepts

repoOptional ¶
public java.lang.String getRepo();

Type: java.lang.String

Chart repository url where to locate the requested chart.

valuesOptional ¶
public java.util.Map<java.lang.String, java.lang.Object> getValues();

Type: java.util.Map
Default: If no values are specified, chart will use the defaults.

Values to pass to the chart.

versionOptional ¶
public java.lang.String getVersion();

Type: java.lang.String

Version constraint for the chart version to use.

This constraint can be a specific tag (e.g. 1.1.1) or it may reference a valid range (e.g. ^2.0.0). If this is not specified, the latest version is used

This name is passed to helm template --version and has all the relevant semantics.

Example

"^2.0.0";

IncludeProps ¶
Initializer ¶
import org.cdk8s.IncludeProps;

IncludeProps.builder()
    .url(java.lang.String)
    .build();

Properties ¶
Name	Type	Description
url	java.lang.String	Local file path or URL which includes a Kubernetes YAML manifest.
urlRequired ¶
public java.lang.String getUrl();

Type: java.lang.String

Local file path or URL which includes a Kubernetes YAML manifest.

Example

// Example automatically generated from non-compiling source. May contain errors.
mymanifest.getYaml();

NameOptions ¶

Options for name generation.

Initializer ¶
import org.cdk8s.NameOptions;

NameOptions.builder()
//  .delimiter(java.lang.String)
//  .extra(java.util.List<java.lang.String>)
//  .includeHash(java.lang.Boolean)
//  .maxLen(java.lang.Number)
    .build();

Properties ¶
Name	Type	Description
delimiter	java.lang.String	Delimiter to use between components.
extra	java.util.List	Extra components to include in the name.
includeHash	java.lang.Boolean	Include a short hash as last part of the name.
maxLen	java.lang.Number	Maximum allowed length for the name.
delimiterOptional ¶
public java.lang.String getDelimiter();

Type: java.lang.String
Default: “-“

Delimiter to use between components.

extraOptional ¶
public java.util.List<java.lang.String> getExtra();

Type: java.util.List
Default: [] use the construct path components

Extra components to include in the name.

includeHashOptional ¶
public java.lang.Boolean getIncludeHash();

Type: java.lang.Boolean
Default: true

Include a short hash as last part of the name.

maxLenOptional ¶
public java.lang.Number getMaxLen();

Type: java.lang.Number
Default: 63

Maximum allowed length for the name.

OwnerReference ¶

OwnerReference contains enough information to let you identify an owning object.

An owning object must be in the same namespace as the dependent, or be cluster-scoped, so there is no namespace field.

Initializer ¶
import org.cdk8s.OwnerReference;

OwnerReference.builder()
    .apiVersion(java.lang.String)
    .kind(java.lang.String)
    .name(java.lang.String)
    .uid(java.lang.String)
//  .blockOwnerDeletion(java.lang.Boolean)
//  .controller(java.lang.Boolean)
    .build();

Properties ¶
Name	Type	Description
apiVersion	java.lang.String	API version of the referent.
kind	java.lang.String	Kind of the referent.
name	java.lang.String	Name of the referent.
uid	java.lang.String	UID of the referent.
blockOwnerDeletion	java.lang.Boolean	If true, AND if the owner has the “foregroundDeletion” finalizer, then the owner cannot be deleted from the key-value store until this reference is removed.
controller	java.lang.Boolean	If true, this reference points to the managing controller.
apiVersionRequired ¶
public java.lang.String getApiVersion();

Type: java.lang.String

API version of the referent.

kindRequired ¶
public java.lang.String getKind();

Type: java.lang.String

Kind of the referent.

https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds

nameRequired ¶
public java.lang.String getName();

Type: java.lang.String

Name of the referent.

http://kubernetes.io/docs/user-guide/identifiers#names

uidRequired ¶
public java.lang.String getUid();

Type: java.lang.String

UID of the referent.

http://kubernetes.io/docs/user-guide/identifiers#uids

blockOwnerDeletionOptional ¶
public java.lang.Boolean getBlockOwnerDeletion();

Type: java.lang.Boolean
Default: false. To set this field, a user needs “delete” permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.

If true, AND if the owner has the “foregroundDeletion” finalizer, then the owner cannot be deleted from the key-value store until this reference is removed.

Defaults to false. To set this field, a user needs “delete” permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.

controllerOptional ¶
public java.lang.Boolean getController();

Type: java.lang.Boolean

If true, this reference points to the managing controller.

SizeConversionOptions ¶

Options for how to convert size to a different unit.

Initializer ¶
import org.cdk8s.SizeConversionOptions;

SizeConversionOptions.builder()
//  .rounding(SizeRoundingBehavior)
    .build();

Properties ¶
Name	Type	Description
rounding	SizeRoundingBehavior	How conversions should behave when it encounters a non-integer result.
roundingOptional ¶
public SizeRoundingBehavior getRounding();

Type: SizeRoundingBehavior
Default: SizeRoundingBehavior.FAIL

How conversions should behave when it encounters a non-integer result.

TimeConversionOptions ¶

Options for how to convert time to a different unit.

Initializer ¶
import org.cdk8s.TimeConversionOptions;

TimeConversionOptions.builder()
//  .integral(java.lang.Boolean)
    .build();

Properties ¶
Name	Type	Description
integral	java.lang.Boolean	If true, conversions into a larger time unit (e.g. Seconds to Minutes) will fail if the result is not an integer.
integralOptional ¶
public java.lang.Boolean getIntegral();

Type: java.lang.Boolean
Default: true

If true, conversions into a larger time unit (e.g. Seconds to Minutes) will fail if the result is not an integer.

Classes ¶
ApiObjectMetadataDefinition ¶

Object metadata.

Initializers ¶
import org.cdk8s.ApiObjectMetadataDefinition;

ApiObjectMetadataDefinition.Builder.create()
//  .annotations(java.util.Map<java.lang.String, java.lang.String>)
//  .finalizers(java.util.List<java.lang.String>)
//  .labels(java.util.Map<java.lang.String, java.lang.String>)
//  .name(java.lang.String)
//  .namespace(java.lang.String)
//  .ownerReferences(java.util.List<OwnerReference>)
    .apiObject(ApiObject)
    .build();

Name	Type	Description
annotations	java.util.Map	Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata.
finalizers	java.util.List	Namespaced keys that tell Kubernetes to wait until specific conditions are met before it fully deletes resources marked for deletion.
labels	java.util.Map	Map of string keys and values that can be used to organize and categorize (scope and select) objects.
name	java.lang.String	The unique, namespace-global, name of this object inside the Kubernetes cluster.
namespace	java.lang.String	Namespace defines the space within each name must be unique.
ownerReferences	java.util.List<OwnerReference>	List of objects depended by this object.
apiObject	ApiObject	Which ApiObject instance is the metadata attached to.
annotationsOptional ¶
Type: java.util.Map
Default: No annotations.

Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata.

They are not queryable and should be preserved when modifying objects.

http://kubernetes.io/docs/user-guide/annotations

finalizersOptional ¶
Type: java.util.List
Default: No finalizers.

Namespaced keys that tell Kubernetes to wait until specific conditions are met before it fully deletes resources marked for deletion.

Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.

https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/

labelsOptional ¶
Type: java.util.Map
Default: No labels.

Map of string keys and values that can be used to organize and categorize (scope and select) objects.

May match selectors of replication controllers and services.

http://kubernetes.io/docs/user-guide/labels

nameOptional ¶
Type: java.lang.String
Default: an app-unique name generated by the chart

The unique, namespace-global, name of this object inside the Kubernetes cluster.

Normally, you shouldn’t specify names for objects and let the CDK generate a name for you that is application-unique. The names CDK generates are composed from the construct path components, separated by dots and a suffix that is based on a hash of the entire path, to ensure uniqueness.

You can supply custom name allocation logic by overriding the chart.generateObjectName method.

If you use an explicit name here, bear in mind that this reduces the composability of your construct because it won’t be possible to include more than one instance in any app. Therefore it is highly recommended to leave this unspecified.

namespaceOptional ¶
Type: java.lang.String
Default: undefined (will be assigned to the ‘default’ namespace)

Namespace defines the space within each name must be unique.

An empty namespace is equivalent to the “default” namespace, but “default” is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty. Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces

ownerReferencesOptional ¶
Type: java.util.List<OwnerReference>
Default: automatically set by Kubernetes

List of objects depended by this object.

If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.

Kubernetes sets the value of this field automatically for objects that are dependents of other objects like ReplicaSets, DaemonSets, Deployments, Jobs and CronJobs, and ReplicationControllers. You can also configure these relationships manually by changing the value of this field. However, you usually don’t need to and can allow Kubernetes to automatically manage the relationships.

https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/

apiObjectRequired ¶
Type: ApiObject

Which ApiObject instance is the metadata attached to.

Methods ¶
Name	Description
add	Adds an arbitrary key/value to the object metadata.
addAnnotation	Add an annotation.
addFinalizers	Add one or more finalizers.
addLabel	Add a label.
addOwnerReference	Add an owner.
getLabel	No description.
toJson	Synthesizes a k8s ObjectMeta for this metadata set.
add ¶
public void add(java.lang.String key, java.lang.Object value)


Adds an arbitrary key/value to the object metadata.

keyRequired ¶
Type: java.lang.String

Metadata key.

valueRequired ¶
Type: java.lang.Object

Metadata value.

addAnnotation ¶
public void addAnnotation(java.lang.String key, java.lang.String value)


Add an annotation.

keyRequired ¶
Type: java.lang.String

The key.

valueRequired ¶
Type: java.lang.String

The value.

addFinalizers ¶
public void addFinalizers(java.lang.String... finalizers)


Add one or more finalizers.

finalizersRequired ¶
Type: java.lang.String…

the finalizers.

addLabel ¶
public void addLabel(java.lang.String key, java.lang.String value)


Add a label.

keyRequired ¶
Type: java.lang.String

The key.

valueRequired ¶
Type: java.lang.String

The value.

addOwnerReference ¶
public void addOwnerReference(OwnerReference owner)


Add an owner.

ownerRequired ¶
Type: OwnerReference

the owner.

getLabel ¶
public java.lang.String getLabel(java.lang.String key)

keyRequired ¶
Type: java.lang.String

the label.

toJson ¶
public java.lang.Object toJson()


Synthesizes a k8s ObjectMeta for this metadata set.

Properties ¶
Name	Type	Description
name	java.lang.String	The name of the API object.
namespace	java.lang.String	The object’s namespace.
nameOptional ¶
public java.lang.String getName();

Type: java.lang.String

The name of the API object.

If a name is specified in metadata.name this will be the name returned. Otherwise, a name will be generated by calling Chart.of(this).generatedObjectName(this), which by default uses the construct path to generate a DNS-compatible name for the resource.

namespaceOptional ¶
public java.lang.String getNamespace();

Type: java.lang.String

The object’s namespace.

Cron ¶

Represents a cron schedule.

Initializers ¶
import org.cdk8s.Cron;

Cron.Builder.create()
//  .day(java.lang.String)
//  .hour(java.lang.String)
//  .minute(java.lang.String)
//  .month(java.lang.String)
//  .weekDay(java.lang.String)
    .build();

Name	Type	Description
day	java.lang.String	The day of the month to run this rule at.
hour	java.lang.String	The hour to run this rule at.
minute	java.lang.String	The minute to run this rule at.
month	java.lang.String	The month to run this rule at.
weekDay	java.lang.String	The day of the week to run this rule at.
dayOptional ¶
Type: java.lang.String
Default: Every day of the month

The day of the month to run this rule at.

hourOptional ¶
Type: java.lang.String
Default: Every hour

The hour to run this rule at.

minuteOptional ¶
Type: java.lang.String
Default: Every minute

The minute to run this rule at.

monthOptional ¶
Type: java.lang.String
Default: Every month

The month to run this rule at.

weekDayOptional ¶
Type: java.lang.String
Default: Any day of the week

The day of the week to run this rule at.

Static Functions ¶
Name	Description
annually	Create a cron schedule which runs first day of January every year.
daily	Create a cron schedule which runs every day at midnight.
everyMinute	Create a cron schedule which runs every minute.
hourly	Create a cron schedule which runs every hour.
monthly	Create a cron schedule which runs first day of every month.
schedule	Create a custom cron schedule from a set of cron fields.
weekly	Create a cron schedule which runs every week on Sunday.
annually ¶
import org.cdk8s.Cron;

Cron.annually()


Create a cron schedule which runs first day of January every year.

daily ¶
import org.cdk8s.Cron;

Cron.daily()


Create a cron schedule which runs every day at midnight.

everyMinute ¶
import org.cdk8s.Cron;

Cron.everyMinute()


Create a cron schedule which runs every minute.

hourly ¶
import org.cdk8s.Cron;

Cron.hourly()


Create a cron schedule which runs every hour.

monthly ¶
import org.cdk8s.Cron;

Cron.monthly()


Create a cron schedule which runs first day of every month.

schedule ¶
import org.cdk8s.Cron;

Cron.schedule(CronOptions options)


Create a custom cron schedule from a set of cron fields.

optionsRequired ¶
Type: CronOptions
weekly ¶
import org.cdk8s.Cron;

Cron.weekly()


Create a cron schedule which runs every week on Sunday.

Properties ¶
Name	Type	Description
expressionString	java.lang.String	Retrieve the expression for this schedule.
expressionStringRequired ¶
public java.lang.String getExpressionString();

Type: java.lang.String

Retrieve the expression for this schedule.

DependencyGraph ¶

Represents the dependency graph for a given Node.

This graph includes the dependency relationships between all nodes in the node (construct) sub-tree who’s root is this Node.

Note that this means that lonely nodes (no dependencies and no dependants) are also included in this graph as childless children of the root node of the graph.

The graph does not include cross-scope dependencies. That is, if a child on the current scope depends on a node from a different scope, that relationship is not represented in this graph.

Initializers ¶
import org.cdk8s.DependencyGraph;

new DependencyGraph(Node node);

Name	Type	Description
node	software.constructs.Node	No description.
nodeRequired ¶
Type: software.constructs.Node
Methods ¶
Name	Description
topology	No description.
topology ¶
public java.util.List<IConstruct> topology()


Vertex.topology ()

Properties ¶
Name	Type	Description
root	DependencyVertex	Returns the root of the graph.
rootRequired ¶
public DependencyVertex getRoot();

Type: DependencyVertex

Returns the root of the graph.

Note that this vertex will always have null as its .value since it is an artifical root that binds all the connected spaces of the graph.

DependencyVertex ¶

Represents a vertex in the graph.

The value of each vertex is an IConstruct that is accessible via the .value getter.

Initializers ¶
import org.cdk8s.DependencyVertex;

new DependencyVertex();,new DependencyVertex(IConstruct value);

Name	Type	Description
value	software.constructs.IConstruct	No description.
valueOptional ¶
Type: software.constructs.IConstruct
Methods ¶
Name	Description
addChild	Adds a vertex as a dependency of the current node.
topology	Returns a topologically sorted array of the constructs in the sub-graph.
addChild ¶
public void addChild(DependencyVertex dep)


Adds a vertex as a dependency of the current node.

Also updates the parents of dep, so that it contains this node as a parent.

This operation will fail in case it creates a cycle in the graph.

depRequired ¶
Type: DependencyVertex

The dependency.

topology ¶
public java.util.List<IConstruct> topology()


Returns a topologically sorted array of the constructs in the sub-graph.

Properties ¶
Name	Type	Description
inbound	java.util.List<DependencyVertex>	Returns the parents of the vertex (i.e dependants).
outbound	java.util.List<DependencyVertex>	Returns the children of the vertex (i.e dependencies).
value	software.constructs.IConstruct	Returns the IConstruct this graph vertex represents.
inboundRequired ¶
public java.util.List<DependencyVertex> getInbound();

Type: java.util.List<DependencyVertex>

Returns the parents of the vertex (i.e dependants).

outboundRequired ¶
public java.util.List<DependencyVertex> getOutbound();

Type: java.util.List<DependencyVertex>

Returns the children of the vertex (i.e dependencies).

valueOptional ¶
public IConstruct getValue();

Type: software.constructs.IConstruct

Returns the IConstruct this graph vertex represents.

null in case this is the root of the graph.

Duration ¶

Represents a length of time.

The amount can be specified either as a literal value (e.g: 10) which cannot be negative.

Methods ¶
Name	Description
toDays	Return the total number of days in this Duration.
toHours	Return the total number of hours in this Duration.
toHumanString	Turn this duration into a human-readable string.
toIsoString	Return an ISO 8601 representation of this period.
toMilliseconds	Return the total number of milliseconds in this Duration.
toMinutes	Return the total number of minutes in this Duration.
toSeconds	Return the total number of seconds in this Duration.
unitLabel	Return unit of Duration.
toDays ¶
public java.lang.Number toDays()
public java.lang.Number toDays(TimeConversionOptions opts)


Return the total number of days in this Duration.

optsOptional ¶
Type: TimeConversionOptions
toHours ¶
public java.lang.Number toHours()
public java.lang.Number toHours(TimeConversionOptions opts)


Return the total number of hours in this Duration.

optsOptional ¶
Type: TimeConversionOptions
toHumanString ¶
public java.lang.String toHumanString()


Turn this duration into a human-readable string.

toIsoString ¶
public java.lang.String toIsoString()


Return an ISO 8601 representation of this period.

https://www.iso.org/fr/standard/70907.html

toMilliseconds ¶
public java.lang.Number toMilliseconds()
public java.lang.Number toMilliseconds(TimeConversionOptions opts)


Return the total number of milliseconds in this Duration.

optsOptional ¶
Type: TimeConversionOptions
toMinutes ¶
public java.lang.Number toMinutes()
public java.lang.Number toMinutes(TimeConversionOptions opts)


Return the total number of minutes in this Duration.

optsOptional ¶
Type: TimeConversionOptions
toSeconds ¶
public java.lang.Number toSeconds()
public java.lang.Number toSeconds(TimeConversionOptions opts)


Return the total number of seconds in this Duration.

optsOptional ¶
Type: TimeConversionOptions
unitLabel ¶
public java.lang.String unitLabel()


Return unit of Duration.

Static Functions ¶
Name	Description
days	Create a Duration representing an amount of days.
hours	Create a Duration representing an amount of hours.
millis	Create a Duration representing an amount of milliseconds.
minutes	Create a Duration representing an amount of minutes.
parse	Parse a period formatted according to the ISO 8601 standard.
seconds	Create a Duration representing an amount of seconds.
days ¶
import org.cdk8s.Duration;

Duration.days(java.lang.Number amount)


Create a Duration representing an amount of days.

amountRequired ¶
Type: java.lang.Number

the amount of Days the Duration will represent.

hours ¶
import org.cdk8s.Duration;

Duration.hours(java.lang.Number amount)


Create a Duration representing an amount of hours.

amountRequired ¶
Type: java.lang.Number

the amount of Hours the Duration will represent.

millis ¶
import org.cdk8s.Duration;

Duration.millis(java.lang.Number amount)


Create a Duration representing an amount of milliseconds.

amountRequired ¶
Type: java.lang.Number

the amount of Milliseconds the Duration will represent.

minutes ¶
import org.cdk8s.Duration;

Duration.minutes(java.lang.Number amount)


Create a Duration representing an amount of minutes.

amountRequired ¶
Type: java.lang.Number

the amount of Minutes the Duration will represent.

parse ¶
import org.cdk8s.Duration;

Duration.parse(java.lang.String duration)


Parse a period formatted according to the ISO 8601 standard.

https://www.iso.org/fr/standard/70907.html

durationRequired ¶
Type: java.lang.String

an ISO-formtted duration to be parsed.

seconds ¶
import org.cdk8s.Duration;

Duration.seconds(java.lang.Number amount)


Create a Duration representing an amount of seconds.

amountRequired ¶
Type: java.lang.Number

the amount of Seconds the Duration will represent.

ImplicitTokenResolver ¶
Implements: IResolver

Resolves implicit tokens.

Initializers ¶
import org.cdk8s.ImplicitTokenResolver;

new ImplicitTokenResolver();

Name	Type	Description
		
Methods ¶
Name	Description
resolve	This function is invoked on every property during cdk8s synthesis.
resolve ¶
public void resolve(ResolutionContext context)


This function is invoked on every property during cdk8s synthesis.

To replace a value, implementations must invoke context.replaceValue.

contextRequired ¶
Type: ResolutionContext
JsonPatch ¶

Utility for applying RFC-6902 JSON-Patch to a document.

Use the the JsonPatch.apply(doc, ...ops) function to apply a set of operations to a JSON document and return the result.

Operations can be created using the factory methods JsonPatch.add(), JsonPatch.remove(), etc.

Example

// Example automatically generated from non-compiling source. May contain errors.
Object output = JsonPatch.apply(input, JsonPatch.replace("/world/hi/there", "goodbye"), JsonPatch.add("/world/foo/", "boom"), JsonPatch.remove("/hello"));

Static Functions ¶
Name	Description
add	Adds a value to an object or inserts it into an array.
apply	Applies a set of JSON-Patch (RFC-6902) operations to document and returns the result.
copy	Copies a value from one location to another within the JSON document.
move	Moves a value from one location to the other.
remove	Removes a value from an object or array.
replace	Replaces a value.
test	Tests that the specified value is set in the document.
add ¶
import org.cdk8s.JsonPatch;

JsonPatch.add(java.lang.String path, java.lang.Object value)


Adds a value to an object or inserts it into an array.

In the case of an array, the value is inserted before the given index. The - character can be used instead of an index to insert at the end of an array.

Example

// Example automatically generated from non-compiling source. May contain errors.
JsonPatch.add("/biscuits/1", Map.of("name", "Ginger Nut"));

pathRequired ¶
Type: java.lang.String
valueRequired ¶
Type: java.lang.Object
apply ¶
import org.cdk8s.JsonPatch;

JsonPatch.apply(java.lang.Object document, JsonPatch... ops)


Applies a set of JSON-Patch (RFC-6902) operations to document and returns the result.

documentRequired ¶
Type: java.lang.Object

The document to patch.

opsRequired ¶
Type: JsonPatch…

The operations to apply.

copy ¶
import org.cdk8s.JsonPatch;

JsonPatch.copy(java.lang.String from, java.lang.String path)


Copies a value from one location to another within the JSON document.

Both from and path are JSON Pointers.

Example

// Example automatically generated from non-compiling source. May contain errors.
JsonPatch.copy("/biscuits/0", "/best_biscuit");

fromRequired ¶
Type: java.lang.String
pathRequired ¶
Type: java.lang.String
move ¶
import org.cdk8s.JsonPatch;

JsonPatch.move(java.lang.String from, java.lang.String path)


Moves a value from one location to the other.

Both from and path are JSON Pointers.

Example

// Example automatically generated from non-compiling source. May contain errors.
JsonPatch.move("/biscuits", "/cookies");

fromRequired ¶
Type: java.lang.String
pathRequired ¶
Type: java.lang.String
remove ¶
import org.cdk8s.JsonPatch;

JsonPatch.remove(java.lang.String path)


Removes a value from an object or array.

Example

// Example automatically generated from non-compiling source. May contain errors.
JsonPatch.remove("/biscuits/0");

pathRequired ¶
Type: java.lang.String
replace ¶
import org.cdk8s.JsonPatch;

JsonPatch.replace(java.lang.String path, java.lang.Object value)


Replaces a value.

Equivalent to a “remove” followed by an “add”.

Example

// Example automatically generated from non-compiling source. May contain errors.
JsonPatch.replace("/biscuits/0/name", "Chocolate Digestive");

pathRequired ¶
Type: java.lang.String
valueRequired ¶
Type: java.lang.Object
test ¶
import org.cdk8s.JsonPatch;

JsonPatch.test(java.lang.String path, java.lang.Object value)


Tests that the specified value is set in the document.

If the test fails, then the patch as a whole should not apply.

Example

// Example automatically generated from non-compiling source. May contain errors.
JsonPatch.test("/best_biscuit/name", "Choco Leibniz");

pathRequired ¶
Type: java.lang.String
valueRequired ¶
Type: java.lang.Object
Lazy ¶
Methods ¶
Name	Description
produce	No description.
produce ¶
public java.lang.Object produce()

Static Functions ¶
Name	Description
any	No description.
any ¶
import org.cdk8s.Lazy;

Lazy.any(IAnyProducer producer)

producerRequired ¶
Type: IAnyProducer
LazyResolver ¶
Implements: IResolver

Resolvers instanecs of Lazy.

Initializers ¶
import org.cdk8s.LazyResolver;

new LazyResolver();

Name	Type	Description
		
Methods ¶
Name	Description
resolve	This function is invoked on every property during cdk8s synthesis.
resolve ¶
public void resolve(ResolutionContext context)


This function is invoked on every property during cdk8s synthesis.

To replace a value, implementations must invoke context.replaceValue.

contextRequired ¶
Type: ResolutionContext
Names ¶

Utilities for generating unique and stable names.

Static Functions ¶
Name	Description
toDnsLabel	Generates a unique and stable name compatible DNS_LABEL from RFC-1123 from a path.
toLabelValue	Generates a unique and stable name compatible label key name segment and label value from a path.
toDnsLabel ¶
import org.cdk8s.Names;

Names.toDnsLabel(Construct scope),Names.toDnsLabel(Construct scope, NameOptions options)


Generates a unique and stable name compatible DNS_LABEL from RFC-1123 from a path.

The generated name will:

contain at most 63 characters
contain only lowercase alphanumeric characters or ‘-’
start with an alphanumeric character
end with an alphanumeric character

The generated name will have the form: --..--

Where are the path components (assuming they are is separated by “/”).

Note that if the total length is longer than 63 characters, we will trim the first components since the last components usually encode more meaning.

https://tools.ietf.org/html/rfc1123

scopeRequired ¶
Type: software.constructs.Construct

The construct for which to render the DNS label.

optionsOptional ¶
Type: NameOptions

Name options.

toLabelValue ¶
import org.cdk8s.Names;

Names.toLabelValue(Construct scope),Names.toLabelValue(Construct scope, NameOptions options)


Generates a unique and stable name compatible label key name segment and label value from a path.

The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.

Valid label values must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.

The generated name will have the form: ..

Where are the path components (assuming they are is separated by “/”).

Note that if the total length is longer than 63 characters, we will trim the first components since the last components usually encode more meaning.

https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set

scopeRequired ¶
Type: software.constructs.Construct

The construct for which to render the DNS label.

optionsOptional ¶
Type: NameOptions

Name options.

NumberStringUnionResolver ¶
Implements: IResolver

Resolves union types that allow using either number or string (as generated by the CLI).

E.g IntOrString, Quantity, …

Initializers ¶
import org.cdk8s.NumberStringUnionResolver;

new NumberStringUnionResolver();

Name	Type	Description
		
Methods ¶
Name	Description
resolve	This function is invoked on every property during cdk8s synthesis.
resolve ¶
public void resolve(ResolutionContext context)


This function is invoked on every property during cdk8s synthesis.

To replace a value, implementations must invoke context.replaceValue.

contextRequired ¶
Type: ResolutionContext
ResolutionContext ¶

Context object for a specific resolution process.

Initializers ¶
import org.cdk8s.ResolutionContext;

new ResolutionContext(ApiObject obj, java.util.List<java.lang.String> key, java.lang.Object value);

Name	Type	Description
obj	ApiObject	Which ApiObject is currently being resolved.
key	java.util.List	Which key is currently being resolved.
value	java.lang.Object	The value associated to the key currently being resolved.
objRequired ¶
Type: ApiObject

Which ApiObject is currently being resolved.

keyRequired ¶
Type: java.util.List

Which key is currently being resolved.

valueRequired ¶
Type: java.lang.Object

The value associated to the key currently being resolved.

Methods ¶
Name	Description
replaceValue	Replaces the original value in this resolution context with a new value.
replaceValue ¶
public void replaceValue(java.lang.Object newValue)


Replaces the original value in this resolution context with a new value.

The new value is what will end up in the manifest.

newValueRequired ¶
Type: java.lang.Object
Properties ¶
Name	Type	Description
key	java.util.List	Which key is currently being resolved.
obj	ApiObject	Which ApiObject is currently being resolved.
value	java.lang.Object	The value associated to the key currently being resolved.
replaced	java.lang.Boolean	Whether or not the value was replaced by invoking the replaceValue method.
replacedValue	java.lang.Object	The replaced value that was set via the replaceValue method.
keyRequired ¶
public java.util.List<java.lang.String> getKey();

Type: java.util.List

Which key is currently being resolved.

objRequired ¶
public ApiObject getObj();

Type: ApiObject

Which ApiObject is currently being resolved.

valueRequired ¶
public java.lang.Object getValue();

Type: java.lang.Object

The value associated to the key currently being resolved.

replacedRequired ¶
public java.lang.Boolean getReplaced();

Type: java.lang.Boolean

Whether or not the value was replaced by invoking the replaceValue method.

replacedValueRequired ¶
public java.lang.Object getReplacedValue();

Type: java.lang.Object

The replaced value that was set via the replaceValue method.

Size ¶

Represents the amount of digital storage.

The amount can be specified either as a literal value (e.g: 10) which cannot be negative.

When the amount is passed as a token, unit conversion is not possible.

Methods ¶
Name	Description
asString	Returns amount with abbreviated storage unit.
toGibibytes	Return this storage as a total number of gibibytes.
toKibibytes	Return this storage as a total number of kibibytes.
toMebibytes	Return this storage as a total number of mebibytes.
toPebibytes	Return this storage as a total number of pebibytes.
toTebibytes	Return this storage as a total number of tebibytes.
asString ¶
public java.lang.String asString()


Returns amount with abbreviated storage unit.

toGibibytes ¶
public java.lang.Number toGibibytes()
public java.lang.Number toGibibytes(SizeConversionOptions opts)


Return this storage as a total number of gibibytes.

optsOptional ¶
Type: SizeConversionOptions
toKibibytes ¶
public java.lang.Number toKibibytes()
public java.lang.Number toKibibytes(SizeConversionOptions opts)


Return this storage as a total number of kibibytes.

optsOptional ¶
Type: SizeConversionOptions
toMebibytes ¶
public java.lang.Number toMebibytes()
public java.lang.Number toMebibytes(SizeConversionOptions opts)


Return this storage as a total number of mebibytes.

optsOptional ¶
Type: SizeConversionOptions
toPebibytes ¶
public java.lang.Number toPebibytes()
public java.lang.Number toPebibytes(SizeConversionOptions opts)


Return this storage as a total number of pebibytes.

optsOptional ¶
Type: SizeConversionOptions
toTebibytes ¶
public java.lang.Number toTebibytes()
public java.lang.Number toTebibytes(SizeConversionOptions opts)


Return this storage as a total number of tebibytes.

optsOptional ¶
Type: SizeConversionOptions
Static Functions ¶
Name	Description
gibibytes	Create a Storage representing an amount gibibytes.
kibibytes	Create a Storage representing an amount kibibytes.
mebibytes	Create a Storage representing an amount mebibytes.
pebibyte	Create a Storage representing an amount pebibytes.
tebibytes	Create a Storage representing an amount tebibytes.
gibibytes ¶
import org.cdk8s.Size;

Size.gibibytes(java.lang.Number amount)


Create a Storage representing an amount gibibytes.

1 GiB = 1024 MiB

amountRequired ¶
Type: java.lang.Number
kibibytes ¶
import org.cdk8s.Size;

Size.kibibytes(java.lang.Number amount)


Create a Storage representing an amount kibibytes.

1 KiB = 1024 bytes

amountRequired ¶
Type: java.lang.Number
mebibytes ¶
import org.cdk8s.Size;

Size.mebibytes(java.lang.Number amount)


Create a Storage representing an amount mebibytes.

1 MiB = 1024 KiB

amountRequired ¶
Type: java.lang.Number
pebibyte ¶
import org.cdk8s.Size;

Size.pebibyte(java.lang.Number amount)


Create a Storage representing an amount pebibytes.

1 PiB = 1024 TiB

amountRequired ¶
Type: java.lang.Number
tebibytes ¶
import org.cdk8s.Size;

Size.tebibytes(java.lang.Number amount)


Create a Storage representing an amount tebibytes.

1 TiB = 1024 GiB

amountRequired ¶
Type: java.lang.Number
Testing ¶

Testing utilities for cdk8s applications.

Static Functions ¶
Name	Description
app	Returns an app for testing with the following properties: - Output directory is a temp dir.
chart	No description.
synth	Returns the Kubernetes manifest synthesized from this chart.
app ¶
import org.cdk8s.Testing;

Testing.app(),Testing.app(AppProps props)


Returns an app for testing with the following properties: - Output directory is a temp dir.

propsOptional ¶
Type: AppProps
chart ¶
import org.cdk8s.Testing;

Testing.chart()

synth ¶
import org.cdk8s.Testing;

Testing.synth(Chart chart)


Returns the Kubernetes manifest synthesized from this chart.

chartRequired ¶
Type: Chart
Yaml ¶

YAML utilities.

Static Functions ¶
Name	Description
formatObjects	No description.
load	Downloads a set of YAML documents (k8s manifest for example) from a URL or a file and returns them as javascript objects.
save	Saves a set of objects as a multi-document YAML file.
stringify	Stringify a document (or multiple documents) into YAML.
tmp	Saves a set of YAML documents into a temp file (in /tmp).
~~formatObjects~~ ¶
import org.cdk8s.Yaml;

Yaml.formatObjects(java.util.List<java.lang.Object> docs)

docsRequired ¶
Type: java.util.List
load ¶
import org.cdk8s.Yaml;

Yaml.load(java.lang.String urlOrFile)


Downloads a set of YAML documents (k8s manifest for example) from a URL or a file and returns them as javascript objects.

Empty documents are filtered out.

urlOrFileRequired ¶
Type: java.lang.String

a URL of a file path to load from.

save ¶
import org.cdk8s.Yaml;

Yaml.save(java.lang.String filePath, java.util.List<java.lang.Object> docs)


Saves a set of objects as a multi-document YAML file.

filePathRequired ¶
Type: java.lang.String

The output path.

docsRequired ¶
Type: java.util.List

The set of objects.

stringify ¶
import org.cdk8s.Yaml;

Yaml.stringify(java.lang.Object... docs)


Stringify a document (or multiple documents) into YAML.

We convert undefined values to null, but ignore any documents that are undefined.

docsRequired ¶
Type: java.lang.Object…

A set of objects to convert to YAML.

tmp ¶
import org.cdk8s.Yaml;

Yaml.tmp(java.util.List<java.lang.Object> docs)


Saves a set of YAML documents into a temp file (in /tmp).

docsRequired ¶
Type: java.util.List

the set of documents to save.

Protocols ¶
IAnyProducer ¶
Implemented By: IAnyProducer
Methods ¶
Name	Description
produce	No description.
produce ¶
public java.lang.Object produce()

IResolver ¶
Implemented By: ImplicitTokenResolver, LazyResolver, NumberStringUnionResolver, IResolver

Contract for resolver objects.

Methods ¶
Name	Description
resolve	This function is invoked on every property during cdk8s synthesis.
resolve ¶
public void resolve(ResolutionContext context)


This function is invoked on every property during cdk8s synthesis.

To replace a value, implementations must invoke context.replaceValue.

contextRequired ¶
Type: ResolutionContext
Enums ¶
SizeRoundingBehavior ¶

Rounding behaviour when converting between units of Size.

Members ¶
Name	Description
FAIL	Fail the conversion if the result is not an integer.
FLOOR	If the result is not an integer, round it to the closest integer less than the result.
NONE	Don’t round.
FAIL ¶

Fail the conversion if the result is not an integer.

FLOOR ¶

If the result is not an integer, round it to the closest integer less than the result.

NONE ¶

Don’t round.

Return even if the result is a fraction.

YamlOutputType ¶

The method to divide YAML output into files.

Members ¶
Name	Description
FILE_PER_APP	All resources are output into a single YAML file.
FILE_PER_CHART	Resources are split into seperate files by chart.
FILE_PER_RESOURCE	Each resource is output to its own file.
FOLDER_PER_CHART_FILE_PER_RESOURCE	Each chart in its own folder and each resource in its own file.
FILE_PER_APP ¶

All resources are output into a single YAML file.

FILE_PER_CHART ¶

Resources are split into seperate files by chart.

FILE_PER_RESOURCE ¶

Each resource is output to its own file.

FOLDER_PER_CHART_FILE_PER_RESOURCE ¶

Each chart in its own folder and each resource in its own file.

© 2025, Amazon Web Services, Inc. or its affiliates. © cdk8s project authors. All rights reserved.
Made with Material for MkDocs
