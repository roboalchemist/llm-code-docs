# Source: https://docs.vespa.ai/search.html.md

# Source: https://docs.vespa.ai/en/reference/applications/services/search.html.md

# Source: https://docs.vespa.ai/search.html.md

# Source: https://docs.vespa.ai/en/reference/applications/services/search.html.md

# Source: https://docs.vespa.ai/search.html.md

# Source: https://docs.vespa.ai/en/reference/applications/services/search.html.md

# services.xml - 'search'

 

This is the reference for the _search_ part of the container config. Related: [Chained components](../../../applications/chaining.html) and the [federation tutorial](../../../querying/federation.html). The root element of the search configuration, declared as a subelement to [container](container.html):

```
search[binding](#binding)[searcher [id, class, bundle, provides, before, after]](#searcher)[federation [id]](#federation)[source [idref]](#source-reference)[federationoptions [timeout, requestTimeout, optional]](#federationoptions)[source-set [inherits]](#source-set)[target-selector](#target-selector)[chain [id, inherits, excludes]](#chain)[searcher [id, class, bundle, provides, before, after]](#searcher)[federation [id]](#federation)[source [idref]](#source-reference)[federationoptions [timeout, requestTimeout, optional]](#federationoptions)[source-set [inherits]](#source-set)[target-selector](#target-selector)[provider [id, type, cluster, excludes]](#provider)[federationoptions [timeout, requestTimeout, optional]](#federationoptions)[source [id]](#source)[searcher [id, class, bundle, provides, before, after]](#searcher)[renderer [id, class, bundle]](#renderer)[significance](#significance)[threadpool](#threadpool)[threads [max]](#threadpool-threads)[queue](#threadpool-queue)
```

