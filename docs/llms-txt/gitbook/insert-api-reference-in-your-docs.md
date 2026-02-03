# Source: https://gitbook.com/docs/documentation/ja-gitbook-documentation/api-references/openapi/insert-api-reference-in-your-docs.md

# Source: https://gitbook.com/docs/documentation/zh/api-references/openapi/insert-api-reference-in-your-docs.md

# Source: https://gitbook.com/docs/documentation/fr/api-references/openapi/insert-api-reference-in-your-docs.md

# Source: https://gitbook.com/docs/api-references/openapi/insert-api-reference-in-your-docs.md

# Insert API reference in your docs

GitBook allows you to automatically generate pages related to the endpoints you have in your OpenAPI spec. These pages will contain OpenAPI operation blocks, allowing you and your visitors to test your endpoints and explore them further based on the information found in the spec.

{% hint style="success" %}
Endpoints added from your spec will continue to be updated anytime your spec is updated. See the [Update your specification](https://gitbook.com/docs/api-references/add-an-openapi-specification#update-your-specification) section for more info.
{% endhint %}

### Automatically create OpenAPI pages from your spec

After you’ve [added your OpenAPI spec](https://gitbook.com/docs/api-references/openapi/add-an-openapi-specification), you can generate endpoint pages by inserting an **OpenAPI Reference** in the table of contents of a Space.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FYy8gCqxfaO4xjv2eqiL5%2Fcreate_api_pages%402x.png?alt=media&#x26;token=62b8386b-9fea-4233-b961-b6a1e582411e" alt="A GitBook screenshot showing how to insert API references into the table of contents of a space"><figcaption><p>Insert API References in the table of contents of a Space.</p></figcaption></figure>

{% stepper %}
{% step %}
**Generate pages from OpenAPI**

In the space you’d like to generate endpoint pages, click the **Add new\...** button from the bottom of your space’s [table of contents](https://gitbook.com/docs/resources/gitbook-ui#table-of-contents).

From here, click **OpenAPI Reference**.
{% endstep %}

{% step %}
**Choose your OpenAPI spec**

Choose your previously uploaded OpenAPI spec, and click **Insert** to automatically add your endpoints to your space. You can optionally choose to add a models page referencing all your OpenAPI schemas.
{% endstep %}

{% step %}
**Manage your API operations**

GitBook will automatically generate pages based on your OpenAPI spec and the tags set inside it’s definition.

Head to [structuring-your-api-reference](https://gitbook.com/docs/api-references/guides/structuring-your-api-reference "mention") to learn more about organizing your operations through your OpenAPI spec.
{% endstep %}
{% endstepper %}

### Add an individual OpenAPI block

Alternatively, you can add OpenAPI operations or schemas from your spec individually to pages throughout your docs.

{% stepper %}
{% step %}
**Add a new OpenAPI block**

Open the block selector by pressing **/**, and search for OpenAPI.
{% endstep %}

{% step %}
**Choose your OpenAPI spec**

Choose your previously uploaded OpenAPI spec, and click **Continue** to choose your the endpoints you’d like to use.
{% endstep %}

{% step %}
**Choose the operations or schemas you’d like to insert**

Pick the operations and the schemas you want to insert in your docs and click **Insert**.
{% endstep %}
{% endstepper %}
