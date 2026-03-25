# Source: https://docs.wandb.ai/weave/tutorial-rag.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluate RAG applications

> Build and evaluate RAG applications using Weave with LLM judges

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

export const ColabLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="colab-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01.21.03zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z" />
    </svg>
    Try in Colab
  </a>;

<div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap' }}>
  <ColabLink url="https://colab.research.google.com/github/wandb/docs/blob/main/weave/cookbooks/source/evaluate_rag_applications.ipynb" />

  <GitHubLink url="https://github.com/wandb/docs/blob/main/weave/cookbooks/source/evaluate_rag_applications.ipynb" />
</div>

Retrieval Augmented Generation (RAG) is a common way of building Generative AI applications that have access to custom knowledge bases.

<img src="https://mintcdn.com/wb-21fd5541/aRvhhwVWqlxBzke5/images/evals-hero.png?fit=max&auto=format&n=aRvhhwVWqlxBzke5&q=85&s=7d7466d666ad412ed3916bfab533d118" alt="Evals hero" width="4100" height="2160" data-path="images/evals-hero.png" />

## What you'll learn:

This guide shows you how to:

* Build a knowledge base
* Create a RAG application with a retrieval step that finds relevant documents
* Track retrieval steps with Weave
* Evaluate RAG applications using an LLM judge to measure context precision
* Define custom scoring functions

## Prerequisites

