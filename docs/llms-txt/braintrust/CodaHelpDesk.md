# Source: https://braintrust.dev/docs/cookbook/recipes/CodaHelpDesk.md

# Coda's Help Desk with and without RAG

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/CodaHelpDesk/CodaHelpDesk.ipynb) by [Austin Moehle](https://www.linkedin.com/in/austinmxx/), [Kenny Wong](https://twitter.com/siuheihk) on 2023-12-21</div>

Large language models have gotten extremely good at answering general questions but often struggle with specific domain knowledge. When building AI-powered help desks or knowledge bases, this limitation becomes apparent. Retrieval-augmented generation (RAG) addresses this challenge by incorporating relevant information from external documents into the model's context.

In this cookbook, we'll build and evaluate an AI application that answers questions about [Coda's Help Desk](https://help.coda.io/en/) documentation. Using Braintrust, we'll compare baseline and RAG-enhanced responses against expected answers to quantitatively measure the improvement.

## Getting started

To follow along, start by installing the required packages:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
pip install autoevals braintrust requests openai lancedb markdownify asyncio pyarrow
```

Next, make sure you have a [Braintrust](https://www.braintrust.dev/signup) account, along with an [OpenAI API key](https://platform.openai.com/). To authenticate with Braintrust, export your `BRAINTRUST_API_KEY` as an environment variable:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
export BRAINTRUST_API_KEY="YOUR_API_KEY_HERE"
```

<Callout type="info">
  Exporting your API key is a best practice, but to make it easier to follow along with this cookbook, you can also hardcode it into the code below.
</Callout>

We'll import our modules and define constants:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import os
import re
import json
import tempfile
from typing import List

import autoevals
import braintrust
import markdownify
import lancedb
import openai
import requests
import asyncio
from pydantic import BaseModel, Field


# Model selection constants
QA_GEN_MODEL = "gpt-4o-mini"
QA_ANSWER_MODEL = "gpt-4o-mini"
QA_GRADING_MODEL = "gpt-4o-mini"
RELEVANCE_MODEL = "gpt-4o-mini"

# Data constants
NUM_SECTIONS = 20
NUM_QA_PAIRS = 20  # Increase this number to test at a larger scale
TOP_K = 2  # Number of relevant sections to retrieve

# Uncomment the following line to hardcode your API key
# os.environ["BRAINTRUST_API_KEY"] = "YOUR_API_KEY_HERE"
```

## Download Markdown docs from Coda's Help Desk

Let's start by downloading the Coda docs and splitting them into their constituent Markdown sections.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
data = requests.get(
    "https://gist.githubusercontent.com/wong-codaio/b8ea0e087f800971ca5ec9eef617273e/raw/39f8bd2ebdecee485021e20f2c1d40fd649a4c77/articles.json"
).json()

markdown_docs = [
    {"id": row["id"], "markdown": markdownify.markdownify(row["body"])} for row in data
]

i = 0
markdown_sections = []
for markdown_doc in markdown_docs:
    sections = re.split(r"(.*\n=+\n)", markdown_doc["markdown"])
    current_section = ""
    for section in sections:
        if not section.strip():
            continue

        if re.match(r".*\n=+\n", section):
            current_section = section
        else:
            section = current_section + section
            markdown_sections.append(
                {
                    "doc_id": markdown_doc["id"],
                    "section_id": i,
                    "markdown": section.strip(),
                }
            )
            current_section = ""
            i += 1

print(f"Downloaded {len(markdown_sections)} Markdown sections. Here are the first 3:")
for i, section in enumerate(markdown_sections[:3]):
    print(f"\nSection {i+1}:\n{section}")
```

```
Downloaded 996 Markdown sections. Here are the first 3:

Section 1:
{'doc_id': '8179780', 'section_id': 0, 'markdown': "Not all Coda docs are used in the same way. You'll inevitably have a few that you use every week, and some that you'll only use once. This is where starred docs can help you stay organized.\n\nStarring docs is a great way to mark docs of personal importance. After you star a doc, it will live in a section on your doc list called **[My Shortcuts](https://coda.io/shortcuts)**. All starred docs, even from multiple different workspaces, will live in this section.\n\nStarring docs only saves them to your personal My Shortcuts. It doesn’t affect the view for others in your workspace. If you’re wanting to shortcut docs not just for yourself but also for others in your team or workspace, you’ll [use pinning](https://help.coda.io/en/articles/2865511-starred-pinned-docs) instead."}

Section 2:
{'doc_id': '8179780', 'section_id': 1, 'markdown': '**Star your docs**\n==================\n\nTo star a doc, hover over its name in the doc list and click the star icon. Alternatively, you can star a doc from within the doc itself. Hover over the doc title in the upper left corner, and click on the star.\n\nOnce you star a doc, you can access it quickly from the [My Shortcuts](https://coda.io/shortcuts) tab of your doc list.\n\n![](https://downloads.intercomcdn.com/i/o/793964361/55a80927217f85d68d44a3c3/Star+doc+to+my+shortcuts.gif)\n\nAnd, as your doc needs change, simply click the star again to un-star the doc and remove it from **My Shortcuts**.'}

Section 3:
{'doc_id': '8179780', 'section_id': 2, 'markdown': '**FAQs**\n========\n\nWhen should I star a doc and when should I pin it?\n--------------------------------------------------\n\nStarring docs is best for docs of *personal* importance. Starred docs appear in your **My Shortcuts**, but they aren’t starred for anyone else in your workspace. For instance, you may want to star your personal to-do list doc or any docs you use on a daily basis.\n\n[Pinning](https://help.coda.io/en/articles/2865511-starred-pinned-docs) is recommended when you want to flag or shortcut a doc for *everyone* in your workspace or folder. For instance, you likely want to pin your company wiki doc to your workspace. And you may want to pin your team task tracker doc to your team’s folder.\n\nCan I star docs for everyone?\n-----------------------------\n\nStarring docs only applies to your own view and your own My Shortcuts. To pin docs (or templates) to your workspace or folder, [refer to this article](https://help.coda.io/en/articles/2865511-starred-pinned-docs).\n\n---'}
```

## Use the Braintrust AI Proxy

Let's initialize the OpenAI client using the [Braintrust proxy](/guides/proxy). The Braintrust AI Proxy provides a single API to access OpenAI and other models. Because the proxy automatically caches and reuses results (when `temperature=0` or the `seed` parameter is set), we can re-evaluate prompts many times without incurring additional API costs.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
client = braintrust.wrap_openai(
    openai.AsyncOpenAI(
        api_key=os.environ.get("BRAINTRUST_API_KEY"),
        base_url="https://api.braintrust.dev/v1/proxy",
        default_headers={"x-bt-use-cache": "always"},
    )
)
```

## Generate question-answer pairs

Before we start evaluating some prompts, let's use the LLM to generate a bunch of question-answer pairs from the text at hand. We'll use these QA pairs as ground truth when grading our models later.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
class QAPair(BaseModel):
    questions: List[str] = Field(
        ...,
        description="List of questions, all with the same meaning but worded differently",
    )
    answer: str = Field(..., description="Answer")


class QAPairs(BaseModel):
    pairs: List[QAPair] = Field(..., description="List of question/answer pairs")


async def produce_candidate_questions(row):
    response = await client.chat.completions.create(
        model=QA_GEN_MODEL,
        messages=[
            {
                "role": "user",
                "content": f"""\
Please generate 8 question/answer pairs from the following text. For each question, suggest
2 different ways of phrasing the question, and provide a unique answer.

Content:

{row['markdown']}
""",
            }
        ],
        functions=[
            {
                "name": "propose_qa_pairs",
                "description": "Propose some question/answer pairs for a given document",
                "parameters": QAPairs.model_json_schema(),
            }
        ],
    )

    pairs = QAPairs(**json.loads(response.choices[0].message.function_call.arguments))
    return pairs.pairs


# Create tasks for all API calls
all_candidates_tasks = [
    asyncio.create_task(produce_candidate_questions(a))
    for a in markdown_sections[:NUM_SECTIONS]
]


all_candidates = [await f for f in all_candidates_tasks]

data = []
row_id = 0
for row, doc_qa in zip(markdown_sections[:NUM_SECTIONS], all_candidates):
    for i, qa in enumerate(doc_qa):
        for j, q in enumerate(qa.questions):
            data.append(
                {
                    "input": q,
                    "expected": qa.answer,
                    "metadata": {
                        "document_id": row["doc_id"],
                        "section_id": row["section_id"],
                        "question_idx": i,
                        "answer_idx": j,
                        "id": row_id,
                        "split": (
                            "test" if j == len(qa.questions) - 1 and j > 0 else "train"
                        ),
                    },
                }
            )
            row_id += 1

print(f"Generated {len(data)} QA pairs. Here are the first 10:")
for x in data[:10]:
    print(x)
```

```
Generated 320 QA pairs. Here are the first 10:
{'input': 'What is the purpose of starring a doc in Coda?', 'expected': 'Starring a doc in Coda helps you mark documents of personal importance, making it easier to organize and access them quickly.', 'metadata': {'document_id': '8179780', 'section_id': 0, 'question_idx': 0, 'answer_idx': 0, 'id': 0, 'split': 'train'}}
{'input': 'Why would someone want to star a document in Coda?', 'expected': 'Starring a doc in Coda helps you mark documents of personal importance, making it easier to organize and access them quickly.', 'metadata': {'document_id': '8179780', 'section_id': 0, 'question_idx': 0, 'answer_idx': 1, 'id': 1, 'split': 'test'}}
{'input': 'Where do starred docs appear in Coda?', 'expected': 'Starred docs appear in a section called My Shortcuts on your doc list, allowing for quick access.', 'metadata': {'document_id': '8179780', 'section_id': 0, 'question_idx': 1, 'answer_idx': 0, 'id': 2, 'split': 'train'}}
{'input': 'After starring a document in Coda, where can I find it?', 'expected': 'Starred docs appear in a section called My Shortcuts on your doc list, allowing for quick access.', 'metadata': {'document_id': '8179780', 'section_id': 0, 'question_idx': 1, 'answer_idx': 1, 'id': 3, 'split': 'test'}}
{'input': 'Does starring a doc affect other users in the workspace?', 'expected': 'No, starring a doc only saves it to your personal My Shortcuts and does not affect the view for others in your workspace.', 'metadata': {'document_id': '8179780', 'section_id': 0, 'question_idx': 2, 'answer_idx': 0, 'id': 4, 'split': 'train'}}
{'input': 'Will my colleagues see the docs I star in Coda?', 'expected': 'No, starring a doc only saves it to your personal My Shortcuts and does not affect the view for others in your workspace.', 'metadata': {'document_id': '8179780', 'section_id': 0, 'question_idx': 2, 'answer_idx': 1, 'id': 5, 'split': 'test'}}
{'input': 'What should I use if I want to share a shortcut to a doc with my team?', 'expected': 'To create a shortcut for a document that your team can access, you should use the pinning feature instead of starring.', 'metadata': {'document_id': '8179780', 'section_id': 0, 'question_idx': 3, 'answer_idx': 0, 'id': 6, 'split': 'train'}}
{'input': 'How can I create a shortcut for a document that everyone in my workspace can access?', 'expected': 'To create a shortcut for a document that your team can access, you should use the pinning feature instead of starring.', 'metadata': {'document_id': '8179780', 'section_id': 0, 'question_idx': 3, 'answer_idx': 1, 'id': 7, 'split': 'test'}}
{'input': 'Can starred documents come from different workspaces in Coda?', 'expected': 'Yes, all starred docs, even from multiple different workspaces, will live in the My Shortcuts section.', 'metadata': {'document_id': '8179780', 'section_id': 0, 'question_idx': 4, 'answer_idx': 0, 'id': 8, 'split': 'train'}}
{'input': 'Is it possible to star docs from multiple workspaces?', 'expected': 'Yes, all starred docs, even from multiple different workspaces, will live in the My Shortcuts section.', 'metadata': {'document_id': '8179780', 'section_id': 0, 'question_idx': 4, 'answer_idx': 1, 'id': 9, 'split': 'test'}}
```

## Evaluate a context-free prompt (no RAG)

Let's evaluate a simple prompt that poses each question without providing context from the Markdown docs. We'll evaluate this naive approach using the [Factuality prompt](https://github.com/braintrustdata/autoevals/blob/main/templates/factuality.yaml) from the Braintrust [autoevals](/reference/autoevals) library.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
async def simple_qa(input):
    completion = await client.chat.completions.create(
        model=QA_ANSWER_MODEL,
        messages=[
            {
                "role": "user",
                "content": f"""\
Please answer the following question:

Question: {input}
""",
            }
        ],
    )
    return completion.choices[0].message.content


await braintrust.Eval(
    name="Coda Help Desk Cookbook",
    experiment_name="No RAG",
    data=data[:NUM_QA_PAIRS],
    task=simple_qa,
    scores=[autoevals.Factuality(model=QA_GRADING_MODEL)],
)
```

### Analyze the evaluation in the UI

The cell above will print a link to a Braintrust experiment. Pause and navigate to the UI to view our baseline eval.

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/CodaHelpDesk/inspect.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=3be22ef4b2b343313c45910de7464e1a" alt="Baseline eval" data-og-width="3360" width="3360" data-og-height="1940" height="1940" data-path="cookbook/assets/CodaHelpDesk/inspect.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/CodaHelpDesk/inspect.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=b21f1f8b14f1796154810169ec451070 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/CodaHelpDesk/inspect.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=922b46848d2b162e68691c2d6f698767 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/CodaHelpDesk/inspect.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=f264cc8dff566076ca09a45d10ba5cc4 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/CodaHelpDesk/inspect.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=fced2c38b6d4ae18bea71231d3f5029a 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/CodaHelpDesk/inspect.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=49884dd68ea2e213c1c727737ac4a611 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/CodaHelpDesk/inspect.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=88894b5dce612d228b71b8db2a78140a 2500w" />

## Try using RAG to improve performance

Let's see if RAG (retrieval-augmented generation) can improve our results on this task.

First, we'll compute embeddings for each Markdown section using `text-embedding-ada-002` and create an index over the embeddings in [LanceDB](https://lancedb.com), a vector database. Then, for any given query, we can convert it to an embedding and efficiently find the most relevant context by searching in embedding space. We'll then provide the corresponding text as additional context in our prompt.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
tempdir = tempfile.TemporaryDirectory()
LANCE_DB_PATH = os.path.join(tempdir.name, "docs-lancedb")


@braintrust.traced
async def embed_text(text):
    params = dict(input=text, model="text-embedding-ada-002")
    response = await client.embeddings.create(**params)
    embedding = response.data[0].embedding

    braintrust.current_span().log(
        metrics={
            "tokens": response.usage.total_tokens,
            "prompt_tokens": response.usage.prompt_tokens,
        },
        metadata={"model": response.model},
        input=text,
        output=embedding,
    )

    return embedding


embedding_tasks = [
    asyncio.create_task(embed_text(row["markdown"]))
    for row in markdown_sections[:NUM_SECTIONS]
]
embeddings = [await f for f in embedding_tasks]

db = lancedb.connect(LANCE_DB_PATH)

try:
    db.drop_table("sections")
except:
    pass

# Convert the data to a pandas DataFrame first
import pandas as pd

table_data = [
    {
        "doc_id": row["doc_id"],
        "section_id": row["section_id"],
        "text": row["markdown"],
        "vector": embedding,
    }
    for (row, embedding) in zip(markdown_sections[:NUM_SECTIONS], embeddings)
]

# Create table using the DataFrame approach
table = db.create_table("sections", data=pd.DataFrame(table_data))
```

## Use AI to judge relevance of retrieved documents

Let's retrieve a few *more* of the best-matching candidates from the vector database than we intend to use, then use the model from `RELEVANCE_MODEL` to score the relevance of each candidate to the input query. We'll use the `TOP_K` blurbs by relevance score in our QA prompt. Doing this should be a little more intelligent than just using the closest embeddings.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
@braintrust.traced
async def relevance_score(query, document):
    response = await client.chat.completions.create(
        model=RELEVANCE_MODEL,
        messages=[
            {
                "role": "user",
                "content": f"""\
Consider the following query and a document

Query:
{query}

Document:
{document}


Please score the relevance of the document to a query, on a scale of 0 to 1.
""",
            }
        ],
        functions=[
            {
                "name": "has_relevance",
                "description": "Declare the relevance of a document to a query",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "score": {"type": "number"},
                    },
                },
            }
        ],
    )

    arguments = response.choices[0].message.function_call.arguments
    result = json.loads(arguments)

    braintrust.current_span().log(
        input={"query": query, "document": document},
        output=result,
    )

    return result["score"]


async def retrieval_qa(input):
    embedding = await embed_text(input)

    with braintrust.current_span().start_span(
        name="vector search", input=input
    ) as span:
        result = table.search(embedding).limit(TOP_K + 3).to_arrow().to_pylist()
        docs = [markdown_sections[i["section_id"]]["markdown"] for i in result]

        relevance_scores = []
        for doc in docs:
            relevance_scores.append(await relevance_score(input, doc))

        span.log(
            output=[
                {
                    "doc": markdown_sections[r["section_id"]]["markdown"],
                    "distance": r["_distance"],
                }
                for r in result
            ],
            metadata={"top_k": TOP_K, "retrieval": result},
            scores={
                "avg_relevance": sum(relevance_scores) / len(relevance_scores),
                "min_relevance": min(relevance_scores),
                "max_relevance": max(relevance_scores),
            },
        )

    context = "\n------\n".join(docs[:TOP_K])
    completion = await client.chat.completions.create(
        model=QA_ANSWER_MODEL,
        messages=[
            {
                "role": "user",
                "content": f"""\
Given the following context

{context}

Please answer the following question:

Question: {input}
""",
            }
        ],
    )

    return completion.choices[0].message.content
```

## Run the RAG evaluation

Now let's run our evaluation with RAG:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
await braintrust.Eval(
    name="Coda Help Desk Cookbook",
    experiment_name=f"RAG TopK={TOP_K}",
    data=data[:NUM_QA_PAIRS],
    task=retrieval_qa,
    scores=[autoevals.Factuality(model=QA_GRADING_MODEL)],
)
```

