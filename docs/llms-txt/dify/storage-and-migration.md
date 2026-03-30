# Source: https://docs.dify.ai/en/self-host/troubleshooting/storage-and-migration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Storage & Migration

## Vector Database Migration

### Migrate from Weaviate to another database

1. **Update configuration**

   Source code deployment (`.env`):

   ```
   VECTOR_STORE=qdrant
   ```

   Docker Compose (`docker-compose.yaml`):

   ```yaml  theme={null}
   VECTOR_STORE: qdrant
   ```

2. **Run migration**

   ```bash  theme={null}
   # Source code
   flask vdb-migrate

   # Docker
   docker exec -it docker-api-1 flask vdb-migrate
   ```

Tested databases: Qdrant, Milvus, AnalyticDB

## Storage Migration

### Move from local to cloud storage

Migrate files from local storage to cloud providers (e.g., Alibaba Cloud OSS):

1. **Configure cloud storage**

   `.env` or `docker-compose.yaml`:

   ```
   STORAGE_TYPE=aliyun-oss
   # Add OSS credentials
   ```

2. **Migrate data**

   Source code:

   ```bash  theme={null}
   flask upload-private-key-file-to-cloud-storage
   flask upload-local-files-to-cloud-storage
   ```

   Docker:

   ```bash  theme={null}
   docker exec -it docker-api-1 flask upload-private-key-file-to-cloud-storage
   docker exec -it docker-api-1 flask upload-local-files-to-cloud-storage
   ```

## Data Cleanup

### Delete old logs

1. **Get tenant ID**
   ```bash  theme={null}
   docker exec -it docker-api-1 bash -c "echo 'from models import Tenant; db.session.query(Tenant.id, Tenant.name).all(); quit()' | flask shell"
   ```

2. **Delete logs older than X days**
   ```bash  theme={null}
   docker exec -it docker-api-1 flask clear-free-plan-tenant-expired-logs \
     --days 30 \
     --batch 100 \
     --tenant_ids 618b5d66-a1f5-4b6b-8d12-f171182a1cb2
   ```

3. **Remove exported logs** (optional)
   ```bash  theme={null}
   docker exec -it docker-api-1 bash -c 'rm -rf ${OPENDAL_FS_ROOT}/free_plan_tenant_expired_logs'
   ```

### Remove orphaned files

**Warning**: Back up database and storage before running. Run during maintenance window.

1. **Clean database records**
   ```bash  theme={null}
   docker exec -it docker-api-1 flask clear-orphaned-file-records
   # Use -f flag to skip confirmation
   ```

2. **Delete orphaned files from storage**
   ```bash  theme={null}
   docker exec -it docker-api-1 flask remove-orphaned-files-on-storage
   # Use -f flag to skip confirmation
   ```

Note: Only works with OpenDAL storage (`STORAGE_TYPE=opendal`).

## Backup & Recovery

### Create backup before upgrade

```bash  theme={null}
cp -r dify "dify.bak.$(date +%Y%m%d%H%M%S)"
```

### What to backup

For Docker Compose deployments:

* Entire `dify/docker/volumes` directory

For source deployments:

* Database
* Storage configuration
* Vector database data
* Environment files

### Database maintenance

After deleting logs, reclaim storage:

PostgreSQL:

```sql  theme={null}
VACUUM FULL;
```

## Upgrade Process

### Version upgrade

Image deployment:

```bash  theme={null}
docker compose pull
docker compose up -d
```

Source code:

```bash  theme={null}
git pull
cd api
flask db upgrade
```

### Database schema migration

Always required for source code updates:

```bash  theme={null}
cd api
flask db upgrade
```


Built with [Mintlify](https://mintlify.com).