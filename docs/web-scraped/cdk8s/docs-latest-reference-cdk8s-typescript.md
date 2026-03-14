# Source: https://cdk8s.io/docs/latest/reference/cdk8s/typescript/

Title: TypeScript - cdk8s

URL Source: https://cdk8s.io/docs/latest/reference/cdk8s/typescript/

Markdown Content:
Constructs [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#constructs "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

### ApiObject [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#apiobject "Permanent link")

#### Initializers [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializers "Permanent link")

```
import { ApiObject } from 'cdk8s'

new ApiObject(scope: Construct, id: string, props: ApiObjectProps)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `scope` | `constructs.Construct` | the construct scope. |
| `id` | `string` | namespace. |
| `props` | `ApiObjectProps` | options. |

* * *

##### `scope`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#scoperequired "Permanent link")

*   _Type:_ constructs.Construct

the construct scope.

* * *

##### `id`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#idrequired "Permanent link")

*   _Type:_ string

namespace.

* * *

##### `props`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#propsrequired "Permanent link")

*   _Type:_[ApiObjectProps](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.ApiObjectProps)

options.

* * *

#### Methods [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#methods "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `toString` | Returns a string representation of this construct. |
| `with` | Applies one or more mixins to this construct. |
| `addDependency` | Create a dependency between this ApiObject and other constructs. |
| `addJsonPatch` | Applies a set of RFC-6902 JSON-Patch operations to the manifest synthesized for this API object. |
| `toJson` | Renders the object to Kubernetes JSON. |

* * *

##### `toString`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#tostring "Permanent link")

```
public toString(): string
```

Returns a string representation of this construct.

##### `with`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#with "Permanent link")

```
public with(mixins: ...IMixin[]): IConstruct
```

Applies one or more mixins to this construct.

Mixins are applied in order. The list of constructs is captured at the start of the call, so constructs added by a mixin will not be visited. Use multiple `with()` calls if subsequent mixins should apply to added constructs.

###### `mixins`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#mixinsrequired "Permanent link")

*   _Type:_ …constructs.IMixin[]

The mixins to apply.

* * *

##### `addDependency`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#adddependency "Permanent link")

```
public addDependency(dependencies: ...IConstruct[]): void
```

Create a dependency between this ApiObject and other constructs.

These can be other ApiObjects, Charts, or custom.

###### `dependencies`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#dependenciesrequired "Permanent link")

*   _Type:_ …constructs.IConstruct[]

the dependencies to add.

* * *

##### `addJsonPatch`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#addjsonpatch "Permanent link")

```
public addJsonPatch(ops: ...JsonPatch[]): void
```

Applies a set of RFC-6902 JSON-Patch operations to the manifest synthesized for this API object.

_Example_

```
kubePod.addJsonPatch(JsonPatch.replace('/spec/enableServiceLinks', true));
```

###### `ops`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#opsrequired "Permanent link")

*   _Type:_ …[JsonPatch](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.JsonPatch)[]

The JSON-Patch operations to apply.

* * *

##### `toJson`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#tojson "Permanent link")

```
public toJson(): any
```

Renders the object to Kubernetes JSON.

To disable sorting of dictionary keys in output object set the `CDK8S_DISABLE_SORT` environment variable to any non-empty value.

#### Static Functions [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#static-functions "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `isConstruct` | Checks if `x` is a construct. |
| `isApiObject` | Return whether the given object is an `ApiObject`. |
| `of` | Returns the `ApiObject` named `Resource` which is a child of the given construct. |

* * *

##### `isConstruct`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#isconstruct "Permanent link")

```
import { ApiObject } from 'cdk8s'

ApiObject.isConstruct(x: any)
```

Checks if `x` is a construct.

Use this method instead of `instanceof` to properly detect `Construct` instances, even when the construct library is symlinked.

Explanation: in JavaScript, multiple copies of the `constructs` library on disk are seen as independent, completely different libraries. As a consequence, the class `Construct` in each copy of the `constructs` library is seen as a different class, and an instance of one class will not test as `instanceof` the other class. `npm install` will not create installations like this, but users may manually symlink construct libraries together or use a monorepo tool: in those cases, multiple copies of the `constructs` library can be accidentally installed, and `instanceof` will behave unpredictably. It is safest to avoid using `instanceof`, and using this type-testing method instead.

###### `x`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#xrequired "Permanent link")

*   _Type:_ any

Any object.

* * *

##### `isApiObject`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#isapiobject "Permanent link")

```
import { ApiObject } from 'cdk8s'

ApiObject.isApiObject(o: any)
```

Return whether the given object is an `ApiObject`.

We do attribute detection since we can’t reliably use ‘instanceof’.

###### `o`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#orequired "Permanent link")

*   _Type:_ any

The object to check.

* * *

##### `of`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#of "Permanent link")

```
import { ApiObject } from 'cdk8s'

ApiObject.of(c: IConstruct)
```

Returns the `ApiObject` named `Resource` which is a child of the given construct.

If `c` is an `ApiObject`, it is returned directly. Throws an exception if the construct does not have a child named `Default`_or_ if this child is not an `ApiObject`.

###### `c`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#crequired "Permanent link")

*   _Type:_ constructs.IConstruct

The higher-level construct.

* * *

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `node` | `constructs.Node` | The tree node. |
| `apiGroup` | `string` | The group portion of the API version (e.g. `authorization.k8s.io`). |
| `apiVersion` | `string` | The object’s API version (e.g. `authorization.k8s.io/v1`). |
| `chart` | `Chart` | The chart in which this object is defined. |
| `kind` | `string` | The object kind. |
| `metadata` | `ApiObjectMetadataDefinition` | Metadata associated with this API object. |
| `name` | `string` | The name of the API object. |

* * *

##### `node`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#noderequired "Permanent link")

```
public readonly node: Node;
```

*   _Type:_ constructs.Node

The tree node.

* * *

##### `apiGroup`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#apigrouprequired "Permanent link")

```
public readonly apiGroup: string;
```

*   _Type:_ string

The group portion of the API version (e.g. `authorization.k8s.io`).

* * *

##### `apiVersion`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#apiversionrequired "Permanent link")

```
public readonly apiVersion: string;
```

*   _Type:_ string

The object’s API version (e.g. `authorization.k8s.io/v1`).

* * *

##### `chart`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#chartrequired "Permanent link")

```
public readonly chart: Chart;
```

*   _Type:_[Chart](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.Chart)

The chart in which this object is defined.

* * *

##### `kind`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#kindrequired "Permanent link")

```
public readonly kind: string;
```

*   _Type:_ string

The object kind.

* * *

##### `metadata`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#metadatarequired "Permanent link")

```
public readonly metadata: ApiObjectMetadataDefinition;
```

*   _Type:_[ApiObjectMetadataDefinition](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.ApiObjectMetadataDefinition)

Metadata associated with this API object.

* * *

##### `name`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#namerequired "Permanent link")

```
public readonly name: string;
```

*   _Type:_ string

The name of the API object.

If a name is specified in `metadata.name` this will be the name returned. Otherwise, a name will be generated by calling `Chart.of(this).generatedObjectName(this)`, which by default uses the construct path to generate a DNS-compatible name for the resource.

* * *

### App [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#app "Permanent link")

Represents a cdk8s application.

#### Initializers [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializers_1 "Permanent link")

```
import { App } from 'cdk8s'

new App(props?: AppProps)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `props` | `AppProps` | configuration options. |

* * *

##### `props`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#propsoptional "Permanent link")

*   _Type:_[AppProps](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.AppProps)

configuration options.

* * *

#### Methods [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#methods_1 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `toString` | Returns a string representation of this construct. |
| `with` | Applies one or more mixins to this construct. |
| `synth` | Synthesizes all manifests to the output directory. |
| `synthYaml` | Synthesizes the app into a YAML string. |

* * *

##### `toString`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#tostring_1 "Permanent link")

```
public toString(): string
```

Returns a string representation of this construct.

##### `with`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#with_1 "Permanent link")

```
public with(mixins: ...IMixin[]): IConstruct
```

Applies one or more mixins to this construct.

Mixins are applied in order. The list of constructs is captured at the start of the call, so constructs added by a mixin will not be visited. Use multiple `with()` calls if subsequent mixins should apply to added constructs.

###### `mixins`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#mixinsrequired_1 "Permanent link")

*   _Type:_ …constructs.IMixin[]

The mixins to apply.

* * *

##### `synth`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#synth "Permanent link")

```
public synth(): void
```

Synthesizes all manifests to the output directory.

##### `synthYaml`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#synthyaml "Permanent link")

```
public synthYaml(): string
```

Synthesizes the app into a YAML string.

#### Static Functions [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#static-functions_1 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `isConstruct` | Checks if `x` is a construct. |
| `of` | _No description._ |

* * *

##### `isConstruct`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#isconstruct_1 "Permanent link")

```
import { App } from 'cdk8s'

App.isConstruct(x: any)
```

Checks if `x` is a construct.

Use this method instead of `instanceof` to properly detect `Construct` instances, even when the construct library is symlinked.

Explanation: in JavaScript, multiple copies of the `constructs` library on disk are seen as independent, completely different libraries. As a consequence, the class `Construct` in each copy of the `constructs` library is seen as a different class, and an instance of one class will not test as `instanceof` the other class. `npm install` will not create installations like this, but users may manually symlink construct libraries together or use a monorepo tool: in those cases, multiple copies of the `constructs` library can be accidentally installed, and `instanceof` will behave unpredictably. It is safest to avoid using `instanceof`, and using this type-testing method instead.

###### `x`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#xrequired_1 "Permanent link")

*   _Type:_ any

Any object.

* * *

##### `of`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#of_1 "Permanent link")

```
import { App } from 'cdk8s'

App.of(c: IConstruct)
```

###### `c`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#crequired_1 "Permanent link")

*   _Type:_ constructs.IConstruct

* * *

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_1 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `node` | `constructs.Node` | The tree node. |
| `charts` | `Chart[]` | Returns all the charts in this app, sorted topologically. |
| `outdir` | `string` | The output directory into which manifests will be synthesized. |
| `outputFileExtension` | `string` | The file extension to use for rendered YAML files. |
| `resolvers` | `IResolver[]` | Resolvers used by this app. |
| `yamlOutputType` | `YamlOutputType` | How to divide the YAML output into files. |

* * *

##### `node`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#noderequired_1 "Permanent link")

```
public readonly node: Node;
```

*   _Type:_ constructs.Node

The tree node.

* * *

##### `charts`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#chartsrequired "Permanent link")

```
public readonly charts: Chart[];
```

*   _Type:_[Chart](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.Chart)[]

Returns all the charts in this app, sorted topologically.

* * *

##### `outdir`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#outdirrequired "Permanent link")

```
public readonly outdir: string;
```

*   _Type:_ string

The output directory into which manifests will be synthesized.

* * *

##### `outputFileExtension`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#outputfileextensionrequired "Permanent link")

```
public readonly outputFileExtension: string;
```

*   _Type:_ string
*   _Default:_ .k8s.yaml

The file extension to use for rendered YAML files.

* * *

##### `resolvers`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#resolversrequired "Permanent link")

```
public readonly resolvers: IResolver[];
```

*   _Type:_[IResolver](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.IResolver)[]

Resolvers used by this app.

This includes both custom resolvers passed by the `resolvers` property, as well as built-in resolvers.

* * *

##### `yamlOutputType`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#yamloutputtyperequired "Permanent link")

```
public readonly yamlOutputType: YamlOutputType;
```

*   _Type:_[YamlOutputType](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.YamlOutputType)
*   _Default:_ YamlOutputType.FILE_PER_CHART

How to divide the YAML output into files.

* * *

### Chart [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#chart "Permanent link")

#### Initializers [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializers_2 "Permanent link")

```
import { Chart } from 'cdk8s'

new Chart(scope: Construct, id: string, props?: ChartProps)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `scope` | `constructs.Construct` | _No description._ |
| `id` | `string` | _No description._ |
| `props` | `ChartProps` | _No description._ |

* * *

##### `scope`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#scoperequired_1 "Permanent link")

*   _Type:_ constructs.Construct

* * *

##### `id`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#idrequired_1 "Permanent link")

*   _Type:_ string

* * *

##### `props`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#propsoptional_1 "Permanent link")

*   _Type:_[ChartProps](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.ChartProps)

* * *

#### Methods [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#methods_2 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `toString` | Returns a string representation of this construct. |
| `with` | Applies one or more mixins to this construct. |
| `addDependency` | Create a dependency between this Chart and other constructs. |
| `generateObjectName` | Generates a app-unique name for an object given it’s construct node path. |
| `toJson` | Renders this chart to a set of Kubernetes JSON resources. |

* * *

##### `toString`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#tostring_2 "Permanent link")

```
public toString(): string
```

Returns a string representation of this construct.

##### `with`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#with_2 "Permanent link")

```
public with(mixins: ...IMixin[]): IConstruct
```

Applies one or more mixins to this construct.

Mixins are applied in order. The list of constructs is captured at the start of the call, so constructs added by a mixin will not be visited. Use multiple `with()` calls if subsequent mixins should apply to added constructs.

###### `mixins`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#mixinsrequired_2 "Permanent link")

*   _Type:_ …constructs.IMixin[]

The mixins to apply.

* * *

##### `addDependency`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#adddependency_1 "Permanent link")

```
public addDependency(dependencies: ...IConstruct[]): void
```

Create a dependency between this Chart and other constructs.

These can be other ApiObjects, Charts, or custom.

###### `dependencies`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#dependenciesrequired_1 "Permanent link")

*   _Type:_ …constructs.IConstruct[]

the dependencies to add.

* * *

##### `generateObjectName`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#generateobjectname "Permanent link")

```
public generateObjectName(apiObject: ApiObject): string
```

Generates a app-unique name for an object given it’s construct node path.

Different resource types may have different constraints on names (`metadata.name`). The previous version of the name generator was compatible with DNS_SUBDOMAIN but not with DNS_LABEL.

For example, `Deployment` names must comply with DNS_SUBDOMAIN while `Service` names must comply with DNS_LABEL.

Since there is no formal specification for this, the default name generation scheme for kubernetes objects in cdk8s was changed to DNS_LABEL, since it’s the common denominator for all kubernetes resources (supposedly).

You can override this method if you wish to customize object names at the chart level.

###### `apiObject`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#apiobjectrequired "Permanent link")

*   _Type:_[ApiObject](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.ApiObject)

The API object to generate a name for.

* * *

##### `toJson`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#tojson_1 "Permanent link")

```
public toJson(): any[]
```

Renders this chart to a set of Kubernetes JSON resources.

#### Static Functions [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#static-functions_2 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `isConstruct` | Checks if `x` is a construct. |
| `isChart` | Return whether the given object is a Chart. |
| `of` | Finds the chart in which a node is defined. |

* * *

##### `isConstruct`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#isconstruct_2 "Permanent link")

```
import { Chart } from 'cdk8s'

Chart.isConstruct(x: any)
```

Checks if `x` is a construct.

Use this method instead of `instanceof` to properly detect `Construct` instances, even when the construct library is symlinked.

Explanation: in JavaScript, multiple copies of the `constructs` library on disk are seen as independent, completely different libraries. As a consequence, the class `Construct` in each copy of the `constructs` library is seen as a different class, and an instance of one class will not test as `instanceof` the other class. `npm install` will not create installations like this, but users may manually symlink construct libraries together or use a monorepo tool: in those cases, multiple copies of the `constructs` library can be accidentally installed, and `instanceof` will behave unpredictably. It is safest to avoid using `instanceof`, and using this type-testing method instead.

###### `x`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#xrequired_2 "Permanent link")

*   _Type:_ any

Any object.

* * *

##### `isChart`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#ischart "Permanent link")

```
import { Chart } from 'cdk8s'

Chart.isChart(x: any)
```

Return whether the given object is a Chart.

We do attribute detection since we can’t reliably use ‘instanceof’.

###### `x`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#xrequired_3 "Permanent link")

*   _Type:_ any

* * *

##### `of`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#of_2 "Permanent link")

```
import { Chart } from 'cdk8s'

Chart.of(c: IConstruct)
```

Finds the chart in which a node is defined.

###### `c`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#crequired_2 "Permanent link")

*   _Type:_ constructs.IConstruct

a construct node.

* * *

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_2 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `node` | `constructs.Node` | The tree node. |
| `apiObjects` | `ApiObject[]` | Returns all the included API objects. |
| `labels` | `{[ key: string ]: string}` | Labels applied to all resources in this chart. |
| `namespace` | `string` | The default namespace for all objects in this chart. |

* * *

##### `node`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#noderequired_2 "Permanent link")

```
public readonly node: Node;
```

*   _Type:_ constructs.Node

The tree node.

* * *

##### `apiObjects`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#apiobjectsrequired "Permanent link")

```
public readonly apiObjects: ApiObject[];
```

*   _Type:_[ApiObject](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.ApiObject)[]

Returns all the included API objects.

* * *

##### `labels`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#labelsrequired "Permanent link")

```
public readonly labels: {[ key: string ]: string};
```

*   _Type:_ {[ key: string ]: string}

Labels applied to all resources in this chart.

This is an immutable copy.

* * *

##### `namespace`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#namespaceoptional "Permanent link")

```
public readonly namespace: string;
```

*   _Type:_ string

The default namespace for all objects in this chart.

* * *

### Helm [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#helm "Permanent link")

Represents a Helm deployment.

Use this construct to import an existing Helm chart and incorporate it into your constructs.

#### Initializers [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializers_3 "Permanent link")

```
import { Helm } from 'cdk8s'

new Helm(scope: Construct, id: string, props: HelmProps)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `scope` | `constructs.Construct` | _No description._ |
| `id` | `string` | _No description._ |
| `props` | `HelmProps` | _No description._ |

* * *

##### `scope`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#scoperequired_2 "Permanent link")

*   _Type:_ constructs.Construct

* * *

##### `id`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#idrequired_2 "Permanent link")

*   _Type:_ string

* * *

##### `props`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#propsrequired_1 "Permanent link")

*   _Type:_[HelmProps](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.HelmProps)

* * *

#### Methods [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#methods_3 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `toString` | Returns a string representation of this construct. |
| `with` | Applies one or more mixins to this construct. |

* * *

##### `toString`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#tostring_3 "Permanent link")

```
public toString(): string
```

Returns a string representation of this construct.

##### `with`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#with_3 "Permanent link")

```
public with(mixins: ...IMixin[]): IConstruct
```

Applies one or more mixins to this construct.

Mixins are applied in order. The list of constructs is captured at the start of the call, so constructs added by a mixin will not be visited. Use multiple `with()` calls if subsequent mixins should apply to added constructs.

###### `mixins`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#mixinsrequired_3 "Permanent link")

*   _Type:_ …constructs.IMixin[]

The mixins to apply.

* * *

#### Static Functions [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#static-functions_3 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `isConstruct` | Checks if `x` is a construct. |

* * *

##### `isConstruct`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#isconstruct_3 "Permanent link")

```
import { Helm } from 'cdk8s'

Helm.isConstruct(x: any)
```

Checks if `x` is a construct.

Use this method instead of `instanceof` to properly detect `Construct` instances, even when the construct library is symlinked.

Explanation: in JavaScript, multiple copies of the `constructs` library on disk are seen as independent, completely different libraries. As a consequence, the class `Construct` in each copy of the `constructs` library is seen as a different class, and an instance of one class will not test as `instanceof` the other class. `npm install` will not create installations like this, but users may manually symlink construct libraries together or use a monorepo tool: in those cases, multiple copies of the `constructs` library can be accidentally installed, and `instanceof` will behave unpredictably. It is safest to avoid using `instanceof`, and using this type-testing method instead.

###### `x`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#xrequired_4 "Permanent link")

*   _Type:_ any

Any object.

* * *

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_3 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `node` | `constructs.Node` | The tree node. |
| `apiObjects` | `ApiObject[]` | Returns all the included API objects. |
| `releaseName` | `string` | The helm release name. |

* * *

##### `node`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#noderequired_3 "Permanent link")

```
public readonly node: Node;
```

*   _Type:_ constructs.Node

The tree node.

* * *

##### `apiObjects`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#apiobjectsrequired_1 "Permanent link")

```
public readonly apiObjects: ApiObject[];
```

*   _Type:_[ApiObject](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.ApiObject)[]

Returns all the included API objects.

* * *

##### `releaseName`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#releasenamerequired "Permanent link")

```
public readonly releaseName: string;
```

*   _Type:_ string

The helm release name.

* * *

### Include [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#include "Permanent link")

Reads a YAML manifest from a file or a URL and defines all resources as API objects within the defined scope.

The names (`metadata.name`) of imported resources will be preserved as-is from the manifest.

#### Initializers [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializers_4 "Permanent link")

```
import { Include } from 'cdk8s'

new Include(scope: Construct, id: string, props: IncludeProps)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `scope` | `constructs.Construct` | _No description._ |
| `id` | `string` | _No description._ |
| `props` | `IncludeProps` | _No description._ |

* * *

##### `scope`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#scoperequired_3 "Permanent link")

*   _Type:_ constructs.Construct

* * *

##### `id`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#idrequired_3 "Permanent link")

*   _Type:_ string

* * *

##### `props`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#propsrequired_2 "Permanent link")

*   _Type:_[IncludeProps](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.IncludeProps)

* * *

#### Methods [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#methods_4 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `toString` | Returns a string representation of this construct. |
| `with` | Applies one or more mixins to this construct. |

* * *

##### `toString`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#tostring_4 "Permanent link")

```
public toString(): string
```

Returns a string representation of this construct.

##### `with`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#with_4 "Permanent link")

```
public with(mixins: ...IMixin[]): IConstruct
```

Applies one or more mixins to this construct.

Mixins are applied in order. The list of constructs is captured at the start of the call, so constructs added by a mixin will not be visited. Use multiple `with()` calls if subsequent mixins should apply to added constructs.

###### `mixins`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#mixinsrequired_4 "Permanent link")

*   _Type:_ …constructs.IMixin[]

The mixins to apply.

* * *

#### Static Functions [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#static-functions_4 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `isConstruct` | Checks if `x` is a construct. |

* * *

##### `isConstruct`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#isconstruct_4 "Permanent link")

```
import { Include } from 'cdk8s'

Include.isConstruct(x: any)
```

Checks if `x` is a construct.

Use this method instead of `instanceof` to properly detect `Construct` instances, even when the construct library is symlinked.

Explanation: in JavaScript, multiple copies of the `constructs` library on disk are seen as independent, completely different libraries. As a consequence, the class `Construct` in each copy of the `constructs` library is seen as a different class, and an instance of one class will not test as `instanceof` the other class. `npm install` will not create installations like this, but users may manually symlink construct libraries together or use a monorepo tool: in those cases, multiple copies of the `constructs` library can be accidentally installed, and `instanceof` will behave unpredictably. It is safest to avoid using `instanceof`, and using this type-testing method instead.

###### `x`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#xrequired_5 "Permanent link")

*   _Type:_ any

Any object.

* * *

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_4 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `node` | `constructs.Node` | The tree node. |
| `apiObjects` | `ApiObject[]` | Returns all the included API objects. |

* * *

##### `node`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#noderequired_4 "Permanent link")

```
public readonly node: Node;
```

*   _Type:_ constructs.Node

The tree node.

* * *

##### `apiObjects`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#apiobjectsrequired_2 "Permanent link")

```
public readonly apiObjects: ApiObject[];
```

*   _Type:_[ApiObject](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.ApiObject)[]

Returns all the included API objects.

* * *

Structs [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#structs "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------

### ApiObjectMetadata [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#apiobjectmetadata "Permanent link")

Metadata associated with this object.

#### Initializer [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializer "Permanent link")

```
import { ApiObjectMetadata } from 'cdk8s'

const apiObjectMetadata: ApiObjectMetadata = { ... }
```

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_5 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `annotations` | `{[ key: string ]: string}` | Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. |
| `finalizers` | `string[]` | Namespaced keys that tell Kubernetes to wait until specific conditions are met before it fully deletes resources marked for deletion. |
| `labels` | `{[ key: string ]: string}` | Map of string keys and values that can be used to organize and categorize (scope and select) objects. |
| `name` | `string` | The unique, namespace-global, name of this object inside the Kubernetes cluster. |
| `namespace` | `string` | Namespace defines the space within each name must be unique. |
| `ownerReferences` | `OwnerReference[]` | List of objects depended by this object. |

* * *

##### `annotations`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#annotationsoptional "Permanent link")

```
public readonly annotations: {[ key: string ]: string};
```

*   _Type:_ {[ key: string ]: string}
*   _Default:_ No annotations.

Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata.

They are not queryable and should be preserved when modifying objects.

> [http://kubernetes.io/docs/user-guide/annotations](http://kubernetes.io/docs/user-guide/annotations)

* * *

##### `finalizers`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#finalizersoptional "Permanent link")

```
public readonly finalizers: string[];
```

*   _Type:_ string[]
*   _Default:_ No finalizers.

Namespaced keys that tell Kubernetes to wait until specific conditions are met before it fully deletes resources marked for deletion.

Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.

> [https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/)

* * *

##### `labels`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#labelsoptional "Permanent link")

```
public readonly labels: {[ key: string ]: string};
```

*   _Type:_ {[ key: string ]: string}
*   _Default:_ No labels.

Map of string keys and values that can be used to organize and categorize (scope and select) objects.

May match selectors of replication controllers and services.

> [http://kubernetes.io/docs/user-guide/labels](http://kubernetes.io/docs/user-guide/labels)

* * *

##### `name`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#nameoptional "Permanent link")

```
public readonly name: string;
```

*   _Type:_ string
*   _Default:_ an app-unique name generated by the chart

The unique, namespace-global, name of this object inside the Kubernetes cluster.

Normally, you shouldn’t specify names for objects and let the CDK generate a name for you that is application-unique. The names CDK generates are composed from the construct path components, separated by dots and a suffix that is based on a hash of the entire path, to ensure uniqueness.

You can supply custom name allocation logic by overriding the `chart.generateObjectName` method.

If you use an explicit name here, bear in mind that this reduces the composability of your construct because it won’t be possible to include more than one instance in any app. Therefore it is highly recommended to leave this unspecified.

* * *

##### `namespace`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#namespaceoptional_1 "Permanent link")

```
public readonly namespace: string;
```

*   _Type:_ string
*   _Default:_ undefined (will be assigned to the ‘default’ namespace)

Namespace defines the space within each name must be unique.

An empty namespace is equivalent to the “default” namespace, but “default” is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty. Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces

* * *

##### `ownerReferences`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#ownerreferencesoptional "Permanent link")

```
public readonly ownerReferences: OwnerReference[];
```

*   _Type:_[OwnerReference](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.OwnerReference)[]
*   _Default:_ automatically set by Kubernetes

List of objects depended by this object.

If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.

Kubernetes sets the value of this field automatically for objects that are dependents of other objects like ReplicaSets, DaemonSets, Deployments, Jobs and CronJobs, and ReplicationControllers. You can also configure these relationships manually by changing the value of this field. However, you usually don’t need to and can allow Kubernetes to automatically manage the relationships.

> [https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/](https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/)

* * *

### ApiObjectMetadataDefinitionOptions [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#apiobjectmetadatadefinitionoptions "Permanent link")

Options for `ApiObjectMetadataDefinition`.

#### Initializer [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializer_1 "Permanent link")

```
import { ApiObjectMetadataDefinitionOptions } from 'cdk8s'

const apiObjectMetadataDefinitionOptions: ApiObjectMetadataDefinitionOptions = { ... }
```

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_6 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `annotations` | `{[ key: string ]: string}` | Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. |
| `finalizers` | `string[]` | Namespaced keys that tell Kubernetes to wait until specific conditions are met before it fully deletes resources marked for deletion. |
| `labels` | `{[ key: string ]: string}` | Map of string keys and values that can be used to organize and categorize (scope and select) objects. |
| `name` | `string` | The unique, namespace-global, name of this object inside the Kubernetes cluster. |
| `namespace` | `string` | Namespace defines the space within each name must be unique. |
| `ownerReferences` | `OwnerReference[]` | List of objects depended by this object. |
| `apiObject` | `ApiObject` | Which ApiObject instance is the metadata attached to. |

* * *

##### `annotations`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#annotationsoptional_1 "Permanent link")

```
public readonly annotations: {[ key: string ]: string};
```

*   _Type:_ {[ key: string ]: string}
*   _Default:_ No annotations.

Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata.

They are not queryable and should be preserved when modifying objects.

> [http://kubernetes.io/docs/user-guide/annotations](http://kubernetes.io/docs/user-guide/annotations)

* * *

##### `finalizers`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#finalizersoptional_1 "Permanent link")

```
public readonly finalizers: string[];
```

*   _Type:_ string[]
*   _Default:_ No finalizers.

Namespaced keys that tell Kubernetes to wait until specific conditions are met before it fully deletes resources marked for deletion.

Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.

> [https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/)

* * *

##### `labels`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#labelsoptional_1 "Permanent link")

```
public readonly labels: {[ key: string ]: string};
```

*   _Type:_ {[ key: string ]: string}
*   _Default:_ No labels.

Map of string keys and values that can be used to organize and categorize (scope and select) objects.

May match selectors of replication controllers and services.

> [http://kubernetes.io/docs/user-guide/labels](http://kubernetes.io/docs/user-guide/labels)

* * *

##### `name`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#nameoptional_1 "Permanent link")

```
public readonly name: string;
```

*   _Type:_ string
*   _Default:_ an app-unique name generated by the chart

The unique, namespace-global, name of this object inside the Kubernetes cluster.

Normally, you shouldn’t specify names for objects and let the CDK generate a name for you that is application-unique. The names CDK generates are composed from the construct path components, separated by dots and a suffix that is based on a hash of the entire path, to ensure uniqueness.

You can supply custom name allocation logic by overriding the `chart.generateObjectName` method.

If you use an explicit name here, bear in mind that this reduces the composability of your construct because it won’t be possible to include more than one instance in any app. Therefore it is highly recommended to leave this unspecified.

* * *

##### `namespace`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#namespaceoptional_2 "Permanent link")

```
public readonly namespace: string;
```

*   _Type:_ string
*   _Default:_ undefined (will be assigned to the ‘default’ namespace)

Namespace defines the space within each name must be unique.

An empty namespace is equivalent to the “default” namespace, but “default” is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty. Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces

* * *

##### `ownerReferences`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#ownerreferencesoptional_1 "Permanent link")

```
public readonly ownerReferences: OwnerReference[];
```

*   _Type:_[OwnerReference](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.OwnerReference)[]
*   _Default:_ automatically set by Kubernetes

List of objects depended by this object.

If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.

Kubernetes sets the value of this field automatically for objects that are dependents of other objects like ReplicaSets, DaemonSets, Deployments, Jobs and CronJobs, and ReplicationControllers. You can also configure these relationships manually by changing the value of this field. However, you usually don’t need to and can allow Kubernetes to automatically manage the relationships.

> [https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/](https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/)

* * *

##### `apiObject`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#apiobjectrequired_1 "Permanent link")

```
public readonly apiObject: ApiObject;
```

*   _Type:_[ApiObject](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.ApiObject)

Which ApiObject instance is the metadata attached to.

* * *

### ApiObjectProps [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#apiobjectprops "Permanent link")

Options for defining API objects.

#### Initializer [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializer_2 "Permanent link")

```
import { ApiObjectProps } from 'cdk8s'

const apiObjectProps: ApiObjectProps = { ... }
```

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_7 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `apiVersion` | `string` | API version. |
| `kind` | `string` | Resource kind. |
| `metadata` | `ApiObjectMetadata` | Object metadata. |

* * *

##### `apiVersion`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#apiversionrequired_1 "Permanent link")

```
public readonly apiVersion: string;
```

*   _Type:_ string

API version.

* * *

##### `kind`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#kindrequired_1 "Permanent link")

```
public readonly kind: string;
```

*   _Type:_ string

Resource kind.

* * *

##### `metadata`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#metadataoptional "Permanent link")

```
public readonly metadata: ApiObjectMetadata;
```

*   _Type:_[ApiObjectMetadata](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.ApiObjectMetadata)

Object metadata.

If `name` is not specified, an app-unique name will be allocated by the framework based on the path of the construct within thes construct tree.

* * *

### AppProps [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#appprops "Permanent link")

#### Initializer [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializer_3 "Permanent link")

```
import { AppProps } from 'cdk8s'

const appProps: AppProps = { ... }
```

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_8 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `outdir` | `string` | The directory to output Kubernetes manifests. |
| `outputFileExtension` | `string` | The file extension to use for rendered YAML files. |
| `recordConstructMetadata` | `boolean` | When set to true, the output directory will contain a `construct-metadata.json` file that holds construct related metadata on every resource in the app. |
| `resolvers` | `IResolver[]` | A list of resolvers that can be used to replace property values before they are written to the manifest file. |
| `yamlOutputType` | `YamlOutputType` | How to divide the YAML output into files. |

* * *

##### `outdir`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#outdiroptional "Permanent link")

```
public readonly outdir: string;
```

*   _Type:_ string
*   _Default:_ CDK8S_OUTDIR if defined, otherwise “dist”

The directory to output Kubernetes manifests.

If you synthesize your application using `cdk8s synth`, you must also pass this value to the CLI using the `--output` option or the `output` property in the `cdk8s.yaml` configuration file. Otherwise, the CLI will not know about the output directory, and synthesis will fail.

This property is intended for internal and testing use.

* * *

##### `outputFileExtension`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#outputfileextensionoptional "Permanent link")

```
public readonly outputFileExtension: string;
```

*   _Type:_ string
*   _Default:_ .k8s.yaml

The file extension to use for rendered YAML files.

* * *

##### `recordConstructMetadata`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#recordconstructmetadataoptional "Permanent link")

```
public readonly recordConstructMetadata: boolean;
```

*   _Type:_ boolean
*   _Default:_ false

When set to true, the output directory will contain a `construct-metadata.json` file that holds construct related metadata on every resource in the app.

* * *

##### `resolvers`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#resolversoptional "Permanent link")

```
public readonly resolvers: IResolver[];
```

*   _Type:_[IResolver](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.IResolver)[]
*   _Default:_ no resolvers.

A list of resolvers that can be used to replace property values before they are written to the manifest file.

When multiple resolvers are passed, they are invoked by order in the list, and only the first one that applies (e.g calls `context.replaceValue`) is invoked.

> [https://cdk8s.io/docs/latest/basics/app/#resolvers](https://cdk8s.io/docs/latest/basics/app/#resolvers)

* * *

##### `yamlOutputType`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#yamloutputtypeoptional "Permanent link")

```
public readonly yamlOutputType: YamlOutputType;
```

*   _Type:_[YamlOutputType](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.YamlOutputType)
*   _Default:_ YamlOutputType.FILE_PER_CHART

How to divide the YAML output into files.

* * *

### ChartProps [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#chartprops "Permanent link")

#### Initializer [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializer_4 "Permanent link")

```
import { ChartProps } from 'cdk8s'

const chartProps: ChartProps = { ... }
```

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_9 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `disableResourceNameHashes` | `boolean` | The autogenerated resource name by default is suffixed with a stable hash of the construct path. |
| `labels` | `{[ key: string ]: string}` | Labels to apply to all resources in this chart. |
| `namespace` | `string` | The default namespace for all objects defined in this chart (directly or indirectly). |

* * *

##### `disableResourceNameHashes`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#disableresourcenamehashesoptional "Permanent link")

```
public readonly disableResourceNameHashes: boolean;
```

*   _Type:_ boolean
*   _Default:_ false

The autogenerated resource name by default is suffixed with a stable hash of the construct path.

Setting this property to true drops the hash suffix.

* * *

##### `labels`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#labelsoptional_2 "Permanent link")

```
public readonly labels: {[ key: string ]: string};
```

*   _Type:_ {[ key: string ]: string}
*   _Default:_ no common labels

Labels to apply to all resources in this chart.

* * *

##### `namespace`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#namespaceoptional_3 "Permanent link")

```
public readonly namespace: string;
```

*   _Type:_ string
*   _Default:_ no namespace is synthesized (usually this implies “default”)

The default namespace for all objects defined in this chart (directly or indirectly).

This namespace will only apply to objects that don’t have a `namespace` explicitly defined for them.

* * *

### CronOptions [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cronoptions "Permanent link")

Options to configure a cron expression.

All fields are strings so you can use complex expressions. Absence of a field implies ‘*’

#### Initializer [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializer_5 "Permanent link")

```
import { CronOptions } from 'cdk8s'

const cronOptions: CronOptions = { ... }
```

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_10 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `day` | `string` | The day of the month to run this rule at. |
| `hour` | `string` | The hour to run this rule at. |
| `minute` | `string` | The minute to run this rule at. |
| `month` | `string` | The month to run this rule at. |
| `weekDay` | `string` | The day of the week to run this rule at. |

* * *

##### `day`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#dayoptional "Permanent link")

```
public readonly day: string;
```

*   _Type:_ string
*   _Default:_ Every day of the month

The day of the month to run this rule at.

* * *

##### `hour`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#houroptional "Permanent link")

```
public readonly hour: string;
```

*   _Type:_ string
*   _Default:_ Every hour

The hour to run this rule at.

* * *

##### `minute`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#minuteoptional "Permanent link")

```
public readonly minute: string;
```

*   _Type:_ string
*   _Default:_ Every minute

The minute to run this rule at.

* * *

##### `month`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#monthoptional "Permanent link")

```
public readonly month: string;
```

*   _Type:_ string
*   _Default:_ Every month

The month to run this rule at.

* * *

##### `weekDay`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#weekdayoptional "Permanent link")

```
public readonly weekDay: string;
```

*   _Type:_ string
*   _Default:_ Any day of the week

The day of the week to run this rule at.

* * *

### GroupVersionKind [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#groupversionkind "Permanent link")

#### Initializer [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializer_6 "Permanent link")

```
import { GroupVersionKind } from 'cdk8s'

const groupVersionKind: GroupVersionKind = { ... }
```

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_11 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `apiVersion` | `string` | The object’s API version (e.g. `authorization.k8s.io/v1`). |
| `kind` | `string` | The object kind. |

* * *

##### `apiVersion`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#apiversionrequired_2 "Permanent link")

```
public readonly apiVersion: string;
```

*   _Type:_ string

The object’s API version (e.g. `authorization.k8s.io/v1`).

* * *

##### `kind`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#kindrequired_2 "Permanent link")

```
public readonly kind: string;
```

*   _Type:_ string

The object kind.

* * *

### HelmProps [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#helmprops "Permanent link")

Options for `Helm`.

#### Initializer [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializer_7 "Permanent link")

```
import { HelmProps } from 'cdk8s'

const helmProps: HelmProps = { ... }
```

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_12 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `chart` | `string` | The chart name to use. It can be a chart from a helm repository or a local directory. |
| `helmExecutable` | `string` | The local helm executable to use in order to create the manifest the chart. |
| `helmFlags` | `string[]` | Additional flags to add to the `helm` execution. |
| `namespace` | `string` | Scope all resources in to a given namespace. |
| `releaseName` | `string` | The release name. |
| `repo` | `string` | Chart repository url where to locate the requested chart. |
| `values` | `{[ key: string ]: any}` | Values to pass to the chart. |
| `version` | `string` | Version constraint for the chart version to use. |

* * *

##### `chart`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#chartrequired_1 "Permanent link")

```
public readonly chart: string;
```

*   _Type:_ string

The chart name to use. It can be a chart from a helm repository or a local directory.

This name is passed to `helm template` and has all the relevant semantics.

* * *

_Example_

```
"bitnami/redis"
```

##### `helmExecutable`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#helmexecutableoptional "Permanent link")

```
public readonly helmExecutable: string;
```

*   _Type:_ string
*   _Default:_ “helm”

The local helm executable to use in order to create the manifest the chart.

* * *

##### `helmFlags`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#helmflagsoptional "Permanent link")

```
public readonly helmFlags: string[];
```

*   _Type:_ string[]
*   _Default:_ []

Additional flags to add to the `helm` execution.

* * *

##### `namespace`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#namespaceoptional_4 "Permanent link")

```
public readonly namespace: string;
```

*   _Type:_ string

Scope all resources in to a given namespace.

* * *

##### `releaseName`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#releasenameoptional "Permanent link")

```
public readonly releaseName: string;
```

*   _Type:_ string
*   _Default:_ if unspecified, a name will be allocated based on the construct path

The release name.

> [https://helm.sh/docs/intro/using_helm/#three-big-concepts](https://helm.sh/docs/intro/using_helm/#three-big-concepts)

* * *

##### `repo`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#repooptional "Permanent link")

```
public readonly repo: string;
```

*   _Type:_ string

Chart repository url where to locate the requested chart.

* * *

##### `values`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#valuesoptional "Permanent link")

```
public readonly values: {[ key: string ]: any};
```

*   _Type:_ {[ key: string ]: any}
*   _Default:_ If no values are specified, chart will use the defaults.

Values to pass to the chart.

* * *

##### `version`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#versionoptional "Permanent link")

```
public readonly version: string;
```

*   _Type:_ string

Version constraint for the chart version to use.

This constraint can be a specific tag (e.g. 1.1.1) or it may reference a valid range (e.g. ^2.0.0). If this is not specified, the latest version is used

This name is passed to `helm template --version` and has all the relevant semantics.

* * *

_Example_

```
"^2.0.0"
```

### IncludeProps [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#includeprops "Permanent link")

#### Initializer [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializer_8 "Permanent link")

```
import { IncludeProps } from 'cdk8s'

const includeProps: IncludeProps = { ... }
```

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_13 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `url` | `string` | Local file path or URL which includes a Kubernetes YAML manifest. |

* * *

##### `url`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#urlrequired "Permanent link")

```
public readonly url: string;
```

*   _Type:_ string

Local file path or URL which includes a Kubernetes YAML manifest.

* * *

_Example_

```
mymanifest.yaml
```

### NameOptions [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#nameoptions "Permanent link")

Options for name generation.

#### Initializer [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializer_9 "Permanent link")

```
import { NameOptions } from 'cdk8s'

const nameOptions: NameOptions = { ... }
```

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_14 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `delimiter` | `string` | Delimiter to use between components. |
| `extra` | `string[]` | Extra components to include in the name. |
| `includeHash` | `boolean` | Include a short hash as last part of the name. |
| `maxLen` | `number` | Maximum allowed length for the name. |

* * *

##### `delimiter`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#delimiteroptional "Permanent link")

```
public readonly delimiter: string;
```

*   _Type:_ string
*   _Default:_ “-“

Delimiter to use between components.

* * *

```
public readonly extra: string[];
```

*   _Type:_ string[]
*   _Default:_ [] use the construct path components

Extra components to include in the name.

* * *

##### `includeHash`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#includehashoptional "Permanent link")

```
public readonly includeHash: boolean;
```

*   _Type:_ boolean
*   _Default:_ true

Include a short hash as last part of the name.

* * *

##### `maxLen`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#maxlenoptional "Permanent link")

```
public readonly maxLen: number;
```

*   _Type:_ number
*   _Default:_ 63

Maximum allowed length for the name.

* * *

### OwnerReference [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#ownerreference "Permanent link")

OwnerReference contains enough information to let you identify an owning object.

An owning object must be in the same namespace as the dependent, or be cluster-scoped, so there is no namespace field.

#### Initializer [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializer_10 "Permanent link")

```
import { OwnerReference } from 'cdk8s'

const ownerReference: OwnerReference = { ... }
```

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_15 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `apiVersion` | `string` | API version of the referent. |
| `kind` | `string` | Kind of the referent. |
| `name` | `string` | Name of the referent. |
| `uid` | `string` | UID of the referent. |
| `blockOwnerDeletion` | `boolean` | If true, AND if the owner has the “foregroundDeletion” finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. |
| `controller` | `boolean` | If true, this reference points to the managing controller. |

* * *

##### `apiVersion`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#apiversionrequired_3 "Permanent link")

```
public readonly apiVersion: string;
```

*   _Type:_ string

API version of the referent.

* * *

##### `kind`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#kindrequired_3 "Permanent link")

```
public readonly kind: string;
```

*   _Type:_ string

Kind of the referent.

> [https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds)

* * *

##### `name`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#namerequired_1 "Permanent link")

```
public readonly name: string;
```

*   _Type:_ string

Name of the referent.

> [http://kubernetes.io/docs/user-guide/identifiers#names](http://kubernetes.io/docs/user-guide/identifiers#names)

* * *

##### `uid`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#uidrequired "Permanent link")

```
public readonly uid: string;
```

*   _Type:_ string

UID of the referent.

> [http://kubernetes.io/docs/user-guide/identifiers#uids](http://kubernetes.io/docs/user-guide/identifiers#uids)

* * *

##### `blockOwnerDeletion`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#blockownerdeletionoptional "Permanent link")

```
public readonly blockOwnerDeletion: boolean;
```

*   _Type:_ boolean
*   _Default:_ false. To set this field, a user needs “delete” permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.

If true, AND if the owner has the “foregroundDeletion” finalizer, then the owner cannot be deleted from the key-value store until this reference is removed.

Defaults to false. To set this field, a user needs “delete” permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.

* * *

##### `controller`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#controlleroptional "Permanent link")

```
public readonly controller: boolean;
```

*   _Type:_ boolean

If true, this reference points to the managing controller.

* * *

### SizeConversionOptions [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#sizeconversionoptions "Permanent link")

Options for how to convert size to a different unit.

#### Initializer [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializer_11 "Permanent link")

```
import { SizeConversionOptions } from 'cdk8s'

const sizeConversionOptions: SizeConversionOptions = { ... }
```

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_16 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `rounding` | `SizeRoundingBehavior` | How conversions should behave when it encounters a non-integer result. |

* * *

##### `rounding`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#roundingoptional "Permanent link")

```
public readonly rounding: SizeRoundingBehavior;
```

*   _Type:_[SizeRoundingBehavior](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.SizeRoundingBehavior)
*   _Default:_ SizeRoundingBehavior.FAIL

How conversions should behave when it encounters a non-integer result.

* * *

### TimeConversionOptions [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#timeconversionoptions "Permanent link")

Options for how to convert time to a different unit.

#### Initializer [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializer_12 "Permanent link")

```
import { TimeConversionOptions } from 'cdk8s'

const timeConversionOptions: TimeConversionOptions = { ... }
```

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_17 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `integral` | `boolean` | If `true`, conversions into a larger time unit (e.g. `Seconds` to `Minutes`) will fail if the result is not an integer. |

* * *

##### `integral`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#integraloptional "Permanent link")

```
public readonly integral: boolean;
```

*   _Type:_ boolean
*   _Default:_ true

If `true`, conversions into a larger time unit (e.g. `Seconds` to `Minutes`) will fail if the result is not an integer.

* * *

Classes [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#classes "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------

### ApiObjectMetadataDefinition [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#apiobjectmetadatadefinition "Permanent link")

Object metadata.

#### Initializers [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializers_5 "Permanent link")

```
import { ApiObjectMetadataDefinition } from 'cdk8s'

new ApiObjectMetadataDefinition(options: ApiObjectMetadataDefinitionOptions)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `options` | `ApiObjectMetadataDefinitionOptions` | _No description._ |

* * *

##### `options`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#optionsrequired "Permanent link")

*   _Type:_[ApiObjectMetadataDefinitionOptions](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.ApiObjectMetadataDefinitionOptions)

* * *

#### Methods [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#methods_5 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `add` | Adds an arbitrary key/value to the object metadata. |
| `addAnnotation` | Add an annotation. |
| `addFinalizers` | Add one or more finalizers. |
| `addLabel` | Add a label. |
| `addOwnerReference` | Add an owner. |
| `getLabel` | _No description._ |
| `toJson` | Synthesizes a k8s ObjectMeta for this metadata set. |

* * *

##### `add`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#add "Permanent link")

```
public add(key: string, value: any): void
```

Adds an arbitrary key/value to the object metadata.

###### `key`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#keyrequired "Permanent link")

*   _Type:_ string

Metadata key.

* * *

###### `value`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#valuerequired "Permanent link")

*   _Type:_ any

Metadata value.

* * *

##### `addAnnotation`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#addannotation "Permanent link")

```
public addAnnotation(key: string, value: string): void
```

Add an annotation.

###### `key`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#keyrequired_1 "Permanent link")

*   _Type:_ string

The key.

* * *

###### `value`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#valuerequired_1 "Permanent link")

*   _Type:_ string

The value.

* * *

##### `addFinalizers`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#addfinalizers "Permanent link")

```
public addFinalizers(finalizers: ...string[]): void
```

Add one or more finalizers.

###### `finalizers`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#finalizersrequired "Permanent link")

*   _Type:_ …string[]

the finalizers.

* * *

##### `addLabel`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#addlabel "Permanent link")

```
public addLabel(key: string, value: string): void
```

Add a label.

###### `key`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#keyrequired_2 "Permanent link")

*   _Type:_ string

The key.

* * *

###### `value`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#valuerequired_2 "Permanent link")

*   _Type:_ string

The value.

* * *

##### `addOwnerReference`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#addownerreference "Permanent link")

```
public addOwnerReference(owner: OwnerReference): void
```

Add an owner.

###### `owner`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#ownerrequired "Permanent link")

*   _Type:_[OwnerReference](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.OwnerReference)

the owner.

* * *

##### `getLabel`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#getlabel "Permanent link")

```
public getLabel(key: string): string
```

###### `key`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#keyrequired_3 "Permanent link")

*   _Type:_ string

the label.

* * *

##### `toJson`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#tojson_2 "Permanent link")

```
public toJson(): any
```

Synthesizes a k8s ObjectMeta for this metadata set.

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_18 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `name` | `string` | The name of the API object. |
| `namespace` | `string` | The object’s namespace. |

* * *

##### `name`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#nameoptional_2 "Permanent link")

```
public readonly name: string;
```

*   _Type:_ string

The name of the API object.

If a name is specified in `metadata.name` this will be the name returned. Otherwise, a name will be generated by calling `Chart.of(this).generatedObjectName(this)`, which by default uses the construct path to generate a DNS-compatible name for the resource.

* * *

##### `namespace`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#namespaceoptional_5 "Permanent link")

```
public readonly namespace: string;
```

*   _Type:_ string

The object’s namespace.

* * *

### Cron [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cron "Permanent link")

Represents a cron schedule.

#### Initializers [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializers_6 "Permanent link")

```
import { Cron } from 'cdk8s'

new Cron(cronOptions?: CronOptions)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `cronOptions` | `CronOptions` | _No description._ |

* * *

##### `cronOptions`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cronoptionsoptional "Permanent link")

*   _Type:_[CronOptions](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.CronOptions)

* * *

#### Static Functions [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#static-functions_5 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `annually` | Create a cron schedule which runs first day of January every year. |
| `daily` | Create a cron schedule which runs every day at midnight. |
| `everyMinute` | Create a cron schedule which runs every minute. |
| `hourly` | Create a cron schedule which runs every hour. |
| `monthly` | Create a cron schedule which runs first day of every month. |
| `schedule` | Create a custom cron schedule from a set of cron fields. |
| `weekly` | Create a cron schedule which runs every week on Sunday. |

* * *

##### `annually`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#annually "Permanent link")

```
import { Cron } from 'cdk8s'

Cron.annually()
```

Create a cron schedule which runs first day of January every year.

##### `daily`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#daily "Permanent link")

```
import { Cron } from 'cdk8s'

Cron.daily()
```

Create a cron schedule which runs every day at midnight.

##### `everyMinute`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#everyminute "Permanent link")

```
import { Cron } from 'cdk8s'

Cron.everyMinute()
```

Create a cron schedule which runs every minute.

##### `hourly`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#hourly "Permanent link")

```
import { Cron } from 'cdk8s'

Cron.hourly()
```

Create a cron schedule which runs every hour.

##### `monthly`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#monthly "Permanent link")

```
import { Cron } from 'cdk8s'

Cron.monthly()
```

Create a cron schedule which runs first day of every month.

##### `schedule`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#schedule "Permanent link")

```
import { Cron } from 'cdk8s'

Cron.schedule(options: CronOptions)
```

Create a custom cron schedule from a set of cron fields.

###### `options`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#optionsrequired_1 "Permanent link")

*   _Type:_[CronOptions](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.CronOptions)

* * *

##### `weekly`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#weekly "Permanent link")

```
import { Cron } from 'cdk8s'

Cron.weekly()
```

Create a cron schedule which runs every week on Sunday.

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_19 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `expressionString` | `string` | Retrieve the expression for this schedule. |

* * *

##### `expressionString`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#expressionstringrequired "Permanent link")

```
public readonly expressionString: string;
```

*   _Type:_ string

Retrieve the expression for this schedule.

* * *

### DependencyGraph [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#dependencygraph "Permanent link")

Represents the dependency graph for a given Node.

This graph includes the dependency relationships between all nodes in the node (construct) sub-tree who’s root is this Node.

Note that this means that lonely nodes (no dependencies and no dependants) are also included in this graph as childless children of the root node of the graph.

The graph does not include cross-scope dependencies. That is, if a child on the current scope depends on a node from a different scope, that relationship is not represented in this graph.

#### Initializers [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializers_7 "Permanent link")

```
import { DependencyGraph } from 'cdk8s'

new DependencyGraph(node: Node)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `node` | `constructs.Node` | _No description._ |

* * *

##### `node`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#noderequired_5 "Permanent link")

*   _Type:_ constructs.Node

* * *

#### Methods [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#methods_6 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `topology` | _No description._ |

* * *

##### `topology`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#topology "Permanent link")

```
public topology(): IConstruct[]
```

> [Vertex.topology ()](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/Vertex.topology%20())

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_20 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `root` | `DependencyVertex` | Returns the root of the graph. |

* * *

##### `root`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#rootrequired "Permanent link")

```
public readonly root: DependencyVertex;
```

*   _Type:_[DependencyVertex](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.DependencyVertex)

Returns the root of the graph.

Note that this vertex will always have `null` as its `.value` since it is an artifical root that binds all the connected spaces of the graph.

* * *

### DependencyVertex [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#dependencyvertex "Permanent link")

Represents a vertex in the graph.

The value of each vertex is an `IConstruct` that is accessible via the `.value` getter.

#### Initializers [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializers_8 "Permanent link")

```
import { DependencyVertex } from 'cdk8s'

new DependencyVertex(value?: IConstruct)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `value` | `constructs.IConstruct` | _No description._ |

* * *

##### `value`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#valueoptional "Permanent link")

*   _Type:_ constructs.IConstruct

* * *

#### Methods [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#methods_7 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `addChild` | Adds a vertex as a dependency of the current node. |
| `topology` | Returns a topologically sorted array of the constructs in the sub-graph. |

* * *

##### `addChild`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#addchild "Permanent link")

```
public addChild(dep: DependencyVertex): void
```

Adds a vertex as a dependency of the current node.

Also updates the parents of `dep`, so that it contains this node as a parent.

This operation will fail in case it creates a cycle in the graph.

###### `dep`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#deprequired "Permanent link")

*   _Type:_[DependencyVertex](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.DependencyVertex)

The dependency.

* * *

##### `topology`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#topology_1 "Permanent link")

```
public topology(): IConstruct[]
```

Returns a topologically sorted array of the constructs in the sub-graph.

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_21 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `inbound` | `DependencyVertex[]` | Returns the parents of the vertex (i.e dependants). |
| `outbound` | `DependencyVertex[]` | Returns the children of the vertex (i.e dependencies). |
| `value` | `constructs.IConstruct` | Returns the IConstruct this graph vertex represents. |

* * *

##### `inbound`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#inboundrequired "Permanent link")

```
public readonly inbound: DependencyVertex[];
```

*   _Type:_[DependencyVertex](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.DependencyVertex)[]

Returns the parents of the vertex (i.e dependants).

* * *

##### `outbound`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#outboundrequired "Permanent link")

```
public readonly outbound: DependencyVertex[];
```

*   _Type:_[DependencyVertex](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.DependencyVertex)[]

Returns the children of the vertex (i.e dependencies).

* * *

##### `value`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#valueoptional_1 "Permanent link")

```
public readonly value: IConstruct;
```

*   _Type:_ constructs.IConstruct

Returns the IConstruct this graph vertex represents.

`null` in case this is the root of the graph.

* * *

### Duration [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#duration "Permanent link")

Represents a length of time.

The amount can be specified either as a literal value (e.g: `10`) which cannot be negative.

#### Methods [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#methods_8 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `toDays` | Return the total number of days in this Duration. |
| `toHours` | Return the total number of hours in this Duration. |
| `toHumanString` | Turn this duration into a human-readable string. |
| `toIsoString` | Return an ISO 8601 representation of this period. |
| `toMilliseconds` | Return the total number of milliseconds in this Duration. |
| `toMinutes` | Return the total number of minutes in this Duration. |
| `toSeconds` | Return the total number of seconds in this Duration. |
| `unitLabel` | Return unit of Duration. |

* * *

##### `toDays`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#todays "Permanent link")

```
public toDays(opts?: TimeConversionOptions): number
```

Return the total number of days in this Duration.

###### `opts`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#optsoptional "Permanent link")

*   _Type:_[TimeConversionOptions](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.TimeConversionOptions)

* * *

##### `toHours`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#tohours "Permanent link")

```
public toHours(opts?: TimeConversionOptions): number
```

Return the total number of hours in this Duration.

###### `opts`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#optsoptional_1 "Permanent link")

*   _Type:_[TimeConversionOptions](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.TimeConversionOptions)

* * *

##### `toHumanString`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#tohumanstring "Permanent link")

```
public toHumanString(): string
```

Turn this duration into a human-readable string.

##### `toIsoString`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#toisostring "Permanent link")

```
public toIsoString(): string
```

Return an ISO 8601 representation of this period.

> [https://www.iso.org/fr/standard/70907.html](https://www.iso.org/fr/standard/70907.html)

##### `toMilliseconds`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#tomilliseconds "Permanent link")

```
public toMilliseconds(opts?: TimeConversionOptions): number
```

Return the total number of milliseconds in this Duration.

###### `opts`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#optsoptional_2 "Permanent link")

*   _Type:_[TimeConversionOptions](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.TimeConversionOptions)

* * *

##### `toMinutes`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#tominutes "Permanent link")

```
public toMinutes(opts?: TimeConversionOptions): number
```

Return the total number of minutes in this Duration.

###### `opts`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#optsoptional_3 "Permanent link")

*   _Type:_[TimeConversionOptions](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.TimeConversionOptions)

* * *

##### `toSeconds`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#toseconds "Permanent link")

```
public toSeconds(opts?: TimeConversionOptions): number
```

Return the total number of seconds in this Duration.

###### `opts`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#optsoptional_4 "Permanent link")

*   _Type:_[TimeConversionOptions](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.TimeConversionOptions)

* * *

##### `unitLabel`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#unitlabel "Permanent link")

```
public unitLabel(): string
```

Return unit of Duration.

#### Static Functions [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#static-functions_6 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `days` | Create a Duration representing an amount of days. |
| `hours` | Create a Duration representing an amount of hours. |
| `millis` | Create a Duration representing an amount of milliseconds. |
| `minutes` | Create a Duration representing an amount of minutes. |
| `parse` | Parse a period formatted according to the ISO 8601 standard. |
| `seconds` | Create a Duration representing an amount of seconds. |

* * *

##### `days`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#days "Permanent link")

```
import { Duration } from 'cdk8s'

Duration.days(amount: number)
```

Create a Duration representing an amount of days.

###### `amount`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#amountrequired "Permanent link")

*   _Type:_ number

the amount of Days the `Duration` will represent.

* * *

##### `hours`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#hours "Permanent link")

```
import { Duration } from 'cdk8s'

Duration.hours(amount: number)
```

Create a Duration representing an amount of hours.

###### `amount`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#amountrequired_1 "Permanent link")

*   _Type:_ number

the amount of Hours the `Duration` will represent.

* * *

##### `millis`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#millis "Permanent link")

```
import { Duration } from 'cdk8s'

Duration.millis(amount: number)
```

Create a Duration representing an amount of milliseconds.

###### `amount`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#amountrequired_2 "Permanent link")

*   _Type:_ number

the amount of Milliseconds the `Duration` will represent.

* * *

##### `minutes`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#minutes "Permanent link")

```
import { Duration } from 'cdk8s'

Duration.minutes(amount: number)
```

Create a Duration representing an amount of minutes.

###### `amount`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#amountrequired_3 "Permanent link")

*   _Type:_ number

the amount of Minutes the `Duration` will represent.

* * *

##### `parse`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#parse "Permanent link")

```
import { Duration } from 'cdk8s'

Duration.parse(duration: string)
```

Parse a period formatted according to the ISO 8601 standard.

> [https://www.iso.org/fr/standard/70907.html](https://www.iso.org/fr/standard/70907.html)

###### `duration`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#durationrequired "Permanent link")

*   _Type:_ string

an ISO-formtted duration to be parsed.

* * *

##### `seconds`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#seconds "Permanent link")

```
import { Duration } from 'cdk8s'

Duration.seconds(amount: number)
```

Create a Duration representing an amount of seconds.

###### `amount`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#amountrequired_4 "Permanent link")

*   _Type:_ number

the amount of Seconds the `Duration` will represent.

* * *

### ImplicitTokenResolver [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#implicittokenresolver "Permanent link")

*   _Implements:_[IResolver](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.IResolver)

Resolves implicit tokens.

#### Initializers [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializers_9 "Permanent link")

```
import { ImplicitTokenResolver } from 'cdk8s'

new ImplicitTokenResolver()
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
|  |  |  |

* * *

#### Methods [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#methods_9 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `resolve` | This function is invoked on every property during cdk8s synthesis. |

* * *

##### `resolve`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#resolve "Permanent link")

```
public resolve(context: ResolutionContext): void
```

This function is invoked on every property during cdk8s synthesis.

To replace a value, implementations must invoke `context.replaceValue`.

###### `context`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#contextrequired "Permanent link")

*   _Type:_[ResolutionContext](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.ResolutionContext)

* * *

### JsonPatch [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#jsonpatch "Permanent link")

Utility for applying RFC-6902 JSON-Patch to a document.

Use the the `JsonPatch.apply(doc, ...ops)` function to apply a set of operations to a JSON document and return the result.

Operations can be created using the factory methods `JsonPatch.add()`, `JsonPatch.remove()`, etc.

_Example_

```
const output = JsonPatch.apply(input,
 JsonPatch.replace('/world/hi/there', 'goodbye'),
 JsonPatch.add('/world/foo/', 'boom'),
 JsonPatch.remove('/hello'));
```

#### Static Functions [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#static-functions_7 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `add` | Adds a value to an object or inserts it into an array. |
| `apply` | Applies a set of JSON-Patch (RFC-6902) operations to `document` and returns the result. |
| `copy` | Copies a value from one location to another within the JSON document. |
| `move` | Moves a value from one location to the other. |
| `remove` | Removes a value from an object or array. |
| `replace` | Replaces a value. |
| `test` | Tests that the specified value is set in the document. |

* * *

##### `add`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#add_1 "Permanent link")

```
import { JsonPatch } from 'cdk8s'

JsonPatch.add(path: string, value: any)
```

Adds a value to an object or inserts it into an array.

In the case of an array, the value is inserted before the given index. The - character can be used instead of an index to insert at the end of an array.

_Example_

```
JsonPatch.add('/biscuits/1', { "name": "Ginger Nut" })
```

###### `path`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#pathrequired "Permanent link")

*   _Type:_ string

* * *

###### `value`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#valuerequired_3 "Permanent link")

*   _Type:_ any

* * *

##### `apply`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#apply "Permanent link")

```
import { JsonPatch } from 'cdk8s'

JsonPatch.apply(document: any, ops: ...JsonPatch[])
```

Applies a set of JSON-Patch (RFC-6902) operations to `document` and returns the result.

###### `document`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#documentrequired "Permanent link")

*   _Type:_ any

The document to patch.

* * *

###### `ops`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#opsrequired_1 "Permanent link")

*   _Type:_ …[JsonPatch](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.JsonPatch)[]

The operations to apply.

* * *

##### `copy`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#copy "Permanent link")

```
import { JsonPatch } from 'cdk8s'

JsonPatch.copy(from: string, path: string)
```

Copies a value from one location to another within the JSON document.

Both from and path are JSON Pointers.

_Example_

```
JsonPatch.copy('/biscuits/0', '/best_biscuit')
```

###### `from`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#fromrequired "Permanent link")

*   _Type:_ string

* * *

###### `path`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#pathrequired_1 "Permanent link")

*   _Type:_ string

* * *

##### `move`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#move "Permanent link")

```
import { JsonPatch } from 'cdk8s'

JsonPatch.move(from: string, path: string)
```

Moves a value from one location to the other.

Both from and path are JSON Pointers.

_Example_

```
JsonPatch.move('/biscuits', '/cookies')
```

###### `from`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#fromrequired_1 "Permanent link")

*   _Type:_ string

* * *

###### `path`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#pathrequired_2 "Permanent link")

*   _Type:_ string

* * *

##### `remove`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#remove "Permanent link")

```
import { JsonPatch } from 'cdk8s'

JsonPatch.remove(path: string)
```

Removes a value from an object or array.

_Example_

```
JsonPatch.remove('/biscuits/0')
```

###### `path`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#pathrequired_3 "Permanent link")

*   _Type:_ string

* * *

##### `replace`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#replace "Permanent link")

```
import { JsonPatch } from 'cdk8s'

JsonPatch.replace(path: string, value: any)
```

Replaces a value.

Equivalent to a “remove” followed by an “add”.

_Example_

```
JsonPatch.replace('/biscuits/0/name', 'Chocolate Digestive')
```

###### `path`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#pathrequired_4 "Permanent link")

*   _Type:_ string

* * *

###### `value`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#valuerequired_4 "Permanent link")

*   _Type:_ any

* * *

##### `test`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#test "Permanent link")

```
import { JsonPatch } from 'cdk8s'

JsonPatch.test(path: string, value: any)
```

Tests that the specified value is set in the document.

If the test fails, then the patch as a whole should not apply.

_Example_

```
JsonPatch.test('/best_biscuit/name', 'Choco Leibniz')
```

###### `path`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#pathrequired_5 "Permanent link")

*   _Type:_ string

* * *

###### `value`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#valuerequired_5 "Permanent link")

*   _Type:_ any

* * *

### Lazy [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#lazy "Permanent link")

#### Methods [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#methods_10 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `produce` | _No description._ |

* * *

##### `produce`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#produce "Permanent link")

```
public produce(): any
```

#### Static Functions [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#static-functions_8 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `any` | _No description._ |

* * *

##### `any`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#any "Permanent link")

```
import { Lazy } from 'cdk8s'

Lazy.any(producer: IAnyProducer)
```

###### `producer`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#producerrequired "Permanent link")

*   _Type:_[IAnyProducer](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.IAnyProducer)

* * *

### LazyResolver [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#lazyresolver "Permanent link")

*   _Implements:_[IResolver](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.IResolver)

Resolvers instanecs of `Lazy`.

#### Initializers [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializers_10 "Permanent link")

```
import { LazyResolver } from 'cdk8s'

new LazyResolver()
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
|  |  |  |

* * *

#### Methods [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#methods_11 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `resolve` | This function is invoked on every property during cdk8s synthesis. |

* * *

##### `resolve`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#resolve_1 "Permanent link")

```
public resolve(context: ResolutionContext): void
```

This function is invoked on every property during cdk8s synthesis.

To replace a value, implementations must invoke `context.replaceValue`.

###### `context`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#contextrequired_1 "Permanent link")

*   _Type:_[ResolutionContext](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.ResolutionContext)

* * *

### Names [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#names "Permanent link")

Utilities for generating unique and stable names.

#### Static Functions [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#static-functions_9 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `toDnsLabel` | Generates a unique and stable name compatible DNS_LABEL from RFC-1123 from a path. |
| `toLabelValue` | Generates a unique and stable name compatible label key name segment and label value from a path. |

* * *

##### `toDnsLabel`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#todnslabel "Permanent link")

```
import { Names } from 'cdk8s'

Names.toDnsLabel(scope: Construct, options?: NameOptions)
```

Generates a unique and stable name compatible DNS_LABEL from RFC-1123 from a path.

The generated name will: - contain at most 63 characters - contain only lowercase alphanumeric characters or ‘-’ - start with an alphanumeric character - end with an alphanumeric character

The generated name will have the form: --..--

Where  are the path components (assuming they are is separated by “/”).

Note that if the total length is longer than 63 characters, we will trim the first components since the last components usually encode more meaning.

> [https://tools.ietf.org/html/rfc1123](https://tools.ietf.org/html/rfc1123)

###### `scope`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#scoperequired_4 "Permanent link")

*   _Type:_ constructs.Construct

The construct for which to render the DNS label.

* * *

###### `options`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#optionsoptional "Permanent link")

*   _Type:_[NameOptions](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.NameOptions)

Name options.

* * *

##### `toLabelValue`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#tolabelvalue "Permanent link")

```
import { Names } from 'cdk8s'

Names.toLabelValue(scope: Construct, options?: NameOptions)
```

Generates a unique and stable name compatible label key name segment and label value from a path.

The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.

Valid label values must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.

The generated name will have the form: ..

Where  are the path components (assuming they are is separated by “/”).

Note that if the total length is longer than 63 characters, we will trim the first components since the last components usually encode more meaning.

> [https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set)

###### `scope`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#scoperequired_5 "Permanent link")

*   _Type:_ constructs.Construct

The construct for which to render the DNS label.

* * *

###### `options`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#optionsoptional_1 "Permanent link")

*   _Type:_[NameOptions](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.NameOptions)

Name options.

* * *

### NumberStringUnionResolver [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#numberstringunionresolver "Permanent link")

*   _Implements:_[IResolver](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.IResolver)

Resolves union types that allow using either number or string (as generated by the CLI).

E.g IntOrString, Quantity, …

#### Initializers [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializers_11 "Permanent link")

```
import { NumberStringUnionResolver } from 'cdk8s'

new NumberStringUnionResolver()
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
|  |  |  |

* * *

#### Methods [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#methods_12 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `resolve` | This function is invoked on every property during cdk8s synthesis. |

* * *

##### `resolve`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#resolve_2 "Permanent link")

```
public resolve(context: ResolutionContext): void
```

This function is invoked on every property during cdk8s synthesis.

To replace a value, implementations must invoke `context.replaceValue`.

###### `context`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#contextrequired_2 "Permanent link")

*   _Type:_[ResolutionContext](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.ResolutionContext)

* * *

### ResolutionContext [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#resolutioncontext "Permanent link")

Context object for a specific resolution process.

#### Initializers [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#initializers_12 "Permanent link")

```
import { ResolutionContext } from 'cdk8s'

new ResolutionContext(obj: ApiObject, key: string[], value: any)
```

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `obj` | `ApiObject` | Which ApiObject is currently being resolved. |
| `key` | `string[]` | Which key is currently being resolved. |
| `value` | `any` | The value associated to the key currently being resolved. |

* * *

##### `obj`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#objrequired "Permanent link")

*   _Type:_[ApiObject](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.ApiObject)

Which ApiObject is currently being resolved.

* * *

##### `key`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#keyrequired_4 "Permanent link")

*   _Type:_ string[]

Which key is currently being resolved.

* * *

##### `value`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#valuerequired_6 "Permanent link")

*   _Type:_ any

The value associated to the key currently being resolved.

* * *

#### Methods [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#methods_13 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `replaceValue` | Replaces the original value in this resolution context with a new value. |

* * *

##### `replaceValue`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#replacevalue "Permanent link")

```
public replaceValue(newValue: any): void
```

Replaces the original value in this resolution context with a new value.

The new value is what will end up in the manifest.

###### `newValue`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#newvaluerequired "Permanent link")

*   _Type:_ any

* * *

#### Properties [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#properties_22 "Permanent link")

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `key` | `string[]` | Which key is currently being resolved. |
| `obj` | `ApiObject` | Which ApiObject is currently being resolved. |
| `value` | `any` | The value associated to the key currently being resolved. |
| `replaced` | `boolean` | Whether or not the value was replaced by invoking the `replaceValue` method. |
| `replacedValue` | `any` | The replaced value that was set via the `replaceValue` method. |

* * *

##### `key`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#keyrequired_5 "Permanent link")

```
public readonly key: string[];
```

*   _Type:_ string[]

Which key is currently being resolved.

* * *

##### `obj`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#objrequired_1 "Permanent link")

```
public readonly obj: ApiObject;
```

*   _Type:_[ApiObject](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.ApiObject)

Which ApiObject is currently being resolved.

* * *

##### `value`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#valuerequired_7 "Permanent link")

```
public readonly value: any;
```

*   _Type:_ any

The value associated to the key currently being resolved.

* * *

##### `replaced`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#replacedrequired "Permanent link")

```
public readonly replaced: boolean;
```

*   _Type:_ boolean

Whether or not the value was replaced by invoking the `replaceValue` method.

* * *

##### `replacedValue`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#replacedvaluerequired "Permanent link")

```
public readonly replacedValue: any;
```

*   _Type:_ any

The replaced value that was set via the `replaceValue` method.

* * *

### Size [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#size "Permanent link")

Represents the amount of digital storage.

The amount can be specified either as a literal value (e.g: `10`) which cannot be negative.

When the amount is passed as a token, unit conversion is not possible.

#### Methods [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#methods_14 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `asString` | Returns amount with abbreviated storage unit. |
| `toGibibytes` | Return this storage as a total number of gibibytes. |
| `toKibibytes` | Return this storage as a total number of kibibytes. |
| `toMebibytes` | Return this storage as a total number of mebibytes. |
| `toPebibytes` | Return this storage as a total number of pebibytes. |
| `toTebibytes` | Return this storage as a total number of tebibytes. |

* * *

##### `asString`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#asstring "Permanent link")

```
public asString(): string
```

Returns amount with abbreviated storage unit.

##### `toGibibytes`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#togibibytes "Permanent link")

```
public toGibibytes(opts?: SizeConversionOptions): number
```

Return this storage as a total number of gibibytes.

###### `opts`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#optsoptional_5 "Permanent link")

*   _Type:_[SizeConversionOptions](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.SizeConversionOptions)

* * *

##### `toKibibytes`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#tokibibytes "Permanent link")

```
public toKibibytes(opts?: SizeConversionOptions): number
```

Return this storage as a total number of kibibytes.

###### `opts`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#optsoptional_6 "Permanent link")

*   _Type:_[SizeConversionOptions](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.SizeConversionOptions)

* * *

##### `toMebibytes`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#tomebibytes "Permanent link")

```
public toMebibytes(opts?: SizeConversionOptions): number
```

Return this storage as a total number of mebibytes.

###### `opts`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#optsoptional_7 "Permanent link")

*   _Type:_[SizeConversionOptions](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.SizeConversionOptions)

* * *

##### `toPebibytes`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#topebibytes "Permanent link")

```
public toPebibytes(opts?: SizeConversionOptions): number
```

Return this storage as a total number of pebibytes.

###### `opts`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#optsoptional_8 "Permanent link")

*   _Type:_[SizeConversionOptions](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.SizeConversionOptions)

* * *

##### `toTebibytes`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#totebibytes "Permanent link")

```
public toTebibytes(opts?: SizeConversionOptions): number
```

Return this storage as a total number of tebibytes.

###### `opts`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#optsoptional_9 "Permanent link")

*   _Type:_[SizeConversionOptions](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.SizeConversionOptions)

* * *

#### Static Functions [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#static-functions_10 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `gibibytes` | Create a Storage representing an amount gibibytes. |
| `kibibytes` | Create a Storage representing an amount kibibytes. |
| `mebibytes` | Create a Storage representing an amount mebibytes. |
| `pebibyte` | Create a Storage representing an amount pebibytes. |
| `tebibytes` | Create a Storage representing an amount tebibytes. |

* * *

##### `gibibytes`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#gibibytes "Permanent link")

```
import { Size } from 'cdk8s'

Size.gibibytes(amount: number)
```

Create a Storage representing an amount gibibytes.

1 GiB = 1024 MiB

###### `amount`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#amountrequired_5 "Permanent link")

*   _Type:_ number

* * *

##### `kibibytes`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#kibibytes "Permanent link")

```
import { Size } from 'cdk8s'

Size.kibibytes(amount: number)
```

Create a Storage representing an amount kibibytes.

1 KiB = 1024 bytes

###### `amount`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#amountrequired_6 "Permanent link")

*   _Type:_ number

* * *

##### `mebibytes`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#mebibytes "Permanent link")

```
import { Size } from 'cdk8s'

Size.mebibytes(amount: number)
```

Create a Storage representing an amount mebibytes.

1 MiB = 1024 KiB

###### `amount`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#amountrequired_7 "Permanent link")

*   _Type:_ number

* * *

##### `pebibyte`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#pebibyte "Permanent link")

```
import { Size } from 'cdk8s'

Size.pebibyte(amount: number)
```

Create a Storage representing an amount pebibytes.

1 PiB = 1024 TiB

###### `amount`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#amountrequired_8 "Permanent link")

*   _Type:_ number

* * *

##### `tebibytes`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#tebibytes "Permanent link")

```
import { Size } from 'cdk8s'

Size.tebibytes(amount: number)
```

Create a Storage representing an amount tebibytes.

1 TiB = 1024 GiB

###### `amount`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#amountrequired_9 "Permanent link")

*   _Type:_ number

* * *

### Testing [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#testing "Permanent link")

Testing utilities for cdk8s applications.

#### Static Functions [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#static-functions_11 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `app` | Returns an app for testing with the following properties: - Output directory is a temp dir. |
| `chart` | _No description._ |
| `synth` | Returns the Kubernetes manifest synthesized from this chart. |

* * *

##### `app`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#app_1 "Permanent link")

```
import { Testing } from 'cdk8s'

Testing.app(props?: AppProps)
```

Returns an app for testing with the following properties: - Output directory is a temp dir.

###### `props`Optional[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#propsoptional_2 "Permanent link")

*   _Type:_[AppProps](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.AppProps)

* * *

##### `chart`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#chart_1 "Permanent link")

```
import { Testing } from 'cdk8s'

Testing.chart()
```

##### `synth`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#synth_1 "Permanent link")

```
import { Testing } from 'cdk8s'

Testing.synth(chart: Chart)
```

Returns the Kubernetes manifest synthesized from this chart.

###### `chart`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#chartrequired_2 "Permanent link")

*   _Type:_[Chart](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.Chart)

* * *

### Yaml [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#yaml "Permanent link")

YAML utilities.

#### Static Functions [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#static-functions_12 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `formatObjects` | _No description._ |
| `load` | Downloads a set of YAML documents (k8s manifest for example) from a URL or a file and returns them as javascript objects. |
| `save` | Saves a set of objects as a multi-document YAML file. |
| `stringify` | Stringify a document (or multiple documents) into YAML. |
| `tmp` | Saves a set of YAML documents into a temp file (in /tmp). |

* * *

##### ~~`formatObjects`~~ [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#formatobjects "Permanent link")

```
import { Yaml } from 'cdk8s'

Yaml.formatObjects(docs: any[])
```

###### `docs`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#docsrequired "Permanent link")

*   _Type:_ any[]

* * *

##### `load`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#load "Permanent link")

```
import { Yaml } from 'cdk8s'

Yaml.load(urlOrFile: string)
```

Downloads a set of YAML documents (k8s manifest for example) from a URL or a file and returns them as javascript objects.

Empty documents are filtered out.

###### `urlOrFile`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#urlorfilerequired "Permanent link")

*   _Type:_ string

a URL of a file path to load from.

* * *

##### `save`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#save "Permanent link")

```
import { Yaml } from 'cdk8s'

Yaml.save(filePath: string, docs: any[])
```

Saves a set of objects as a multi-document YAML file.

###### `filePath`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#filepathrequired "Permanent link")

*   _Type:_ string

The output path.

* * *

###### `docs`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#docsrequired_1 "Permanent link")

*   _Type:_ any[]

The set of objects.

* * *

##### `stringify`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#stringify "Permanent link")

```
import { Yaml } from 'cdk8s'

Yaml.stringify(docs: ...any[])
```

Stringify a document (or multiple documents) into YAML.

We convert undefined values to null, but ignore any documents that are undefined.

###### `docs`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#docsrequired_2 "Permanent link")

*   _Type:_ …any[]

A set of objects to convert to YAML.

* * *

##### `tmp`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#tmp "Permanent link")

```
import { Yaml } from 'cdk8s'

Yaml.tmp(docs: any[])
```

Saves a set of YAML documents into a temp file (in /tmp).

###### `docs`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#docsrequired_3 "Permanent link")

*   _Type:_ any[]

the set of documents to save.

* * *

Protocols [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#protocols "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------

### IAnyProducer [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#ianyproducer "Permanent link")

*   _Implemented By:_[IAnyProducer](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.IAnyProducer)

#### Methods [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#methods_15 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `produce` | _No description._ |

* * *

##### `produce`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#produce_1 "Permanent link")

```
public produce(): any
```

### IResolver [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#iresolver "Permanent link")

*   _Implemented By:_[ImplicitTokenResolver](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.ImplicitTokenResolver), [LazyResolver](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.LazyResolver), [NumberStringUnionResolver](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.NumberStringUnionResolver), [IResolver](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.IResolver)

Contract for resolver objects.

#### Methods [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#methods_16 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `resolve` | This function is invoked on every property during cdk8s synthesis. |

* * *

##### `resolve`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#resolve_3 "Permanent link")

```
public resolve(context: ResolutionContext): void
```

This function is invoked on every property during cdk8s synthesis.

To replace a value, implementations must invoke `context.replaceValue`.

###### `context`Required[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#contextrequired_3 "Permanent link")

*   _Type:_[ResolutionContext](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#cdk8s.ResolutionContext)

* * *

Enums [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#enums "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------

### SizeRoundingBehavior [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#sizeroundingbehavior "Permanent link")

Rounding behaviour when converting between units of `Size`.

#### Members [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#members "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `FAIL` | Fail the conversion if the result is not an integer. |
| `FLOOR` | If the result is not an integer, round it to the closest integer less than the result. |
| `NONE` | Don’t round. |

* * *

##### `FAIL`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#fail "Permanent link")

Fail the conversion if the result is not an integer.

* * *

##### `FLOOR`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#floor "Permanent link")

If the result is not an integer, round it to the closest integer less than the result.

* * *

##### `NONE`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#none "Permanent link")

Don’t round.

Return even if the result is a fraction.

* * *

### YamlOutputType [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#yamloutputtype "Permanent link")

The method to divide YAML output into files.

#### Members [](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#members_1 "Permanent link")

| **Name** | **Description** |
| --- | --- |
| `FILE_PER_APP` | All resources are output into a single YAML file. |
| `FILE_PER_CHART` | Resources are split into seperate files by chart. |
| `FILE_PER_RESOURCE` | Each resource is output to its own file. |
| `FOLDER_PER_CHART_FILE_PER_RESOURCE` | Each chart in its own folder and each resource in its own file. |

* * *

##### `FILE_PER_APP`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#file_per_app "Permanent link")

All resources are output into a single YAML file.

* * *

##### `FILE_PER_CHART`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#file_per_chart "Permanent link")

Resources are split into seperate files by chart.

* * *

##### `FILE_PER_RESOURCE`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#file_per_resource "Permanent link")

Each resource is output to its own file.

* * *

##### `FOLDER_PER_CHART_FILE_PER_RESOURCE`[](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)[¶](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/#folder_per_chart_file_per_resource "Permanent link")

Each chart in its own folder and each resource in its own file.

* * *
