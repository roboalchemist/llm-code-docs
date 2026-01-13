# Source: https://docs.datadoghq.com/agent/supported_platforms/puppet.md

---
title: Puppet
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Agent > Supported Platforms > Puppet
source_url: https://docs.datadoghq.com/supported_platforms/puppet/index.html
---

# Puppet

This module installs the Datadog Agent and sends Puppet reports to Datadog.

## Prerequisites{% #prerequisites %}

The Datadog Puppet module supports Linux and Windows and is compatible with Puppet >= 7.34.x or Puppet Enterprise version >= 2021.7.x. For detailed information on compatibility, see the [module page on Puppet Forge](https://forge.puppet.com/datadog/datadog_agent).

## Installation{% #installation %}

Follow the [inâapp installation guide in Fleet Automation](https://app.datadoghq.com/fleet/install-agent/latest?platform=puppet) to select your required features, copy the generated manifest snippet, add it to your Puppet manifest, and apply your standard Puppet deployment to roll out the Agent. See the [Datadog Agent module](https://forge.puppet.com/datadog/datadog_agent) or the Advanced configurations section for additional configurations, including managing Agent upgrades, enabling Agent integrations and setting up Puppet run reporting.

### Upgrading the Agent{% #upgrading-the-agent %}

[!IMPORTANT] The Datadog Puppet Module v4.x drops support for Puppet <= 6 and Datadog Agent v5. To upgrade or install the Datadog Agent v5+ on Puppet <= 6, use module v3.x.

- By default, Datadog Agent v7.x is installed. To use Agent version 6, change the setting `agent_major_version`.
- Agent v5-specific legacy options have been removed. Refer to the CHANGELOG.md for more details and the datadog_agent class comments for all available options.

[!IMPORTANT] Updates and breaking changes have been made in the below agent integrations:

- ActiveMQ_XML
  - `suppress_errors` config should now be used instead of `supress_errors` (backward-compatible)
- ElasticSearch **[BREAKING CHANGES]**
  - `ssl_verify` accepts only Boolean values
  - `tls_verify` options have been added
- Disk Check **[BREAKING CHANGES]**
  - `use_mount`, `all_partitions`, and `tag_by_filesystem` accept only Boolean values
- TCP Check
  - `skip_event` option has been removed sinced Datadog Agent v6.4+

### Configuration{% #configuration %}

Once the `datadog_agent` module is installed on your `puppetserver`/`puppetmaster` (or on a masterless host), follow these configuration steps:

1. Obtain your [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys).

1. Add the Datadog class to your node manifests (eg: `/etc/puppetlabs/code/environments/production/manifests/site.pp`).

   ```
   class { 'datadog_agent':
       api_key => "<YOUR_DD_API_KEY>",
   }
   ```

If using a Datadog site other than the default 'datadoghq.com', set it here as well:

   ```
   class { 'datadog_agent':
       api_key => "<YOUR_DD_API_KEY>",
       datadog_site => "datadoghq.eu",
   }
   ```

For CentOS/RHEL versions <7.0 and for Ubuntu < 15.04, specify the service provider as `upstart`:

   ```
   class { 'datadog_agent':
       api_key => "<YOUR_DD_API_KEY>",
       service_provider => 'upstart'
   }
   ```

See the Configuration variables section for list of arguments you can use here.

1. (Optional) Include any integrations you want to use with the Agent. The following example installs the mongo integration:

   ```
   class { 'datadog_agent::integrations::mongo':
       # integration arguments go here
   }
   ```

See the [comments in code](https://github.com/DataDog/puppet-datadog-agent/blob/master/manifests/integrations/mongo.pp) for all arguments available for a given integration.

If an integration does not have a [manifest with a dedicated class](https://github.com/DataDog/puppet-datadog-agent/tree/master/manifests/integrations), you can still add a configuration for it. Below is an example for the `ntp` check:

   ```
   class { 'datadog_agent':
       api_key      => "<YOUR_DD_API_KEY>",
       integrations => {
           "ntp" => {
               init_config => {},
               instances => [{
                   offset_threshold => 30,
               }],
           },
       },
   }
   ```

1. (Optional) To collect metrics and events about Puppet itself, see the section about Reporting.

## Advanced configurations{% #advanced-configurations %}

### Upgrading integrations{% #upgrading-integrations %}

To install and pin specific integration versions, use `datadog_agent::install_integration`. This calls the `datadog-agent integration` command to ensure a specific integration is installed or uninstalled, for example:

```
datadog_agent::install_integration { "mongo-1.9":
    ensure => present,
    integration_name => 'datadog-mongo',
    version => '1.9.0',
    third_party => false,
}
```

The `ensure` argument can take two values:

- `present` (default)
- `absent` (removes a previously pinned version of an integration)

To install a third-party integration (eg: from the marketplace) set the `third_party` argument to `true`.

Note it's not possible to downgrade an integration to a version older than the one bundled with the Agent.

### Reporting{% #reporting %}

To enable reporting of Puppet runs to your Datadog timeline, enable the report processor on your Puppet master and reporting for your clients. The clients send a run report after each check-in back to the master.

1. Set the `puppet_run_reports` option to true in the node configuration manifest for your master:

   ```ruby
   class { 'datadog-agent':
     api_key            => '<YOUR_DD_API_KEY>',
     puppet_run_reports => true
     # ...
   }
   ```

The dogapi gem is automatically installed. Set `manage_dogapi_gem` to false if you want to customize the installation.

1. Add these configuration options to the Puppet master config (eg: `/etc/puppetlabs/puppet/puppet.conf`):

   ```ini
   [main]
   # No modification needed to this section
   # ...
   
   [master]
   # Enable reporting to Datadog
   reports=datadog_reports
   # If you use other reports, add datadog_reports to the end,
   # for example: reports=store,log,datadog_reports
   # ...
   
   [agent]
   # ...
   report=true
   ```

With the [`ini_setting` module](https://forge.puppet.com/modules/puppetlabs/inifile):

```puppet
  ini_setting { 'puppet_conf_master_report_datadog_puppetdb':
    ensure  => present,
    path    => '/etc/puppetlabs/puppet/puppet.conf',
    section => 'master',
    setting => 'reports',
    value   => 'datadog_reports,puppetdb',
    notify  => [
      Service['puppet'],
      Service['puppetserver'],
    ],
  }
```

On all of your Puppet client nodes, add the following in the same location:

```ini
[agent]
# ...
report=true
```

With the [`ini_setting` module](https://forge.puppet.com/modules/puppetlabs/inifile):

```puppet
  ini_setting { 'puppet_conf_agent_report_true':
    ensure  => present,
    path    => '/etc/puppetlabs/puppet/puppet.conf',
    section => 'agent',
    setting => 'report',
    value   => 'true',
    notify  => [
      Service['puppet'],
    ],
  }
```

(Optional) Enable tagging of reports with facts:

You can add tags to reports that are sent to Datadog as events. These tags can be sourced from Puppet facts for the given node the report is regarding. These should be 1:1 and not involve structured facts (hashes, arrays, etc.) to ensure readability. To enable regular fact tagging, set the parameter `datadog_agent::reports::report_fact_tags` to the array value of factsâfor example `["virtual","operatingsystem"]`. To enable trusted fact tagging, set the parameter `datadog_agent::reports::report_trusted_fact_tags` to the array value of factsâfor example `["certname","extensions.pp_role","hostname"]`.

NOTE: Changing these settings requires a restart of pe-puppetserver (or puppetserver) to re-read the report processor. Ensure the changes are deployed prior to restarting the service(s).

Tips:

- Use dot index to specify a target fact; otherwise, the entire fact data set becomes the value as a string (not very useful)
- Do not duplicate common data from monitoring like hostname, uptime, memory, etc.
- Coordinate core facts like role, owner, template, datacenter, etc., that help you build meaningful correlations to the same tags from metrics

Verify your Puppet data is in Datadog by searching for `sources:puppet` in the [Event Stream](https://app.datadoghq.com/event/stream).

### NPM setup{% #npm-setup %}

To enable the Datadog Agent Network Performance Monitoring (NPM) features follow these steps:

1. (Windows only) If the Agent is already installed, uninstall it by passing `win_ensure => absent` to the main class and removing other classes' definitions.
1. (Windows only) Pass the `windows_npm_install` option with value `true` to the `datadog::datadog_agent` class. Remove `win_ensure` if added on previous step.
1. Use the `datadog_agent::system_probe` class to properly create the configuration file:

```
class { 'datadog_agent::system_probe':
    network_enabled => true,
}
```

### USM setup{% #usm-setup %}

To enable the Datadog Agent Universal Service Monitoring (USM) use the `datadog_agent::system_probe` class to properly create the configuration file:

```
class { 'datadog_agent::system_probe':
    service_monitoring_enabled => true,
}
```

### Troubleshooting{% #troubleshooting %}

You can run the Puppet Agent manually to check for errors in the output:

````
```shell
sudo systemctl restart puppetserver
sudo puppet agent --onetime --no-daemonize --no-splay --verbose
```

 Example response:

```text
info: Retrieving plugin
info: Caching catalog for alq-linux.dev.datadoghq.com
info: Applying configuration version '1333470114'
notice: Finished catalog run in 0.81 seconds
```
````

If you see the following error, ensure `reports=datadog_reports` is defined in `[master]`, not `[main]`.

````
```text
err: Could not send report:
Error 400 on SERVER: Could not autoload datadog_reports:
Class Datadog_reports is already defined in Puppet::Reports
```
````

If you don't see any reports coming in, check your Puppet server logs.

### Masterless Puppet{% #masterless-puppet %}

1. The Datadog module and its dependencies have to be installed on all nodes running masterless.

1. Add this to each node's `site.pp` file:

   ```
   class { "datadog_agent":
       api_key            => "<YOUR_DD_API_KEY>",
       puppet_run_reports => true
   }
   ```

1. Run puppet in masterless configuration:

   ```shell
   puppet apply --modulepath <path_to_modules> <path_to_site.pp>
   ```

### Tagging client nodes{% #tagging-client-nodes %}

The Datadog Agent configuration file is recreated from the template every Puppet run. If you need to tag your nodes, add an array entry in Hiera:

```
datadog_agent::tags:
- 'keyname:value'
- 'anotherkey:%{factname}'
```

To generate tags from custom facts classify your nodes with Puppet facts as an array to the `facts_to_tags` paramter either through the Puppet Enterprise console or Hiera. Here is an example:

```
class { "datadog_agent":
  api_key            => "<YOUR_DD_API_KEY>",
  facts_to_tags      => ["os.family","networking.domain","my_custom_fact"],
}
```

Tips:

1. For structured facts index into the specific fact value otherwise the entire array comes over as a string and ultimately be difficult to use.
1. Dynamic facts such as CPU usage, Uptime, and others that are expected to change each run are not ideal for tagging. Static facts that are expected to stay for the life of a node are best candidates for tagging.

### Configuration variables{% #configuration-variables %}

These variables can be set in the `datadog_agent` class to control settings in the Agent. See the [comments in code](https://github.com/DataDog/puppet-datadog-agent/blob/master/manifests/init.pp) for the full list of supported arguments.

| variable name                | description                                                                                                                                                                                  |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_major_version`        | The version of the Agent to install: either 6 or 7 (default: 7).                                                                                                                             |
| `agent_version`              | Lets you pin a specific minor version of the Agent to install, for example: `1:7.16.0-1`. Leave empty to install the latest version.                                                         |
| `collect_ec2_tags`           | Collect an instance's custom EC2 tags as Agent tags by using `true`.                                                                                                                         |
| `collect_instance_metadata`  | Collect an instance's EC2 metadata as Agent tags by using `true`.                                                                                                                            |
| `datadog_site`               | The Datadog site to report to. Defaults to `datadoghq.com`, eg: `datadoghq.eu` or `us3.datadoghq.com`.                                                                                       |
| `dd_url`                     | The Datadog intake server URL. You are unlikely to need to change this. Overrides `datadog_site`                                                                                             |
| `host`                       | Overrides the node's host name.                                                                                                                                                              |
| `local_tags`                 | An array of `<KEY:VALUE>` strings that are set as tags for the node.                                                                                                                         |
| `non_local_traffic`          | Allow other nodes to relay their DogstatsD traffic through this node.                                                                                                                        |
| `apm_enabled`                | A boolean to enable the APM Agent (defaults to false).                                                                                                                                       |
| `process_enabled`            | A boolean to enable the process Agent (defaults to false).                                                                                                                                   |
| `scrub_args`                 | A boolean to enable the process cmdline scrubbing (defaults to true).                                                                                                                        |
| `custom_sensitive_words`     | An array to add more words beyond the default ones used by the scrubbing feature (defaults to `[]`).                                                                                         |
| `logs_enabled`               | A boolean to enable the logs Agent (defaults to false).                                                                                                                                      |
| `windows_npm_install`        | A boolean to enable the Windows NPM driver installation (defaults to false).                                                                                                                 |
| `win_ensure`                 | An enum (present/absent) to ensure the presence/absence of the Datadog Agent on Windows (defaults to present)                                                                                |
| `container_collect_all`      | A boolean to enable logs collection for all containers.                                                                                                                                      |
| `agent_extra_options`1       | A hash to provide additional configuration options (Agent v6 and v7 only).                                                                                                                   |
| `hostname_extraction_regex`2 | A regex used to extract the hostname captured group to report the run in Datadog instead of reporting the Puppet nodename, for example:`'^(?<hostname>.*\.datadoghq\.com)(\.i-\w{8}\..*)?$'` |

(1) `agent_extra_options` is used to provide a fine grain control of additional Agent v6/v7 config options. A deep merge is performed that may override options provided in the `datadog_agent` class parameters. For example:

```
class { "datadog_agent":
    < your other arguments to the class >,
    agent_extra_options => {
        use_http => true,
        use_compression => true,
        compression_level => 6,
    },
}
```

(2) `hostname_extraction_regex` is useful when the Puppet module and the Datadog Agent are reporting different host names for the same host in the infrastructure list.
