# Source: https://herd.laravel.com/docs/macos/migration-guides/mamp.md

# Migrating from MAMP

# How to migrate from MAMP to Herd

If you're currently using MAMP or MAMP Pro for your local PHP development and want to switch to Herd, this guide will
help you migrate your setup smoothly. Herd provides several advantages over MAMP, including:

* Deeply Integrated Laravel Support
* Advanced Web Development Debugging Tools
* Database Instance Management for MySQL, PostgreSQL, MongoDB and redis
* Additional Service Management for TypeSense, MeiliSearch, MinIO and Laravel Reverb
* First Party Laravel Forge Integration
* Native Xdebug Integration and Detection

## Before You Begin

Before starting the migration process, make sure you have:

1. A list of all your active MAMP sites
2. Database exports of all your databases
3. [Installed Herd](/macos/getting-started/installation)

## Exporting MAMP Databases

The first step is to export all your databases from MAMP. You can do this using phpMyAdmin that ships with MAMP or via the command line.

### Via phpMyAdmin

1. Open MAMP and start your servers
2. Navigate to phpMyAdmin (usually at [http://localhost:8888/phpMyAdmin](http://localhost:8888/phpMyAdmin))
3. Select each database you want to export
4. Click "Export" in the top menu
5. Choose "Quick" export method and "SQL" format
6. Click "Go" to download the SQL file

### Via Command Line

If you prefer using the command line, you can use the MySQL executable that ships with MAMP:

```bash  theme={null}
"/Applications/MAMP/Library/bin/mysqldump" -u root -p database_name > database_name.sql
```

## Setting Up Databases in Herd

After exporting your databases, you'll need to set them up in Herd. You have several options:

### Option 1: Herd Pro Services (Recommended)

If you're using [Herd Pro](/macos/herd-pro-services/services), you can install MySQL directly from the Services panel:

1. Open Herd settings
2. Go to the Services tab
3. Click the + button and select MySQL
4. Import your database dumps using TablePlus or AdminerEvo directly from the service panel

### Option 2: Standalone MySQL

If you're using the free version of Herd, you can:

1. Install MySQL separately via Homebrew or download it from mysql.com
2. Import your databases using the mysql command line tool:

```bash  theme={null}
mysql -u root database_name < database_name.sql
```

## Migrating Sites

### Step 1: Document Current Sites

First, make a list of your current MAMP sites and their document roots. In MAMP Pro, you can find these in the Hosts section of the application.

### Step 2: Set Up Herd Directory

Herd uses a central directory for serving sites. By default, this is `~/Herd`. You can also add additional [parked paths](/macos/getting-started/sites) in the settings.

### Step 3: Move Your Projects

1. Create your desired directory structure in your Herd directory
2. Move or copy your project files to this new location
3. Access your sites via their new `.test` domains automatically

For example, if your site was at:

```
/Applications/MAMP/htdocs/mysite
```

Move it to:

```
~/Herd/mysite
```

It will then be accessible at `http://mysite.test`

## Updating Configuration

### PHP Version

MAMP and Herd handle PHP versions differently. In Herd, you can:

1. Set a global PHP version via the menu bar or CLI:

```bash  theme={null}
herd use 8.2
```

2. [Set per-site PHP versions](/macos/technology/php-versions#per-site-php-versions) either through the Site Manager or CLI:

```bash  theme={null}
cd ~/Herd/mysite
herd isolate 8.1
```

### Database Connections

Update your database configuration in your applications. For Laravel applications, modify your `.env` file:

```env  theme={null}
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306 # Or the port you configured in Herd
DB_DATABASE=your_database
DB_USERNAME=root
DB_PASSWORD=
```

### Virtual Hosts

Unlike MAMP, Herd doesn't require manual virtual host configuration. Simply placing your project in a [parked directory](/macos/getting-started/sites) makes it accessible via its `.test` domain. If you need custom domains, you can use the `link` command:

```bash  theme={null}
cd ~/Herd/mysite
herd link custom-domain
```

### SSL Certificates

If you were using SSL certificates in MAMP, you can secure your sites in Herd with a single command:

```bash  theme={null}
cd ~/Herd/mysite
herd secure
```

This automatically generates and installs a trusted SSL certificate for your local domain.

## PHP Extensions

Herd includes most common PHP extensions by default. If you need additional extensions, check the [PHP Extensions](/macos/technology/php-extensions) documentation for installation instructions.

## Mail Testing

If you were using MAMP's built-in mail catching, Herd Pro offers an [improved mail testing feature](/macos/herd-pro-services/mail) that captures all outgoing emails and provides a modern interface for inspection.

## Troubleshooting

### Common Issues

1. **Database Connection Issues**: Ensure you're using the correct port for your database connection. If you're using Herd Pro's MySQL service, check the port in the Services panel.

2. **PHP Version Mismatch**: If your application requires a specific PHP version, use `herd isolate` to set the correct version for that project.

3. **Missing Extensions**: Check the [PHP Extensions](/macos/technology/php-extensions) documentation if you need to install additional extensions.

For more help, consult the [troubleshooting guide](/macos/troubleshooting/common-issues) or reach out to the [community support](/macos/troubleshooting/support).

## Final Steps

1. Test all your migrated sites and ensure they work as expected
2. Verify database connections and functionality
3. Test any special PHP configurations or requirements
4. Once everything is working, you can uninstall MAMP

After completing this migration, you'll have a faster, more modern development environment that's easier to maintain and better integrated with macOS.
