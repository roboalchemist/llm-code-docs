# Source: https://docs.avaamo.com/user-guide/llamb/multi-language-support.md

# Multi-language support

### Multi-language support in LLaMB responses

LLaMB enables seamless, real-time conversations in multiple languages, enhancing the user experience across diverse regions. With real-time streaming translation, LLaMB supports all languages available in the Avaamo Conversational AI Platform.

Users can interact with the agent in any supported language, and the agent will respond in the same language, even if the original content is authored in English. This eliminates the need to maintain separate content for each language, simplifying content management while ensuring a natural and fluid conversation flow.

By leveraging this capability, organizations can effortlessly expand their global reach, providing a consistent and localized experience for users worldwide.

Below is a sneak peek of LLaMB’s multi-language support in action. You can see how responses are generated in the respective languages when the same question is asked in English (en-US) and French (fr-FR).

<div align="left"><figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FeCrOnII6xB1f9oYQHZga%2FScreenRecording2025-04-08at11.43.42PM-ezgif.com-video-to-gif-converter%20(1).gif?alt=media&#x26;token=b34a02d1-29e8-4363-9646-c9c536f92fbb" alt="" width="375"><figcaption></figcaption></figure></div>

Follow these steps to enable and test multilingual support in your LLaMB agent:

1. **Ingest content in English:** Prepare and ingest your documents in English. Document ingestion currently supports only the `en-US` locale. Refer [Ingest enterprise content](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content), for more information.
2. **Enable markdown format:** Ensure that the Markdown format is enabled for your agent in the channel configuration. Refer [Enable markdown format](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/advanced#enable-markdown-format), for more information.
3. **Add languages to your agent**
   * Navigate to `Configuration > Language`.
   * Click `Add Languages`.
   * Select the desired language(s) from the dropdown list.
   * Click `Save`. Refer [Languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-languages), for more information.
4. **Test multilingual capability in simulator**
   * Open the [Simulator](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/simulator).&#x20;
   * Initially, ask a question in English — you will receive responses in English.
   * To switch the language, use the command:\
     `#switch_lang <language_code>` *For example: `#switch_lang fr-FR` to switch to French.*
   * After switching, ask a question in the selected language. The agent will respond in the same language.&#x20;

### Support for multilingual document ingestion

LLaMB supports multilingual document ingestion, allowing you to upload, train, and query documents in multiple languages. This capability improves accessibility, accuracy, and global usability by enabling the system to process content and respond in the user’s selected conversation language.

LLaMB can automatically detect a document's language during ingestion, eliminating the need to specify it in the request payload manually. This reduces errors, speeds up processing, and ensures more reliable handling of non-English content.

{% hint style="info" %}
**Note:** Automatic language detection is available only for API-based document ingestion.
{% endhint %}

If you provide a language parameter during ingestion, LLaMB uses that language for extraction. If no language is provided, LLaMB automatically identifies the document’s language and processes it accordingly. Refer [Upload content](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/upload-content) and [Content ingestion APIs](https://docs.avaamo.com/user-guide/llamb/llamb-rest-apis/content-ingestion-apis), for more information.

If no language is specified, LLaMB detects the document’s language during ingestion.

```javascript
curl --location 'https://c6.avaamo.com/llamb-content-skill/content-ingestion/upload-file' \
--header 'access-token: 238c2e50cxxxxae0def75b223' \
--form 'source=@"/Users/Downloads/swedish-document.pdf"' \
--form 'document_group_id="9xx5"' \
--form 'type="pdf"'
```

If you provide a language code, LLaMB uses the specified language and does not perform auto-detection.

```javascript
curl --location 'https://c6.avaamo.com/llamb-content-skill/content-ingestion/upload-file' \
--header 'access-token: 238c2e50cxxxxae0def75b223' \
--form 'source=@"/Users/Downloads/swedish-document.pdf"' \
--form 'document_group_id="9xx5"' \
--form 'type="pdf"' \
--form 'language="es-ES"'
```

### Key points

* **Language-aware ingestion:** You can specify the document’s language by passing the appropriate language code (for example, `es-ES`, `fr-FR`, `sv-SE`) during ingestion.
* **Agent configuration:** Add or configure the target language in the agent settings before ingestion to ensure proper processing and response handling.
* **Comprehensive file support:** Multilingual ingestion works with all supported document types, including PDF, Word, Excel, PowerPoint, CSV, and HTML.
* **Cross-language querying:** LLaMB can understand and respond to queries in English, the document’s original language, or any other supported non-English language, depending on the user's selected conversation language.
