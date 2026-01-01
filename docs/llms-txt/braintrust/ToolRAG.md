# Source: https://braintrust.dev/docs/cookbook/recipes/ToolRAG.md

# Using functions to build a RAG agent

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/ToolRAG/ToolRAG.mdx) by [Ornella Altunyan](https://twitter.com/ornelladotcom), [Ankur Goyal](https://twitter.com/ankrgyl) on 2024-10-08</div>

Let's say you've built an AI agent to answer questions about your documentation and receive some feedback from users that it doesn't produce
enough code examples in its responses. Normally, you would have to jump into your codebase, tweak the prompt, and try out the changes. If you want
to compare multiple versions side-by-side, you'd have to deploy each version separately.

Using Braintrust, you can experiment with different
prompts together with retrieval logic, side-by-side, all within the playground UI. In this cookbook, we'll walk through exactly how.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Side-by-side.gif?s=2564618f6bcfdd86f9bf278b1df63a09" alt="Side-by-side" data-og-width="1068" width="1068" data-og-height="720" height="720" data-path="cookbook/assets/ToolRAG/Side-by-side.gif" data-optimize="true" data-opv="3" />

## Architecture

Retrieval augmented generation (RAG) is a powerful technique for adding context to your LLM responses. However, the retrieval step involves API calls
and therefore you usually need to iterate on RAG applications in your codebase. Braintrust offers an alternative workflow, where instead, you
`push` the retrieval tool from your codebase to Braintrust. Using Braintrust functions, a RAG agent can be defined as just two components:

* A system prompt containing instructions for how to retrieve content and synthesize answers
* A vector search tool, implemented in TypeScript, which embeds a query, searches for relevant documents, and returns them

In this cookbook, we'll define an agent that answers questions about the Braintrust documentation, iterate on it in the Braintrust playground, and use
scorer functions to evaluate the results.

## Getting started

To get started, you'll need a few accounts:

* [Braintrust](https://www.braintrust.dev/signup)
* [Pinecone](https://app.pinecone.io/?sessionType=signup)
* [OpenAI](https://platform.openai.com/signup)

and `node`, `npm`, and `typescript` installed locally. If you'd like to follow along in code,
the [tool-rag](https://github.com/braintrustdata/braintrust-cookbook/tree/main/examples/ToolRAG/tool-rag)
project contains a working example with all of the documents and code snippets we'll use.

## Clone the repo

To start, clone the repo and install the dependencies:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
git clone https://github.com/braintrustdata/braintrust-cookbook.git
cd braintrust-cookbook/examples/ToolRAG/tool-rag
npm install
```

Next, create a `.env.local` file with your API keys:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
BRAINTRUST_API_KEY=<your-api-key>
PINECONE_API_KEY=<your-pinecone-api-key>
```

Finally, make sure to set your `OPENAI_API_KEY` environment variable in the [AI providers](https://www.braintrust.dev/app/braintrustdata.com/settings/secrets) section
of your account, and set the `PINECONE_API_KEY` environment variable in the [Environment variables](https://www.braintrust.dev/app/settings?subroute=env-vars) section.

<Note>
  We'll use the local environment variables to embed and upload the vectors, and
  the Braintrust variables to run the RAG tool and LLM calls remotely.
</Note>

## Upload the vectors

To upload the vectors, run the `upload-vectors.ts` script:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
npx tsx upload-vectors.ts
```

This script reads all the files from the `docs-sample` directory, breaks them into sections based on headings, and creates vector embeddings for each section using OpenAI's API. It then stores those embeddings along with the section's title and content in Pinecone.

That's it for setup! Now let's try to retrieve the vectors using Braintrust.

## Creating a RAG tool

Braintrust makes it easy to create tools and then run them in the UI, API, and, of course, via prompts. This is
an easy way to iterate on assistant-style agents.

The retrieval tool is defined in `retrieval.ts`:

```javascript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
async ({ query, top_k }) => {
  const embedding = await openai.embeddings
    .create({
      input: query,
      model: "text-embedding-3-small",
    })
    .then((res) => res.data[0].embedding);

  const queryResponse = await pc.query({
    vector: embedding,
    topK: top_k,
    includeMetadata: true,
  });

  return queryResponse.matches.map((match) => ({
    title: match.metadata?.title,
    content: match.metadata?.content,
  }));
};
```

In just a few lines of code, it takes a search query, converts it into a numerical vector using OpenAI's embedding model, and then sends that vector to Pinecone to find the most similar items stored in the database. It retrieves the top results based on similarity and returns key information (title and content) from the matching items.

To push the tool to Braintrust, run:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
npx braintrust push retrieval.ts
```

The output should be:

```
1 file uploaded successfully
```

### Try out the tool

To try out the tool, visit the project in Braintrust, and navigate to **Tools**.

<img src="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/ToolRAG/Test-tool.gif?s=73e38c771f02906fb8196d2956c56464" alt="Test tool" data-og-width="800" width="800" data-og-height="675" height="675" data-path="cookbook/assets/ToolRAG/Test-tool.gif" data-optimize="true" data-opv="3" />

Here, you can test different searches and refine the logic. For example, you could try playing with various
`top_k` values, or adding a prefix to the query to guide the results. If you change the code, run
`npx braintrust push retrieval.ts` again to update the tool.

## Writing a prompt

Next, let's wire the tool into a prompt. In `prompt.ts`, there's an initial definition of the prompt:

```javascript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  messages: [
    {
      role: "system",
      content:
        "You are a helpful assistant that can " +
        "answer questions about the Braintrust documentation.",
    },
    {
      role: "user",
      content: "{{{question}}}",
    },
  ],
```

Run the following command to initialize the prompt:

```
npx braintrust push prompt.ts
```

Once the prompt uploads, you can run it in the UI and even try it out on some examples:

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Test-prompt.gif?s=3cb7143b239d5f4e59fbefe1b004c57a" alt="Test prompt" data-og-width="800" width="800" data-og-height="675" height="675" data-path="cookbook/assets/ToolRAG/Test-prompt.gif" data-optimize="true" data-opv="3" />

If you visit the **Logs** tab, you can check out detailed logs for each call:

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Prompt-logs.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=941c5cb6f92577aa6b37c20cf6df9181" alt="Prompt logs" data-og-width="1050" width="1050" data-og-height="890" height="890" data-path="cookbook/assets/ToolRAG/Prompt-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Prompt-logs.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=a75d6ef45245afb0ffe16a45c6b2c239 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Prompt-logs.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=8089dbaf26b32305309f5587d80e37fa 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Prompt-logs.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=c7b75d4e84521710b250b4fb73565046 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Prompt-logs.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=b9ba878a5ac39310b810ee38299ab65f 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Prompt-logs.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=c11034a307caaf6ab00b904c26e8aaf6 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Prompt-logs.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=65de656e373b0c94860a963e73def94d 2500w" />

<Note>
  We recommend using code-based prompts to initialize projects, but we'll show
  how convenient it is to tweak your prompts in the UI in a moment.
</Note>

## Import a dataset

To get a better sense of how well this prompt and tool work, let's upload a dataset with
a few questions and assertions. The assertions allow us to test specific characteristics
about the answers, without spelling out the exact answer itself.

The dataset is defined in `questions-dataset.ts`, and you can upload it by running:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
npx tsx questions-dataset.ts
```

Once you create it, if you visit the **Datasets** tab, you'll be able to explore it:

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Dataset.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=688782d08e332413181e47ddc0c97b06" alt="Dataset" data-og-width="2730" width="2730" data-og-height="1956" height="1956" data-path="cookbook/assets/ToolRAG/Dataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Dataset.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=2a33b98e50386bd046f1f4b6e05f7a3d 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Dataset.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=0d0127ac9b250edd2e756cc8eaa3de52 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Dataset.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=b73da723db99798182b2ef8ac8573fcf 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Dataset.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=1ca9b3a35c477b82676165be90ed12cd 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Dataset.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=0ba5c1572325b8c367380f93553dd888 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Dataset.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=16ec1d5d663e28bb146b58e2d3769c45 2500w" />

## Create a playground

To try out the prompt together with the dataset, we'll create a playground.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Create-playground.gif?s=a6194c7ec23c0c246765815eeb7755f5" alt="Create playground" data-og-width="800" width="800" data-og-height="573" height="573" data-path="cookbook/assets/ToolRAG/Create-playground.gif" data-optimize="true" data-opv="3" />

Once you create the playground, hit **Run** to run the prompt and tool on the questions
in the dataset.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Run-playground.gif?s=4289a6c5bdc07c9a4347eb9ccd0192f7" alt="Run playground" data-og-width="800" width="800" data-og-height="573" height="573" data-path="cookbook/assets/ToolRAG/Run-playground.gif" data-optimize="true" data-opv="3" />

### Define a scorer

Now that we have an interactive environment to test out our prompt and tool call, let's define
a scorer that helps us evaluate the results.

Select the **Scorers** dropdown menu, then **Create custom scorer**. Choose the **LLM-as-a-judge** tab, and enter

```javascript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
Consider the following question:

{{input.question}}

and answer:

{{output}}

Does the answer satisfy each of the following assertions? Meticulously check each one, and write out your reasoning in the rationale section.

{{#expected.assertions}}
{{.}}
{{/expected.assertions}}

a) It correctly satisfies every assertion.
b) It satisfies some of the assertions
c) It satisfies none of the assertions
```

For the choice scores, configure (a) as 1, (b) as 0.5, and (c) as 0.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Choice-scores.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=0fc0eabaa1ed7374efc862930a7dee68" alt="Choice scores" data-og-width="1158" width="1158" data-og-height="464" height="464" data-path="cookbook/assets/ToolRAG/Choice-scores.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Choice-scores.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=cf05cd117846ae3a29cf21538a4198f5 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Choice-scores.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=83f37e7b8524c339aceba7976cde91b1 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Choice-scores.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=319b1c1f74e65f6a7cf573817afe3d9a 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Choice-scores.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=297e7bfdc9e2bb1e052b9aebefd4b35d 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Choice-scores.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=f249c3a7d626638cc092b73b79e38e90 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Choice-scores.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=8304014e2e5acb4f319ee98cfb762e97 2500w" />

Once you define the scorer, hit **Run** to run it on the questions in the dataset.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Playground-scored.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=bb2b8465985b84415766db6eaa612240" alt="Playground with scores" data-og-width="2726" width="2726" data-og-height="1948" height="1948" data-path="cookbook/assets/ToolRAG/Playground-scored.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Playground-scored.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=f831a343c1efa93b939c7ad0a7217e83 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Playground-scored.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=528af1f7f8113ba797edca6516c5deba 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Playground-scored.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=9a65508dcae64cc7c71779021af9adad 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Playground-scored.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=6b20ae818dac15b59147cfa0cef9f283 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Playground-scored.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=b869cdc755c9aa855d3bec5b3fde0050 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Playground-scored.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=43e3dfa992857de7ea5f0734eb1bb914 2500w" />

### Tweak the prompt

Now, let's tweak the prompt to see if we can improve the results. Hit the copy icon to duplicate your prompt and start tweaking. You can also tweak the original prompt and save your changes there if you'd like. For example, you can try instructing the model to always include a Python and
TypeScript code snippet.

<img src="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/ToolRAG/Tweak-prompt.gif?s=b65473fad6600bad803374b8d2ccdc90" alt="Tweak prompt" data-og-width="800" width="800" data-og-height="572" height="572" data-path="cookbook/assets/ToolRAG/Tweak-prompt.gif" data-optimize="true" data-opv="3" />

Once you're satisfied with the prompt, hit **Update** to save the changes. Each time you save the prompt, you
create a new version. To learn more about how to use a prompt in your code, check out the
[prompts guide](/core/functions/prompts#using-prompts-in-your-code).

## Run full experiments

The playground is very interactive, but if you'd like to create a more detailed evaluation, where you can:

* See every step, including the tool calls and scoring prompts
* Compare side-by-side diffs, improvements, and regressions
* Share a permanent snapshot of results with others on your team

then you can run a full experiment by selecting **+Experiments**. Once you run the experiments, you can dig in further to the full analysis:

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Experiment.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=90db98805bad75a9b74df35dd5e256ba" alt="Experiment" data-og-width="2726" width="2726" data-og-height="1950" height="1950" data-path="cookbook/assets/ToolRAG/Experiment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Experiment.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=64721b57e61c70aa0d800243e1f9eb87 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Experiment.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=eb3364c1974e0da79450bd66421eda49 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Experiment.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=324c4f326c1862268f3ae67801eeac42 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Experiment.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=515f84a5e1efdd8e2e5003e1fa6676c8 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Experiment.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=1f2b75842923e51c796ec1a882d860cb 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/ToolRAG/Experiment.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=72ff3b865c2c767bbf3ebc2166f0726e 2500w" />

## Next steps

Now that you've built a RAG app in Braintrust, you can:

* [Deploy the prompt in your app](/core/functions/prompts#using-prompts-in-your-code)
* [Conduct more detailed evaluations](/core/experiments)
* Learn about [logging LLM calls](/core/logs) to create a data flywheel


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt