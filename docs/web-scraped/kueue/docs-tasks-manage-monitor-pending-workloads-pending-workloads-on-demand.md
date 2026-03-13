# Source: https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/pending_workloads_on_demand/

Title: Pending Workloads on-demand

URL Source: https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/pending_workloads_on_demand/

Published Time: 2024-09-30T00:00:00+00:00

Markdown Content:
Monitor pending Workloads with the on-demand visibility API

This page shows you how to monitor pending workloads with `VisibilityOnDemand` feature.

The intended audience for this page are [batch administrators](https://kueue.sigs.k8s.io/docs/tasks/#batch-administrator) for [Cluster Queue visibility section](https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/pending_workloads_on_demand/#cluster-queue-visibility-via-kubectl), and [batch users](https://kueue.sigs.k8s.io/docs/tasks/#batch-user) for [Local Queue Visibility section](https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/pending_workloads_on_demand/#local-queue-visibility-via-kubectl).

From version v0.6.0, Kueue provides the ability for a batch administrators to monitor the pipeline of pending jobs, and help users to estimate when their jobs will start.

Before you begin [](https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/pending_workloads_on_demand/#before-you-begin)
----------------------------------------------------------------------------------------------------------------------------------------

Make sure the following conditions are met:

*   A Kubernetes cluster is running.
*   The kubectl command-line tool has communication with your cluster.
*   [Kueue is installed](https://kueue.sigs.k8s.io/docs/installation/) in version v0.6.0 or later.

### Configure API Priority and Fairness: [](https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/pending_workloads_on_demand/#configure-api-priority-and-fairness)

To install the [API Priority and Fairness](https://kubernetes.io/docs/concepts/cluster-administration/flow-control/) configuration for the visibility API apply manifests:

```
kubectl apply --server-side -f https://github.com/kubernetes-sigs/kueue/releases/download/v0.16.2/visibility-apf.yaml
```

### Directly accessing the Visibility API [](https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/pending_workloads_on_demand/#directly-accessing-the-visibility-api)

If you want to directly access the Visibility API with a http client like `curl` or `wget`, or a browser, there are multiple ways you can locate and authenticate against the Visibility API server:

#### (Recommended) Using kubectl proxy [](https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/pending_workloads_on_demand/#recommended-using-kubectl-proxy)

Run kubectl in proxy mode. This method is recommended, since it uses the stored API server location and verifies the identity of the API server using a self-signed certificate. No man-in-the-middle (MITM) attack is possible using this method.

For more details, see [kubectl documentation](https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api/#using-kubectl-proxy).

#### Without kubectl proxy [](https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/pending_workloads_on_demand/#without-kubectl-proxy)

Alternatively, you can provide the location and credentials directly to the http client. This works with client code that is confused by proxies. To protect against man in the middle attacks, you’ll need to import a root cert into your browser.

For more details, see [kubectl documentation](https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api/#without-kubectl-proxy).

You then need to create `ClusterRole` and `ClusterRoleBinding` for that same (default) k8s service account

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: kueue-visibility-server-api
rules:
- apiGroups:
  - "visibility.kueue.x-k8s.io"
  resources:
  - "clusterqueues/pendingworkloads"
  - "localqueues/pendingworkloads"
  verbs:
  - get
  - list
  - watch
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: kueue-visibility-server-api
  namespace: default
subjects:
- kind: ServiceAccount
  name: default
  namespace: default
roleRef:
  kind: ClusterRole
  name: kueue-visibility-server-api
  apiGroup: rbac.authorization.k8s.io
```

using a command:

```
kubectl apply -f https://kueue.sigs.k8s.io/examples/visibility/cluster-role-and-binding.yaml
```

Monitor pending workloads on demand [](https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/pending_workloads_on_demand/#monitor-pending-workloads-on-demand)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Feature state beta since Kueue v0.9

To install a simple setup of ClusterQueue

```
apiVersion: kueue.x-k8s.io/v1beta2
kind: ResourceFlavor
metadata:
  name: "default-flavor"
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: ClusterQueue
metadata:
  name: "cluster-queue"
spec:
  namespaceSelector: {} # match all.
  resourceGroups:
  - coveredResources: ["cpu", "memory"]
    flavors:
    - name: "default-flavor"
      resources:
      - name: "cpu"
        nominalQuota: 9
      - name: "memory"
        nominalQuota: 36Gi
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: LocalQueue
metadata:
  namespace: "default"
  name: "user-queue"
spec:
  clusterQueue: "cluster-queue"
```

run the following command:

```
kubectl apply -f https://kueue.sigs.k8s.io/examples/admin/single-clusterqueue-setup.yaml
```

Now, let’s create 6 jobs

```
apiVersion: batch/v1
kind: Job
metadata:
  generateName: sample-job-
  namespace: default
  labels:
    kueue.x-k8s.io/queue-name: user-queue
spec:
  parallelism: 3
  completions: 3
  template:
    spec:
      containers:
      - name: dummy-job
        image: registry.k8s.io/e2e-test-images/agnhost:2.53
        command: [ "/bin/sh" ]
        args: [ "-c", "sleep 60" ]
        resources:
          requests:
            cpu: "1"
            memory: "200Mi"
      restartPolicy: Never
```

using a command:

```
for i in {1..6}; do kubectl create -f https://kueue.sigs.k8s.io/examples/jobs/sample-job.yaml; done
```

3 of them saturate the ClusterQueue and the other 3 should be pending.

### Cluster Queue visibility via kubectl [](https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/pending_workloads_on_demand/#cluster-queue-visibility-via-kubectl)

To view pending workloads in ClusterQueue `cluster-queue` run the following command:

```
kubectl get --raw "/apis/visibility.kueue.x-k8s.io/v1beta2/clusterqueues/cluster-queue/pendingworkloads"
```

You should get results similar to:

```
{
  "kind": "PendingWorkloadsSummary",
  "apiVersion": "visibility.kueue.x-k8s.io/v1beta2",
  "metadata": {
    "creationTimestamp": null
  },
  "items": [
    {
      "metadata": {
        "name": "job-sample-job-jrjfr-8d56e",
        "namespace": "default",
        "creationTimestamp": "2023-12-05T15:42:03Z",
        "ownerReferences": [
          {
            "apiVersion": "batch/v1",
            "kind": "Job",
            "name": "sample-job-jrjfr",
            "uid": "5863cf0e-b0e7-43bf-a445-f41fa1abedfa"
          }
        ]
      },
      "priority": 0,
      "localQueueName": "user-queue",
      "positionInClusterQueue": 0,
      "positionInLocalQueue": 0
    },
    {
      "metadata": {
        "name": "job-sample-job-jg9dw-5f1a3",
        "namespace": "default",
        "creationTimestamp": "2023-12-05T15:42:03Z",
        "ownerReferences": [
          {
            "apiVersion": "batch/v1",
            "kind": "Job",
            "name": "sample-job-jg9dw",
            "uid": "fd5d1796-f61d-402f-a4c8-cbda646e2676"
          }
        ]
      },
      "priority": 0,
      "localQueueName": "user-queue",
      "positionInClusterQueue": 1,
      "positionInLocalQueue": 1
    },
    {
      "metadata": {
        "name": "job-sample-job-t9b8m-4e770",
        "namespace": "default",
        "creationTimestamp": "2023-12-05T15:42:03Z",
        "ownerReferences": [
          {
            "apiVersion": "batch/v1",
            "kind": "Job",
            "name": "sample-job-t9b8m",
            "uid": "64c26c73-6334-4d13-a1a8-38d99196baa5"
          }
        ]
      },
      "priority": 0,
      "localQueueName": "user-queue",
      "positionInClusterQueue": 2,
      "positionInLocalQueue": 2
    }
  ]
}
```

You can pass optional query parameters:

*   limit `<integer>` - 1000 on default. It indicates max number of pending workloads that should be fetched.
*   offset `<integer>` - 0 by default. It indicates position of the first pending workload that should be fetched, starting from 0.

To view only 1 pending workloads use, starting from position 1 in ClusterQueue run:

```
kubectl get --raw "/apis/visibility.kueue.x-k8s.io/v1beta2/clusterqueues/cluster-queue/pendingworkloads?limit=1&offset=1"
```

You should get results similar to

```
{
  "kind": "PendingWorkloadsSummary",
  "apiVersion": "visibility.kueue.x-k8s.io/v1beta2",
  "metadata": {
    "creationTimestamp": null
  },
  "items": [
    {
      "metadata": {
        "name": "job-sample-job-jg9dw-5f1a3",
        "namespace": "default",
        "creationTimestamp": "2023-12-05T15:42:03Z",
        "ownerReferences": [
          {
            "apiVersion": "batch/v1",
            "kind": "Job",
            "name": "sample-job-jg9dw",
            "uid": "fd5d1796-f61d-402f-a4c8-cbda646e2676"
          }
        ]
      },
      "priority": 0,
      "localQueueName": "user-queue",
      "positionInClusterQueue": 1,
      "positionInLocalQueue": 1
    }
  ]
}
```

### Cluster Queue visibility via curl [](https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/pending_workloads_on_demand/#cluster-queue-visibility-via-curl)

If you followed steps described in [Directly accessing the Visibility API](https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/pending_workloads_on_demand/#directly-accessing-the-visibility-api) above, you can use curl to view pending workloads in ClusterQueue using following commands:

`curl http://localhost:8080/apis/visibility.kueue.x-k8s.io/v1beta2/clusterqueues/cluster-queue/pendingworkloads`

`curl -X GET $APISERVER/apis/visibility.kueue.x-k8s.io/v1beta2/clusterqueues/cluster-queue/pendingworkloads --header "Authorization: Bearer $TOKEN" --insecure`

You should get results similar to:

```
{
  "kind": "PendingWorkloadsSummary",
  "apiVersion": "visibility.kueue.x-k8s.io/v1beta2",
  "metadata": {
    "creationTimestamp": null
  },
  "items": [
    {
      "metadata": {
        "name": "job-sample-job-z8sc5-223e8",
        "namespace": "default",
        "creationTimestamp": "2024-09-29T10:58:32Z",
        "ownerReferences": [
          {
            "apiVersion": "batch/v1",
            "kind": "Job",
            "name": "sample-job-z8sc5",
            "uid": "7086b1bb-39b7-42e5-9f6b-ee07d0100051"
          }
        ]
      },
      "priority": 0,
      "localQueueName": "user-queue",
      "positionInClusterQueue": 0,
      "positionInLocalQueue": 0
    },
    {
      "metadata": {
        "name": "job-sample-job-2mfzb-28f54",
        "namespace": "default",
        "creationTimestamp": "2024-09-29T10:58:32Z",
        "ownerReferences": [
          {
            "apiVersion": "batch/v1",
            "kind": "Job",
            "name": "sample-job-2mfzb",
            "uid": "51ae8e48-8785-4bbb-9811-f9c1f041b368"
          }
        ]
      },
      "priority": 0,
      "localQueueName": "user-queue",
      "positionInClusterQueue": 1,
      "positionInLocalQueue": 1
    },
    {
      "metadata": {
        "name": "job-sample-job-dpggt-3ecac",
        "namespace": "default",
        "creationTimestamp": "2024-09-29T10:58:32Z",
        "ownerReferences": [
          {
            "apiVersion": "batch/v1",
            "kind": "Job",
            "name": "sample-job-dpggt",
            "uid": "870655da-07d5-4910-be99-7650bf89b0d2"
          }
        ]
      },
      "priority": 0,
      "localQueueName": "user-queue",
      "positionInClusterQueue": 2,
      "positionInLocalQueue": 2
    }
  ]
}
```

### Local Queue visibility via kubectl [](https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/pending_workloads_on_demand/#local-queue-visibility-via-kubectl)

Similarly to ClusterQueue, to view pending workloads in LocalQueue `user-queue` run the following command:

```
kubectl get --raw /apis/visibility.kueue.x-k8s.io/v1beta2/namespaces/default/localqueues/user-queue/pendingworkloads
```

You should get results similar to:

```
{
  "kind": "PendingWorkloadsSummary",
  "apiVersion": "visibility.kueue.x-k8s.io/v1beta2",
  "metadata": {
    "creationTimestamp": null
  },
  "items": [
    {
      "metadata": {
        "name": "job-sample-job-jrjfr-8d56e",
        "namespace": "default",
        "creationTimestamp": "2023-12-05T15:42:03Z",
        "ownerReferences": [
          {
            "apiVersion": "batch/v1",
            "kind": "Job",
            "name": "sample-job-jrjfr",
            "uid": "5863cf0e-b0e7-43bf-a445-f41fa1abedfa"
          }
        ]
      },
      "priority": 0,
      "localQueueName": "user-queue",
      "positionInClusterQueue": 0,
      "positionInLocalQueue": 0
    },
    {
      "metadata": {
        "name": "job-sample-job-jg9dw-5f1a3",
        "namespace": "default",
        "creationTimestamp": "2023-12-05T15:42:03Z",
        "ownerReferences": [
          {
            "apiVersion": "batch/v1",
            "kind": "Job",
            "name": "sample-job-jg9dw",
            "uid": "fd5d1796-f61d-402f-a4c8-cbda646e2676"
          }
        ]
      },
      "priority": 0,
      "localQueueName": "user-queue",
      "positionInClusterQueue": 1,
      "positionInLocalQueue": 1
    },
    {
      "metadata": {
        "name": "job-sample-job-t9b8m-4e770",
        "namespace": "default",
        "creationTimestamp": "2023-12-05T15:42:03Z",
        "ownerReferences": [
          {
            "apiVersion": "batch/v1",
            "kind": "Job",
            "name": "sample-job-t9b8m",
            "uid": "64c26c73-6334-4d13-a1a8-38d99196baa5"
          }
        ]
      },
      "priority": 0,
      "localQueueName": "user-queue",
      "positionInClusterQueue": 2,
      "positionInLocalQueue": 2
    }
  ]
}
```

You can pass optional query parameters:

*   limit `<integer>` - 1000 on default. It indicates max number of pending workloads that should be fetched.
*   offset `<integer>` - 0 by default. It indicates position of the first pending workload that should be fetched, starting from 0.

To view only 1 pending workloads use, starting from position 1 in LocalQueue run:

```
kubectl get --raw "/apis/visibility.kueue.x-k8s.io/v1beta2/namespaces/default/localqueues/user-queue/pendingworkloads?limit=1&offset=1"
```

You should get results similar to

```
{
  "kind": "PendingWorkloadsSummary",
  "apiVersion": "visibility.kueue.x-k8s.io/v1beta2",
  "metadata": {
    "creationTimestamp": null
  },
  "items": [
    {
      "metadata": {
        "name": "job-sample-job-jg9dw-5f1a3",
        "namespace": "default",
        "creationTimestamp": "2023-12-05T15:42:03Z",
        "ownerReferences": [
          {
            "apiVersion": "batch/v1",
            "kind": "Job",
            "name": "sample-job-jg9dw",
            "uid": "fd5d1796-f61d-402f-a4c8-cbda646e2676"
          }
        ]
      },
      "priority": 0,
      "localQueueName": "user-queue",
      "positionInClusterQueue": 1,
      "positionInLocalQueue": 1
    }
  ]
}
```

### Local Queue visibility via curl [](https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/pending_workloads_on_demand/#local-queue-visibility-via-curl)

If you followed steps described in [Directly accessing the Visibility API](https://kueue.sigs.k8s.io/docs/tasks/manage/monitor_pending_workloads/pending_workloads_on_demand/#directly-accessing-the-visibility-api) above, you can use curl to view pending workloads in LocalQueue using following commands:

`curl http://localhost:8080/apis/visibility.kueue.x-k8s.io/v1beta2/namespaces/default/localqueues/user-queue/pendingworkloads`

`curl -X GET $APISERVER/apis/visibility.kueue.x-k8s.io/v1beta2/namespaces/default/localqueues/user-queue/pendingworkloads --header "Authorization: Bearer $TOKEN" --insecure`

You should get results similar to:

```
{
  "kind": "PendingWorkloadsSummary",
  "apiVersion": "visibility.kueue.x-k8s.io/v1beta2",
  "metadata": {
    "creationTimestamp": null
  },
  "items": [
    {
      "metadata": {
        "name": "job-sample-job-z8sc5-223e8",
        "namespace": "default",
        "creationTimestamp": "2024-09-29T10:58:32Z",
        "ownerReferences": [
          {
            "apiVersion": "batch/v1",
            "kind": "Job",
            "name": "sample-job-z8sc5",
            "uid": "7086b1bb-39b7-42e5-9f6b-ee07d0100051"
          }
        ]
      },
      "priority": 0,
      "localQueueName": "user-queue",
      "positionInClusterQueue": 0,
      "positionInLocalQueue": 0
    },
    {
      "metadata": {
        "name": "job-sample-job-2mfzb-28f54",
        "namespace": "default",
        "creationTimestamp": "2024-09-29T10:58:32Z",
        "ownerReferences": [
          {
            "apiVersion": "batch/v1",
            "kind": "Job",
            "name": "sample-job-2mfzb",
            "uid": "51ae8e48-8785-4bbb-9811-f9c1f041b368"
          }
        ]
      },
      "priority": 0,
      "localQueueName": "user-queue",
      "positionInClusterQueue": 1,
      "positionInLocalQueue": 1
    },
    {
      "metadata": {
        "name": "job-sample-job-dpggt-3ecac",
        "namespace": "default",
        "creationTimestamp": "2024-09-29T10:58:32Z",
        "ownerReferences": [
          {
            "apiVersion": "batch/v1",
            "kind": "Job",
            "name": "sample-job-dpggt",
            "uid": "870655da-07d5-4910-be99-7650bf89b0d2"
          }
        ]
      },
      "priority": 0,
      "localQueueName": "user-queue",
      "positionInClusterQueue": 2,
      "positionInLocalQueue": 2
    }
  ]
}
```
