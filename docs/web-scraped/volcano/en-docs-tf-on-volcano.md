# Source: https://volcano.sh/en/docs/tf_on_volcano/

Title: TensorFlow on Volcano | Volcano

URL Source: https://volcano.sh/en/docs/tf_on_volcano/

Published Time: 2021-04-07T00:00:00+00:00

Markdown Content:
Last updated on Mar 14, 2025

### TensorFlow introduction[](https://volcano.sh/en/docs/tf_on_volcano/#tensorflow-introduction)

TensorFlow is a symbolic mathematical system based on data flow programming, which is widely used in programming and realization of various machine learning algorithms. Its predecessor is DistBelief, a neural network algorithm library of Google.

### TensorFlow on Volcano[](https://volcano.sh/en/docs/tf_on_volcano/#tensorflow-on-volcano)

PS-worker model: Parameter Server performs model-related services, Work Server trains related services, inference calculation, gradient calculation, etc[1].

![Image 1: image](https://volcano.sh/img/ps-worker.png)

#### ps-worker[](https://volcano.sh/en/docs/tf_on_volcano/#ps-worker)

TensorFlow on Kubernetes has many problems:

*   Resource isolation.
*   Lack of GPU scheduling, Gang Schuler.
*   Process Legacy.
*   Training log is not convenient to save.

Create `tftest.yaml`.

```
apiVersion: batch.volcano.sh/v1alpha1
kind: Job
metadata:
  name: tensorflow-dist-mnist
spec:
  minAvailable: 3
  schedulerName: volcano
  plugins:
    env: []
    svc: []
  policies:
    - event: PodEvicted
      action: RestartJob
  queue: default
  tasks:
    - replicas: 1
      name: ps
      template:
        spec:
          containers:
            - command:
                - sh
                - -c
                - |
                  PS_HOST=`cat /etc/volcano/ps.host | sed 's/$/&:2222/g' | sed 's/^/"/;s/$/"/' | tr "\n" ","`;
                  WORKER_HOST=`cat /etc/volcano/worker.host | sed 's/$/&:2222/g' | sed 's/^/"/;s/$/"/' | tr "\n" ","`;
                  export TF_CONFIG={\"cluster\":{\"ps\":[${PS_HOST}],\"worker\":[${WORKER_HOST}]},\"task\":{\"type\":\"ps\",\"index\":${VK_TASK_INDEX}},\"environment\":\"cloud\"};
                  python /var/tf_dist_mnist/dist_mnist.py
              image: volcanosh/dist-mnist-tf-example:0.0.1
              name: tensorflow
              ports:
                - containerPort: 2222
                  name: tfjob-port
              resources: {}
          restartPolicy: Never
    - replicas: 2
      name: worker
      policies:
        - event: TaskCompleted
          action: CompleteJob
      template:
        spec:
          containers:
            - command:
                - sh
                - -c
                - |
                  PS_HOST=`cat /etc/volcano/ps.host | sed 's/$/&:2222/g' | sed 's/^/"/;s/$/"/' | tr "\n" ","`;
                  WORKER_HOST=`cat /etc/volcano/worker.host | sed 's/$/&:2222/g' | sed 's/^/"/;s/$/"/' | tr "\n" ","`;
                  export TF_CONFIG={\"cluster\":{\"ps\":[${PS_HOST}],\"worker\":[${WORKER_HOST}]},\"task\":{\"type\":\"worker\",\"index\":${VK_TASK_INDEX}},\"environment\":\"cloud\"};
                  python /var/tf_dist_mnist/dist_mnist.py
              image: volcanosh/dist-mnist-tf-example:0.0.1
              name: tensorflow
              ports:
                - containerPort: 2222
                  name: tfjob-port
              resources: {}
          restartPolicy: Never
```

Deploy `tftest.yaml`.

```
kubectl apply -f tftest.yaml
```

View job health.

```
kubectl get pod
```
