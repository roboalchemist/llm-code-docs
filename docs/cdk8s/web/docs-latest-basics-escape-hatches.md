# Source: https://cdk8s.io/docs/latest/basics/escape-hatches/

Title: Escape Hatches - cdk8s

URL Source: https://cdk8s.io/docs/latest/basics/escape-hatches/

Markdown Content:
Escape Hatches - cdk8s
===============
- [x] - [x] 

[Skip to content](https://cdk8s.io/docs/latest/basics/escape-hatches/#escape-hatches)

[![Image 1: logo](https://cdk8s.io/docs/latest/assets/logo.png)](https://cdk8s.io/ "cdk8s")

 cdk8s 

 Escape Hatches 

 Initializing search 

[cdk8s-team/cdk8s](https://github.com/cdk8s-team/cdk8s "Go to repository")

[![Image 2: logo](https://cdk8s.io/docs/latest/assets/logo.png)](https://cdk8s.io/ "cdk8s") cdk8s  

[cdk8s-team/cdk8s](https://github.com/cdk8s-team/cdk8s "Go to repository")

*   [What is cdk8s?](https://cdk8s.io/docs/latest/)
*   - [x] [Getting started](https://cdk8s.io/docs/latest/get-started/)  Getting started  
    *   [Python](https://cdk8s.io/docs/latest/get-started/python/)
    *   [TypeScript](https://cdk8s.io/docs/latest/get-started/typescript/)
    *   [Java](https://cdk8s.io/docs/latest/get-started/java/)
    *   [Go](https://cdk8s.io/docs/latest/get-started/go/)

*   - [x] [Basics](https://cdk8s.io/docs/latest/basics/)  Basics  
    *   [Constructs](https://cdk8s.io/docs/latest/basics/constructs/)
    *   [Chart](https://cdk8s.io/docs/latest/basics/chart/)
    *   [ApiObject](https://cdk8s.io/docs/latest/basics/api-object/)
    *   [Dependencies](https://cdk8s.io/docs/latest/basics/deps/)
    *   [App](https://cdk8s.io/docs/latest/basics/app/)
    *   - [x]  Escape Hatches  [Escape Hatches](https://cdk8s.io/docs/latest/basics/escape-hatches/) On this page  
        *   [Patching API objects directly](https://cdk8s.io/docs/latest/basics/escape-hatches/#patching-api-objects-directly)
        *   [Patching API objects behind higher-level APIs](https://cdk8s.io/docs/latest/basics/escape-hatches/#patching-api-objects-behind-higher-level-apis)

    *   [Helm Support](https://cdk8s.io/docs/latest/basics/helm/)
    *   [Include](https://cdk8s.io/docs/latest/basics/include/)
    *   [Testing](https://cdk8s.io/docs/latest/basics/testing/)

*   - [x] [cdk8s+](https://cdk8s.io/docs/latest/plus/)  cdk8s+  
    *   - [x]  cdk8s-plus-31   cdk8s-plus-31  
        *   [ConfigMap](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/config-map/)
        *   [Container](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/container/)
        *   [CronJob](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/cronjob/)
        *   [Deployment](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/deployment/)
        *   [HorizontalPodAutoscaler](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/horizontal-pod-autoscaler/)
        *   [Ingress](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/ingress/)
        *   [Job](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/job/)
        *   [Namespace](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/namespace/)
        *   [Network Policy](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/network-policy/)
        *   [Pod](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/pod/)
        *   [PersistentVolume](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/pv/)
        *   [PersistentVolumeClaim](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/pvc/)
        *   [Role Based Access Control](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/rbac/)
        *   [Secret](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/secret/)
        *   [ServiceAccount](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/service-account/)
        *   [Service](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/service/)
        *   [Volume](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/volume/)

    *   - [x]  cdk8s-plus-32   cdk8s-plus-32  
        *   [ConfigMap](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/config-map/)
        *   [Container](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/container/)
        *   [CronJob](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/cronjob/)
        *   [Deployment](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/deployment/)
        *   [HorizontalPodAutoscaler](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/horizontal-pod-autoscaler/)
        *   [Ingress](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/ingress/)
        *   [Job](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/job/)
        *   [Namespace](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/namespace/)
        *   [Network Policy](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/network-policy/)
        *   [Pod](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/pod/)
        *   [PersistentVolume](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/pv/)
        *   [PersistentVolumeClaim](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/pvc/)
        *   [Role Based Access Control](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/)
        *   [Secret](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/secret/)
        *   [ServiceAccount](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/service-account/)
        *   [Service](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/service/)
        *   [Volume](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/volume/)

    *   - [x]  cdk8s-plus-33   cdk8s-plus-33  
        *   [ConfigMap](https://cdk8s.io/docs/latest/plus/cdk8s-plus-33/config-map/)
        *   [Container](https://cdk8s.io/docs/latest/plus/cdk8s-plus-33/container/)
        *   [CronJob](https://cdk8s.io/docs/latest/plus/cdk8s-plus-33/cronjob/)
        *   [Deployment](https://cdk8s.io/docs/latest/plus/cdk8s-plus-33/deployment/)
        *   [HorizontalPodAutoscaler](https://cdk8s.io/docs/latest/plus/cdk8s-plus-33/horizontal-pod-autoscaler/)
        *   [Ingress](https://cdk8s.io/docs/latest/plus/cdk8s-plus-33/ingress/)
        *   [Job](https://cdk8s.io/docs/latest/plus/cdk8s-plus-33/job/)
        *   [Namespace](https://cdk8s.io/docs/latest/plus/cdk8s-plus-33/namespace/)
        *   [Network Policy](https://cdk8s.io/docs/latest/plus/cdk8s-plus-33/network-policy/)
        *   [Pod](https://cdk8s.io/docs/latest/plus/cdk8s-plus-33/pod/)
        *   [PersistentVolume](https://cdk8s.io/docs/latest/plus/cdk8s-plus-33/pv/)
        *   [PersistentVolumeClaim](https://cdk8s.io/docs/latest/plus/cdk8s-plus-33/pvc/)
        *   [Role Based Access Control](https://cdk8s.io/docs/latest/plus/cdk8s-plus-33/rbac/)
        *   [Secret](https://cdk8s.io/docs/latest/plus/cdk8s-plus-33/secret/)
        *   [ServiceAccount](https://cdk8s.io/docs/latest/plus/cdk8s-plus-33/service-account/)
        *   [Service](https://cdk8s.io/docs/latest/plus/cdk8s-plus-33/service/)
        *   [Volume](https://cdk8s.io/docs/latest/plus/cdk8s-plus-33/volume/)

*   - [x] [CLI](https://cdk8s.io/docs/latest/cli/)  CLI  
    *   [Install the cdk8s CLI](https://cdk8s.io/docs/latest/cli/installation/)
    *   [init](https://cdk8s.io/docs/latest/cli/init/)
    *   [import](https://cdk8s.io/docs/latest/cli/import/)
    *   [synth](https://cdk8s.io/docs/latest/cli/synth/)

*   - [x] [API Reference](https://cdk8s.io/docs/latest/reference/)  API Reference  
    *   - [x]  cdk8s   cdk8s  
        *   [TypeScript](https://cdk8s.io/docs/latest/reference/cdk8s/typescript/)
        *   [Python](https://cdk8s.io/docs/latest/reference/cdk8s/python/)
        *   [Java](https://cdk8s.io/docs/latest/reference/cdk8s/java/)
        *   [Go](https://cdk8s.io/docs/latest/reference/cdk8s/go/)

    *   - [x]  cdk8s-plus-31   cdk8s-plus-31  
        *   [TypeScript](https://cdk8s.io/docs/latest/reference/cdk8s-plus-31/typescript/)
        *   [Python](https://cdk8s.io/docs/latest/reference/cdk8s-plus-31/python/)
        *   [Java](https://cdk8s.io/docs/latest/reference/cdk8s-plus-31/java/)
        *   [Go](https://cdk8s.io/docs/latest/reference/cdk8s-plus-31/go/)

    *   - [x]  cdk8s-plus-32   cdk8s-plus-32  
        *   [TypeScript](https://cdk8s.io/docs/latest/reference/cdk8s-plus-32/typescript/)
        *   [Python](https://cdk8s.io/docs/latest/reference/cdk8s-plus-32/python/)
        *   [Java](https://cdk8s.io/docs/latest/reference/cdk8s-plus-32/java/)
        *   [Go](https://cdk8s.io/docs/latest/reference/cdk8s-plus-32/go/)

    *   - [x]  cdk8s-plus-33   cdk8s-plus-33  
        *   [TypeScript](https://cdk8s.io/docs/latest/reference/cdk8s-plus-33/typescript/)
        *   [Python](https://cdk8s.io/docs/latest/reference/cdk8s-plus-33/python/)
        *   [Java](https://cdk8s.io/docs/latest/reference/cdk8s-plus-33/java/)
        *   [Go](https://cdk8s.io/docs/latest/reference/cdk8s-plus-33/go/)

*   - [x] [Examples](https://cdk8s.io/docs/latest/examples/)  Examples  

*   [Ecosystem Interoperability](https://cdk8s.io/docs/latest/ecosystem-interoperability/)
*   [Migrating from 1.x](https://cdk8s.io/docs/latest/migrating-from-1.x/)
*   - [x]  Support   Support  
    *   [Issues](https://github.com/cdk8s-team/cdk8s/issues/)
    *   [Report a new issue](https://github.com/cdk8s-team/cdk8s/issues/new/choose)
    *   [Stack overflow](https://stackoverflow.com/questions/tagged/cdk8s)
    *   [Slack](https://cdk.dev/)
    *   [Mailing list](https://groups.google.com/forum/#!forum/cdk8s)

*   [Changelog](https://cdk8s.io/docs/latest/CHANGELOG/)
*   [Roadmap](https://cdk8s.io/docs/latest/ROADMAP/)
*   [Contribution guide](https://cdk8s.io/docs/latest/CONTRIBUTING/)
*   [Media](https://cdk8s.io/docs/latest/media/)

 On this page  
*   [Patching API objects directly](https://cdk8s.io/docs/latest/basics/escape-hatches/#patching-api-objects-directly)
*   [Patching API objects behind higher-level APIs](https://cdk8s.io/docs/latest/basics/escape-hatches/#patching-api-objects-behind-higher-level-apis)

Escape Hatches[¶](https://cdk8s.io/docs/latest/basics/escape-hatches/#escape-hatches "Permanent link")
======================================================================================================

An “escape hatch” is an intentional _leak_ in the abstraction layer. It allows users to “escape the abstraction” and reach out to a lower layer.

Similarly, in CDKs, escape hatches are mechanisms that allow users to tweak the synthesized output when the abstraction they use does not “hold water”.

You may need to use an escape hatch in the following cases:

1.   You are using an imported API object (e.g. `KubeDeployment`) and there is an issue with the schema or a bug in “import” which results in an invalid manifest or missing fields (as an example see [issue #140](https://github.com/cdk8s-team/cdk8s/issues/140)).
2.   You are using a high-level API (e.g. cdk8s+) which does not expose some functionality which exists in the lower-level resources.

Patching API objects directly[¶](https://cdk8s.io/docs/latest/basics/escape-hatches/#patching-api-objects-directly "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------

The [`ApiObject`](https://cdk8s.io/docs/latest/basics/api-object/) class, which is the base of all objects synthesized into a Kubernetes manifest offers an API for patching the synthesized output at the wire level using JSON Patch ([RFC-6902](http://tools.ietf.org/html/rfc6902)):

```
import { JsonPatch } from 'cdk8s';
apiObject.addJsonPatch(JsonPatch.replace('/foo', 'bar'));
apiObject.addJsonPatch(JsonPatch.add('/foo/bar/0', { bar: 123 }));
```

During synthesis, patches are applied in-order after the API object synthesized itself.

All classes generated using the CLI [import](https://cdk8s.io/docs/latest/cli/import/) command extend `ApiObject`, and therefore include the `addJsonPatch()` method.

Patching API objects behind higher-level APIs[¶](https://cdk8s.io/docs/latest/basics/escape-hatches/#patching-api-objects-behind-higher-level-apis "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

The second use case for using escape hatches is when you are working against a higher-level construct which, for some reason, does not allow you to achieve what you need.

For example, let’s say you are using the `Pod` class from cdk8s+ and you wish to set [`enableServiceLinks`] to `true`. This feature is currently not supported in the cdk8s+ `Pod` API, so you’ll want to patch the underlying `KubePod` and set this value.

To do that, you will need to “peak” into the construct tree and find the underlying API object, so you can apply the patch to it:

```
import { Pod } from 'cdk8s-plus-33';
import { ApiObject } from 'cdk8s';

const pod = new Pod(...);
const kubePod = ApiObject.of(pod);
kubePod.addJsonPatch(...);
```

The `ApiObject.of()` method uses capabilities of the [constructs programming model](https://cdk8s.io/docs/latest/basics/constructs/) to find the “default child” of a construct (`Node.of(c).defaultChild`). When a construct is initialized, it can either explicitly assign the value of `Node.of(this).defaultChild = xxx` or it can use the identity `Default` for one of its child constructs. This will automatically identify it as the default child.

Tip

The `ApiObject.of()` method recursively searches down the construct tree through child constructs called `Default` until it finds a child of type `ApiObject`. This means, for example, that `ApiObject.of(apiObject)` returns the same object.

There could be situations where a default child is not recorded by a high-level construct. This still does not mean you are blocked from patching the underlying API objects. You can still use `Node.of(x)` to traverse the construct tree to obtain the child. For example, you can use `Node.of(x).findChild(id)` to retrieve any child by its ID.

 © 2025, Amazon Web Services, Inc. or its affiliates. © cdk8s project authors. All rights reserved. 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

[](https://cdk.dev/ "Join the cdk8s Slack channel")[](https://github.com/cdk8s-team/cdk8s "cdk8s on GitHub")[](https://stackoverflow.com/questions/tagged/cdk8s "cdk8s on Stack Overflow")
