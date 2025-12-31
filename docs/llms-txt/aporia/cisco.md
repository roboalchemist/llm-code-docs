# Source: https://docs.aporia.com/integrations/cisco.md

# Cisco

You can integrate Aporia with Cisco's Full-Stack Observability Platform to receive alerts and notifications directly to the platform, and view your models health status in a centralized place.

### Setting up the FSOP Integration

1. Create a service principal in Cisco's platform
   1. Login to <https://accounts.appdynamics.com/overview>
   2. Click on **Access Management** and go to **Service Principals**

      <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FXyfxcCAaZ6VDESsIHb18%2Fimage.png?alt=media&#x26;token=e744a972-0c84-4bc7-a023-4af49bd86cad" alt=""><figcaption><p>Cisco FSOP Account Management</p></figcaption></figure>
   3. Click on **Add**

      <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2F8twLdSLYkI3WOqjXq2D5%2Fimage.png?alt=media&#x26;token=0d1a4908-f08d-447e-981a-cd630308120c" alt=""><figcaption><p>Cisco FSOP Service Principal Management</p></figcaption></figure>
   4. Define the new service principal. Note to pick **Basic** for **Authentication Type** and add the **Agent** default role access (Under **Edit Role Access**). Then click on **Create**.

      <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FIVt9Xvt9uitTsGkE4o8Y%2Fimage.png?alt=media&#x26;token=39ddc55b-4370-43de-8876-302aa7e70822" alt=""><figcaption><p>Service-Principal Configuration</p></figcaption></figure>
   5. Save the output service principal details - They will be needed for the Aporia integration.

      <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FboC4wutsO60uxnIis49c%2Fimage.png?alt=media&#x26;token=10a07d63-744c-431e-b423-1a9d7dc29ebb" alt=""><figcaption><p>Service Principal Details</p></figcaption></figure>
2. Log into Aporia’s console. On the navbar on the left, click on **Integrations,** switch to the **Applications** tab, and choose **Cisco**.

   <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FrPJwx7FEnS795ICXkKwM%2Fimage.png?alt=media&#x26;token=51d275b4-9d94-44f8-8553-c57359375e03" alt=""><figcaption><p>Cisco Integration</p></figcaption></figure>
3. Enter your **Tenant Details** and **Service Principal Details**, as created in the previous ste&#x70;**.** The Tenant URL should include the schema with no added URIs (https\://\<tenant>.observe.appdynamics.com).

   <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FFdR62SfBGSNEgPxc9CED%2Fimage.png?alt=media&#x26;token=fcd094c9-1577-4191-97dd-7aabfd3b9fde" alt=""><figcaption><p>Integration Configuration</p></figcaption></figure>
4. Click Save. On success the save button will become disabled, and you'll be able to Test the integration.

**Congratulations: You’ve now successfully integrated Aporia to Cisco's FSO Platform!**

After Integrating Cisco FSOP, any monitors will be automatically configured to send alerts to the platform.<br>

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FnLqK4uqOyTY4n7MV26Iq%2Fimage.png?alt=media&#x26;token=fcad7ec5-38b3-488a-8207-da83522e265c" alt=""><figcaption><p>Monitor Configuration</p></figcaption></figure>

In addition, the workspace state will now be synced to the FSO platform periodically, including models and alerts.

Happy Monitoring!
