# Source: https://docs.datafold.com/data-diff/in-database-diffing/creating-a-new-data-diff.md

# Source: https://docs.datafold.com/data-diff/cross-database-diffing/creating-a-new-data-diff.md

# Source: https://docs.datafold.com/data-diff/in-database-diffing/creating-a-new-data-diff.md

# Source: https://docs.datafold.com/data-diff/cross-database-diffing/creating-a-new-data-diff.md

# Source: https://docs.datafold.com/data-diff/in-database-diffing/creating-a-new-data-diff.md

# Source: https://docs.datafold.com/data-diff/cross-database-diffing/creating-a-new-data-diff.md

# Source: https://docs.datafold.com/data-diff/in-database-diffing/creating-a-new-data-diff.md

# Source: https://docs.datafold.com/data-diff/cross-database-diffing/creating-a-new-data-diff.md

# Source: https://docs.datafold.com/data-diff/in-database-diffing/creating-a-new-data-diff.md

# Source: https://docs.datafold.com/data-diff/cross-database-diffing/creating-a-new-data-diff.md

# Creating a New Data Diff

> Datafold's Data Diff can compare data across databases (e.g., PostgreSQL <> Snowflake, or between two SQL Server instances) to validate migrations, meet regulatory and compliance requirements, or ensure data is flowing successfully from source to target.

This powerful algorithm provides full row-, column-, and value-level detail into discrepancies between data tables.

## Creating a new data diff

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/creating.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=51b3d0c833d953bc4c773a3cb9852a1a" data-og-width="1414" width="1414" data-og-height="1540" height="1540" data-path="images/creating.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/creating.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=25d6e6399462fda4e49a15595530b1da 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/creating.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=46933ba2c7f36514ff9f64d951073f3e 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/creating.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=39df2f5bbff7af814d08f317266874f9 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/creating.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a2084bf150cb297459092928e06120a6 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/creating.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=b3a327e131204aba94717368790a338a 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/creating.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4ee7a1980c87da54411e4ceafaa13d48 2500w" />
</Frame>

Setting up a new data diff in Datafold is straightforward. You can configure your data diffs with the following parameters and options:

### Source and Target datasets

#### Data connection

Pick your data connection(s).

#### Diff type

Choose how you want to compare your data:

* Table: Select this to compare data directly from database tables
* Query: Use this to compare results from specific SQL queries

#### Dataset

Choose the dataset you want to compare. This can be a table or a view in your relational database.

#### Filter

Insert your filter clause after the WHERE keyword to refine your dataset. For example: `created_at > '2000-01-01'` will only include data created after January 1, 2000.

### Materialize inputs

Select this option to improve diffing speed when query is heavy on compute, or if filters are applied to non-indexed columns, or if primary keys are transformed using concatenation, coalesce, or another function.

## Column remapping

Designate columns with the same data type and different column names to be compared. Data Diff will surface differences under the column name used in the Source dataset.
<Note>Datafold automatically handles differences in data types to ensure accurate comparisons. See our best practices below for how this is handled.</Note>

## General

### Primary key

The primary key is one or more columns used to uniquely identify a row in the dataset during diffing. The primary key (or keys) does not need to be formally defined in the database or elsewhere as it is used for unique row identification during diffing.

<Note>
  Textual primary keys do not support values outside the set of characters `a-zA-Z0-9!"()*/^+-<>=`. If these values exist, we recommend filtering them out before running the diff operation.
</Note>

### Columns

#### Columns to compare

Specify which columns to compare between datasets.
Note that this has performance implications when comparing a large number of columns, especially in wide tables with 30 or more columns. It is recommended to initially focus on comparisons using only the primary key or to select a limited subset of columns.

### Row sampling

Use sampling to compare a subset of your data instead of the entire dataset. This is best for diffing large datasets. Sampling can be configured to select a percentage of rows to compare, or to ensure differences are found to a chosen degree of statistical confidence.

#### Sampling tolerance

Sampling tolerance defines the allowable margin of error for our estimate. It sets the acceptable percentage of rows with primary key errors (e.g., nulls, duplicates, or primary keys exclusive to one dataset) before disabling sampling.
When sampling is enabled, not every row is examined, which introduces a probability of missing certain discrepancies. This threshold represents the level of difference we are willing to accept before considering the results unreliable and thereby disabling sampling. It essentially sets a limit on how much variance is tolerable in the sample compared to the complete dataset.
Default: 0.001%

#### Sampling confidence

Sampling confidence reflects our level of certainty that our sample accurately represents the entire dataset. It represents the minimum confidence level that the rate of primary key errors is below the threshold defined in sampling tolerance.
To put it simply, a 95% confidence level with a 5% tolerance means we are 95% certain that the true value falls within 5% of our estimate.
Default: 99%

#### Sampling threshold

Sampling is automatically disabled when the total row count of the largest table in the comparison falls below a specified threshold value. This approach is adopted because, for smaller datasets, a complete dataset comparison is not only more feasible but also quicker and more efficient than sampling. Disabling sampling in these scenarios ensures comprehensive data coverage and provides more accurate insights, as it becomes practical to examine every row in the dataset without significant time or resource constraints.

#### Sample size

This provides an estimated count of the total number of rows included in the combined sample from Datasets A and B, used for the diffing process. It's important to note that this number is an estimate and can vary from the actual sample size due to several factors:
The presence of duplicate primary keys in the datasets will likely increase this estimate, as it inflates the perceived uniqueness of rows.

* Applying filters to the datasets tends to reduce the estimate, as it narrows down the data scope.
* The number of rows we sample is not fixed; instead, we use a statistical approach called the Poisson distribution. This involves picking rows randomly from an infinite pool of rows with uniform random sampling. Importantly, we don't need to perform a full diff (compare every single row) to establish a baseline.

Example: Imagine there are two datasets we want to compare, Source and Target. Since we prefer not to check every row, we use a statistical approach to determine the number of rows to sample from each dataset. To do so, we set the following parameters:

* Sampling tolerance: 5%
* Sampling confidence: 95%

Sampling confidence reflects our level of certainty that our sample accurately represents the entire dataset, while sampling tolerance defines the allowable margin of error for our estimate. Here, with a 95% sampling confidence and a 5% sampling tolerance, we are 95% confident that the true value falls within 5% of our estimate. Datafold will then estimate the sample size needed (e.g., 200 rows) to achieve these parameters.

### Advanced

#### Materialize diff results to table

Create a detailed table from your diff results, indicating each row where differences occur. This table will include corresponding values from both datasets and flags showing whether each row matches or mismatches.
