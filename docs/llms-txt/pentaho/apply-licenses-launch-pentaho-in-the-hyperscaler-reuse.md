# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/hyperscalers-landing-page/launching-pentaho-ami-in-aws-cp/apply-licenses-launch-pentaho-in-the-hyperscaler-reuse.md

# Apply licenses

After launching a "bring your own license" (BYOL) instance of Pentaho in the marketplace, perform the following steps to apply your Pentaho licenses to the instance.

**Note:** If you launched an AWS hourly or annually licensed image, you can skip this step.

1. Copy or download the Pentaho license files to your local computer.

   **Note:** If you do not already have your Pentaho license keys, you can obtain them from your Pentaho sales representative in the form of Pentaho license files.
2. Navigate to the Pentaho Server at `http://*&lt;private ip&gt;*:8080`
3. Log in as the `Evaluation Admin User`.

   You are redirected to the License Management page in the Administrative perspective.
4. Click the **Add** (**+**) icon in License Keys to add a new license.
5. Click **Choose Files**.

   1. Select the server license file from your local computer.
   2. Click **Upload** to upload the license keys.

   After you enter the server license key, the Pentaho Server activates, and you are redirected to the Home page in the Pentaho User Console.
6. (Optional) Navigate back to the License Management page to complete any additional license key entries needed.

Your instance is licensed and ready to use.