* A [W\&B account](https://wandb.ai/signup)
* Python 3.8+ or Node.js 18+
* Required packages installed:
  * **Python**: `pip install weave openai`
  * **TypeScript**: `npm install weave openai`
* An [OpenAI API key](https://platform.openai.com/api-keys) set as an environment variable

## Build a knowledge base

First, compute the embeddings for the articles. You would typically do this once with your articles and put the embeddings and metadata in a database, but here it's done every time the script runs for simplicity.

<Tabs>
  <Tab title="Python">
    ```python lines theme={null}
    from openai import OpenAI
    import weave
    from weave import Model
    import numpy as np
    import json
    import asyncio

    articles = [
        "Novo Nordisk and Eli Lilly rival soars 32 percent after promising weight loss drug results Shares of Denmarks Zealand Pharma shot 32 percent higher in morning trade, after results showed success in its liver disease treatment survodutide, which is also on trial as a drug to treat obesity. The trial “tells us that the 6mg dose is safe, which is the top dose used in the ongoing [Phase 3] obesity trial too,” one analyst said in a note. The results come amid feverish investor interest in drugs that can be used for weight loss.",
        "Berkshire shares jump after big profit gain as Buffetts conglomerate nears $1 trillion valuation Berkshire Hathaway shares rose on Monday after Warren Buffetts conglomerate posted strong earnings for the fourth quarter over the weekend. Berkshires Class A and B shares jumped more than 1.5%, each. Class A shares are higher by more than 17% this year, while Class B has gained more than 18%. Berkshire was last valued at $930.1 billion, up from $905.5 billion where it closed on Friday, according to FactSet. Berkshire on Saturday posted fourth-quarter operating earnings of $8.481 billion, about 28 percent higher than the $6.625 billion from the year-ago period, driven by big gains in its insurance business. Operating earnings refers to profits from businesses across insurance, railroads and utilities. Meanwhile, Berkshires cash levels also swelled to record levels. The conglomerate held $167.6 billion in cash in the fourth quarter, surpassing the $157.2 billion record the conglomerate held in the prior quarter.",
        "Highmark Health says its combining tech from Google and Epic to give doctors easier access to information Highmark Health announced it is integrating technology from Google Cloud and the health-care software company Epic Systems. The integration aims to make it easier for both payers and providers to access key information they need, even if its stored across multiple points and formats, the company said. Highmark is the parent company of a health plan with 7 million members, a provider network of 14 hospitals and other entities",
        "Rivian and Lucid shares plunge after weak EV earnings reports Shares of electric vehicle makers Rivian and Lucid fell Thursday after the companies reported stagnant production in their fourth-quarter earnings after the bell Wednesday. Rivian shares sank about 25 percent, and Lucids stock dropped around 17 percent. Rivian forecast it will make 57,000 vehicles in 2024, slightly less than the 57,232 vehicles it produced in 2023. Lucid said it expects to make 9,000 vehicles in 2024, more than the 8,428 vehicles it made in 2023.",
        "Mauritius blocks Norwegian cruise ship over fears of a potential cholera outbreak Local authorities on Sunday denied permission for the Norwegian Dawn ship, which has 2,184 passengers and 1,026 crew on board, to access the Mauritius capital of Port Louis, citing “potential health risks.” The Mauritius Ports Authority said Sunday that samples were taken from at least 15 passengers on board the cruise ship. A spokesperson for the U.S.-headquartered Norwegian Cruise Line Holdings said Sunday that 'a small number of guests experienced mild symptoms of a stomach-related illness' during Norwegian Dawns South Africa voyage.",
        "Intuitive Machines lands on the moon in historic first for a U.S. company Intuitive Machines Nova-C cargo lander, named Odysseus after the mythological Greek hero, is the first U.S. spacecraft to soft land on the lunar surface since 1972. Intuitive Machines is the first company to pull off a moon landing — government agencies have carried out all previously successful missions. The company's stock surged in extended trading Thursday, after falling 11 percent in regular trading.",
        "Lunar landing photos: Intuitive Machines Odysseus sends back first images from the moon Intuitive Machines cargo moon lander Odysseus returned its first images from the surface. Company executives believe the lander caught its landing gear sideways on the moon's surface while touching down and tipped over. Despite resting on its side, the company's historic IM-1 mission is still operating on the moon.",
    ]

    def docs_to_embeddings(docs: list) -> list:
        openai = OpenAI()
        document_embeddings = []
        for doc in docs:
            response = (
                openai.embeddings.create(input=doc, model="text-embedding-3-small")
                .data[0]
                .embedding
            )
            document_embeddings.append(response)
        return document_embeddings

    article_embeddings = docs_to_embeddings(articles) # Note: you would typically do this once with your articles and put the embeddings & metadata in a database
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript lines theme={null}
    require('dotenv').config();
    import { OpenAI } from 'openai';
    import * as weave from 'weave';

    interface Article {
        text: string;
        embedding?: number[];
    }

    const articles: Article[] = [
        { 
            text: `Novo Nordisk and Eli Lilly rival soars 32 percent after promising weight loss drug results Shares of Denmarks Zealand Pharma shot 32 percent higher in morning trade, after results showed success in its liver disease treatment survodutide, which is also on trial as a drug to treat obesity. The trial tells us that the 6mg dose is safe, which is the top dose used in the ongoing [Phase 3] obesity trial too, one analyst said in a note. The results come amid feverish investor interest in drugs that can be used for weight loss.`
        },
        { 
            text: `Berkshire shares jump after big profit gain as Buffetts conglomerate nears $1 trillion valuation Berkshire Hathaway shares rose on Monday after Warren Buffetts conglomerate posted strong earnings for the fourth quarter over the weekend. Berkshires Class A and B shares jumped more than 1.5%, each. Class A shares are higher by more than 17% this year, while Class B has gained more than 18%. Berkshire was last valued at $930.1 billion, up from $905.5 billion where it closed on Friday, according to FactSet. Berkshire on Saturday posted fourth-quarter operating earnings of $8.481 billion, about 28 percent higher than the $6.625 billion from the year-ago period, driven by big gains in its insurance business. Operating earnings refers to profits from businesses across insurance, railroads and utilities. Meanwhile, Berkshires cash levels also swelled to record levels. The conglomerate held $167.6 billion in cash in the fourth quarter, surpassing the $157.2 billion record the conglomerate held in the prior quarter.`
        },
        { 
            text: `Highmark Health says its combining tech from Google and Epic to give doctors easier access to information Highmark Health announced it is integrating technology from Google Cloud and the health-care software company Epic Systems. The integration aims to make it easier for both payers and providers to access key information they need, even if its stored across multiple points and formats, the company said. Highmark is the parent company of a health plan with 7 million members, a provider network of 14 hospitals and other entities`
        }
    ];

    function cosineSimilarity(a: number[], b: number[]): number {
        const dotProduct = a.reduce((sum, val, i) => sum + val * b[i], 0);
        const magnitudeA = Math.sqrt(a.reduce((sum, val) => sum + val * val, 0));
        const magnitudeB = Math.sqrt(b.reduce((sum, val) => sum + val * val, 0));
        return dotProduct / (magnitudeA * magnitudeB);
    }

    const docsToEmbeddings = weave.op(async function(docs: Article[]): Promise<Article[]> {
        const openai = new OpenAI();
        const enrichedDocs = await Promise.all(docs.map(async (doc) => {
            const response = await openai.embeddings.create({
                input: doc.text,
                model: "text-embedding-3-small"
            });
            return {
                ...doc,
                embedding: response.data[0].embedding
            };
        }));
        return enrichedDocs;
    });
    ```
  </Tab>
</Tabs>

## Create a RAG app

Next, wrap the retrieval function `get_most_relevant_document` with a `weave.op()` decorator and create a `Model` class. Call `weave.init('<team-name>/rag-quickstart')` to begin tracking all the inputs and outputs of your functions for later inspection. If you do not specify a team name, the output is recorded to your [W\&B default team or entity](/platform/app/settings-page/user-settings#default-team).

<Tabs>
  <Tab title="Python">
    ```python lines theme={null}
    from openai import OpenAI
    import weave
    from weave import Model
    import numpy as np
    import asyncio

    @weave.op()
    def get_most_relevant_document(query):
        openai = OpenAI()
        query_embedding = (
            openai.embeddings.create(input=query, model="text-embedding-3-small")
            .data[0]
            .embedding
        )
        similarities = [
            np.dot(query_embedding, doc_emb)
            / (np.linalg.norm(query_embedding) * np.linalg.norm(doc_emb))
            for doc_emb in article_embeddings
        ]
        # Get the index of the most similar document
        most_relevant_doc_index = np.argmax(similarities)
        return articles[most_relevant_doc_index]

    class RAGModel(Model):
        system_message: str
        model_name: str = "gpt-3.5-turbo-1106"

        @weave.op()
        def predict(self, question: str) -> dict: # note: `question` will be used later to select data from our evaluation rows
            from openai import OpenAI
            context = get_most_relevant_document(question)
            client = OpenAI()
            query = f"""Use the following information to answer the subsequent question. If the answer cannot be found, write "I don't know."
            Context:
            \"\"\"
            {context}
            \"\"\"
            Question: {question}"""
            response = client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": self.system_message},
                    {"role": "user", "content": query},
                ],
                temperature=0.0,
                response_format={"type": "text"},
            )
            answer = response.choices[0].message.content
            return {'answer': answer, 'context': context}

    # Set your team and project names
    weave.init('<team-name>/rag-quickstart')
    model = RAGModel(
        system_message="You are an expert in finance and answer questions related to finance, financial services, and financial markets. When responding based on provided information, be sure to cite the source."
    )
    model.predict("What significant result was reported about Zealand Pharma's obesity trial?")
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript lines theme={null}
    class RAGModel {
        private openai: OpenAI;
        private systemMessage: string;
        private modelName: string;
        private articleEmbeddings: Article[];

        constructor(config: {
            systemMessage: string;
            modelName?: string;
            articleEmbeddings: Article[];
        }) {
            this.openai = new OpenAI();
            this.systemMessage = config.systemMessage;
            this.modelName = config.modelName || "gpt-3.5-turbo-1106";
            this.articleEmbeddings = config.articleEmbeddings;
            this.predict = weave.op(this, this.predict);
        }

        async predict(question: string): Promise<{
            answer: string;
            context: string;
        }> {
            const context = await this.getMostRelevantDocument(question);
            
            const response = await this.openai.chat.completions.create({
                model: this.modelName,
                messages: [
                    { role: "system", content: this.systemMessage },
                    { role: "user", content: `Use the following information to answer the subsequent question. If the answer cannot be found, write "I don't know."
                        Context:
                        """
                        ${context}
                        """
                        Question: ${question}` }
                ],
                temperature: 0
            });

            return {
                answer: response.choices[0].message.content || "",
                context
            };
        }
    }
    ```
  </Tab>
</Tabs>

## Evaluating with an LLM Judge

When there aren't simple ways to evaluate your application, one approach is to use an LLM to evaluate aspects of it. Here is an example of using an LLM judge to try to measure the context precision by prompting it to verify if the context was useful in arriving at the given answer. This prompt was augmented from the popular [RAGAS framework](https://docs.ragas.io/en/stable/).

### Defining a scoring function

As in the [Build an Evaluation pipeline tutorial](/weave/tutorial-eval), define a set of example rows to test your app against and a scoring function. The scoring function takes one row and evaluates it. The input arguments should match with the corresponding keys in your row, so `question` here is taken from the row dictionary. `output` is the output of the model. The input to the model is taken from the example based on its input argument, so `question` here too. This example uses `async` functions so they run fast in parallel. If you need a quick introduction to async, you can find one [here](https://docs.python.org/3/library/asyncio.html).

<Tabs>
  <Tab title="Python">
    ```python lines theme={null}
    from openai import OpenAI
    import weave
    import asyncio

    @weave.op()
    async def context_precision_score(question, output):
        context_precision_prompt = """Given question, answer and context verify if the context was useful in arriving at the given answer. Give verdict as "1" if useful and "0" if not with json output.
        Output in only valid JSON format.

        question: {question}
        context: {context}
        answer: {answer}
        verdict: """
        client = OpenAI()

        prompt = context_precision_prompt.format(
            question=question,
            context=output['context'],
            answer=output['answer'],
        )

        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[{"role": "user", "content": prompt}],
            response_format={ "type": "json_object" }
        )
        response_message = response.choices[0].message
        response = json.loads(response_message.content)
        return {
            "verdict": int(response["verdict"]) == 1,
        }

    questions = [
        {"question": "What significant result was reported about Zealand Pharma's obesity trial?"},
        {"question": "How much did Berkshire Hathaway's cash levels increase in the fourth quarter?"},
        {"question": "What is the goal of Highmark Health's integration of Google Cloud and Epic Systems technology?"},
        {"question": "What were Rivian and Lucid's vehicle production forecasts for 2024?"},
        {"question": "Why was the Norwegian Dawn cruise ship denied access to Mauritius?"},
        {"question": "Which company achieved the first U.S. moon landing since 1972?"},
        {"question": "What issue did Intuitive Machines' lunar lander encounter upon landing on the moon?"}
    ]
    evaluation = weave.Evaluation(dataset=questions, scorers=[context_precision_score])
    asyncio.run(evaluation.evaluate(model)) # note: you'll need to define a model to evaluate
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript lines theme={null}
    const contextPrecisionScore = weave.op(async function(args: {
        datasetRow: QuestionRow;
        modelOutput: { answer: string; context: string; }
    }): Promise<ScorerResult> {
        const openai = new OpenAI();
        
        const prompt = `Given question, answer and context verify if the context was useful...`;

        const response = await openai.chat.completions.create({
            model: "gpt-4-turbo-preview",
            messages: [{ role: "user", content: prompt }],
            response_format: { type: "json_object" }
        });

        const result = JSON.parse(response.choices[0].message.content || "{}");
        return {
            verdict: parseInt(result.verdict) === 1
        };
    });

    const evaluation = new weave.Evaluation({
        dataset: createQuestionDataset(),
        scorers: [contextPrecisionScore]
    });

    await evaluation.evaluate({
        model: weave.op((args: { datasetRow: QuestionRow }) => 
            model.predict(args.datasetRow.question)
        )
    });
    ```
  </Tab>
</Tabs>

### Optional: Defining a `Scorer` class

In some applications you may want to create custom evaluation classes - where for example a standardized `LLMJudge` class should be created with specific parameters (e.g. chat model, prompt), specific scoring of each row, and specific calculation of an aggregate score. Weave defines a list of ready-to-use `Scorer` classes and also makes it easy to create a custom `Scorer` - the following example shows how to create a custom `class CorrectnessLLMJudge(Scorer)`.

On a high-level the steps to create custom Scorer are quite simple:

1. Define a custom class that inherits from `weave.flow.scorer.Scorer`
2. Overwrite the `score` function and add a `@weave.op()` if you want to track each call of the function
   * this function has to define an `output` argument where the prediction of the model will be passed to. Define it as type `Optional[dict]` in case the model might return "None".
   * the rest of the arguments can either be a general `Any` or `dict` or can select specific columns from the dataset that is used to evaluate the model using the `weave.Evaluate` class - they have to have the exact same names as the column names or keys of a single row after being passed to `preprocess_model_input` if that is used.
3. *Optional:* Overwrite the `summarize` function to customize the calculation of the aggregate score. By default Weave uses the `weave.flow.scorer.auto_summarize` function if you don't define a custom function.
   * this function has to have a `@weave.op()` decorator.

<Tabs>
  <Tab title="Python">
    ```python lines theme={null}
    from weave import Scorer

    class CorrectnessLLMJudge(Scorer):
        prompt: str
        model_name: str
        device: str

        @weave.op()
        async def score(self, output: Optional[dict], query: str, answer: str) -> Any:
            """Score the correctness of the predictions by comparing the pred, query, target.
            Args:
                - output: the dict that will be provided by the model that is evaluated
                - query: the question asked - as defined in the dataset
                - answer: the target answer - as defined in the dataset
            Returns:
                - single dict {metric name: single evaluation value}"""

            # get_model is defined as general model getter based on provided params (OpenAI,HF...)
            eval_model = get_model(
                model_name = self.model_name,
                prompt = self.prompt
                device = self.device,
            )
            # async evaluation to speed up evaluation - this doesn't have to be async
            grade = await eval_model.async_predict(
                {
                    "query": query,
                    "answer": answer,
                    "result": output.get("result"),
                }
            )
            # output parsing - could be done more reobustly with pydantic
            evaluation = "incorrect" not in grade["text"].strip().lower()

            # the column name displayed in Weave
            return {"correct": evaluation}

        @weave.op()
        def summarize(self, score_rows: list) -> Optional[dict]:
            """Aggregate all the scores that are calculated for each row by the scoring function.
            Args:
                - score_rows: a list of dicts. Each dict has metrics and scores
            Returns:
                - nested dict with the same structure as the input"""

            # if nothing is provided the weave.flow.scorer.auto_summarize function is used
            # return auto_summarize(score_rows)

            valid_data = [x.get("correct") for x in score_rows if x.get("correct") is not None]
            count_true = list(valid_data).count(True)
            int_data = [int(x) for x in valid_data]

            sample_mean = np.mean(int_data) if int_data else 0
            sample_variance = np.var(int_data) if int_data else 0
            sample_error = np.sqrt(sample_variance / len(int_data)) if int_data else 0

            # the extra "correct" layer is not necessary but adds structure in the UI
            return {
                "correct": {
                    "true_count": count_true,
                    "true_fraction": sample_mean,
                    "stderr": sample_error,
                }
            }
    ```
  </Tab>

  <Tab title="TypeScript">
    ```plaintext  theme={null}
    This feature is not available in TypeScript yet.
    ```
  </Tab>
</Tabs>

To use this as a scorer, you would initialize it and pass it to `scorers` argument in your \`Evaluation like this:

<Tabs>
  <Tab title="Python">
    ```python lines theme={null}
    evaluation = weave.Evaluation(dataset=questions, scorers=[CorrectnessLLMJudge()])
    ```
  </Tab>

  <Tab title="TypeScript">
    ```plaintext  theme={null}
    This feature is not available in TypeScript yet.
    ```
  </Tab>
</Tabs>

## Pulling it all together

To get the same result for your RAG apps:

* Wrap LLM calls & retrieval step functions with `weave.op()`
* (optional) Create a `Model` subclass with `predict` function and app details
* Collect examples to evaluate
* Create scoring functions that score one example
* Use `Evaluation` class to run evaluations on your examples

**NOTE:** Sometimes the async execution of Evaluations will trigger a rate limit on the models of OpenAI, Anthropic, etc. To prevent that you can set an environment variable to limit the amount of parallel workers e.g. `WEAVE_PARALLELISM=3`.

Here is the code in its entirety.

<Tabs>
  <Tab title="Python">
    ```python lines {34,52-77} theme={null}
    from openai import OpenAI
    import weave
    from weave import Model
    import numpy as np
    import json
    import asyncio

    # Examples to use for evaluations
    articles = [
        "Novo Nordisk and Eli Lilly rival soars 32 percent after promising weight loss drug results Shares of Denmarks Zealand Pharma shot 32 percent higher in morning trade, after results showed success in its liver disease treatment survodutide, which is also on trial as a drug to treat obesity. The trial “tells us that the 6mg dose is safe, which is the top dose used in the ongoing [Phase 3] obesity trial too,” one analyst said in a note. The results come amid feverish investor interest in drugs that can be used for weight loss.",
        "Berkshire shares jump after big profit gain as Buffetts conglomerate nears $1 trillion valuation Berkshire Hathaway shares rose on Monday after Warren Buffetts conglomerate posted strong earnings for the fourth quarter over the weekend. Berkshires Class A and B shares jumped more than 1.5%, each. Class A shares are higher by more than 17% this year, while Class B has gained more than 18%. Berkshire was last valued at $930.1 billion, up from $905.5 billion where it closed on Friday, according to FactSet. Berkshire on Saturday posted fourth-quarter operating earnings of $8.481 billion, about 28 percent higher than the $6.625 billion from the year-ago period, driven by big gains in its insurance business. Operating earnings refers to profits from businesses across insurance, railroads and utilities. Meanwhile, Berkshires cash levels also swelled to record levels. The conglomerate held $167.6 billion in cash in the fourth quarter, surpassing the $157.2 billion record the conglomerate held in the prior quarter.",
        "Highmark Health says its combining tech from Google and Epic to give doctors easier access to information Highmark Health announced it is integrating technology from Google Cloud and the health-care software company Epic Systems. The integration aims to make it easier for both payers and providers to access key information they need, even if it's stored across multiple points and formats, the company said. Highmark is the parent company of a health plan with 7 million members, a provider network of 14 hospitals and other entities",
        "Rivian and Lucid shares plunge after weak EV earnings reports Shares of electric vehicle makers Rivian and Lucid fell Thursday after the companies reported stagnant production in their fourth-quarter earnings after the bell Wednesday. Rivian shares sank about 25 percent, and Lucids stock dropped around 17 percent. Rivian forecast it will make 57,000 vehicles in 2024, slightly less than the 57,232 vehicles it produced in 2023. Lucid said it expects to make 9,000 vehicles in 2024, more than the 8,428 vehicles it made in 2023.",
        "Mauritius blocks Norwegian cruise ship over fears of a potential cholera outbreak Local authorities on Sunday denied permission for the Norwegian Dawn ship, which has 2,184 passengers and 1,026 crew on board, to access the Mauritius capital of Port Louis, citing “potential health risks.” The Mauritius Ports Authority said Sunday that samples were taken from at least 15 passengers on board the cruise ship. A spokesperson for the U.S.-headquartered Norwegian Cruise Line Holdings said Sunday that 'a small number of guests experienced mild symptoms of a stomach-related illness' during Norwegian Dawns South Africa voyage.",
        "Intuitive Machines lands on the moon in historic first for a U.S. company Intuitive Machines Nova-C cargo lander, named Odysseus after the mythological Greek hero, is the first U.S. spacecraft to soft land on the lunar surface since 1972. Intuitive Machines is the first company to pull off a moon landing — government agencies have carried out all previously successful missions. The company's stock surged in extended trading Thursday, after falling 11 percent in regular trading.",
        "Lunar landing photos: Intuitive Machines Odysseus sends back first images from the moon Intuitive Machines cargo moon lander Odysseus returned its first images from the surface. Company executives believe the lander caught its landing gear sideways on the surface of the moon while touching down and tipped over. Despite resting on its side, the company's historic IM-1 mission is still operating on the moon.",
    ]

    def docs_to_embeddings(docs: list) -> list:
        openai = OpenAI()
        document_embeddings = []
        for doc in docs:
            response = (
                openai.embeddings.create(input=doc, model="text-embedding-3-small")
                .data[0]
                .embedding
            )
            document_embeddings.append(response)
        return document_embeddings

    article_embeddings = docs_to_embeddings(articles) # Note: you would typically do this once with your articles and put the embeddings & metadata in a database

    # Add a decorator to the retrieval step
    @weave.op()
    def get_most_relevant_document(query):
        openai = OpenAI()
        query_embedding = (
            openai.embeddings.create(input=query, model="text-embedding-3-small")
            .data[0]
            .embedding
        )
        similarities = [
            np.dot(query_embedding, doc_emb)
            / (np.linalg.norm(query_embedding) * np.linalg.norm(doc_emb))
            for doc_emb in article_embeddings
        ]
        # Get the index of the most similar document
        most_relevant_doc_index = np.argmax(similarities)
        return articles[most_relevant_doc_index]

    # Create a Model subclass with details about the app, along with a predict function that produces a response
    class RAGModel(Model):
        system_message: str
        model_name: str = "gpt-3.5-turbo-1106"

        @weave.op()
        def predict(self, question: str) -> dict: # note: `question` will be used later to select data from our evaluation rows
            from openai import OpenAI
            context = get_most_relevant_document(question)
            client = OpenAI()
            query = f"""Use the following information to answer the subsequent question. If the answer cannot be found, write "I don't know."
            Context:
            \"\"\"
            {context}
            \"\"\"
            Question: {question}"""
            response = client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": self.system_message},
                    {"role": "user", "content": query},
                ],
                temperature=0.0,
                response_format={"type": "text"},
            )
            answer = response.choices[0].message.content
            return {'answer': answer, 'context': context}

    # Set your team and project names
    weave.init('<team-name>/rag-quickstart')
    model = RAGModel(
        system_message="You are an expert in finance and answer questions related to finance, financial services, and financial markets. When responding based on provided information, be sure to cite the source."
    )

    # Here is our scoring function uses our question and output to product a score
    @weave.op()
    async def context_precision_score(question, output):
        context_precision_prompt = """Given question, answer and context verify if the context was useful in arriving at the given answer. Give verdict as "1" if useful and "0" if not with json output.
        Output in only valid JSON format.

        question: {question}
        context: {context}
        answer: {answer}
        verdict: """
        client = OpenAI()

        prompt = context_precision_prompt.format(
            question=question,
            context=output['context'],
            answer=output['answer'],
        )

        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[{"role": "user", "content": prompt}],
            response_format={ "type": "json_object" }
        )
        response_message = response.choices[0].message
        response = json.loads(response_message.content)
        return {
            "verdict": int(response["verdict"]) == 1,
        }

    questions = [
        {"question": "What significant result was reported about Zealand Pharma's obesity trial?"},
        {"question": "How much did Berkshire Hathaway's cash levels increase in the fourth quarter?"},
        {"question": "What is the goal of Highmark Health's integration of Google Cloud and Epic Systems technology?"},
        {"question": "What were Rivian and Lucid's vehicle production forecasts for 2024?"},
        {"question": "Why was the Norwegian Dawn cruise ship denied access to Mauritius?"},
        {"question": "Which company achieved the first U.S. moon landing since 1972?"},
        {"question": "What issue did Intuitive Machines' lunar lander encounter upon landing on the moon?"}
    ]

    # Define an Evaluation object and pass example questions along with scoring functions
    evaluation = weave.Evaluation(dataset=questions, scorers=[context_precision_score])
    asyncio.run(evaluation.evaluate(model))
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript lines theme={null}
    require('dotenv').config();
    import { OpenAI } from 'openai';
    import * as weave from 'weave';

    interface Article {
        text: string;
        embedding?: number[];
    }

    const articles: Article[] = [
        { 
            text: `Novo Nordisk and Eli Lilly rival soars 32 percent after promising weight loss drug results Shares of Denmarks Zealand Pharma shot 32 percent higher in morning trade, after results showed success in its liver disease treatment survodutide, which is also on trial as a drug to treat obesity. The trial tells us that the 6mg dose is safe, which is the top dose used in the ongoing [Phase 3] obesity trial too, one analyst said in a note. The results come amid feverish investor interest in drugs that can be used for weight loss.`
        },
        { 
            text: `Berkshire shares jump after big profit gain as Buffetts conglomerate nears $1 trillion valuation Berkshire Hathaway shares rose on Monday after Warren Buffetts conglomerate posted strong earnings for the fourth quarter over the weekend. Berkshires Class A and B shares jumped more than 1.5%, each. Class A shares are higher by more than 17% this year, while Class B has gained more than 18%. Berkshire was last valued at $930.1 billion, up from $905.5 billion where it closed on Friday, according to FactSet. Berkshire on Saturday posted fourth-quarter operating earnings of $8.481 billion, about 28 percent higher than the $6.625 billion from the year-ago period, driven by big gains in its insurance business. Operating earnings refers to profits from businesses across insurance, railroads and utilities. Meanwhile, Berkshires cash levels also swelled to record levels. The conglomerate held $167.6 billion in cash in the fourth quarter, surpassing the $157.2 billion record the conglomerate held in the prior quarter.`
        },
        { 
            text: `Highmark Health says its combining tech from Google and Epic to give doctors easier access to information Highmark Health announced it is integrating technology from Google Cloud and the health-care software company Epic Systems. The integration aims to make it easier for both payers and providers to access key information they need, even if its stored across multiple points and formats, the company said. Highmark is the parent company of a health plan with 7 million members, a provider network of 14 hospitals and other entities`
        }
    ];

    function cosineSimilarity(a: number[], b: number[]): number {
        const dotProduct = a.reduce((sum, val, i) => sum + val * b[i], 0);
        const magnitudeA = Math.sqrt(a.reduce((sum, val) => sum + val * val, 0));
        const magnitudeB = Math.sqrt(b.reduce((sum, val) => sum + val * val, 0));
        return dotProduct / (magnitudeA * magnitudeB);
    }

    const docsToEmbeddings = weave.op(async function(docs: Article[]): Promise<Article[]> {
        const openai = new OpenAI();
        const enrichedDocs = await Promise.all(docs.map(async (doc) => {
            const response = await openai.embeddings.create({
                input: doc.text,
                model: "text-embedding-3-small"
            });
            return {
                ...doc,
                embedding: response.data[0].embedding
            };
        }));
        return enrichedDocs;
    });

    class RAGModel {
        private openai: OpenAI;
        private systemMessage: string;
        private modelName: string;
        private articleEmbeddings: Article[];

        constructor(config: {
            systemMessage: string;
            modelName?: string;
            articleEmbeddings: Article[];
        }) {
            this.openai = new OpenAI();
            this.systemMessage = config.systemMessage;
            this.modelName = config.modelName || "gpt-3.5-turbo-1106";
            this.articleEmbeddings = config.articleEmbeddings;
            this.predict = weave.op(this, this.predict);
        }

        private async getMostRelevantDocument(query: string): Promise<string> {
            const queryEmbedding = await this.openai.embeddings.create({
                input: query,
                model: "text-embedding-3-small"
            });

            const similarities = this.articleEmbeddings.map(doc => {
                if (!doc.embedding) return 0;
                return cosineSimilarity(queryEmbedding.data[0].embedding, doc.embedding);
            });

            const mostRelevantIndex = similarities.indexOf(Math.max(...similarities));
            return this.articleEmbeddings[mostRelevantIndex].text;
        }

        async predict(question: string): Promise<{
            answer: string;
            context: string;
        }> {
            const context = await this.getMostRelevantDocument(question);
            
            const response = await this.openai.chat.completions.create({
                model: this.modelName,
                messages: [
                    { role: "system", content: this.systemMessage },
                    { 
                        role: "user", 
                        content: `Use the following information to answer the subsequent question. If the answer cannot be found, write "I don't know."
                        Context:
                        """
                        ${context}
                        """
                        Question: ${question}`
                    }
                ],
                temperature: 0
            });

            return {
                answer: response.choices[0].message.content || "",
                context
            };
        }
    }

    interface ScorerResult {
        verdict: boolean;
    }

    interface QuestionRow {
        question: string;
    }

    function createQuestionDataset(): weave.Dataset<QuestionRow> {
        return new weave.Dataset<QuestionRow>({
            id: 'rag-questions',
            rows: [
                { question: "What significant result was reported about Zealand Pharma's obesity trial?" },
                { question: "How much did Berkshire Hathaway's cash levels increase in the fourth quarter?" },
                { question: "What is the goal of Highmark Health's integration of Google Cloud and Epic Systems technology?" }
            ]
        });
    }

    const contextPrecisionScore = weave.op(async function(args: {
        datasetRow: QuestionRow;
        modelOutput: { answer: string; context: string; }
    }): Promise<ScorerResult> {
        const openai = new OpenAI();
        
        const prompt = `Given question, answer and context verify if the context was useful in arriving at the given answer. Give verdict as "1" if useful and "0" if not with json output.
        Output in only valid JSON format.

        question: ${args.datasetRow.question}
        context: ${args.modelOutput.context}
        answer: ${args.modelOutput.answer}
        verdict: `;

        const response = await openai.chat.completions.create({
            model: "gpt-4-turbo-preview",
            messages: [{ role: "user", content: prompt }],
            response_format: { type: "json_object" }
        });

        const result = JSON.parse(response.choices[0].message.content || "{}");
        return {
            verdict: parseInt(result.verdict) === 1
        };
    });

    async function main() {
        # Set your team and project names
        await weave.init('<team-name>/rag-quickstart');
        
        const articleEmbeddings = await docsToEmbeddings(articles);
        
        const model = new RAGModel({
            systemMessage: "You are an expert in finance and answer questions related to finance, financial services, and financial markets. When responding based on provided information, be sure to cite the source.",
            articleEmbeddings
        });

        const evaluation = new weave.Evaluation({
            dataset: createQuestionDataset(),
            scorers: [contextPrecisionScore]
        });

        const results = await evaluation.evaluate({
            model: weave.op((args: { datasetRow: QuestionRow }) => 
                model.predict(args.datasetRow.question)
            )
        });
        
        console.log('Evaluation results:', results);
    }

    if (require.main === module) {
        main().catch(console.error);
    }
    ```
  </Tab>
</Tabs>

## Conclusion

This tutorial showed how to build observability into different steps of your applications, like the retrieval step in this example. You also learned how to build more complex scoring functions, like an LLM judge, for automatic evaluation of application responses.

## Next Steps

Check out the [RAG++ course](https://www.wandb.courses/courses/rag-in-production?utm_source=wandb_docs\&utm_medium=code\&utm_campaign=weave_docs) for a more advanced dive into practical RAG techniques for engineers, where you'll learn production-ready solutions from Weights & Biases, Cohere and Weaviate to optimize performance, cut costs, and enhance the accuracy and relevance of your applications.
