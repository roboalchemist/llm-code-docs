# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/hyperscalers-landing-page.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/hyperscalers-landing-page.md

# Hyperscalers

You can take advantage of Pentaho with your hyperscaler environment by launching an instance of Pentaho in the Amazon Web Services (AWS) marketplace or by deploying pre-configured Docker images of specific Pentaho products on your AWS environments.

### Launching Pentaho AMI in AWS

You can launch a new Pentaho Amazon Machine Image (AMI) from the AWS Marketplace. To use the Pentaho AMI, you must create a customized security group and select or create an SSH key pair during the launch configuration. You can then install your licenses to activate the software after you launch an instance of the AMI.

#### Find and configure the Pentaho AMI

If you found us through the [Marketplace Search Page](https://aws.amazon.com/marketplace), your flow and prompts will differ, but you can end up with the same result. When prompted, you select Launch Via Ec2 to follow that flow.

#### Verify the server is running

Perform the following steps to verify that the Pentaho Server is running.

1. Navigate to the Pentaho Server at `http://*&lt;private ip&gt;*:8080`
2. Log in as the `Evaluation Admin User` using the Evaluation links provided.
3. Proceed according to the type of licensing you are using:
   * If this is a consumption-based license, the Pentaho Home page opens. Navigate to the License Management page and open in the Administrative perspective. The server will display all the currently active licenses. This completes the launch of the Pentaho AMI instance.
   * If this is a BYOL (bring your own license) server installation, the License Management page opens in the Administrative perspective. See [Apply licenses](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/broken-reference) for instructions to apply your licenses.

#### Apply licenses

After launching a BYOL instance of Pentaho in the marketplace, perform the following steps to apply your Pentaho licenses to the instance.

**Note:** If you launched an AWS consumption-based licensed image, you can skip these steps.

1. Have your public License URL or Activation ID available.
2. Click the **Add** (**+**) icon in PentahoLicense Manager to add a new license.
3. Copy and paste the public License URL or Activation ID into the **Add License** field and press **OK**.

   If the server can obtain the entitlements, you will see them refreshed in the **Licenses** list in License Manager.

Your BYOL instance is licensed and ready to use.

#### See also

#### Administration of Pentaho in your instance

The Pentaho software is owned by the `pentaho` user. A PostgreSQL repository is also installed on this instance and owned by the `postgres` user. Neither user has a password. You can only access these users via the `sudo` command.

The Pentaho software and the PostgreSQL data files are installed on the second volume (`/install`). The `/install/pentaho` directory is symlinked to the`/opt/pentaho` directory.

#### Pentaho Server

Pentaho is installed as an auto-start service in your instance. To check the status of the Pentaho Server, SSH to the machine and run the following command:

`sudo systemctl status pentaho`

See **Logging and performance monitoring** and **Troubleshooting** in the **Administer Pentaho Data Integration and Analytics** document for further details on maintaining the Pentaho Server

#### Upgrades

See [Pentaho upgrade](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp) for instructions on how to apply service packs and upgrades with the Pentaho Upgrade Installer.

#### Client tools

The following information in the **Pentaho Data Integration** document helps to extend your knowledge of client tool installation, the Pentaho Repository, and run configurations of remote jobs from the Pentaho Data Integration (PDI) client (also known as Spoon):

* See **Use a Pentaho Repository in PDI** for instructions to connect your PDI client in the instance to your Pentaho Repository.
* See **Run configurations** for instructions to configure your PDI jobs to run remotely in the instance.

**Note:** If you have not already installed the PDI client, see [Install PDI tools and plugins](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-of-the-pentaho-design-tools/install-the-pdi-tools-and-plugins) for installation instructions.
