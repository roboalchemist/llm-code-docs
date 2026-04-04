# Source: https://docs.avaamo.com/user-guide/live-agent-console/supervisor/quick-responses.md

# Quick responses

In the context of a live agent system, Quick responses, also known as canned responses or predefined messages are pre-written replies or messages that agents can use to quickly respond to common customer inquiries or issues.&#x20;

### How do Quick Responses help?

The following are a few points that list the benefits of having quick responses in your organization:

* **Efficiency and Speed**: Quick responses enable agents to respond rapidly to customer queries, reducing response time and improving overall customer satisfaction. Agents can select relevant pre-written responses instead of typing out full replies, saving valuable time during interactions.
* **Consistency**: Quick responses ensure consistency in customer service. By using predefined messages, agents can deliver accurate and standardized information across multiple conversations.&#x20;
* **Accuracy and Quality**: Quick responses are crafted by business owners or supervisors, ensuring that they contain accurate and reliable information. Agents can rely on these pre-approved responses to provide customers with correct answers, minimizing the chances of errors or misinformation. This helps in maintaining a high level of quality in customer support interactions.
* **Complex or Technical Issues**: Some customer inquiries may involve complex or technical information that agents need to communicate accurately. Quick responses can be specifically designed to address such issues, ensuring that agents have access to well-constructed explanations or solutions.&#x20;
* **Training and Onboarding**: Quick responses can help during live agent training and onboarding processes. New live agents can familiarize themselves with common customer queries and their corresponding responses, helping them learn the ropes quickly.&#x20;
* **Empathy to sensitive situation**s: Quick responses can also be designed to address emotional or sensitive situations. Agents can have predefined messages that show empathy, understanding, or apology, helping them handle delicate customer interactions with care and professionalism.

### View all quick responses

* Click `Settings -> Avaamo Live Agent` in the Avaamo dashboard home page to view the Supervisor interface.
* Click `Settings icon -> Quick Responses` page in the left navigation pane of the Supervisor interface to view all the quick responses in your organization.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FkGvvIZNRMyrB0ddtarx3%2Fimage.png?alt=media&#x26;token=bc116ef4-5b24-416b-8446-4dc440850d43" alt=""><figcaption></figcaption></figure>

* By default, the quick responses are displayed in descending order, organized according to their creation time, which implies that the last created quick response appears first in the list.
* Each row in the list provides essential information about a quick response, including the `Quick response name` and the message corresponding to the name.

### Create a new quick response

* Click `Settings -> Avaamo Live Agent` in the Avaamo dashboard home page to view the Supervisor interface.
* Click `Settings icon -> Quick Responses` page in the left navigation pane of the Supervisor interface to view all the quick responses in your organization.
* In the `Quick Responses` page, click `Create Quick Response` and specify the following details:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FGwGXIJC5YVHLBG3DUhs1%2Fimage.png?alt=media&#x26;token=af4bb311-119f-4281-9761-b806180e3429" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="154.44475920679886">Parameters</th><th width="440.798167959476">Description</th><th align="center">Maximum length</th></tr></thead><tbody><tr><td>Quick response</td><td><p>Indicates the name of the quick response. Specify a name that clearly identifies the team, making it easier to associate and add new live agents to the team. </p><p></p><p>Supported characters: Quick response must start with an alphabet and can contain only alphabets, numbers, or underscores. </p><p></p><p>Quick response name must be unique which implies that there is only one name for one template.</p></td><td align="center">20 characters</td></tr><tr><td>Template</td><td><p>The actual text of the quick response. This is the text displayed when you type a quick response name. You can make the messages personalized by leveraging the values from the <a href="../../how-to/build-skills/create-skill/customize-your-skill/reference-library/context/user">context.user</a> and <a href="../../how-to/build-skills/create-skill/customize-your-skill/reference-library/context/user-1">context.live_agent_user</a> objects. </p><p></p><p>For example, you can use first name and last name from the custom user properties and make the message dynamic and personalized.</p><p></p><p>Hello, ${context.user.custom_properties.first_name} ${context.user.custom_properties.last_name}, thank you for contacting us. I am ${context.live_agent_user.first_name}, your Sparsh Healthcare customer care assistant. How can I help you today?</p></td><td align="center">5000 characters</td></tr></tbody></table>

* Click **Save** to complete the creation of the new `Quick response`. Currently, the platform offers the ability to create an unlimited number of quick responses for an account.

### Edit quick response

You can edit the `Quick response` and template from the `Supervisor -> Quick Responses` page.

* Click `Settings -> Avaamo Live Rgent` in the Avaamo dashboard home page to view the Supervisor interface.
* Click `Settings icon -> Quick responses` page in the left navigation pane of the Supervisor interface to view all the quick responses in your organization.
* Search for the quick response you wish to edit. See [Search quick response](#search-quick-response), for more information.
* Click three ellipse dots in the `Actions` column of the quick response to view the extended menu and click `Edit` against the quick response you wish to edit.
* You can edit details such as the `Quick response name` and `Template` of the quick response.

### Delete quick response

A supervisor can delete a quick response for various reasons. A few examples can be&#x20;

* When the quick response is no longer required or serves no purpose. Deleting such responses helps to maintain a more manageable and organized structure within the live agent system.
* When there is a need to restructure the quick response within the organization by merging, reassigning, or consolidating responses.

**To delete a quick response**:

* Click `Settings -> Avaamo Live Agent` in the Avaamo dashboard home page to view the Supervisor interface.
* Click `Settings icon -> Quick Responses` page in the left navigation pane of the Supervisor interface to view all the quick responses in your organization.
* Search for the quick response you wish to edit. See [Search quick response](#search-quick-response), for more information.
* Click three ellipse dots in the `Actions` column of the quick response to view the extended menu and click `Delete`**.** Click `OK` in the confirmation message to delete the quick response.&#x20;

### Search quick response

You can search for quick responses using the search icon in the `Quick Responses` page. To search for a quick response, enter the desired text in the Search text box and press enter.
