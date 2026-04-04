# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/data-center-edition/updating.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/data-center-edition/updating.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/data-center-edition/updating.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/data-center-edition/updating.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/data-center-edition/updating.md

# Updating

To update your Data Center Edition to a newer version:

1. [determine-path](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/determine-path "mention").
2. Read the [release-notes](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/release-notes "mention") between the SonarQube Server versions.
3. Back up the SonarQube Server database.
4. [starting-stopping-cluster](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/starting-stopping-cluster "mention").
5. Update each application and search node as follows (do not trigger the setup phase):
   * [pre-update-steps](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/pre-update-steps "mention").
   * [update](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/update "mention").
   * [post-update-steps](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/post-update-steps "mention").
6. Once all nodes have the same binaries, restart the cluster. See [starting-stopping-cluster](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/starting-stopping-cluster "mention") for more information.
7. At this point, only one of the application nodes is up and waiting for the /setup endpoint to be accessed. Try to access `node_ip:port/setup` on each application node, and trigger the setup operation on the one that responds.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [dce-topology](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/dce-topology "mention")
* [starting-stopping-cluster](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/starting-stopping-cluster "mention")
* [monitoring](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/data-center-edition/monitoring "mention") your cluster
* [improving-performance](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/data-center-edition/improving-performance "mention") of your cluster
* [scaling](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/data-center-edition/scaling "mention") your cluster
