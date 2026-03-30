# Source: https://cdk8s.io/docs/latest/reference/cdk8s/python/

Title: Python - cdk8s

URL Source: https://cdk8s.io/docs/latest/reference/cdk8s/python/

Markdown Content:
Skip to content
cdk8s
Python
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
cdk8s (Python) ¶
Constructs ¶
ApiObject ¶
Initializers ¶
import cdk8s

cdk8s.ApiObject(
  scope: Construct,
  id: str,
  api_version: str,
  kind: str,
  metadata: ApiObjectMetadata = None
)

Name	Type	Description
scope	constructs.Construct	the construct scope.
id	str	namespace.
api_version	str	API version.
kind	str	Resource kind.
metadata	ApiObjectMetadata	Object metadata.
scopeRequired ¶
Type: constructs.Construct

the construct scope.

idRequired ¶
Type: str

namespace.

api_versionRequired ¶
Type: str

API version.

kindRequired ¶
Type: str

Resource kind.

metadataOptional ¶
Type: ApiObjectMetadata

Object metadata.

If name is not specified, an app-unique name will be allocated by the framework based on the path of the construct within thes construct tree.

Methods ¶
Name	Description
to_string	Returns a string representation of this construct.
with	Applies one or more mixins to this construct.
add_dependency	Create a dependency between this ApiObject and other constructs.
add_json_patch	Applies a set of RFC-6902 JSON-Patch operations to the manifest synthesized for this API object.
to_json	Renders the object to Kubernetes JSON.
to_string ¶
def to_string() -> str


Returns a string representation of this construct.

with ¶
def with(
  mixins: *IMixin
) -> IConstruct


Applies one or more mixins to this construct.

Mixins are applied in order. The list of constructs is captured at the start of the call, so constructs added by a mixin will not be visited. Use multiple with() calls if subsequent mixins should apply to added constructs.

mixinsRequired ¶
Type: *constructs.IMixin

The mixins to apply.

add_dependency ¶
def add_dependency(
  dependencies: *IConstruct
) -> None


Create a dependency between this ApiObject and other constructs.

These can be other ApiObjects, Charts, or custom.

dependenciesRequired ¶
Type: *constructs.IConstruct

the dependencies to add.

add_json_patch ¶
def add_json_patch(
  ops: *JsonPatch
) -> None


Applies a set of RFC-6902 JSON-Patch operations to the manifest synthesized for this API object.

Example

# Example automatically generated from non-compiling source. May contain errors.
kube_pod.add_json_patch(JsonPatch.replace("/spec/enableServiceLinks", True))

opsRequired ¶
Type: *JsonPatch

The JSON-Patch operations to apply.

to_json ¶
def to_json() -> typing.Any


Renders the object to Kubernetes JSON.

To disable sorting of dictionary keys in output object set the CDK8S_DISABLE_SORT environment variable to any non-empty value.

Static Functions ¶
Name	Description
is_construct	Checks if x is a construct.
is_api_object	Return whether the given object is an ApiObject.
of	Returns the ApiObject named Resource which is a child of the given construct.
is_construct ¶
import cdk8s

cdk8s.ApiObject.is_construct(
  x: typing.Any
)


Checks if x is a construct.

Use this method instead of instanceof to properly detect Construct instances, even when the construct library is symlinked.

Explanation: in JavaScript, multiple copies of the constructs library on disk are seen as independent, completely different libraries. As a consequence, the class Construct in each copy of the constructs library is seen as a different class, and an instance of one class will not test as instanceof the other class. npm install will not create installations like this, but users may manually symlink construct libraries together or use a monorepo tool: in those cases, multiple copies of the constructs library can be accidentally installed, and instanceof will behave unpredictably. It is safest to avoid using instanceof, and using this type-testing method instead.

xRequired ¶
Type: typing.Any

Any object.

is_api_object ¶
import cdk8s

cdk8s.ApiObject.is_api_object(
  o: typing.Any
)


Return whether the given object is an ApiObject.

We do attribute detection since we can’t reliably use ‘instanceof’.

oRequired ¶
Type: typing.Any

The object to check.

of ¶
import cdk8s

cdk8s.ApiObject.of(
  c: IConstruct
)


Returns the ApiObject named Resource which is a child of the given construct.

If c is an ApiObject, it is returned directly. Throws an exception if the construct does not have a child named Default or if this child is not an ApiObject.

cRequired ¶
Type: constructs.IConstruct

The higher-level construct.

Properties ¶
Name	Type	Description
node	constructs.Node	The tree node.
api_group	str	The group portion of the API version (e.g. authorization.k8s.io).
api_version	str	The object’s API version (e.g. authorization.k8s.io/v1).
chart	Chart	The chart in which this object is defined.
kind	str	The object kind.
metadata	ApiObjectMetadataDefinition	Metadata associated with this API object.
name	str	The name of the API object.
nodeRequired ¶
node: Node

Type: constructs.Node

The tree node.

api_groupRequired ¶
api_group: str

Type: str

The group portion of the API version (e.g. authorization.k8s.io).

api_versionRequired ¶
api_version: str

Type: str

The object’s API version (e.g. authorization.k8s.io/v1).

chartRequired ¶
chart: Chart

Type: Chart

The chart in which this object is defined.

kindRequired ¶
kind: str

Type: str

The object kind.

metadataRequired ¶
metadata: ApiObjectMetadataDefinition

Type: ApiObjectMetadataDefinition

Metadata associated with this API object.

nameRequired ¶
name: str

Type: str

The name of the API object.

If a name is specified in metadata.name this will be the name returned. Otherwise, a name will be generated by calling Chart.of(this).generatedObjectName(this), which by default uses the construct path to generate a DNS-compatible name for the resource.

App ¶

Represents a cdk8s application.

Initializers ¶
import cdk8s

cdk8s.App(
  outdir: str = None,
  output_file_extension: str = None,
  record_construct_metadata: bool = None,
  resolvers: typing.List[IResolver] = None,
  yaml_output_type: YamlOutputType = None
)

Name	Type	Description
outdir	str	The directory to output Kubernetes manifests.
output_file_extension	str	The file extension to use for rendered YAML files.
record_construct_metadata	bool	When set to true, the output directory will contain a construct-metadata.json file that holds construct related metadata on every resource in the app.
resolvers	typing.List[IResolver]	A list of resolvers that can be used to replace property values before they are written to the manifest file.
yaml_output_type	YamlOutputType	How to divide the YAML output into files.
outdirOptional ¶
Type: str
Default: CDK8S_OUTDIR if defined, otherwise “dist”

The directory to output Kubernetes manifests.

If you synthesize your application using cdk8s synth, you must also pass this value to the CLI using the --output option or the output property in the cdk8s.yaml configuration file. Otherwise, the CLI will not know about the output directory, and synthesis will fail.

This property is intended for internal and testing use.

output_file_extensionOptional ¶
Type: str
Default: .k8s.yaml

The file extension to use for rendered YAML files.

record_construct_metadataOptional ¶
Type: bool
Default: false

When set to true, the output directory will contain a construct-metadata.json file that holds construct related metadata on every resource in the app.

resolversOptional ¶
Type: typing.List[IResolver]
Default: no resolvers.

A list of resolvers that can be used to replace property values before they are written to the manifest file.

When multiple resolvers are passed, they are invoked by order in the list, and only the first one that applies (e.g calls context.replaceValue) is invoked.

https://cdk8s.io/docs/latest/basics/app/#resolvers

yaml_output_typeOptional ¶
Type: YamlOutputType
Default: YamlOutputType.FILE_PER_CHART

How to divide the YAML output into files.

Methods ¶
Name	Description
to_string	Returns a string representation of this construct.
with	Applies one or more mixins to this construct.
synth	Synthesizes all manifests to the output directory.
synth_yaml	Synthesizes the app into a YAML string.
to_string ¶
def to_string() -> str


Returns a string representation of this construct.

with ¶
def with(
  mixins: *IMixin
) -> IConstruct


Applies one or more mixins to this construct.

Mixins are applied in order. The list of constructs is captured at the start of the call, so constructs added by a mixin will not be visited. Use multiple with() calls if subsequent mixins should apply to added constructs.

mixinsRequired ¶
Type: *constructs.IMixin

The mixins to apply.

synth ¶
def synth() -> None


Synthesizes all manifests to the output directory.

synth_yaml ¶
def synth_yaml() -> str


Synthesizes the app into a YAML string.

Static Functions ¶
Name	Description
is_construct	Checks if x is a construct.
of	No description.
is_construct ¶
import cdk8s

cdk8s.App.is_construct(
  x: typing.Any
)


Checks if x is a construct.

Use this method instead of instanceof to properly detect Construct instances, even when the construct library is symlinked.

Explanation: in JavaScript, multiple copies of the constructs library on disk are seen as independent, completely different libraries. As a consequence, the class Construct in each copy of the constructs library is seen as a different class, and an instance of one class will not test as instanceof the other class. npm install will not create installations like this, but users may manually symlink construct libraries together or use a monorepo tool: in those cases, multiple copies of the constructs library can be accidentally installed, and instanceof will behave unpredictably. It is safest to avoid using instanceof, and using this type-testing method instead.

xRequired ¶
Type: typing.Any

Any object.

of ¶
import cdk8s

cdk8s.App.of(
  c: IConstruct
)

cRequired ¶
Type: constructs.IConstruct
Properties ¶
Name	Type	Description
node	constructs.Node	The tree node.
charts	typing.List[Chart]	Returns all the charts in this app, sorted topologically.
outdir	str	The output directory into which manifests will be synthesized.
output_file_extension	str	The file extension to use for rendered YAML files.
resolvers	typing.List[IResolver]	Resolvers used by this app.
yaml_output_type	YamlOutputType	How to divide the YAML output into files.
nodeRequired ¶
node: Node

Type: constructs.Node

The tree node.

chartsRequired ¶
charts: typing.List[Chart]

Type: typing.List[Chart]

Returns all the charts in this app, sorted topologically.

outdirRequired ¶
outdir: str

Type: str

The output directory into which manifests will be synthesized.

output_file_extensionRequired ¶
output_file_extension: str

Type: str
Default: .k8s.yaml

The file extension to use for rendered YAML files.

resolversRequired ¶
resolvers: typing.List[IResolver]

Type: typing.List[IResolver]

Resolvers used by this app.

This includes both custom resolvers passed by the resolvers property, as well as built-in resolvers.

yaml_output_typeRequired ¶
yaml_output_type: YamlOutputType

Type: YamlOutputType
Default: YamlOutputType.FILE_PER_CHART

How to divide the YAML output into files.

Chart ¶
Initializers ¶
import cdk8s

cdk8s.Chart(
  scope: Construct,
  id: str,
  disable_resource_name_hashes: bool = None,
  labels: typing.Mapping[str] = None,
  namespace: str = None
)

Name	Type	Description
scope	constructs.Construct	No description.
id	str	No description.
disable_resource_name_hashes	bool	The autogenerated resource name by default is suffixed with a stable hash of the construct path.
labels	typing.Mapping[str]	Labels to apply to all resources in this chart.
namespace	str	The default namespace for all objects defined in this chart (directly or indirectly).
scopeRequired ¶
Type: constructs.Construct
idRequired ¶
Type: str
disable_resource_name_hashesOptional ¶
Type: bool
Default: false

The autogenerated resource name by default is suffixed with a stable hash of the construct path.

Setting this property to true drops the hash suffix.

labelsOptional ¶
Type: typing.Mapping[str]
Default: no common labels

Labels to apply to all resources in this chart.

namespaceOptional ¶
Type: str
Default: no namespace is synthesized (usually this implies “default”)

The default namespace for all objects defined in this chart (directly or indirectly).

This namespace will only apply to objects that don’t have a namespace explicitly defined for them.

Methods ¶
Name	Description
to_string	Returns a string representation of this construct.
with	Applies one or more mixins to this construct.
add_dependency	Create a dependency between this Chart and other constructs.
generate_object_name	Generates a app-unique name for an object given it’s construct node path.
to_json	Renders this chart to a set of Kubernetes JSON resources.
to_string ¶
def to_string() -> str


Returns a string representation of this construct.

with ¶
def with(
  mixins: *IMixin
) -> IConstruct


Applies one or more mixins to this construct.

Mixins are applied in order. The list of constructs is captured at the start of the call, so constructs added by a mixin will not be visited. Use multiple with() calls if subsequent mixins should apply to added constructs.

mixinsRequired ¶
Type: *constructs.IMixin

The mixins to apply.

add_dependency ¶
def add_dependency(
  dependencies: *IConstruct
) -> None


Create a dependency between this Chart and other constructs.

These can be other ApiObjects, Charts, or custom.

dependenciesRequired ¶
Type: *constructs.IConstruct

the dependencies to add.

generate_object_name ¶
def generate_object_name(
  api_object: ApiObject
) -> str


Generates a app-unique name for an object given it’s construct node path.

Different resource types may have different constraints on names (metadata.name). The previous version of the name generator was compatible with DNS_SUBDOMAIN but not with DNS_LABEL.

For example, Deployment names must comply with DNS_SUBDOMAIN while Service names must comply with DNS_LABEL.

Since there is no formal specification for this, the default name generation scheme for kubernetes objects in cdk8s was changed to DNS_LABEL, since it’s the common denominator for all kubernetes resources (supposedly).

You can override this method if you wish to customize object names at the chart level.

api_objectRequired ¶
Type: ApiObject

The API object to generate a name for.

to_json ¶
def to_json() -> typing.List[typing.Any]


Renders this chart to a set of Kubernetes JSON resources.

Static Functions ¶
Name	Description
is_construct	Checks if x is a construct.
is_chart	Return whether the given object is a Chart.
of	Finds the chart in which a node is defined.
is_construct ¶
import cdk8s

cdk8s.Chart.is_construct(
  x: typing.Any
)


Checks if x is a construct.

Use this method instead of instanceof to properly detect Construct instances, even when the construct library is symlinked.

Explanation: in JavaScript, multiple copies of the constructs library on disk are seen as independent, completely different libraries. As a consequence, the class Construct in each copy of the constructs library is seen as a different class, and an instance of one class will not test as instanceof the other class. npm install will not create installations like this, but users may manually symlink construct libraries together or use a monorepo tool: in those cases, multiple copies of the constructs library can be accidentally installed, and instanceof will behave unpredictably. It is safest to avoid using instanceof, and using this type-testing method instead.

xRequired ¶
Type: typing.Any

Any object.

is_chart ¶
import cdk8s

cdk8s.Chart.is_chart(
  x: typing.Any
)


Return whether the given object is a Chart.

We do attribute detection since we can’t reliably use ‘instanceof’.

xRequired ¶
Type: typing.Any
of ¶
import cdk8s

cdk8s.Chart.of(
  c: IConstruct
)


Finds the chart in which a node is defined.

cRequired ¶
Type: constructs.IConstruct

a construct node.

Properties ¶
Name	Type	Description
node	constructs.Node	The tree node.
api_objects	typing.List[ApiObject]	Returns all the included API objects.
labels	typing.Mapping[str]	Labels applied to all resources in this chart.
namespace	str	The default namespace for all objects in this chart.
nodeRequired ¶
node: Node

Type: constructs.Node

The tree node.

api_objectsRequired ¶
api_objects: typing.List[ApiObject]

Type: typing.List[ApiObject]

Returns all the included API objects.

labelsRequired ¶
labels: typing.Mapping[str]

Type: typing.Mapping[str]

Labels applied to all resources in this chart.

This is an immutable copy.

namespaceOptional ¶
namespace: str

Type: str

The default namespace for all objects in this chart.

Helm ¶

Represents a Helm deployment.

Use this construct to import an existing Helm chart and incorporate it into your constructs.

Initializers ¶
import cdk8s

cdk8s.Helm(
  scope: Construct,
  id: str,
  chart: str,
  helm_executable: str = None,
  helm_flags: typing.List[str] = None,
  namespace: str = None,
  release_name: str = None,
  repo: str = None,
  values: typing.Mapping[typing.Any] = None,
  version: str = None
)

Name	Type	Description
scope	constructs.Construct	No description.
id	str	No description.
chart	str	The chart name to use. It can be a chart from a helm repository or a local directory.
helm_executable	str	The local helm executable to use in order to create the manifest the chart.
helm_flags	typing.List[str]	Additional flags to add to the helm execution.
namespace	str	Scope all resources in to a given namespace.
release_name	str	The release name.
repo	str	Chart repository url where to locate the requested chart.
values	typing.Mapping[typing.Any]	Values to pass to the chart.
version	str	Version constraint for the chart version to use.
scopeRequired ¶
Type: constructs.Construct
idRequired ¶
Type: str
chartRequired ¶
Type: str

The chart name to use. It can be a chart from a helm repository or a local directory.

This name is passed to helm template and has all the relevant semantics.

Example

"bitnami/redis"

helm_executableOptional ¶
Type: str
Default: “helm”

The local helm executable to use in order to create the manifest the chart.

helm_flagsOptional ¶
Type: typing.List[str]
Default: []

Additional flags to add to the helm execution.

namespaceOptional ¶
Type: str

Scope all resources in to a given namespace.

release_nameOptional ¶
Type: str
Default: if unspecified, a name will be allocated based on the construct path

The release name.

https://helm.sh/docs/intro/using_helm/#three-big-concepts

repoOptional ¶
Type: str

Chart repository url where to locate the requested chart.

valuesOptional ¶
Type: typing.Mapping[typing.Any]
Default: If no values are specified, chart will use the defaults.

Values to pass to the chart.

versionOptional ¶
Type: str

Version constraint for the chart version to use.

This constraint can be a specific tag (e.g. 1.1.1) or it may reference a valid range (e.g. ^2.0.0). If this is not specified, the latest version is used

This name is passed to helm template --version and has all the relevant semantics.

Example

"^2.0.0"

Methods ¶
Name	Description
to_string	Returns a string representation of this construct.
with	Applies one or more mixins to this construct.
to_string ¶
def to_string() -> str


Returns a string representation of this construct.

with ¶
def with(
  mixins: *IMixin
) -> IConstruct


Applies one or more mixins to this construct.

Mixins are applied in order. The list of constructs is captured at the start of the call, so constructs added by a mixin will not be visited. Use multiple with() calls if subsequent mixins should apply to added constructs.

mixinsRequired ¶
Type: *constructs.IMixin

The mixins to apply.

Static Functions ¶
Name	Description
is_construct	Checks if x is a construct.
is_construct ¶
import cdk8s

cdk8s.Helm.is_construct(
  x: typing.Any
)


Checks if x is a construct.

Use this method instead of instanceof to properly detect Construct instances, even when the construct library is symlinked.

Explanation: in JavaScript, multiple copies of the constructs library on disk are seen as independent, completely different libraries. As a consequence, the class Construct in each copy of the constructs library is seen as a different class, and an instance of one class will not test as instanceof the other class. npm install will not create installations like this, but users may manually symlink construct libraries together or use a monorepo tool: in those cases, multiple copies of the constructs library can be accidentally installed, and instanceof will behave unpredictably. It is safest to avoid using instanceof, and using this type-testing method instead.

xRequired ¶
Type: typing.Any

Any object.

Properties ¶
Name	Type	Description
node	constructs.Node	The tree node.
api_objects	typing.List[ApiObject]	Returns all the included API objects.
release_name	str	The helm release name.
nodeRequired ¶
node: Node

Type: constructs.Node

The tree node.

api_objectsRequired ¶
api_objects: typing.List[ApiObject]

Type: typing.List[ApiObject]

Returns all the included API objects.

release_nameRequired ¶
release_name: str

Type: str

The helm release name.

Include ¶

Reads a YAML manifest from a file or a URL and defines all resources as API objects within the defined scope.

The names (metadata.name) of imported resources will be preserved as-is from the manifest.

Initializers ¶
import cdk8s

cdk8s.Include(
  scope: Construct,
  id: str,
  url: str
)

Name	Type	Description
scope	constructs.Construct	No description.
id	str	No description.
url	str	Local file path or URL which includes a Kubernetes YAML manifest.
scopeRequired ¶
Type: constructs.Construct
idRequired ¶
Type: str
urlRequired ¶
Type: str

Local file path or URL which includes a Kubernetes YAML manifest.

Example

# Example automatically generated from non-compiling source. May contain errors.
mymanifest.yaml

Methods ¶
Name	Description
to_string	Returns a string representation of this construct.
with	Applies one or more mixins to this construct.
to_string ¶
def to_string() -> str


Returns a string representation of this construct.

with ¶
def with(
  mixins: *IMixin
) -> IConstruct


Applies one or more mixins to this construct.

Mixins are applied in order. The list of constructs is captured at the start of the call, so constructs added by a mixin will not be visited. Use multiple with() calls if subsequent mixins should apply to added constructs.

mixinsRequired ¶
Type: *constructs.IMixin

The mixins to apply.

Static Functions ¶
Name	Description
is_construct	Checks if x is a construct.
is_construct ¶
import cdk8s

cdk8s.Include.is_construct(
  x: typing.Any
)


Checks if x is a construct.

Use this method instead of instanceof to properly detect Construct instances, even when the construct library is symlinked.

Explanation: in JavaScript, multiple copies of the constructs library on disk are seen as independent, completely different libraries. As a consequence, the class Construct in each copy of the constructs library is seen as a different class, and an instance of one class will not test as instanceof the other class. npm install will not create installations like this, but users may manually symlink construct libraries together or use a monorepo tool: in those cases, multiple copies of the constructs library can be accidentally installed, and instanceof will behave unpredictably. It is safest to avoid using instanceof, and using this type-testing method instead.

xRequired ¶
Type: typing.Any

Any object.

Properties ¶
Name	Type	Description
node	constructs.Node	The tree node.
api_objects	typing.List[ApiObject]	Returns all the included API objects.
nodeRequired ¶
node: Node

Type: constructs.Node

The tree node.

api_objectsRequired ¶
api_objects: typing.List[ApiObject]

Type: typing.List[ApiObject]

Returns all the included API objects.

Structs ¶
ApiObjectMetadata ¶

Metadata associated with this object.

Initializer ¶
import cdk8s

cdk8s.ApiObjectMetadata(
  annotations: typing.Mapping[str] = None,
  finalizers: typing.List[str] = None,
  labels: typing.Mapping[str] = None,
  name: str = None,
  namespace: str = None,
  owner_references: typing.List[OwnerReference] = None
)

Properties ¶
Name	Type	Description
annotations	typing.Mapping[str]	Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata.
finalizers	typing.List[str]	Namespaced keys that tell Kubernetes to wait until specific conditions are met before it fully deletes resources marked for deletion.
labels	typing.Mapping[str]	Map of string keys and values that can be used to organize and categorize (scope and select) objects.
name	str	The unique, namespace-global, name of this object inside the Kubernetes cluster.
namespace	str	Namespace defines the space within each name must be unique.
owner_references	typing.List[OwnerReference]	List of objects depended by this object.
annotationsOptional ¶
annotations: typing.Mapping[str]

Type: typing.Mapping[str]
Default: No annotations.

Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata.

They are not queryable and should be preserved when modifying objects.

http://kubernetes.io/docs/user-guide/annotations

finalizersOptional ¶
finalizers: typing.List[str]

Type: typing.List[str]
Default: No finalizers.

Namespaced keys that tell Kubernetes to wait until specific conditions are met before it fully deletes resources marked for deletion.

Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.

https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/

labelsOptional ¶
labels: typing.Mapping[str]

Type: typing.Mapping[str]
Default: No labels.

Map of string keys and values that can be used to organize and categorize (scope and select) objects.

May match selectors of replication controllers and services.

http://kubernetes.io/docs/user-guide/labels

nameOptional ¶
name: str

Type: str
Default: an app-unique name generated by the chart

The unique, namespace-global, name of this object inside the Kubernetes cluster.

Normally, you shouldn’t specify names for objects and let the CDK generate a name for you that is application-unique. The names CDK generates are composed from the construct path components, separated by dots and a suffix that is based on a hash of the entire path, to ensure uniqueness.

You can supply custom name allocation logic by overriding the chart.generateObjectName method.

If you use an explicit name here, bear in mind that this reduces the composability of your construct because it won’t be possible to include more than one instance in any app. Therefore it is highly recommended to leave this unspecified.

namespaceOptional ¶
namespace: str

Type: str
Default: undefined (will be assigned to the ‘default’ namespace)

Namespace defines the space within each name must be unique.

An empty namespace is equivalent to the “default” namespace, but “default” is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty. Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces

owner_referencesOptional ¶
owner_references: typing.List[OwnerReference]

Type: typing.List[OwnerReference]
Default: automatically set by Kubernetes

List of objects depended by this object.

If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.

Kubernetes sets the value of this field automatically for objects that are dependents of other objects like ReplicaSets, DaemonSets, Deployments, Jobs and CronJobs, and ReplicationControllers. You can also configure these relationships manually by changing the value of this field. However, you usually don’t need to and can allow Kubernetes to automatically manage the relationships.

https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/

ApiObjectMetadataDefinitionOptions ¶

Options for ApiObjectMetadataDefinition.

Initializer ¶
import cdk8s

cdk8s.ApiObjectMetadataDefinitionOptions(
  annotations: typing.Mapping[str] = None,
  finalizers: typing.List[str] = None,
  labels: typing.Mapping[str] = None,
  name: str = None,
  namespace: str = None,
  owner_references: typing.List[OwnerReference] = None,
  api_object: ApiObject
)

Properties ¶
Name	Type	Description
annotations	typing.Mapping[str]	Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata.
finalizers	typing.List[str]	Namespaced keys that tell Kubernetes to wait until specific conditions are met before it fully deletes resources marked for deletion.
labels	typing.Mapping[str]	Map of string keys and values that can be used to organize and categorize (scope and select) objects.
name	str	The unique, namespace-global, name of this object inside the Kubernetes cluster.
namespace	str	Namespace defines the space within each name must be unique.
owner_references	typing.List[OwnerReference]	List of objects depended by this object.
api_object	ApiObject	Which ApiObject instance is the metadata attached to.
annotationsOptional ¶
annotations: typing.Mapping[str]

Type: typing.Mapping[str]
Default: No annotations.

Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata.

They are not queryable and should be preserved when modifying objects.

http://kubernetes.io/docs/user-guide/annotations

finalizersOptional ¶
finalizers: typing.List[str]

Type: typing.List[str]
Default: No finalizers.

Namespaced keys that tell Kubernetes to wait until specific conditions are met before it fully deletes resources marked for deletion.

Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.

https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/

labelsOptional ¶
labels: typing.Mapping[str]

Type: typing.Mapping[str]
Default: No labels.

Map of string keys and values that can be used to organize and categorize (scope and select) objects.

May match selectors of replication controllers and services.

http://kubernetes.io/docs/user-guide/labels

nameOptional ¶
name: str

Type: str
Default: an app-unique name generated by the chart

The unique, namespace-global, name of this object inside the Kubernetes cluster.

Normally, you shouldn’t specify names for objects and let the CDK generate a name for you that is application-unique. The names CDK generates are composed from the construct path components, separated by dots and a suffix that is based on a hash of the entire path, to ensure uniqueness.

You can supply custom name allocation logic by overriding the chart.generateObjectName method.

If you use an explicit name here, bear in mind that this reduces the composability of your construct because it won’t be possible to include more than one instance in any app. Therefore it is highly recommended to leave this unspecified.

namespaceOptional ¶
namespace: str

Type: str
Default: undefined (will be assigned to the ‘default’ namespace)

Namespace defines the space within each name must be unique.

An empty namespace is equivalent to the “default” namespace, but “default” is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty. Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces

owner_referencesOptional ¶
owner_references: typing.List[OwnerReference]

Type: typing.List[OwnerReference]
Default: automatically set by Kubernetes

List of objects depended by this object.

If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.

Kubernetes sets the value of this field automatically for objects that are dependents of other objects like ReplicaSets, DaemonSets, Deployments, Jobs and CronJobs, and ReplicationControllers. You can also configure these relationships manually by changing the value of this field. However, you usually don’t need to and can allow Kubernetes to automatically manage the relationships.

https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/

api_objectRequired ¶
api_object: ApiObject

Type: ApiObject

Which ApiObject instance is the metadata attached to.

ApiObjectProps ¶

Options for defining API objects.

Initializer ¶
import cdk8s

cdk8s.ApiObjectProps(
  api_version: str,
  kind: str,
  metadata: ApiObjectMetadata = None
)

Properties ¶
Name	Type	Description
api_version	str	API version.
kind	str	Resource kind.
metadata	ApiObjectMetadata	Object metadata.
api_versionRequired ¶
api_version: str

Type: str

API version.

kindRequired ¶
kind: str

Type: str

Resource kind.

metadataOptional ¶
metadata: ApiObjectMetadata

Type: ApiObjectMetadata

Object metadata.

If name is not specified, an app-unique name will be allocated by the framework based on the path of the construct within thes construct tree.

AppProps ¶
Initializer ¶
import cdk8s

cdk8s.AppProps(
  outdir: str = None,
  output_file_extension: str = None,
  record_construct_metadata: bool = None,
  resolvers: typing.List[IResolver] = None,
  yaml_output_type: YamlOutputType = None
)

Properties ¶
Name	Type	Description
outdir	str	The directory to output Kubernetes manifests.
output_file_extension	str	The file extension to use for rendered YAML files.
record_construct_metadata	bool	When set to true, the output directory will contain a construct-metadata.json file that holds construct related metadata on every resource in the app.
resolvers	typing.List[IResolver]	A list of resolvers that can be used to replace property values before they are written to the manifest file.
yaml_output_type	YamlOutputType	How to divide the YAML output into files.
outdirOptional ¶
outdir: str

Type: str
Default: CDK8S_OUTDIR if defined, otherwise “dist”

The directory to output Kubernetes manifests.

If you synthesize your application using cdk8s synth, you must also pass this value to the CLI using the --output option or the output property in the cdk8s.yaml configuration file. Otherwise, the CLI will not know about the output directory, and synthesis will fail.

This property is intended for internal and testing use.

output_file_extensionOptional ¶
output_file_extension: str

Type: str
Default: .k8s.yaml

The file extension to use for rendered YAML files.

record_construct_metadataOptional ¶
record_construct_metadata: bool

Type: bool
Default: false

When set to true, the output directory will contain a construct-metadata.json file that holds construct related metadata on every resource in the app.

resolversOptional ¶
resolvers: typing.List[IResolver]

Type: typing.List[IResolver]
Default: no resolvers.

A list of resolvers that can be used to replace property values before they are written to the manifest file.

When multiple resolvers are passed, they are invoked by order in the list, and only the first one that applies (e.g calls context.replaceValue) is invoked.

https://cdk8s.io/docs/latest/basics/app/#resolvers

yaml_output_typeOptional ¶
yaml_output_type: YamlOutputType

Type: YamlOutputType
Default: YamlOutputType.FILE_PER_CHART

How to divide the YAML output into files.

ChartProps ¶
Initializer ¶
import cdk8s

cdk8s.ChartProps(
  disable_resource_name_hashes: bool = None,
  labels: typing.Mapping[str] = None,
  namespace: str = None
)

Properties ¶
Name	Type	Description
disable_resource_name_hashes	bool	The autogenerated resource name by default is suffixed with a stable hash of the construct path.
labels	typing.Mapping[str]	Labels to apply to all resources in this chart.
namespace	str	The default namespace for all objects defined in this chart (directly or indirectly).
disable_resource_name_hashesOptional ¶
disable_resource_name_hashes: bool

Type: bool
Default: false

The autogenerated resource name by default is suffixed with a stable hash of the construct path.

Setting this property to true drops the hash suffix.

labelsOptional ¶
labels: typing.Mapping[str]

Type: typing.Mapping[str]
Default: no common labels

Labels to apply to all resources in this chart.

namespaceOptional ¶
namespace: str

Type: str
Default: no namespace is synthesized (usually this implies “default”)

The default namespace for all objects defined in this chart (directly or indirectly).

This namespace will only apply to objects that don’t have a namespace explicitly defined for them.

CronOptions ¶

Options to configure a cron expression.

All fields are strings so you can use complex expressions. Absence of a field implies ‘*’

Initializer ¶
import cdk8s

cdk8s.CronOptions(
  day: str = None,
  hour: str = None,
  minute: str = None,
  month: str = None,
  week_day: str = None
)

Properties ¶
Name	Type	Description
day	str	The day of the month to run this rule at.
hour	str	The hour to run this rule at.
minute	str	The minute to run this rule at.
month	str	The month to run this rule at.
week_day	str	The day of the week to run this rule at.
dayOptional ¶
day: str

Type: str
Default: Every day of the month

The day of the month to run this rule at.

hourOptional ¶
hour: str

Type: str
Default: Every hour

The hour to run this rule at.

minuteOptional ¶
minute: str

Type: str
Default: Every minute

The minute to run this rule at.

monthOptional ¶
month: str

Type: str
Default: Every month

The month to run this rule at.

week_dayOptional ¶
week_day: str

Type: str
Default: Any day of the week

The day of the week to run this rule at.

GroupVersionKind ¶
Initializer ¶
import cdk8s

cdk8s.GroupVersionKind(
  api_version: str,
  kind: str
)

Properties ¶
Name	Type	Description
api_version	str	The object’s API version (e.g. authorization.k8s.io/v1).
kind	str	The object kind.
api_versionRequired ¶
api_version: str

Type: str

The object’s API version (e.g. authorization.k8s.io/v1).

kindRequired ¶
kind: str

Type: str

The object kind.

HelmProps ¶

Options for Helm.

Initializer ¶
import cdk8s

cdk8s.HelmProps(
  chart: str,
  helm_executable: str = None,
  helm_flags: typing.List[str] = None,
  namespace: str = None,
  release_name: str = None,
  repo: str = None,
  values: typing.Mapping[typing.Any] = None,
  version: str = None
)

Properties ¶
Name	Type	Description
chart	str	The chart name to use. It can be a chart from a helm repository or a local directory.
helm_executable	str	The local helm executable to use in order to create the manifest the chart.
helm_flags	typing.List[str]	Additional flags to add to the helm execution.
namespace	str	Scope all resources in to a given namespace.
release_name	str	The release name.
repo	str	Chart repository url where to locate the requested chart.
values	typing.Mapping[typing.Any]	Values to pass to the chart.
version	str	Version constraint for the chart version to use.
chartRequired ¶
chart: str

Type: str

The chart name to use. It can be a chart from a helm repository or a local directory.

This name is passed to helm template and has all the relevant semantics.

Example

"bitnami/redis"

helm_executableOptional ¶
helm_executable: str

Type: str
Default: “helm”

The local helm executable to use in order to create the manifest the chart.

helm_flagsOptional ¶
helm_flags: typing.List[str]

Type: typing.List[str]
Default: []

Additional flags to add to the helm execution.

namespaceOptional ¶
namespace: str

Type: str

Scope all resources in to a given namespace.

release_nameOptional ¶
release_name: str

Type: str
Default: if unspecified, a name will be allocated based on the construct path

The release name.

https://helm.sh/docs/intro/using_helm/#three-big-concepts

repoOptional ¶
repo: str

Type: str

Chart repository url where to locate the requested chart.

valuesOptional ¶
values: typing.Mapping[typing.Any]

Type: typing.Mapping[typing.Any]
Default: If no values are specified, chart will use the defaults.

Values to pass to the chart.

versionOptional ¶
version: str

Type: str

Version constraint for the chart version to use.

This constraint can be a specific tag (e.g. 1.1.1) or it may reference a valid range (e.g. ^2.0.0). If this is not specified, the latest version is used

This name is passed to helm template --version and has all the relevant semantics.

Example

"^2.0.0"

IncludeProps ¶
Initializer ¶
import cdk8s

cdk8s.IncludeProps(
  url: str
)

Properties ¶
Name	Type	Description
url	str	Local file path or URL which includes a Kubernetes YAML manifest.
urlRequired ¶
url: str

Type: str

Local file path or URL which includes a Kubernetes YAML manifest.

Example

# Example automatically generated from non-compiling source. May contain errors.
mymanifest.yaml

NameOptions ¶

Options for name generation.

Initializer ¶
import cdk8s

cdk8s.NameOptions(
  delimiter: str = None,
  extra: typing.List[str] = None,
  include_hash: bool = None,
  max_len: typing.Union[int, float] = None
)

Properties ¶
Name	Type	Description
delimiter	str	Delimiter to use between components.
extra	typing.List[str]	Extra components to include in the name.
include_hash	bool	Include a short hash as last part of the name.
max_len	typing.Union[int, float]	Maximum allowed length for the name.
delimiterOptional ¶
delimiter: str

Type: str
Default: “-“

Delimiter to use between components.

extraOptional ¶
extra: typing.List[str]

Type: typing.List[str]
Default: [] use the construct path components

Extra components to include in the name.

include_hashOptional ¶
include_hash: bool

Type: bool
Default: true

Include a short hash as last part of the name.

max_lenOptional ¶
max_len: typing.Union[int, float]

Type: typing.Union[int, float]
Default: 63

Maximum allowed length for the name.

OwnerReference ¶

OwnerReference contains enough information to let you identify an owning object.

An owning object must be in the same namespace as the dependent, or be cluster-scoped, so there is no namespace field.

Initializer ¶
import cdk8s

cdk8s.OwnerReference(
  api_version: str,
  kind: str,
  name: str,
  uid: str,
  block_owner_deletion: bool = None,
  controller: bool = None
)

Properties ¶
Name	Type	Description
api_version	str	API version of the referent.
kind	str	Kind of the referent.
name	str	Name of the referent.
uid	str	UID of the referent.
block_owner_deletion	bool	If true, AND if the owner has the “foregroundDeletion” finalizer, then the owner cannot be deleted from the key-value store until this reference is removed.
controller	bool	If true, this reference points to the managing controller.
api_versionRequired ¶
api_version: str

Type: str

API version of the referent.

kindRequired ¶
kind: str

Type: str

Kind of the referent.

https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds

nameRequired ¶
name: str

Type: str

Name of the referent.

http://kubernetes.io/docs/user-guide/identifiers#names

uidRequired ¶
uid: str

Type: str

UID of the referent.

http://kubernetes.io/docs/user-guide/identifiers#uids

block_owner_deletionOptional ¶
block_owner_deletion: bool

Type: bool
Default: false. To set this field, a user needs “delete” permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.

If true, AND if the owner has the “foregroundDeletion” finalizer, then the owner cannot be deleted from the key-value store until this reference is removed.

Defaults to false. To set this field, a user needs “delete” permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.

controllerOptional ¶
controller: bool

Type: bool

If true, this reference points to the managing controller.

SizeConversionOptions ¶

Options for how to convert size to a different unit.

Initializer ¶
import cdk8s

cdk8s.SizeConversionOptions(
  rounding: SizeRoundingBehavior = None
)

Properties ¶
Name	Type	Description
rounding	SizeRoundingBehavior	How conversions should behave when it encounters a non-integer result.
roundingOptional ¶
rounding: SizeRoundingBehavior

Type: SizeRoundingBehavior
Default: SizeRoundingBehavior.FAIL

How conversions should behave when it encounters a non-integer result.

TimeConversionOptions ¶

Options for how to convert time to a different unit.

Initializer ¶
import cdk8s

cdk8s.TimeConversionOptions(
  integral: bool = None
)

Properties ¶
Name	Type	Description
integral	bool	If true, conversions into a larger time unit (e.g. Seconds to Minutes) will fail if the result is not an integer.
integralOptional ¶
integral: bool

Type: bool
Default: true

If true, conversions into a larger time unit (e.g. Seconds to Minutes) will fail if the result is not an integer.

Classes ¶
ApiObjectMetadataDefinition ¶

Object metadata.

Initializers ¶
import cdk8s

cdk8s.ApiObjectMetadataDefinition(
  annotations: typing.Mapping[str] = None,
  finalizers: typing.List[str] = None,
  labels: typing.Mapping[str] = None,
  name: str = None,
  namespace: str = None,
  owner_references: typing.List[OwnerReference] = None,
  api_object: ApiObject
)

Name	Type	Description
annotations	typing.Mapping[str]	Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata.
finalizers	typing.List[str]	Namespaced keys that tell Kubernetes to wait until specific conditions are met before it fully deletes resources marked for deletion.
labels	typing.Mapping[str]	Map of string keys and values that can be used to organize and categorize (scope and select) objects.
name	str	The unique, namespace-global, name of this object inside the Kubernetes cluster.
namespace	str	Namespace defines the space within each name must be unique.
owner_references	typing.List[OwnerReference]	List of objects depended by this object.
api_object	ApiObject	Which ApiObject instance is the metadata attached to.
annotationsOptional ¶
Type: typing.Mapping[str]
Default: No annotations.

Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata.

They are not queryable and should be preserved when modifying objects.

http://kubernetes.io/docs/user-guide/annotations

finalizersOptional ¶
Type: typing.List[str]
Default: No finalizers.

Namespaced keys that tell Kubernetes to wait until specific conditions are met before it fully deletes resources marked for deletion.

Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.

https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/

labelsOptional ¶
Type: typing.Mapping[str]
Default: No labels.

Map of string keys and values that can be used to organize and categorize (scope and select) objects.

May match selectors of replication controllers and services.

http://kubernetes.io/docs/user-guide/labels

nameOptional ¶
Type: str
Default: an app-unique name generated by the chart

The unique, namespace-global, name of this object inside the Kubernetes cluster.

Normally, you shouldn’t specify names for objects and let the CDK generate a name for you that is application-unique. The names CDK generates are composed from the construct path components, separated by dots and a suffix that is based on a hash of the entire path, to ensure uniqueness.

You can supply custom name allocation logic by overriding the chart.generateObjectName method.

If you use an explicit name here, bear in mind that this reduces the composability of your construct because it won’t be possible to include more than one instance in any app. Therefore it is highly recommended to leave this unspecified.

namespaceOptional ¶
Type: str
Default: undefined (will be assigned to the ‘default’ namespace)

Namespace defines the space within each name must be unique.

An empty namespace is equivalent to the “default” namespace, but “default” is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty. Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces

owner_referencesOptional ¶
Type: typing.List[OwnerReference]
Default: automatically set by Kubernetes

List of objects depended by this object.

If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.

Kubernetes sets the value of this field automatically for objects that are dependents of other objects like ReplicaSets, DaemonSets, Deployments, Jobs and CronJobs, and ReplicationControllers. You can also configure these relationships manually by changing the value of this field. However, you usually don’t need to and can allow Kubernetes to automatically manage the relationships.

https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/

api_objectRequired ¶
Type: ApiObject

Which ApiObject instance is the metadata attached to.

Methods ¶
Name	Description
add	Adds an arbitrary key/value to the object metadata.
add_annotation	Add an annotation.
add_finalizers	Add one or more finalizers.
add_label	Add a label.
add_owner_reference	Add an owner.
get_label	No description.
to_json	Synthesizes a k8s ObjectMeta for this metadata set.
add ¶
def add(
  key: str,
  value: typing.Any
) -> None


Adds an arbitrary key/value to the object metadata.

keyRequired ¶
Type: str

Metadata key.

valueRequired ¶
Type: typing.Any

Metadata value.

add_annotation ¶
def add_annotation(
  key: str,
  value: str
) -> None


Add an annotation.

keyRequired ¶
Type: str

The key.

valueRequired ¶
Type: str

The value.

add_finalizers ¶
def add_finalizers(
  finalizers: *str
) -> None


Add one or more finalizers.

finalizersRequired ¶
Type: *str

the finalizers.

add_label ¶
def add_label(
  key: str,
  value: str
) -> None


Add a label.

keyRequired ¶
Type: str

The key.

valueRequired ¶
Type: str

The value.

add_owner_reference ¶
def add_owner_reference(
  api_version: str,
  kind: str,
  name: str,
  uid: str,
  block_owner_deletion: bool = None,
  controller: bool = None
) -> None


Add an owner.

api_versionRequired ¶
Type: str

API version of the referent.

kindRequired ¶
Type: str

Kind of the referent.

https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds

nameRequired ¶
Type: str

Name of the referent.

http://kubernetes.io/docs/user-guide/identifiers#names

uidRequired ¶
Type: str

UID of the referent.

http://kubernetes.io/docs/user-guide/identifiers#uids

block_owner_deletionOptional ¶
Type: bool
Default: false. To set this field, a user needs “delete” permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.

If true, AND if the owner has the “foregroundDeletion” finalizer, then the owner cannot be deleted from the key-value store until this reference is removed.

Defaults to false. To set this field, a user needs “delete” permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.

controllerOptional ¶
Type: bool

If true, this reference points to the managing controller.

