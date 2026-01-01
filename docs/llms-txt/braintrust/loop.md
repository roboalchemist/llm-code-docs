# Source: https://braintrust.dev/docs/core/loop.md

# Loop

Loop is Braintrust's AI assistant that helps teams query, analyze, and improve AI in production. Use Loop to search logs semantically, generate filters from natural language, bootstrap scorers, optimize experiments, generate datasets, and more.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop-main.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=a79590b1d265ea02942e292bbd2144a6" alt="Loop" data-og-width="2514" width="2514" data-og-height="1458" height="1458" data-path="images/guides/loop/loop-main.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop-main.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=e13ee83cf20299364bc5ac86367374ae 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop-main.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=a685a9d1f3e22c53e0af5d04a05ca42c 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop-main.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=b14b6fcf2dd77db3007adc362ff5ae04 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop-main.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=a789eeffe24eaefc6971bd05ae8bf76e 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop-main.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=290b1635703c7347641aebd625751197 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop-main.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=50bd7bb730bcae8dfb621c4e11a1396b 2500w" />

## What you can do with Loop

Loop operates on data sources from across your project to summarize, generate, modify, and optimize your observability and evaluation tools based on real application data using natural language.

With Loop, you can:

* [Generate and optimize prompts](#generate-and-optimize-prompts)
* [Generate and optimize scorers](#generate-and-optimize-scorers)
* [Generate, optimize, and analyze datasets](#generate,-optimize,-and-analyze-datasets)
* [Summarize and improve experiments](#summarize-and-improve-experiments)
* [Analyze and filter project logs](#analyze-and-filter-project-logs)
* [Generate and troubleshoot BTQL queries in the BTQL sandbox](#generate-and-troubleshoot-btql-queries-in-the-btql-sandbox)
* [Generate custom charts on the Monitor page](#generate-custom-charts-on-the-monitor-page)
* [Search the documentation](#search-the-documentation)

Loop chat is available in [Playgrounds](/core/playground), [Logs](/core/logs), [Datasets](/core/datasets), [Experiments](/core/experiments), [Scorers](/core/functions/scorers), [Prompts](/core/functions/prompts), and the [BTQL sandbox](/reference/btql#btql-sandbox). Look for the <Icon icon="blend" /> **Loop** button in the bottom right corner of a page to open a window and start a chat, or use product search and look for "Loop".

<img src="https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/loop-logs-page.png?fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=d8de15cb53e88a301a321e94dc00f197" alt="Loop on a Logs page" data-og-width="1986" width="1986" data-og-height="1424" height="1424" data-path="images/core/loop/loop-logs-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/loop-logs-page.png?w=280&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=ef35bef05f0d76e76b31d2d5c37bbb08 280w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/loop-logs-page.png?w=560&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=07ebb2e2c1945d0c968dac39ec893842 560w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/loop-logs-page.png?w=840&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=b33fda0afd4cd4a595aa85433c96ce07 840w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/loop-logs-page.png?w=1100&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=f5b583c3fe62c51a83a018ff479732d1 1100w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/loop-logs-page.png?w=1650&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=f0d4f2485f26cd271fbe1b1ba48d79d5 1650w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/loop-logs-page.png?w=2500&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=685dfff5199b1c45e08376b7c2aea692 2500w" />

Loop keeps track of your queries in a queue, so you can ask multiple follow-ups while it's running. Use the Enter key to interrupt the current operation and execute the next query in the queue.

Loop also keeps a history of your conversations. Edit and re-run earlier Loop chat messages and make inline model and tool changes.

## Setup

### Select a model

Loop uses the AI models available in your Braintrust account via the [Braintrust AI Proxy](/guides/proxy). Only org-level AI providers are supported. We currently support the following models:

* `claude-4.5-sonnet` (recommended)
* `claude-4.5-haiku`
* `claude-4-sonnet`
* `claude-4.1-opus`
* `gpt-5`
* `gpt-4.1`
* `o3`
* `o4-mini`

Change the model in the dropdown at the bottom of the Loop chat window.

Administrators can designate which models are available to be used in Loop for the organization. On your organization's Settings page, select <Icon icon="blend" /> **Loop** and select the models you want to allow in Loop.

### Toggle auto-accept

By default, Loop asks you for confirmation before executing certain tool calls, like running an eval or editing a prompt. To turn on auto-accept, select the <Icon icon="settings-2" /> settings button in your Loop chat window and select **Auto-accept edits**.

### Select data sources

Loop can access different parts of your project, which lets you generate prompts based on datasets, optimize scorers based on results from evals, and run other multidimensional operations.

In a chat, Loop prompts you to select a data source when you make a request that references one. For example, if you tell Loop "use a different dataset" from a playground, Loop asks you to select a dataset as a data source from a dropdown menu.

<img src="https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/specify-data-source.png?fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=05a1170a16ccc1956879e631489a3649" alt="Specity data source" data-og-width="2196" width="2196" data-og-height="1440" height="1440" data-path="images/core/loop/specify-data-source.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/specify-data-source.png?w=280&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=894fe9910e8e24bd883db547fcf2bac9 280w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/specify-data-source.png?w=560&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=ab38899ebb444d65b152a581a65c2b09 560w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/specify-data-source.png?w=840&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=38cbedd74e23877f41753c2ece8b3690 840w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/specify-data-source.png?w=1100&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=19de8e40355419368af3570bf8dad11c 1100w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/specify-data-source.png?w=1650&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=b313450cb6a7bd1b9e9e7bcb58cee529 1650w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/specify-data-source.png?w=2500&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=b4f18bacb1e0c12c997acc05ce057753 2500w" />

You can also give Loop access to data sources in the chat window. Select the <Icon icon="file-plus-2" /> add context icon and search for the data sources you want to let Loop query.

## Generate and optimize prompts

Use Loop to generate, optimize, and edit your [prompts](/core/functions/prompts). Loop can work with prompts from a **Prompt** or **Playground** page.

### Generate prompts

Loop can generate prompts from scratch. On the **Prompts** page, select **+ Prompt** to add a new, blank prompt. On a **Playground** page, [add an empty **Task**](/core/playground#tasks). Then tell Loop to generate a prompt based on your request and it populates the prompt editor with the generated prompt.

Example queries:

* "Generate a prompt for a chatbot that can answer questions about the product"
* "Write a good prompt based on recent logs"

### Edit and optimize prompts

Loop can optimize existing prompts from a **Prompt** or **Playground** page. Ask Loop to optimize the prompt based on your request and it will suggest improvements. In a playground, select the <Icon icon="blend" /> **Loop** icon in the top right corner of a task to automatically select the task as a data source in the Loop chat window or quickly optimize the prompt.

<img src="https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/optimize-prompt.png?fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=69c3c4207216da020e82466eeafa9757" alt="Optimize prompt" data-og-width="2196" width="2196" data-og-height="1440" height="1440" data-path="images/core/loop/optimize-prompt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/optimize-prompt.png?w=280&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=2008620e03918e4e8542bd9cfd4c6deb 280w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/optimize-prompt.png?w=560&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=6ba920cb11ce802d045cf2e416cb4f17 560w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/optimize-prompt.png?w=840&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=0f60a16ade8e1c40d7e413aab475dfcc 840w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/optimize-prompt.png?w=1100&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=a15e98e46caaea6c564c4f5051f84f4b 1100w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/optimize-prompt.png?w=1650&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=2283cbb65a38550537bdc50fba3769d6 1650w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/optimize-prompt.png?w=2500&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=114ec6047beaa5fb8d407bd25f5baba4 2500w" />

Example queries:

* "Add few-shot examples based on project logs"
* "Optimize the prompts in this playground"
* "Improve this prompt to make it friendlier and more engaging"

## Generate and optimize scorers

Use Loop to generate, optimize, and edit your [scorers](/core/functions/scorers). Loop can work with scorers from **Scorer**, **Prompt**, **Experiment**, **Dataset**, or **Playground** pages. You can also generate scorers from the **Logs** page.

### Generate scorers

Loop can generate both code-based and LLM-as-a-judge scorers from scratch. On the **Scorers** page, select **+ Scorer** to add a new, blank scorer. Then tell Loop to generate a scorer based on your request and it populates the scorer editor with the generated scorer.  If you don't specify the type of scorer, Loop generates an LLM-as-a-judge scorer.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/write-new-scorer.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=97aa04fa2c997b8ecea25396ec257478" alt="Create new scorer" data-og-width="2362" width="2362" data-og-height="1634" height="1634" data-path="images/guides/loop/write-new-scorer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/write-new-scorer.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=d5ef47d3587cd41fa6861ef1617e2060 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/write-new-scorer.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=4f7de3f11f9a0c8c93565ba0a8bc3150 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/write-new-scorer.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=c7e1b8966d9894dade47c4d55e4c7cdf 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/write-new-scorer.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=a0ed87e67e958ac22e312a074bec4bda 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/write-new-scorer.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=f6c9ac942cd950081ab032961e70a554 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/write-new-scorer.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=3259195cbdfa57234ec80aa12a8cbbb2 2500w" />

On other pages, tell Loop to generate a new scorer and Loop will save it to your project. Loop gathers context from the resources on the page to build the scorer.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/logsToScorer.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=71ed0861ebcbe0efe5dfc62327d0733e" alt="Generate scorer from logs" data-og-width="4177" width="4177" data-og-height="1304" height="1304" data-path="images/guides/loop/logsToScorer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/logsToScorer.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=ba2ad7a61ee28807763d5e0aa7f01a76 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/logsToScorer.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=11df4f1cabda854bd415892aa26c4238 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/logsToScorer.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=2da287fde7e248781d29e17cba7f50d3 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/logsToScorer.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=3f7c2fb6057edecbe1701dcd775f9eb8 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/logsToScorer.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=a8884e5ff20430dda77ac604e9a08243 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/logsToScorer.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=2e38430332b79f948faa92f8fca1ca4f 2500w" />

Loop can currently only generate code-based scorers for one language at a time. Specify the language you want to use when you generate a code-based scorer.

Example queries:

* "Write a good LLM-as-a-judge scorer for a chatbot that can answer questions about the product"
* "Generate a code-based scorer based on project logs"
* "Generate a code-based scorer based on this dataset"

### Edit and optimize scorers

Loop can optimize existing scorers from a **Scorer** or **Playground** page. Ask Loop to optimize the scorer based on your request and it suggests improvements. If you ask Loop to optimize a built-in scorer from a **Playground** page, it suggests improvements and creates a new scorer with the changes.

Loop can also take manually labelled target classification from evaluations in the playground and adjust scorer classification behavior. Select the rows that the scorers did not perform expectedly on, then select **Tune scorer**.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/tune-scorer-1.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=33ee6fd263f9dea71e47169de39762d0" alt="tune scorer - step 1" data-og-width="1879" width="1879" data-og-height="2293" height="2293" data-path="images/guides/loop/tune-scorer-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/tune-scorer-1.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=b6b1935083542247a06a780424726cec 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/tune-scorer-1.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=a323e7fc17f76eefab6bb128925914b4 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/tune-scorer-1.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=ab0fa97a15bbad1d13e6f78c7a2ce093 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/tune-scorer-1.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=7f66f9f5191c476f7539ec6ac7e47aad 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/tune-scorer-1.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=5af3f7d43a898356f6f32f84332678ec 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/tune-scorer-1.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=2ac53bc21a1fd950a6740282fd0df7b5 2500w" />

Select the desired classification, provide optional additional instruction and submit to Loop to tune the scorer. Loop adjusts the scorer based on the provided context.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/tune-scorer-2.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=3ff21b5d9327315ce52d0b2c6f4ec8e7" alt="tune scorer - step 2" data-og-width="2074" width="2074" data-og-height="1330" height="1330" data-path="images/guides/loop/tune-scorer-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/tune-scorer-2.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=92c4f3d9d762a4ca3aa8de797fc82e9b 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/tune-scorer-2.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=5cab6df2a06b864809d5386023db0c7f 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/tune-scorer-2.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=44165523932bda3c19e111fba148e7e6 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/tune-scorer-2.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=9c88be75c9ce1d15cfc65b046ecbc92e 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/tune-scorer-2.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=d55e12e3ec19ec5c5aa54bfb14d4dc81 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/tune-scorer-2.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=401dfc34fcf4a3e7dbfb290eb059b619 2500w" />

Example queries:

* "Optimize the Helpfulness scorer"
* "Improve the Accuracy scorer based on the first prompt"
* "Adjust the scorer to be more lenient"

## Generate, optimize, and analyze datasets

Use Loop to generate, optimize, and analyze your [datasets](/core/datasets). Loop can analyze a dataset from a **Dataset** or **Playground** page and generate and modify datasets from any other project page.

### Generate datasets

Loop can generate datasets from scratch based on parameters you provide, or it can create a dataset tailored to a specific context in your project. Generate a dataset from a specific page in your project to tailor the dataset to the context of that page.

<img src="https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=37336e72e52b9f902fd94930efe6c3b2" alt="Generate dataset from logs" data-og-width="2196" width="2196" data-og-height="1440" height="1440" data-path="images/core/loop/generate-dataset-from-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?w=280&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=785ed8b42659598dda1691b56f699551 280w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?w=560&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=24ec8f783bf99431a47667810d6b5142 560w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?w=840&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=1faf0cd0f303fe9cd24f0b6de0b67818 840w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?w=1100&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=0865dfcd4958a651495a7567ddab5355 1100w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?w=1650&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=c0f7badaa8b6b2f3d501f542651f458c 1650w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?w=2500&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=29a88190e99b6b806bb29b005b154ad7 2500w" />

Example queries:

* "Generate a dataset from the highest-scoring examples in this experiment"
* "Create a dataset with the most common inputs in the logs"

### Analyze and optimize datasets

On a **Dataset** page or **Playground** page, you can ask Loop to analyze the dataset and generate a report. This gives you a high-level overview of the dataset including the dataset's content, characteristics, strengths, and recommendations for improvement. You can then ask Loop to optimize the dataset based on the report or modify based on your requests.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/optimize-dataset.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=bdf0d67114d7aaabc40c71a4d6c029db" alt="Optimize dataset" data-og-width="2358" width="2358" data-og-height="1664" height="1664" data-path="images/guides/loop/optimize-dataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/optimize-dataset.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=076f4aa114304423971a22a155f18cdc 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/optimize-dataset.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=86fa35f611ee688acc96181c4e5c5f82 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/optimize-dataset.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=0b97980cee3a6983eb5c5dbf35b7937a 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/optimize-dataset.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=3a66f09ca25d7028ac1a61a37923a52b 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/optimize-dataset.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=0fdacd72ce26cccee617b1d870184e6a 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/optimize-dataset.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=6ddef1333f8519b31480036f9f8b69c3 2500w" />

Example queries:

* "Summarize this dataset"
* "Add five more rows"
* "What edge cases are missing from this dataset?"

## Summarize and improve experiments

Use Loop to summarize the results of your [experiments](/core/experiments), drill down into specific eval rows, and make suggestions for changes and improvements.

On your **Experiments** page, select a single experiment or multiple experiments to compare. On the **Experiment** page that opens, ask Loop to summarize the results of the experiments and provide insights. Use these insights to generate or update your datasets, prompts, and scorers. You can also ask Loop to provide sample code for an improved experiment that you can add to your application and run to test the changes.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop-experiment.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=7d1c09e7430e728ce8068bd01b6b7a33" alt="Summarize experiments" data-og-width="2906" width="2906" data-og-height="1508" height="1508" data-path="images/guides/loop/loop-experiment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop-experiment.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=a8cfa99714bc31b1cced392739c545d6 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop-experiment.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=234b457f9c1df077bc3ba858b0b593e6 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop-experiment.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=71e3c8e28ddec70ec9dc367a68c3a401 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop-experiment.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=e9c21ab8e7993e8ab34465b89e04a675 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop-experiment.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=274cc163b0469e03c0da713a203cfb76 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop-experiment.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=32ce8d4422d3d978af487ec4d7e43986 2500w" />

Loop can also analyze specific eval rows and provide insights or suggest improvements. For example, Loop can identify eval rows where a scorer performed poorly and generate a new dataset with those rows. It then gives you suggestions for how to use the dataset to improve your application.

Example queries:

* "What improved from the last experiment?"
* "Categorize the errors in this experiment"
* "Pick the best scorers for this task"

## Analyze and filter project logs

Use Loop to analyze and filter your project's [logs](/core/logs). Loop understands the shape of your logs data and makes arbitrary queries to answer questions and provide insights. You can then use these insights to generate datasets, prompts, scorers, and more.

### Analyze logs

On the **Logs** page, ask Loop to analyze the logs and give you insights. If you don't specify an analysis vector, Loop gives you a comprehensive overview with general insights about health, activity trends, top errors, performance, and recommendations for ways to improve your project.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop_logs.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=086194ec668a33e2499a3c7099c53f8f" alt="Analyze logs" data-og-width="2560" width="2560" data-og-height="1430" height="1430" data-path="images/guides/loop/loop_logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop_logs.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=5a2aab0272987f7e758ed4ac9adcf6e4 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop_logs.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=042f7ad46746ca4c9e811a823a6f7d4b 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop_logs.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=a4955b7d7211a2c55ef424669bf8e93a 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop_logs.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=5f572a5ccf6e5b24a9d9734acda4b665 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop_logs.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=642b6af758bd006c8928823481d8657c 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/loop_logs.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=e1ae8d457b77f263bba66c67a47f9f79 2500w" />

Example queries:

* "What are the most common errors?"
* "What user retention trends do you see?"
* "Find common failure modes"

### Filter logs

Use Loop to generate BTQL queries to filter logs. Select the <Icon icon="list-filter" /> **Filter** button to open the filter editor and select **BTQL** to switch to BTQL mode. Select <Icon icon="blend" /> **Generate** and type in a natural language description of the filter you want to apply. Loop generates a BTQL query based on your description.

Example queries:

* "Only LLM spans"
* "From user John Smith"
* "logs from the last 5 days where factuality score is less than 0.5"

## Generate and troubleshoot BTQL queries in the BTQL sandbox

Use Loop to generate and troubleshoot [BTQL queries](/reference/btql). BTQL queries can return and filter project data, including logs, dataset rows, experiment traces, project prompts, and project scorers.

### Generate and run BTQL queries

Loop can generate BTQL queries from natural language descriptions. For example, you can ask Loop to generate a BTQL query to find the most recent errors from the last 24 hours in your project logs.

In the **BTQL sandbox**, Loop automatically populates the sandbox with the generated BTQL query and runs it. It also gives you a text summary of the results and suggests additional queries you can run to get more insights.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/btql-sandbox.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=159fb80f1b7bb3c8479c927cdb52334d" alt="BTQL sandbox" data-og-width="3022" width="3022" data-og-height="1544" height="1544" data-path="images/guides/loop/btql-sandbox.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/btql-sandbox.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=1be95c4234ed050504468ae257239b8f 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/btql-sandbox.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=93aeee06a301e84415573a94c29554ae 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/btql-sandbox.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=f79f3cacdc565d77d4236c9f605ee50e 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/btql-sandbox.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=92f8c9c46a8e6ee398adc1a272a4cd4c 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/btql-sandbox.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=772e7b615dd132360d2bfd9e485a8bc6 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/btql-sandbox.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=36d322179b388d8f50b19ffdb413c5cc 2500w" />

Example queries:

* "Find the most common errors in logs over the last week"
* "What are the highest scoring rows in my experiment"

Once you have a query in the sandbox, use Loop to update and optimize it.

* "Update the query to show me error distribution over time"
* "Add a filter to only show errors from specific models"

### Troubleshoot BTQL queries

Loop can also help you resolve errors in your BTQL queries. Errors can occur when the query is syntactically incorrect, when the query is not valid against the data schema, or when the query is not valid against the data source. Select the **Fix with Loop** button next to the error in the sandbox. Loop analyzes the specific error type and context to provide targeted fixes, whether it's correcting syntax, suggesting the right field names, or helping optimize query performance.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/btql-parser-fix-with-loop.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=0b27ae0784b1c127f2ccf846b9b7ba58" alt="Fix BTQL query errors" data-og-width="3024" width="3024" data-og-height="1542" height="1542" data-path="images/guides/loop/btql-parser-fix-with-loop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/btql-parser-fix-with-loop.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=c432d53ccb1537ca0c2aec90a1416e19 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/btql-parser-fix-with-loop.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=67232e9a6c322e59bf65ea379592676c 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/btql-parser-fix-with-loop.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=f0cb9be719813165a351f6d727c567a5 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/btql-parser-fix-with-loop.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=5e10ecdbfa7557852be5c29dae9f2635 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/btql-parser-fix-with-loop.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=d741d5dbc93b49b29665a5388a408994 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/btql-parser-fix-with-loop.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=e767eac469c5bc40a86020363c815191 2500w" />

## Generate custom charts on the Monitor page

Use Loop to create a new chart on the [**Monitor**](/core/monitor) page with a natural language description.

On the **Monitor** page, select the <Icon icon="plus" /> **Chart** button in the top right corner to open the chart editor. Use the text input at the top of the editor to describe the chart you want to create. Loop then selects the best chart type and configuration based on the description.

<video className="w-full rounded-md aspect-auto" loop playsInline autoPlay muted>
  <source src="https://mintcdn.com/braintrust/K03I1H4NEGXIvatB/images/guides/loop/chart-generation-loop.mp4?fit=max&auto=format&n=K03I1H4NEGXIvatB&q=85&s=666bfba19e9f4fa235bd6c00779fbe79" type="video/mp4" data-path="images/guides/loop/chart-generation-loop.mp4" />
</video>

Example queries:

* "List the top 5 models by error rate over the last 7 days"
* "Show error rate over time for claude models"

## Search the documentation

Use Loop to search through the Braintrust documentation to find relevant information and guidance. Ask Loop to search the documentation from any page where Loop is available.

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/docs-search-loop.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=59fde0c8eb4fa1f61a248f2321689750" alt="Search docs with loop" data-og-width="2884" width="2884" data-og-height="1798" height="1798" data-path="images/guides/loop/docs-search-loop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/docs-search-loop.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=e5d2b2c3402c50bf96e80e6d5add0645 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/docs-search-loop.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=2197518b3fa4dae33bf3a94fd7b54cb8 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/docs-search-loop.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=7148f6467517014ac541f83318c4c611 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/docs-search-loop.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=64e307da353d97c14ef130a8a88b5795 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/docs-search-loop.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=48fc06ca101300dc912d78ca02cdd3c9 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/docs-search-loop.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=48fa33f193e019744d6c27d5dfc291ad 2500w" />

Example queries:

* "How do I use the Braintrust SDK?"
* "What is the difference between a prompt and a scorer?"
* "How do I use the Braintrust API?"

## Next steps

Try out Loop using these examples:

* From the Logs page: "find queries that took longer than 60 seconds" or "create a dataset from logs with errors"
* From a Prompt page: "optimize this prompt to be friendlier but also more concise" or "add few-shot examples based on project logs"
* From a Dataset page: "add 20 rows with more complex inputs" or "update this dataset to be more helpful when evaluating my most recent prompt"
* From a Playground: "choose the best scorer for this eval" or "generate 10 more dataset rows"
* In the BTQL sandbox: "write a query to return a list of org-level prompts" or "find the highest scoring rows in an experiment"

Check out the [Loop cookbook](/cookbook/recipes/Loop) for more examples and use cases.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt