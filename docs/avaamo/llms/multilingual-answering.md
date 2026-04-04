# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/multilingual-answering.md

# Multilingual answering

Typically, in any global business, it is a necessity to design and build assistants or agents that can interact with the users in their local language. The Avaamo platform provides multilingual support for agent development in different languages, with English (en-US) as the default language. Users can converse with your agent in any local language and expect responses to be in the same local language.&#x20;

This helps in:

* Providing a wider reach of your agents. Makes agents more accessible to a broader scope of users.
* Providing more personal experience with your agents since interacting in the local language is more natural and relatable.

Regardless of the language in which any information is stored in the knowledge base, the Answers skill can use the information to reply in the language that the user is conversing in. For example, consider that a user is conversing in Spanish with an Avaamo agent. The user asks for information that is stored in English in the knowledge base. The agent is capable of translating the information to Spanish and responding.

Hence, documents and content uploaded in any language can be used for answering queries.

### What is Multilingual answering?

You can use Avaamo Answers to ingest content in any of the [Avaamo-supported languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-supported-languages) and provide responses to user queries from the content available in the user's preferred language. See [Add Document or URL](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/add-document-or-url-1), for more information.

The following illustration depicts how Avaamo answers can provide responses to a user query in the local language from the ingested document in the corresponding language:

### ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FLCZ3NrkT9mJJQSYc8X9J%2Fimage.png?alt=media\&token=a8c6d970-b701-4252-a860-c4e5f02c368f)

### How to use it?

* You must first add the language of the document you wish to upload to your agent. See [Add languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-languages), for more information on adding languages to your agent.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FTxJq1vBkr3NMGvWlTMjm%2Flanguage-step1-ans.png?alt=media\&token=ed1ecc3c-0006-4c26-8c25-f619c6d4fab6)

* After the content is ingested, a knowledge base is created. See [View and edit knowledge](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/view-and-edit-knowledge), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F2XG6teUOolBjY9Vu9pLc%2Flanguage-step2-ans.png?alt=media\&token=e817c26d-4fc9-47cc-aac6-81cd171284ec)

* You can now ask queries in the local language, say Spanish in this use case, and get the agent's response in Spanish. Note that if you ask a query in say English, the agent response in English is displayed.&#x20;

{% hint style="info" %}
**Note**: To switch from one language to another when conversing with the agent, the user has to type the command `#switch_lang language-code.`See [Language.switch](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/language.switch) and [Skill commands](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/skill-commands)
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FLCZ3NrkT9mJJQSYc8X9J%2Fimage.png?alt=media\&token=a8c6d970-b701-4252-a860-c4e5f02c368f)

### Key points

Avaamo Platform allows you to customize the translated responses of the agent in the **Configuration -> Language** tab. Currently, this cannot be used for customizing the translated response of the agent for the Answers skill.&#x20;
