# Source: https://docs.jfrog.com/artifactory/docs/distribution-target-troubleshooting_distribute-release-bundles-v1.md

# Distribution Target Troubleshooting

If you receive the message, **No distribution targets are available** when attempting to distribute a Release Bundle (v1 or v2), check the following possible causes:

* No distribution targets, in particular Edge nodes, have been installed. For more information, see <Anchor label="Installing Artifactory Edge" target="_blank" href="/installation/docs/installing-artifactory-edge">Installing Artifactory Edge</Anchor>.
* Edge nodes have been installed but have not been added to your JPD. To perform this procedure, see <Anchor label="Register a Platform Deployment" target="_blank" href="/administration/docs/manage-platform-deployments#register-a-platform-deployment">Register a Platform Deployment</Anchor>.
* You do not have the required permissions to view the available Edge nodes and other distribution targets. In that case, contact your platform administrator.
* There are connectivity issues between your JPD and the Edge nodes.