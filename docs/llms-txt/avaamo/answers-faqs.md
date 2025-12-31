# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/answers-faqs.md

# Answers skill - FAQs

This article lists a few frequently asked questions related to Answers skill:

### 1. What are the types of files I can load in the Answers skill?

The following are the different ways of uploading content:

* Directly upload PDF, Excel, or CSV files.
* Upload content from any externally accessible URL.
* To upload .doc or .docx files, you can convert these files to PDF and then upload them.
* Use CMS Webhooks to upload content from a Content Management System.
* Use the document parsing utility to ingest content from websites
* Upload video transcripts.
* Upload information that is in the FAQ format.

See [Upload Content](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/add-document-or-url-1) for more information.

### 2. Is there any limit on the number of URLs or PDF sizes?

There is no limit on the number of URLs that can be uploaded using the Answers skill. Further, you can upload multiple PDF documents and each PDF document can be more than 1000 pages. See [Key Points](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/manage-avaamo-answers-1/add-document-or-url-1#key-points), for more information.

### 3. How do I handle disambiguation in Answers skill?

Given following are the main ways to handle disambiguation in Answers skill:

* You can define attributes for the uploaded documents or URLs in your Answers skill to facilitate disambiguation. See [Defining attributes for documents or URLs](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/manage-avaamo-answers-1/perform-common-actions#defining-attributes-for-documents-or-urls), for more information.
* You can disambiguate acronyms that can be expanded in more than one way.
* You can disambiguate using training data in different sections.&#x20;

### 4. Can we link this to any content management system?

Yes, you can use CMS Webhooks to pull content from a Content Management System and push it to Avaamo Platform. See [Content ingestion using Webhooks](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/content-ingestion) for more information.

### 5. What if my content is in Tabular format?

You can directly upload Excel or CSV files. Using the parsing utility, you can also upload PDF and HTML files that have tables in them. Responses to user queries can be fetched from the information in tables. See Tabular Answering for more information.

### 6. What languages are supported currently in Answers?

The Avaamo platform provides multilingual support for agent development in any of the Avaamo-supported languages, with English (en-US) as the default language. Avaamo Answers can also ingest content in other languages.

Answers can also translate information stored in other languages to the language in which the user is conversing and respond accordingly. For example, if the agent is conversing in Spanish, the skill can translate information stored in English and respond in Spanish.&#x20;

### 7. Will Answers search text present on images?

No.&#x20;

### 8. How to provide document metadata in Answers skill?

You can define attributes for the uploaded documents or URLs in your Answers skill. See [Defining attributes for documents or URLs](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/manage-avaamo-answers-1/perform-common-actions#defining-attributes-for-documents-or-urls), for more information.

### 9. Does the user feedback on the Answer skill response be automatically trained back in the skill?

Currently, the feedback can be used only for analytical purposes only. If a user gives negative feedback on a card response for an Answers skill, you can check the feedback, update, tune, and retrain the Answers skill.&#x20;

### 10. How to improve the accuracy of the Answers skill?

Please see the Improving Accuracy in Answers Skill page.

### 11. How does the agent disambiguate between responses that are found in more than one Answers skill?

When a response to a user query is found in multiple answers skills, the agent presents the names of the answers skills that have the response. Based on the answer skill that the user selects, the corresponding response is displayed.
