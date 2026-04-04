# Source: https://fly.io/docs/kubernetes/using-volumes/

Title: Using volumes with FKS

URL Source: https://fly.io/docs/kubernetes/using-volumes/

Markdown Content:
Using volumes with FKS · Fly Docs
===============

[Skip to content](https://fly.io/docs/kubernetes/using-volumes/#main-content-start)

[](https://fly.io/)[](https://fly.io/docs/)

[**Need a Logo?** View Our Brand Assets](https://fly.io/docs/about/brand/)

Search K

Open main menu[](https://fly.io/)[](https://fly.io/docs/)

[Pricing](https://fly.io/pricing/)[Support](https://fly.io/docs/about/support/)

[Sign In](https://fly.io/app/sign-in/)[Sign Up](https://fly.io/app/sign-up/)

[Getting Started](https://fly.io/docs/getting-started/launch)Toggle Getting Started section
*   [Quickstart: Launch your app](https://fly.io/docs/getting-started/launch/)
*   [Launch HelloFly Demo App](https://fly.io/docs/getting-started/launch-demo)
*   [Deep Dive Demo App](https://fly.io/docs/deep-dive/)
*   [Choose a Language or Framework](https://fly.io/docs/getting-started/get-started-by-framework/)
*   [Fly.io Essentials](https://fly.io/docs/getting-started/essentials/)
*   [Migrate from Heroku](https://fly.io/docs/getting-started/migrate-from-heroku/)
*   [Troubleshoot Deployments](https://fly.io/docs/getting-started/troubleshooting/)

[Guides (Blueprints)](https://fly.io/docs/blueprints/)Toggle Guides (Blueprints) section
*   [Guides Overview](https://fly.io/docs/blueprints/)

[Apps on Fly.io](https://fly.io/docs/apps/overview)Toggle Apps on Fly.io section
*   [Fly Apps Overview](https://fly.io/docs/apps/overview/)
*   [Fly Launch](https://fly.io/docs/launch/)
*   [Secrets](https://fly.io/docs/apps/secrets/)
*   [Production Checklist](https://fly.io/docs/apps/going-to-production/)

[Languages & Frameworks](https://fly.io/docs/languages-and-frameworks/)Toggle Languages & Frameworks section
*   [Elixir](https://fly.io/docs/elixir/)
*   [Rails](https://fly.io/docs/rails/getting-started/)
*   [Laravel](https://fly.io/docs/laravel/)
*   [Django](https://fly.io/docs/django/getting-started/)
*   [JavaScript](https://fly.io/docs/js/)
*   [Rust](https://fly.io/docs/rust/)
*   [Python](https://fly.io/docs/python/)
*   [More...](https://fly.io/docs/languages-and-frameworks/)

[Fly Machines](https://fly.io/docs/machines/overview)Toggle Fly Machines section
*   [Introduction to Fly Machines](https://fly.io/docs/machines/overview/)
*   [Machines API](https://fly.io/docs/machines/api/)
*   [Run a New Machine](https://fly.io/docs/machines/flyctl/fly-machine-run/)
*   [Update a Machine](https://fly.io/docs/machines/flyctl/fly-machine-update/)
*   [Machine Sizing](https://fly.io/docs/machines/guides-examples/machine-sizing/)
*   [Machine Restart Policy](https://fly.io/docs/machines/guides-examples/machine-restart-policy/)
*   [Machine States](https://fly.io/docs/machines/machine-states/)
*   [Run User Code on Fly Machines](https://fly.io/docs/machines/guides-examples/functions-with-machines/)
*   [One App Per Customer - Why?](https://fly.io/docs/machines/guides-examples/one-app-per-user-why/)
*   [The Machine Runtime Environment](https://fly.io/docs/machines/runtime-environment/)

[Managed Postgres](https://fly.io/docs/mpg)Toggle Managed Postgres section
*   [Create and Connect to a Managed Postgres Cluster](https://fly.io/docs/mpg/create-and-connect/)
*   [Cluster Configuration Options](https://fly.io/docs/mpg/configuration/)
*   [Phoenix with Managed Postgres](https://fly.io/docs/mpg/guides-examples/phoenix-guide/)
*   [Monitoring and Metrics](https://fly.io/docs/mpg/metrics/)
*   [Import data from another postgres cluster](https://fly.io/docs/mpg/import/)
*   [Supported Postgres Extensions](https://fly.io/docs/mpg/extensions/)

[Fly GPUs](https://fly.io/docs/gpus/gpu-quickstart)Toggle Fly GPUs section
*   [GPU Quickstart](https://fly.io/docs/gpus/gpu-quickstart/)
*   [Getting Started with GPU Machines](https://fly.io/docs/gpus/getting-started-gpus/)
*   [Python GPU Dev Machine](https://fly.io/docs/gpus/python-gpu-example/)

[Databases & Storage](https://fly.io/docs/database-storage-guides/)Toggle Databases & Storage section
*   [Fly Managed Postgres](https://fly.io/docs/mpg/)
*   [Tigris Object Storage](https://fly.io/docs/tigris/)
*   [Upstash for Redis®](https://fly.io/docs/upstash/redis/)

[Fly Volumes](https://fly.io/docs/volumes/overview)Toggle Fly Volumes section
*   [Fly Volumes Overview](https://fly.io/docs/volumes/overview/)
*   [Create and Manage Volumes](https://fly.io/docs/volumes/volume-manage/)
*   [Manage Volume Snapshots](https://fly.io/docs/volumes/snapshots/)
*   [Volume States](https://fly.io/docs/volumes/volume-states/)

[Fly Kubernetes](https://fly.io/docs/kubernetes/fks-quickstart)Toggle Fly Kubernetes section
*   [Fly Kubernetes Quickstart](https://fly.io/docs/kubernetes/fks-quickstart/)
*   [Fly Kubernetes Features](https://fly.io/docs/kubernetes/fks-features/)
*   [Create an FKS Cluster](https://fly.io/docs/kubernetes/clusters/)
*   [Connect to an FKS Cluster](https://fly.io/docs/kubernetes/connect-clusters/)
*   [Configure FKS Services](https://fly.io/docs/kubernetes/services/)
*   [Use GPUs with FKS](https://fly.io/docs/kubernetes/using-gpus/)
*   [Use Volumes with FKS](https://fly.io/docs/kubernetes/using-volumes/)

[Networking](https://fly.io/docs/networking/)Toggle Networking section
*   [Connect to an App Service](https://fly.io/docs/networking/app-services/)
*   [Public Networking](https://fly.io/docs/networking/services/)
*   [Private Networking](https://fly.io/docs/networking/private-networking/)
*   [Custom Private Networks](https://fly.io/docs/networking/custom-private-networks/)
*   [Flycast - Private Proxy Services](https://fly.io/docs/networking/flycast/)
*   [Egress IP Addresses](https://fly.io/docs/networking/egress-ips/)
*   [Dynamic Request Routing](https://fly.io/docs/networking/dynamic-request-routing/)
*   [Custom Domains](https://fly.io/docs/networking/custom-domain/)
*   [Understanding Cloudflare](https://fly.io/docs/networking/understanding-cloudflare/)
*   [Request Headers](https://fly.io/docs/networking/request-headers/)
*   [Run UDP Services](https://fly.io/docs/networking/udp-and-tcp/)
*   [TLS Support](https://fly.io/docs/networking/tls/)

[Monitoring](https://fly.io/docs/monitoring/)Toggle Monitoring section
*   [Metrics](https://fly.io/docs/monitoring/metrics/)
*   [Sentry Error Tracking](https://fly.io/docs/monitoring/sentry/)
*   [Logging](https://fly.io/docs/monitoring/logging-overview/)Toggle Logging section
    *   [Live Tail Logs](https://fly.io/docs/monitoring/live-tail-logs/)
    *   [Logs API Options](https://fly.io/docs/monitoring/logs-api-options/)
    *   [Search Logs](https://fly.io/docs/monitoring/search-logs/)
    *   [Export Logs](https://fly.io/docs/monitoring/exporting-logs/)
    *   [Error Codes](https://fly.io/docs/monitoring/error-codes/)

[Security](https://fly.io/docs/security/)Toggle Security section
*   [Organization Roles and Permissions](https://fly.io/docs/security/org-roles-permissions/)
*   [SSO for Organizations](https://fly.io/docs/security/sso/)
*   [Remove a Member from an Org](https://fly.io/docs/security/remove-org-member/)
*   [TLS Termination](https://fly.io/docs/security/tls-termination/)
*   [App Security by Arcjet](https://fly.io/docs/security/arcjet/)
*   [Access Tokens](https://fly.io/docs/security/tokens/)
*   [OpenID Connect](https://fly.io/docs/reference/openid-connect/)
*   [Shared Responsibility Model](https://fly.io/docs/security/shared-responsibility/)
*   [Security Practices and Compliance](https://fly.io/docs/security/security-at-fly-io/)

[Reference](https://fly.io/docs/reference/)Toggle Reference section
*   [flyctl](https://fly.io/docs/flyctl/)
*   [App Config Reference (fly.toml)](https://fly.io/docs/reference/configuration/)
*   [Architecture](https://fly.io/docs/reference/architecture/)
*   [Autoscaling](https://fly.io/docs/reference/autoscaling/)
*   [AWS to Fly Overview](https://fly.io/docs/reference/aws-to-fly-guide/)
*   [Builders](https://fly.io/docs/reference/builders/)
*   [Content Encoding](https://fly.io/docs/reference/content-encoding/)
*   [Fly Launch](https://fly.io/docs/reference/fly-launch/)
*   [Health Checks](https://fly.io/docs/reference/health-checks/)
*   [Load Balancing](https://fly.io/docs/reference/load-balancing/)
*   [Machine Migration](https://fly.io/docs/reference/machine-migration/)
*   [Multiple Processes in Apps](https://fly.io/docs/app-guides/multiple-processes/)
*   [Fly Proxy](https://fly.io/docs/reference/fly-proxy/)
*   [Fly Proxy Autostop/Autostart](https://fly.io/docs/reference/fly-proxy-autostop-autostart/)
*   [Regions](https://fly.io/docs/reference/regions/)
*   [Suspend/Resume](https://fly.io/docs/reference/suspend-resume/)

[About](https://fly.io/docs/about/)Toggle About section
*   [Pricing](https://fly.io/docs/about/pricing/)
*   [Billing](https://fly.io/docs/about/billing/)
*   [Cost Management](https://fly.io/docs/about/cost-management/)
*   [Free Trial](https://fly.io/docs/about/free-trial/)
*   [Support](https://fly.io/docs/about/support/)
*   [Engineering Jobs](https://fly.io/docs/hiring/)
*   [Healthcare on Fly.io](https://fly.io/docs/about/healthcare/)
*   [Extensions Program](https://fly.io/docs/about/extensions/)
*   [Extensions API](https://fly.io/docs/reference/extensions_api/)
*   [Merch](https://fly.io/docs/about/merch/)
*   [Open Source](https://fly.io/docs/about/open-source/)
*   [Using Our Brand](https://fly.io/docs/about/brand/)
*   [Privacy Policy](https://fly.io/legal/privacy-policy/)
*   [Terms of Service](https://fly.io/legal/terms-of-service/)

--- title: Using volumes with FKS layout: docs toc: true nav: firecracker --- <div class= "important icon"> Fly Kubernetes is in closed beta and not recommended for critical production usage. To report issues or provide feedback, email us at beta@fly.io. </div> Fly Kubernetes supports [persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/+external) and [generic ephemeral volumes](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/#generic-ephemeral-volumes+external). There are general considerations to keep in mind when using volumes in Fly Kubernetes: * Volumes are built on top of [Fly Volumes](/docs/volumes/). They are local NVME drives and require your Pod to be deployed in the same region as the volume. * Only one persistent or ephemeral volume can be mounted at a time. * The maximum storage size available is 500GB. ## Persistent Volumes PersistentVolumes are managed through PersistentVolumeClaims (PVCs). PersistentVolumes (PVs) are tied to the lifecycle of a PersistentVolumeClaim. By default, creating a PVC creates an underlying PV and deleting a PVC deletes the PV bound to it. Below is an example of configuring a PersistentVolume to use with a Pod: ```yaml apiVersion: v1 kind: PersistentVolumeClaim metadata: name: myclaim spec: selector: matchLabels: region: iad storageClassName: flyio-volume accessModes: - ReadWriteOncePod resources: requests: storage: 5Gi --- apiVersion: v1 kind: Pod metadata: name: nginx spec: containers: - name: nginx image: nginx:latest volumeMounts: - mountPath: "/var/www/html" name: mypd resources: limits: memory: "512Mi" cpu: "1" volumes: - name: mypd persistentVolumeClaim: claimName: myclaim ``` In our configuration: * The `storageClassName` must be set to either `flyio-volume` or `flyio-volume-retain`. You can view the available storage classes with `kubectl get sc`. The default StorageClass is `flyio-volume`. * `selector` is optional. It serves a dual purpose. First, it ensures that a PVC is bound to a PV in the region specified in the selector. Second, if a PVC requires dynamic provisioning of the underlying Fly Volume, it is provisioned in the specified region. If not set, the volume is created in the region of the cluster. * `accessModes` only supports `ReadWriteOncePod`. After applying the configuration, you can view the PVC and PV generated by the definition using `kubectl`. ``` > kubectl get pvc NAME STATUS VOLUME CAPACITY ACCESS MODES STORAGECLASS AGE myclaim Bound pvc-r1plo75g59d25l0r 5Gi RWOP flyio-volume 9s ``` ``` > kubectl get pv NAME CAPACITY ACCESS MODES RECLAIM POLICY STATUS CLAIM STORAGECLASS REASON AGE pvc-r1plo75g59d25l0r 5Gi RWOP Delete Bound default/myclaim flyio-volume 55s ``` ### Reclaim policy Fly Kubernetes supports both the `Delete` and `Retain` policy for PersistentVolumes. * StorageClass `flyio-volume` has a reclaim policy set to `Delete` * StorageClass `flyio-volume-retain` has a reclaim policy set to `Retain` By default, `flyio-volume` is used. When using the `flyio-volume-retain` StorageClass, you are responsible for deleting the PersistentVolume object and its underlying Fly Volume. The details of the underlying storage are found in the annotations of the PersistentVolume. Using the PV from above ``` > kubectl describe pv pvc-r1plo75g59d25l0r Name: pvc-r1plo75g59d25l0r Labels: region=iad Annotations: fly.io/app: fks-default-vz5dlqz7v4ylrnpq fly.io/region: iad pv.kubernetes.io/provisioned-by: volume.csi.fly.io volume.fly.io/id: vol_r1plo75g59d25l0r Finalizers: [kubernetes.io/pv-protection] StorageClass: flyio-volume Status: Bound Claim: default/myclaim Reclaim Policy: Delete Access Modes: RWOP VolumeMode: Filesystem Capacity: 5Gi Node Affinity: <none> Message: Source: Type: CSI (a Container Storage Interface (CSI) volume source) Driver: volume.csi.fly.io FSType: ext4 VolumeHandle: vol_r1plo75g59d25l0r ReadOnly: false VolumeAttributes: <none> Events: <none> ``` The annotation `fly.io/app` specifies which Fly app the volumes belongs to. The annotation `volume.fly.io/id` gives you the ID of the volume. You can delete the Fly Volume using `flyctl` ``` fly vol rm pvc-r1plo75g59d25l0r -a fks-default-vz5dlqz7v4ylrnpq ``` ## Generic ephemeral volumes Fly Kubernetes supports ephemeral volumes through generic ephemeral volumes. It uses the same underlying PVC and PV machinery. Kubernetes handles creating the PVC and its corresponding PV and deleting both objects when the Pod is deleted. Below is an example of creating a Pod with a generic ephemeral volume: ```yaml apiVersion: v1 kind: Pod metadata: name: nginx spec: containers: image: nginx:latest volumeMounts: - mountPath: "/var/www/html" name: scratch-volume resources: limits: memory: "512Mi" cpu: "1" volumes: - name: scratch-volume ephemeral: volumeClaimTemplate: spec: accessModes: - ReadWriteOncePod storageClassName: "flyio-volume" resources: requests: storage: 5Gi ``` For generic ephemeral volumes to work as expected, `storageClassName` must be set to `flyio-volume`. 

[Docs](https://fly.io/docs/)[Fly Kubernetes](https://fly.io/docs/kubernetes)Using volumes with FKS
Using volumes with FKS
======================

Fly Kubernetes is in closed beta and not recommended for critical production usage. To report issues or provide feedback, email us at [beta@fly.io](mailto:beta@fly.io).

Fly Kubernetes supports [persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) and [generic ephemeral volumes](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/#generic-ephemeral-volumes). There are general considerations to keep in mind when using volumes in Fly Kubernetes:

*   Volumes are built on top of [Fly Volumes](https://fly.io/docs/volumes/). They are local NVME drives and require your Pod to be deployed in the same region as the volume. 
*   Only one persistent or ephemeral volume can be mounted at a time. 
*   The maximum storage size available is 500GB. 

[](https://fly.io/docs/kubernetes/using-volumes/#persistent-volumes)Persistent Volumes
--------------------------------------------------------------------------------------

PersistentVolumes are managed through PersistentVolumeClaims (PVCs). PersistentVolumes (PVs) are tied to the lifecycle of a PersistentVolumeClaim. By default, creating a PVC creates an underlying PV and deleting a PVC deletes the PV bound to it.

Below is an example of configuring a PersistentVolume to use with a Pod:

 Wrap text  Copy to clipboard 

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: myclaim
spec:
  selector:
    matchLabels:
      region: iad
  storageClassName: flyio-volume
  accessModes:
    - ReadWriteOncePod
  resources:
    requests:
      storage: 5Gi
---
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
    - name: nginx
      image: nginx:latest
      volumeMounts:
        - mountPath: "/var/www/html"
          name: mypd
      resources:
        limits:
          memory: "512Mi"
          cpu: "1"
  volumes:
    - name: mypd
      persistentVolumeClaim:
        claimName: myclaim
```

In our configuration:

*   The `storageClassName` must be set to either `flyio-volume` or `flyio-volume-retain`. You can view the available storage classes with `kubectl get sc`. The default StorageClass is `flyio-volume`. 
*   `selector` is optional. It serves a dual purpose. First, it ensures that a PVC is bound to a PV in the region specified in the selector. Second, if a PVC requires dynamic provisioning of the underlying Fly Volume, it is provisioned in the specified region. If not set, the volume is created in the region of the cluster. 
*   `accessModes` only supports `ReadWriteOncePod`. 

After applying the configuration, you can view the PVC and PV generated by the definition using `kubectl`.

 Wrap text  Copy to clipboard 

```
> kubectl get pvc
NAME          STATUS   VOLUME                 CAPACITY   ACCESS MODES   STORAGECLASS   AGE
myclaim       Bound    pvc-r1plo75g59d25l0r   5Gi        RWOP           flyio-volume   9s
```

 Wrap text  Copy to clipboard 

```
> kubectl get pv
NAME                   CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                 STORAGECLASS   REASON   AGE
pvc-r1plo75g59d25l0r   5Gi        RWOP           Delete           Bound    default/myclaim       flyio-volume            55s
```

### [](https://fly.io/docs/kubernetes/using-volumes/#reclaim-policy)Reclaim policy

Fly Kubernetes supports both the `Delete` and `Retain` policy for PersistentVolumes.

*   StorageClass `flyio-volume` has a reclaim policy set to `Delete`
*   StorageClass `flyio-volume-retain` has a reclaim policy set to `Retain`

By default, `flyio-volume` is used.

When using the `flyio-volume-retain` StorageClass, you are responsible for deleting the PersistentVolume object and its underlying Fly Volume. The details of the underlying storage are found in the annotations of the PersistentVolume. Using the PV from above

 Wrap text  Copy to clipboard 

```
> kubectl describe pv pvc-r1plo75g59d25l0r
Name:            pvc-r1plo75g59d25l0r
Labels:          region=iad
Annotations:     fly.io/app: fks-default-vz5dlqz7v4ylrnpq
                 fly.io/region: iad
                 pv.kubernetes.io/provisioned-by: volume.csi.fly.io
                 volume.fly.io/id: vol_r1plo75g59d25l0r
Finalizers:      [kubernetes.io/pv-protection]
StorageClass:    flyio-volume
Status:          Bound
Claim:           default/myclaim
Reclaim Policy:  Delete
Access Modes:    RWOP
VolumeMode:      Filesystem
Capacity:        5Gi
Node Affinity:   <none>
Message:
Source:
    Type:              CSI (a Container Storage Interface (CSI) volume source)
    Driver:            volume.csi.fly.io
    FSType:            ext4
    VolumeHandle:      vol_r1plo75g59d25l0r
    ReadOnly:          false
    VolumeAttributes:  <none>
Events:                <none>
```

The annotation `fly.io/app` specifies which Fly app the volumes belongs to. The annotation `volume.fly.io/id` gives you the ID of the volume. You can delete the Fly Volume using `flyctl`

 Wrap text  Copy to clipboard 

```
fly vol rm pvc-r1plo75g59d25l0r -a fks-default-vz5dlqz7v4ylrnpq
```

[](https://fly.io/docs/kubernetes/using-volumes/#generic-ephemeral-volumes)Generic ephemeral volumes
----------------------------------------------------------------------------------------------------

Fly Kubernetes supports ephemeral volumes through generic ephemeral volumes. It uses the same underlying PVC and PV machinery. Kubernetes handles creating the PVC and its corresponding PV and deleting both objects when the Pod is deleted. Below is an example of creating a Pod with a generic ephemeral volume:

 Wrap text  Copy to clipboard 

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
      image: nginx:latest
      volumeMounts:
        - mountPath: "/var/www/html"
          name: scratch-volume
      resources:
        limits:
          memory: "512Mi"
          cpu: "1"
  volumes:
    - name: scratch-volume
      ephemeral:
        volumeClaimTemplate:
          spec:
            accessModes:
              - ReadWriteOncePod
            storageClassName: "flyio-volume"
            resources:
              requests:
                storage: 5Gi
```

For generic ephemeral volumes to work as expected, `storageClassName` must be set to `flyio-volume`.

Copy page as markdown or[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fkubernetes%2Fusing-volumes.html.markerb)

[Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Using+volumes+with+FKS%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fkubernetes%2Fusing-volumes%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fkubernetes%2Fusing-volumes.html.markerb%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Using+volumes+with+FKS%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/kubernetes/using-volumes.html.markerb)

[On this page](https://fly.io/docs/kubernetes/using-volumes/#)
*   [Persistent Volumes](https://fly.io/docs/kubernetes/using-volumes/#persistent-volumes)
    *   [Reclaim policy](https://fly.io/docs/kubernetes/using-volumes/#reclaim-policy)

*   [Generic ephemeral volumes](https://fly.io/docs/kubernetes/using-volumes/#generic-ephemeral-volumes)

Copy page as markdown[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fkubernetes%2Fusing-volumes.html.markerb)