get_label ¶
def get_label(
  key: str
) -> str

keyRequired ¶
Type: str

the label.

to_json ¶
def to_json() -> typing.Any


Synthesizes a k8s ObjectMeta for this metadata set.

Properties ¶
Name	Type	Description
name	str	The name of the API object.
namespace	str	The object’s namespace.
nameOptional ¶
name: str

Type: str

The name of the API object.

If a name is specified in metadata.name this will be the name returned. Otherwise, a name will be generated by calling Chart.of(this).generatedObjectName(this), which by default uses the construct path to generate a DNS-compatible name for the resource.

namespaceOptional ¶
namespace: str

Type: str

The object’s namespace.

Cron ¶

Represents a cron schedule.

Initializers ¶
import cdk8s

cdk8s.Cron(
  day: str = None,
  hour: str = None,
  minute: str = None,
  month: str = None,
  week_day: str = None
)

Name	Type	Description
day	str	The day of the month to run this rule at.
hour	str	The hour to run this rule at.
minute	str	The minute to run this rule at.
month	str	The month to run this rule at.
week_day	str	The day of the week to run this rule at.
dayOptional ¶
Type: str
Default: Every day of the month

The day of the month to run this rule at.

hourOptional ¶
Type: str
Default: Every hour

The hour to run this rule at.

minuteOptional ¶
Type: str
Default: Every minute

The minute to run this rule at.

monthOptional ¶
Type: str
Default: Every month

The month to run this rule at.

week_dayOptional ¶
Type: str
Default: Any day of the week

The day of the week to run this rule at.

Static Functions ¶
Name	Description
annually	Create a cron schedule which runs first day of January every year.
daily	Create a cron schedule which runs every day at midnight.
every_minute	Create a cron schedule which runs every minute.
hourly	Create a cron schedule which runs every hour.
monthly	Create a cron schedule which runs first day of every month.
schedule	Create a custom cron schedule from a set of cron fields.
weekly	Create a cron schedule which runs every week on Sunday.
annually ¶
import cdk8s

cdk8s.Cron.annually()


Create a cron schedule which runs first day of January every year.

daily ¶
import cdk8s

cdk8s.Cron.daily()


Create a cron schedule which runs every day at midnight.

every_minute ¶
import cdk8s

cdk8s.Cron.every_minute()


Create a cron schedule which runs every minute.

hourly ¶
import cdk8s

cdk8s.Cron.hourly()


Create a cron schedule which runs every hour.

monthly ¶
import cdk8s

cdk8s.Cron.monthly()


Create a cron schedule which runs first day of every month.

schedule ¶
import cdk8s

cdk8s.Cron.schedule(
  day: str = None,
  hour: str = None,
  minute: str = None,
  month: str = None,
  week_day: str = None
)


Create a custom cron schedule from a set of cron fields.

dayOptional ¶
Type: str
Default: Every day of the month

The day of the month to run this rule at.

hourOptional ¶
Type: str
Default: Every hour

The hour to run this rule at.

minuteOptional ¶
Type: str
Default: Every minute

The minute to run this rule at.

monthOptional ¶
Type: str
Default: Every month

The month to run this rule at.

week_dayOptional ¶
Type: str
Default: Any day of the week

The day of the week to run this rule at.

weekly ¶
import cdk8s

cdk8s.Cron.weekly()


Create a cron schedule which runs every week on Sunday.

Properties ¶
Name	Type	Description
expression_string	str	Retrieve the expression for this schedule.
expression_stringRequired ¶
expression_string: str

Type: str

Retrieve the expression for this schedule.

DependencyGraph ¶

Represents the dependency graph for a given Node.

This graph includes the dependency relationships between all nodes in the node (construct) sub-tree who’s root is this Node.

Note that this means that lonely nodes (no dependencies and no dependants) are also included in this graph as childless children of the root node of the graph.

The graph does not include cross-scope dependencies. That is, if a child on the current scope depends on a node from a different scope, that relationship is not represented in this graph.

Initializers ¶
import cdk8s

cdk8s.DependencyGraph(
  node: Node
)

Name	Type	Description
node	constructs.Node	No description.
nodeRequired ¶
Type: constructs.Node
Methods ¶
Name	Description
topology	No description.
topology ¶
def topology() -> typing.List[IConstruct]


Vertex.topology ()

Properties ¶
Name	Type	Description
root	DependencyVertex	Returns the root of the graph.
rootRequired ¶
root: DependencyVertex

Type: DependencyVertex

Returns the root of the graph.

Note that this vertex will always have null as its .value since it is an artifical root that binds all the connected spaces of the graph.

DependencyVertex ¶

Represents a vertex in the graph.

The value of each vertex is an IConstruct that is accessible via the .value getter.

Initializers ¶
import cdk8s

cdk8s.DependencyVertex(
  value: IConstruct = None
)

Name	Type	Description
value	constructs.IConstruct	No description.
valueOptional ¶
Type: constructs.IConstruct
Methods ¶
Name	Description
add_child	Adds a vertex as a dependency of the current node.
topology	Returns a topologically sorted array of the constructs in the sub-graph.
add_child ¶
def add_child(
  dep: DependencyVertex
) -> None


Adds a vertex as a dependency of the current node.

Also updates the parents of dep, so that it contains this node as a parent.

This operation will fail in case it creates a cycle in the graph.

depRequired ¶
Type: DependencyVertex

The dependency.

topology ¶
def topology() -> typing.List[IConstruct]


Returns a topologically sorted array of the constructs in the sub-graph.

Properties ¶
Name	Type	Description
inbound	typing.List[DependencyVertex]	Returns the parents of the vertex (i.e dependants).
outbound	typing.List[DependencyVertex]	Returns the children of the vertex (i.e dependencies).
value	constructs.IConstruct	Returns the IConstruct this graph vertex represents.
inboundRequired ¶
inbound: typing.List[DependencyVertex]

Type: typing.List[DependencyVertex]

Returns the parents of the vertex (i.e dependants).

outboundRequired ¶
outbound: typing.List[DependencyVertex]

Type: typing.List[DependencyVertex]

Returns the children of the vertex (i.e dependencies).

valueOptional ¶
value: IConstruct

Type: constructs.IConstruct

Returns the IConstruct this graph vertex represents.

null in case this is the root of the graph.

Duration ¶

Represents a length of time.

The amount can be specified either as a literal value (e.g: 10) which cannot be negative.

Methods ¶
Name	Description
to_days	Return the total number of days in this Duration.
to_hours	Return the total number of hours in this Duration.
to_human_string	Turn this duration into a human-readable string.
to_iso_string	Return an ISO 8601 representation of this period.
to_milliseconds	Return the total number of milliseconds in this Duration.
to_minutes	Return the total number of minutes in this Duration.
to_seconds	Return the total number of seconds in this Duration.
unit_label	Return unit of Duration.
to_days ¶
def to_days(
  integral: bool = None
) -> typing.Union[int, float]


Return the total number of days in this Duration.

integralOptional ¶
Type: bool
Default: true

If true, conversions into a larger time unit (e.g. Seconds to Minutes) will fail if the result is not an integer.

to_hours ¶
def to_hours(
  integral: bool = None
) -> typing.Union[int, float]


Return the total number of hours in this Duration.

integralOptional ¶
Type: bool
Default: true

If true, conversions into a larger time unit (e.g. Seconds to Minutes) will fail if the result is not an integer.

to_human_string ¶
def to_human_string() -> str


Turn this duration into a human-readable string.

to_iso_string ¶
def to_iso_string() -> str


Return an ISO 8601 representation of this period.

https://www.iso.org/fr/standard/70907.html

to_milliseconds ¶
def to_milliseconds(
  integral: bool = None
) -> typing.Union[int, float]


Return the total number of milliseconds in this Duration.

integralOptional ¶
Type: bool
Default: true

If true, conversions into a larger time unit (e.g. Seconds to Minutes) will fail if the result is not an integer.

to_minutes ¶
def to_minutes(
  integral: bool = None
) -> typing.Union[int, float]


Return the total number of minutes in this Duration.

integralOptional ¶
Type: bool
Default: true

If true, conversions into a larger time unit (e.g. Seconds to Minutes) will fail if the result is not an integer.

to_seconds ¶
def to_seconds(
  integral: bool = None
) -> typing.Union[int, float]


Return the total number of seconds in this Duration.

integralOptional ¶
Type: bool
Default: true

If true, conversions into a larger time unit (e.g. Seconds to Minutes) will fail if the result is not an integer.

unit_label ¶
def unit_label() -> str


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
import cdk8s

cdk8s.Duration.days(
  amount: typing.Union[int, float]
)


Create a Duration representing an amount of days.

amountRequired ¶
Type: typing.Union[int, float]

the amount of Days the Duration will represent.

hours ¶
import cdk8s

cdk8s.Duration.hours(
  amount: typing.Union[int, float]
)


Create a Duration representing an amount of hours.

amountRequired ¶
Type: typing.Union[int, float]

the amount of Hours the Duration will represent.

millis ¶
import cdk8s

cdk8s.Duration.millis(
  amount: typing.Union[int, float]
)


Create a Duration representing an amount of milliseconds.

amountRequired ¶
Type: typing.Union[int, float]

the amount of Milliseconds the Duration will represent.

minutes ¶
import cdk8s

cdk8s.Duration.minutes(
  amount: typing.Union[int, float]
)


Create a Duration representing an amount of minutes.

amountRequired ¶
Type: typing.Union[int, float]

the amount of Minutes the Duration will represent.

parse ¶
import cdk8s

cdk8s.Duration.parse(
  duration: str
)


Parse a period formatted according to the ISO 8601 standard.

https://www.iso.org/fr/standard/70907.html

durationRequired ¶
Type: str

an ISO-formtted duration to be parsed.

seconds ¶
import cdk8s

cdk8s.Duration.seconds(
  amount: typing.Union[int, float]
)


Create a Duration representing an amount of seconds.

amountRequired ¶
Type: typing.Union[int, float]

the amount of Seconds the Duration will represent.

ImplicitTokenResolver ¶
Implements: IResolver

Resolves implicit tokens.

Initializers ¶
import cdk8s

cdk8s.ImplicitTokenResolver()

Name	Type	Description
		
Methods ¶
Name	Description
resolve	This function is invoked on every property during cdk8s synthesis.
resolve ¶
def resolve(
  context: ResolutionContext
) -> None


This function is invoked on every property during cdk8s synthesis.

To replace a value, implementations must invoke context.replaceValue.

contextRequired ¶
Type: ResolutionContext
JsonPatch ¶

Utility for applying RFC-6902 JSON-Patch to a document.

Use the the JsonPatch.apply(doc, ...ops) function to apply a set of operations to a JSON document and return the result.

Operations can be created using the factory methods JsonPatch.add(), JsonPatch.remove(), etc.

Example

# Example automatically generated from non-compiling source. May contain errors.
output = JsonPatch.apply(input,
    JsonPatch.replace("/world/hi/there", "goodbye"),
    JsonPatch.add("/world/foo/", "boom"),
    JsonPatch.remove("/hello"))

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
import cdk8s

cdk8s.JsonPatch.add(
  path: str,
  value: typing.Any
)


Adds a value to an object or inserts it into an array.

In the case of an array, the value is inserted before the given index. The - character can be used instead of an index to insert at the end of an array.

Example

# Example automatically generated from non-compiling source. May contain errors.
JsonPatch.add("/biscuits/1", name="Ginger Nut")

pathRequired ¶
Type: str
valueRequired ¶
Type: typing.Any
apply ¶
import cdk8s

cdk8s.JsonPatch.apply(
  document: typing.Any,
  ops: *JsonPatch
)


Applies a set of JSON-Patch (RFC-6902) operations to document and returns the result.

documentRequired ¶
Type: typing.Any

The document to patch.

opsRequired ¶
Type: *JsonPatch

The operations to apply.

copy ¶
import cdk8s

cdk8s.JsonPatch.copy(
  from: str,
  path: str
)


Copies a value from one location to another within the JSON document.

Both from and path are JSON Pointers.

Example

# Example automatically generated from non-compiling source. May contain errors.
JsonPatch.copy("/biscuits/0", "/best_biscuit")

fromRequired ¶
Type: str
pathRequired ¶
Type: str
move ¶
import cdk8s

cdk8s.JsonPatch.move(
  from: str,
  path: str
)


Moves a value from one location to the other.

Both from and path are JSON Pointers.

Example

# Example automatically generated from non-compiling source. May contain errors.
JsonPatch.move("/biscuits", "/cookies")

fromRequired ¶
Type: str
pathRequired ¶
Type: str
remove ¶
import cdk8s

cdk8s.JsonPatch.remove(
  path: str
)


Removes a value from an object or array.

Example

# Example automatically generated from non-compiling source. May contain errors.
JsonPatch.remove("/biscuits/0")

pathRequired ¶
Type: str
replace ¶
import cdk8s

cdk8s.JsonPatch.replace(
  path: str,
  value: typing.Any
)


Replaces a value.

Equivalent to a “remove” followed by an “add”.

Example

# Example automatically generated from non-compiling source. May contain errors.
JsonPatch.replace("/biscuits/0/name", "Chocolate Digestive")

pathRequired ¶
Type: str
valueRequired ¶
Type: typing.Any
test ¶
import cdk8s

cdk8s.JsonPatch.test(
  path: str,
  value: typing.Any
)


Tests that the specified value is set in the document.

If the test fails, then the patch as a whole should not apply.

Example

# Example automatically generated from non-compiling source. May contain errors.
JsonPatch.test("/best_biscuit/name", "Choco Leibniz")

pathRequired ¶
Type: str
valueRequired ¶
Type: typing.Any
Lazy ¶
Methods ¶
Name	Description
produce	No description.
produce ¶
def produce() -> typing.Any

Static Functions ¶
Name	Description
any	No description.
any ¶
import cdk8s

cdk8s.Lazy.any(
  producer: IAnyProducer
)

producerRequired ¶
Type: IAnyProducer
LazyResolver ¶
Implements: IResolver

Resolvers instanecs of Lazy.

Initializers ¶
import cdk8s

cdk8s.LazyResolver()

Name	Type	Description
		
Methods ¶
Name	Description
resolve	This function is invoked on every property during cdk8s synthesis.
resolve ¶
def resolve(
  context: ResolutionContext
) -> None


This function is invoked on every property during cdk8s synthesis.

To replace a value, implementations must invoke context.replaceValue.

contextRequired ¶
Type: ResolutionContext
Names ¶

Utilities for generating unique and stable names.

Static Functions ¶
Name	Description
to_dns_label	Generates a unique and stable name compatible DNS_LABEL from RFC-1123 from a path.
to_label_value	Generates a unique and stable name compatible label key name segment and label value from a path.
to_dns_label ¶
import cdk8s

cdk8s.Names.to_dns_label(
  scope: Construct,
  delimiter: str = None,
  extra: typing.List[str] = None,
  include_hash: bool = None,
  max_len: typing.Union[int, float] = None
)


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
Type: constructs.Construct

The construct for which to render the DNS label.

delimiterOptional ¶
Type: str
Default: “-“

Delimiter to use between components.

extraOptional ¶
Type: typing.List[str]
Default: [] use the construct path components

Extra components to include in the name.

include_hashOptional ¶
Type: bool
Default: true

Include a short hash as last part of the name.

max_lenOptional ¶
Type: typing.Union[int, float]
Default: 63

Maximum allowed length for the name.

to_label_value ¶
import cdk8s

cdk8s.Names.to_label_value(
  scope: Construct,
  delimiter: str = None,
  extra: typing.List[str] = None,
  include_hash: bool = None,
  max_len: typing.Union[int, float] = None
)


Generates a unique and stable name compatible label key name segment and label value from a path.

The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.

Valid label values must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.

The generated name will have the form: ..

Where are the path components (assuming they are is separated by “/”).

Note that if the total length is longer than 63 characters, we will trim the first components since the last components usually encode more meaning.

https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set

scopeRequired ¶
Type: constructs.Construct

The construct for which to render the DNS label.

delimiterOptional ¶
Type: str
Default: “-“

Delimiter to use between components.

extraOptional ¶
Type: typing.List[str]
Default: [] use the construct path components

Extra components to include in the name.

include_hashOptional ¶
Type: bool
Default: true

Include a short hash as last part of the name.

max_lenOptional ¶
Type: typing.Union[int, float]
Default: 63

Maximum allowed length for the name.

NumberStringUnionResolver ¶
Implements: IResolver

Resolves union types that allow using either number or string (as generated by the CLI).

E.g IntOrString, Quantity, …

Initializers ¶
import cdk8s

cdk8s.NumberStringUnionResolver()

Name	Type	Description
		
Methods ¶
Name	Description
resolve	This function is invoked on every property during cdk8s synthesis.
resolve ¶
def resolve(
  context: ResolutionContext
) -> None


This function is invoked on every property during cdk8s synthesis.

To replace a value, implementations must invoke context.replaceValue.

contextRequired ¶
Type: ResolutionContext
ResolutionContext ¶

Context object for a specific resolution process.

Initializers ¶
import cdk8s

cdk8s.ResolutionContext(
  obj: ApiObject,
  key: typing.List[str],
  value: typing.Any
)

Name	Type	Description
obj	ApiObject	Which ApiObject is currently being resolved.
key	typing.List[str]	Which key is currently being resolved.
value	typing.Any	The value associated to the key currently being resolved.
objRequired ¶
Type: ApiObject

Which ApiObject is currently being resolved.

keyRequired ¶
Type: typing.List[str]

Which key is currently being resolved.

valueRequired ¶
Type: typing.Any

The value associated to the key currently being resolved.

Methods ¶
Name	Description
replace_value	Replaces the original value in this resolution context with a new value.
replace_value ¶
def replace_value(
  new_value: typing.Any
) -> None


Replaces the original value in this resolution context with a new value.

The new value is what will end up in the manifest.

