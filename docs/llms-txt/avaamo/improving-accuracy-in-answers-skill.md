# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/improving-accuracy-in-answers-skill.md

# Improving accuracy in Answers Skill

There are some important techniques that can be used to improve the accuracy of the Answers skill.

### Appropriate parsing templates

Accuracy in Answers skill is directly related to how precisely the extraction happens. This extraction completely depends on the parsing templates that are being used. Specially in HTML pages where there are header, footers, and navigation panels, it is important to identify the main content for extraction and use the appropriate parsing template. If the available templates do not work well, it is necessary to create custom templates.

Before using a parsing template for bulk upload of documents, it is recommended to try it out with a few documents and check if the extraction works fine.

### Use APIs for bulk content upload&#x20;

Whenever the volume of content to be ingested is large, such as content from CMS, it is better to use APIs to integrate with the CMS.&#x20;

Using APIs for bulk content upload has the following advantages:

* Avoid the creation of parsing templates.
* Avoid the necessity to update maintain parsing templates to match the user interface - in cases  where the design of the web pages changes.&#x20;
* Integration with the source system using API allows the knowledge base to be updated as and when the source content is updated.

### Adding custom domain-related terms

Adding domain-related terms as synonyms to words in the uploaded content. Sometimes, the answers skill may not be able to extract responses because terms and verbiages in the content might not be domain-specific. Adding domain-related terms as synonyms can improve accuracy. For examples, using synonyms like card, chip or processor when the content is about CPUs, the system can extract the relevant information easily.

### Using disambiguation strategies

Disambiguation is the ability of the agent to distinguish between similar responses based on the context of a chat conversation. For example: The security policy for an organization may be different based on region. When an agent is able to perform disambiguation, the agent can categorize security policies based on regions - thereby improving accuracy in the chat conversation.

You can disambiguate using:

* Attributes: See [Defining attributes for documents or URLs](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/manage-avaamo-answers-1/perform-common-actions#defining-attributes-for-documents-or-urls)
* Acronyms: See [Disambiguation](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/configure-answers-skill#disambiguation)
* Training data: See [Disambiguation](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/configure-answers-skill#disambiguation)
