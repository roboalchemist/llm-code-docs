# Source: https://docs.avaamo.com/user-guide/recent-releases/release-notes-v9.1.0/fix-patch-releases-v9.1.1.md

# Fix patch releases (v9.1.1)

This article summarizes a list of fix patch releases made in the Avaamo Conversational AI Platform version 9.1.1. The following are some of the key fixes included in this release:

1. [Custom formatting instructions for LLaMB responses](#custom-formatting-instructions-for-llamb-responses)
2. [Enhanced support for multilingual document ingestion](#enhanced-support-for-multilingual-document-ingestion)
3. [Enhanced document filters and statuses in DataSync](#enhanced-document-filters-and-statuses-in-datasync)
4. [Multilingual document ingestion support for DataSync](#multilingual-document-ingestion-support-for-datasync)
5. [SSO flow improvements for Microsoft Teams](#sso-flow-improvements-for-microsoft-teams)
6. [Enhanced security validation for SMS channel](#enhanced-security-validation-for-sms-channel)
7. [Response cutoff message translation](#response-cutoff-message-translation)
8. [Improved filtering options in the JS errors page](#improved-filtering-options-in-the-js-errors-page)
9. [File transfer capture support for custom live agent integrations](#file-transfer-capture-support-for-custom-live-agent-integrations)

### Custom formatting instructions for LLaMB responses

In this release, we are introducing `Custom Formatting Instructions` for LLaMB responses. This feature allows teams to define the tone, structure, and layout of every generated response, ensuring consistent communication that aligns with organizational guidelines and specific use-case requirements.

To configure custom formatting instructions, navigate to the `Advanced settings` section within the LLaMB skill page.

Click `Edit`

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FVQpI9e6GrcpdcmRqH06G%2FScreenshot%202025-11-18%20at%203.09.55%E2%80%AFPM.png?alt=media&#x26;token=5afb6970-9495-4bf5-9371-c409c1801f12" alt=""><figcaption></figcaption></figure>

After writing the message, click `Save`.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FvRE71GOeTEN1Yt532ah0%2FScreenshot%202025-11-18%20at%203.10.42%E2%80%AFPM.png?alt=media&#x26;token=8ed18489-3217-450e-82ed-61df45be344e" alt=""><figcaption></figcaption></figure>

Refer [Advanced Settings](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content), for more information.

### Enhanced multilingual document ingestion support for LLaMB

In this release, multilingual document ingestion is expanded to support documents uploaded via the platform UI, previously limited to API-based ingestion.

**Key enhancements include:**

**UI-based auto-detection control:** You can now enable or disable language auto-detection for all selected documents uploaded via the UI.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fxu90WPKxeUmO65l1qhJu%2FScreenshot%202025-11-19%20at%205.40.47%E2%80%AFPM.png?alt=media&#x26;token=90d68333-bb7b-465f-a541-5d5ec0301ac0" alt=""><figcaption></figcaption></figure>

**Language selection when auto-detection is off:** If you turn off auto-detection, you can manually select the document’s language from a dropdown. The dropdown displays all [languages configured](https://docs.avaamo.com/user-guide/configuration/language) for the agent, allowing accurate classification of the uploaded document.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FRaoNjm5g8iqCYgrNjVZP%2FScreenshot%202025-11-19%20at%205.40.17%E2%80%AFPM.png?alt=media&#x26;token=e9259298-23b7-4ecf-a784-e047264f3f4b" alt=""><figcaption></figcaption></figure>

**Header editing improvements:** For multilingual documents, the original header remains non-editable while the translated (English) header can be edited. English documents continue to behave as before.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F9Aum3VJj6LZkbiVjlO5T%2FScreenshot%202025-11-04%20at%2012.48.03%E2%80%AFPM.png?alt=media&#x26;token=e75d8d23-9d0f-4188-83e9-cba349751486" alt=""><figcaption></figcaption></figure>

**Original and translated view toggle:** A new toggle allows you to switch between the original and translated tables for easier review and editing.

<div align="left"><figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FwrQkgvqGqxsNzEI5GWSM%2FScreenshot%202025-11-20%20at%207.49.26%E2%80%AFAM.png?alt=media&#x26;token=36c55487-38af-4722-9cc4-010ac4878ddb" alt=""><figcaption></figcaption></figure></div>

### Enhanced document filters and statuses in DataSync

This release introduces multiple improvements to document filtering, status visibility, and ingestion transparency within the DataSync UI:

**Multi-select status filter:** A new multi-select dropdown lets users apply multiple document statuses simultaneously, enabling more flexible, efficient filtering.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FmfGWhTbCAjLfXkdsy0yC%2FScreenshot%202025-11-20%20at%201.06.44%E2%80%AFPM.png?alt=media&#x26;token=d0aef170-69c9-4f8d-943e-3acd35351d4e" alt=""><figcaption></figcaption></figure>

**New “Others” category in top statistics:** A new `Others` tile appears alongside existing categories, helping teams quickly identify document counts that do not fall under ingestion, failed, or progressing statuses. This ensures alignment between categorized counts and the total document count. The Others category count represents the combined total of all `Skipped` and `Warning` statuses.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fjv53z2P2JvuwNPPfaWhx%2FScreenshot%202025-11-20%20at%201.25.25%E2%80%AFPM.png?alt=media&#x26;token=ec8e4882-0277-4825-95ad-e9185750a0ef" alt=""><figcaption></figcaption></figure>

**Detailed status insights:** Hovering over **Warning**, **Error**, and **Skipped** statuses reveals the underlying issue or reason.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FpTJChZLzmV23oEzk3l1r%2FScreenshot%202025-11-20%20at%201.07.31%E2%80%AFPM.png?alt=media&#x26;token=2e138116-b1a0-44a3-8fa5-f32705564a23" alt=""><figcaption></figcaption></figure>

**Introducing the Skipped status:**\
The new `Skipped` status identifies documents that are intentionally ignored during the ingestion. This status includes a tooltip explaining why the content was skipped.

For example, suppose the content remains unchanged in Web, ServiceNow, or SharePoint sources between runs, whether triggered manually via Sync Now or via auto-sync. In that case, the system skips the ingestion process.

{% hint style="info" %}
**Key points:**

* URLs imported via CSV are always processed and marked as **Ingested**, and do not show **Skipped**.
* Force re-ingesting a single document from the menu overrides existing states, moving the document to **Ingested**.
  {% endhint %}

### Multilingual document ingestion support for DataSync

In this release, multilingual document ingestion is added to DataSync, allowing it to process documents in any language supported by the platform. You can now upload documents or files in any language supported by the platform, expanding flexibility for global and multilingual use cases.

You can also use the **Auto Detect Language** toggle if you want the system to automatically identify the language of the uploaded document.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fufekv242vgiY2dg5GrO5%2FScreenshot%202025-11-20%20at%202.06.30%E2%80%AFPM.png?alt=media&#x26;token=53b3739c-084d-4a58-91a1-822c5e9bff7e" alt=""><figcaption></figcaption></figure>

### SSO flow improvements for Microsoft Teams

In this release, the SSO flow for the **Microsoft Teams channel** has been enhanced as part of the transition away from the deprecated SDK and the upgrade to the new cloud adapter. These changes were necessary because Microsoft deprecated the previously used SSO process, requiring internal updates to maintain compatibility and provide a smoother authentication experience for users.

Refer [Deprecation details](https://learn.microsoft.com/en-us/azure/bot-service/what-is-new?view=azure-bot-service-4.0) from Microsoft for more information.

### Enhanced security validation for the SMS channel

In this release, an extra security layer has been added to the SMS channel to verify the authenticity of requests originating from Twilio. This enhancement improves protection against unauthorized or spoofed traffic and ensures more reliable message handling.

### Response cutoff message translation

In this release, the **Response Cutoff Message** is automatically translated based on the user’s query language. This ensures a consistent and seamless multilingual experience, allowing users to receive cutoff notifications in the same language as their interaction.

### Improved filtering options in the JS errors page

In this release, enhanced filtering capabilities have been added to the **JS errors** page. Users can now filter errors by type, such as **Warning** or **Error,** making it easier to isolate specific issues, focus on relevant problem areas, and streamline debugging and analysis.

Additionally, file exports now include **only the log results that match the currently applied filter**, ensuring clean, relevant, and targeted exports for further review or reporting.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F94LSCKwVpVFYAFzE2dsj%2FScreenshot%202025-11-18%20at%2012.51.30%E2%80%AFPM.png?alt=media&#x26;token=13f424d6-5521-485a-b782-22c3707a5f61" alt=""><figcaption></figcaption></figure>

Refer [JS errors](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents/js-errors), for more information.

### **File transfer capture support for custom live agent integrations**

In this release, support for capturing file transfers in custom live agent integrations has been introduced. Previously, file transfer events were not recorded. With this enhancement, all file transfers are now fully tracked to provide complete visibility into conversation activity.
