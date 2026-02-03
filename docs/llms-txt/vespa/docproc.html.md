# Source: https://docs.vespa.ai/en/reference/applications/services/docproc.html.md

# services.xml - document-processing

 

This is the [document-processing](../../../applications/document-processors.html)reference in [services.xml](services.html):

```
[container](container.html)document-processing [numnodesperclient, preferlocalnode, maxmessagesinqueue, maxqueuebytesize, maxqueuewait, maxconcurrentfactor, documentexpansionfactor, containercorememory][include](container.html#include)[documentprocessor [class, bundle, id, idref, provides, before, after]](#documentprocessor)[provides](#provides)[before](processing.html#before)[after](processing.html#after)[map](#map)[field [doctype, in-document, in-processor]](#map)[chain [name, id, idref, inherits, excludes, documentprocessors]](#chain)[map](#map)[field [doctype, in-document, in-processor]](#map)[inherits](processing.html#inherits)[chain](processing.html#chain)[exclude](processing.html#exclude)[documentprocessor [class, bundle, id, idref, provides, before, after]](#documentprocessor)[provides](#provides)[before](processing.html#before)[after](processing.html#after)[map](#map)[field [doctype, in-document, in-processor]](#map)[phase [id, idref, before, after]](processing.html#phase)[before](processing.html#before)[after](processing.html#after)[threadpool](#threadpool)
```

The root element of the _document-processing_ configuration model.

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| numnodesperclient | optional | | | 

 **Deprecated:** Ignored and deprecated, will be removed in Vespa 9.
 Set to some number below the amount of nodes in the cluster to limit how many nodes a single client can connect to. If you have many clients, this can reduce the memory usage on both document-processing and client nodes. |
| preferlocalnode | optional | | false | 

 **Deprecated:** Ignored and deprecated, will be removed in Vespa 9.
 Set to always prefer sending to a document-processing node running on the same host as the client. You should use this if you are running a client on each document-processing node. |
| maxmessagesinqueue | | | | 

 |
| maxqueuebytesize | | | | 

 **Deprecated:** Ignored and deprecated, will be removed in Vespa 9.
 |
| maxqueuewait | optional | | | 

The maximum number of seconds a message should wait in queue before being processed. Docproc will adapt its queue size to adhere to this. If the queue is full, new messages will be replied to with SESSION\_BUSY.

 |
| maxconcurrentfactor | | | | 

 |
| documentexpansionfactor | optional | | | 

 |
| containercorememory | | | | 

 |

## Document Processor elements

_documentprocessor_ elements are contained in [docproc chain elements](#chain)or in the _document-processing_ root.

A documentprocessor element is either a document processor definition or document processor reference. The rest of this section deals with document processor definitions; document processor references are described in [docproc chain elements](#docproc-chain-elements).

A documentprocessor definition causes the creation of exactly one document processor instance. This instance is set up according to the content of the documentprocessor element.

A documentprocessor definition contained in a docproc chain element defines an_inner document processor_. Otherwise, it defines an _outer document processor._

For inner documentprocessors, the name must be unique inside the docproc chain. For outer documentprocessors, the component id must be unique. An inner documentprocessor is not permitted to have the same name as an outer documentprocessor.

Optional sub-elements:

- provides, a single name that should be added to the provides list
- before, a single name that should be added to the before list
- after, a single name that should be added to the after list
- config (one or more)

For more information on provides, before and after, see [Chained components](../../../applications/chaining.html).

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| class | | | | |
| bundle | | | | |
| id | required | | | 

The component id of the documentprocessor instance.

 |
| idref | | | | |
| provides | optional | | | 

A space-separated list of names that represents what this documentprocessor produces.

 |
| before | optional | | | 

A space-separated list of phase or provided names. Phases or documentprocessors providing these names will be placed later in the docproc chain than this document processor.

 |
| after | optional | | | 

A space-separated list of phase or provided names. Phases or documentprocessors providing these names will be placed earlier in the docproc chain than this document processor.

 |

### documentprocessor

Defines a documentprocessor instance of a user specified class.

```
<documentprocessor id="componentId"
                   class="className:versionSpecification"
                   bundle="the name in <artifactId> in pom.xml">
    ...
</documentprocessor>
```

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| id | required | | | The component id of the documentprocessor instance. |
| class | optional | | | A component specification containing the name of the class to instantiate to create the document processor instance. If missing, copied from id. |
| bundle | optional | | | The bundle containing the class: The name in \<artifactId\> in pom.xml. If a bundle is not specified, the bundle containing document processors bundled with Vespa is used. |

## Docproc chain elements

Specifies how a docproc chain should be instantiated, and how the contained document processors should be ordered.

### chain

Contained in _document-processing_. Refer to the [chain reference](processing.html#chain). Chains can [inherit](processing.html#inherits) document processors from other chains and use [phases](processing.html#phase) for ordering. Optional sub-elements:

- [documentprocessor element](#documentprocessor) (one or more), either a documentprocessor reference or documentprocessor definition. If the name given for a documentprocessor matches an _outer documentprocessor_, it is a _documentprocessor reference_ - otherwise, it is a _documentprocessor definition_. If it is a documentprocessor definition, it is also an implicit documentprocessor reference saying: use _exactly_ this documentprocessor. All these documentprocessor elements must have different name. 
- [phase](processing.html#phase) (one or more). 
- [config](../config-files.html#generic-configuration-in-services-xml) (one or more - will apply to all _inner_ documentprocessors in this docproc chain, unless overridden by individual inner documentprocessors). 

## Map

Set up a field name mapping from the name(s) of field(s) in the input documents to the names used in a deployed docproc. The purpose is to reuse functionality without changing the field names. The example below shows the configuration:

```
<chain name="myChain">
    <map>
        <field in-document="key" in-processor="id"/>
    </map>
    <documentprocessor type="CityDocProc">
        <map>
            <field in-document="town" in-processor="city" doctype="restaurant"/>
        </map>
    </documentprocessor>
    <documentprocessor type="CarDocProc">
        <map>
            <field in-document="engine.cylinders" in-processor="cyl"/>
        </map>
    </documentprocessor>
</chain>
```

In the example, a chain is deployed with 2 docprocs.

For the chain, a mapping from _key_ to _id_ is set up. Imagine that some or all of the docprocs in the chain read and write to a field called _id_, but we want this functionality to the document field _key_.

Furthermore, a similar thing is done for the `CityDocProc`: The docproc accesses the field_city_, whereas it's called _town_ in the feed. The mapping only applies to the document type _restaurant_.

The `CarDocProc` accesses a field called _cyl_. In this example this is mapped to the field _cylinders_ of a struct _engine_using a dotted notation.

If you specify mappings on different levels of the config (say both for a cluster and a docproc), the mapping closest to the actual docproc will take precedence.

## threadpool

Available since Vespa 8.601.12

Specifies configuration for the thread pool used by document processor chains. All values scale with the number of vCPU—see the [container tuning example](../../../performance/container-tuning.html#container-worker-threads-example). When all workers are busy, new document processing requests are rejected.

### threads

Number of worker threads per vCPU. Default value is `1`. The pool runs with `threads * vCPU` workers.

 Copyright © 2026 - [Cookie Preferences](#)

### On this page:

- [Document Processor elements](#document-processor-elements)
- [documentprocessor](#documentprocessor)
- [Docproc chain elements](#docproc-chain-elements)
- [chain](#chain)
- [Map](#map)
- [threadpool](#threadpool)
- [threads](#threadpool-threads)

