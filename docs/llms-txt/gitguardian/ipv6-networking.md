# Source: https://docs.gitguardian.com/self-hosting/management/infrastructure-management/ipv6-networking.md

# IPv6 networking

> Configure IPv6 and dual-stack networking for GitGuardian self-hosted Kubernetes deployments.

GitGuardian self-hosted supports IPv4, IPv6, and dual-stack networking configurations for maximum flexibility in modern cloud and on-premises environments. IPv6 is available exclusively for Helm-based installations.

:::tip When to use IPv6
IPv6 support is useful when:
- Your Kubernetes cluster is IPv6-only or dual-stack
- You're migrating from IPv4 to IPv6
- Cloud provider requirements (some AWS regions encourage IPv6-only)
- Corporate security policies require IPv6
:::

## Quick start

### Helm values
IPv6 support can activated via the Helm chart value `network.ipFamily`.
| Your cluster setup | Use `network.ipFamily` | Notes |
| --- | --- | --- |
| **IPv4-only** (default) | `ipv4` | Backward compatible, no changes needed |
| **IPv6-only** | `ipv6` | All services use IPv6 addresses only |
| **Dual-stack** | `dualstack` or `ipv6` | See platform-specific notes below |

### Platform-specific considerations

#### AWS EKS

:::warning EKS dual-stack limitation
AWS EKS does not support true dual-stack Kubernetes services. Even when your VPC is dual-stack, Kubernetes services must be **either** IPv4 **or** IPv6, not both.

**Always use `ipFamily: 'ipv6'` on EKS**, even when your VPC is dual-stack.
:::

Your pods in a dual-stack EKS VPC can still reach both IPv4 and IPv6 external services (databases, Redis, APIs), but Kubernetes services themselves will only have IPv6 addresses.

#### Google GKE

GKE fully supports dual-stack services where services receive both IPv4 and IPv6 addresses simultaneously.

**Requirements:**
- GKE cluster with `stack_type = "IPV4_IPV6"`
- Advanced Datapath (Dataplane V2) enabled
- Kubernetes 1.28+

You can use any `ipFamily` value (`ipv4`, `ipv6`, or `dualstack`) based on your needs.

#### Azure AKS

AKS supports dual-stack services similar to GKE. Services can have both IPv4 and IPv6 addresses.

You can use any `ipFamily` value based on your needs.

#### On-premises

IPv6 support depends on your CNI plugin and cluster configuration:

| CNI Plugin | IPv6 Support |
| --- | --- |
| Calico | â Full support |
| Cilium | â Full support |
| Flannel | â ï¸ Limited (IPv6-only, no dual-stack) |
| Weave Net | â ï¸ Experimental |

We recommend testing your cluster's IPv6 capabilities before deploying in production.

## Prerequisites

### Cluster requirements

1. **Kubernetes 1.28+** (required for stable dual-stack support)
2. **IPv6-enabled cluster**: Verify with:
   ```bash
   kubectl get nodes -o jsonpath='{.items[*].spec.podCIDRs}'
   ```
   You should see IPv6 CIDRs like `2001:db8::/64`

3. **CNI plugin with IPv6 support**: AWS VPC CNI, Calico, Cilium, etc.

### PostgreSQL

Your PostgreSQL must be IPv6-accessible:

**Cloud providers:**
- **AWS RDS**: Set `network_type = "DUAL"`
- **Google Cloud SQL**: IPv6 is automatically available
- **Azure Database for PostgreSQL**: Enable IPv6 in networking settings

**Self-hosted**: Ensure `listen_addresses` includes IPv6:
```ini
# postgresql.conf
listen_addresses = '::'  # Listen on all IPv4 and IPv6 addresses
```

And configure `pg_hba.conf` for IPv6 connections:
```
host    all    all    2001:db8::/32    md5
```

### Redis

Your Redis must be IPv6-accessible:

**Cloud providers:**
- **AWS ElastiCache**: Set `network_type = "dual_stack"`
- **Google Memorystore**: IPv6 is automatically available for certain tiers. However,  Memorystore for Redis instances is not compatible with IPv6.
- **Azure Cache for Redis**: Enable IPv6 in networking settings

**Self-hosted**: Ensure Redis binds to IPv6:
```ini
# redis.conf
bind :: 0.0.0.0
```

### Network connectivity

Different IPv6 cluster configurations have different connectivity capabilities:

| Cluster Type | Can reach IPv4 services | Can reach IPv6 services | Common setup |
| --- | --- | --- | --- |
| **Dual-stack** | â Yes | â Yes | Most common, recommended |
| **IPv6-only with NAT64/DNS64** | â Yes (via translation) | â Yes | AWS EKS default |
| **IPv6-only without NAT64** | â No | â Yes | Rare, not recommended |

:::info NAT64/DNS64
NAT64 and DNS64 enable IPv6-only pods to reach IPv4-only external services by translating IPv6 requests to IPv4. AWS EKS enables this by default for IPv6 clusters.
:::

## Configuration

### Helm values configuration

Add the `network.ipFamily` configuration to your Helm values file:

#### IPv4-only (default)

```yaml
# No configuration needed - this is the default
network:
  ipFamily: 'ipv4'
```

#### IPv6-only

```yaml
network:
  ipFamily: 'ipv6'

# PostgreSQL and Redis must be IPv6-accessible
postgresql:
  host: '2001:db8::1234'  # IPv6 address or hostname with AAAA record
redis:
  main:
    host: '2001:db8::5678'
```

You must also configure Loki for IPv6. See [Loki IPv6 configuration](#loki-ipv6-configuration) below.

#### Dual-stack (GKE/AKS)

```yaml
network:
  ipFamily: 'dualstack'

postgresql:
  host: 'postgres.example.com'  # Must have A or AAAA DNS record
redis:
  main:
    host: 'redis.example.com'
```

Loki IPv6 configuration is optional for dual-stack (components can use IPv4).

### Loki IPv6 configuration

Loki requires explicit IPv6 configuration in IPv6-only clusters because it uses memberlist for service discovery between components. Add this to your Helm values:

```yaml
loki:
  loki:
    commonConfig:
      ring:
        instance_enable_ipv6: true
        kvstore:
          store: "memberlist"
    compactor:
      compactor_ring:
        instance_enable_ipv6: true
    distributor:
      ring:
        instance_enable_ipv6: true
    extraMemberlistConfig:
      bind_addr:
        - '::'
    frontend:
      instance_enable_ipv6: true
    index_gateway:
      ring:
        instance_enable_ipv6: true
    ingester:
      lifecycler:
        enable_inet6: true
    pattern_ingester:
      enabled: true
      lifecycler:
        enable_inet6: true
    query_scheduler:
      scheduler_ring:
        instance_enable_ipv6: true
    ruler:
      ring:
        instance_enable_ipv6: true
```

| Requirement | Notes |
| --- | --- |
| **IPv6-only** | Required - components cannot communicate without it |
| **Dual-stack** | Optional - components can fall back to IPv4 |

## Deployment

:::tip Preflights
When your external databases are IPv6-ready, test connectivity using our [preflights](../../installation/installation-existing-cluster-helm#run-preflight-checks-).
:::

### Upgrading existing IPv4 deployment

#### To dual-stack (GKE/AKS - zero downtime)

Dual-stack upgrades are seamless because existing IPv4 services continue working while IPv6 is added:

```yaml
# values-ipv6.yaml
network:
  ipFamily: 'dualstack'
```

```bash
helm upgrade gitguardian gitguardian/gitguardian \
  --namespace gitguardian \
  -f values.yaml \
  -f values-ipv6.yaml
```

#### To IPv6-only (requires planning)

:::caution Downtime required
Migrating to IPv6-only requires service disruption as IP addresses change.
:::

1. **Backup your data**
2. **Migrate PostgreSQL and Redis to IPv6**
3. **Update Helm values**:
   ```yaml
   network:
     ipFamily: 'ipv6'

   postgresql:
     host: '2001:db8::1234'  # New IPv6 address

   redis:
     main:
       host: '2001:db8::5678'  # New IPv6 address
   ```
4. **Deploy**:
   ```bash
   helm upgrade gitguardian gitguardian/gitguardian \
     --namespace gitguardian \
     -f values.yaml \
     -f values-ipv6.yaml
   ```
5. **Update DNS records** to AAAA records
6. **Test connectivity**

## Validation

After deployment, verify IPv6 is working:

### Check service IP addresses

```bash
kubectl get svc -n gitguardian -o wide
```

Services should show IPv6 addresses (e.g., `2001:db8:1234:5678::a`) or both IPv4 and IPv6 for dual-stack.

### Test connectivity

```bash
# Get service IP and test health endpoint
SERVICE_IP=$(kubectl get svc internal-api -n gitguardian -o jsonpath='{.spec.clusterIP}')
kubectl run test-ipv6 --rm -it --image=curlimages/curl -- \
  curl -v "http://[$SERVICE_IP]:5050/api/v1/health"
```

### Check application logs

```bash
kubectl logs -n gitguardian deployment/webapp-internal-api --tail=50
```

Look for Gunicorn binding to `[::]` and no connection errors to PostgreSQL/Redis.

## Troubleshooting

### Services not getting IPv6 addresses

**Symptoms**: Services show `<none>` or only IPv4 addresses

**Checklist**:
1. Verify cluster has IPv6 service CIDR: `kubectl cluster-info dump | grep -i service-cluster-ip-range`
2. Check `network.ipFamily` is set correctly in Helm values
3. For EKS, verify cluster was created with `ip_family = "ipv6"`

### PostgreSQL connection failures

**Symptoms**: `could not translate host name to address`

**Checklist**:
1. Test connectivity: `kubectl run test-pg --rm -it --image=postgres:16 -- psql -h 2001:db8::1234 -U gitguardian`
2. Verify DNS returns AAAA records (if using hostname)
3. Check PostgreSQL `listen_addresses` includes `::` 
4. Verify `pg_hba.conf` allows your IPv6 subnet

### Redis connection failures

**Symptoms**: `ConnectionError: Error connecting to Redis`

**Checklist**:
1. Test connectivity: `kubectl run test-redis --rm -it --image=redis:7 -- redis-cli -h 2001:db8::5678 PING`
2. Check Redis `bind` config includes `::`
3. Use correct URL format: `redis://[2001:db8::5678]:6379` (brackets required for IPv6)

### Nginx fails to start

**Symptoms**: `bind() to [::]:80 failed (99: Cannot assign requested address)`

**Solution**: Your cluster doesn't support IPv6. Verify CNI plugin supports IPv6 or use `network.ipFamily: 'ipv4'`.

### Application crashes with port parsing error

**Symptoms**: `'' is not a valid port number`

**Solution**: Don't set both `redis.main.url` and `redis.main.host`. Use one or the other:
- URL format: `redis.main.url: 'redis://[2001:db8::5678]:6379'`
- Or host/port: `redis.main.host: '2001:db8::5678'` with `redis.main.port: 6379`

### Loki fails to start or components can't communicate

**Symptoms**: `failed to join memberlist`, `no healthy instances in ring`, or `too many unhealthy instances in the ring`

**Solution**: Ensure the complete [Loki IPv6 configuration](#loki-ipv6-configuration) is applied. The most commonly missed setting is `extraMemberlistConfig.bind_addr: ['::']`.

After fixing configuration, restart Loki:
```bash
kubectl rollout restart deployment/loki-backend -n gitguardian
kubectl rollout restart statefulset/loki-write -n gitguardian
kubectl rollout restart statefulset/loki-read -n gitguardian
```

## Ingress and load balancers

### AWS Application Load Balancer (ALB)

```yaml
ingress:
  controller: aws_alb
  annotations:
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/ip-address-type: dualstack
    alb.ingress.kubernetes.io/target-type: ip
```

### Nginx Ingress Controller

```yaml
controller:
  service:
    ipFamilyPolicy: PreferDualStack
    ipFamilies: [IPv4, IPv6]
```

### Istio Gateway

```bash
kubectl patch svc istio-ingressgateway -n istio-system \
  -p '{"spec":{"ipFamilyPolicy":"PreferDualStack","ipFamilies":["IPv4","IPv6"]}}'
```

## Performance considerations

IPv6 has comparable performance to IPv4 with negligible latency difference. In IPv6-only clusters with NAT64/DNS64, expect ~5-10ms translation overhead when accessing IPv4-only external services.

## Security considerations

- **Firewall rules**: Add `ip6tables` rules alongside your `iptables` rules
- **Network policies**: Include IPv6 CIDRs in your Kubernetes NetworkPolicy `ipBlock` rules
- **TLS/SSL**: Works identically to IPv4 (same certificates, protocols, and cipher suites)

## Backward compatibility

All IPv6 changes are **100% backward compatible**. Existing IPv4 deployments continue working without changesâno Helm value changes or application code changes required unless you're enabling IPv6.

## Cost optimization

| Platform | Potential savings |
| --- | --- |
| **AWS EKS** | $40-100/month (no NAT Gateway or public IPv4 costs) |
| **GCP GKE** | Minimal impact (IPv6 addresses are free) |

## Additional resources

- [Kubernetes IPv6/Dual-stack Documentation](https://kubernetes.io/docs/concepts/services-networking/dual-stack/)
- [AWS EKS IPv6 Documentation](https://docs.aws.amazon.com/eks/latest/userguide/cni-ipv6.html)
- [GCP GKE IPv6 Documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#ipv6)
- [PostgreSQL IPv6 Configuration](https://www.postgresql.org/docs/current/runtime-config-connection.html)
- [Redis IPv6 Configuration](https://redis.io/docs/management/config/)

## Support

When reporting IPv6-related issues, please provide:

```bash
# Kubernetes version
kubectl version --short

# Cluster IP families
kubectl cluster-info dump | grep -i service-cluster-ip-range

# CNI plugin
kubectl get pods -n kube-system | grep -i cni

# Service configuration
kubectl get svc internal-api -n gitguardian -o yaml

# Pod logs
kubectl logs deployment/webapp-internal-api -n gitguardian --tail=100

# Helm values (redact sensitive information)
helm get values gitguardian -n gitguardian
```
