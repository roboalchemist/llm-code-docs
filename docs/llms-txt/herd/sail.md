# Source: https://herd.laravel.com/docs/macos/migration-guides/sail.md

# Migrating from Sail

# How to migrate from Laravel Sail to Herd

If you're currently using Laravel Sail for local development and want to switch to Herd, this guide will walk you through the migration process. While both tools provide excellent development environments, they have different approaches to managing services and dependencies.

## Understanding the Differences

Laravel Sail uses Docker containers to provide isolated development environments, while Herd takes a native approach by running services directly on your machine. Here are the key differences:

<CardGroup cols={2}>
  <Card title="Laravel Sail" icon="docker">
    * Uses Docker containers
    * Requires Docker Desktop
    * Services defined in docker-compose.yml
    * Container-based isolation
  </Card>

  <Card title="Herd" icon="elephant">
    * Uses native services
    * No Docker required
    * Services managed via Herd UI/CLI
    * Native performance
  </Card>
</CardGroup>

## Migration Steps

### 1. Stop Sail Services

Before switching to Herd, make sure to stop all running Sail containers:

```bash  theme={null}
./vendor/bin/sail down
```

### 2. Install Herd

Download and install Herd from the [official website](https://herd.laravel.com). Follow the [installation instructions](/macos/getting-started/installation) to get Herd up and running on your machine.

### 3. Update Environment Configuration

Your `.env` file likely contains Docker-specific configurations. Here's how to update common settings:

#### Database Configuration

If you're using MySQL:

```env  theme={null}
# From Sail
DB_HOST=mysql
DB_PORT=3306

# To Herd
DB_HOST=127.0.0.1
DB_PORT=3306 # Default Herd MySQL port
```

#### Redis Configuration

If you're using Redis:

```env  theme={null}
# From Sail
REDIS_HOST=redis

# To Herd
REDIS_HOST=127.0.0.1
```

#### Mail Configuration

If you're using Mailhog with Sail, switch to Herd's mail service:

```env  theme={null}
# From Sail
MAIL_HOST=mailhog
MAIL_PORT=1025

# To Herd
MAIL_MAILER=smtp
MAIL_HOST=127.0.0.1
MAIL_PORT=2525
MAIL_USERNAME=${APP_NAME}
MAIL_PASSWORD=null
MAIL_ENCRYPTION=null
```

### 4. Set Up Required Services

<Note>
  If you're using [Herd Pro](https://herd.laravel.com/checkout), you can install services directly from the Herd UI. The free version requires manual installation of additional services.
</Note>

Review your `docker-compose.yml` file to identify which services your application needs. Common services include:

* Database (MySQL/PostgreSQL)
* Redis
* Meilisearch

For Herd Pro users, you can install these services via the Services tab in settings. Free version users should install these services separately.

### 5. Remove Sail Dependencies

You can now remove Sail from your project:

```bash  theme={null}
composer remove laravel/sail --dev
```

Also, clean up Sail-related files:

* `docker-compose.yml`
* `docker/` directory
* Any custom Dockerfile configurations

### 6. Update Development Scripts

Update your `composer.json` scripts section to remove Sail commands. For example:

```json  theme={null}
{
    "scripts": {
        // Remove these Sail-based scripts
        "sail:up": "./vendor/bin/sail up -d",
        "sail:down": "./vendor/bin/sail down"
    }
}
```

### 7. Create Herd Configuration (optional)

Create a `herd.yml` file in your project root to define project-specific configurations either manually or by running `herd init`:

```yaml  theme={null}
name: your-project-name
php: '8.3'
services:
    mysql:
        version: 8.0.36
        port: '${DB_PORT}'
    redis:
        version: 7.0.0
        port: '${REDIS_PORT}'
```

### 8. Initialize the Project

Initialize your project with Herd:

```bash  theme={null}
herd init
```

This command will configure your project according to the `herd.yml` file and set up any required services.

## Common Challenges

### Database Migration

If you need to migrate your data from Sail's MySQL container:

1. Export your database from Sail:

```bash  theme={null}
./vendor/bin/sail mysql --execute="SHOW DATABASES" > databases.txt
./vendor/bin/sail mysqldump your_database > database_backup.sql
```

2. Import into Herd's MySQL:

```bash  theme={null}
mysql -u root -P 3306 -h 127.0.0.1 -e "CREATE DATABASE your_database_name;"
mysql -u root -P 3306 -h 127.0.0.1 your_database_name < database_backup.sql
```

### File Permissions

Since Herd runs services natively rather than in containers, you might need to adjust file permissions:

```bash  theme={null}
chmod -R 755 storage bootstrap/cache
```

## Using Herd in a Team

When working with a team, make sure to:

1. Share your `herd.yml` configuration file via version control
2. Document any specific service requirements
3. Standardize PHP versions across the team

## Getting Help

If you encounter issues during migration:

1. Check the [troubleshooting guides](/macos/troubleshooting/common-issues)
2. Join the [community support](/macos/troubleshooting/support)

[Herd Pro](https://herd.laravel.com/checkout) users can also access priority email support for migration assistance.