[config](../config-files.html#generic-configuration-in-services-xml) applies to all searchers in the JDisc cluster's search chains, unless overridden by individual search chains or searchers.

## binding

The URI to map the SearchHandler to. The default binding is `http://*/search/*`. Multiple elements are allowed. Example:

```
<binding>http://*/search/*</binding>
```

## searcher

Searcher elements are contained in [chain](#chain) elements or in the search root.

A searcher element is either a _definition_ (using _id_) or a _reference_ (using _idref_).

A searcher definition causes the creation of exactly one searcher instance. This instance is set up according to the content of the searcher element. A searcher definition contained in a search chain element defines an _inner searcher_. Otherwise, it defines an _outer searcher._

Searcher definition:

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| id | required | string | | 

The component id of the searcher instance. For inner searchers, the id must be unique inside the search chain. For outer searchers, the id must be unique. An inner searcher is not permitted to have the same id as an outer searcher.

 |
| class | optional | | | 

A component specification containing the name of the class to instantiate to create the searcher instance. If missing, copied from id

 |
| bundle | optional | | | 

A component specification containing the bundle symbolic name and version used to select the bundle: The name in \<artifactId\> in pom.xml. The class is loaded from this bundle. If no bundle is specified, it defaults to the bundle containing the searchers bundled with Vespa.

 |
| provides | optional | | | 

A space-separated list of names that represents what this searcher produces. For more information on provides, before and after, see [chained components](../../../applications/chaining.html)

 |
| before | optional | | | 

A space-separated list of phase or provided names. Phases or searchers providing these names will be placed later in the search chain than this searcher

 |
| after | optional | | | 

A space-separated list of phase or provided names. Phases or searchers providing these names will be placed earlier in the search chain than this searcher

 |

Example:

```
<searcher id="componentId"
          class="className:versionSpecification"
          bundle="the name in <artifactId> in pom.xml" />
```

Searcher reference:

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| idref | required | string | | 

Reference to a searcher definition

 |

Example:

```
<searcher idref="componentId" />
```

## federation

A federation is a [searcher](../../../applications/searchers.html#searchers) - see above. This element implements _federation_ - it defines a searcher instance that sends each query to a set of search chains in parallel and combines the results. Read the [federation guide](../../../querying/federation.html) to learn more and find examples for use of federation and its children [source](#source), [source-set](#source-set) and [target-selector](#target-selector), as well as [provider](#provider).

```
<federation id="componentId">
    <source idref="componentSpecification" />
    <target-selector />
</federation>
```

## target-selector

Specifies a component that should be used to select search chains to federate to. This component must inherit from com.yahoo.search.federation.selection.TargetSelector. See [component](container.html#component) for attributes and subelements.

## source-set

Used to duplicate the sources of e.g. the built-in federation searcher:

```
<federation id="combinator">
    <source-set inherits="default" />
    …
</federation>
```

## source

Reference to a source that should be used by the enclosing federation searcher. Child element [federationoptions](#federationoptions) is optional.

```
<source idref="componentSpecification">
    <federationoptions/>
</source>
```

## federationoptions

Contained in [source](#source) or [provider](#provider). Specifies _how_ a federation searcher should federate to a given search chain. If a federation options A _overrides_ another federation options B, the result is a new federation options containing:

- all the options in B not present in A
- all the options in A

When federating to a source or provider, the federation searcher per default uses the federation options from the search chain. If a [source reference](#source-reference) contains federation options, it overrides the options of the search chain when used from the enclosing federation searcher.

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| timeout | optional | number | | 

The minimum number of seconds or milliseconds (if ms is present) the federation searcher waits for the federated search chain executing the query

 |
| requestTimeout | optional | number | | 

The minimum number of seconds or milliseconds (if ms is present) the search chain executing the query should continue execution. In some cases it is useful to set this higher than the timeout, such that a chain can keep waiting for requested data longer than the query is waiting for the chain. This allows queries to populate caches within the search chain even though populating the caches requires waiting longer than the query timeout

 |
| optional | optional | true/false | false | 

Determines if the federation searcher should wait for this search chain at all. Normally, it only waits for mandatory (i.e. not optional) search chains, and when they are done, cancels the remaining search chains that are not finished. If all the search chains federated to are optional, all of them will be treated as mandatory. All search chains are per default mandatory

 |

Example:

```
<federationoptions timeout="2.0" requestTimeout="2500ms" optional="true" />
```

## renderer

The definition of a [search result renderer](../../../applications/result-renderers.html).

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| id | required | string | | 

The component ID

 |
| class | optional | string | | 

The class of the component, defaults to id

 |
| bundle | optional | string | | 

The bundle to load the component from: The name in \<artifactId\> in your pom.xml. If no bundle is given, the bundle containing renderers provided by Vespa is used.

 |

Example:

```
<renderer id="componentId"
          class="className:versionSpecification"
          bundle="the name in <artifactId> in pom.xml" />
```

## significance

Contained in [searcher](#searcher). Specifies one or more global significance [models](#model).

```
<significance>
    <model model-id="significance-en-wikipedia-v1"/>
    <model url="https://some/uri/my-model.model.multilingual.json"/>
    <model path="models/my-model.no.json.zst"/>
</significance>
```

The models are either provided by _Vespa_ or generated with [vespa-significance tool](../../operations/self-managed/tools.html#vespa-significance). The order determines model precedence - with the last element having the highest priority. To use these models, schema needs to [enable significance models in the rank-profile](../../schemas/schemas.html#significance).

Sub-elements:

- [model](#model) (required, one or more)

## model

Contained in [significance](#significance). Specifies [global significance model](../../../ranking/significance#global-significance-model). Models are identified by `model-id` or by providing `url` or `path` to a model file in the application package.

Models with `model-id` are provided by _Vespa_ and listed [here](../../../rag/model-hub.html#significance-models). Example with `model-id`:

```
<model model-id="significance-en-wikipedia-v1"/>
```

A model specified with `url` and `path` are JSON files, which can be also compressed with [zstandard](https://facebook.github.io/zstd/). Model files can be generated using [vespa-significance tool](../../operations/self-managed/tools.html#vespa-significance). Example with `url`:

```
<model url="https://some/uri/mymodel.multilingual.json"/>
```

Models with `path` should be placed in the application package. The path is relative to the application package root. Example with `path`:

```
<model path="models/mymodel.no.json.zst"/>
```

## chain

Specifies how a search chain should be instantiated, and how the contained searchers should be ordered. Refer to the [chain reference](processing.html#chain) for attributes and child elements. Chains can [inherit](processing.html#inherits) searchers from other chains and use [phases](processing.html#phase) for ordering. Note that [provider](#provider) and [source](#source) elements are also chains. Specify a search chain in a query using [searchChain](../../api/query.html#searchchain).

Example which inherits from the built-in _vespa_ chain so that the searcher can dispatch queries to the content clusters:

```
<chain id="common" inherits="vespa">
    <searcher class="com.yahoo.vespatest.ExtraHitSearcher" id="CommonSearcher" bundle="the name in <artifactId> in your pom.xml" >
        <config name="vespatest.extra-hit">
            <exampleString>A searcher for ...</exampleString>
        </config>
    </searcher>
</chain>
```

Optional sub-elements:

- searcher or federation (one or more), either a reference or definition. If the name given for a searcher matches an _outer searcher_, it is a _searcher reference_. Otherwise, it is a _searcher definition_. If it is a searcher definition, it is also an implicit searcher reference saying: use _exactly_ this searcher. All these searcher elements must have different name.
- [phase](processing.html#phase) (one or more).
- [config](../config-files.html#generic-configuration-in-services-xml) (one or more - will apply to all _inner_ searchers in this search chain, unless overridden by individual inner searchers).

You can put search config in separate files in a directory under the application package using [include](container.html#include). Each file must contain one `<search>` element like above. Vespa behaves as if each chain configured within was "inline" in `services.xml`. This is handy when multiple developers need to deploy individual search chains, say in different packages.

 **Note:** If using multiple container clusters, the modular search chains will be available in all the clusters.

Each searcher reference must match the _type_ of the searcher definition. So for example the searcher reference _federation idref="myId"_ must match an outer searcher defined as _federation id="myId"_, not _searcher id="myId"_.

## provider

A provider is a search chain responsible for talking to an external service. Everything covered in [chain](#chain) is also valid for providers.

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| id | required | string | | 

ID

 |
| excludes | optional | | | 

 |
| type | optional | local | | 

Determines which searchers are implicitly added to this search chain to talk to the external service.

 |

### local provider

Local providers are providers with the type set to _local_, accessing a local Vespa cluster (i.e. a content cluster in the same application).

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| cluster | required | string | | 

The name of the local cluster.

 |

```
<provider id="music" cluster="music" type="local" excludes="com.yahoo.prelude.querytransform.StemmingSearcher" />
```

## source

Defines a source search chain and an associated source.

```
<provider id="providerA">
    <source id="commonSource">
        <searcher id="com.yahoo.example.AddHitSearcher" bundle="the name in <artifactId> in your pom.xml" >
            <config name="vespatest.hit-title">
                <hitTitle>providerA</hitTitle>
            </config>
        </searcher>
    </source>
</provider>
```

The component id specified is the id of the associated source. The associated source consists of all the source search chains with the same source name.

Only a single source search chain can specify the source name using the "id" attribute. This search chain is called the _leader_. The other source search chains must specify the source name using the "idref" attribute. The latter search chains are called participants.

A source can be used for _federation_. When federating to a source, the leader search chain is normally used. To use one of the participant search chains, the following query parameter must be set: source._sourceId_.provider._providerId_.

The id of the source search chain is _sourceId@providerId_. This search chain automatically inherits from the enclosing provider. It also automatically inherits the federation options of the enclosing provider. If the source contains federation options, they override the inherited ones. In all other respects, this search chain behaves like any other search chain.

## threadpool

Specifies configuration for the thread pool for the jdisc search handler. All parameters are relative to the number of CPU cores—see the [container tuning example](../../../performance/container-tuning.html#container-worker-threads-example). This thread pool also supports the optional `max` attribute, which lets the pool grow up to `max * vCPU` threads under load before shrinking back after 5 seconds of idleness. Requests are rejected once the allowed number of threads is reached, all are busy, and the queue is full.

### threads

The number of permanent threads relative to number of vCPU cores. Default value is `10`.

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| max | optional | number | equal to `<threads>` | 

The maximum number of threads relative to vCPU cores. Value must be greater than or equal to `<threads>`.

 |

### queue

The size of the request queue relative to effective number of threads. Specify `0` to disable queuing. Default value is `40`.

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [binding](#binding)
- [searcher](#searcher)
- [federation](#federation)
- [target-selector](#target-selector)
- [source-set](#source-set)
- [source](#source-reference)
- [federationoptions](#federationoptions)
- [renderer](#renderer)
- [significance](#significance)
- [model](#model)
- [chain](#chain)
- [provider](#provider)
- [local provider](#local-provider)
- [source](#source)
- [threadpool](#threadpool)
- [threads](#threadpool-threads)
- [queue](#threadpool-queue)

