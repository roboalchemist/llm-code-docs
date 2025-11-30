# Source: https://dagshub.com/docs/tutorials/experiment_tutorial/0_data/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/tutorials/experiment_tutorial/0_data.md "Edit this page")

# Level 0 - Data Exploration[¶](#level-0-data-exploration "Permanent link") 

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1m-sghZTdPqtMguXIVJOeHqk-mn16Rg5Q?usp=sharing)

## Level overview[¶](#level-overview "Permanent link")

**This level of the tutorial covers downloading the data and performing some basic analysis of it to see what we have.**

The full analysis can be found in [this Colab notebook](https://colab.research.google.com/drive/1m-sghZTdPqtMguXIVJOeHqk-mn16Rg5Q?usp=sharing), but we\'ll go over the main points and conclusions together.

If you want to just skip ahead to the code, you can go straight to [the next level](../1_setup/).

## Description of the data[¶](#description-of-the-data "Permanent link")

Our data is a CSV file describing questions on the [Cross Validated Stack Exchange](https://stats.stackexchange.com/), a Q&A site for statistics.

It was generated from the Stack Exchange API with [this query](https://data.stackexchange.com/stats/query/1290704/relevant-crossvalidated-posts-latest). To make things easier for you, we already ran the query and saved its result in our public storage, so **you can download it straight [from here](https://dagshub-public.s3.us-east-2.amazonaws.com/tutorials/stackexchange/CrossValidated-Questions-Nov-2020.csv)**.

The data itself looks like this (click to get a full-size view):

[![DataFrame](../assets/df.png)](../assets/df.png)

The columns are pretty self-explanatory - we have:

- Two textual features (`Title` & `Body`).

We can already tell that this text is full of HTML tags, which we will probably need to clean to get good results.

- One string column that is the list of `Tags` for this question.
- Some numeric features: `Score, ViewCount, AnswerCount, CommentCount, FavoriteCount`.
- One `CreationDate` feature that needs to be processed correctly.

## Our objective[¶](#our-objective "Permanent link")

Each question on Cross Validated can be labeled with a set of topic tags, to make it easier for experts to find & answer.

For this tutorial, our goal will be to predict whether a given Cross Validated question should be tagged as a `machine-learning` related question. This is a supervised binary classification task, and the ground truth can be found in the `Tags` column:

    df['MachineLearning'] = df['Tags'].str.contains('machine-learning')

One important thing to note is that only about 11.1% of the data is labeled positive. This means that we\'re dealing with an imbalanced classification problem, and we will need to take this into account when choosing our performance metrics, and possibly use special sampling strategies or model configurations.

[![ML label distribution](../assets/ml_label_distribution.png)](../assets/ml_label_distribution.png)

## Conclusions from data exploration[¶](#conclusions-from-data-exploration "Permanent link")

- Our label `MachineLearning` is not too strongly related to any other single feature.
- We should drop the `FavoriteCount` column since it\'s highly correlated with `Score` and contains mostly `NaN`.
- `Score, ViewCount, AnswerCount` are highly skewed, so we\'ll take that into account in data preparation.

### Numeric features[¶](#numeric-features "Permanent link")

After massaging the numerical features so that they\'re scaled and less skewed, here are their distributions (click to get a full-size view):

[![Pairplot](../assets/pairplot.png)](../assets/pairplot.png)

These scaled numerical features were good enough to train a simple logistic regression classifier, that performs only slightly better than random. This can be seen in the model\'s [precision-recall curve](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html):

[![Numerical features PR plot](../assets/numerical_features_pr.png)](../assets/numerical_features_pr.png)

### Text features[¶](#text-features "Permanent link")

It makes sense that most of the information on a question\'s topic will be contained in its text content.

To turn the two textual features of the data into something we can train an ML model on, we first concatenate them:

    df['Text'] = df['Title'] + ' ' + df['Body']

And then train a [`TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) using this text column. For now, we don\'t do any fancy text processing - we just use the default logic contained in `TfidfVectorizer`.

This is already enough to get a very decently performing model:

[![TFIDF PR plot](../assets/tfidf_pr.png)](../assets/tfidf_pr.png)

Looking at the terms learned by the trained `TfidfVectorizer`, we can note some possible directions for improvement:

- Various numbers, like `00`, `00000000e` etc. It could be useful to prevent this splitting of numbers into many different terms in the vocabulary since it probably won\'t matter to classifying the text.
- Multiple terms are grouped due to an underscore, like `variable_2`. This is probably an artifact of embedded Python or TeX code. It might help the model if we break these down into separate terms.
- Remember, the questions contain embedded HTML. While we\'re not seeing any terms that were clearly garbage created by HTML, it\'s a good bet that it will be useful to clean up the HTML tags in the text.
- Of course, there\'s room to experiment with different hyperparameters of the `TfidfVectorizer` - vocabulary size, ngram range, etc.

## Next steps[¶](#next-steps "Permanent link")

We got a good sense of our data, the type of preprocessing required, and managed to train some decent classifiers with it.

At this point in a Python data science project, it\'s common to take the conclusions and working code from the exploratory notebook, and turn them into normal Python modules. This enables us to more easily:

- Create reusable components that will be useful as the project matures.
- Use code versioning tools like Git.
- Make the process more reproducible by defining a clear pipeline (order of operations) for the data and model training.
- Automate running and tracking of experiments.
- Version our different experiments and models, so that we preserve knowledge and don\'t risk losing work by accident.

[In the next level of this tutorial](../1_setup/), we\'ll take what works from this notebook and turn it into a Python project, before going forward with [data versioning](../2_data_versioning/) and [experimentation](../3_experiments/) to find the best performing model for our problem.

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).