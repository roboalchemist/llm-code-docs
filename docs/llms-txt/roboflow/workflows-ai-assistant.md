# Source: https://docs.roboflow.com/changelog/februrary-2025/workflows-ai-assistant.md

# Source: https://docs.roboflow.com/roboflow/roboflow-ko/workflows/workflows-ai-assistant.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/workflows/workflows-ai-assistant.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/workflows/workflows-ai-assistant.md

# Source: https://docs.roboflow.com/workflows/workflows-ai-assistant.md

# Workflows AI Assistant

The Workflows AI Assistant lets you build, update, and debug Workflows from a chat interface.

The Workflows AI Assistant can answer questions about an existing Workflow, make changes based on the goal you have for your project, and fix errors in your Workflow if you encounter one.

To use the Workflows AI Assistant, click the sparkle icon on the left side of the Workflows editing window:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-0673d03caa3fc5f2067dbe05d49437bb2f7e6d63%2FScreenshot%202025-05-19%20at%2011.09.10.png?alt=media" alt=""><figcaption></figcaption></figure>

The AI Assistant will open as a sidebar in your Workflows editor:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-6d98cecb914adfea39988cf3690f2f45d8edff3b%2FScreenshot%202025-05-19%20at%2011.11.36.png?alt=media" alt=""><figcaption></figcaption></figure>

You can then start to ask questions in the chat interface.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-b74148bcd40f139113f719fce2c1241a9ebfefb4%2FScreenshot%202025-05-19%20at%2011.23.59.png?alt=media" alt=""><figcaption><p>Example showing the results for the question "How do I save predictions to a CSV?", with the Assistant creating a plan to save detections to a CSV file.</p></figcaption></figure>

### Editing Workflows

You can ask the Workflows AI Assistant to make changes to your Workflow.

For example, you could ask to:

* Add object tracking to a Workflow.
* Make your current Workflow run only if a classification model returns a certain result.
* Change the confidence threshold of a model used in a Workflow.

When you do, the AI Assistant will make changes, then ask whether you want to save them to your Workflow or revert the changes.

Changes are not saved to your production Workflow until you save changes.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-c7ce339432dd83bf1af402b32d2f85c812215d81%2FScreenshot%202025-05-19%20at%2011.20.20.png?alt=media" alt=""><figcaption></figcaption></figure>

Here is an example of a Workflow where a CSV block was added after asking the Assistant to save records to a CSV file:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-b786cde6a8144f4b607e9268cb16cec23a230671%2FScreenshot%202025-05-19%20at%2011.25.04.png?alt=media" alt=""><figcaption></figcaption></figure>

Of note, the block may not be configured when added. In this example, the CSV Formatter is created and connected to the relevant block — the one that returns tracked predictions — but does not save any results. You can click into any blocks created by the Workflows AI Assistant to make the necessary configurations according to your project needs.
