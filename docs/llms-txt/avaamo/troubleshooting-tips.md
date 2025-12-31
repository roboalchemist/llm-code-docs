# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/troubleshooting-tips.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-q-and-a-designer/troubleshooting-tips.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/troubleshooting-tips.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/troubleshooting-tips.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/troubleshooting-tips.md

# Source: https://docs.avaamo.com/user-guide/datasync-ai/troubleshooting-tips.md

# Source: https://docs.avaamo.com/user-guide/llamb/troubleshooting-tips.md

# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/troubleshooting-tips.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-q-and-a-designer/troubleshooting-tips.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/troubleshooting-tips.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/troubleshooting-tips.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/troubleshooting-tips.md

# Source: https://docs.avaamo.com/user-guide/datasync-ai/troubleshooting-tips.md

# Source: https://docs.avaamo.com/user-guide/llamb/troubleshooting-tips.md

# Troubleshooting tips

In case you are unable to receive the expected response from LLaMB, the following few troubleshooting tips can help:

* Check if the URL you are trying to upload is publicly accessible without any firewall restrictions. Make a GET request in any API tool such as Postman and check if you are receiving the proper response.
* Check if the PDFs must have permission to read from and write to and must not be access-controlled or password-protected.
* Check if the document or URL is uploaded successfully, without any errors. For errors, click **Error** in the **Status** column to view more details.&#x20;
* Try to [retrain](https://docs.avaamo.com/user-guide/get-started/step-2-ingest-enterprise-content/common-actions#retrain) the errored-out documents or URLs, if required. If the error persists, contact Avaamo Support, for more details.
* If the upload is successful and yet you are not receiving the expected responses, then&#x20;
  * Click the eye icon below the user query to know the intent mapped to the query.
  * In the insights pop-up, you can know if the query is mapped to the required intent type, name, response node, and the language of the query.&#x20;
  * Try to edit the knowledge base in any of the following ways:

    1. Add additional training data to the extracted sections.
    2. Add additional acronyms, if required.
    3. Add additional synonyms for the extracted vocabulary.

    See [View and edit knowledge](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/view-and-edit-knowledge), for more information.