new_valueRequired ¶
Type: typing.Any
Properties ¶
Name	Type	Description
key	typing.List[str]	Which key is currently being resolved.
obj	ApiObject	Which ApiObject is currently being resolved.
value	typing.Any	The value associated to the key currently being resolved.
replaced	bool	Whether or not the value was replaced by invoking the replaceValue method.
replaced_value	typing.Any	The replaced value that was set via the replaceValue method.
keyRequired ¶
key: typing.List[str]

Type: typing.List[str]

Which key is currently being resolved.

objRequired ¶
obj: ApiObject

Type: ApiObject

Which ApiObject is currently being resolved.

valueRequired ¶
value: typing.Any

Type: typing.Any

The value associated to the key currently being resolved.

replacedRequired ¶
replaced: bool

Type: bool

Whether or not the value was replaced by invoking the replaceValue method.

replaced_valueRequired ¶
replaced_value: typing.Any

Type: typing.Any

The replaced value that was set via the replaceValue method.

Size ¶

Represents the amount of digital storage.

The amount can be specified either as a literal value (e.g: 10) which cannot be negative.

When the amount is passed as a token, unit conversion is not possible.

Methods ¶
Name	Description
as_string	Returns amount with abbreviated storage unit.
to_gibibytes	Return this storage as a total number of gibibytes.
to_kibibytes	Return this storage as a total number of kibibytes.
to_mebibytes	Return this storage as a total number of mebibytes.
to_pebibytes	Return this storage as a total number of pebibytes.
to_tebibytes	Return this storage as a total number of tebibytes.
as_string ¶
def as_string() -> str


Returns amount with abbreviated storage unit.

to_gibibytes ¶
def to_gibibytes(
  rounding: SizeRoundingBehavior = None
) -> typing.Union[int, float]


Return this storage as a total number of gibibytes.

roundingOptional ¶
Type: SizeRoundingBehavior
Default: SizeRoundingBehavior.FAIL

How conversions should behave when it encounters a non-integer result.

to_kibibytes ¶
def to_kibibytes(
  rounding: SizeRoundingBehavior = None
) -> typing.Union[int, float]


Return this storage as a total number of kibibytes.

roundingOptional ¶
Type: SizeRoundingBehavior
Default: SizeRoundingBehavior.FAIL

How conversions should behave when it encounters a non-integer result.

to_mebibytes ¶
def to_mebibytes(
  rounding: SizeRoundingBehavior = None
) -> typing.Union[int, float]


Return this storage as a total number of mebibytes.

roundingOptional ¶
Type: SizeRoundingBehavior
Default: SizeRoundingBehavior.FAIL

How conversions should behave when it encounters a non-integer result.

to_pebibytes ¶
def to_pebibytes(
  rounding: SizeRoundingBehavior = None
) -> typing.Union[int, float]


Return this storage as a total number of pebibytes.

roundingOptional ¶
Type: SizeRoundingBehavior
Default: SizeRoundingBehavior.FAIL

How conversions should behave when it encounters a non-integer result.

to_tebibytes ¶
def to_tebibytes(
  rounding: SizeRoundingBehavior = None
) -> typing.Union[int, float]


Return this storage as a total number of tebibytes.

roundingOptional ¶
Type: SizeRoundingBehavior
Default: SizeRoundingBehavior.FAIL

How conversions should behave when it encounters a non-integer result.

Static Functions ¶
Name	Description
gibibytes	Create a Storage representing an amount gibibytes.
kibibytes	Create a Storage representing an amount kibibytes.
mebibytes	Create a Storage representing an amount mebibytes.
pebibyte	Create a Storage representing an amount pebibytes.
tebibytes	Create a Storage representing an amount tebibytes.
gibibytes ¶
import cdk8s

cdk8s.Size.gibibytes(
  amount: typing.Union[int, float]
)


Create a Storage representing an amount gibibytes.

1 GiB = 1024 MiB

amountRequired ¶
Type: typing.Union[int, float]
kibibytes ¶
import cdk8s

cdk8s.Size.kibibytes(
  amount: typing.Union[int, float]
)


Create a Storage representing an amount kibibytes.

1 KiB = 1024 bytes

amountRequired ¶
Type: typing.Union[int, float]
mebibytes ¶
import cdk8s

cdk8s.Size.mebibytes(
  amount: typing.Union[int, float]
)


Create a Storage representing an amount mebibytes.

1 MiB = 1024 KiB

amountRequired ¶
Type: typing.Union[int, float]
pebibyte ¶
import cdk8s

cdk8s.Size.pebibyte(
  amount: typing.Union[int, float]
)


Create a Storage representing an amount pebibytes.

1 PiB = 1024 TiB

amountRequired ¶
Type: typing.Union[int, float]
tebibytes ¶
import cdk8s

cdk8s.Size.tebibytes(
  amount: typing.Union[int, float]
)


Create a Storage representing an amount tebibytes.

1 TiB = 1024 GiB

amountRequired ¶
Type: typing.Union[int, float]
Testing ¶

Testing utilities for cdk8s applications.

Static Functions ¶
Name	Description
app	Returns an app for testing with the following properties: - Output directory is a temp dir.
chart	No description.
synth	Returns the Kubernetes manifest synthesized from this chart.
app ¶
import cdk8s

cdk8s.Testing.app(
  outdir: str = None,
  output_file_extension: str = None,
  record_construct_metadata: bool = None,
  resolvers: typing.List[IResolver] = None,
  yaml_output_type: YamlOutputType = None
)


Returns an app for testing with the following properties: - Output directory is a temp dir.

outdirOptional ¶
Type: str
Default: CDK8S_OUTDIR if defined, otherwise “dist”

The directory to output Kubernetes manifests.

If you synthesize your application using cdk8s synth, you must also pass this value to the CLI using the --output option or the output property in the cdk8s.yaml configuration file. Otherwise, the CLI will not know about the output directory, and synthesis will fail.

This property is intended for internal and testing use.

output_file_extensionOptional ¶
Type: str
Default: .k8s.yaml

The file extension to use for rendered YAML files.

record_construct_metadataOptional ¶
Type: bool
Default: false

When set to true, the output directory will contain a construct-metadata.json file that holds construct related metadata on every resource in the app.

resolversOptional ¶
Type: typing.List[IResolver]
Default: no resolvers.

A list of resolvers that can be used to replace property values before they are written to the manifest file.

When multiple resolvers are passed, they are invoked by order in the list, and only the first one that applies (e.g calls context.replaceValue) is invoked.

https://cdk8s.io/docs/latest/basics/app/#resolvers

yaml_output_typeOptional ¶
Type: YamlOutputType
Default: YamlOutputType.FILE_PER_CHART

How to divide the YAML output into files.

chart ¶
import cdk8s

cdk8s.Testing.chart()

synth ¶
import cdk8s

cdk8s.Testing.synth(
  chart: Chart
)


Returns the Kubernetes manifest synthesized from this chart.

chartRequired ¶
Type: Chart
Yaml ¶

YAML utilities.

Static Functions ¶
Name	Description
format_objects	No description.
load	Downloads a set of YAML documents (k8s manifest for example) from a URL or a file and returns them as javascript objects.
save	Saves a set of objects as a multi-document YAML file.
stringify	Stringify a document (or multiple documents) into YAML.
tmp	Saves a set of YAML documents into a temp file (in /tmp).
~~format_objects~~ ¶
import cdk8s

cdk8s.Yaml.format_objects(
  docs: typing.List[typing.Any]
)

docsRequired ¶
Type: typing.List[typing.Any]
load ¶
import cdk8s

cdk8s.Yaml.load(
  url_or_file: str
)


Downloads a set of YAML documents (k8s manifest for example) from a URL or a file and returns them as javascript objects.

Empty documents are filtered out.

url_or_fileRequired ¶
Type: str

a URL of a file path to load from.

save ¶
import cdk8s

cdk8s.Yaml.save(
  file_path: str,
  docs: typing.List[typing.Any]
)


Saves a set of objects as a multi-document YAML file.

file_pathRequired ¶
Type: str

The output path.

docsRequired ¶
Type: typing.List[typing.Any]

The set of objects.

stringify ¶
import cdk8s

cdk8s.Yaml.stringify(
  docs: *typing.Any
)


Stringify a document (or multiple documents) into YAML.

We convert undefined values to null, but ignore any documents that are undefined.

docsRequired ¶
Type: *typing.Any

A set of objects to convert to YAML.

tmp ¶
import cdk8s

cdk8s.Yaml.tmp(
  docs: typing.List[typing.Any]
)


Saves a set of YAML documents into a temp file (in /tmp).

docsRequired ¶
Type: typing.List[typing.Any]

the set of documents to save.

Protocols ¶
IAnyProducer ¶
Implemented By: IAnyProducer
Methods ¶
Name	Description
produce	No description.
produce ¶
def produce() -> typing.Any

IResolver ¶
Implemented By: ImplicitTokenResolver, LazyResolver, NumberStringUnionResolver, IResolver

Contract for resolver objects.

Methods ¶
Name	Description
resolve	This function is invoked on every property during cdk8s synthesis.
resolve ¶
def resolve(
  context: ResolutionContext
) -> None


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
