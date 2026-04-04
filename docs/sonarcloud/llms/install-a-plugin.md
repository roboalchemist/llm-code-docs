# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/plugins/install-a-plugin.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/setup-and-upgrade/install-a-plugin.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/setup-and-upgrade/install-a-plugin.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/setup-and-upgrade/install-a-plugin.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/setup-and-upgrade/install-a-plugin.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/setup-and-upgrade/install-a-plugin.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/setup-and-upgrade/install-a-plugin.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/install-a-plugin.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/setup-and-upgrade/install-a-plugin.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/install-a-plugin.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/install-a-plugin.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/plugins/install-a-plugin.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/plugins/install-a-plugin.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/plugins/install-a-plugin.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/plugins/install-a-plugin.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/plugins/install-a-plugin.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/plugins/install-a-plugin.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/plugins/install-a-plugin.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/plugins/install-a-plugin.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/plugins/install-a-plugin.md

# Installing a plugin

You need to manually install plugins when using SonarQube Server (you cannot use the SonarQube Marketplace).

To see what plugins are available and which version is appropriate for your SonarQube Server, use the [plugin-version-matrix](https://docs.sonarsource.com/sonarqube-server/server-installation/plugins/plugin-version-matrix "mention"), which is kept up to date with current plugin availability and compatibility.

{% hint style="warning" %}
Plugins are not provided by Sonar; therefore, you install them at your own risk. A SonarQube Server administrator needs to acknowledge this risk in the Marketplace before installing plugins or when prompted in SonarQube Server after installing a plugin manually.
{% endhint %}

### Installing a plugin <a href="#manually-installing-plugins" id="manually-installing-plugins"></a>

{% tabs %}
{% tab title="ZIP INSTALLATION" %}

* Download the plugin you want to install. The version needs to be compatible with your SonarQube version.
* Put the downloaded jar in `<sonarqubeHome>/extensions/plugins`, and remove any previous versions of the same plugins.
* Restart your SonarQube.

{% hint style="info" %}
In case of a Data Center edition:

* Plugins are not shared, meaning if you install/uninstall/upgrade a given plugin on one application node, you need to perform the same actions on the other application nodes.
* All application nodes must be stopped when installing, uninstalling, or upgrading a plugin.
  {% endhint %}
  {% endtab %}

{% tab title="DOCKER INSTALLATION" %}
When running SonarQube Server under Docker, any plugin you want to install must also be copied into the Docker volume you create during installation. See the [installation-overview](https://docs.sonarsource.com/sonarqube-server/server-installation/from-docker-image/installation-overview "mention") article in our documentation for more details about creating the volume and container.

{% hint style="info" %}
Once SonarQube Server UI is up, you can encrypt sensitive properties stored in `<sonarqubeHome>/conf/sonar.properties`. See the [encrypting-settings](https://docs.sonarsource.com/sonarqube-server/instance-administration/security/encrypting-settings "mention") page.
{% endhint %}

Let’s assume that your SonarQube docker container is called `sonarqube`. The easiest way to install manually a plugin in the container is the following.

* Check if an existing version of the plugin exists. Run `docker exec sonarqube bash -c 'ls "$SONARQUBE_HOME"/extensions/plugins'` to see the entire list of plugins that are installed manually.
* If a previous version of the plugin is listed, remove it using `docker exec sonarqube bash -c 'rm "$SONARQUBE_HOME"/extensions/plugins/<PLUGIN_JAR_FILE_NAME>'`
* Install the new plugin using `docker exec sonarqube bash -c 'wget <PLUGIN_JAR_URL> -P "$SONARQUBE_HOME"/extensions/plugins/'`
* Restart the SonarQube docker container using `docker restart sonarqube`

Note that if you have followed the guidelines outlined on the [prepare-installation](https://docs.sonarsource.com/sonarqube-server/server-installation/from-docker-image/prepare-installation "mention") page, the resulting plugin will be available in the `sonarqube_extensions` volume, which is attached to the `<SONARQUBE_HOME>/extensions/plugins` folder.

{% hint style="info" %}
In case of a Data Center edition:

* Plugins are not shared, meaning if you install/uninstall/upgrade a given plugin on one application node, you need to perform the same actions on the other application nodes.
* All application nodes must be stopped when installing, uninstalling, or upgrading a plugin.
  {% endhint %}
  {% endtab %}

{% tab title="KUBERNETES INSTALLATION" %}

1. Download the appropriate plugin JAR file from a trusted source, ensuring it’s compatible with your SonarQube version.
2. Add the plugins section to your `values.yaml` file as illustrated below and use the `helm upgrade` command to apply the new chart.

```yaml
plugins:
  install:
   - "https://github.com/SonarOpenCommunity/sonar-cxx/releases/download/cxx-2.0.7/sonar-cxx-plugin-2.0.7.3119.jar"
```

Or use the `helm upgrade` command as illustrated below:

```sh
helm upgrade --install -n sonarqube sonarqube sonarqube/sonarqube \
 --set "plugins.install={https://github.com/SonarOpenCommunity/sonar-cxx/releases/download/cxx-2.0.7/sonar-cxx-plugin-2.0.7.3119.jar}"
```

{% endtab %}
{% endtabs %}

To verify the plugin installation, go to **Administration** > **Marketplace.**

### Uninstalling a plugin <a href="#uninstalling-plugins" id="uninstalling-plugins"></a>

To uninstall a plugin:

1. Delete the plugin from the `<sonarqubeHome>/extensions/plugins` folder.
2. Restart your SonarQube Server.
