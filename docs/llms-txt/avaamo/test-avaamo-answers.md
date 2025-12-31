# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/test-avaamo-answers.md

# Test Answers skill

Once the documents or URLs are uploaded successfully to your skill, you can test to ensure the extracted knowledge provides appropriate responses for user queries. Further, you can view and fine-tune the knowledge base for providing more accurate responses.

{% hint style="info" %}
**Notes**:&#x20;

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can test skills immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/quick-start-tutorials/create-an-agent), for more information.
* If you wish to test an already created agent, then navigate to the Agents tab in the top menu, search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents#search-agents), for more information.&#x20;
* Currently, you can test the Answers skill only from the Agent page.
  {% endhint %}

**To test the skill:**

* In the Agent page, navigate to `Test -> Simulator` option in the left navigation menu. Alternatively, you can also test using the agent icon in the bottom right corner.
* You can now ask queries and test if you are receiving appropriate responses from user queries. Also, note that certain keywords from the user queries are also highlighted in the response.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FEh6emzIq0gUFxWE4qw5o%2Fimage.png?alt=media\&token=7efda156-ebad-4824-ac31-5d440ea8d2fd)

* Click `View More` to view the actual section in the document or the URL.&#x20;

{% hint style="success" %}
**Key Points**:&#x20;

* All the conversations are stored in the Conversation history and you can view the same to fine-tune the knowledge base. See [Conversation history](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents/conversation-history), for more information.
* The `View more` link is visible for all responses, except for cases where a document has been uploaded using the `QAExcelDocumentTemplate` parsing template. Also, note that for any other CSV/XLSX document, clicking the "View more" link results in downloading a local copy of the uploaded CSV or XLSX document. See [Parsing templates](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/parsing-templates), for more information.
  {% endhint %}

### Key points on "View more" Scrolling

If you have uploaded URLs (web pages) to the Answers skill, then the ability to scroll to a particular section in the webpage depends on the availability of one of the following in the webpage:

* **Permalinks**: If the website supports permalinks, then the same can be used in the "View more" link to land at the target section of the page. Example: <https://docs.avaamo.com/v5/#quick-starts>
* **Text search using (#:\~:text=)**: This requires browser support. In this case, the "View more" link scrolls and highlights the first occurrence of the specified text:
  * Chrome version 80 or above
  * Unique header or part of the text for a section of the webpage. Example: <https://docs.avaamo.com/v5/#:\\~:text=Quick%20Starts>.

### Key points on highlighting in Answer responses

The following are key points to note for highlighting in the Answer responses:

* Answer response highlighting works best when the user queries lead to direct answers from the knowledge base, typically, fact-based responses.
* Highlighting works best when there are user queries with full proper statements rather than just sub-phrases.&#x20;
  * Positive example: Where is the IT support desk?
  * Negative example: IT support desk
* The presence of extremely business-specific terminology reduces the probability of getting a highlighted response.
