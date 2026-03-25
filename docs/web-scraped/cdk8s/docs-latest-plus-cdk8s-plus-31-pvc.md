# Source: https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/pvc/

Title: PersistentVolumeClaim - cdk8s

URL Source: https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/pvc/

Markdown Content:
PersistentVolumeClaim - cdk8s
===============
- [x] - [x] 

[Skip to content](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/pvc/#persistentvolumeclaim)

[![Image 1: logo](https://cdk8s.io/docs/latest/assets/logo.png)](https://cdk8s.io/ "cdk8s")

 cdk8s 

 PersistentVolumeClaim 

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
    *   [Escape Hatches](https://cdk8s.io/docs/latest/basics/escape-hatches/)
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
        *   - [x]  PersistentVolumeClaim  [PersistentVolumeClaim](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/pvc/) On this page  
            *   [Storage Class](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/pvc/#storage-class)
            *   [Bind](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/pvc/#bind)

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
*   [Storage Class](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/pvc/#storage-class)
*   [Bind](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/pvc/#bind)

PersistentVolumeClaim[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/pvc/#persistentvolumeclaim "Permanent link")
=====================================================================================================================

A `PersistentVolumeClaim` (PVC) is a request for storage by a pod.

[API Reference](https://cdk8s.io/docs/latest/reference/cdk8s-plus-31/typescript/#persistent-volume-claim)

A `PersistentVolumeClaim` contains the requirements of the request, and the Kubernetes control plane is responsible providing a physical volume that satisfies the claim’s requirements.

```
import * as kplus from 'cdk8s-plus-31';
import * as cdk8s from 'cdk8s';

const pod = new kplus.Pod(chart, 'Pod');
const container = pod.addContainer({ image: 'node' });

// create the storage request
const claim = new kplus.PersistentVolumeClaim(chart, 'Claim', {
  storage: cdk8s.Size.gibibytes(50),
});

// mount a volume based on the request to the container
// this will also add the volume itself to the pod spec.
container.mount('/data', kplus.Volume.fromPersistentVolumeClaim(claim));
```

Storage Class[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/pvc/#storage-class "Permanent link")
-----------------------------------------------------------------------------------------------------

By default, the `storageClassName` property of a claim is not set. This means that the backing volume can be provided by one of two methods:

1.   Dynamically provision a volume with the default storage class.
2.   If a default storage class is not configured in the cluster, the backing volume must pre-exist and not be assigned to any storage class.

> See [Provisioning](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#provisioning) for more details.

You can also provide an explicit storage class name,

```
const claim = new kplus.PersistentVolumeClaim(chart, 'Claim', {
  storage: cdk8s.Size.gibibytes(50),
  storageClassName: 'large-ebs',
});
```

In this case, Kubernetes control plane will either locate an existing volume with the `larg-ebs` storage class, or dynamically provision a new using the appropriate provisioner.

You can also pass in a special `""` value, this means the volume must not be assigned to any storage class. Since all dynamically provisioend volumes belong to a storage class, setting this value effectively disables dynamic provisioning for this claim.

```
const claim = new kplus.PersistentVolumeClaim(chart, 'Claim', {
  storage: cdk8s.Size.gibibytes(50),
  // disable dynamic provisioning
  storageClassName: "",
});
```

Bind[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/pvc/#bind "Permanent link")
-----------------------------------------------------------------------------------

Binding is a part of the reservation process, but it only creates a one directional link. You can use it to bind a PVC to an existing PV. Note however that if the PV is not bound to the PVC, there’s no guarantee this claim will indeed be given to that specific volume.

```
const claim = new kplus.PersistentVolumeClaim(chart, 'Claim', {
  storage: cdk8s.Size.gibibytes(50),
});

const vol = kplus.PersistentVolume.fromPersistentVolumeName('vol');

// will modify the claim resource to refer to the volume.
// but no the other way around.
claim.bind(vol);
```

 © 2025, Amazon Web Services, Inc. or its affiliates. © cdk8s project authors. All rights reserved. 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

[](https://cdk.dev/ "Join the cdk8s Slack channel")[](https://github.com/cdk8s-team/cdk8s "cdk8s on GitHub")[](https://stackoverflow.com/questions/tagged/cdk8s "cdk8s on Stack Overflow")
