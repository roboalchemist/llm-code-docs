# Source: https://docs.port.io/docs-ai-assistant.md

# Docs AI assistant

Port's AI assistant is here to help you get the most out of your portal by answering your questions, creating resources, and assisting with troubleshooting.

To use the AI assistant, click on the `Ask AI` button in the top-right corner âï¸ and ask a question.<br /><!-- -->It is also available in your portal, via the `?` button in the top-right corner.

## Ways to use the assistant[â](#ways-to-use-the-assistant "Direct link to Ways to use the assistant")

â **Ask documentation questions**<br /><!-- -->You can ask the assistant about any aspect of Portâs documentation, features, or concepts.<br /><!-- -->For example:

* "How do I create a new blueprint?"
* "What is a relation in Port?"
* "What configuration options are available when creating a self-service action?"

â **Request resource definitions**<br /><!-- -->The assistant can generate JSON definitions for Port resources.<br /><!-- -->Try prompts like:

* "Write a blueprint definition for a YouTube video with properties for title, description, likes, and views"
* "Write an automation definition that sends a Slack message to a channel when a new user is created"

â **Debugging help**<br /><!-- -->If you have an error in a JSON/YAML definition, paste it in and ask for help:

* "Why is this entity definition invalid?"
  <!-- -->
  ```
  {
    "identifier": "provision",
    "title": "Provision",
    "icon": "Microservice",
    "team": "myTeam",
    "properties": {},
    "relations": {
      "repository": "provision"
    }
  }
  ```
* "I'm trying to ingest a YAML file using the GitHub integration into a property called `spec`, but I'm getting an error saying that `spec` must be string.
  <br />
  <!-- -->
  Here is the data source mapping:"
  <!-- -->
  ```
  - kind: file
    selector:
      query: 'true'
      files:
        - path: '**/openapi.yaml'
    port:
      entity:
        mappings:
          identifier: .repo.full_name
          blueprint: '"api_specs"'
          properties:
            spec: .file.content
        relations:
          repository: .repo.full_name
  ```

â **Step-by-step guidance**<br /><!-- -->The assistant can walk you through processes:

* "Guide me through setting up a webhook integration"
* "How do I map properties from my data source to Port entities?"

â **Troubleshooting**<br /><!-- -->If you encounter issues, describe the problem and the assistant can suggest solutions or point you to the relevant documentation.

## Tips for getting the best results[â](#tips-for-getting-the-best-results "Direct link to Tips for getting the best results")

â **Be specific**<br /><!-- -->The more details you provide, the better the assistant can help. Include relevant context, error messages, or code snippets when possible.

â **Iterate and clarify**<br /><!-- -->If the first answer isnât quite right, ask follow-up questions or clarify your request.

â **Use examples**<br /><!-- -->When asking for definitions or debugging, include your current JSON/YAML or the error message youâre seeing.

â **Look ahead**<br /><!-- -->The assistant can provide insights into new features, in-progress work, or upcoming changes.

â **Provide feedback**<br /><!-- -->After receiving an answer, you can upvote or downvote it to help improve the assistant's responses.

## Privacy & security[â](#privacy--security "Direct link to Privacy & security")

â The assistant is trained only on public sources, including:

* Port's documentation & API reference
* Port's roadmap
* Port's Terraform provider
* Port's Pulumi provider

â The assistant does not have access to any private data or data from any Port instance.

AI-generated content

As with any AI assistant, answers may not always be accurate, so remember to use your own judgement.
