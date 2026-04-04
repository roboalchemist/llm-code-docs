# Exports

Your model data (domains, objects, connections, flows, tags, etc.) can be exported as JSON, CSV, SVG, PNG, and PDF. We recommend using [Share links & embeds](https://docs.icepanel.io/collaboration/sharing) if you want to share diagrams with team members since they'll always remain up-to-date.

{% hint style="info" %}
Data can be exported in-app and also using our [rest-api](https://docs.icepanel.io/integrations/rest-api "mention").
{% endhint %}

## Full model export (JSON)

You can export your full model in a landscape or diagram to JSON. This will include all information in your model, from objects to connections to granular metadata.&#x20;

Top-level information in the export:

* Domains
* Flows
* Model connections
* Model objects
* Tag groups
* Tags
* Teams

To export your model as JSON:

1. Click on the `Share` button on the top right of the navigation bar.
2. Click on the `Export` tab.
3. Select the `JSON` as the file type.
4. Select whether you want to export the Landscape or Diagram.
5. Click download.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FffFadQKyYRE9x15CHZmh%2FScreenshot%202024-10-02%20at%2012.14.00%E2%80%AFPM.png?alt=media&#x26;token=2cb899f3-7462-4f5a-84e8-1222899e2eb9" alt=""><figcaption><p>Exporting an entire model in JSON</p></figcaption></figure>

{% file src="<https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FUXHqzoNQ9uxf9SFptWPZ%2FIcePanel%20Platform.json?alt=media&token=1178fd68-6d6d-489f-9b11-6a23bf2fa6df>" %}
Example JSON export
{% endfile %}

## Full model summary (PDF, Markdown, HTML, LLMs.txt)

You can also export a summary of your model, which can be helpful to share with external stakeholders or an LLM. This export contains model objects, flows, tags, and teams in the selected scope.

To export a summary of your model:

* Click on the `Share` button on the top right of the navigation.
* Click on the `Export` tab.
* Select `PDF`, `Markdown`, `HTML`, or `LLMs.txt` as the file type.
* Select the orientation (Portrait or landscape).
* Select the scope of the export (landscape, domain, model object, or diagram).
* Click download.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FAHekEfyYLb7TSHd6iVwb%2FScreenshot%202025-05-13%20at%202.39.47%E2%80%AFPM.png?alt=media&#x26;token=abbf9dbb-1cd8-4e45-8bf7-74183d2ffaa1" alt=""><figcaption><p>PDF exports</p></figcaption></figure>

{% file src="<https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FSZudN3PZaztjXMAKJsAk%2FIcePanel%20Platform%20Export.pdf?alt=media&token=1cc62fdf-62bb-4b58-a0c7-c6f66d55b09a>" %}
Example PDF export
{% endfile %}

## Model objects (CSV)

To export model objects in a landscape:

1. Click on the `Share` button on the top right of the navigation.
2. Click on the `Export` tab.
3. Select `CSV` as the file type.
4. Select `Model objects` under contents and click download.

This will give you a list of objects in the landscape with metadata similar to the full JSON export. Connections or flows will **not be included**.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FAXZ92REqBXQbBkSpuVGS%2FScreenshot%202024-10-02%20at%201.25.34%E2%80%AFPM.png?alt=media&#x26;token=ebf95006-de59-4621-928c-b5f1578f6d9a" alt=""><figcaption><p>Exporting model objects as CSV</p></figcaption></figure>

### Export fields

* Identifier
* Belongs Inside System
* Belongs Inside App
* Belongs Inside Store
* Object Name
* Object Type
* Object Status
* Object External
* Object Displayed Description
* Object Tags
* Object Technology
* Object Teams
* Object Link
* Object Share Link
* Object Description

## Model connections (CSV)

To export model connections in a landscape:

1. Click on the `Share` button on the top right of the navigation.
2. Select `CSV` as the file type.
3. Select `Connections` under contents and click download.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FJEPX4VBfejxdWa40oIHB%2FScreenshot%202024-10-02%20at%201.28.00%E2%80%AFPM.png?alt=media&#x26;token=5975a88f-70e9-4f92-9134-ed8fe413d358" alt=""><figcaption><p>Exporting connections as CSV</p></figcaption></figure>

### Connection Export fields

* Identifier
* Sender Belongs Inside
* Sender Object Name
* Sender Object Type
* Sender Object External
* Sender Object Tags
* Sender Object Technology
* Sender Object Teams
* Connection Name
* Connection Status
* Connection Direction
* Connection Tags
* Connection Technology
* Connection Description
* Receiver Belongs Inside
* Receiver Object Name
* Receiver Object Type
* Receiver Object External
* Receiver Object Tags
* Receiver Object Technology
* Receiver Object Teams

## Diagram export  (SVG or PNG)

Diagrams can be exported as SVG or PNG in light or dark themes.

To export a diagram in this format:

1. Navigate to the diagram you want to export.
2. Click on the `Share` button on the top right of the navigation.
3. Click on the `Export` tab.
4. Select  `SVG` or `PNG` as the file type.
5. Select `Light` or `Dark` for the theme and click download.

{% hint style="warning" %}
If downloads aren't working, we recommend disabling any pop-up blockers in your browser.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F6RPuLNwc3ramHZqLE67y%2FScreenshot%202024-10-02%20at%201.28.47%E2%80%AFPM.png?alt=media&#x26;token=accb71c6-39a2-4420-9bdb-bce5a6f80401" alt=""><figcaption><p>Exporting diagram PNGs</p></figcaption></figure>

### Example SVG export

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FoDr3TLKdTxaDKftFpWex%2FContext%20Diagram%201%20(Latest).svg?alt=media&#x26;token=f63ee024-7f24-46e5-931e-9e7cbb579458" alt=""><figcaption><p>Dark theme</p></figcaption></figure>

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FCtEY2qTcm5cDg5aG7aOB%2FContext%20Diagram%201%20(Latest)%20(1).svg?alt=media&#x26;token=8e9a6a40-3747-4c55-9510-98fda4ae775d" alt=""><figcaption><p>Light theme</p></figcaption></figure>
