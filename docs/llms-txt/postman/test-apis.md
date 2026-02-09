# Test API functionality and performance in Postman

Testing is a critical part of the API development lifecycle. Testing confirms that API endpoints, methods, and integrations work as expected and that your API can meet the expected load.

Here are some of the essential types of API testing you can perform in Postman:

* **Integration testing** - Observe data flow and test compatibility between the various components in your application. You can also test how your application interacts with other systems. Learn more at [Test API integrations and data flow in Postman](/docs/tests-and-scripts/test-apis/integration-testing/).
* **End-to-end testing** - Simulate complex user operations from start to finish to test real-world workflows. End-to-ending testing makes sure the entire system works as expected and helps identify problems with user experience. Learn more at [Test end-to-end API workflows in Postman](/docs/tests-and-scripts/test-apis/end-to-end-testing/).
* **Regression testing** - Make sure updates and improvements to your application don't introduce any new defects or issues. Regression testing supports the overall quality of your API by ensuring code changes are backwards compatible. Learn more at [Test your APIs for regressions in Postman](/docs/tests-and-scripts/test-apis/regression-testing/).
* **Performance testing** - Simulate real-world traffic to your application with virtual users. Each virtual user sends a series of requests to your API, so you can observe how your API behaves under load. Learn more at [Test your API's performance in Postman](/docs/tests-and-scripts/test-apis/performance-testing/).

To explore recommended testing types across different API patterns, see [best practices for API test automation in Postman](https://www.postman.com/postman-best-practices/api-test-automation/).

## Postman Vault integrations

Integrate your Postman Vault with Postman Flows to enable you to link vault secrets with secrets that are stored in an external vault. You can then reference vault secrets in your Postman team, and retrieve the value of external vault secrets using end-to-end encryption when you send HTTP requests.

Postman supports the following Postman Vault integrations:

* [1Password](/docs/sending-requests/postman-vault/1password/)
* [AWS Secrets Manager](/docs/sending-requests/postman-vault/aws-secrets-manager/)
* [Azure Key Vault](/docs/sending-requests/postman-vault/azure-key-vault/)
* [HashiCorp Vault](/docs/sending-requests/postman-vault/hashicorp-vault/)

You can create Postman Vault integrations from the Postman desktop app, and you can also create an integration from the Postman web app.

## Feature availability

The following features require the Postman desktop app:

* **Open Postman Vault from public workspaces** - You must use the Postman desktop app to open your Postman Vault from a public workspace. If you're using the Postman web app, you must add new vault secrets to your Postman Vault if you're opening it from a public workspace.
* **Create and manage Postman Vault integrations** ([Enterprise teams only](https://www.postman.com/pricing/))

## Troubleshoot vault secrets

Postman's Secret Scanner scans public workspaces and published documentation to detect exposed secrets on all Postman plans.

Postman's Secret Scanner actively scans for secrets in the following Postman elements when changes are made:

* HTTP collections
* Environments variable values
* Global variable values

Postman's Secret Scanner scans public workspaces and published documentation to detect exposed secrets on all Postman plans.

Postman also identifies governance issues for components, but only once they're [referenced in your specification](#reference-a-component-in-a-specification).

## Version and publish a component file

Publish a version of a component file to share the latest changes to your reusable components with your team. Versioning component files is useful for publishing a new version of your reusable components, while still supporting earlier versions. You can't edit versions once they're published.

You can't delete published versions of component files.

## Reference a component in a specification

Reference reusable components in your OpenAPI specifications using the URL to the component and its version. A component file must have a [published version](#version-and-publish-a-component-file) before you can reference its components in your specifications.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/local-secret-protection/#edit-workspace-details).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation as you edit your component file. To show the documentation preview, click [![Image 1: Docs icon](https://assets.postman.com/postman-docs/aether-icons/state-info-stroke.svg#icon)](#view-live-documentation) **Live preview** in the right sidebar. Click [![Image 2: Close icon](https://assets.postman.com/postman-docs/aether-icons/action-close-stroke.svg#icon)](#close) to hide the documentation preview.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance