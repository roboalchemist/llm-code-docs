# Source: https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/container/

Title: Container - cdk8s

URL Source: https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/container/

Markdown Content:
Define containers that run in a pod using the `Container` class.

Environment[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/container/#environment "Permanent link")
-------------------------------------------------------------------------------------------------------

A container’s environment can be populated by various methods.

### Variables[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/container/#variables "Permanent link")

Environment variables can be added to containers by specifying the variable name and value. The value can come from different sources, either dynamic or static.

```
import * as kplus from 'cdk8s-plus-31';
import { Construct } from 'constructs';
import { App, Chart, ChartProps } from 'cdk8s';

export class MyChart extends Chart {
  constructor(scope: Construct, id: string, props: ChartProps = { }) {
    super(scope, id, props);

    const pod = new kplus.Pod(this, 'Pod');
    const container = pod.addContainer({
      image: 'my-app'
    });

    // use a static value.
    container.env.addVariable('endpoint', kplus.EnvValue.fromValue('value'));

    // use a specific key from a config map.
    const backendsConfig = kplus.ConfigMap.fromConfigMapName(this, 'BackendConfig', 'backends');
    container.env.addVariable('endpoint', kplus.EnvValue.fromConfigMap(backendsConfig, 'endpoint'));

    // use a specific key from a secret.
    const credentials = kplus.Secret.fromSecretName(this, 'Credentials', 'credentials');
    container.env.addVariable('password', kplus.EnvValue.fromSecretValue({ secret: credentials, key: 'password' }));
  }
}

const app = new App();
new MyChart(app, 'container');
app.synth();
```

### Sources[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/container/#sources "Permanent link")

Environment variables can also be populated by referencing other objects as an environment source. With this method, all the key-value data of the source is added as environment variables, where the key is the env name and the value is the env value.

```
const pod = new kplus.Pod(this, 'Pod');
const cm = new kplus.ConfigMap(this, 'ConfigMap', {
  data: {
    key: 'value',
  }
});
const container = pod.addContainer({
  image: 'my-app'
});

// this will add 'key=value' env variable at runtime.
container.env.copyFrom(kplus.Env.fromConfigMap(cm));
```

Volume Mounts[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/container/#volume-mounts "Permanent link")
-----------------------------------------------------------------------------------------------------------

A very common capability is to mount a volume with some data onto a container. Using pure kubernetes API, this would require writing something like:

```
kind: Pod
apiVersion: v1
spec:
  containers:
    - name: main
      volumeMounts:
        - mountPath: /path/to/mount
          name: 'config-volume'
  volumes:
    - name: 'config-volume'
      configMap:
        name: 'config'
```

Notice the apparent redundancy of having to specify the volume name twice. Also, if you happen to need the same mount in other pods, you would need to duplicate this configuration. This can get complex and cluttered very fast.

In contrast, here is how to do this with `cdk8s+`:

```
const config = kplus.ConfigMap.fromConfigMapName(this, 'Config', 'config');
const volume = kplus.Volume.fromConfigMap(this, 'Volume', config);

const pod = new kplus.Pod(this, 'Pod');
const container = pod.addContainer({
  image: 'my-app'
})

// Cool alert: every pod that will later be configured with this container,
// will automatically have access to this volume, so you don't need to explicitly add it to the pod spec!.
container.mount('/path/to/mount', volume);
```

Probes[¶](https://cdk8s.io/docs/latest/plus/cdk8s-plus-31/container/#probes "Permanent link")
---------------------------------------------------------------------------------------------

A [Probe](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.19/#probe-v1-core) is a diagnostic performed periodically by the kubelet on a Container. To perform a diagnostic, the kubelet calls a Handler implemented by the container.

A `Probe` instance can be created through one of the `fromXxx` static methods:

*   `Probe.fromHttpGet()`
*   `Probe.fromCommand()`

Readiness, liveness, and startup probes can be configured at the container-level through the `readiness`, `liveness`, and `startup` options:

```
new kplus.Pod(this, 'Pod', {
  containers: [
    {
      image: 'my-app',
      readiness: kplus.Probe.fromHttpGet('/ping'),
    }
  ]
});
```

See the API reference for details.
