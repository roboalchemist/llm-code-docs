# Source: https://braintrust.dev/docs/cookbook/recipes/Text2SQL.md

# Text-to-SQL

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/Text2SQL/Text2SQL.ipynb) by [Ankur Goyal](https://twitter.com/ankrgyl) on 2023-08-12</div>

This tutorial will teach you how to create an application that converts natural language questions into SQL queries, and then evaluating how well
the queries work. We'll even make an improvement to the prompts, and evaluate the impact! By the time you finish this tutorial, you should be ready
to run your own experiments.

Before starting, please make sure that you have a Braintrust account. If you do not, please [sign up](https://braintrust.dev).

## Setting up the environment

The next few commands will install some libraries and include some helper code for the text2sql application. Feel free to copy/paste/tweak/reuse this code in your own tools.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
!pip install braintrust duckdb datasets openai pyarrow python-Levenshtein autoevals
```

We're going to use a public dataset called [WikiSQL](https://github.com/salesforce/WikiSQL) that contains natural language questions and their corresponding SQL queries.

## Exploring the data

In this section, we'll take a look at the dataset and ground truth text/sql pairs to better understand the problem and data.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from datasets import load_dataset

data = list(load_dataset("wikisql")["test"])
```

Here's an example question:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
idx = 1
data[idx]["question"]
```

```
'What club was in toronto 1995-96'
```

We'll use Arrow and DuckDB to help us explore the data and run SQL queries on it:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import duckdb
import pyarrow as pa


def get_table(table):
    rows = [
        {h: row[i] for (i, h) in enumerate(table["header"])} for row in table["rows"]
    ]

    return pa.Table.from_pylist(rows)


table = get_table(data[idx]["table"])
duckdb.arrow(table).query("table", 'SELECT * FROM "table"')
```

```
┌──────────────────────┬─────────┬───────────────┬────────────────┬──────────────────┬──────────────────┐
│        Player        │   No.   │  Nationality  │    Position    │ Years in Toronto │ School/Club Team │
│       varchar        │ varchar │    varchar    │    varchar     │     varchar      │     varchar      │
├──────────────────────┼─────────┼───────────────┼────────────────┼──────────────────┼──────────────────┤
│ Aleksandar Radojević │ 25      │ Serbia        │ Center         │ 1999-2000        │ Barton CC (KS)   │
│ Shawn Respert        │ 31      │ United States │ Guard          │ 1997-98          │ Michigan State   │
│ Quentin Richardson   │ N/A     │ United States │ Forward        │ 2013-present     │ DePaul           │
│ Alvin Robertson      │ 7, 21   │ United States │ Guard          │ 1995-96          │ Arkansas         │
│ Carlos Rogers        │ 33, 34  │ United States │ Forward-Center │ 1995-98          │ Tennessee State  │
│ Roy Rogers           │ 9       │ United States │ Forward        │ 1998             │ Alabama          │
│ Jalen Rose           │ 5       │ United States │ Guard-Forward  │ 2003-06          │ Michigan         │
│ Terrence Ross        │ 31      │ United States │ Guard          │ 2012-present     │ Washington       │
└──────────────────────┴─────────┴───────────────┴────────────────┴──────────────────┴──────────────────┘
```

In WikiSQL, the queries are formatted as a series of projection and filter expressions. Although there is a `human_readable` field, it's not valid SQL!

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
data[idx]["sql"]
```

```
{'human_readable': 'SELECT School/Club Team FROM table WHERE Years in Toronto = 1995-96',
 'sel': 5,
 'agg': 0,
 'conds': {'column_index': [4],
  'operator_index': [0],
  'condition': ['1995-96']}}
```

Let's define a `codegen_query` function that turns it into executable SQL.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
AGG_OPS = [None, "MAX", "MIN", "COUNT", "SUM", "AVG"]
COND_OPS = [" ILIKE ", ">", "<"]  # , "OP"]


def esc_fn(s):
    return f'''"{s.replace('"', '""')}"'''


def esc_value(s):
    if isinstance(s, str):
        return s.replace("'", "''")
    else:
        return s


def codegen_query(query):
    header = query["table"]["header"]

    projection = f"{esc_fn(header[query['sql']['sel']])}"

    agg_op = AGG_OPS[query["sql"]["agg"]]
    if agg_op is not None:
        projection = f"{agg_op}({projection})"

    conds = query["sql"]["conds"]

    filters = " and ".join(
        [
            f"""{esc_fn(header[field])}{COND_OPS[cond]}'{esc_value(value)}'"""
            for (field, cond, value) in zip(
                conds["column_index"], conds["operator_index"], conds["condition"]
            )
        ]
    )

    if filters:
        filters = f" WHERE {filters}"

    return f'SELECT {projection} FROM "table"{filters}'


gt_sql = codegen_query(data[idx])
print(gt_sql)
```

```
SELECT "School/Club Team" FROM "table" WHERE "Years in Toronto" ILIKE '1995-96'
```

Now, we can run this SQL directly.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
duckdb.arrow(table).query("table", gt_sql)
```

```
┌──────────────────┐
│ School/Club Team │
│     varchar      │
├──────────────────┤
│ Arkansas         │
└──────────────────┘
```

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import duckdb
import pyarrow as pa
from datasets import load_dataset
from Levenshtein import distance

NUM_TEST_EXAMPLES = 10


# Define some helper functions


def green(s):
    return "\x1b[32m" + s + "\x1b[0m"


def run_query(sql, table_record):
    table = get_table(table_record)  # noqa
    rel_from_arrow = duckdb.arrow(table)

    result = rel_from_arrow.query("table", sql).fetchone()
    if result and len(result) > 0:
        return result[0]
    return None


def score(r1, r2):
    if r1 is None and r2 is None:
        return 1
    if r1 is None or r2 is None:
        return 0

    r1, r2 = str(r1), str(r2)

    total_len = max(len(r1), len(r2))
    return 1 - distance(r1, r2) / total_len
```

## Running your first experiment

In this section, we'll create our first experiment and analyze the results in Braintrust.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import os

from braintrust import wrap_openai
from openai import OpenAI

client = wrap_openai(
    OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "Your OPENAI_API_KEY here"))
)


