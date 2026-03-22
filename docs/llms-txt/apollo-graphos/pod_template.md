# Source: https://www.apollographql.com/docs/apollo-operator/resources/supergraph/pod_template.md

# Supergraph podTemplate

The `.spec.podTemplate` section of your **Supergraph** resource allows you to customize the underlying **Pod**s and containers.

## Properties

### `routerContainer`

Override values in the main **router** container. This replicates the Kubernetes **Container** specification but doesn't allow setting `name`, `image`, `command`, `args`, or `workingDir`.

```yaml
spec:
  podTemplate:
    routerContainer:
      additionalEnv:
        - name: APOLLO_ROUTER_LOG
          value: debug
      additionalVolumeMounts:
        - name: config-vol
          mountPath: /etc/config
```

#### `additionalEnv`

List of additional environment variables to set in the router container.

```yaml
spec:
  podTemplate:
    routerContainer:
      additionalEnv:
        - name: APOLLO_ROUTER_LOG
          value: debug
```

#### `additionalEnvFrom`

List of additional sources to populate environment variables in the router container.

```yaml
spec:
  podTemplate:
    routerContainer:
      additionalEnvFrom:
        - configMapRef:
            name: router-env-config
```

### `additionalVolumes`

List of additional volumes that can be mounted by containers belonging to the pod. For more information, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/storage/volumes).

```yaml
spec:
  podTemplate:
    additionalVolumes:
      - name: config-vol
        configMap:
          name: my-config
    routerContainer:
      additionalVolumeMounts:
        - name: config-vol
          mountPath: /etc/config
```

#### `imagePullPolicy`

Image pull policy. One of `Always`, `Never`, `IfNotPresent`.

```yaml
spec:
  podTemplate:
    routerContainer:
      imagePullPolicy: Always
```

#### `lifecycle`

Actions that the management system should take in response to container lifecycle events. For more information, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/).

```yaml
spec:
  podTemplate:
    routerContainer:
      lifecycle:
        preStop:
          exec:
            command: ["/bin/sh", "-c", "sleep 10"]
```

#### `livenessProbe`

Periodic probe of container liveness. Container will be restarted if the probe fails. Overrides the default liveness probe. For more information, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/).

```yaml
spec:
  podTemplate:
    routerContainer:
      livenessProbe:
        httpGet:
          path: /health?live
          port: 8088
        initialDelaySeconds: 10
        periodSeconds: 5
```

#### `additionalPorts`

List of additional ports to expose from the router container.

```yaml
spec:
  podTemplate:
    routerContainer:
      additionalPorts:
        - containerPort: 9090
          name: metrics
          protocol: TCP
```

#### `readinessProbe`

Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Overrides the default readiness probe. For more information, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/).

```yaml
spec:
  podTemplate:
    routerContainer:
      readinessProbe:
        httpGet:
          path: /health?ready
          port: 8088
        initialDelaySeconds: 5
        periodSeconds: 10
```

#### `additionalResizePolicies`

Resources resize policy for the container.

```yaml
spec:
  podTemplate:
    routerContainer:
      additionalResizePolicies:
        - resourceName: cpu
          restartPolicy: NotRequired
```

#### `resources`

Compute resources required by the router container.

```yaml
spec:
  podTemplate:
    routerContainer:
      resources:
        requests:
          cpu: 100m
          memory: 128Mi
        limits:
          cpu: 500m
          memory: 512Mi
```

#### `securityContext`

Security options the router container should be run with.

```yaml
spec:
  podTemplate:
    routerContainer:
      securityContext:
        runAsNonRoot: true
        readOnlyRootFilesystem: true
```

#### `startupProbe`

Startup probe indicates that the Pod has successfully initialized. For more information, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/).

```yaml
spec:
  podTemplate:
    routerContainer:
      startupProbe:
        httpGet:
          path: /health?live
          port: 8088
        failureThreshold: 30
        periodSeconds: 10
```

#### `stdin`

Whether this container should allocate a buffer for stdin in the container runtime.

```yaml
spec:
  podTemplate:
    routerContainer:
      stdin: true
```

