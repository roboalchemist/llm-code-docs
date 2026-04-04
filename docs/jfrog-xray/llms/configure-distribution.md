# Source: https://docs.jfrog.com/artifactory/docs/configure-distribution.md

# Configure Distribution

<Callout icon="📘" theme="info">
  **Subscription Information**

  This feature is supported with the **Enterprise+** license.
</Callout>

After you have completed <Anchor label="Installing Distribution" target="_blank" href="/installation/docs/installing-distribution">Installing Distribution</Anchor>, continue to the following required configurations:

* **[Setting up GPG Signing](/docs/gpg-signing):** JFrog Distribution secures Release Bundle delivery using a preconfigured GPG key. A Release Bundle, distributed to an Edge node, is signed with this GPG key.

  Providing an additional layer of protection on the contents in your Release Bundles. As part of the Release Bundle signing process, Distribution triggers Artifactory to clone the contents of a Release Bundle into an isolated *release-bundles* repository.
* Use one of the following methods to connect Artifactory and the Edge nodes:

  * **<Anchor label="Using Scope Tokens (Pairing Tokens)" target="_blank" href="/administration/docs/access-tokens/#generate-scoped-tokens">Using Scope Tokens (Pairing Tokens)</Anchor>**: Connect the source Artifactory and the Edge nodes using the JFrog Platform scoped tokens function. This function is available from Artifactory version 7.29.7 with the release of the Distribution Edges Add-on and is the default option used for connecting the source and node. (If you are unable to upgrade your self-hosted instance, or need to continue using the Circle of Trust, see the next method.)
  * **<Anchor label="Circle of Trust" target="_blank" href="/administration/docs/access-tokens#circle-of-trust-cross-instance-authentication">Circle of Trust</Anchor>**: Establish a circle of trust between your source Artifactory and Edge nodes. This should be applied to both the source and target Artifactory nodes.

In addition, the following optional configurations are available:

* Verify that <Anchor label="**Mission Control**" target="_blank" href="/installation/docs/installing-mission-control">**Mission Control**</Anchor> is enabled in your JPD and includes at least one registered Edge node.
* **<Anchor label="Distribution System YAML" target="_blank" href="/installation/docs/distribution-system-yaml">Distribution System YAML</Anchor>:** You can configure an existing JFrog Distribution instance system settings using a simple YAML configuration file.
* **<Anchor label="Distribution Application Config YAML File" target="_blank" href="/installation/docs/distribution-application-config-yaml-file">Distribution Application Config YAML File</Anchor>:** An alternative way to specify application-related settings for JFrog Distribution.

After you have finished the configuration of distribution assets, you can start to [Distribute Release Bundles (v1)](/docs/distribute-release-bundles-v1).

<Callout icon="📘" theme="info">
  **Note**

  For details about installing and configuring Edge nodes, see <Anchor label="Installing Artifactory Edge" target="_blank" href="/installation/docs/installing-artifactory-edge">Installing Artifactory Edge</Anchor>.
</Callout>