### Analyzing the results

<img src="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/CodaHelpDesk/rag.png?fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=7a38e893aa2baeaf205d10504fb36015" alt="Experiment RAG" data-og-width="3364" width="3364" data-og-height="1944" height="1944" data-path="cookbook/assets/CodaHelpDesk/rag.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/CodaHelpDesk/rag.png?w=280&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=85f8ea2e8b7c17c4a9f5250d561472cc 280w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/CodaHelpDesk/rag.png?w=560&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=f65c84637707f1d6a497568675ff2931 560w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/CodaHelpDesk/rag.png?w=840&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=87bfd5017c65442a45a81bc9aafda91f 840w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/CodaHelpDesk/rag.png?w=1100&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=6d03acb4817a320517165dfaa27bef02 1100w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/CodaHelpDesk/rag.png?w=1650&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=0391d0867ea021ccbdb45bb47773c4e9 1650w, https://mintcdn.com/braintrust/miepTDmD0QMRaWQF/cookbook/assets/CodaHelpDesk/rag.png?w=2500&fit=max&auto=format&n=miepTDmD0QMRaWQF&q=85&s=65e9e0093f7447185493b9c8458f1abd 2500w" />

Select the new experiment to analyze the results. You should notice several things:

* Braintrust automatically compares the new experiment to your previous one
* You should see an increase in scores with RAG
* You can explore individual examples to see exactly which responses improved

Try adjusting the constants set at the beginning of this tutorial, such as `NUM_QA_PAIRS`, to run your evaluation on a larger dataset and gain more confidence in your findings.

## Next steps

* Learn about [using functions to build a RAG agent](/cookbook/recipes/ToolRAG).
* Compare your [evals across different models](/cookbook/recipes/ModelComparison).
* If RAG is just one part of your agent, learn how to [evaluate a prompt chaining agent](/cookbook/recipes/PromptChaining).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt