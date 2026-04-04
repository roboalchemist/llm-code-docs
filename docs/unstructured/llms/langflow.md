# Source: https://docs.unstructured.io/examplecode/tools/langflow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Langflow

[Langflow](https://www.langflow.org/) is a visual framework for building multi-agent and RAG applications.
It is open-source, fully customizable, and works with most LLMs and many vector stores out of the box.

<img src="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/designer.png?fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=852eec6f836e103a7b9bfa921c99385d" alt="Langflow designer" data-og-width="889" width="889" data-og-height="656" height="656" data-path="img/langflow/designer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/designer.png?w=280&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=b7ae3409dad2733d010402245700ff87 280w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/designer.png?w=560&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=0f4a5ee139a6dd40fa83b7f6597831a8 560w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/designer.png?w=840&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=83c0c41faa2ef9d03a1df84841c61fce 840w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/designer.png?w=1100&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=bdd5e3c6c79d9d6e764c61f50b53a9d9 1100w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/designer.png?w=1650&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=88e77caa1607538895371b43c6d74c22 1650w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/designer.png?w=2500&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=e0ef48c4169e045c2f5db95b2e0900c4 2500w" />

This no-code, hands-on demonstration walks you through creating a Langflow project that enables you to use GPT-4o-mini to chat
in real time with a PDF document that is processed by Unstructured and has its processed data stored in an
[Astra DB](https://www.datastax.com/products/datastax-astra) vector database.

## Prerequisites

<iframe width="560" height="315" src="https://www.youtube.com/embed/PMs1iwL52aM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* An IBM Cloud account or DataStax account.

  * For an IBM Cloud account, [sign up](https://cloud.ibm.com/registration) for an IBMid, and then [sign in](https://accounts.datastax.com/session-service/v1/login) to DataStax with your IBMid.
  * For a DataStax account, [sign up](https://astra.datastax.com/signup) for a DataStax account, and then [sign in](https://accounts.datastax.com/session-service/v1/login) to DataStax with your DataStax account.

* An Astra DB database in the DataStax account. To create a database:

  a. After you sign in to DataStax, click **Create database**.<br />
  b. Click the **Serverless (vector)** tile, if it is not already selected.<br />
  c. For **Database name**, enter some unique name for the database.<br />
  d. Select a **Provider** and a **Region**, and then click **Create database**.<br />

  [Learn more](https://docs.datastax.com/en/astra-db-classic/databases/manage-create.html).

* An application token for the database. To create an application token:

  a. After you sign in to DataStax, in the list of databases, click the name of the target database.<br />
  b. On the **Overview** tab, under **Database Details**, in the **Application Tokens** tile, click **Generate Token**.<br />
  c. Enter some **Token description** and select and **Expiration** time period, and then click **Generate token**.<br />
  d. Save the application token that is displayed to a secure location, and then click **Close**.<br />

  [Learn more](https://docs.datastax.com/en/astra-db-serverless/administration/manage-application-tokens.html).

* A keyspace in the database. To create a keyspace:

  a. After you sign in to DataStax, in the list of databases, click the name of the target database.<br />
  b. On the **Data Explorer** tab, in the **Keyspace** list, select **Create keyspace**.<br />
  c. Enter some **Keyspace name**, and then click **Add keyspace**.<br />

  [Learn more](https://docs.datastax.com/en/astra-db-serverless/databases/manage-keyspaces.html#keyspaces).

* A collection in the keyspace.

  For the [Unstructured UI](/ui/overview) and [Unstructured API](/api-reference/overview):

  * An existing collection is not required. At runtime, the collection behavior is as follows:

    * If an existing collection name is specified, and Unstructured generates embeddings,
      but the number of dimensions that are generated does not match the existing collection's embedding settings, the run will fail.
      You must change your Unstructured embedding settings or your existing collection's embedding settings to match, and try the run again.
    * If a collection name is not specified, Unstructured creates a new collection in your keyspace. If Unstructured generates embeddings,
      the new collection's name will be `u<short-workflow-id>_<short-embedding-model-name>_<number-of-dimensions>`.
      If Unstructured does not generate embeddings, the new collection's name will be `u<short-workflow-id`.

  For [Unstructured Ingest](/open-source/ingestion/overview):

  * For the source connector only, an existing collection is required.
  * For the destination connector only, an existing collection is not required. At runtime, the collection behavior is as follows:

    * If an existing collection name is specified, and Unstructured generates embeddings,
      but the number of dimensions that are generated does not match the existing collection's embedding settings, the run will fail.
      You must change your Unstructured embedding settings or your existing collection's embedding settings to match, and try the run again.
    * If a collection name is not specified, Unstructured creates a new collection in your keyspace. The new collection's name will be `unstructuredautocreated`.

  To create a collection yourself:

  a. After you sign in to DataStax, in the list of databases, click the name of the target database.<br />
  b. On the **Data Explorer** tab, in the **Keyspace** list, select the name of the target keyspace.<br />
  c. In the **Collections** list, select **Create collection**.<br />
  d. Enter some **Collection name**.<br />
  e. Turn on **Vector-enabled collection**, if it is not already turned on.<br />
  f. Choose a mode for **Embedding generation method**. See [Astra DB generated embeddings](#astra-db-generated-embeddings).<br />
  g. If you chose **Bring my own**, enter the number of dimensions for the embedding model that you plan to use.<br />
  h. For **Similarity metric**, select **Cosine**.<br />
  i. Click **Create collection**.<br />

  [Learn more](https://docs.datastax.com/en/astra-db-serverless/databases/manage-collections.html#create-collection).

Also:

* [Sign up for an OpenAI account](https://platform.openai.com/signup), and [get your OpenAI API key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key).
* [Sign up for a free Langflow account](https://astra.datastax.com/signup?type=langflow).
* Get your Unstructured account and Unstructured API key:

  1. If you do not already have an Unstructured account, [sign up for free](https://unstructured.io/?modal=try-for-free).
     After you sign up, you are automatically signed in to your new Unstructured **Let's Go** account, at [https://platform.unstructured.io](https://platform.unstructured.io).

     <Note>
       To sign up for a **Business** account instead, [contact Unstructured Sales](https://unstructured.io/?modal=contact-sales), or [learn more](/api-reference/overview#pricing).
     </Note>

  2. If you have an Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business SaaS** account and are not already signed in, sign in to your account at [https://platform.unstructured.io](https://platform.unstructured.io).

     <Note>
       For other types of **Business** accounts, see your Unstructured account administrator for sign-in instructions,
       or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).
     </Note>

  3. Get your Unstructured API key:<br />

     a. After you sign in to your Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business** account, click **API Keys** on the sidebar.<br />

     <Note>
       For a **Business** account, before you click **API Keys**, make sure you have selected the organizational workspace you want to create an API key
       for. Each API key works with one and only one organizational workspace. [Learn more](/ui/account/workspaces#create-an-api-key-for-a-workspace).
     </Note>

     b. Click **Generate API Key**.<br />
     c. Follow the on-screen instructions to finish generating the key.<br />
     d. Click the **Copy** icon next to your new key to add the key to your system's clipboard. If you lose this key, simply return and click the **Copy** icon again.<br />

## Create and run the demonstration project

<Steps>
  <Step title="Create the Langflow project">
    1. Sign in to your Langflow dashboard.
    2. From your dashboard, click **New Project**.
    3. Click **Blank Flow**.
  </Step>

  <Step title="Add the Unstructured component">
    In this step, you add a component that instructs the legacy Unstructured Partition Endpoint to process a local file that you specify.

    1. On the sidebar, expand **Experimental (Beta)**, and then expand **Loaders**.

    2. Drag the **Unstructured** component onto the designer area.

    3. In the **Unstructured** component, click the box or icon next to **File**, and then select a local file for Unstructured to process.

       This component works only with the file extensions `.pdf`, `.docx`, and `.txt`. Although you can use any local file with one of these extensions,
       this demonstration uses [the text of the United States Constitution in PDF format](https://constitutioncenter.org/media/files/constitution.pdf),
       saved to your local development machine.

       <Tip>
         To work with multiple local files, or to work with remote files, see the suggested options in [Next steps](#next-steps).
       </Tip>

    4. For **Unstructured.io Serverless API Key**, enter your Unstructured API key value.

       <img src="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/unstructured-component.png?fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=cac667e124074c079b3b87c072e7d9bf" alt="Unstructured component" data-og-width="300" width="300" data-og-height="343" height="343" data-path="img/langflow/unstructured-component.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/unstructured-component.png?w=280&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=0b383dd3c65cad6c335c64212f4cb57c 280w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/unstructured-component.png?w=560&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=8e89ce38bd97785d16bd0b1e3fba10d7 560w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/unstructured-component.png?w=840&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=a883043e2fba8c64d5d582e46ece9efb 840w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/unstructured-component.png?w=1100&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=8ceb03746b280e0d29e33492b3c3b631 1100w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/unstructured-component.png?w=1650&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=8255ce7a80bc7e8d78b30aaaef931869 1650w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/unstructured-component.png?w=2500&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=479da08f97af52bb6562f857ef006616 2500w" />

    5. Wait until **Saved** appears in the top navigation bar.

       <img src="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/saved.png?fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=d29665b48a04781f5806efece7999de1" alt="Saved message" data-og-width="332" width="332" data-og-height="188" height="188" data-path="img/langflow/saved.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/saved.png?w=280&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=494a284ed6e18995895d9743af89bbac 280w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/saved.png?w=560&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=3ceeef577d16a7bf7e2251c30e773dbb 560w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/saved.png?w=840&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=06b62386025285585631f178bb132aa2 840w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/saved.png?w=1100&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=e7f642b654dcdbd62fe5a731956e28e7 1100w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/saved.png?w=1650&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=aa82635399b55d39bb99f9404f50cab1 1650w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/saved.png?w=2500&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=ae37ef36e92f5b8c410d6a09a92b6b2d 2500w" />
  </Step>

  <Step title="Add the OpenAI Embeddings component">
    In this step, you add a component that generates vector embeddings for the processed data that Unstructured outputs.

    1. On the sidebar, expand **Embeddings**, and then drag the **OpenAI Embeddings** component onto the designer area.

    2. In the **OpenAI Embeddings** component, for **Model**, select `text-embedding-3-large`.

    3. For **OpenAI API Key**, enter your OpenAI API key's value.

       <img src="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/openai-embeddings-component.png?fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=f2023451994645df89c4d203e4fd8043" alt="OpenAI Embeddings component" data-og-width="302" width="302" data-og-height="302" height="302" data-path="img/langflow/openai-embeddings-component.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/openai-embeddings-component.png?w=280&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=cade9dc87224b3c0450a81d06f963a5c 280w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/openai-embeddings-component.png?w=560&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=3db0a42c7d71189099350e9cfc5b32e4 560w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/openai-embeddings-component.png?w=840&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=0bc635b42442d5a29fa364e6e17ed90e 840w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/openai-embeddings-component.png?w=1100&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=deab3ada3bd71c66fe21dcb35937de57 1100w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/openai-embeddings-component.png?w=1650&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=2f2931b79d99451e6c4726643272302e 1650w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/openai-embeddings-component.png?w=2500&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=3a8b5a7aa8e77b75af43a3ab561d968b 2500w" />

    4. Wait until **Saved** appears in the top navigation bar.
  </Step>

  <Step title="Add the Astra DB components">
    In this step, you add two components. The first component instructs Astra DB to ingest into the specified Astra DB collection the processed data that Unstructured outputs along
    with the associated generated vector embeddings. The second component instructs Astra DB to take user-supplied chat messages and perform contextual
    searches over the ingested data in the specified Astra DB collection, outputting its search results.

    1. On the sidebar, expand **Vector Stores**, and then drag the **Astra DB** component onto the designer area.

    2. Double-click the **Astra DB** component's title bar, and rename the component to `Astra DB Ingest`.

    3. Repeat these previous two actions to add a second **Astra DB** component, renaming it to `Astra DB RAG`.

    4. In both of these **Astra DB** components, in the **Database** list, select the name of your Astra DB database. Make sure this is the same database name in both components.

    5. In the **Collection** list in both components, select the name of the collection in the database. Make sure this is the same collection name in both components.

    6. In the **Astra DB Application Token** box in both components, enter your Astra DB application token's value. Make sure this is the same application token value in both components.

    7. Connect the **Data** output from the **Unstructured** component to the **Ingest Data** input in the **Astra DB Ingest** component.

       To make the connection, click and hold your mouse pointer inside of the circle next to **Data** in the **Unstructured** component.
       While holding your mouse pointer, drag it over into the circle next to **Ingest Data** in the **Astra DB Ingest** component. Then
       release your mouse pointer. A line appears between these two circles.

    8. Connect the **Embeddings** output from the **OpenAI Embeddings** component to the **Embedding or Astra Vectorize** input in the  **Astra DB Ingest** component.

       <img src="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/astra-db-component.png?fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=5ce7cda4d2ea04c9c910540880b04afd" alt="Astra DB component" data-og-width="641" width="641" data-og-height="662" height="662" data-path="img/langflow/astra-db-component.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/astra-db-component.png?w=280&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=029bf986244b66fc9047ba7a50ec72da 280w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/astra-db-component.png?w=560&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=acb001e7a4d7513f1077e7d8321ae505 560w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/astra-db-component.png?w=840&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=e18d697c90a0825a708ed5548c066f87 840w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/astra-db-component.png?w=1100&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=b96ae14858773aef30e72475c085f0c3 1100w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/astra-db-component.png?w=1650&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=28e057a6635aecaf819d276fb9d60a1a 1650w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/astra-db-component.png?w=2500&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=7790fbd32e87bb6d98af782d169094d7 2500w" />

    9. Wait until **Saved** appears in the top navigation bar.

    10. In the title bar of the **Astra DB Ingest** component, click the play icon. This ingests the processed data
        from Unstructured and the associated generated vector embeddings into the specified Astra DB collection.

        <img src="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/build.png?fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=6bd04369d6ab5bb9acbd2edbfadfa18e" alt="Play icon" data-og-width="304" width="304" data-og-height="238" height="238" data-path="img/langflow/build.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/build.png?w=280&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=dcf55c3968bb840f9cf7c11d1e2291aa 280w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/build.png?w=560&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=f2d6fe2216cd4f17e2956e65b59b5875 560w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/build.png?w=840&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=77b15a34ac2665f1fb5bd1ef3d1e47ce 840w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/build.png?w=1100&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=ef144153a824af1f5a7a6eb8d4f8d681 1100w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/build.png?w=1650&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=c275fcb8f78f3ffc253891714004aee1 1650w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/build.png?w=2500&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=c9a578853cab0252f7427067b00ea3a1 2500w" />

    11. Wait until **Building** disppears from the top navigation bar, and a green check mark appears next to this play icon. This could take several minutes.

        <Note>
          Each time you click the play icon in the **Astra DB Ingest** component, Unstructured reprocesses the specified local
          file. If this file does not change, this could result in multiple duplicate records
          being inserted into the specified Astra DB collection. You should only click the play icon in the **Astra DB Ingest** component when you want to insert new processed data into
          the specified Astra DB collection.
        </Note>
  </Step>

  <Step title="Add the Chat Input component">
    In this step, you add a component that takes user-supplied chat messages and sends them as input to Astra DB for contextual searching.

    1. On the sidebar, expand **Inputs**, and then drag the **Chat Input** component onto the designer area.

    2. Connect the **Message** output from the **Chat Input** component to the **Search Input** input in the **Astra DB RAG** component.

       <img src="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/chat-input-component.png?fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=2d30e0b85062cbcc258949a1eb17becc" alt="Chat Input component" data-og-width="612" width="612" data-og-height="555" height="555" data-path="img/langflow/chat-input-component.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/chat-input-component.png?w=280&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=c9284a018b6323f4290693868ebf4539 280w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/chat-input-component.png?w=560&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=13a39f15ad42a65cc06d464ba9a7695a 560w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/chat-input-component.png?w=840&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=d327bc420919de51ae117ed2731f0e3c 840w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/chat-input-component.png?w=1100&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=a655ea34fd605b24293dba97bc75e046 1100w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/chat-input-component.png?w=1650&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=4999760c72c26e5caeebbc6310f0303c 1650w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/chat-input-component.png?w=2500&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=4f882ed9379a03a0b4be24a38f187678 2500w" />

    3. Wait until **Saved** appears in the top navigation bar.
  </Step>

  <Step title="Add the Parse Data component">
    In this step, you add a component that takes the Astra DB search results and converts them into plain text, suitable for inclusion in
    a prompt to a text-based LLM.

    1. On the sidebar, expand **Helpers**, and then drag the **Parse Data** component onto the designer area.

    2. Connect the **Search Results** output from the **Astra DB RAG** component to the **Data** input in the **Parse Data** component.

       <img src="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/parse-data-component.png?fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=aee3ceade9844f8a8f79114451b4efff" alt="Parse Data component" data-og-width="631" width="631" data-og-height="558" height="558" data-path="img/langflow/parse-data-component.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/parse-data-component.png?w=280&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=4d4c76bcc18a5c173feed2b30b700d11 280w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/parse-data-component.png?w=560&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=53149d30f1774f40c349b5e8934c69c0 560w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/parse-data-component.png?w=840&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=ba2f80469e71f0f7097dedb95b9c8351 840w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/parse-data-component.png?w=1100&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=8e16926076d1e43fe7c05979ac8ab8ff 1100w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/parse-data-component.png?w=1650&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=400d970fcdabe603b0bcb84b0dec9ec9 1650w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/parse-data-component.png?w=2500&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=1ba8e2431472250ad9f2c61a97f832b8 2500w" />

    3. Wait until **Saved** appears in the top navigation bar.
  </Step>

  <Step title="Add the Prompt component">
    In this step, you add a component that builds a prompt and then sends it to a text-based LLM.

    1. On the sidebar, expand **Prompts**, and then drag the **Prompt** component onto the designer area.

    2. In the **Prompt** component, next to **Template**, click the box or arrow icon.

    3. In the **Edit Prompt** window, enter the following prompt:

       ```text  theme={null}
       {context}

       ---

       Given the context above, answer the question as best as possible.

       Question: {question}

       Answer: 
       ```

       <Tip>
         To answer the question, the preceding prompt uses the context along with general information that the text-based LLM is
         trained on. To use only the context to answer the question, you can change the prompt, for example to something like this:

         ```text  theme={null}
         {context}

         ---

         Given the context above, answer the question as best as possible. Use only the context to answer the question. Do not use 
         any other sources of information. If the context does not provide enough information to answer the question, reply with 
         'I do not have enough context to answer the question.'

         Question: {question}

         Answer:
         ```
       </Tip>

    4. Click **Check & Save**.

       <img src="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/edit-prompt.png?fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=6fb35fff77621f8a58ee36d7ad8e6918" alt="Prompt component" data-og-width="668" width="668" data-og-height="478" height="478" data-path="img/langflow/edit-prompt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/edit-prompt.png?w=280&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=ff1a2f937929c1e200da935f9df84cfb 280w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/edit-prompt.png?w=560&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=848d15a2e48144bf23619bd3741e982f 560w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/edit-prompt.png?w=840&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=cadf0dcf8c220fbdf874c27e4e0b1774 840w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/edit-prompt.png?w=1100&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=3df4ca6f04cbae6b61794bb526c589e1 1100w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/edit-prompt.png?w=1650&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=6b53a1bea4b64ab5ba19e42ec654cde9 1650w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/edit-prompt.png?w=2500&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=af93f60a7ea0f9408263e8615d7bd0c0 2500w" />

    5. Connect the **Text** output from the **Parse Data** component to the **context** input in the **Prompt** component.

       <img src="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/connect-prompt-component.png?fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=b12062a4f475e7e4d8eb690eac7e0b09" alt="Connect Prompt component" data-og-width="570" width="570" data-og-height="346" height="346" data-path="img/langflow/connect-prompt-component.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/connect-prompt-component.png?w=280&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=9fd01c465685dc7aa68d60d2004ea442 280w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/connect-prompt-component.png?w=560&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=97e7f16d5a33337d6925cc70e54ce20e 560w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/connect-prompt-component.png?w=840&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=7ebc17f173b13993ad038cce38f5fae3 840w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/connect-prompt-component.png?w=1100&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=abd799c03c311fe4ae78b9f34dce8590 1100w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/connect-prompt-component.png?w=1650&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=701a24419153a2733377faa46409b56a 1650w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/connect-prompt-component.png?w=2500&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=6a78b4faeae35296158e78deb9e692ed 2500w" />

    6. Connect the **Message** output from the **Chat Input** component to the **question** input in the **Prompt** component.

       <Note>
         You will now have two connections from the **Message** output in the **Chat Input** component:

         * One connection was already made to the **Search Input** input in the **Astra DB RAG** component.
         * Another connection has just now been made to the **question** input in the **Prompt** component.
       </Note>

    7. Wait until **Saved** appears in the top navigation bar.
  </Step>

  <Step title="Add the OpenAI component">
    In this step, you create a component that sends a prompt to a text-based LLM and outputs the LLM's response.

    1. On the sidebar, expand **Models**, and then drag the **OpenAI** component onto the designer area.

    2. In the **Model Name** list, select **gpt-4o-mini**.

    3. For **OpenAI API Key**, enter your OpenAI API key's value.

    4. For **Temperature**, enter `0.1`.

    5. Connect the **Prompt Message** output from the **Prompt** component to the **Input** input in the **OpenAI** component.

       <img src="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/openai-component.png?fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=01aaa221efac51f332fd15d67ad514ed" alt="OpenAI component" data-og-width="637" width="637" data-og-height="445" height="445" data-path="img/langflow/openai-component.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/openai-component.png?w=280&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=d6cdd28db68fd6308796fb6b6c522572 280w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/openai-component.png?w=560&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=d3a7ea38a2b7fff8e78159f834f28de3 560w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/openai-component.png?w=840&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=630e9932e82212eb09209fa918ac0ca1 840w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/openai-component.png?w=1100&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=d49793a908f2e04f3ede62817fc1d2b3 1100w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/openai-component.png?w=1650&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=2afd4d229f0be16f05888cd05673a8f2 1650w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/openai-component.png?w=2500&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=16df000fcba23aa59232dec0cd6e58ed 2500w" />

    6. Wait until **Saved** appears in the top navigation bar.
  </Step>

  <Step title="Add the Chat Output component">
    In this step, you create a component that returns the answer to the user's original chat message.

    1. On the sidebar, expand **Outputs**, and then drag the **Chat Output** component onto the designer area.

    2. Connect the **Text** output from the **OpenAI** component to the **Text** input in the **Chat Output** component.

       <img src="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/chat-output-component.png?fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=8b65e1dcb81c0c1d65735f8f7817f53e" alt="Chat Output component" data-og-width="563" width="563" data-og-height="403" height="403" data-path="img/langflow/chat-output-component.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/chat-output-component.png?w=280&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=423c8059a05b4511e03d4a6cef4c5b3d 280w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/chat-output-component.png?w=560&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=0978a1ce48ba8d7e341fca34807fcd3b 560w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/chat-output-component.png?w=840&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=10ff261c061e0b7e17f21251604b3cc7 840w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/chat-output-component.png?w=1100&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=f4f2cf4be656460bdb1739aee426ca78 1100w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/chat-output-component.png?w=1650&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=73ff59bfcbc4ab8e66a36ead62b86c0e 1650w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/chat-output-component.png?w=2500&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=a2ced3bf796befc226cdfdb7ae6ad14d 2500w" />

    3. Wait until **Saved** appears in the top navigation bar.

    The final project should look like this:

        <img src="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/final-project.png?fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=de1291d825959b4372c735d72a2b44e2" alt="Final project results" data-og-width="1281" width="1281" data-og-height="821" height="821" data-path="img/langflow/final-project.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/final-project.png?w=280&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=3ebb819762d5e0518dcb27f9497aa5eb 280w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/final-project.png?w=560&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=eda7ceb544c4c864ffc6d21511eb1e26 560w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/final-project.png?w=840&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=131300deec714573611ed0141395147a 840w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/final-project.png?w=1100&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=0bb2fcb6c075cb5eb4fdfebe22bc5c32 1100w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/final-project.png?w=1650&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=45e8e8afd082d6fc6a2d88336cd1519e 1650w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/final-project.png?w=2500&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=d52323f672344dd09f355c7dbacfac6e 2500w" />
  </Step>

  <Step title="Run the project">
    1. In the designer area, click **Playground**.

       <img src="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/open-playground.png?fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=c2e028f53b624a3796ef9aca63a15482" alt="Open Playground button" data-og-width="248" width="248" data-og-height="121" height="121" data-path="img/langflow/open-playground.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/open-playground.png?w=280&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=38d917b5cae796c3b86beeb8651b804c 280w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/open-playground.png?w=560&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=6e5f8397d7c1187217ef27fcec9e7ca4 560w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/open-playground.png?w=840&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=24f604cbe6848d68e11592f54b6ef714 840w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/open-playground.png?w=1100&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=c6df8b9f561a989a56b787e1fcc73e35 1100w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/open-playground.png?w=1650&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=d93f6a23090ea8eca52fe574d0b9cba1 1650w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/open-playground.png?w=2500&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=a1a2a65eeba16231583d820c05b44093 2500w" />

    2. Enter a question into the chat box, for example, `What rights does the fifth amendment guarantee?` Then press the send button.

       <img src="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/playground.png?fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=3fc1e1a430ab4bf1d0354df333a2d939" alt="Playground window" data-og-width="927" width="927" data-og-height="488" height="488" data-path="img/langflow/playground.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/playground.png?w=280&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=535a1caa67389b4e306dfebe3eeb2af3 280w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/playground.png?w=560&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=2b5366a9bc31d529fc3e5e432d1fb910 560w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/playground.png?w=840&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=c71b744f4a523b9979c6aae6ca770d76 840w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/playground.png?w=1100&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=3a63f491a7fa7b5ed5086850e6feef85 1100w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/playground.png?w=1650&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=0e62204226159ad49b942153514ca6f1 1650w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/langflow/playground.png?w=2500&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=b72180ce106cc2ce7e7d340059969ef4 2500w" />

    3. Wait until the answer appears.

    4. Ask as many additional questions as you want to.
  </Step>
</Steps>

## Next steps

Now that you have your pipeline set up, here are just a few ways that you could modify it to support different requirements,
such as processing multiple files or using a different vector store.

### Process multiple files

In this demonstration, you pass to Unstructured a single local file. To pass multiple local or
non-local files to Unstructured instead, you can use the
[Unstructured UI](/ui/overview) or the [Unstructured API](/api-reference/overview) or
[Unstructured Ingest](/open-source/ingestion/overview) outside of Langflow.

To do this, you can:

* [Use the Unstructured UI to create a workflow](/ui/quickstart) that relies on any available
  [source connector](/ui/sources/overview) to connect to
  [Astra DB](/ui/destinations/astradb). Run this workflow outside of Langflow anytime you have new documents in that source location that
  you want Unstructured to process and then insert the new processed data into Astra DB. Then, back in the Langflow project,
  use the **Playground** to ask additional questions, which will now include the new data when generating answers.

* [Use Unstructured Ingest to create a pipeline](/open-source/ingestion/overview) that relies on any available
  [source connector](/open-source/ingestion/source-connectors/overview) to connect to
  [Astra DB](/open-source/ingestion/destination-connectors/astradb). Run this pipeline outside of Langflow anytime you have new documents in that non-local source location that
  you want Unstructured to process and then insert the new processed data into Astra DB. Then, back in the Langflow project,
  use the **Playground** to ask additonal questions, which will now include the new data when generating answers.

### Use a different vector store

In this demonstration, you use Astra DB as the vector store. Langflow and Unstructured support several vector stores in addition to Astra DB.

To do this, you can:

[Use the Unstructured UI to create a workflow](/ui/quickstart) that relies on any available
[source connector](/ui/sources/overview) to connect to
one of the following available vector stores that Langflow also supports:

* [Milvus](/ui/destinations/milvus)
* [MongoDB](/ui/destinations/mongodb)
* [Pinecone](/ui/destinations/pinecone)

Run this workflow outside of Langflow anytime you have new documents in the source location that
you want Unstructured to process and then insert the new processed data into the vector store. Then, back in the Langflow project,
swap out the **Astra DB RAG** component for the corresponding **Vector Stores** component that matches the new vector
store's name. Configure the new component, and then
use the **Playground** to ask additional questions, which will now use the new vector store when generating answers.

Or, [use Unstructured Ingest to create a pipeline](/open-source/ingestion/overview) that relies on any available
[source connector](/open-source/ingestion/source-connectors/overview) to connect to
one of the following available vector stores that Langflow also supports:

* [Chroma DB](/open-source/ingestion/destination-connectors/chroma)
* [Couchbase](/open-source/ingestion/destination-connectors/couchbase)
* [Elasticsearch](/open-source/ingestion/destination-connectors/elasticsearch)
* [Milvus](/open-source/ingestion/destination-connectors/milvus)
* [MongoDB](/open-source/ingestion/destination-connectors/mongodb)
* [OpenSearch](/open-source/ingestion/destination-connectors/opensearch)
* [Pinecone](/open-source/ingestion/destination-connectors/pinecone)
* [Qdrant](/open-source/ingestion/destination-connectors/qdrant)
* [Vectara](/open-source/ingestion/destination-connectors/vectara)
* [Weaviate](/open-source/ingestion/destination-connectors/weaviate)

Run this pipeline outside of Langflow anytime you have new documents in the source location that
you want Unstructured to process and then insert the new processed data into the vector store. Then, back in the Langflow project,
swap out the **Astra DB RAG** component for the corresponding **Vector Stores** component that matches the new vector
store's name. Configure the new component, and then
use the **Playground** to ask additional questions, which will now use the new vector store when generating answers.

## Learn more

* See the [Langflow documentation](https://docs.langflow.org/).
* <Icon icon="blog" />  [No-Code AI Assistant in No Time with Unstructured Platform, AstraDB, and Langflow](https://unstructured.io/blog/no-code-ai-assistant-in-no-time-with-unstructured-platform-astradb-and-langflow)
