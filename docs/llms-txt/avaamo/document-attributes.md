# Source: https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/document-attributes.md

# Document attributes

In enterprise organizations, content is extensive and often tailored to specific user groups. LLaMB facilitates seamless content ingestion and allows you to associate attributes with uploaded content.

Document attributes are valuable for filtering responses and creating personalized responses based on user properties like region, roles, and products. By creating user properties and associating document attributes with the ingested content in LLaMB, personalized responses can be efficiently generated from your enterprise content.

### Scenario: How to use it?

Consider a scenario in an enterprise organization where different privacy policies apply based on the employee's region. There is a requirement to display responses from the appropriate region-specific privacy policy according to the employee's location.&#x20;

For example, if an employee from India inquires about the privacy policy, the response must be provided from the policy applicable to the India region. Similarly, if an employee from the US inquires about the privacy policy, the response must be sourced from the policy applicable to the US region.

### Step 1: Identify attributes

Identify the set of attributes from the URLs you wish to ingest into your LLaMB content and understand how the content is organized. Categorizing the content helps in determining the necessary attributes for creating personalized responses.&#x20;

For example, you can define "region" as an attribute name for regional content. Similarly, for a set of Microsoft Office 365 suite URLs, you could define "product" as an attribute name. Another example is using "status" as an attribute to display responses based on the employee's status.

### Step 2: Create user property

The next step is to create a user property based on your identified attributes.&#x20;

For the [given scenario](#scenario-how-to-use-it), you can create a `region`user property in the `Configuration -> User property` section. See [User property](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-user-properties), for more information.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FJcHgnC2Jr8zfTKn1PVeJ%2Fimage.png?alt=media&#x26;token=acc1f120-cbdf-41df-a703-b4440f576e18" alt=""><figcaption></figcaption></figure>

### Step 3: Associate document attributes with the URL

Ingest the URL into your LLaMB Content skill and associate attributes based on the ingested content. Document attributes can be any name-value pair formatted as valid JSON. You can specify the attributes either at the time of [uploading the URL](https://docs.avaamo.com/user-guide/llamb/get-started/upload-content#upload-from-url) or if the URL has already been uploaded, you can [edit the document](https://docs.avaamo.com/user-guide/llamb/get-started/common-actions#edit) to associate the required attributes.

{% hint style="success" %}
**Key points:**&#x20;

* Document attributes must be valid JSON.
* Ensure that the name of the user property matches the document attribute.
  {% endhint %}

<table><thead><tr><th width="308.2777777777778">Property</th><th width="432.73761065294696">Description</th></tr></thead><tbody><tr><td>&#x3C;&#x3C;attribute_name>></td><td>Indicates the name of the attribute. Ensure that the name of the user property matches the document attribute.</td></tr><tr><td>&#x3C;&#x3C;attribute_name>> -> value</td><td>Indicates the attribute value associated with this content.</td></tr></tbody></table>

**Example 1:** Adding an Attribute with a Single Value Associated with a Key

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FXSIQfKuIYXowbBTQgGaR%2Fimage.png?alt=media&#x26;token=4f563ad2-7a48-426a-bf16-49d69b159d52" alt=""><figcaption></figcaption></figure>

**Example 2:** Adding an Attribute with an Array as the Value

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FT2Br4NVyN2wr081SwmBR%2FScreenshot%2005-08-2024%20at%2017.31.png?alt=media&#x26;token=f04170a1-f6fb-4656-b9f7-d98d994ee4d6" alt=""><figcaption></figcaption></figure>

### Step 4: Set user property

You can set the user properties in various ways based on your requirements.&#x20;

* Using [User.setProperty](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/user.setproperty) or [User.setProperties](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/user.setproperties) in the conversational flow. Example: In the Greeting node or the User authentication handler as per your requirements.
* If you are using a custom channel, then you can specify user properties in the custom channel payload. See [Custom channel](https://docs.avaamo.com/user-guide/llamb/custom-channel), for more information.

For the [given scenario](#scenario-how-to-use-it), the user property is directly set in the Greeting node.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FbGNnNijESN8lyTNOkyEN%2Fimage.png?alt=media&#x26;token=1b85a405-3a6d-4a35-9996-9120bca594f7" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
**Key points**:&#x20;

* The hardcoded value used in this example is for demonstration purposes only. In a real enterprise setting, user property values are typically set dynamically, such as from an API response following user authorization.
* If the user properties are not set, all ingested content in your agent, regardless of attributes, is used to render responses.
  {% endhint %}

### Step 5: Test the conversation flow to view personalized responses&#x20;

Open the agent simulator and ask a query from the uploaded Privacy Policy document.

In this example, the uploaded Privacy Policy document has the "region" attribute set to "India." Since the user property is set to "India," the responses is displayed from the document with the region attribute set to "India."

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fq93nF5UlkdY2cB6pypmW%2Fimage.png?alt=media&#x26;token=85bbefe4-9080-4ffc-a530-e26bfa5dca60" alt=""><figcaption></figcaption></figure>

Now, update the user property to "China" and ask a query from the uploaded Privacy Policy document. Since the user property is set to "China" and there are no documents with the region attribute set to "China," an unhandled response is displayed.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FSZJgCyzB7IKTP6bnWIgF%2Fimage.png?alt=media&#x26;token=ad65f36d-1411-4324-8051-2ec8792cc952" alt=""><figcaption></figcaption></figure>
