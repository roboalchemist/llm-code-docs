# Source: https://uptrace.dev/raw/get/hosted/ansible.md

# Deploying Uptrace with Ansible

> Automate Uptrace deployments on bare metal with the official Ansible playbooks, inventories, and role based setup.

This guide provides comprehensive instructions for deploying Uptrace, an open-source APM and observability platform, on bare metal servers using Ansible automation. Uptrace supports distributed tracing, metrics, and log management to help you monitor your applications effectively.

## What is Ansible?

Ansible is an open-source IT automation tool that enables configuration management, application deployment, infrastructure provisioning, and orchestration. It allows you to automate repetitive tasks, deploy software, and manage systems consistently and reliably across multiple servers.

## Prerequisites

Before proceeding with this guide, ensure you have:

1. **Ansible installed** on your control machine - Follow the [official installation guide](https://docs.ansible.com/ansible/latest/installation_guide/index.html)
2. **SSH access** to your target servers with sudo privileges
3. **Minimum server requirements**:

  - 2+ CPU cores
  - 4GB+ RAM
  - 20GB+ disk space
  - Ubuntu 24.04
4. **Network connectivity** between servers for cluster configurations

## Getting Started

### Clone the Ansible Repository

Uptrace maintains a comprehensive set of Ansible playbooks to deploy Uptrace with all required dependencies, including ClickHouse, PostgreSQL, and Redis:

```shell
git clone https://github.com/uptrace/ansible.git
cd ansible
```

### Understanding the Repository Structure

The repository contains several key components:

- **Playbooks**: Main deployment scripts (`.yml` files in the root directory)
- **Roles**: Reusable automation components for each service
- **Templates**: Configuration file templates
- **Inventory**: Server definitions and groupings
- **Group variables**: Shared configuration settings

## Inventory Configuration

### Understanding Ansible Inventory

An Ansible inventory is a file that defines the hosts (servers or nodes) that Ansible will manage and execute tasks on. It organizes your infrastructure into logical groups and defines variables for each host or group.

### Setting Up Your Inventory

1. **Copy the sample inventory file**:```shell
cp inventory.sample.yml inventory.yml
```
2. **Edit the inventory file** to include your server details.

### Inventory Best Practices

- Use descriptive hostnames or IP addresses
- Group related services together
- Consider network topology when assigning hosts
- Plan for high availability from the start

## Configuration Management

### Configuration File Locations

The configuration is distributed across several locations for modularity and maintainability:

- **group_vars/all.yml**: Main configuration file containing database passwords and basic Uptrace settings
- **roles/uptrace/templates/config.yml**: Advanced Uptrace configuration options
- **roles/clickhouse-server/templates/config.xml**: ClickHouse-specific configuration
- **Role-specific templates**: Each service role contains its own configuration templates

### Setting Up Main Configuration

1. **Copy the sample configuration**:```shell
cp group_vars/all.sample.yml group_vars/all.yml
```
2. **Update the configuration** with your specific requirements:
  - Database passwords
  - Network settings
  - Security configurations
  - Resource limits

### Configuration Security

- Use strong, unique passwords for all services
- Consider using Ansible Vault for sensitive data
- Regularly rotate credentials
- Implement proper firewall rules

## Deployment Process

### Step 1: Bootstrap Servers

Bootstrap your servers and install common software, including the OpenTelemetry Collector:

```shell
ansible-playbook -i inventory.yml bootstrap.yml
```

**What this does**:

- Updates system packages
- Installs essential tools and dependencies
- Configures basic security settings
- Sets up OpenTelemetry Collector

### Step 2: Deploy ClickHouse

ClickHouse stores all observability data including spans, logs, events, and metrics.

1. **Update ClickHouse variables** in `group_vars/all.yml`:```yaml
ch_cluster: uptrace1
ch_password: your_secure_password
ch_database: uptrace
```
2. **Deploy ClickHouse**:```shell
ansible-playbook -i inventory.yml ch_server.yml
```

#### High Availability ClickHouse Configuration

For production environments, configure multiple ClickHouse instances:

```yaml
clickhouse_server:
  hosts:
    10.10.1.1:
      ch_cluster: uptrace1
      ch_shard: shard1
      ch_replica: replica1
    10.10.1.2:
      ch_cluster: uptrace1
      ch_shard: shard1
      ch_replica: replica2
    10.10.1.3:
      ch_cluster: uptrace1
      ch_shard: shard2
      ch_replica: replica1
    10.10.1.4:
      ch_cluster: uptrace1
      ch_shard: shard2
      ch_replica: replica2
```

**Important**: When adding new replicas to an existing ClickHouse cluster, you must manually configure [ClickHouse replication](https://kb.altinity.com/altinity-kb-setup-and-maintenance/altinity-kb-data-migration/add_remove_replica/) on the new replica.

### Step 3: Deploy PostgreSQL

PostgreSQL stores metadata such as users, projects, and monitor configurations.

1. **Update PostgreSQL variables** in `group_vars/all.yml`:```yaml
pg_database: uptrace
pg_user: uptrace
pg_password: your_secure_password
```
2. **Deploy PostgreSQL**:```shell
ansible-playbook -i inventory.yml pg.yml
```

#### High Availability PostgreSQL Configuration

Configure primary-standby replication for high availability:

```yaml
postgresql:
  hosts:
    10.10.1.1: # Primary server
    10.10.1.2: # Standby server
      pg_primary_host: 10.10.1.1
```

**Note**: You must manually set up PostgreSQL replication between the standby and primary servers. This typically involves:

1. Creating a base backup on the primary server
2. Restoring the backup on the standby server
3. Configuring streaming replication

### Step 4: Deploy Redis

Redis provides in-memory caching for improved performance.

**Deploy Redis**:

```shell
ansible-playbook -i inventory.yml redis.yml
```

#### High Availability Redis Configuration

Configure multiple Redis instances for redundancy:

```yaml
redis_cache:
  hosts:
    10.10.1.1:
      redis_node_id: alpha
      redis_maxmemory_mb: 256
    10.10.1.2:
      redis_node_id: bravo
      redis_maxmemory_mb: 256
    10.10.1.3:
      redis_node_id: charlie
      redis_maxmemory_mb: 256
```

**Note**: Each Redis node operates independently, so no replication setup is required. Uptrace handles node selection automatically.

### Step 5: Deploy Uptrace

With all dependencies in place, deploy the main Uptrace application:

```shell
ansible-playbook -i inventory.yml uptrace.yml
```

#### Verification

Check that Uptrace is running correctly:

```shell
# View Uptrace logs
sudo journalctl -u uptrace -f

# Check service status
sudo systemctl status uptrace

# Test connectivity
curl -f http://localhost:80/api/v1/health
```

## SSL/TLS Configuration with Let's Encrypt

### Prerequisites for Let's Encrypt

Let's Encrypt uses HTTP challenge for domain verification. Ensure:

1. **Domain resolution**: Your domain must be publicly resolvable:```shell
nslookup your-domain.com
```
2. **Port accessibility**: Ports 80 and 443 must be accessible from the internet

### Configure Let's Encrypt

Update your `group_vars/all.yml` file:

```yaml
# Domain for SSL certificate
site_url: https://your-domain.com/

# Enable Let's Encrypt
certmagic_enabled: true

# Use staging environment for testing (disable for production)
certmagic_staging_ca: true

# Listen on HTTPS port
listen_http_addr: ':443'
```

### Testing SSL Configuration

1. **Test with staging environment** first (set `certmagic_staging_ca: true`)
2. **Verify certificate issuance** in logs
3. **Switch to production** (set `certmagic_staging_ca: false`)
4. **Redeploy** to get production certificate

## Optional Components

### Mailhog for Email Testing

Deploy Mailhog to capture and view emails sent by Uptrace during development:

```shell
ansible-playbook -i inventory.yml mailhog.yml
```

Access Mailhog web interface at [http://localhost:8025](http://localhost:8025).

**Production Note**: Disable Mailhog in production environments and configure proper SMTP settings.

## Scaling and Maintenance

### Horizontal Scaling

#### Scaling Uptrace Application

Add additional Uptrace instances for load distribution:

```yaml
uptrace:
  hosts:
    10.10.1.1:
    10.10.1.2:
    10.10.1.3:
```

Redeploy after updating inventory:

```shell
ansible-playbook -i inventory.yml uptrace.yml
```

#### Scaling ClickHouse

Scale ClickHouse by adding [shards and replicas](https://clickhouse.com/docs/architecture/horizontal-scaling):

```yaml
clickhouse_server:
  hosts:
    # Shard 1
    10.10.1.1: { ch_cluster: uptrace1, ch_shard: shard1, ch_replica: replica1 }
    10.10.1.2: { ch_cluster: uptrace1, ch_shard: shard1, ch_replica: replica2 }
    # Shard 2
    10.10.1.3: { ch_cluster: uptrace1, ch_shard: shard2, ch_replica: replica1 }
    10.10.1.4: { ch_cluster: uptrace1, ch_shard: shard2, ch_replica: replica2 }
```

## Troubleshooting

### Common Issues and Solutions

#### Connection Issues

**Problem**: Ansible cannot connect to hosts

**Solution**:

```shell
# Test connectivity
ansible all -i inventory.yml -m ping

# Check SSH access
ssh user@host-ip

# Verify inventory syntax
ansible-inventory -i inventory.yml --list
```

#### Service Failures

**Problem**: Services fail to start

**Solution**:

```shell
# Check service status
ansible all -i inventory.yml -m systemd -a "name=uptrace state=status"

# View logs
ansible all -i inventory.yml -m shell -a "journalctl -u uptrace -n 50"

# Check disk space
ansible all -i inventory.yml -m shell -a "df -h"
```

#### Performance Issues

**Problem**: Slow query performance

**Solutions**:

- Increase ClickHouse memory allocation
- Add more ClickHouse replicas
- Optimize query patterns
- Review resource utilization

### Diagnostic Commands

```shell
# Check all services status
ansible all -i inventory.yml -m shell -a "systemctl status uptrace clickhouse-server postgresql redis"

# Monitor resource usage
ansible all -i inventory.yml -m shell -a "top -n 1 -b"

# Check network connectivity between services
ansible all -i inventory.yml -m shell -a "netstat -tlnp"

# Verify configuration files
ansible all -i inventory.yml -m shell -a "nginx -t" # if using nginx
```

## Security Considerations

### Network Security

- Configure firewalls to allow only necessary ports
- Use VPN or private networks for inter-service communication
- Implement proper network segmentation

### Access Control

- Use SSH key authentication instead of passwords
- Implement role-based access control
- Regularly audit user access

### Data Protection

- Encrypt sensitive data at rest
- Use TLS for all network communications
- Implement proper backup encryption

## Best Practices

### Infrastructure Management

1. **Use version control** for all configuration files
2. **Test changes** in a staging environment first
3. **Implement monitoring** for all services
4. **Document custom configurations** and procedures
5. **Plan for disaster recovery** scenarios

### Configuration Management

1. **Use Ansible Vault** for sensitive data
2. **Implement configuration validation** before deployment
3. **Maintain environment-specific configurations**
4. **Use meaningful variable names** and comments

### Operational Excellence

1. **Automate routine tasks** with additional playbooks
2. **Implement health checks** and monitoring
3. **Create runbooks** for common scenarios
4. **Establish maintenance windows** for updates

## Upgrading Uptrace

Only upgrades to the next minor version are tested and supported, for example, upgrading from 1.1 to 1.2. Skipping minor versions (e.g., 1.1 to 1.3) is not supported â upgrade one minor version at a time.

To upgrade Uptrace:

1. **Back up your databases.** Create backups of both PostgreSQL and ClickHouse before proceeding.
2. **Re-run the Uptrace playbook:**```shell
ansible-playbook -i inventory.yml uptrace.yml
```

The playbook automatically installs the new version, validates the config, runs database migrations, and restarts Uptrace.

## Alternative Deployment Methods

Ansible is one of several deployment options for Uptrace:

- [Docker](/get/hosted/docker) - Quick deployment for development and small-scale production
- [DEB/RPM packages](/get/hosted/install) - Traditional server deployments
- [Kubernetes](/get/hosted/k8s) - Container orchestration at scale

Choose the method that best fits your infrastructure and requirements.

## Next Steps

After successful deployment:

1. **Configure your applications** to send telemetry data to Uptrace
2. **Set up monitoring dashboards** for your services
3. **Create alerting rules** for critical metrics
4. **Implement log aggregation** for better observability
5. **Explore advanced features** like distributed tracing and custom metrics
