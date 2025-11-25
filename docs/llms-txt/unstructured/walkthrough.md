# Source: https://docs.unstructured.io/ui/walkthrough.md

# Unstructured UI walkthrough

This walkthrough provides you with deep, hands-on experience with the [Unstructured user interface (UI)](/ui/overview). As you follow along, you will learn how to use many of Unstructured's
features for [partitioning](/ui/partitioning), [enriching](/ui/enriching/overview), [chunking](/ui/chunking), and [embedding](/ui/embedding). These features are optimized for turning
your source documents and data into information that is well-tuned for
[retrieval-augmented generation (RAG)](https://unstructured.io/blog/rag-whitepaper),
[agentic AI](https://unstructured.io/problems-we-solve#powering-agentic-ai),
and [model fine-tuning](https://www.geeksforgeeks.org/deep-learning/what-is-fine-tuning/).

This walkthrough uses two sample files to demonstrate how Unstructured identifies and processes content such as image, graphs, complex tables, non-English characters, and handwriting.
These files, which are available for you to download to your local machine, include:

* Wang, Z., Liu, X., & Zhang, M. (2022, November 23).
  *Breaking the Representation Bottleneck of Chinese Characters: Neural Machine Translation with Stroke Sequence Modeling*.
  arXiv.org. [https://arxiv.org/pdf/2211.12781](https://arxiv.org/pdf/2211.12781). This 12-page PDF file features English and non-English characters, images, graphs, and complex tables.
  Throughout this walkthrough, this file's title is shortened to "Chinese Characters" for brevity.
* United States Central Security Service. (2012, January 27). *National Cryptologic Museum Opens New Exhibit on Dr. John Nash*.
  United States National Security Agency. [https://courses.csail.mit.edu/6.857/2012/files/H03-Cryptosystem-proposed-by-Nash.pdf](https://courses.csail.mit.edu/6.857/2012/files/H03-Cryptosystem-proposed-by-Nash.pdf).
  This PDF file features English handwriting and scanned images of documents.
  Throughout this walkthrough, this file's title is shortened to "Nash letters" for brevity.

<Note>
  This walkthrough focuses on local files for ease-of-use demonstration purposes.

  This walkthrough does not cover how to use
  Unstructured to set up [connectors](/ui/connectors) to do large-scale batch processing of multiple files and semi-structured data that are stored in remote locations.
  To learn how to set up connectors and do large-scale batch processing later, see the [next steps](#next-steps) after you finish this walkthrough.
</Note>

If you are not able to complete any of the following steps, contact Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

<Tip>
  *What are these green boxes?*

  As you move through this walkthrough, you will notice tips like this one. These tips are designed to help expand
  your knowledge about Unstructured as you go. Feel free to skip these tips for now if you are in a hurry. You can always return to them later to learn more.
</Tip>

## Step 1: Sign up and sign in to Unstructured

Let's get started!

1. If you do not already have an Unstructured account, [sign up for free](https://unstructured.io/?modal=try-for-free).
   After you sign up, you are automatically signed in to your new Unstructured **Let's Go** account, at [https://platform.unstructured.io](https://platform.unstructured.io).

   <Note>
     To sign up for a **Business** account instead, [contact Unstructured Sales](https://unstructured.io/?modal=contact-sales), or [learn more](/ui/overview#how-am-i-billed%3F).
   </Note>

2. If you have an Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business SaaS** account and are not already signed in, sign in to your account at [https://platform.unstructured.io](https://platform.unstructured.io).

   <Note>
     For other types of **Business** accounts, see your Unstructured account administrator for sign-in instructions,
     or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).
   </Note>

## Step 2: Create a custom workflow

In this step, you create a custom [workflow](/ui/workflows) in your Unstructured account.

Workflows are defined sequences of processes that automate the flow of data from your source documents and data into Unstructured for processing.
Unstructured then sends its processed data over into your destination file storage locations, databases, and vector stores. Your
RAG apps, agents, and models can then use this processed data in those destinations to do things more quickly and accurately such as
[answering users' questions](https://learn.microsoft.com/en-us/azure/developer/ai/advanced-retrieval-augmented-generation),
[automating business processes](https://unstructured.io/problems-we-solve#business-process-automation),
and [expanding your organization's available body of knowledge](http://knowledgemanagement.ie/the-critical-role-of-knowledge-management-as-a-foundation-for-llms-and-ai/).

<Tip>
  *Which kinds of sources and destinations does Unstructured support?*

  Unstructured can connect to many types of sources and destinations including file storage services such as Amazon S3 and Google Cloud Storage;
  databases such as PostgreSQL; and vector storage and database services such as MongoDB Atlas and Pinecone.

  See the full list of [supported source and destination connectors](/ui/connectors).
</Tip>

<Tip>
  *Which kinds of files does Unstructured support?*

  Unstructured can process a wide variety of file types including PDFs, word processing documents, spreadsheets, slide decks, HTML, image files, emails, and more.

  See the full list of [supported file types](/ui/supported-file-types).
</Tip>

Let's get going!

1. After you are signed in to your Unstructured account, on the sidebar, click **Workflows**.

   <img src="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/WorkflowsSidebar.png?fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=a186dac681921c7549bd4c4a177ea2c0" alt="Workflows button on the sidebar" data-og-width="154" width="154" data-og-height="576" height="576" data-path="img/ui/walkthrough/WorkflowsSidebar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/WorkflowsSidebar.png?w=280&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=69d6baeed15d2daa2cf959435e5b5fdc 280w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/WorkflowsSidebar.png?w=560&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=1d05d3180399e17848ca0bc12694c486 560w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/WorkflowsSidebar.png?w=840&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=9174985fbda5b8fea2465d1165402d8b 840w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/WorkflowsSidebar.png?w=1100&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=a0ad18378a92b5b1d84993f8c057c410 1100w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/WorkflowsSidebar.png?w=1650&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=24a7e78f3735c1790ed528ef30207b85 1650w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/WorkflowsSidebar.png?w=2500&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=6c4638587fe11d7d21aa4e23fcc0c0b8 2500w" />

   <Tip>
     *What do the other buttons on the sidebar do?*

     * **Start** takes you to the UI home page. The home page features a simple way to process one local file at a time with limited default settings. [Learn how](/welcome#unstructured-ui-quickstart).
     * **Connectors** allows you to create and manage your [source](/ui/sources/overview) and
       [destination](/ui/destinations/overview) connectors.
     * **Jobs** allows you to see the results of your workflows that are run manually (on-demand) and automatically (on a regular time schedule). [Learn more](/ui/jobs).
     * **API Keys** allows you to use code to create and manage connectors, workflows, and jobs programmatically instead of by using the UI. [Learn more](/ui/account/api-key-url).
     * Your user icon at the bottom of the sidebar allows you to manage your Unstructured account. You can also sign out of your account from here. [Learn more](/ui/account/overview).
   </Tip>

2. Click **New Workflow**.

   <img src="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/NewWorkflow.png?fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=51f8e5ea86c39fa060e6f00b6ff25d86" alt="New Workflow button" data-og-width="302" width="302" data-og-height="92" height="92" data-path="img/ui/walkthrough/NewWorkflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/NewWorkflow.png?w=280&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=f066dc6c870e5aadd72614ad0c2c15e4 280w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/NewWorkflow.png?w=560&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=7faf4f5406e3842a8a720bb4809c2284 560w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/NewWorkflow.png?w=840&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=e3ff5a08b831d62a2c931eda06ea012b 840w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/NewWorkflow.png?w=1100&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=4b775c07b8c3be215ea58513a1da7583 1100w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/NewWorkflow.png?w=1650&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=aabdde8b96d8dbbe45643dcb3ee8fac6 1650w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/NewWorkflow.png?w=2500&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=56668eb2c797ea5e8bf65ec774cd28c4 2500w" />

3. With **Build it Myself** already selected, click **Continue**.

   <img src="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/BuildItMyself.png?fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=9c8163fcfd133b78ce3fea528716bbb7" alt="Build it Myself workflow option" data-og-width="1156" width="1156" data-og-height="840" height="840" data-path="img/ui/walkthrough/BuildItMyself.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/BuildItMyself.png?w=280&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=e22555d99cb3544a2eb6bf3324b311ef 280w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/BuildItMyself.png?w=560&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=8dd92dd65a4698374d6d9d3678177c2b 560w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/BuildItMyself.png?w=840&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=93c855ec54c5c4577f1c0ef7288d099e 840w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/BuildItMyself.png?w=1100&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=3308af186a7cf6096fd76caaa8385ffc 1100w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/BuildItMyself.png?w=1650&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=3244be6c003226335a9fd78fd30eb79a 1650w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/BuildItMyself.png?w=2500&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=f086430c81d6cd32468aa7e8f7bc31bc 2500w" />

   <Tip>
     *What does **Build it For Me** do?*

     The **Build it For Me** option creates an [automatic workflow](/ui/workflows#create-an-automatic-workflow) with limited, sensible default settings to enable you to get good-quality results faster. However,
     this option requires that you first have an existing remote source and destination connector to add to the workflow. To speed things up here and keep things simple,
     this walkthrough only processes files from your local machine and skips the use of connectors. To learn how to use connectors later,
     see the [next steps](#next-steps) at the end of this walkthrough.
   </Tip>

4. The workflow designer appears.

   <img src="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/WorkflowDesigner.png?fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=60a471f3f104f39ecaabbd872cd0ae6a" alt="The workflow designer" data-og-width="2140" width="2140" data-og-height="1500" height="1500" data-path="img/ui/walkthrough/WorkflowDesigner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/WorkflowDesigner.png?w=280&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=a52d30b30531fd752cebb1eed27afbff 280w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/WorkflowDesigner.png?w=560&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=f6961d1340f333891279dcc27f277575 560w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/WorkflowDesigner.png?w=840&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=9677273e8c44e2e3449a1eb7f949ddb6 840w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/WorkflowDesigner.png?w=1100&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=9db3ab0c08037b003b70f3f1ef201107 1100w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/WorkflowDesigner.png?w=1650&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=a884e119d27627938283fa4832210f27 1650w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/WorkflowDesigner.png?w=2500&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=83ab39ffda8b7a28e912d465a8d570a5 2500w" />

   <Tip>
     *What are all the parts of the workflow designer?*

     The middle portion of the workflow designer is the workflow *directed acyclic graph* (DAG), which contains a
     a collection of *nodes* connected by *edges* that go in only one direction. You can think of the DAG similar to a flowchart
     for a process. *Directed* means the arrows show the flow from one step to the next, and *acyclic* means you cannot
     follow the arrows backward to get back to the starting point.

     The workflow settings pane on the right includes the following tabs:

     * The settings on the **Details** tab allow you to change this workflow's name. You can also see when this workflow was created and which jobs were run for this workflow.
     * **Schedule** allows you to set up a schedule for this workflow to run automatically (on a regular time schedule).
     * **Settings** allows you to specify whether every time this workflow runs, that Unstructured's results will overwrite any previous results in the destination location.
       To turn on this behavior, check the **Overwrite existing results** box. To turn it off, uncheck the box. Note that this setting works only
       for blog storage destination connectors such as the ones for Amazon S3, Azure Blob Storage, and Google Cloud Storage.
     * **FAQ** contains additional information about how to use the workflow designer.

     If the workflow settings pane is not visible, click the **Settings** button near the bottom to show it.

     There are also buttons near the bottom to undo or redo recent edits to the workflow DAG, zoom in and out of the workflow
     designer, re-center the DAG within the designer, and add a new node to the DAG.
   </Tip>

## Step 3: Experiment with partitioning

In this step, you use your new workflow to [partition](/ui/partitioning) the sample PDF files that you downloaded earlier onto your local machine.
Partitioning is the process where Unstructured identifies and extracts content from your source documents and then
outputs this content as a series of contextually-rich [document elements and metadata](/ui/document-elements), which are
well-tuned for RAG, agentic AI, and model fine-tuning. This step
shows how well Unstructured's **VLM** partitioning strategy handles challenging content such as complex tables, multilanguage characters, and handwriting.

1. With the workflow designer active from the previous step, at the bottom of the **Source** node, click **Drop file to test**.

   <img src="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/DropFileToTest.png?fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=52077c448ce7a41cbee4dda614be7316" alt="Drop file to test button" data-og-width="262" width="262" data-og-height="208" height="208" data-path="img/ui/walkthrough/DropFileToTest.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/DropFileToTest.png?w=280&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=5087d5653dcca2e8f6cb6cd001b24ac5 280w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/DropFileToTest.png?w=560&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=414f994854bc441b694e800f8e167695 560w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/DropFileToTest.png?w=840&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=9d49fce9a043f6ce9a9b03069e0c33a3 840w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/DropFileToTest.png?w=1100&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=d4151c7ea621d15dff3328bef16ea5ba 1100w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/DropFileToTest.png?w=1650&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=679dae353372fc2d6be1219b571cf479 1650w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/DropFileToTest.png?w=2500&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=dfcf79a62465cb9a59961b2e2c7a64f6 2500w" />

2. Browse to and select the "Chinese Characters" PDF file that you downloaded earlier.

3. In the workflow designer, click the **Partitioner** node and then, in the node's settings pane's **Details** tab, select **VLM**.<br />

   <Tip>
     *When would I choose **Auto**, **Fast**, **High Res**, or **VLM**?*

     * **Auto** is recommended in most cases. It lets Unstructured figure out the best strategy to switch over to for each incoming file (and even for each page if the incoming file is a PDF), so you don't have to!
     * **Fast** is only for when you know for certain that none of your files have tables, images, or multilanguage, scanned, or handwritten content in them. It's optimized for partitioning text-only content and is the fastest of all the strategies. It can recognize the text for only a few languages other than English.
     * **High Res** is only for when you know for certain that at least one of your files has images or simple tables in them, and that none of your files also have scanned or handwritten content in them. It can recognize the text for more languages than **Fast** but not as many as **VLM**.
     * **VLM** is great for any file, but it is best when you know for certain that some of your files have a combination of tables (especially complex ones), images, and multilanguage, scanned, or handwritten content. It's the highest quality but slowest of all the strategies.
   </Tip>

4. Under **Select VLM Model**, under **Vertex AI**, select **Gemini 2.0 Flash**.<br />

   <img src="https://mintcdn.com/unstructured-53/pyo7Q_5IJVFy-j1Z/img/ui/walkthrough/VLMPartitioner.png?fit=max&auto=format&n=pyo7Q_5IJVFy-j1Z&q=85&s=066c0a3b8958a8b7461862749aa2a9ce" alt="Selecting the VLM for partitioning" data-og-width="3456" width="3456" data-og-height="1868" height="1868" data-path="img/ui/walkthrough/VLMPartitioner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/pyo7Q_5IJVFy-j1Z/img/ui/walkthrough/VLMPartitioner.png?w=280&fit=max&auto=format&n=pyo7Q_5IJVFy-j1Z&q=85&s=74e86039dd90f753e5eb952a46458e17 280w, https://mintcdn.com/unstructured-53/pyo7Q_5IJVFy-j1Z/img/ui/walkthrough/VLMPartitioner.png?w=560&fit=max&auto=format&n=pyo7Q_5IJVFy-j1Z&q=85&s=6c0f49b0aad04b853c131c32e79698a9 560w, https://mintcdn.com/unstructured-53/pyo7Q_5IJVFy-j1Z/img/ui/walkthrough/VLMPartitioner.png?w=840&fit=max&auto=format&n=pyo7Q_5IJVFy-j1Z&q=85&s=a1a0b3de833895d0472e368e672c6936 840w, https://mintcdn.com/unstructured-53/pyo7Q_5IJVFy-j1Z/img/ui/walkthrough/VLMPartitioner.png?w=1100&fit=max&auto=format&n=pyo7Q_5IJVFy-j1Z&q=85&s=516e87c89e048e89088914fceba58679 1100w, https://mintcdn.com/unstructured-53/pyo7Q_5IJVFy-j1Z/img/ui/walkthrough/VLMPartitioner.png?w=1650&fit=max&auto=format&n=pyo7Q_5IJVFy-j1Z&q=85&s=6b7dcc4c6059564c59227b5e53f59702 1650w, https://mintcdn.com/unstructured-53/pyo7Q_5IJVFy-j1Z/img/ui/walkthrough/VLMPartitioner.png?w=2500&fit=max&auto=format&n=pyo7Q_5IJVFy-j1Z&q=85&s=c1f5faa79edb9edff6b68d9451b88642 2500w" />

   <Tip>
     *When I choose **VLM**, when would I choose one of these models over another?*

     A *vision language model* (VLM) is designed to use sophisticated AI techniques and logic to combine advanced image and text understanding, resulting in more accurate and
     contextually-rich output.

     As VLMs are constantly being released and improved, Unstructured is always adding to and updating its list of supported VLMs.
     If you aren't getting consistent results with one VLM for a particular set of files, switching over to another one might improve your results, depending on that VLM's capabilities and the sample data that is was trained on.
   </Tip>

5. Click **Test**.<br />

   <img src="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/TestLocalFile.png?fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=1879649f0470091648cf9d2dd0b80174" alt="Begin testing the local file" data-og-width="258" width="258" data-og-height="268" height="268" data-path="img/ui/walkthrough/TestLocalFile.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/TestLocalFile.png?w=280&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=e27b6de5df2a6728ab9bd543fcae81b5 280w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/TestLocalFile.png?w=560&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=43a44e067df1f5e7b4835ef076de5c3a 560w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/TestLocalFile.png?w=840&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=5987140ec1836711f8fbc6bde50052dc 840w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/TestLocalFile.png?w=1100&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=700342b5cd086c3f2d02bdcd8cd0e570 1100w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/TestLocalFile.png?w=1650&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=24501ef8d4e504d6b640810fde797c2d 1650w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/TestLocalFile.png?w=2500&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=a5c34808fd95f208b50367f8eb8e4e3e 2500w" />

6. The PDF file appears in a pane on the left side of the screen, and Unstructured's output appears in a **Test output** pane on the right side of the screen.

   <img src="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/TestOutputResults.png?fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=8321e62ca7454823a235c02d0a4be25d" alt="Showing the test output results" data-og-width="2140" width="2140" data-og-height="1496" height="1496" data-path="img/ui/walkthrough/TestOutputResults.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/TestOutputResults.png?w=280&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=7cdad9879545b79c2511150a93c9b858 280w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/TestOutputResults.png?w=560&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=de44e7a06a286bbbeb4efb8366b2fdd5 560w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/TestOutputResults.png?w=840&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=15ced22b19ab13415c5b31aadb855866 840w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/TestOutputResults.png?w=1100&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=62d765731852f1c2528e1b3857029f68 1100w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/TestOutputResults.png?w=1650&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=c1dc86896e4790c782b490b9b1eeb49b 1650w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/TestOutputResults.png?w=2500&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=de533417b248e3b5ea80998e44ce206a 2500w" />

   <Tip>
     *What am I looking at in the output here?*

     * Unstructured outputs its results in industry-standard [JSON](https://www.json.org) format, which is ideal for RAG, agentic AI, and model fine-tuning.
     * Each object in the JSON is called a [document element](/ui/document-elements) and contains a `text` representation of the content that Unstructured detected for the particular portion of the document that was analyzed.
     * The `type` is the kind of document element that Unstructured categorizes it as, such as whether it is a title (`Title`), a table (`Table`), an image (`Image`), a series of well-formulated sentences
       (`NarrativeText`), some kind of free text (`UncategorizedText`), a part of a list (`ListItem`), and so on. [Learn more](/ui/document-elements#element-type).
     * The `element_id` is a unique identifier that Unstructured generates to refer to each document element. [Learn more](/ui/document-elements#element-id).
     * `metadata` contains supporting details about each document element, such as the page number it occurred on, the file it occurred in, and so on. [Learn more](/ui/document-elements#metadata).
   </Tip>

   <Tip>
     *What else can I do here?*

     * You can scroll through the original file on the left or, where supported for a given file type, click the up and down arrows to page through the file one page at a time.
     * You can scroll through Unstructured's JSON output on the right, and you can click **Search JSON** to search for specific text in the JSON output. You will do this next.
     * **Download Full JSON** allows you to download the full output to your local machine as a JSON file.
     * **View JSON at this step** allows you to view the JSON output at each step in the workflow as it was further processed. There's only one step right now (the **Partitioner** step),
       but as you add more nodes to the workflow DAG, this can be a useful tool to see how the JSON output changes along the way.
     * The close (**X**) button returns you to the workflow designer.
   </Tip>

7. Notice the following in the JSON output, which you can get to by clicking **Search JSON** above the output:

   <img src="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/SearchJSON.png?fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=3028d7115aed7d90b490347befe89e83" alt="Searching the JSON output" data-og-width="2136" width="2136" data-og-height="1500" height="1500" data-path="img/ui/walkthrough/SearchJSON.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/SearchJSON.png?w=280&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=026ef7b3f3f07681b853729e821ea4f7 280w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/SearchJSON.png?w=560&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=9a6302b83929246d20320120df5e01b4 560w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/SearchJSON.png?w=840&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=cf7982f6cdc4444e33aa5e8377a66785 840w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/SearchJSON.png?w=1100&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=c5cf497d058a9f06ca0239eb6c47814a 1100w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/SearchJSON.png?w=1650&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=10fee17bf5c5f753ecb22436619b5225 1650w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/SearchJSON.png?w=2500&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=760a35166e8946a8109b14543f3fbece 2500w" />

   * The Chinese characters on page 1. Search for the text `verbs. The characters`. Notice how the Chinese characters are output. We'll see accuracy improvements to this output later in Step 4 in the enrichments portion of this walkthrough.
   * The tables on pages 1, 6, 7, 8, 9, and 12. Search for the text `"Table"` (including the quotation marks) to see how the VLM interprets the various tables. We'll see changes to these elements' `text` and `metadata.text_as_html` contents later in Step 4 in the enrichments portion of this walkthrough.
   * The images on pages 3, 7, and 8. Search for the text `"Image"` (including the quotation marks) to see how the VLM interprets the various images. We'll see changes to these elements' `text` contents later in Step 4 in the enrichments portion of this walkthrough.

   <Note>
     If **Search JSON** is not clickable, this is probably because the JSON output is too large for the online viewer.
     Click **Download full JSON** and open the downloaded JSON file in an offline text editor (such as Visual Studio Code).
     [Learn more](/examplecode/tools/conversion-tools#visual-studio-code).
   </Note>

8. Now try looking at the "Nash letters" PDF file's output. To do this:

   a. Click the close (**X**) button above the output on the right side of the screen.<br />
   b. At the bottom of the **Source** node, click the existing PDF's file name.<br />
   c. Browse to and select the "Nash letters" file that you downloaded earlier to your local machine.<br />
   d. Click **Test**.<br />

9. Notice the following in the JSON output:

   * The handwriting on page 3. Search for the text `I have written RAND`. Notice how well the handwriting is recognized.
   * The mimeograph on page 18. Search for the text `The system which`. Notice how well the mimeographed content is recognized.

10. When you are done, be sure to click the close (**X**) button above the output on the right side of the screen, to return to
    the workflow designer for the next step.

## Step 4: Experiment with enriching

In this step, you add several [enrichments](/ui/enriching/overview) to your workflow, such as generating summary descriptions of detected images and tables,
HTML representations of detected tables, and detected entities (such as people and organizations) and the inferred relationships among these entities.

1. With the workflow designer active from the previous step, change the **Partitioner** node to use **High Res**.

2. Between the **Partitioner** and **Destination** nodes, click the add (**+**) icon, and then click **Enrich > Enrichment**.

   <img src="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddEnrichment.png?fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=41e46e3cf540af32a23febb00a45161b" alt="Adding an enrichment node" data-og-width="1380" width="1380" data-og-height="494" height="494" data-path="img/ui/walkthrough/AddEnrichment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddEnrichment.png?w=280&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=e714c2769f1e9c623412dafeefc3ed0e 280w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddEnrichment.png?w=560&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=328fd1a7a31c7eca067f8ceaa7d3a499 560w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddEnrichment.png?w=840&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=ce73ba90e1fd58baed66fca4d9f10a66 840w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddEnrichment.png?w=1100&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=1911ff51771cc824c4ca564d5a68916a 1100w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddEnrichment.png?w=1650&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=39f4a71051c48a54c25c6fb19d6885f9 1650w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddEnrichment.png?w=2500&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=b9ffa0cd362a84917e65009cba6bb688 2500w" />

3. In the node's settings pane's **Details** tab, click:

   * **Image** under **Input Type**.
   * Any available choice for **Provider** (for example, **Anthropic**).
   * Any available choice for **Model** (for example, **Claude Sonnet 4.5** if you chose **Anthropic** for **Provider**).
   * If not already selected, **Image Description** under **Task**.

   <Tip>
     The image description enrichment generates a summary description of each detected image. This can help you to more quickly and easily understand
     what each image is all about without having to stop to manually visualize and interpret the image's content yourself. This also provides additional helpful context about the image for your RAG apps, agents, and models. [Learn more](/ui/enriching/image-descriptions).
   </Tip>

4. Repeat this process to add four more nodes between the **Partitioner** and **Destination** nodes. To do this, click
   the add (**+**) icon, and then click **Enrich > Enrichment**, as follows:

   a. Add a table description enrichment (click the add (**+**) icon to the right of the preceding node, and then click \*\*Enrich > Enrichment).

   In the node's settings pane's **Details** tab, click:

   * **Table** under **Input Type**.
   * Any available choice for **Provider** (for example, **Anthropic**).
   * Any available choice for **Model** (for example, **Claude Sonnet 4.5** if you chose **Anthropic** for **Provider**).
   * If not already selected, **Table Description** under **Task**.

   <Tip>
     The table description enrichment generates a summary description of each detected table. This can help you to more quickly and easily understand
     what each table is all about without having to stop to manually read through the table's content yourself. This also provides additional helpful context about the table for your RAG apps, agents, and models. [Learn more](/ui/enriching/table-descriptions).
   </Tip>

   b. Add a table to HTML enrichment (click the add (**+**) icon to the right of the preceding node, and then click \*\*Enrich > Enrichment).

   In the node's settings pane's **Details** tab, click:

   * **Table** under **Input Type**.
   * Any available choice for **Provider** (for example, **Anthropic**).
   * Any available choice for **Model** (for example, **Claude Sonnet 4.5** if you chose **Anthropic** for **Provider**).
   * **Table to HTML** under **Task**.

   <Tip>
     The table to HTML enrichment generates an HTML representation of each detected table. This can help you to more quickly and accurately recreate the table's content elsewhere later as needed. This also provides additional context about the table's structure for your RAG apps, agents, and models. [Learn more](/ui/enriching/table-to-html).
   </Tip>

   c. Add a named entity recognition enrichment (click the add (**+**) icon to the right of the preceding node, and then click \*\*Enrich > Enrichment).

   In the node's settings pane's **Details** tab, click:

   * **Text** under **Input Type**.
   * Any available choice for **Provider** (for example, **Anthropic**).
   * Any available choice for **Model** (for example, **Claude Sonnet 4.5** if you chose **Anthropic** for **Provider**).

   <Tip>
     The named entity recognition (NER) enrichment generates a list of detected entities (such as people and organizations) and the inferred relationships among these entities. This provides additional context about these entities' types and their relationships for your graph databases, RAG apps, agents, and models. [Learn more](/ui/enriching/ner).
   </Tip>

   d. Add a generative OCR enrichment (click the add (**+**) icon to the right of the preceding node, and then click \*\*Enrich > Enrichment).

   In the node's settings pane's **Details** tab, click:

   * **Image** under **Input Type**.
   * Any available choice for **Provider** (for example, **Anthropic**).
   * Any available choice for **Model** (for example, **Claude Sonnet 4.5** if you chose **Anthropic** for **Provider**).
   * **Generative OCR** under **Task**.

   <Tip>
     The generative OCR enrichment improves, as needed, the accuracy of text blocks that Unstructured initially processed during its partitioning phase. [Learn more](/ui/enriching/generative-ocr).
   </Tip>

   <Warning>
     Generative OCR does not process any text blocks by default. You must also explicitly specify which document element
     types containing text that you want generative OCR to process. To do this:

     1. Click the **Partitioner** node.
     2. In the node's settings pane, scroll down to and then click a blank area inside of the **Extract Image Block Types** list.
     3. Select each [document element types](/ui/document-elements#element-type) that you want generative OCR to process. For this
        walkthrough, select only **NarrativeText**.

     Generative OCR does not process the text of any `Image` or `Table` elements if they have already been processed by
     [image description](#image-description-task) or [table description](#table-description-task) enrichments, respectively. Do
     not remove the **Image** or **Table** document elements types from this **Extract Image Block Types** list, or else
     the image description and table description enrichments in your workflow might produce unexepcted results or might not work at all.
   </Warning>

   <Note>
     The **Generative OCR** enrichment appears under the **Input Type** of **Image**, even though this is not an image-related enrichment.
     This is a known issue and will be addressed in a future release.
   </Note>

   The workflow designer should now look similar to this:

   <img src="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/walkthrough/EnrichedWorkflow.png?fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=10a8f84b1810538346101f9d02eabdfd" alt="The workflow with enrichments added" data-og-width="2194" width="2194" data-og-height="174" height="174" data-path="img/ui/walkthrough/EnrichedWorkflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/walkthrough/EnrichedWorkflow.png?w=280&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=960e4fc78ae25b1402fe6c9a7206fac2 280w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/walkthrough/EnrichedWorkflow.png?w=560&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=ecca8f8a3148bc0186e8df66582527de 560w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/walkthrough/EnrichedWorkflow.png?w=840&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=a7a2ca1abb45fc3fe2a8fd86f357d062 840w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/walkthrough/EnrichedWorkflow.png?w=1100&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=4810319cda8b482da0c1f8d9b63c7bce 1100w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/walkthrough/EnrichedWorkflow.png?w=1650&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=ab4deabfb5303161ce64bb5c046c7287 1650w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/walkthrough/EnrichedWorkflow.png?w=2500&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=87d7a4120ddd14d0ea0755a7419a70fa 2500w" />

5. Change the **Source** node to use the "Chinese Characters" PDF file, and then click **Test**.

6. In the **Test output** pane, make sure that **Enrichment (6 of 6)** is showing. If not, click the right arrow (**>**) until **Enrichment (6 of 6)** appears, which will show the output from the last node in the workflow.

   <img src="https://mintcdn.com/unstructured-53/Tq3ntZXiZPvizKeV/img/ui/walkthrough/GoToEnrichmentNode.png?fit=max&auto=format&n=Tq3ntZXiZPvizKeV&q=85&s=d16a686d8feabe07322be15c00bffa18" alt="The final Enrichment node's output" data-og-width="658" width="658" data-og-height="124" height="124" data-path="img/ui/walkthrough/GoToEnrichmentNode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/Tq3ntZXiZPvizKeV/img/ui/walkthrough/GoToEnrichmentNode.png?w=280&fit=max&auto=format&n=Tq3ntZXiZPvizKeV&q=85&s=afa8e57035924fd46e613b986b5eded4 280w, https://mintcdn.com/unstructured-53/Tq3ntZXiZPvizKeV/img/ui/walkthrough/GoToEnrichmentNode.png?w=560&fit=max&auto=format&n=Tq3ntZXiZPvizKeV&q=85&s=30a51bbd558b55e6aad2988d60bec9d9 560w, https://mintcdn.com/unstructured-53/Tq3ntZXiZPvizKeV/img/ui/walkthrough/GoToEnrichmentNode.png?w=840&fit=max&auto=format&n=Tq3ntZXiZPvizKeV&q=85&s=be5b93ccaca2455fd9625a603a3cb3c0 840w, https://mintcdn.com/unstructured-53/Tq3ntZXiZPvizKeV/img/ui/walkthrough/GoToEnrichmentNode.png?w=1100&fit=max&auto=format&n=Tq3ntZXiZPvizKeV&q=85&s=244d8637c75904b6f67dedcdc1cabc2b 1100w, https://mintcdn.com/unstructured-53/Tq3ntZXiZPvizKeV/img/ui/walkthrough/GoToEnrichmentNode.png?w=1650&fit=max&auto=format&n=Tq3ntZXiZPvizKeV&q=85&s=cfde0fe257912da8767ea044f61b0559 1650w, https://mintcdn.com/unstructured-53/Tq3ntZXiZPvizKeV/img/ui/walkthrough/GoToEnrichmentNode.png?w=2500&fit=max&auto=format&n=Tq3ntZXiZPvizKeV&q=85&s=a341bac7ef0bfad7be1e436438314411 2500w" />

7. Some interesting portions of the output include the following:

   * The Chinese characters on page 1. Search again for the text `verbs. The characters`. Notice how the accuracy of the Chinese character output is improved.
   * The images on pages 3, 7, and 8. Search again for the text `"Image"` (including the quotation marks). Notice the summary description for each image.
   * The tables on pages 1, 6, 7, 8, 9, and 12. Search again for the text `"Table"` (including the quotation marks). Notice the summary description for each of these tables.
     Also notice the `text_as_html` field for each of these tables.
   * The identified entities and inferred relationships among them. Search for the text `Zhijun Wang`. Of the eight instances of this name, notice
     the author's identification as a `PERSON` three times, the author's `published` relationship twice, and the author's `affiliated_with` relationship twice.

8. When you are done, be sure to click the close (**X**) button above the output on the right side of the screen, to return to
   the workflow designer for the next step.

## Step 5: Experiment with chunking

In this step, you apply [chunking](/ui/chunking) to your workflow. Chunking is the process where Unstructured rearranges
the resulting document elements' `text` content into manageable "chunks" to stay within the limits of an AI model and to improve retrieval precision.

<Tip>
  *What kind of chunking strategy should I use, and how big should my chunks be?*

  Unfortunately, there is no one-size-fits-all answer to this question. However, there are some general considerations and guidelines that can help you to determine
  the best chunking strategy and chunk size for your specific use case. Be sure of course to also consult the documentation for your target AI model and downstream application toolsets.

  Is your content primarily organized by title, by page, by interrelated subject matter, or none of these? This can help you determine whether a
  by-title, by-page, by-similarity, or basic (by-character) chunking strategy is best. (You'll experiment with each of these strategies here later.)

  If your chunks are too small, they might lose necessary context, leading to the model providing inaccurate, irrelevant, or hallucinated results.
  On the other hand, if your chunks are too large, the model can struggle with the sheer volume of information, leading to information overload, diluted meaning, and potentially higher processing costs.
  You should aim to find a balance between chunks that are big enough to contain meaningful information, while small enough to enable performant applications and low latency responses.

  For example, smaller chunks of 128 or 256 tokens might be sufficient for capturing more granular semantic information, while larger chunks of 512 or 1024 tokens might be better for retaining more context.
  It's important here to note that *tokens* and *characters* are not the same thing! In terms of
  characters, for English text, a common approximation is 1 token being equal to about 3 or 4 characters or three-quarters of a word. Many AI model providers publish their own token-to-character calculators online that you can use for estimation purposes.

  You should experiement with a variety of chunk sizes, taking into account the kinds of content, the length and complexity of user queries and agent tasks,
  the intended end use, and of course the limits of the models you are using. Try different chunking strategies and sizes with your models and evaluate the results for yourself.
</Tip>

1. With the workflow designer active from the previous step, just before the **Destination** node, click the add (**+**) icon, and then click **Enrich > Chunker**.

   <img src="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddChunker.png?fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=47f6b2cd36cb6f0df036711ea9426605" alt="Adding a chunker node" data-og-width="672" width="672" data-og-height="416" height="416" data-path="img/ui/walkthrough/AddChunker.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddChunker.png?w=280&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=340e10547b7fd52fe7ff476936cb1925 280w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddChunker.png?w=560&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=8cd2d6acac2fba70f6242d9a43fce0a7 560w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddChunker.png?w=840&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=93c30fcf997272f420e985d0cce36037 840w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddChunker.png?w=1100&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=a89c6dec6dcac999a063881d310a5f1a 1100w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddChunker.png?w=1650&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=9ca9516c8e63d5ebe2a447527634730f 1650w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddChunker.png?w=2500&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=adb5677c9934e5ad66cc1c667e203db8 2500w" />

2. In the node's settings pane's **Details** tab, select **Chunk by Character**.

3. Under **Chunk by Character**, specify the following settings:

   * Check the box labelled **Include Original Elements**.
   * Set **Max Characters** to **500**.
   * Set **New After N Characters** to **400**.
   * Set **Overlap** to **50**.
   * Leave **Contextual Chunking** turned off and **Overlap All** unchecked.

   <img src="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/ChunkByCharacter.png?fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=ecb8f8abe3a0b8289ac807a9092eb66f" alt="Setting up the Chunk by Character strategy" data-og-width="1624" width="1624" data-og-height="1500" height="1500" data-path="img/ui/walkthrough/ChunkByCharacter.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/ChunkByCharacter.png?w=280&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=cd40d4a76a99458a886b8f5a328d4e9c 280w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/ChunkByCharacter.png?w=560&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=7fdb66c932e566bc4e4bafd8ccafe569 560w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/ChunkByCharacter.png?w=840&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=6990da22a2a522c9d25a95f10cbe4f2a 840w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/ChunkByCharacter.png?w=1100&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=b8777a302ae1cdd0e808216dc77dd123 1100w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/ChunkByCharacter.png?w=1650&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=ecc05fd02d05d0f2eeb6e83a70cc95b3 1650w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/ChunkByCharacter.png?w=2500&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=10fef9fc9571df92512aab2e71f0b249 2500w" />

   <Tip>
     *What do each of these chunking settings do?*

     * **Contextual Chunking** prepends chunk-specific explanatory context to each chunk, which has been shown to yield significant improvements in downstream retrieval accuracy. [Learn more](/ui/chunking#contextual-chunking).
     * **Include Original Elements** outputs into each chunk's `metadata` field's `orig_elements` value the elements that were used to form that particular chunk. [Learn more](/ui/chunking#include-original-elements-setting).
     * **Max Characters** is the "hard" or maximum number of characters that any one chunk can contain. Unstructured cannot exceed this number when forming chunks. [Learn more](/ui/chunking#max-characters-setting).
     * **New After N Characters**: is the "soft" or approximate number of characters that any one chunk can contain. Unstructured can exceed this number if needed when forming chunks (but still cannot exceed the **Max Characters** setting). [Learn more](/ui/chunking#new-after-n-characters-setting).
     * **Overlap**, when applied (see **Overlap All**), prepends to the current chunk the specified number of characters from the previous chunk, which can help provide additional context about this chunk relative to the previous chunk. [Learn more](/ui/chunking#overlap-setting)
     * **Overlap All** applies the **Overlap** setting (if greater than zero) to all chunks. Otherwise, unchecking this box means that the **Overlap** setting (if greater than zero)is applied only in edge cases where "normal" chunks cannot be formed by combining whole elements. Check this box with caution as it can introduce noise into otherwise clean semantic units. [Learn more](/ui/chunking#overlap-all-setting).
   </Tip>

4. With the "Chinese Characters" PDF file still selected in the **Source** node, click **Test**.

5. In the **Test output** pane, make sure that **Chunker (7 of 7)** is showing. If not, click the right arrow (**>**) until **Chunker (7 of 7)** appears, which will show the output from the last node in the workflow.

6. To explore the chunker's results, search for the text `"CompositeElement"` (including the quotation marks).

   <Tip>
     *In the chunked output, where did all of the document elements I saw before, such as `Title`, `Image`, and `Table`, go?*

     During chunking, the document elements that were generated during partitioning are now chunked. Because some of these document elements can be split into multiple chunks
     or combined with other chunks, these chunked document elements are now of type `CompositeElement` and `TableChunk`.

     You can have Unstructured also output the original document elements that
     these chunks were derived from by putting them into each chunk's `metadata`. To have Unstructured do this, use the **Include Original Elements** setting, as described in the preceding tip.
   </Tip>

7. Optionally, you can try running this workflow again with the **Chunk by Title** strategy, as follows:

   a. Click the close (**X**) button above the output on the right side of the screen.<br />
   b. In the workflow designer, click the **Chunker** node and then, in the node's settings pane's **Details** tab, select **Chunk by Title**.<br />
   c. Under **Chunk by Title**, specify the following settings:

   * Check the box labelled **Include Original Elements**.
   * Set **Max Characters** to **500**.
   * Set **New After N Characters** to **400**.
   * Set **Overlap** to **50**.
   * Leave **Contextual Chunking** turned off, leave **Combine Text Under N Characters** blank, and leave **Multipage Sections** and **Overlap All** unchecked.

   <Tip>
     *What do each of the chunking settings here that were not already described in the preceding tip do?*

     * **Combine Text Under N Characters** combines elements from a section into a chunk until a section reaches a length of this many characters. [Learn more](/ui/chunking#combine-text-under-n-characters-setting).
     * **Multipage Sections** when checked, allows sections to span multiple pages. [Learn more](/ui/chunking#multipage-sections-setting).
   </Tip>

   d. Click **Test**.<br />
   e. In the **Test output** pane, make sure that **Chunker (7 of 7)** is showing. If not, click the right arrow (**>**) until **Chunker (7 of 7)** appears, which will show the output from the last node in the workflow.<br />
   f. To explore the chunker's results, search for the text `"CompositeElement"` (including the quotation marks). Notice that the lengths of some of the chunks that immediately
   precede titles might be shortened due to the presence of the title impacting the chunk's size.

8. Optionally, you can try running this workflow again with the **Chunk by Page** strategy, as follows:

   a. Click the close (**X**) button above the output on the right side of the screen.<br />
   b. In the workflow designer, click the **Chunker** node and then, in the node's settings pane's **Details** tab, select **Chunk by Page**.<br />
   c. Under **Chunk by Page**, specify the following settings:

   * Check the box labelled **Include Original Elements**.
   * Set **Max Characters** to **500**.
   * Set **New After N Characters** to **400**.
   * Set **Overlap** to **50**.
   * Leave **Contextual Chunking** turned off, and leave **Overlap All** unchecked.

   d. Click **Test**.<br />
   e. In the **Test output** pane, make sure that **Chunker (7 of 7)** is showing. If not, click the right arrow (**>**) until **Chunker (7 of 7)** appears, which will show the output from the last node in the workflow.<br />
   f. To explore the chunker's results, search for the text `"CompositeElement"` (including the quotation marks). Notice that the lengths of some of the chunks that immediately
   precede page breaks might be shortened due to the presence of the page break impacting the chunk's size.<br />

9. Optionally, you can try running this workflow again with the **Chunk by Similarity** strategy, as follows:

   a. Click the close (**X**) button above the output on the right side of the screen.<br />
   b. In the workflow designer, click the **Chunker** node and then, in the node's settings pane's **Details** tab, select **Chunk by Similarity**.<br />
   c. Under **Chunk by Similarity**, specify the following settings:

   * Check the box labelled **Include Original Elements**.
   * Set **Max Characters** to **500**.
   * Set **Similarity Threshold** to **0.99**.
   * Leave **Contextual Chunking** turned off.

   <Tip>
     *What does **Similarity Threshold** mean?*

     * The **Similarity Threshold** is a number between 0 and 1 exclusive (**0.01** to **0.99** inclusive).
     * **0.01** means that any two segments of text that are being compared to each other and are considered least identical in semantic meaning to each other are more likely to be combined into the same chunk together, when such combining must occur.
     * **0.99** means that any two segments of text that are being compared to each other and are considered almost identical in semantic meaning to each other are more likely to be combined into the same chunk together, when such combining must occur.
     * Numbers toward **0.01** bias toward least-identical semantic matches, while numbers toward **0.99** bias toward near-identical semantic matches.
   </Tip>

   d. Click **Test**.<br />
   e. In the **Test output** pane, make sure that **Chunker (7 of 7)** is showing. If not, click the right arrow (**>**) until **Chunker (7 of 7)** appears, which will show the output from the last node in the workflow.<br />
   f. To explore the chunker's results, search for the text `"CompositeElement"` (including the quotation marks). Notice that the lengths of many of the chunks fall well short of the **Max Characters** limit. This is because a similarity threshold
   of **0.99** means that only sentences or text segments with a near-perfect semantic match will be grouped together into the same chunk. This is an extremely high threshold, resulting in very short, highly specific chunks of text. <br />
   g. If you change **Similarity Threshold** to **0.01** and run the workflow again, searching for the text `"CompositeElement"` (including the quotation marks), many of the chunks will now come closer to the **Max Characters** limit. This is because a similarity threshold
   of **0.01** provides an extreme tolerance of differences between pieces of text, grouping almost anything together.<br />

10. When you are done, be sure to click the close (**X**) button above the output on the right side of the screen, to return to
    the workflow designer for the next step.

## Step 6 (Optional): Experiment with embedding

In this step, you generate [embeddings](/ui/embedding) for your workflow. Embeddings are vectors of numbers that represent various aspects of the text that is extracted by Unstructured.
These vectors are stored or "embedded" next to the text itself in a vector store or vector database. Chatbots, agents, and other AI solutions can use
these vector embeddings to more efficiently and effectively find, analyze, and use the associated text. These vector embeddings are generated by an
embedding model that is provided by an embedding provider. For the best embedding model to apply to your use case, see the documentation for your target downstream application toolsets.

1. With the workflow designer active from the previous step, just before the **Destination** node, click the add (**+**) icon, and then click **Transform > Embedder**.

   <img src="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddEmbedder.png?fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=4d049be4f18543fef20362134cf84f41" alt="Adding an embedder node" data-og-width="516" width="516" data-og-height="426" height="426" data-path="img/ui/walkthrough/AddEmbedder.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddEmbedder.png?w=280&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=57d5ffa906c9d6e5b469c6dcd9f76aa2 280w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddEmbedder.png?w=560&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=018e968a2dff5cf9fb8caadbfce0445c 560w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddEmbedder.png?w=840&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=d79683579a735185714eeac6a2fb91a7 840w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddEmbedder.png?w=1100&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=dde31a1658a3d67781fc971ae7888507 1100w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddEmbedder.png?w=1650&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=a8f321eaf4412b988ee0c4e7861d3eef 1650w, https://mintcdn.com/unstructured-53/Ab8t-j4Gj_ozXcQ7/img/ui/walkthrough/AddEmbedder.png?w=2500&fit=max&auto=format&n=Ab8t-j4Gj_ozXcQ7&q=85&s=7c8e53991551435bace6b6c8839e4bd9 2500w" />

2. In the node's settings pane's **Details** tab, under **Select Embedding Model**, for **Azure OpenAI**, select **Text Embedding 3 Small \[dim 1536]**.

3. With the "Chinese Characters" PDF file still selected in the **Source** node, click **Test**.

4. In the **Test output** pane, make sure that **Embedder (8 of 8)** is showing. If not, click the right arrow (**>**) until **Embedder (8 of 8)** appears, which will show the output from the last node in the workflow.

5. To explore the embeddings, search for the text `"embeddings"` (including the quotation marks).

   <Tip>
     *What do all of these numbers mean?*

     All by themselves, the numbers in the `embeddings` field of the output have no human-interpretable meaning on their own.
     However, when combined with the specific text that these numbers are associated with, and the embedding model's
     logic that was used to generate these numbers, the numbers in the `embeddings` field are extremely powerful when leveraged by
     downstream chatbots, agents, and other AI solutions.

     These numbers typically represent complex, abstract attributes about the text that are known only to the embedding model that generated these numbers. These
     attributes can be about the text's overall sentiment, intent, subject, semantic meaning, grammatical function, relationships between words, or any number of other things that the model is good at figuring out. This
     is why the embedding model you choose here must be the exact same embedding model that you use in any related chatbot, agent, or other
     AI solution that relies on these numbers. Otherwise, the numbers that are generated here will not have the same meaning
     downstream as well. Also, the number of *dimensions* (or the number of numbers in the `embeddings` field)
     you choose here must also be the exact same number of dimensions downstream as well.

     To repeat, the name and number of dimensions
     for the embedding model you choose here must be the exact same name and number of dimensions for the embedding model you use in your
     related downstream chatbots, agents, and other AI solutions that rely on this particular text and its associated embeddings that were generated here.
   </Tip>

6. When you are done, be sure to click the close (**X**) button above the output on the right side of the screen, to return to
   the workflow designer so that you can continue designing things later as you see fit.

## Next steps

Congratulations! You now have an Unstructured workflow that partitions, enriches, chunks, and embeds your source documents, producing
context-rich data that is ready for retrieval-augmented generation (RAG), agentic AI, and model fine-tuning.

Right now, your workflow only accepts one local file at a time for input. Your workflow also only sends Unstructured's processed data to your screen or to be saved locally as a JSON file.
You can modify your workflow to accept multiple files and data from—and send Unstructured's processed data to—one or more file storage
locations, databases, and vector stores. To learn how to do this, try one or more of the following quickstarts:

* [Remote quickstart](/ui/quickstart#remote-quickstart) - This quickstart show you how to begin processing files and semi-structured data from remote source locations at scale, instead of just one local file at a time.
* [Dropbox source connector quickstart](/ui/sources/dropbox-source-quickstart) - If you don't have any remote source locations available for Unstructured to connect to, this quickstart shows you how to set up a Dropbox account to store your documents in, and then connect Unstructured to your Dropbox account.
* [Pinecone destination connector quickstart](/ui/destinations/pinecone-destination-quickstart) - If you don't have any remote destination locations available for Unstructured to send its processed data to, this quickstart shows you how to set up a Pinecone account to have Unstructured store its processed data in, and then connect Unstructured to your Pinecone account.

Unstructured also offers an API and SDKs, which allow you to use code to work with Unstructured programmatically instead of only with the UI. For details, see:

* [Unstructured API quickstart](/api-reference/workflow/overview#quickstart) - This quickstart uses the Unstructured Workflow Endpoint to programmatically create a Dropbox source connector and a Pinecone destination connector in your Unstructured account. You then programmatically add these connectors to a workflow in your Unstructured account, run that workflow as a job, and then explore the job's results.
* [Unstructured Python SDK](/api-reference/workflow/overview#unstructured-python-sdk) - This article provides an overview of the Unstructured Python SDK and how to use it.
* [Unstructured API overview](/api-reference/overview) - This article provides an overview of the Unstructured API and how to use it.

If you are not able to complete any of the preceding quickstarts, contact Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).
