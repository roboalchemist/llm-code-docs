# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/hyperscalers-landing-page/launching-pentaho-ami-in-aws-cp/launch-the-pentaho-ami-instance-launch-pentaho-in-aws.md

# Launch the Pentaho AMI instance

Perform the following steps to launch an instance of the Pentaho AMI from the EC2:AMI Catalog

1. Select the AMI Catalog from the EC2 menu and search the AWS Marketplace AMIs for the Pentaho AMI.
2. Select to view the AMI you want to launch.
3. Review the product details and terms, then select the AMI you want to use, and press **Continue**.
4. Click **Launch Instance from AMI**.

   The EC2 Launch screen opens.
5. Name your new server.
6. Select your instance type.
7. In the **Key pair (login)** section of the Launch an instance page, select **Choose an existing key pair** if you already have a valid key pair, or select **Create a new key pair** to create a new one.
   * **Choose an existing key pair**: Select a key pair from the list of available key pairs.
   * **Create a new key pair**: Enter a name for the key pair and click **Create**. The private key file will be downloaded automatically to your local computer. Be sure to store the private key file in a secure location, as you will need it to connect to the instance using SSH.
8. Set port 22 for SSH access and allow traffic from your desired IP addresses in the **Network Settings** > **Create security group** option.
9. Create a new rule or edit existing rules or to allow traffic on port 8080 from your desired IP addresses or IP ranges.

   **Note:** You do not need to adjust the attached disk volumes in **Configure storage**.
10. Review the launch configuration and click **Launch instance** to start the instance.

Once the instance is running, you can connect to it using SSH and the private key file for the key pair you selected or created.
