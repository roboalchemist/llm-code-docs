# Source: https://symfony.com/doc/8.0/cloud/index.html

Title: Deploy Symfony on Upsun

URL Source: https://symfony.com/doc/8.0/cloud/index.html

Published Time: Thu, 05 Mar 2026 10:46:12 GMT

Markdown Content:
Deploy Symfony on Upsun | Upsun Docs
===============

 Platform.sh is now Upsun. [Click here to learn more](https://upsun.com/platform-sh-is-now-upsun/)

[![Image 1: Upsun User Documentation](https://symfony.com/images/logo.svg)](https://symfony.com/)

[Log in](https://console.upsun.com/)[Sign up](https://upsun.com/register/)

Site navigation
---------------

### Get started

#### [Introduction](https://symfony.com/get-started/here.html)

* [Setup](https://symfony.com/get-started/here/setup.html)
* [Create a project](https://symfony.com/get-started/here/create-project.html)
* [Configure your project](https://symfony.com/get-started/here/configure.html)
  * [JavaScript/Node.js](https://symfony.com/get-started/here/configure/nodejs.html)
  * [PHP](https://symfony.com/get-started/here/configure/php.html)
  * [Python](https://symfony.com/get-started/here/configure/python.html)

* [Set resources](https://symfony.com/get-started/here/set-resources.html)
* [Revisions](https://symfony.com/get-started/here/make-changes.html)
* [Local development](https://symfony.com/get-started/here/local.html)
  * [Tethered](https://symfony.com/get-started/here/local/tethered.html)

* [Third party integrations](https://symfony.com/get-started/here/third-party.html)
* [Get support](https://symfony.com/get-started/here/support.html)

#### [How to deploy](https://symfony.com/get-started/stacks.html)

##### Javascript/Node.js

* [Express](https://symfony.com/get-started/stacks/express.html)
  * [Add a database to Express](https://symfony.com/get-started/stacks/express/add-database.html)

* [Next.js](https://symfony.com/get-started/stacks/nextjs.html)
* [Strapi](https://symfony.com/get-started/stacks/strapi.html)
  * [Add a database to Strapi](https://symfony.com/get-started/stacks/strapi/add-database.html)

##### Python

* [Django](https://symfony.com/get-started/stacks/django.html)
* [Flask](https://symfony.com/get-started/stacks/flask.html)

##### PHP

* [Drupal](https://symfony.com/get-started/stacks/drupal.html)
* [Laravel](https://symfony.com/get-started/stacks/laravel.html)
  * [Get started](https://symfony.com/get-started/stacks/laravel/get-started.html)
  * [Environment variables](https://symfony.com/get-started/stacks/laravel/environment-variables.html)
  * [Set up Redis](https://symfony.com/get-started/stacks/laravel/setup-redis.html)
  * [Handle queues with Horizon](https://symfony.com/get-started/stacks/laravel/laravel-horizon.html)
  * [Cron jobs](https://symfony.com/get-started/stacks/laravel/crons.html)
  * [Blackfire](https://symfony.com/get-started/stacks/laravel/blackfire.html)
  * [Debug with Laravel Telescope](https://symfony.com/get-started/stacks/laravel/laravel-telescope.html)
  * [FAQ](https://symfony.com/get-started/stacks/laravel/faq.html)

* [Magento](https://symfony.com/get-started/stacks/magento.html)
* [Symfony Partner](https://symfony.com/get-started/stacks/symfony.html)
  * [Get started](https://symfony.com/get-started/stacks/symfony/get-started.html)
  * [Symfony integration](https://symfony.com/get-started/stacks/symfony/integration.html)
  * [Environment variables](https://symfony.com/get-started/stacks/symfony/environment-variables.html)
  * [Workers](https://symfony.com/get-started/stacks/symfony/workers.html)
  * [Cron jobs](https://symfony.com/get-started/stacks/symfony/crons.html)
  * [Blackfire](https://symfony.com/get-started/stacks/symfony/blackfire.html)
  * [Local development](https://symfony.com/get-started/stacks/symfony/local.html)
  * [FAQ](https://symfony.com/get-started/stacks/symfony/faq.html)
  * [Symfony CLI Tips](https://symfony.com/get-started/stacks/symfony/symfony-cli-tips.html)

* [WordPress](https://symfony.com/get-started/stacks/wordpress.html)
  * [Composer WordPress](https://symfony.com/get-started/stacks/wordpress/composer.html)
  * [WordPress Multisite](https://symfony.com/get-started/stacks/wordpress/multisite.html)
  * [Bedrock WordPress](https://symfony.com/get-started/stacks/wordpress/bedrock.html)
  * [Vanilla WordPress](https://symfony.com/get-started/stacks/wordpress/vanilla.html)

* [Pimcore PaaS Partner](https://symfony.com/get-started/stacks/pimcore.html)
* [Shopware PaaS Partner](https://symfony.com/get-started/stacks/shopware.html)

#### [How to deploy AI](https://symfony.com/get-started/ai.html)

* [Host AI Agents](https://symfony.com/get-started/ai/aiagent.html)
* [Hosting Model Context Protocal (MCP) Servers](https://symfony.com/get-started/ai/deploy-mcp.html)
* [The Upsun MCP Server New](https://symfony.com/get-started/ai/using-the-mcp.html)

### Learn

#### [What is Upsun?](https://symfony.com/learn/overview.html)

* [Philosophy](https://symfony.com/learn/overview/philosophy.html)
* [YAML](https://symfony.com/learn/overview/yaml.html)
  * [What YAML is](https://symfony.com/learn/overview/yaml/what-is-yaml.html)
  * [Upsun YAML structure](https://symfony.com/learn/overview/yaml/yaml-structure.html)
  * [Upsun YAML tags](https://symfony.com/learn/overview/yaml/platform-yaml-tags.html)

* [Structure](https://symfony.com/learn/overview/structure.html)
* [Build and deploy](https://symfony.com/learn/overview/build-deploy.html)
* [Get support](https://symfony.com/learn/overview/get-support.html)

#### [Tutorials](https://symfony.com/learn/tutorials.html)

* [Convert to Upsun](https://symfony.com/learn/tutorials/migrating.html)
  * [Converting from Upsun Fixed (formerly Platform.sh)](https://symfony.com/learn/tutorials/migrating/from-fixed.html)

* [Automate your code updates](https://symfony.com/learn/tutorials/dependency-updates.html)
* [Restrict service access](https://symfony.com/learn/tutorials/restrict-service-access.html)
* [Exporting data](https://symfony.com/learn/tutorials/exporting.html)

#### [Best practices](https://symfony.com/learn/bestpractices.html)

* [HTTP caching](https://symfony.com/learn/bestpractices/http-caching.html)
* [Monolith, headless or microservices?](https://symfony.com/learn/bestpractices/oneormany.html)
* [Keep your Git repository clean](https://symfony.com/learn/bestpractices/clean-repository.html)

### Reference

#### [Configure apps](https://symfony.com/create-apps.html)

* [Choose an image type](https://symfony.com/create-apps/app-reference.html)
  * [Single-runtime image](https://symfony.com/create-apps/app-reference/single-runtime-image.html)
  * [Composable image](https://symfony.com/create-apps/app-reference/composable-image.html)

* [Image properties](https://symfony.com/create-apps/image-properties.html)
  * [access](https://symfony.com/create-apps/image-properties/access.html)
  * [additional_hosts](https://symfony.com/create-apps/image-properties/additional_hosts.html)
  * [container_profile](https://symfony.com/create-apps/image-properties/container_profile.html)
  * [crons](https://symfony.com/create-apps/image-properties/crons.html)
  * [firewall](https://symfony.com/create-apps/image-properties/firewall.html)
  * [hooks](https://symfony.com/create-apps/image-properties/hooks.html)
  * [mounts](https://symfony.com/create-apps/image-properties/mounts.html)
  * [relationships](https://symfony.com/create-apps/image-properties/relationships.html)
  * [source](https://symfony.com/create-apps/image-properties/source.html)
  * [variables](https://symfony.com/create-apps/image-properties/variables.html)
  * [web](https://symfony.com/create-apps/image-properties/web.html)
  * [workers](https://symfony.com/create-apps/image-properties/workers.html)

* [Source operations](https://symfony.com/create-apps/source-operations.html)
* [Runtime operations](https://symfony.com/create-apps/runtime-operations.html)
* [Configure what’s served](https://symfony.com/create-apps/web.html)
  * [PHP with front controller](https://symfony.com/create-apps/web/php-basic.html)
  * [Rewrite requests](https://symfony.com/create-apps/web/rewrite-requests.html)
  * [Serve different paths](https://symfony.com/create-apps/web/serve-different-directories.html)
  * [Static sites](https://symfony.com/create-apps/web/static.html)
  * [Custom headers](https://symfony.com/create-apps/web/custom-headers.html)

* [Multiple apps](https://symfony.com/create-apps/multi-app.html)
  * [Choose a project structure](https://symfony.com/create-apps/multi-app/project-structure.html)
  * [Define routes](https://symfony.com/create-apps/multi-app/routes.html)
  * [Define relationships](https://symfony.com/create-apps/multi-app/relationships.html)

* [Timezones](https://symfony.com/create-apps/timezone.html)
* [Troubleshoot disks](https://symfony.com/create-apps/troubleshoot-disks.html)
* [Troubleshoot mounts](https://symfony.com/create-apps/troubleshoot-mounts.html)
* [Use build and deploy hooks](https://symfony.com/create-apps/hooks.html)
  * [Change hooks in different environments](https://symfony.com/create-apps/hooks/vary-hooks-by-environment.html)
  * [Comparison of hooks](https://symfony.com/create-apps/hooks/hooks-comparison.html)
  * [Use hooks with dependencies](https://symfony.com/create-apps/hooks/hooks-and-dependencies.html)

* [Work with workers](https://symfony.com/create-apps/workers.html)

#### [Add services](https://symfony.com/add-services.html)

* [Chroma](https://symfony.com/add-services/chroma.html)
* [ClickHouse](https://symfony.com/add-services/clickhouse.html)
* [Elasticsearch Premium](https://symfony.com/add-services/elasticsearch.html)
* [Edgee (Edge Analytics) Partner](https://symfony.com/add-services/edgee.html)
* [Gotenberg](https://symfony.com/add-services/gotenberg.html)
* [Headless Chrome](https://symfony.com/add-services/headless-chrome.html)
* [InfluxDB](https://symfony.com/add-services/influxdb.html)
* [Kafka](https://symfony.com/add-services/kafka.html)
* [MariaDB/MySQL](https://symfony.com/add-services/mysql.html)
  * [MariaDB read-only replication](https://symfony.com/add-services/mysql/mysql-readonly-replication.html)
  * [External replication](https://symfony.com/add-services/mysql/mysql-replication.html)
  * [Troubleshoot](https://symfony.com/add-services/mysql/troubleshoot.html)

* [Memcached](https://symfony.com/add-services/memcached.html)
* [Mercure](https://symfony.com/add-services/mercure.html)
* [MongoDB Premium](https://symfony.com/add-services/mongodb.html)
* [Network Storage](https://symfony.com/add-services/network-storage.html)
* [OpenSearch](https://symfony.com/add-services/opensearch.html)
* [PostgreSQL](https://symfony.com/add-services/postgresql.html)
  * [Read-only replication](https://symfony.com/add-services/postgresql/postgresql-readonly-replication.html)

* [Qdrant](https://symfony.com/add-services/qdrant.html)
* [RabbitMQ](https://symfony.com/add-services/rabbitmq.html)
* [Redis](https://symfony.com/add-services/redis.html)
* [Solr](https://symfony.com/add-services/solr.html)
* [Valkey](https://symfony.com/add-services/valkey.html)
* [Varnish](https://symfony.com/add-services/varnish.html)
* [Vault KMS](https://symfony.com/add-services/vault.html)

#### [Define routes](https://symfony.com/define-routes.html)

* [Server Side Includes (SSI)](https://symfony.com/define-routes/ssi.html)
* [HTTP cache](https://symfony.com/define-routes/cache.html)
* [HTTPS](https://symfony.com/define-routes/https.html)
* [Proxy routes](https://symfony.com/define-routes/proxy.html)
* [Redirects](https://symfony.com/define-routes/redirects.html)

#### [Manage resources](https://symfony.com/manage-resources.html)

* [How resources work on Upsun](https://symfony.com/manage-resources/how-resources-work.html)
* [Resource initialization](https://symfony.com/manage-resources/resource-init.html)
* [Resource configuration](https://symfony.com/manage-resources/adjust-resources.html)
* [Autoscaling](https://symfony.com/manage-resources/autoscaling.html)
* [Guaranteed resources](https://symfony.com/manage-resources/guaranteed-resources.html)
* [Project build resources](https://symfony.com/manage-resources/build-resources.html)

#### [Languages](https://symfony.com/languages.html)

* [C#/.NET Core](https://symfony.com/languages/dotnet.html)
* [Elixir](https://symfony.com/languages/elixir.html)
* [Go](https://symfony.com/languages/go.html)
* [Java](https://symfony.com/languages/java.html)
  * [Moving to Upsun](https://symfony.com/languages/java/migration.html)
  * [Tuning](https://symfony.com/languages/java/tuning.html)

* [JavaScript/Node.js](https://symfony.com/languages/nodejs.html)
  * [Debugging](https://symfony.com/languages/nodejs/debug.html)
  * [Manage Node.js versions](https://symfony.com/languages/nodejs/node-version.html)

* [PHP](https://symfony.com/languages/php.html)
  * [Extensions](https://symfony.com/languages/php/extensions.html)
  * [PHP performance tuning](https://symfony.com/languages/php/tuning.html)
  * [PHP-FPM sizing](https://symfony.com/languages/php/fpm.html)
  * [FrankenPHP](https://symfony.com/languages/php/frankenphp.html)
  * [Xdebug](https://symfony.com/languages/php/xdebug.html)
  * [Custom Redis](https://symfony.com/languages/php/redis.html)
  * [Swoole](https://symfony.com/languages/php/swoole.html)
  * [Authenticated Composer](https://symfony.com/languages/php/composer-auth.html)
  * [Troubleshoot](https://symfony.com/languages/php/troubleshoot.html)

* [Python](https://symfony.com/languages/python.html)
  * [Manage dependencies](https://symfony.com/languages/python/dependencies.html)
  * [Web servers](https://symfony.com/languages/python/server.html)
  * [Python in non-Python containers](https://symfony.com/languages/python/python-version.html)

* [Ruby](https://symfony.com/languages/ruby.html)
* [Rust](https://symfony.com/languages/rust.html)

#### [Development](https://symfony.com/development.html)

* [Local development](https://symfony.com/development/local.html)

##### Integrated environments

    *   [DDEV](https://symfony.com/development/local/ddev.html)
    
##### Supported environments

    *   [Tethered](https://symfony.com/development/local/tethered.html)
    *   [Untethered](https://symfony.com/development/local/untethered.html)

* [Variables overview](https://symfony.com/development/variables.html)
  * [Set variables](https://symfony.com/development/variables/set-variables.html)
  * [Use variables](https://symfony.com/development/variables/use-variables.html)

* [Access your site](https://symfony.com/development/access-site.html)
* [Transfer files](https://symfony.com/development/file-transfer.html)
* [Headers](https://symfony.com/development/headers.html)
* [Email](https://symfony.com/development/email.html)
* [Private repositories](https://symfony.com/development/private-repository.html)
* [Git submodules](https://symfony.com/development/submodules.html)
* [Connect with SSH](https://symfony.com/development/ssh.html)
  * [SSH keys](https://symfony.com/development/ssh/ssh-keys.html)
  * [Troubleshoot SSH](https://symfony.com/development/ssh/troubleshoot-ssh.html)

* [Regions](https://symfony.com/development/regions.html)
* [502 error resolutions](https://symfony.com/development/502-errors.html)
* [Troubleshoot](https://symfony.com/development/troubleshoot.html)
* [Sanitize databases](https://symfony.com/development/sanitize-db.html)
  * [MariaDB and Drupal](https://symfony.com/development/sanitize-db/mariadb.html)
  * [PostgreSQL and Django](https://symfony.com/development/sanitize-db/postgresql.html)
  * [PostgreSQL and Symfony](https://symfony.com/development/sanitize-db/postgresql-symfony.html)

#### [Integrations](https://symfony.com/integrations.html)

* [Overview](https://symfony.com/integrations/overview.html)
* [Activity scripts](https://symfony.com/integrations/activity.html)
  * [Activity reference](https://symfony.com/integrations/activity/reference.html)
  * [Utility routines](https://symfony.com/integrations/activity/utility.html)
  * [Example: Discord](https://symfony.com/integrations/activity/discord.html)
  * [Example: Slack](https://symfony.com/integrations/activity/slack.html)
  * [Webhooks](https://symfony.com/integrations/activity/webhooks.html)

* [Source integrations](https://symfony.com/integrations/source.html)
  * [Bitbucket](https://symfony.com/integrations/source/bitbucket.html)
  * [GitHub](https://symfony.com/integrations/source/github.html)
  * [GitLab](https://symfony.com/integrations/source/gitlab.html)
  * [Resolve access](https://symfony.com/integrations/source/troubleshoot.html)

* [Fastly CDN](https://symfony.com/integrations/fastly-cdn.html)
* [Health notifications](https://symfony.com/integrations/notifications.html)

#### [Increase observability](https://symfony.com/increase-observability.html)

* [Infrastructure metrics](https://symfony.com/increase-observability/metrics.html)
  * [HTTP metrics](https://symfony.com/increase-observability/metrics/http-metrics.html)
  * [Understand metrics](https://symfony.com/increase-observability/metrics/understand-metrics.html)

* [Application metrics](https://symfony.com/increase-observability/application-metrics.html)
  * [Monitor Cron job executions](https://symfony.com/increase-observability/application-metrics/cron-metrics.html)
  * [Understanding application observablity](https://symfony.com/increase-observability/application-metrics/understanding.html)
  * [Blackfire for PHP and Python](https://symfony.com/increase-observability/application-metrics/blackfire.html)
  * [Comparing Continuous Profiling Timeframes](https://symfony.com/increase-observability/application-metrics/cont-prof-comparison.html)
  * [Continuous Profiling dashboard](https://symfony.com/increase-observability/application-metrics/cont-prof.html)
  * [Go continuous profiler](https://symfony.com/increase-observability/application-metrics/go.html)
  * [Java continuous profiler](https://symfony.com/increase-observability/application-metrics/java.html)
  * [Node.js continuous profiler](https://symfony.com/increase-observability/application-metrics/nodejs.html)
  * [PHP continuous profiler](https://symfony.com/increase-observability/application-metrics/php.html)
  * [Python continuous profiler](https://symfony.com/increase-observability/application-metrics/python.html)
  * [Ruby continuous profiler](https://symfony.com/increase-observability/application-metrics/ruby.html)
  * [Rust continuous profiler](https://symfony.com/increase-observability/application-metrics/rust.html)

* [Consume logs](https://symfony.com/increase-observability/logs.html)
  * [Access logs](https://symfony.com/increase-observability/logs/access-logs.html)
  * [Forward Upsun and Blackfire logs](https://symfony.com/increase-observability/logs/forward-logs.html)

#### [Manage environments](https://symfony.com/environments.html)

* [Back up an environment](https://symfony.com/environments/backup.html)
* [Restore an environment](https://symfony.com/environments/restore.html)
* [Cancel an activity](https://symfony.com/environments/cancel-activity.html)
* [Change parent](https://symfony.com/environments/change-parent.html)
* [Configure HTTP access control](https://symfony.com/environments/http-access-control.html)
* [Deactivate an environment](https://symfony.com/environments/deactivate-environment.html)
* [Manage search indexing](https://symfony.com/environments/search-engine-visibility.html)
* [Rename the default environment](https://symfony.com/environments/default-environment.html)

#### [Manage projects](https://symfony.com/projects.html)

* [Change regions](https://symfony.com/projects/region-migration.html)
* [Change the project timezone](https://symfony.com/projects/change-project-timezone.html)
* [Delete a project](https://symfony.com/projects/delete-project.html)

#### [Custom domains](https://symfony.com/domains.html)

* [Set up a custom domain](https://symfony.com/domains/steps.html)
  * [DNS and apex domains](https://symfony.com/domains/steps/dns.html)
  * [Custom TLS certificates](https://symfony.com/domains/steps/tls.html)
  * [Handle subdomains](https://symfony.com/domains/steps/subdomains.html)
  * [Preview environments](https://symfony.com/domains/steps/custom-domains-preview-environments.html)

* [Content delivery networks](https://symfony.com/domains/cdn.html)
  * [Fastly setup](https://symfony.com/domains/cdn/fastly.html)
  * [Managed Fastly CDN](https://symfony.com/domains/cdn/managed-fastly.html)
  * [Cloudflare setup](https://symfony.com/domains/cdn/cloudflare.html)

* [Troubleshooting](https://symfony.com/domains/troubleshoot.html)

#### [Administration](https://symfony.com/administration.html)

* [Command line interface (CLI)](https://symfony.com/administration/cli.html)
  * [API tokens](https://symfony.com/administration/cli/api-tokens.html)
  * [Command reference](https://symfony.com/administration/cli/reference.html)
  * [Initialize a project](https://symfony.com/administration/cli/init.html)

* [Console](https://symfony.com/administration/web.html)
  * [Configure a project](https://symfony.com/administration/web/configure-project.html)
  * [Configure environments](https://symfony.com/administration/web/configure-environment.html)

* [Organizations](https://symfony.com/administration/organizations.html)
* [Teams](https://symfony.com/administration/teams.html)
* [Users](https://symfony.com/administration/users.html)
* [Pricing](https://symfony.com/administration/pricing.html)
* [Billing](https://symfony.com/administration/billing.html)
  * [Administer your billing](https://symfony.com/administration/billing/billing-admin.html)
  * [Monitor your billing information](https://symfony.com/administration/billing/monitor-billing.html)
  * [Payment FAQ](https://symfony.com/administration/billing/payment-faq.html)
  * [Subscribe to an add-on](https://symfony.com/administration/billing/add-on-subscription.html)

* [Server upgrades](https://symfony.com/administration/servers.html)
* [Security](https://symfony.com/administration/security.html)
  * [Multifactor Authentication (MFA)](https://symfony.com/administration/security/mfa.html)
  * [Single Sign-On (SSO)](https://symfony.com/administration/security/sso.html)

#### [Security and compliance](https://symfony.com/security.html)

* [Fastly WAF](https://symfony.com/security/fastly-waf.html)
* [Upsun WAF](https://symfony.com/security/waf.html)
* [Data retention](https://symfony.com/security/data-retention.html)
* [Project isolation](https://symfony.com/security/project-isolation.html)

#### [Glossary](https://symfony.com/glossary.html)

#### [Request features](https://symfony.com/request-features.html)

### API Documentation

[View in markdown](https://symfony.com/get-started/stacks/symfony.md "Open this page in a markdown format. This format is easier for AI and other tools to read.")

[Edit page](https://github.com/platformsh/platformsh-docs/edit/main/sites/upsun/src/get-started/stacks/symfony/_index.md)

Deploy Symfony on Upsun
=======================

### [Back to home](https://symfony.com/)

### On this page

* [Further resources](https://symfony.com/doc/8.0/cloud/index.html#further-resources)
  * [Documentation](https://symfony.com/doc/8.0/cloud/index.html#documentation)
  * [Community content](https://symfony.com/doc/8.0/cloud/index.html#community-content)
  * [Videos](https://symfony.com/doc/8.0/cloud/index.html#videos)

 Try Upsun for 15 days

 After that, enjoy the same game-changing Upsun features for less with the [First Project Incentive](https://upsun.com/blog/first-project-incentive/)!¹ A monthly $19 perk!

[Activate your 15-day trial](https://upsun.com/register/)

 ¹Terms and conditions apply

### Note

Before you start, check out the [Upsun demo app](https://console.upsun.com/projects/create-project) and the main [Getting started guide](https://symfony.com/get-started/here.html). They provide all of the core concepts and common commands you need to know before using the materials below.

1. [Get started](https://symfony.com/get-started/stacks/symfony/get-started.html)
2. [Symfony integration](https://symfony.com/get-started/stacks/symfony/integration.html)
3. [Configure environment variables](https://symfony.com/get-started/stacks/symfony/environment-variables.html)
4. [Configure workers](https://symfony.com/get-started/stacks/symfony/workers.html)
5. [Set up cron jobs](https://symfony.com/get-started/stacks/symfony/crons.html)
6. [Manage continous observability with Blackfire](https://symfony.com/get-started/stacks/symfony/blackfire.html)
7. [Local development](https://symfony.com/get-started/stacks/symfony/local.html)
8. [FAQ](https://symfony.com/get-started/stacks/symfony/faq.html)
9. [Symfony CLI Tips](https://symfony.com/get-started/stacks/symfony/symfony-cli-tips.html)

Further resources [![Image 2: Anchor to this heading](https://symfony.com/images/svg/link.svg)](https://symfony.com/doc/8.0/cloud/index.html#further-resources)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

### Documentation [![Image 3: Anchor to this heading](https://symfony.com/images/svg/link.svg)](https://symfony.com/doc/8.0/cloud/index.html#documentation)

* [PHP documentation](https://symfony.com/languages/php.html)

* [Extensions](https://symfony.com/languages/php/extensions.html)

* [Performance tuning](https://symfony.com/languages/php/tuning.html)

* [PHP-FPM sizing](https://symfony.com/languages/php/fpm.html)

* [Swoole on Upsun](https://symfony.com/languages/php/swoole.html)

* [Authenticated Composer](https://symfony.com/languages/php/composer-auth.html)

### Community content [![Image 4: Anchor to this heading](https://symfony.com/images/svg/link.svg)](https://symfony.com/doc/8.0/cloud/index.html#community-content)

* [Symfony topics](https://support.platform.sh/hc/en-us/search?utf8=%E2%9C%93&query=symfony)

* [PHP topics](https://support.platform.sh/hc/en-us/search?utf8=%E2%9C%93&query=php)

### Videos [![Image 5: Anchor to this heading](https://symfony.com/images/svg/link.svg)](https://symfony.com/doc/8.0/cloud/index.html#videos)

* [Refactoring monolith to multi-app](https://youtu.be/5hApjWiTO1M?feature=shared)
* [Upsun: From zero to scaling hero](https://youtu.be/FEFBUomV5aY?feature=shared)

[Get started](https://docs.upsun.com/get-started/stacks/symfony/get-started.html)
