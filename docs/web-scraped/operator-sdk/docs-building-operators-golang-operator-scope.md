# Source: https://sdk.operatorframework.io/docs/building-operators/golang/operator-scope/

Title: Operators Scope

URL Source: https://sdk.operatorframework.io/docs/building-operators/golang/operator-scope/

Markdown Content:
Overview
--------

A namespace-scoped operator watches and manages resources in a single Namespace, whereas a cluster-scoped operator watches and manages resources cluster-wide.

An operator should be cluster-scoped if it watches resources that can be created in any Namespace. An operator should be namespace-scoped if it is intended to be flexibly deployed. This scope permits decoupled upgrades, namespace isolation for failures and monitoring, and differing API definitions.

By default, `operator-sdk init` scaffolds a cluster-scoped operator. This document details conversion of default operator projects to namespaced-scoped operators. Before proceeding, be aware that your operator may be better suited as cluster-scoped. For example, the [cert-manager](https://github.com/jetstack/cert-manager) operator is often deployed with cluster-scoped permissions and watches so that it can manage and issue certificates for an entire cluster.

**IMPORTANT**: When a [Manager](https://pkg.go.dev/sigs.k8s.io/controller-runtime/pkg/manager#Manager) instance is created in the `main.go` file, the Namespaces are set via [Cache Config](https://pkg.go.dev/sigs.k8s.io/controller-runtime/pkg/cache#Config) as described below. These Namespaces should be watched and cached for the Client which is provided by the Manager. Only clients provided by cluster-scoped Managers are able to manage cluster-scoped CRD’s. For further information see: [CRD scope doc](https://sdk.operatorframework.io/docs/building-operators/golang/crds-scope/).

Manager watching options
------------------------

### Watching resources in all Namespaces (default)

A [Manager](https://pkg.go.dev/sigs.k8s.io/controller-runtime/pkg/manager#Manager) is initialized with no Cache option specified, or with a Cache.DefaultNamespaces of `Namespace: ""` will watch all Namespaces:

```
...
mgr, err := ctrl.NewManager(ctrl.GetConfigOrDie(), ctrl.Options{
    Scheme:             scheme,
    MetricsBindAddress: metricsAddr,
    Port:               9443,
    LeaderElection:     enableLeaderElection,
    LeaderElectionID:   "f1c5ece8.example.com",
})
...
```

### Watching resources in specific Namespaces

To restrict the scope of the [Manager’s](https://pkg.go.dev/sigs.k8s.io/controller-runtime/pkg/manager#Manager) cache to a specific Namespace, set `Cache.DefaultNamespaces` field in [Options](https://pkg.go.dev/sigs.k8s.io/controller-runtime/pkg/manager#Options):

```
...
mgr, err := ctrl.NewManager(ctrl.GetConfigOrDie(), ctrl.Options{
    Scheme:             scheme,
    MetricsBindAddress: metricsAddr,
    Port:               9443,
    LeaderElection:     enableLeaderElection,
    LeaderElectionID:   "f1c5ece8.example.com",
    Cache: cache.Options{
      DefaultNamespaces: map[string]cache.Config{"operator-namespace": cache.Config{}},
    },
})
...
```

### Watching resources in a set of Namespaces

It is also possible to use `DefaultNamespaces` to watch and manage resources in a set of Namespaces:

```
...
mgr, err := ctrl.NewManager(ctrl.GetConfigOrDie(), ctrl.Options{
    Scheme:             scheme,
    MetricsBindAddress: metricsAddr,
    Port:               9443,
    LeaderElection:     enableLeaderElection,
    LeaderElectionID:   "f1c5ece8.example.com",
    Cache: cache.Options{
      DefaultNamespaces: map[string]cache.Config{
        "operator-namespace1": cache.Config{},
        "operator-namespace2": cache.Config{},
      },
    },
})
...
```

In the above example, a CR created in a Namespace not in the set passed to `Cache.DefaultNamespaces` will not be reconciled by its controller because the [Manager](https://pkg.go.dev/sigs.k8s.io/controller-runtime/pkg/manager#Manager) does not manage that Namespace. Further restrictions and qualifications can created on a per-namespace basis by setting fields in the cache.Config object, for further information see the [controller runtime docs](https://pkg.go.dev/sigs.k8s.io/controller-runtime/pkg/cache#Config)

**IMPORTANT:** Note that this is not intended to be used for excluding Namespaces, this is better done via a Predicate.

Restricting Roles and permissions
---------------------------------

An operator’s scope defines its [Manager’s](https://pkg.go.dev/sigs.k8s.io/controller-runtime/pkg/manager#Manager) cache’s scope but not the permissions to access the resources. After updating the Manager’s scope to be Namespaced, [Role-Based Access Control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) permissions applied to the operator’s service account should be restricted accordingly.

These permissions are found in the directory `config/rbac/`. The `ClusterRole` in `role.yaml` and `ClusterRoleBinding` in `role_binding.yaml` are used to grant the operator permissions to access and manage its resources.

**NOTE** For changing the operator’s scope only the `role.yaml` and `role_binding.yaml` manifests need to be updated. For the purposes of this doc, the other RBAC manifests `<kind>_editor_role.yaml`, `<kind>_viewer_role.yaml`, and `auth_proxy_*.yaml` are not relevant to changing the operator’s resource permissions.

### Changing the permissions to Namespaced

To change the scope of the RBAC permissions from cluster-wide to a specific namespace, you will need to:

*   Use `Role`s instead of `ClusterRole`s.

[`RBAC markers`](https://book.kubebuilder.io/reference/markers/rbac.html) defined in the controller (e.g `controllers/memcached_controller.go`) are used to generate the operator’s [RBAC ClusterRole](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole) (e.g `config/rbac/role.yaml`). The default markers don’t specify a `namespace` property and will result in a `ClusterRole`.

Update the [`RBAC markers`](https://book.kubebuilder.io/reference/markers/rbac.html) in `<kind>_controller.go` with `namespace=<namespace>` where the `Role` is to be applied, such as:

```
//+kubebuilder:rbac:groups=cache.example.com,namespace=memcached-operator-system,resources=memcacheds,verbs=get;list;watch;create;update;patch;delete
//+kubebuilder:rbac:groups=cache.example.com,namespace=memcached-operator-system,resources=memcacheds/status,verbs=get;update;patch
```

Then run `make manifests` to update `config/rbac/role.yaml`. In our example it would look like:

```
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  creationTimestamp: null
  name: manager-role
  namespace: memcached-operator-system
```

*   Use `RoleBinding`s instead of `ClusterRoleBinding`s. The `config/rbac/role_binding.yaml` needs to be manually updated:

```
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: manager-rolebinding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: manager-role
subjects:
- kind: ServiceAccount
  name: controller-manager
  namespace: system
```

Configuring watch namespaces dynamically
----------------------------------------

Instead of having any Namespaces hard-coded in the `main.go` file a good practice is to use an environment variable to allow the restrictive configurations. The one suggested here is `WATCH_NAMESPACE`, a comma-separated list of namespaces passed to the manager at deploy time.

### Configuring Namespace scoped operators

*   Add a helper function in the `main.go` file:

```
// getWatchNamespace returns the Namespace the operator should be watching for changes
func getWatchNamespace() (string, error) {
    // WatchNamespaceEnvVar is the constant for env variable WATCH_NAMESPACE
    // which specifies the Namespace to watch.
    // An empty value means the operator is running with cluster scope.
    var watchNamespaceEnvVar = "WATCH_NAMESPACE"

    ns, found := os.LookupEnv(watchNamespaceEnvVar)
    if !found {
        return "", fmt.Errorf("%s must be set", watchNamespaceEnvVar)
    }
    return ns, nil
}
```

*   Use the environment variable value:

```
...
watchNamespace, err := getWatchNamespace()
if err != nil {
    setupLog.Error(err, "unable to get WatchNamespace, " +
       "the manager will watch and manage resources in all namespaces")
}

mgr, err := ctrl.NewManager(ctrl.GetConfigOrDie(), ctrl.Options{
    Scheme:             scheme,
    MetricsBindAddress: metricsAddr,
    Port:               9443,
    LeaderElection:     enableLeaderElection,
    LeaderElectionID:   "f1c5ece8.example.com",
    Cache: cache.Options{
      DefaultNamespaces: map[string]cache.Config{watchNamespace: cache.Config{}},
    },
})
...
```

*   Define the environment variable in the `config/manager/manager.yaml`:

```
spec:
  containers:
  - command:
    - /manager
    args:
    - --leader-elect
    image: controller:latest
    name: manager
    resources:
      limits:
        cpu: 100m
        memory: 30Mi
      requests:
        cpu: 100m
        memory: 20Mi
    env:
      - name: WATCH_NAMESPACE
        valueFrom:
          fieldRef:
            fieldPath: metadata.namespace
  terminationGracePeriodSeconds: 10
```

**NOTE**`WATCH_NAMESPACE` here will always be set as the namespace where the operator is deployed.

### Configuring cluster-scoped operators with MultiNamespacedCacheBuilder

*   Add a helper function to get the environment variable value in the `main.go` file as done in the previous example (e.g `getWatchNamespace()`)
*   Use the environment variable value and check if it is a multi-namespace scenario:

```
...
watchNamespace, err := getWatchNamespace()
if err != nil {
    setupLog.Error(err, "unable to get WatchNamespace, " +
        "the manager will watch and manage resources in all Namespaces")
}

options := ctrl.Options{
    Scheme:             scheme,
    MetricsBindAddress: metricsAddr,
    Port:               9443,
    LeaderElection:     enableLeaderElection,
    LeaderElectionID:   "f1c5ece8.example.com",
    Cache: cache.Options{
      DefaultNamespaces: map[string]cache.Config{watchNamespace: cache.Config{}},
    },
}

// Add support for MultiNamespace set in WATCH_NAMESPACE (e.g ns1,ns2)
if strings.Contains(watchNamespace, ",") {
    setupLog.Info("manager set up with multiple namespaces", "namespaces", watchNamespace)
    // configure cluster-scoped with MultiNamespacedCacheBuilder
    options.Namespace = ""
    options.NewCache = cache.MultiNamespacedCacheBuilder(strings.Split(watchNamespace, ","))
}
...
```

*   Define the environment variable in the `config/manager/manager.yaml`:

```
...
    env:
      - name: WATCH_NAMESPACE
        value: "ns1,ns2"
  terminationGracePeriodSeconds: 10
...
```

Updating your CSV’s installModes
--------------------------------

If your operator is [integrated with OLM](https://sdk.operatorframework.io/docs/olm-integration), you will want to update your [CSV base’s](https://sdk.operatorframework.io/docs/olm-integration/generation/#kustomize-files)`spec.installModes` list to support the desired namespacing requirements. Support for multiple types of namespacing is allowed, so supporting multiple install modes in a CSV is permitted. After doing so, update your [bundle](https://sdk.operatorframework.io/docs/olm-integration/quickstart-bundle) or [package manifests](https://sdk.operatorframework.io/docs/olm-integration/tutorial-package-manifests) by following the linked guides.

### Watching resources in all Namespaces (default)

Only the `AllNamespaces` install mode is `supported: true` by default, so no changes are required.

### Watching resources in a single Namespace

If the operator can watch its own namespace, set the following in your `spec.installModes` list:

```
- type: OwnNamespace
    supported: true
```

If the operator can watch a single namespace that is not its own, set the following in your `spec.installModes` list:

```
- type: SingleNamespace
    supported: true
```

### Watching resources in multiple Namespaces

If the operator can watch multiple namespaces, set the following in your `spec.installModes` list:

```
- type: MultiNamespace
    supported: true
```