def text2sql(input):
    table = input["table"]
    meta = "\n".join(f'"{h}"' for h in table["header"])

    messages = [
        {
            "role": "system",
            "content": f"""
Print a SQL query (over a table named "table" quoted with double quotes) that answers the question below.

You have the following columns:
{meta}

The user will provide a question. Reply with a valid ANSI SQL query that answers the question, and nothing else.""",
        },
        {
            "role": "user",
            "content": f"Question: {input['question']}",
        },
    ]

    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    sql_text = resp.choices[0].message.content
    return sql_text.rstrip(";")


output_sql = text2sql(data[idx])
print(output_sql)

duckdb.arrow(table).query("table", output_sql)
```

```
SELECT "School/Club Team"
FROM "table"
WHERE "Years in Toronto" = '1995-96'
```

```
┌──────────────────┐
│ School/Club Team │
│     varchar      │
├──────────────────┤
│ Arkansas         │
└──────────────────┘
```

Exciting! Now that we've tested it out on an example, we can run an evaluation on a bigger dataset to understand how well the prompt works.

## Running an eval

To run an eval, we simply need to stitch together the pieces we've already created into the `Eval()` function, which takes:

* The data you want to evaluate
* A `task` function that, given some input, returns an output
* One or more scoring functions that evaluate the output.

Let's start by logging into Braintrust. You can technically skip this step if you've set `BRAINTRUST_API_KEY` in your environment.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import braintrust

braintrust.login(
    api_key=os.environ.get("BRAINTRUST_API_KEY", "Your BRAINTRUST_API_KEY here")
)
```

### Scoring functions

Next, we need to figure out how we'll score the outputs. One way is to string compare the SQL queries. This is not a perfect signal, because two different query strings might return the correct result, but it is a useful signal about how different the generated query is from the ground truth.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from autoevals import Levenshtein

Levenshtein().eval(output=output_sql, expected=gt_sql)
```

```
Score(name='Levenshtein', score=0.9113924050632911, metadata={}, error=None)
```

A more robust way to test the queries is to run them on a database and compare the results. We'll use DuckDB for this. We'll define a scoring function that runs the generated SQL and compares the results to the ground truth.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from autoevals import Score


@braintrust.traced
def result_score(output, expected, input):
    expected_answer = run_query(expected, input["table"])

    # These log statements allow us to see the expected and output values in the Braintrust UI
    braintrust.current_span().log(expected=expected_answer)

    try:
        output_answer = run_query(output, input["table"])
    except Exception as e:
        return Score(name="SQL Result", score=0, metadata={"message": f"Error: {e}"})

    braintrust.current_span().log(output=output_answer)

    return Score(
        name="SQL Result",
        score=Levenshtein()(output=output_answer, expected=expected_answer).score,
    )


result_score(output_sql, gt_sql, data[idx])
```

