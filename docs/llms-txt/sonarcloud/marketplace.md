# Source: https://docs.sonarsource.com/sonarqube-community-build/server-update-and-maintenance/update/marketplace.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/instance-administration/marketplace.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/marketplace.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/marketplace.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/marketplace.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/marketplace.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/marketplace.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/marketplace.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/marketplace.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/marketplace.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/marketplace.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/server-upgrade-and-maintenance/upgrade/marketplace.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/upgrade/marketplace.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/upgrade/marketplace.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/upgrade/marketplace.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/update/marketplace.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/update/marketplace.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/update/marketplace.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/update/marketplace.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/marketplace.md

# Using Marketplace

Administrators can access the SonarQube Server Marketplace via **Administration** > **Marketplace**. The Marketplace tab is the place for keeping the pieces of the SonarQube Server platform up to date. It lets you:

See:

* The currently installed SonarQube Server Edition
* Which plugins are installed

Discover:

* Which other Editions are available, to enable more features

{% hint style="warning" %}
A third-party website called `sonarplugins.com` also exists. This website is not the same as the Marketplace and is not endorsed by, affiliated with, maintained, authorized, or sponsored by Sonar.
{% endhint %}

### Pending operations <a href="#pending-operations" id="pending-operations"></a>

When you perform an action in the Marketplace (install, update, or uninstall a plugin), a yellow banner appears at the top of the page showing pending operations that will be executed once SonarQube Server is restarted. Pending operations can be canceled until the server is restarted.

### Restart SonarQube Server <a href="#restart-sonarqube" id="restart-sonarqube"></a>

Restarting SonarQube Server can be done manually from the command line by running `sonar.sh restart`. When you have Pending Changes, the restart button will be displayed in the yellow banner (see **Pending Operations** above). Please note that restarting SonarQube Server won’t reload the changes applied to the `sonar.properties`.

### Manual updates <a href="#manual-updates" id="manual-updates"></a>

If you’re using a commercial edition or your server doesn’t have internet access, you won’t be able to rely on the Marketplace tab for plugins and will have to handle plugin installations and updates manually.

To see what plugins are available and which version of a plugin is appropriate for your server, use the [plugin-version-matrix](https://docs.sonarsource.com/sonarqube-server/server-installation/plugins/plugin-version-matrix "mention"), which is kept up to date with current plugin availability and compatibility.

To install a plugin, simply download it using the manual download link on the plugin’s documentation page, place it in `<sonarqubeHome>/extensions/plugins`, and restart the server.

#### Stopping the Marketplace from searching for plugin updates <a href="#stopping-the-marketplace-from-searching-for-plugin-updates" id="stopping-the-marketplace-from-searching-for-plugin-updates"></a>

Your SonarQube Server needs internet access for the Marketplace to search for plugin updates. If your server doesn’t have internet access, you may get errors in your logs when the Marketplace tries to search for new plugins. You can stop this by updating `sonar.updatecenter.activate` in `<sonarqubeHome>/conf/sonar.properties`.

### Which URLs does the Marketplace connect to? <a href="#which-urls-does-the-marketplace-connect-to" id="which-urls-does-the-marketplace-connect-to"></a>

The SonarQube Marketplace connects to <https://downloads.sonarsource.com/?prefix=sonarqube/update> to get the list of plugins. Most of the referenced plugins are downloaded from:

* <https://binaries.sonarsource.com/>
* <https://github.com/>

### Using the Marketplace behind a proxy <a href="#using-the-marketplace-behind-a-proxy" id="using-the-marketplace-behind-a-proxy"></a>

Marketplace uses HTTP(S) connections to external servers to provide these services. If SonarQube Server is located behind a proxy, additional information must be provided in `<sonarqubeHome>/conf/sonar.properties`:

```css-79elbk
http.proxyHost=<your.proxy.host>
http.proxyPort=<your.proxy.port>

#If proxy authentication is required
http.proxyUser=<your.proxy.user>
http.proxyPassword=<your.proxy.password> 
```

Note:

* the same properties can be used in the `https.*` form for HTTPS connections.
* `http.proxyHost` does not work it if contains a schema ("http\://" or "https\://")

### Deploying to the Marketplace <a href="#deploying-to-the-marketplace" id="deploying-to-the-marketplace"></a>

If you have developed a SonarQube Server plugin, you can check out the [requirements](https://community.sonarsource.com/t/deploying-to-the-marketplace/35236) for adding it to the Marketplace in the [Plugin Development community](https://community.sonarsource.com/c/plugins/15).
