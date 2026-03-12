# Source: https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/volume/

Title: Volume - cdk8s

URL Source: https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/volume/

Markdown Content:
Volume - cdk8s
===============
- [x] - [x] 

[Skip to content](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/volume/#volume)

[![Image 1: logo](https://cdk8s.io/docs/latest/assets/logo.png)](https://cdk8s.io/ "cdk8s")

 cdk8s 

 Volume 

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
        *   [PersistentVolumeClaim](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/pvc/)
        *   [Role Based Access Control](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/rbac/)
        *   [Secret](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/secret/)
        *   [ServiceAccount](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/service-account/)
        *   [Service](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/service/)
        *   - [x]  Volume  [Volume](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/volume/) On this page  
            *   [Create from a ConfigMap](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/volume/#create-from-a-configmap)
            *   [Create from an EmptyDir](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/volume/#create-from-an-emptydir)
            *   [Using PersistentVolumeClaim Templates with StatefulSets](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/volume/#using-persistentvolumeclaim-templates-with-statefulsets)

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
*   [Create from a ConfigMap](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/volume/#create-from-a-configmap)
*   [Create from an EmptyDir](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/volume/#create-from-an-emptydir)
*   [Using PersistentVolumeClaim Templates with StatefulSets](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/volume/#using-persistentvolumeclaim-templates-with-statefulsets)

Volume[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/volume/#volume "Permanent link")
==========================================================================================

Volume represents a named volume in a pod that may be accessed by any container in the pod.

[API Reference](https://cdk8s.io/docs/latest/reference/cdk8s-plus-31/typescript/#volume)

Create from a ConfigMap[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/volume/#create-from-a-configmap "Permanent link")
----------------------------------------------------------------------------------------------------------------------------

A very useful operation is to create a volume from a `ConfigMap`. Kubernetes will translate every key in the config map to a file, who’s content is the value of the key.

```
import * as kplus from 'cdk8s-plus-31';

const configMap = kplus.ConfigMap.fromConfigMapName('redis-config');
const configVolume = kplus.Volume.fromConfigMap(configMap);
```

Create from an EmptyDir[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/volume/#create-from-an-emptydir "Permanent link")
----------------------------------------------------------------------------------------------------------------------------

The easiest way to allocate some persistent storage to your container is to create a volume from an empty directory. This volume, as the name suggests, is initially empty, and can be written to by containers who mount it. The data in the volume is preserved throughout the lifecycle of the pod, but is deleted forever as soon as the pod itself is removed.

```
import * as kplus from 'cdk8s-plus-31';

const data = kplus.Volume.fromEmptyDir(configMap);

const pod = new kplus.Pod(this, 'Pod');
const redis = pod.addContainer({
  image: 'redis'
})

// mount to the redis container.
redis.mount('/var/lib/redis', data);
```

Using PersistentVolumeClaim Templates with StatefulSets[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/volume/#using-persistentvolumeclaim-templates-with-statefulsets "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When working with StatefulSets, you can use PersistentVolumeClaim templates to create stable storage for each pod in the StatefulSet. This allows each pod to have its own storage that persists even if the pod is rescheduled to a different node.

```
import * as kplus from 'cdk8s-plus-32';
import { Size } from 'cdk8s';

const dataVolume = Volume.fromName(chart, "pvc-template-data", "data-volume")

// Create a StatefulSet with a PVC template
const statefulSet = new kplus.StatefulSet(this, 'StatefulSet', {
  containers: [{
    image: 'nginx',
    volumeMounts: [{
      volume: dataVolume,
      path: '/data',
    }, {
      volume: Volume.fromName(chart, "pvc-template-temp", "temp-volume"),
      path: '/data',
    }],
  }],
  // Define PVC templates during initialization
  volumeClaimTemplates: [{
    name: dataVolume.name,
    storage: Size.gibibytes(10),
    accessModes: [kplus.PersistentVolumeAccessMode.READ_WRITE_ONCE],
    storageClassName: 'standard',  // Optional: Specify the storage class
  }, {
    name: 'temp-volume',  // Must match a volume mount name in a container
    storage: Size.gibibytes(10),
    accessModes: [kplus.PersistentVolumeAccessMode.READ_WRITE_ONCE],
    storageClassName: 'standard',  // Optional: Specify the storage class
  }],
});

// Or add PVC templates after creation
statefulSet.addVolumeClaimTemplate({
  name: 'logs-volume',
  storage: Size.gibibytes(5),
  accessModes: [kplus.PersistentVolumeAccessMode.READ_WRITE_ONCE],
});
```

Each pod in the StatefulSet will get its own PVC instance based on these templates, with names like `data-volume-my-statefulset-0`, `data-volume-my-statefulset-1`, etc.

 © 2025, Amazon Web Services, Inc. or its affiliates. © cdk8s project authors. All rights reserved. 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

[](https://cdk.dev/ "Join the cdk8s Slack channel")[](https://github.com/cdk8s-team/cdk8s "cdk8s on GitHub")[](https://stackoverflow.com/questions/tagged/cdk8s "cdk8s on Stack Overflow")
