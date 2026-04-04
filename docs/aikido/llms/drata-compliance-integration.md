# Source: https://help.aikido.dev/compliance-and-reporting/iso-27001-and-soc-2-compliance-overview/drata-compliance-integration.md

# Drata Integration

### API Key <a href="#api-key" id="api-key"></a>

You'll need to create a Drata API Key. You can generate such key in Drata via [Username > Settings > API Keys > Create API Key](https://app.drata.com/account-settings/api-keys/add).

#### Details <a href="#details" id="details"></a>

Make sure the Expiration is set to 'Never Expires'.

![API key setup screen with fields for name, expiration, and allowed IP addresses.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-ce2ced2d8afd26e882bfa10b9544644878a5613f%2Fdrata-compliance-integration_434c3577-6525-4dd7-bd05-3d8542874506.png?alt=media)

#### Scopes <a href="#scopes" id="scopes"></a>

The access for the scopes can be set to 'Custom' with at least following scopes.

**Controls:**

* **Controls list:** *Read*
* **Add control:** *Write*
* **Map external evidence:** *Read, Write*
* **Delete mapped external evidence:** *Write*

**Workspaces:**

* **List workspaces:** *Read*

**Frameworks:**

* **List frameworks:** *Read*
* **List framework requirements:** *Read*

![User permissions matrix for controls, workspaces, and frameworks management.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-56e43412287c1f066db5b5b63fad51eb21fd6351%2Fdrata-compliance-integration_34731256-9c26-4160-a673-b0c3ab16d664.png?alt=media)

#### Save <a href="#save" id="save"></a>

Next, click 'Save' and copy your generated API Key.

Back in Aikido, paste the API Key and click 'Next'. After that, choose your Drata workspace and click 'Save'.

![Enter your Drata API Key to integrate data and proceed to the next step.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-28b8f7c905281f4c5b11bd356e166ce42e85430d%2Fdrata-compliance-integration_650bf49f-49d4-4848-8513-f93aaa9f8a47.png?alt=media)

### Done <a href="#done" id="done"></a>

Aikido will now daily create a PDF report and sync this as 'external evidence' to Drata. We'll create a control with code 'AIKIDO' and link the relevant SOC2 and ISO27001 requirements. You can search for this control [here](https://app.drata.com/compliance/controls/inscope?q=Aikido).

Under 'Control evidence', the Aikido PDF will be attached every month

#### &#x20;<a href="#set-up-drata-integration" id="set-up-drata-integration"></a>