```
Score(name='SQL Result', score=1.0, metadata={}, error=None)
```

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from braintrust import EvalAsync

await EvalAsync(
    "Text2SQL Cookbook",
    data=[
        {"input": d, "expected": codegen_query(d), "metadata": {"idx": i}}
        for (i, d) in enumerate(data[:NUM_TEST_EXAMPLES])
    ],
    task=text2sql,
    scores=[Levenshtein, result_score],
)
```

```
Experiment text-2-sql-1706754968 is running at https://www.braintrust.dev/app/braintrust.dev/p/Text2SQL%20Cookbook/text-2-sql-1706754968
Text2SQL Cookbook (data): 10it [00:00, 42711.85it/s]
```

```
Text2SQL Cookbook (tasks):   0%|          | 0/10 [00:00<?, ?it/s]
```

```

=========================SUMMARY=========================
See results for text-2-sql-1706754968 at https://www.braintrust.dev/app/braintrust.dev/p/Text2SQL%20Cookbook/text-2-sql-1706754968
```

Once the eval completes, you can click on the link to see the results in the Braintrust UI.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/initial-results.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=ee57d7c422430b4490d4e1168a704aa7" alt="Eval results" data-og-width="1672" width="1672" data-og-height="950" height="950" data-path="cookbook/assets/Text2SQL/initial-results.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/initial-results.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=c3026980a791dba54ab9785bc8757e33 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/initial-results.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=7d7814536534cfc3b499f14101bf164a 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/initial-results.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=7c111e6007de2653c61d19bd49be042c 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/initial-results.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=a894767dce057d845709ff40c3142106 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/initial-results.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=d1eabce65d07f1df777e055996de8a25 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/initial-results.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=da9febded92f92e5186169a9e5c42f86 2500w" />

Take a look at the failures. Feel free to explore individual examples, filter down to low `answer` scores, etc. You should notice that `idx=8` is one of the failures. Let's debug it and see if we can improve the prompt.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/idx-8.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=ffa86a955ffeaf17df166fa755082c31" alt="idx=4" data-og-width="4080" width="4080" data-og-height="2348" height="2348" data-path="cookbook/assets/Text2SQL/idx-8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/idx-8.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=b18291fd276a91bd651a44e19cc472e4 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/idx-8.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=35df2b4dd8d6bf15b223cb48f16f0266 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/idx-8.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=466228f374dcad5d318b15c85938e921 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/idx-8.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=079a59d8da1c411c8ec9671b6fe19798 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/idx-8.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=9abd38f0927b6f157c1491e04a65d593 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/idx-8.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=8862ac03e79a0c60ce8a5554d1b88e57 2500w" />

## Debugging a failure

We'll first set `idx=8` and reproduce the failure.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
idx = 8
```

Here is the ground truth:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
print(data[idx]["question"])

table = get_table(data[idx]["table"])
print(duckdb.arrow(table).query("table", 'SELECT * FROM "table" LIMIT 5'))

gt_sql = codegen_query(data[idx])
print(gt_sql)

