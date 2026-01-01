# Source: https://braintrust.dev/docs/cookbook/recipes/SimpleRagas.md

# Optimizing Ragas to evaluate a RAG pipeline

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/SimpleRagas/SimpleRagas.ipynb) by [Ankur Goyal](https://twitter.com/ankrgyl), [Nelson Auner](https://twitter.com/nelsonauner) on 2024-05-27</div>

Ragas is a popular framework for evaluating Retrieval Augmented Generation (RAG) applications. Braintrust natively supports the [Ragas](https://arxiv.org/abs/2309.15217) metrics, with several improvements to aid debugging and accuracy, in our open source [`autoevals`](https://github.com/braintrustdata/autoevals) library.

In this cookbook, we'll walk through using a few Ragas metrics to evaluate a simple RAG pipeline that does Q\&A on [Coda's help desk](https://coda.io/). We'll reuse many of the components we built in a [previous cookbook](https://www.braintrust.dev/docs/cookbook/CodaHelpDesk) on RAG, which
you can check out to learn some of the basics around evaluating RAG systems.

Let's dive in and start by installing dependencies:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
%pip install -U autoevals braintrust openai scipy lancedb markdownify --quiet
```

## Setting up the RAG application

We'll quickly set up a full end-to-end RAG application, based on our earlier [cookbook](https://www.braintrust.dev/docs/cookbook/CodaHelpDesk). We use the Coda Q\&A dataset, LanceDB for our vector database, and OpenAI's embedding model.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import asyncio
import os
import re
import tempfile

import braintrust
import lancedb
import markdownify
import openai
import requests

NUM_SECTIONS = 20
CODA_QA_FILE_LOC = "https://gist.githubusercontent.com/wong-codaio/b8ea0e087f800971ca5ec9eef617273e/raw/39f8bd2ebdecee485021e20f2c1d40fd649a4c77/articles.json"

braintrust.login(
    api_key=os.environ.get("BRAINTRUST_API_KEY", "Your BRAINTRUST_API_KEY here")
)

openai_client = braintrust.wrap_openai(
    openai.AsyncOpenAI(
        base_url="https://api.braintrust.dev/v1/proxy",
        default_headers={"x-bt-use-cache": "always"},
        api_key=os.environ.get("OPENAI_API_KEY", "Your OPENAI_API_KEY here"),
    )
)

coda_qa_content_data = requests.get(CODA_QA_FILE_LOC).json()

markdown_sections = [
    {"doc_id": row["id"], "markdown": section.strip()}
    for row in coda_qa_content_data
    for section in re.split(r"(.*\n=+\n)", markdownify.markdownify(row["body"]))
    if section.strip() and not re.match(r".*\n=+\n", section)
]


LANCE_DB_PATH = os.path.join(tempfile.TemporaryDirectory().name, "docs-lancedb")


@braintrust.traced
async def embed_text(text: str):
    params = dict(input=text, model="text-embedding-3-small")
    response = await openai_client.embeddings.create(**params)
    embedding = response.data[0].embedding
    return embedding


embeddings = await asyncio.gather(
    *(embed_text(section["markdown"]) for section in markdown_sections)
)

db = lancedb.connect(LANCE_DB_PATH)
table = db.create_table(
    "sections",
    data=[
        {
            "doc_id": row["doc_id"],
            "section_id": i,
            "markdown": row["markdown"],
            "vector": embedding,
        }
        for i, (row, embedding) in enumerate(
            zip(markdown_sections[:NUM_SECTIONS], embeddings)
        )
    ],
)

table.count_rows()
```

```
/Users/ankur/projects/braintrust/cookbook/content/examples/SimpleRagas/.venv/lib/python3.12/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html
  from .autonotebook import tqdm as notebook_tqdm
```

```
20
```

Done! Next, we'll write some simple, framework-free code to (a) retrieve relevant documents and (b) generate an answer given those documents.

### Retrieving documents

To perform retrieval, we'll use the same embedding model as we did for the document sections to embed the `input` query, and then search for the
`TOP_K` (2) most relevant documents.

You'll notice that here and elsewhere we've decorated functions with `@braintrust.traced`. For now, it's a no-op, but we'll see shortly how `@braintrust.traced`
helps us trace python functions and debug them in Braintrust.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from textwrap import dedent
from typing import Iterable, List

QA_ANSWER_MODEL = "gpt-3.5-turbo"
TOP_K = 2


@braintrust.traced
async def fetch_top_k_relevant_sections(input: str) -> List[str]:
    embedding = await embed_text(input)
    results = table.search(embedding).limit(TOP_K).to_arrow().to_pylist()
    return [result["markdown"] for result in results]
```

Let's try it out on a simple question, and take a look at the retrieved documents:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
question = (
    "What impact does starring a document have on other workspace members in Coda?"
)

relevant_sections = await fetch_top_k_relevant_sections(question)

for section in relevant_sections:
    print("----")
    print(section)
    print("\n")
```

```
----
Not all Coda docs are used in the same way. You'll inevitably have a few that you use every week, and some that you'll only use once. This is where starred docs can help you stay organized.



Starring docs is a great way to mark docs of personal importance. After you star a doc, it will live in a section on your doc list called **[My Shortcuts](https://coda.io/shortcuts)**. All starred docs, even from multiple different workspaces, will live in this section.



Starring docs only saves them to your personal My Shortcuts. It doesn’t affect the view for others in your workspace. If you’re wanting to shortcut docs not just for yourself but also for others in your team or workspace, you’ll [use pinning](https://help.coda.io/en/articles/2865511-starred-pinned-docs) instead.
```

### Generating the final answer

To generate the final answer, we can simply pass in the retrieved documents and the original question to a simple prompt defined below. Feel free to tweak this prompt as you experiment!

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
@braintrust.traced
async def generate_answer_from_docs(question: str, relevant_sections: Iterable[str]):
    context = "\n\n".join(relevant_sections)
    completion = await openai_client.chat.completions.create(
        model=QA_ANSWER_MODEL,
        messages=[
            {
                "role": "user",
                "content": dedent(
                    f"""\
            Given the following context
            {context}
            Please answer the following question:
            Question: {question}
            """
                ),
            }
        ],
    )
    return completion.choices[0].message.content
```

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
answer = await generate_answer_from_docs(question, relevant_sections)

print(answer)
```

```
Starring a document in Coda only affects the individual who starred it. It does not impact other workspace members as the starred document will only appear in the individual's personal My Shortcuts section. It is a way to mark documents of personal importance for easy access.
```

### Combining retrieval and generation

We'll define a convenience function to combine these two steps, and return both the final answer and the retrieved documents so we can observe if we picked useful documents! (Later, returning documents will come in useful for evaluations)

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
@braintrust.traced
async def generate_answer_e2e(question: str):
    retrieved_content = await fetch_top_k_relevant_sections(question)
    answer = await generate_answer_from_docs(question, retrieved_content)
    return dict(answer=answer, retrieved_docs=retrieved_content)


e2e_answer = await generate_answer_e2e(question)
print(e2e_answer["answer"])
```

```
Starring a document in Coda only affects the individual who starred it. It does not impact other workspace members as the starred document will only appear in the individual's personal My Shortcuts section. It is a way to mark documents of personal importance for easy access.
```

Perfect! Now that we have the whole system working, we can compute Ragas metrics and try a couple improvements.

## Baseline Ragas metrics with autoevals

To get a large enough sample size for evaluations, we're going to use the synthetic test questions we generated in [our earlier cookbook](https://www.braintrust.dev/docs/cookbook/CodaHelpDesk). Feel free to check out that cookbook for details on how the synthetic data generation process works.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import json

CODA_QA_PAIRS_LOC = "https://gist.githubusercontent.com/nelsonauner/2ef4d38948b78a9ec2cff4aa265cff3f/raw/c47306b4469c68e8e495f4dc050f05aff9f997e1/qa_pairs_coda_data.jsonl"


coda_qa_pairs = requests.get(CODA_QA_PAIRS_LOC)
qa_pairs = [json.loads(line) for line in coda_qa_pairs.text.split("\n") if line]
qa_pairs[0]
```

```
{'input': 'What is the purpose of starred docs in Coda?',
 'expected': 'Starring docs in Coda helps to mark documents of personal importance and organizes them in a specific section called My Shortcuts for easy access.',
 'metadata': {'document_id': '8179780',
  'section_id': 0,
  'question_idx': 0,
  'answer_idx': 0,
  'id': 0,
  'split': 'train'}}
```

Ragas provides a [variety of metrics](https://docs.ragas.io/en/stable/concepts/metrics/index.html), but for the purposes of this guide, we'll show you how to calculate two scores we've found to be useful:

* `ContextRecall` compares the retrieved context to the information in the ground truth answer. This is a helpful way of testing how relevant the retrieved documents are with respect to the answer itself.
* `AnswerCorrectness` evaluates the generated answer to the golden answer. Under the hood, it checks each statement in the answer and classifies it as a true positive, false positive, or false negative.

Before we calculate metrics, we'll write a short wrapper class that splits the returned output and context into two arguments that our Ragas evaluator classes can easily ingest.

And now we can run our evaluation!

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from braintrust import EvalAsync

from autoevals import AnswerCorrectness, ContextRecall


# Wrap ContextRecall() to propagate along the "answer" and "context" values separately
async def context_recall(output, **kwargs):
    return await ContextRecall().eval_async(
        output=output["answer"], context=output["retrieved_docs"], **kwargs
    )


async def answer_correctness(output, **kwargs):
    return await AnswerCorrectness().eval_async(output=output["answer"], **kwargs)


eval_result = await EvalAsync(
    name="Rag Metrics with Ragas",
    experiment_name=f"RAG {QA_ANSWER_MODEL}",
    data=qa_pairs[:NUM_SECTIONS],
    task=generate_answer_e2e,
    scores=[context_recall, answer_correctness],
    metadata=dict(model=QA_ANSWER_MODEL, topk=TOP_K),
)
```

```
Experiment RAG gpt-3.5-turbo is running at https://www.braintrust.dev/app/braintrustdata.com/p/Rag%20Metrics%20with%20Ragas/experiments/RAG%20gpt-3.5-turbo
Rag Metrics with Ragas [experiment_name=RAG gpt-3.5-turbo] (data): 20it [00:00, 51941.85it/s]
Rag Metrics with Ragas [experiment_name=RAG gpt-3.5-turbo] (tasks): 100%|██████████| 20/20 [00:01<00:00, 10.48it/s]
```

```

=========================SUMMARY=========================
95.00% 'ContextRecall'     score
67.28% 'AnswerCorrectness' score

1.58s duration

See results for RAG gpt-3.5-turbo at https://www.braintrust.dev/app/braintrustdata.com/p/Rag%20Metrics%20with%20Ragas/experiments/RAG%20gpt-3.5-turbo
```

Not bad! It looks like we're doing really well on context recall, but worse on the final answer's correctness.

### Interpreting the results in Braintrust

Although Ragas is very powerful, it can be difficult to get detailed insight into low scoring values. Braintrust makes that very simple.

Sometimes an average of 67% means that 2/3 of the values had a score of 1 and 1/3 had a score of 0. However, the distribution chart makes it clear
that in our case, many of the scores are partially correct:

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/distribution_chart.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=40dd7a094a2d5cd04595c0ec8ac5e4c5" alt="distribution chart" data-og-width="1125" width="1125" data-og-height="178" height="178" data-path="cookbook/assets/SimpleRagas/distribution_chart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/distribution_chart.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=4b652ff5514e3b3b671dcec9c0a18b38 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/distribution_chart.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=01d8382249ea63ed027ef2d9b83ac002 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/distribution_chart.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=d0a2688b334e380dcb99004200c587a6 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/distribution_chart.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=cf858ce3f40cb77282ff9945563a4535 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/distribution_chart.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=4a52537263eb9994da8239fa9c476bd7 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/distribution_chart.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=b171bd20f373d7288300d0e1be3a39a7 2500w" />

Now, let's dig into one of these records. Braintrust allows us to see all the raw outputs from the constituent pieces:

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/constituent_pieces.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=acbeff056644d1f2d9fc81c9d0f2c1c8" alt="constituent pieces" data-og-width="733" width="733" data-og-height="358" height="358" data-path="cookbook/assets/SimpleRagas/constituent_pieces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/constituent_pieces.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=c822153c36b60c1854f835d988425183 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/constituent_pieces.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=c35a0dd6f8e4bbbbf03b4aa9b4de66e2 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/constituent_pieces.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=32f29607eaf58b45292c371faf2ed9c3 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/constituent_pieces.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=03c21e3798837f0ee6a3d101a760c81c 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/constituent_pieces.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=f0018018e9c1de4b685a3c3bb6a5d82e 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/constituent_pieces.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=5efcf13e0aea25514b0f756dc57d2a14 2500w" />

To me, this looks like it might be an error in the scoring function itself. `No, starring a doc in Coda does not affect other users` seems like a true, not false, positive.
Let's try changing the scoring model for `AnswerCorrectness` to be `gpt-4`, and see if that changes anything.

### Swapping grading model

By default, Ragas is configured to use `gpt-3.5-turbo-16k`. As we observed, it looks like the `AnswerCorrectness` score may be returning bogus
results, and maybe we should try using `gpt-4` instead. Braintrust lets us test the effect of this quickly, directly in the UI, before we run
a full experiment:

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/try-gpt-4.gif?s=5bb279fbbff69ee227abc78c263c4e57" alt="try gpt-4" data-og-width="1141" width="1141" data-og-height="697" height="697" data-path="cookbook/assets/SimpleRagas/try-gpt-4.gif" data-optimize="true" data-opv="3" />

Looks better. Let's update our scoring function to use it and re-run the experiment.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
# Wrap ContextRecall() to propagate along the "answer" and "context" values separately
async def context_recall(output, **kwargs):
    return await ContextRecall().eval_async(
        output=output["answer"], context=output["retrieved_docs"], **kwargs
    )


async def answer_correctness(output, **kwargs):
    return await AnswerCorrectness(model="gpt-4").eval_async(
        output=output["answer"], **kwargs
    )


eval_result = await EvalAsync(
    name="Rag Metrics with Ragas",
    experiment_name=f"Score with gpt-4",
    data=qa_pairs[:NUM_SECTIONS],
    task=generate_answer_e2e,
    scores=[context_recall, answer_correctness],
    metadata=dict(model=QA_ANSWER_MODEL, topk=TOP_K),
)
```

```
Experiment Score with gpt-4 is running at https://www.braintrust.dev/app/braintrustdata.com/p/Rag%20Metrics%20with%20Ragas/experiments/Score%20with%20gpt-4
Rag Metrics with Ragas [experiment_name=Score with gpt-4] (data): 20it [00:00, 19864.10it/s]
Rag Metrics with Ragas [experiment_name=Score with gpt-4] (tasks): 100%|██████████| 20/20 [00:07<00:00,  2.71it/s]
```

```

=========================SUMMARY=========================
Score with gpt-4 compared to RAG gpt-3.5-turbo:
72.10% (+04.83%) 'AnswerCorrectness' score	(10 improvements, 4 regressions)
95.00% (-) 'ContextRecall'     score	(0 improvements, 0 regressions)

4.67s (+309.08%) 'duration'	(0 improvements, 20 regressions)

See results for Score with gpt-4 at https://www.braintrust.dev/app/braintrustdata.com/p/Rag%20Metrics%20with%20Ragas/experiments/Score%20with%20gpt-4
```

Great, it looks like changing our grading model improved the answer correctness score for the same set of questions:

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/score_progression.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=6ff12991b59e01c7539dc69394a7c9ca" alt="score progression" data-og-width="2174" width="2174" data-og-height="668" height="668" data-path="cookbook/assets/SimpleRagas/score_progression.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/score_progression.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=635f0ebbb930a8a9503d1c77ef56264f 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/score_progression.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=fe53b6d4957149fdf87fd64724eb8f30 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/score_progression.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=e850de499c9571d007e7c23dd4cc0920 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/score_progression.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=efd5ac9e58346b835aba1c94df52d76a 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/score_progression.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=189625db8f8b673f43d328cb48f1542e 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/score_progression.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=b7b806eb647f8477cb786c21c8ff5e4a 2500w" />

### Optimizing document retrieval

Now, let's see if we can further optimize our RAG pipeline without regressing scores. We're going to try pulling just one document, rather than two.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
TOP_K = 1

eval_result = await EvalAsync(
    name="Rag Metrics with Ragas",
    experiment_name=f"TOP_K={TOP_K}",
    data=qa_pairs[:NUM_SECTIONS],
    task=generate_answer_e2e,
    scores=[context_recall, answer_correctness],
    metadata=dict(model=QA_ANSWER_MODEL, topk=TOP_K),
)
```

```
Experiment TOP_K=1 is running at https://www.braintrust.dev/app/braintrustdata.com/p/Rag%20Metrics%20with%20Ragas/experiments/TOP_K%3D1
Rag Metrics with Ragas [experiment_name=TOP_K=1] (data): 20it [00:00, 99039.06it/s]
Rag Metrics with Ragas [experiment_name=TOP_K=1] (tasks): 100%|██████████| 20/20 [00:01<00:00, 11.07it/s]
```

```

=========================SUMMARY=========================
TOP_K=1 compared to Score with gpt-4:
97.29% (+02.29%) 'ContextRecall'     score	(1 improvements, 3 regressions)
71.99% (-00.12%) 'AnswerCorrectness' score	(9 improvements, 11 regressions)

1.56s (-311.18%) 'duration'	(20 improvements, 0 regressions)

See results for TOP_K=1 at https://www.braintrust.dev/app/braintrustdata.com/p/Rag%20Metrics%20with%20Ragas/experiments/TOP_K%3D1
```

Although not a pure fail, it does seem like in 3 cases we're not retrieving the right documents anymore, and 11 cases had worse results.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/topk1.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=7f617d4e9523ff7d93b4550be1cde6b4" alt="topk1" data-og-width="910" width="910" data-og-height="210" height="210" data-path="cookbook/assets/SimpleRagas/topk1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/topk1.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=dfcac647b92445aa6edf13504c71b3e4 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/topk1.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=360d8a08671f02b23636e867028b0b27 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/topk1.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=6ec83ef156d4db893dbb4d020f2520f0 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/topk1.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=336ec3e55e38543e90207f96a557b6a2 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/topk1.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=ffd4022b31cfb63306b6336f3b7015b7 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/topk1.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=522669a0ef33f1fb0de9837e6834c58c 2500w" />

We can drill down on individual examples of each regression type to better understand it. The side-by-side diffs built into Braintrust make
it easy to deeply understand every step of the pipeline, for example, which documents were missing, and why.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SimpleRagas/missing-docs.gif?s=9c7def7a1708ba7cef51179c884251a8" alt="missing docs" data-og-width="1141" width="1141" data-og-height="697" height="697" data-path="cookbook/assets/SimpleRagas/missing-docs.gif" data-optimize="true" data-opv="3" />

And there you have it! Ragas is a powerful technique, that with the right tools and iteration can lead to really high quality RAG applications. Happy evaling!


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt