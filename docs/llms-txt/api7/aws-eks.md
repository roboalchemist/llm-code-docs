# Source: https://docs.api7.ai/enterprise/performance/aws-eks.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/performance/aws-eks.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/performance/aws-eks.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/performance/aws-eks.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/performance/aws-eks.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/performance/aws-eks.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/performance/aws-eks.md

# Source: https://docs.api7.ai/enterprise/3.8.x/performance/aws-eks.md

# Source: https://docs.api7.ai/enterprise/3.7.x/performance/aws-eks.md

# Source: https://docs.api7.ai/enterprise/3.6.x/performance/aws-eks.md

# Source: https://docs.api7.ai/enterprise/3.5.x/performance/aws-eks.md

# Source: https://docs.api7.ai/enterprise/3.4.x/performance/aws-eks.md

# Source: https://docs.api7.ai/enterprise/3.3.x/performance/aws-eks.md

# Prepare the Testing Environment (AWS EKS)

You can also visit the publicly accessible [performance benchmark repository](https://github.com/api7/api7-gateway-performance-benchmark). This repository documents in detail all the resource deployment configurations used for testing as well as the specific configuration information for each test scenario.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

### Create Cluster[â](#create-cluster "Direct link to Create Cluster")

1. Add a new cluster in AWS EKS:

![create cluster](https://static.api7.ai/uploads/2024/05/13/uKDFAOxA_eks-create-cluster.png)

2. Configure the cluster. If you have not used the EKS service to configure a cluster service role before, you can create an EKS cluster role according to the [document](https://docs.aws.amazon.com/eks/latest/userguide/service_IAM_role.html#create-service-role).

![configuration cluster](https://static.api7.ai/uploads/2024/05/13/64KiamCu_eks-config-cluster.jpeg)

3. Configure network:

![configuration cluster networks](https://static.api7.ai/uploads/2024/05/13/wN8AG0vb_eks-cluster-network.jpeg)

4. Configure observability:

![configuration observability](https://static.api7.ai/uploads/2024/05/13/vhj347ea_eks-cluster-observability.jpeg)

5. Configure plugin:

![configuration cluster plugin](https://static.api7.ai/uploads/2024/05/13/RQlUBoXL_eks-cluster-plugin.jpeg)

6. Create cluster:

![wait cluster creating](https://static.api7.ai/uploads/2024/05/13/w2Fl0M9o_eks-create-success.jpeg)

### Add Node[â](#add-node "Direct link to Add Node")

#### Create Key Pairs (Optional)[â](#create-key-pairs-optional "Direct link to Create Key Pairs (Optional)")

After configuring `Key Pairs` in the node, you can log in to the node directly. If you already have `Key Pairs`, you can skip the step of creating key pairs.

1. Select "EC2" in the AWS console, enter the EC2 interface, click "Key Pairs" on the left, and click "Create key pair" on the right.

![create key pairs](https://static.api7.ai/uploads/2024/05/13/aqJHPWbn_eks-create-key-pairs.jpeg)

2. Set key pairs name:

![configuration key pairs](https://static.api7.ai/uploads/2024/05/13/BTPp2hFV_eks-config-key-pairs.jpeg)

3. Create a key pair. At this time, the browser will automatically download the key pair. This should be saved so that you can use the command to log in to the node later.

![create key pairs success](https://static.api7.ai/uploads/2024/05/13/IlyfsC4q_eks-create-key-success.jpeg)

#### Create Node Groups[â](#create-node-groups "Direct link to Create Node Groups")

You will be adding 3 node groups, in which you will deploy API7 EE, NGINX upstream, and `wrk2` to different node groups respectively.

**Note:** If you have not created an EKS Node Role before, you need to create it first. The steps are similar to the process of creating a cluster service role in EKS. See [Amazon EKS node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html) for more details.

1. Select **Compute** and click **Add node group**.

![add node group](https://static.api7.ai/uploads/2024/05/13/2vLqMbcE_eks-add-node.jpeg)

2. Configure node group details, such as name and node IAM role.

![configure node group details](https://static.api7.ai/uploads/2024/05/13/L1K9q32x_eks-config-node.jpeg)

3. Select `Amazon Linux 2 (AL2_x86_64)` as the AMI type and `c5.4xlarge` as the instance type.

![configuration EC2](https://static.api7.ai/uploads/2024/05/13/Cmv2MlYL_eks-config-node-ec2.jpeg)

4. Configure network. If you need to SSH into the node, configure the node remote access control accordingly.

![configuration networks](https://static.api7.ai/uploads/2024/05/13/AFBAAuFq_eks-config-node-networks.jpeg)

5. Repeat the above steps to create 3 Nodes named: api7ee, upstream, `wrk2`

![node info](https://static.api7.ai/uploads/2024/05/13/KGHlNq4l_eks-node-info.jpeg)

#### Configure AWS CLI[â](#configure-aws-cli "Direct link to Configure AWS CLI")

1. Enable `kubectl` to communicate with the cluster previously created by adding a new context to the `kubectl` `config` file. See [Creating an Amazon EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html) for more details.

```
aws eks update-kubeconfig --region region-code --name my-cluster
```

2. Run `kubectl get svc` to verify successful communication with the cluster.

```
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.100.0.1   <none>        443/TCP   39m
```

#### Configure K8s Cluster Node Label[â](#configure-k8s-cluster-node-label "Direct link to Configure K8s Cluster Node Label")

Label the nodes:

```
kubectl label nodes <your-node-name> <label_key=label_value>

# example
kubectl label nodes <your-node1-name> nodeName=api7ee
kubectl label nodes <your-node2-name> nodeName=upstream
kubectl label nodes <your-node3-name> nodeName=wrk2
```

## Install[â](#install "Direct link to Install")

### Install API7 EE[â](#install-api7-ee "Direct link to Install API7 EE")

#### Control Plane[â](#control-plane "Direct link to Control Plane")

1. Create a new namespace:

```
kubectl create namespace api7
```

2. Install API7 Control Plane:

```
helm repo add api7 https://charts.api7.ai
helm repo update
# Specify the Node for the api7ee installation (the label we set for the Node earlier).
helm install api7ee3 api7/api7ee3 --set nodeSelector."nodeName"=api7ee --set postgresql.primary.nodeSelector."nodeName"=api7ee --set prometheus.server.nodeSelector."nodeName"=api7ee -n api7
```

By default, PostgreSQL and Prometheus enable persistent storage and you may receive some errors if you do not configure [StorageClass](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#dynamic) for your cluster.

You can also temporarily disable persistent storage with the command below, but be careful **not to disable it in a production environment** or the data will be lost after the Pod restarts.

```
helm install api7ee3 api7/api7ee3 --set nodeSelector."nodeName"=api7ee --set postgresql.primary.nodeSelector."nodeName"=api7ee --set prometheus.server.nodeSelector."nodeName"=api7ee --set postgresql.primary.persistence.enabled=false --set prometheus.server.persistence.enabled=false -n api7
```

3. Check deployment status:

```
kubectl get svc -owide -l app.kubernetes.io/name=api7ee3 -n api7

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE   SELECTOR
api7ee3-dashboard    ClusterIP   10.100.25.236   <none>        7080/TCP            18s   app.kubernetes.io/component=dashboard,app.kubernetes.io/instance=api7ee3,app.kubernetes.io/name=api7ee3
api7ee3-dp-manager   ClusterIP   10.100.239.32   <none>        7900/TCP,7943/TCP   18s   app.kubernetes.io/component=dp-manager,app.kubernetes.io/instance=api7ee3,app.kubernetes.io/name=api7ee3
```

4. Forward the dashboard port to the local machine, log in to the console, and upload the license:

[License Free Trial](https://api7.ai/try?product=enterprise)

```
kubectl -n api7 port-forward svc/api7ee3-dashboard 7443:7443
```

5. Set the Control Plane address:

Log in to the dashboard and configure the "Control Plane Address" in the **Gateway Settings**: `https://api7ee3-dp-manager:7943`

![gateway settings](https://static.api7.ai/uploads/2024/08/09/MAIazLjD_control-plane-addr.jpeg)

#### Disable Global Plugin `prometheus`[â](#disable-global-plugin-prometheus "Direct link to disable-global-plugin-prometheus")

![disable Prometheus](https://static.api7.ai/uploads/2024/05/13/2XUKYxfv_disable-prometheus.jpeg)

#### API7 Gateway (Data Plane)[â](#api7-gateway-data-plane "Direct link to API7 Gateway (Data Plane)")

1. Click the **Add Gateway Instance** button:

![add gateway instance](https://static.api7.ai/uploads/2024/05/13/mb3sy7wc_add-gateway-instance.jpeg)

2. Select the Kubernetes method:

Select the **Kubernetes** method and configure the "namespace" to generate an install script and run it. By default, API7 Gateway and Control Plane will authenticate with mTLS for verification. For example:

```
helm repo add api7 https://charts.api7.ai
helm repo update
cat > /tmp/tls.crt <<EOF
-----BEGIN CERTIFICATE-----
MIIBiDCCATqgAwIBAgICBAAwBQYDK2VwMEQxCzAJBgNVBAYTAlVTMRMwEQYDVQQI
EwpDYWxpZm9ybmlhMQ0wCwYDVQQKEwRBUEk3MREwDwYDVQQDEwhBUEk3IEluYzAe
Fw0yNDA4MDkwNjM0NDRaFw0yNTA5MDgwNjM0NDRaMDAxDTALBgNVBAoTBEFQSTcx
HzAdBgNVBAMTFmFwaTdlZTMtYXBpc2l4LWdhdGV3YXkwKjAFBgMrZXADIQA4EF9i
qogMWwWQnhrD478bCTQxxeDrT8zUUC+KC4lbLaNkMGIwDgYDVR0PAQH/BAQDAgeA
MBMGA1UdJQQMMAoGCCsGAQUFBwMCMC0GA1UdDgQmBCQzMmE2MTU3Yi0yMGFmLTQ4
NDctYWEyOC04M2M1M2ZmMTY4ZDAwDAYDVR0jBAUwA4ABMDAFBgMrZXADQQDzxx2i
QV62ZB0WOdxofuQ2J+35sh6tYCOayrjAn5KISQ5L1JMIrDZKotq5G8JLM3qMs9Nc
DZjDWzx+W1j94GAO
-----END CERTIFICATE-----
EOF
cat > /tmp/tls.key <<EOF
-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VwBCIEILY+bFM98L+OLxTWd73hnl9FmYGfhGASUhuYrpt/Q0CE
-----END PRIVATE KEY-----
EOF
cat > /tmp/ca.crt <<EOF
-----BEGIN CERTIFICATE-----
MIIBdjCCASigAwIBAgIRAJDZ9s+rZMNiqiiAyT3NXpkwBQYDK2VwMEQxCzAJBgNV
BAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMQ0wCwYDVQQKEwRBUEk3MREwDwYD
VQQDEwhBUEk3IEluYzAeFw0yNDA4MDkwNjI4MDBaFw0zNDA4MDcwNjI4MDBaMEQx
CzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMQ0wCwYDVQQKEwRBUEk3
MREwDwYDVQQDEwhBUEk3IEluYzAqMAUGAytlcAMhAN/VCNB2ChcL4BrXVImIW/EH
YZi2oDrXVub/mXaMSr7Zoy8wLTAOBgNVHQ8BAf8EBAMCAoQwDwYDVR0TAQH/BAUw
AwEB/zAKBgNVHQ4EAwQBMDAFBgMrZXADQQCA0M1McTsw6c9LGqmFP1g/BXNyeyDI
dBnVnPlZgCwMQCDqkI9S8wyZbz4jLGGccKnqAclNhuJsSn94UGuteaIG
-----END CERTIFICATE-----
EOF
kubectl create secret generic -n api7 api7-ee-3-gateway-tls --from-file=tls.crt=/tmp/tls.crt --from-file=tls.key=/tmp/tls.key --from-file=ca.crt=/tmp/ca.crt
helm upgrade --install -n api7 --create-namespace api7-ee-3-gateway api7/gateway \
  --set "etcd.auth.tls.enabled=true" \
  --set "etcd.auth.tls.existingSecret=api7-ee-3-gateway-tls" \
  --set "etcd.auth.tls.certFilename=tls.crt" \
  --set "etcd.auth.tls.certKeyFilename=tls.key" \
  --set "etcd.auth.tls.verify=true" \
  --set "gateway.tls.existingCASecret=api7-ee-3-gateway-tls" \
  --set "gateway.tls.certCAFilename=ca.crt" \
  --set "apisix.extraEnvVars[0].name=API7_GATEWAY_GROUP_SHORT_ID" \
  --set "apisix.extraEnvVars[0].value=default" \
  --set "etcd.host[0]=https://api7ee3-dp-manager:7943" \
  --set "apisix.replicaCount=1" \
  --set "apisix.image.repository=api7/api7-ee-3-gateway" \
  --set "apisix.image.tag=3.2.14.4" \
  --set "nginx.workerProcesses"=1 \
  --set apisix.nodeSelector.nodeName=api7ee \
  --set apisix.securityContext.runAsNonRoot=false \
  --set apisix.securityContext.runAsUser=0
```

You should install the Gateway on a separate node and adjust the `worker_processes` as needed. In addition, if you want to install `top` and other tools in the gateway container, you can start it as root. For example:

â¶ configure gateway worker\_processes: `--set "nginx.workerProcesses"=1`

â· configure node selector: `--set apisix.nodeSelector.nodeName=api7ee`

â¸ run as root user:

* `--set apisix.securityContext.runAsNonRoot=false`
* `--set apisix.securityContext.runAsUser=0`

### Install NGINX Upstream[â](#install-nginx-upstream "Direct link to Install NGINX Upstream")

1. Create a NGINX upstream deployment file:

nginx-upstream.yaml

```
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-config
  namespace: api7
data:
  nginx.conf: |
    master_process on;

    worker_processes 1;
    events {
        worker_connections 4096;
    }

    http {
        resolver ipv6=off 8.8.8.8;

        #access_log logs/access.log;
        access_log off;
        server_tokens off;
        keepalive_requests 10000000;

        server {
            listen 1980;
            server_name _;

            location / {
                proxy_set_header Connection "";
                return 200 "hello world\n";
            }
        }
    }
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: api7
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        volumeMounts:
        - name: nginx-config-volume
          mountPath: /etc/nginx/nginx.conf
          subPath: nginx.conf
      nodeSelector:
        nodeName: upstream
      volumes:
      - name: nginx-config-volume
        configMap:
          name: nginx-config
---
```

2. Deploy NGINX upstream

```
kubectl apply -f nginx-upstream.yaml
```

### Install `wrk2`[â](#install-wrk2 "Direct link to install-wrk2")

1. Create a `wrk2` deployment file:

wrk2.yaml

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wrk2-deployment
  namespace: api7
spec:
  replicas: 1
  selector:
    matchLabels:
      app: wrk2
  template:
    metadata:
      labels:
        app: wrk2
    spec:
      containers:
      - name: wrk2
        image: bootjp/wrk2
      nodeSelector:
        nodeName: wrk2
```

2. Deploy `wrk2`

```
kubectl apply -f wrk2.yaml
```

## Configurations[â](#configurations "Direct link to Configurations")

You can find the configuration for each test scenario in the public [performance benchmark repository](https://github.com/api7/api7-gateway-performance-benchmark) and create the configuration for each scenario directly using the [ADC](https://docs.api7.ai/enterprise/3.3.x/best-practices/devops-adc.md) tool.

* [One route without plugins](https://github.com/api7/api7-gateway-performance-benchmark/blob/main/adc_conf/1-one-route-without-plugin.yaml)
* [One route with `limit-count` plugin](https://github.com/api7/api7-gateway-performance-benchmark/blob/main/adc_conf/2-one-route-with-limit-count.yaml)
* [One route with `key-auth` and `limit-count` plugin](https://github.com/api7/api7-gateway-performance-benchmark/blob/main/adc_conf/3-one-route-with-key-auth-and-limit-count.yaml)
* [One route and one consumer with `key-auth` plugin](https://github.com/api7/api7-gateway-performance-benchmark/blob/main/adc_conf/4-one-route-with-key-auth.yaml)
* [100 routes without plugins](https://github.com/api7/api7-gateway-performance-benchmark/blob/main/adc_conf/5-100-route-without-plugin.yaml)
* [100 routes with `limit-count` plugin](https://github.com/api7/api7-gateway-performance-benchmark/blob/main/adc_conf/6-100-route-with-limit-count.yaml)
* [100 routes and 100 consumers with `key-auth` and `limit-count` plugin](https://github.com/api7/api7-gateway-performance-benchmark/blob/main/adc_conf/7-100-route-and-consumer-with-key-auth-limit-count.yaml)
* [100 routes and 100 consumers with `key-auth` plugin](https://github.com/api7/api7-gateway-performance-benchmark/blob/main/adc_conf/8-100-route-and-consumer-with-key-auth.yaml)
