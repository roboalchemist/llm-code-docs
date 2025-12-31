# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/configure-answers-skill.md

# Configure Answers skill

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can manage a skill immediately after creating the skill. See [Create new Answers skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/create-new-knowledge-base), for more information.
* If you wish to edit skill in an agent, then:
  * Navigate to the Agents tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents#search-agents), for more information.&#x20;
  * Click Edit to unlock the agent before editing.
  * In the Agent page, navigate to the Skills option in the left navigation menu. Search and open the required skill.&#x20;
    {% endhint %}

In the **Answers skill** page, navigate to the **Configuration** option in the left navigation menu to view the configuration options. Configuration options in the Answers skill help you to fine-tune your agent's responses.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FxLmRGdIOCjSYFwWV0fC6%2Fimage.png?alt=media&#x26;token=64fc2189-c65e-494f-a1f6-baaebdf6df45" alt=""><figcaption></figcaption></figure>

### **Acronym Intro Message**&#x20;

If this configuration option is selected, any acronyms from a user's query are first expanded in the response. This allows the user to know how the agent has expanded the acronym.&#x20;

For example, if the user types 'What is ISP?'. The agent would first respond 'I am assuming by ISP you mean Internet Service Provider'.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FzsLYCp4ldW0TtICGOfrp%2Facronym.png?alt=media\&token=41bf4283-d071-43c1-a3e9-4b1fecbf04fc)

If this configuration option is not selected, the agent directly responds to user queries that have acronyms without expanding them first. By default, the Acronym Intro Message option is selected.

### **Response type**&#x20;

You can configure the default UI element to be used to display responses. You can choose between the accordion UI element or the Carousel UI element. If Accordion is selected, the main response is displayed using one main card and additional responses using expandable/collapsable links within another card. \
\
If Carousel is selected, the response is displayed using a Carousel. See [Skill Messages](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-skill-messages-responses) for more information on UI elements. By default, the Accordion view is selected.

{% hint style="info" %}
**Note**: The **Accordion** view is not supported in the Microsoft Teams channel due to limitations on the channel's side; the Carousel view is displayed instead.

See [Microsoft Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information on deploying your agent in the MS Teams channel.&#x20;
{% endhint %}

### **Feedback**

Choose **Enable Feedback** if you want to provide the option for users to give feedback on responses using thumbs up or thumbs down. Enabling this option allows you to track users' satisfaction with responses from your Answers skill. By default, Feedback is selected.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FvUhDbMfA7x89aE3gIHF2%2Fcollect-feedback.png?alt=media\&token=a16777c8-645c-409e-ad64-cec8929b7a44)

### **Render as HTML**

Select this option if you want to use rich HTML for the styling content in cards instead of plain text. \
By default, Render as HTML is selected.

### Use document name for card title

This option allows you to enable or disable displaying of the document title in the agent response when the response is rendered as HTML. When you disable **Use document name for card title** toggle, then document title is not displayed and only the section header is displayed in the agent response. See [Sections](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/manage-avaamo-answers-1/view-and-edit-knowledge#sections), for more information.

{% hint style="info" %}
**Notes**:&#x20;

* This option works only when **Render as HTML** option is enabled.
* By default, in a newly created Answers skill, **Render as HTML** and **Use document name for card title** toggle options are enabled.
  {% endhint %}

| Use document name for card title = enabled                                                                                                                                                                                                       | Use document name for card title = disabled                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FNoJevvhNgp8C87GU7SsU%2F6.2-answers-document-title-enabled.png?alt=media\&token=05401d6a-a76d-4b75-999b-0884f8b0795a) | ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FrCqsBU8aWOo6r7T6QugH%2F6.2answers-document-title-disabled.png?alt=media\&token=9734fe2b-9ca4-4ec5-8916-41d6735c73fb) |

### **Trim text response**

Select this option if you want only the most relevant few lines from the response to be displayed instead of the whole section. The **Trim text response** toggle is used and applicable only for PDF content and has no effect on the HTML content.

### **De-duplicate response**

If there are multiple responses from the same document to a question, select this option to have all the responses combined into one single card. \
\
For example, for the question "How to book my flight ticket?", the document may have multiple options such as 'Booking from an agency' and 'Booking from our website'. If you want all the information to be displayed in a single card, choose this option. If you want each of the options to be displayed in different cards, do not choose this option.\
\
In occasions where the same information is repeated more than once in a document, selecting this option is useful to combine all the information into the same card. By default, the 'De-duplicate response' option is selected.

### **Open in New Tab**

Responses from Answer's skill usually have a **View More** link at the bottom of the response.&#x20;

If the **Open in New Tab** option is selected, clicking the **View More** link displays information in a new tab in the current browser window. If this option is not selected, clicking the **View More** link displays the information in an independent iframe.

This is specifically helpful for authenticated webpages - where enabling this option opens the page in another tab if the user is already signed in; if this option is not enabled, the login page is displayed in an iframe.\
\
By default, the **Open in New Tab** option is not selected.

### **Use Preview App**

Responses from Answers skill usually have a **View More** link at the bottom of the response. When this option is selected, a copy of the relevant webpage is loaded onto an iframe on clicking **View More**.&#x20;

This is specifically helpful for websites that have security restrictions on iframe loading.\
This option cannot be enabled when the **Open in New Tab** option is enabled. By default, this option is disabled.

### Display single table row

Select this option when you only want the row (instead of the entire table) that has the response to the user's question to be extracted and displayed along with the column names. In this case, only the single but entire row that has the response will be extracted and listed such that the information in each cell in a row is displayed against the column name.

Benefits of displaying only a single row instead of the entire table:

* Allows the user to get a precise response.
* Eliminates the need to scroll through the table to locate the information.
* Allows information to be displayed clearly (without clutter and formatting issues) as there is just one row to be displayed. In addition, the column name against each cell provides a quick and easy understanding of the information displayed.

The following illustration depicts the difference between a full table display versus a single table row display in the Answers response for the same user query

|                                                                                                              Full table                                                                                                             |                                                                                                          Single table row                                                                                                          |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FFzLEie8bfwh6qtsAdJlB%2F6.x-tabular-answering.png?alt=media\&token=b0081f22-a83d-4862-84f0-b069771cff47) | ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FXQ88xrsqtYZUg4dMipKG%2F6.x-single-table-row.png?alt=media\&token=ec392826-b543-4fcd-9c35-6e8a1f9c42d8) |

### Display concise tabular answer

Select this option when you want the responses from tables to be extracted and displayed as plain text - making the response conversational and easy to understand.&#x20;

For example, the response to the query 'what is the IPO of burger king' is in a table. When this user query is posted to the agent, the response is extracted from the table and displayed as a sentence. The corresponding table from which the information is extracted is displayed below the generated sentence.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FkZkskVd0xm77hziOZlQ1%2F6.x-display-generative-answer.png?alt=media\&token=599a47d6-080f-48f0-9358-3d65ffe9b76a)

If this option is not selected, the entire table that contains the response is displayed and the specific response is highlighted.

### Translation configuration

The Translation configuration options are useful when you have the same content uploaded in multiple languages. It helps you to display relevant responses to the users based on the business requirement and languages of the uploaded document. The following options are available in the Configuration -> Translation section:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FOrI7wTmO3HsJjMa1JezO%2Fimage.png?alt=media&#x26;token=84da198c-4e7f-4b6f-8430-5fd9996d24fd" alt=""><figcaption></figcaption></figure>

* **Get responses only from documents in the query language**: Display responses only from the documents in which the user query is posted.
* **Fallback to all documents**: If the response is not available in the user query language, then translated response, if available in another language document is displayed. By default, this toggle is enabled and functional only when the **Get responses only from documents in the query language** toggle is enabled.&#x20;

{% hint style="info" %}
**Note**: By default, in a newly created Answers skill the toggle **Get responses only from documents in the query language** is disabled.
{% endhint %}

Consider that you have the same content uploaded in English and French.&#x20;

**Example 1**: &#x20;

* Get responses only from documents in the query language toggle = Enabled
* Fallback to all documents = Enabled
* User asks a question in French and the response is available in the French document
* **Result**: Agent response from the French document is displayed

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FcLZs4AVUVm3dGhiDA61N%2F6.1-answers-lang-conf-example-1.png?alt=media\&token=7df921a9-990d-407b-a27f-d662fb061062)

**Example 2**: &#x20;

* Get responses only from documents in the query language toggle = Enabled
* Fallback to all documents = Enabled
* User asks a question in French but the response is not available in the French document and is available in English content.
* **Result**: Agent response from the English document is translated to French and displayed to the user&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FNNXcH2dJOC7N4JIiNgom%2F6.1-answers-lang-conf-example-2.png?alt=media\&token=5c6d3867-88d7-4a0e-a044-0ea4390ae1e6)

**Example 3**:&#x20;

* Get responses only from documents in the query language toggle = Enabled
* Fallback to all documents = Disabled
* User asks a question in French and the response is available in the French document.
* **Result**: Agent response from the French document is displayed

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FcLZs4AVUVm3dGhiDA61N%2F6.1-answers-lang-conf-example-1.png?alt=media\&token=7df921a9-990d-407b-a27f-d662fb061062)

**Example 4**:&#x20;

* Get responses only from documents in the query language toggle = Enabled
* Fallback to all documents = Disabled
* User asks a question in French but the response is not available in the French document and is available in English content.
* **Result**: Unhandled response&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F6QplKW7OXOFBAgyIvv2O%2F6.2-answers-lang-conf-example-4.png?alt=media\&token=7d36fe1f-6ced-4ead-b9f9-96fcfe7a27fa)

### Answering mechanism

This option allows you to select a relevant model to be used by the Platform for providing agent responses based on the content type in your knowledge base. The platform uses the selected model to optimize the response and hence results in better accuracy.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FnCCroACAwLMi48HbFTlT%2F6.2-configure-answering-mechanism.png?alt=media\&token=8c40c85f-b895-4b62-96e2-25ca6104d3c6)

The following options are available:

<table><thead><tr><th width="150">Mechanism</th><th width="604.4285714285713">When to use?</th></tr></thead><tbody><tr><td>Default</td><td>For all types of content. This is the default selected mechanism for any newly created Answers skill.</td></tr><tr><td>NLP Boost</td><td>Best suited for small to medium-sized Answers skills (upto 4000 chunks). If the document is large, then it is recommended to set the <code>Answering mechanism</code> to the <code>Default</code> option.</td></tr><tr><td>Legacy</td><td>Also works for all types of content and is selected for Answers skills created earlier to the <a href="../../../../release-notes/v6.0-to-v6.4.x-releases/v6.2.x/release-notes-v6.2.0">v6.2.0 release</a>. Using the Default model is a better option.</td></tr></tbody></table>

### **Search as fallback**

When this option is selected, the answer skill attempts to find the best possible responses for a query when an accurate response is not available. In other words, when no accurate responses are found, a simple search is performed to find any related content that may produce possible responses.&#x20;

### **Disambiguation**&#x20;

Disambiguation is the ability of the agent to distinguish between similar responses based on the context of a chat conversation. For example: Security policy for an organization may be different based on region. When an agent is able to perform disambiguation, the agent can categorize security policies based on regions - thereby improving accuracy in the chat conversation.

**Disambiguate using acronyms:** If this option is selected, the agent disambiguates between acronyms that can be expanded in more than one way. The agent provides the full forms of the acronym for selection. \
\
The agent uses the acronyms listed under the Acronyms tab in the knowledge base to perform this disambiguation. If your acronym is there in your knowledge base but is not extracted as an acronym and listed under the Acronyms tab, the agent does not disambiguate. See [Acronym](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/manage-avaamo-answers-1/view-and-edit-knowledge#acronyms) for more information.\
\
For example, API can be expanded as Application Programming Interface or American Petroleum Institute. When the user's query has the term API, both the expansions are displayed for the user to choose. By default, this option is enabled.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FDEvG1hX5c25Ry7ZIJBBA%2Facro-disamb.png?alt=media\&token=0d08926c-10d3-423c-9ccc-e793b90374a4)

### **Filter responses based on query keywords**

Select this option when you want to prioritize responses that have words that closely match the keywords used in the query. This option is provided with the intention to encourage responses that contain exact query keyword matches - thereby discouraging responses that do not contain direct matches.\
By default, this option is disabled.\
\
This option can be combined with the **Use Strict** option to do a strict filter on responses based on query keywords.

### **Strict Attribute Match**&#x20;

Select this option when you want responses to be filtered exclusively based on attributes. This means that only responses from the knowledge base that match the attributes in context is displayed. If no responses are found that match relevant attributes, the agent notifies the user accordingly.
