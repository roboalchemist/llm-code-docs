# Source: https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/

Title: Role Based Access Control - cdk8s

URL Source: https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/

Markdown Content:
Role Based Access Control - cdk8s
===============
- [x] - [x] 

[Skip to content](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#role-based-access-control)

[![Image 1: logo](https://cdk8s.io/docs/latest/assets/logo.png)](https://cdk8s.io/ "cdk8s")

 cdk8s 

 Role Based Access Control 

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
        *   - [x]  Role Based Access Control  [Role Based Access Control](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/) On this page  
            *   [Role](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#role)
                *   [Create role and add rules to it](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#create-role-and-add-rules-to-it)

            *   [ClusterRole](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#clusterrole)
                *   [Create ClusterRole and add rules to it](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#create-clusterrole-and-add-rules-to-it)

            *   [Resource Permission Methods](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#resource-permission-methods)
                *   [grantReadWrite Method](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#grantreadwrite-method)

            *   [Add subjects to an already bound role](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#add-subjects-to-an-already-bound-role)

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
*   [Role](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#role)
    *   [Create role and add rules to it](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#create-role-and-add-rules-to-it)

*   [ClusterRole](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#clusterrole)
    *   [Create ClusterRole and add rules to it](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#create-clusterrole-and-add-rules-to-it)

*   [Resource Permission Methods](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#resource-permission-methods)
    *   [grantReadWrite Method](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#grantreadwrite-method)

*   [Add subjects to an already bound role](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#add-subjects-to-an-already-bound-role)

Role Based Access Control[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#role-based-access-control "Permanent link")
==============================================================================================================================

Role Based Access Control(RBAC) helps you restrict actions that can be performed on specific Kubernetes resources. To make this possible, RBAC lets you create roles with rules which define access permissions for your specified resource.

These roles can then be binded to Kubernetes subjects, which could be User, Group or ServiceAccount.

Note

Rules or permissions are purely additive and there are no deny rules.

Now, there are two types of roles available, * Role: These set permissions within a particular namespace i.e. is for namespaced resources, like, pods, deployments. * ClusterRole: These set permissions for non-namespaced resources, like, nodes, urls.

and, similarly there are two types of binding available, * RoleBinding: These grant permissions within a specific namespace. * ClusterRoleBinding: These grant cluster wide permissions .

Learn more

*   [Role API Reference](https://cdk8s.io/docs/latest/reference/cdk8s-plus-32/typescript/#role)
*   [RoleBinding API Reference](https://cdk8s.io/docs/latest/reference/cdk8s-plus-32/typescript/#role-binding)

Role[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#role "Permanent link")
------------------------------------------------------------------------------------

### Create role and add rules to it[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#create-role-and-add-rules-to-it "Permanent link")

```
import * as kplus from 'cdk8s-plus-32';
import { Construct } from 'constructs';
import { App, Chart, ChartProps } from 'cdk8s';

export class MyChart extends Chart {
  constructor(scope: Construct, id: string, props: ChartProps = { }) {
    super(scope, id, props);

    // Creating RBAC Role
    const role = new kplus.Role(this, 'SampleRole');

    // The convenience method here `allowReadWrite` would add
    // `get, list, watch, create, update, patch, delete,
    // deletecollection` rules to the role for deployment resources.
    role.allowReadWrite(kplus.ApiResource.DEPLOYMENTS);

    const user = kplus.User.fromName(this, 'SampleUser', 'Jane');
    const group = kplus.Group.fromName(this, 'SampleGroup', 'sample-group');
    const serviceAccount = new kplus.ServiceAccount(this, 'SampleServiceAccount');

    // You can bind this role to a specific user, group or service account
    role.bind(user, group, serviceAccount);
  }
}

const app = new App();
new MyChart(app, 'rbac-docs');
app.synth();
```

ClusterRole[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#clusterrole "Permanent link")
--------------------------------------------------------------------------------------------------

### Create ClusterRole and add rules to it[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#create-clusterrole-and-add-rules-to-it "Permanent link")

```
// Creating RBAC ClusterRole
const clusterRole = new kplus.ClusterRole(this, 'SampleClusterRole');

// Adding list of rules to the ClusterRole for 'Nodes' and 'URL' non-namespaced resource
clusterRole.allowReadWrite(kplus.ApiResource.NODES, kplus.NonApiResource.of('/healthz'));

const user = kplus.User.fromName(this, 'SampleUser', 'Jane');
const group = kplus.Group.fromName(this, 'SampleGroup', 'sample-group');
const serviceAccount = new kplus.ServiceAccount(this, 'SampleServiceAccount');

// You can bind this cluster role to a specific user, group or service account
clusterRole.bind(user, group, serviceAccount);
```

Resource Permission Methods[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#resource-permission-methods "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------

You can use convenience methods like `grantRead` and `grantReadWrite` which would make it easier to grant list of subjects set of permissions for the resource.

### `grantReadWrite` Method[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#grantreadwrite-method "Permanent link")

```
// Creating a Pod resource
const pod = new kplus.Pod(this, 'Pod', {
    containers: [{ image: 'image' }],
});

const user = kplus.User.fromName(this, 'SampleUser', 'Jane');
const group = kplus.Group.fromName(this, 'SampleGroup', 'sample-group');
const serviceAccount = new kplus.ServiceAccount(this, 'SampleServiceAccount');

// You can grant permissions to specific user, group or service account.
pod.permissions.grantReadWrite(user, group, serviceAccount);
```

Add subjects to an already bound role[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-32/rbac/#add-subjects-to-an-already-bound-role "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------

```
const user = kplus.User.fromName(this, 'SampleUser', 'Jane');
const binding = role.bind(user);

const anotherUser = kplus.User.fromName(this, 'AnotherSampleUser', 'James');
binding.addSubjects(anotherUser);
```

 © 2025, Amazon Web Services, Inc. or its affiliates. © cdk8s project authors. All rights reserved. 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

[](https://cdk.dev/ "Join the cdk8s Slack channel")[](https://github.com/cdk8s-team/cdk8s "cdk8s on GitHub")[](https://stackoverflow.com/questions/tagged/cdk8s "cdk8s on Stack Overflow")
