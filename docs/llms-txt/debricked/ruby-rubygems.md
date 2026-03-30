# Source: https://docs.debricked.com/overview/language-support/ruby-rubygems.md

# Ruby - RubyGems

OpenText Core SCA now tracks Ruby dependencies through  RubyGems, using its associated *Gemfile.lock* files. If at least one of the supported files is committed to the repository, it will be automatically scanned for dependencies when integrated with OpenText Core SCA CI/CD pipeline.

### **Supported file formats and features**

<table data-full-width="true"><thead><tr><th>Package manager</th><th>Supported file formats</th><th data-type="checkbox">Root dependencies </th><th data-type="checkbox">Indirect dependencies</th><th data-type="checkbox">Dependency trees</th><th data-type="checkbox">Security scanning</th><th data-type="checkbox">License scanning</th><th data-type="checkbox">Root fix</th><th data-type="checkbox">Pull Request</th><th data-type="checkbox">Reachability Analysis</th><th>High Performance Scan</th></tr></thead><tbody><tr><td>RubyGems</td><td><em>Gemfile.lock</em></td><td>true</td><td>true</td><td>false</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>Yes*</td></tr></tbody></table>

**\***&#x54;his is a native lock file format. Native lock file formats are the fastest formats to scan.