#### `stdinOnce`

Whether the container runtime should close the stdin channel after it has been opened by a single attach.

```yaml
spec:
  podTemplate:
    routerContainer:
      stdinOnce: true
```

#### `terminationMessagePath`

Path to the file containing the container’s termination message.

```yaml
spec:
  podTemplate:
    routerContainer:
      terminationMessagePath: /dev/termination-log
```

#### `terminationMessagePolicy`

Indicate how the termination message should be populated. `File` will use the contents of `terminationMessagePath`.

```yaml
spec:
  podTemplate:
    routerContainer:
      terminationMessagePolicy: File
```

#### `tty`

Whether this container should allocate a TTY for itself. Requires `stdin` to be true.

```yaml
spec:
  podTemplate:
    routerContainer:
      tty: true
      stdin: true
```

#### `additionalVolumeDevices`

List of block devices to be used by the container.

```yaml
spec:
  podTemplate:
    routerContainer:
      additionalVolumeDevices:
        - name: data
          devicePath: /dev/xvda
```

#### `additionalVolumeMounts`

Pod volumes to mount into the router container's filesystem.

```yaml
spec:
  podTemplate:
    routerContainer:
      additionalVolumeMounts:
        - name: config-vol
          mountPath: /etc/config
```

### `additionalContainers`

Runs additional containers alongside the main **router** container. This replicates the **Deployment** specification for containers.

```yaml
spec:
  podTemplate:
    additionalContainers:
      - name: my-container
        image: my-image:latest
```

### `additionalInitContainers`

Runs additional init containers. This replicates the **Deployment** specification for containers.

```yaml
spec:
  podTemplate:
    additionalInitContainers:
      - name: my-container
        image: my-image:latest
```

### `affinity`

The pod’s scheduling constraints. This replicates the Deployment specification for affinity.

```yaml
spec:
  podTemplate:
    affinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: topology.kubernetes.io/zone
            operator: In
            values:
            - us-east-1a
            - us-east-1b
```

### `annotations`

Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. For more information, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations).

```yaml
spec:
  podTemplate:
    annotations:
      sidecar.istio.io/inject: "false"
```

### `image`

Custom Apollo Router image. Please note that you cannot use `image` and `routerVersion` at the same time.

```yaml
spec:
  podTemplate:
    image: my-image:latest
```

### `labels`

Map of string keys and values that can be used to organize and categorize (scope and select) objects. For more information, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels).

```yaml
spec:
  podTemplate:
    labels:
      app: my-app
      tier: backend
```

### `podSecurityContext`

Holds pod-level security attributes and common container settings.

```yaml
spec:
  podTemplate:
    podSecurityContext:
      runAsUser: 1000
      fsGroup: 2000
```

### `priorityClassName`

Indicates the pod’s priority.

```yaml
spec:
  podTemplate:
    priorityClassName: high-priority
```

### `routerVersion`

Apollo Router version. The Apollo GraphOS Operator will automatically use the default Apollo Router image with that version. Please note that you cannot use `image` and `routerVersion` at the same time.

```yaml
spec:
  podTemplate:
    routerVersion: 2.4.0
```

### `serviceAccountName`

The name of the ServiceAccount to use to run this pod.

```yaml
spec:
  podTemplate:
    serviceAccountName: my-service-account
```

### `terminationGracePeriodSeconds`

The duration in seconds that Kubernetes waits before forcefully terminating the pod.

```yaml
spec:
  podTemplate:
    terminationGracePeriodSeconds: 30
```

### `tolerations`

The pod’s tolerations.

```yaml
spec:
  podTemplate:
    tolerations:
      - key: dedicated
        operator: Equal
        value: gpu
        effect: NoSchedule
```

### `topologySpreadConstraints`

Describes how a group of pods ought to spread across topology domains.

```yaml
spec:
  podTemplate:
    topologySpreadConstraints:
      - maxSkew: 1
        topologyKey: topology.kubernetes.io/zone
        whenUnsatisfiable: ScheduleAnyway
        labelSelector:
          matchLabels:
            app: my-app
```
