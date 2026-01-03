# Source: https://docs.promptlayer.com/features/evaluations/score-card.md

# Score Card

The score card feature in PromptLayer allows you to assign a score to each evaluation you run. This score provides a quick and easy way to assess the performance of your prompts and compare different versions.

## Configuring the Score Card

<Frame>
    <img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/default.png?fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=deaba2a75eba0127193ea65860c76341" alt="Score Card Example" data-og-width="1270" width="1270" data-og-height="870" height="870" data-path="images/score-card/default.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/default.png?w=280&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=a0ec211ac503de14f1fdf06c97beb257 280w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/default.png?w=560&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=19cba28ff5abd602a530cf117def4b80 560w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/default.png?w=840&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=e576dc325e6c597575ed0635cac45b0f 840w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/default.png?w=1100&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=fd7956c86e1990bd4b447bf6db52265d 1100w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/default.png?w=1650&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=e571a15baeb553cc6571e14ecfa14bb4 1650w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/default.png?w=2500&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=1e457a012964ad94b32d2c301a835bd4 2500w" />
</Frame>

### Default Configuration

By default, the score is calculated based on the last column in your evaluation results:

* If the last column contains Booleans, the score will be the percentage of `true` values.
* If the last column contains numbers, the score will be the average of those numbers.

### Custom Column Selection

You can customize which columns are included in the score card calculation. When setting up your evaluation pipeline, click the "Score card" button to configure the score card.

Here, you can add specific columns to be included in the score calculation:

* If you add multiple numeric columns, the total score will be the average of the averages for each selected column.
* If you add multiple Boolean columns, the total score will be the average of the `true` percentages for each selected column.
* Columns that do not contain numbers or Booleans will not be included in the score calculation.

<Frame>
    <img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/columns.png?fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=6301a9d554bf4dda8caff15c347c1304" alt="Score Card Columns" data-og-width="1246" width="1246" data-og-height="853" height="853" data-path="images/score-card/columns.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/columns.png?w=280&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=0d53901496069505a69164584635dda2 280w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/columns.png?w=560&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=4655e0b8d005b9a2e32d925576922ba4 560w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/columns.png?w=840&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=a364d5ad712bd4883a906ff222946a29 840w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/columns.png?w=1100&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=bcd43f85c1bb7605dd9e8008c5ef78ae 1100w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/columns.png?w=1650&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=7e6c4c3bab3748259549675ed5795038 1650w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/columns.png?w=2500&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=3ba834b831b2ef5e5454f0a36445a278 2500w" />
</Frame>

These selected columns will also be formatted for more easy viewing in the evaluation report. You will see larger numbers, and check/x icons for booleans.

### Custom Scoring Logic

For more advanced scoring needs, you can provide your own custom scoring logic using Python or JavaScript code. The code execution environment is the same as the one used for the code execution evaluation column type [(learn more)](/features/evaluations/eval-types#code-execution).

This custom scoring logic can be used to generate a single score number or a drill-down matrix.

<Frame>
    <img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/matrix.png?fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=b75be2e45eaacc67d82185b24dfaaf65" alt="Score Card Matrix" data-og-width="640" width="640" data-og-height="400" height="400" data-path="images/score-card/matrix.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/matrix.png?w=280&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=611189b47bd4b85695a060e72bc8cc12 280w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/matrix.png?w=560&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=bdd0c28fc750324907cca1acd7ed0f17 560w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/matrix.png?w=840&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=cde7149f5dbca565a2ecfd973bcad458 840w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/matrix.png?w=1100&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=2e16ddcc5c5a7d604ded526660cb02b1 1100w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/matrix.png?w=1650&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=0fed4bbc31d96c3353009f2c2656af13 1650w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/matrix.png?w=2500&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=dbc87bdd6d467f8eaa43eee7991528cf 2500w" />
</Frame>

You can optionally return multiple drill-down matrices. This is useful for generating confusion matrices.

<Frame>
    <img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/matrices.gif?s=d847ca181f27b9b453a29162dfe6a61d" alt="Score Card Matrices" data-og-width="800" width="800" data-og-height="469" height="469" data-path="images/score-card/matrices.gif" data-optimize="true" data-opv="3" />
</Frame>

Your custom scoring code must return an object with the following keys:

* `score` (required): A number representing the overall score. This is mandatory.
* `score_matrix` (optional): A list of lists of lists, representing one or more matrices of drilled-down scores. Each cell in these matrices can be a raw value or an object with metadata.

#### Score Matrix Cell Format

Each cell in the `score_matrix` can be either:

* A raw value (string or number), or
* An object with the following properties:
  * `value`: The actual value of the cell, which can be a string or number.
  * `positive_metric`: (Optional) A boolean indicating whether an increase in this value is considered positive (`true`). If absent, we default to true.

**Examples**

* Simple value: `42`
* Object with metadata: `{"value": 42, "positive_metric": true}`

The optional `positive_metric` property can be used to indicate how changes in the value should be interpreted when comparing evaluations. This is particularly useful for automated reporting and analysis tools.

#### Adding Titles to Score Matrices

To add titles to your score matrices, simply add an extra field to the first row of the matrix and it will automatically be interpreted as the primary title. For example, if you have a matrix like:

```python  theme={null}
[[1,2],[1,2]]
```

You can add a title by modifying it to:

```python  theme={null}
[["Title",1,2],[1,2]]
```

### Code example

The `data` variable will be available in your scoring code, which is a list containing a dictionary for each row in the evaluation results. The keys in each dictionary correspond to the column names, and the values are the corresponding cell values.

For example:

```py Python theme={null}
# The variable `data` is a list of rows.
# Each row is a dictionary of column name -> value
# For example: [
#       {'columnA': 1, 'columnB': 2},
#       {'columnA': 4, 'columnB': 1}
#  ]
#
# Must return a dictionary with the following structure:
# {
#   'score': int,  # Required
#   'score_matrix': [[[int, int, ...], ...]...],  # Optional - list of lists of lists of integers
# }

return {
    'score': len(data),
    'score_matrix': [[
        ["Criteria", "Weight", "Value"],
        ["Correctness", 4, 7],
        ["Completeness", 3, 6],
        ["Accuracy", 5, 8],
        ["Relevance", 4, 9]
    ]],
}
```

## Comparing Evaluation Reports

You can compare two evaluation reports to see how scores and other metrics have changed between runs. Simply click the "Compare" button and select the evaluation reports you want to compare.

The score card and any score matrices will be displayed side-by-side for easy comparison of your prompt's performance over time.

<Frame>
    <img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/compare.png?fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=5192d223841cf30ff0e0cf84d61e3db9" alt="Compare Score Cards" data-og-width="1203" width="1203" data-og-height="830" height="830" data-path="images/score-card/compare.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/compare.png?w=280&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=4242a8ff0e0284cc60db0fa0e660bb50 280w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/compare.png?w=560&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=a20ceebcbaee7983dfeee326adab8a3a 560w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/compare.png?w=840&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=0884129fee1d5372f274463e43ab8da1 840w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/compare.png?w=1100&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=7b1e1b9ab8841e7bdc28b13a8f777118 1100w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/compare.png?w=1650&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=6924015175eba7391b03b7ae89b1ca5b 1650w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-card/compare.png?w=2500&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=c40ab82f35ca2df9ab4db69708bab309 2500w" />
</Frame>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt