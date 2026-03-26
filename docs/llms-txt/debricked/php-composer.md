# Source: https://docs.debricked.com/overview/language-support/php-composer.md

# PHP - Composer

OpenText Core SCA currently tracks PHP dependencies installed through Composer dependency manager, using either the *composer.json* or *composer.lock* files.

OpenText Core SCA recommends including the *composer.lock* file, as it contains resolved versions of both direct and indirect dependencies, leading to more accurate scan results.

The *composer.lock* file is generated whenever one of the following commands is executed:

```
composer install

composer required

composer update
```

If at least one of the supported files is committed to the repository, it will be automatically scanned for dependencies when integrated with OpenText Core SCA CI/CD pipeline.

### **Supported file formats and features**

<table data-full-width="true"><thead><tr><th>Package manager</th><th>Supported file formats</th><th data-type="checkbox">Root dependencies </th><th data-type="checkbox">Indirect dependencies</th><th data-type="checkbox">Dependency trees</th><th data-type="checkbox">Security scanning</th><th data-type="checkbox">License scanning</th><th data-type="checkbox">Root fix</th><th data-type="checkbox">Pull Request</th><th data-type="checkbox">Reachability Analysis</th><th>High Performance Scan</th></tr></thead><tbody><tr><td>Composer</td><td><em>composer.json</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>Yes</td></tr><tr><td>Composer</td><td><em>composer.lock</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>Yes*</td></tr></tbody></table>

**\***&#x54;his is a native lock file format. Native lock file formats are the fastest formats to scan.