print(duckdb.arrow(table).query("table", gt_sql))
```

```
What are the nationalities of the player picked from Thunder Bay Flyers (ushl)
┌─────────┬──────────────────┬────────────┬────────────────┬──────────────────────┬────────────────────────────────────┐
│  Pick   │      Player      │  Position  │  Nationality   │       NHL team       │      College/junior/club team      │
│ varchar │     varchar      │  varchar   │    varchar     │       varchar        │              varchar               │
├─────────┼──────────────────┼────────────┼────────────────┼──────────────────────┼────────────────────────────────────┤
│ 27      │ Rhett Warrener   │ Defence    │ Canada         │ Florida Panthers     │ Saskatoon Blades (WHL)             │
│ 28      │ Johan Davidsson  │ Left Wing  │ Sweden         │ Mighty Ducks of An…  │ HV71 (Sweden)                      │
│ 29      │ Stanislav Neckar │ Defence    │ Czech Republic │ Ottawa Senators      │ HC České Budějovice ( Czech Repu…  │
│ 30      │ Deron Quint      │ Defence    │ United States  │ Winnipeg Jets        │ Seattle Thunderbirds (WHL)         │
│ 31      │ Jason Podollan   │ Right Wing │ Canada         │ Florida Panthers     │ Spokane Chiefs (WHL)               │
└─────────┴──────────────────┴────────────┴────────────────┴──────────────────────┴────────────────────────────────────┘

SELECT "Nationality" FROM "table" WHERE "College/junior/club team" ILIKE 'Thunder Bay Flyers (USHL)'
┌─────────────┐
│ Nationality │
│   varchar   │
├─────────────┤
│ Canada      │
└─────────────┘
```

And then what the model spits out:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
output_sql = text2sql(data[idx])
print(output_sql)
duckdb.arrow(table).query("table", output_sql)
```

```
SELECT DISTINCT "Nationality"
FROM "table"
WHERE "College/junior/club team" = 'Thunder Bay Flyers (ushl)'
```

```
┌─────────────┐
│ Nationality │
│   varchar   │
├─────────────┤
│   0 rows    │
└─────────────┘
```

Hmm, if only the model knew that `'ushl'` is actually capitalized in the data. Let's fix this by providing some sample data for each column:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def text2sql(input):
    table = input["table"]
    rows = [
        {h: row[i] for (i, h) in enumerate(table["header"])} for row in table["rows"]
    ]
    meta = "\n".join(f'"{h}": {[row[h] for row in rows[:10]]}' for h in table["header"])

    messages = [
        {
            "role": "system",
            "content": f"""
Print a SQL query (over a table named "table" quoted with double quotes) that answers the question below.

You have the following columns (each with some sample data). Make sure to use the correct
column names for each data value:

{meta}

The user will provide a question. Reply with a valid ANSI SQL query that answers the question, and nothing else.""",
        },
        {
            "role": "user",
            "content": f"Question: {input['question']}",
        },
    ]

    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    sql_text = resp.choices[0].message.content
    return sql_text.rstrip(";")


output_sql = text2sql(data[idx])
print(output_sql)

duckdb.arrow(table).query("table", output_sql)
```

```
SELECT Nationality FROM "table" WHERE "College/junior/club team" = 'Thunder Bay Flyers (USHL)'
```

```
┌─────────────┐
│ Nationality │
│   varchar   │
├─────────────┤
│ Canada      │
└─────────────┘
```

Ok great! Now let's re-run the loop with this new version of the code.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
await EvalAsync(
    "Text2SQL Cookbook",
    data=[
        {"input": d, "expected": codegen_query(d), "metadata": {"idx": i}}
        for (i, d) in enumerate(data[:NUM_TEST_EXAMPLES])
    ],
    task=text2sql,
    scores=[Levenshtein, result_score],
)
```

```
Experiment text-2-sql-1706755609 is running at https://www.braintrust.dev/app/braintrust.dev/p/Text2SQL%20Cookbook/text-2-sql-1706755609
Text2SQL Cookbook (data): 10it [00:00, 22562.15it/s]
```

```
Text2SQL Cookbook (tasks):   0%|          | 0/10 [00:00<?, ?it/s]
```

```

=========================SUMMARY=========================
text-2-sql-1706755609 compared to text-2-sql-1706754968:
63.82% (+10.33%) 'SQL Result'  score	(2 improvements, 1 regressions)
80.53% (+03.66%) 'Levenshtein' score	(5 improvements, 3 regressions)

1.22s (-16.20%) 'duration'	(8 improvements, 2 regressions)

See results for text-2-sql-1706755609 at https://www.braintrust.dev/app/braintrust.dev/p/Text2SQL%20Cookbook/text-2-sql-1706755609
```

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/second-experiment.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=a50d5deed6be112ceeacc9b8de8e26c7" alt="Second experiment" data-og-width="1590" width="1590" data-og-height="956" height="956" data-path="cookbook/assets/Text2SQL/second-experiment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/second-experiment.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=e03542cf712f166db566b722f87b23b4 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/second-experiment.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=409b40f47f1d7e6ba21366b2c20f7486 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/second-experiment.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=b7e017193a0e726c23df1ddbccc0aa68 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/second-experiment.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=c0d689e75cad1629ea72921d0be26685 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/second-experiment.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=92eaa71da1b51b20025d8a16217c2ceb 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/Text2SQL/second-experiment.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=47be7480913c16b206a1c46320e908d3 2500w" />

## Wrapping up

Congrats 🎉. You've run your first couple of experiments. Now, return back to the tutorial docs to proceed to the next step where we'll analyze the experiments.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt