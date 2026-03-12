# Source: https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration/creating-a-custom-field-in-servicenow.md

# Creating a Custom Field in ServiceNow

Creating custom fields in ServiceNow enables better data organization and adapts the platform to meet specific business requirements. This opens a new way to map data fields across various platforms, ensuring seamless data flow and synchronization.

### How to Create Custom Fields in ServiceNow <a href="#how-to-create-custom-fields-in-servicenow" id="how-to-create-custom-fields-in-servicenow"></a>

Here’s a step-by-step guide to creating custom fields in ServiceNow:

#### 1. Select the Appropriate Table: <a href="#id-1.-select-the-appropriate-table" id="id-1.-select-the-appropriate-table"></a>

* Choose the table where the new custom field will be created. ServiceNow organizes its data in tables, such as Incidents, Change, or Task, and each table can have customized fields.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDn7EBsvxjOn86pM8NqFC%2FServiceNow%20Incident%20Task.png?alt=media&#x26;token=47870e5c-3fb4-4704-9d0b-738abcb21c8e" alt=""><figcaption></figcaption></figure>

#### 2. Access the Form Layout to Create a Custom Field: <a href="#id-2.-access-the-form-layout-to-create-a-custom-field" id="id-2.-access-the-form-layout-to-create-a-custom-field"></a>

* Click the three horizontal bars (as shown below) and select **Configure > Form Layout**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEAktKbQWMVNAiJ6fiCpc%2FConfiguring%20Form%20Layouts%20to%20Create%20Custom%20fields.png?alt=media&#x26;token=9d1bf23e-16c7-4e12-85bf-b515e5b4b9b4" alt=""><figcaption></figcaption></figure>

* In the **Create new field** section, provide the necessary details:
  * **Name**: Enter the name of the field.
  * **Type**: Select the field type.
  * **Field Length**: Specify the length of the field.
  * **View Name**: Choose the view for displaying the field (Default view is recommended).
  * **Section**: Determine which section the field will be displayed in.
  * Click **Add** to create the field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGCpCTHNPcjRvjGME0TTf%2FExample%20of%20a%20custom%20field%20being%20created.png?alt=media&#x26;token=93989af6-b782-4255-a165-ba10bccf298d" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
As of the publication date of this article, Getint supports the following field types: Date, Dropdown, Text, Reference, and URL.
{% endhint %}

#### 3. Place the Field <a href="#id-3.-place-the-field" id="id-3.-place-the-field"></a>

* Use the ServiceNow **slushbucket** (the term slushbucket refers to a user interface component used to transfer items between two lists) to place the new field in the desired position on the form.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxNKOUeUQijEjcrhWJLvv%2FCreating%20a%20custom%20field.png?alt=media&#x26;token=786f3fad-cb58-42ee-9b07-ee40b980a232" alt=""><figcaption><p>Think of it as a method for sorting and organizing data within forms and catalog items</p></figcaption></figure>

* Click **Save** to finalize your changes.

#### 4. Test Your Custom Field <a href="#id-4.-test-your-custom-field" id="id-4.-test-your-custom-field"></a>

* Ensure the new field appears correctly on the form and functions as intended.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FrMzvXGnjiPB1j6otD3Fb%2FCustom%20field%20being%20created.png?alt=media&#x26;token=081fa150-dde5-45f5-8060-bdd7047f8586" alt=""><figcaption></figcaption></figure>

* It is important to also test the field in your ServiceNow integration to validate it is working as expected. The new field should be available from the dropdown list of field mapping.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FgTnqDgjEB5Rb4ze3HfbF%2FCustom%20field%20being%20recognized%20by%20Getint.png?alt=media&#x26;token=5878bc3d-f530-4cd7-a82d-fd64a50f8046" alt=""><figcaption><p>The newly created custom field appears when searching for ServiceNow fields</p></figcaption></figure>

When integrating ServiceNow with other tools using Getint, mapping custom fields is essential to maintain consistent data synchronization. Getint facilitates field mapping by allowing users to connect different platforms' fields, which may vary in naming conventions and types. If fields unique to ServiceNow (like Assignment Group) need to be mapped to other platforms, creating corresponding custom fields in those platforms can ensure a smooth integration experience.

These steps help customize the ServiceNow environment to fit specific use cases, enhance data management, and improve workflow automation. For more information about our tool or if need assistance with your integration, please contact our [Help Center](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
