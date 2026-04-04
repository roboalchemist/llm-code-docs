# Source: https://docs.aporia.com/explainability/shap-values.md

# SHAP values

In the following guide we will explain how one can visualize SHAP values in Aporia to gain better explainability for their model’s predictions and increase trust.

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FzkrP6zUluI7FFQR4ZwDD%2Fshap.gif?alt=media&#x26;token=63730b82-dc06-4b3e-be81-f89cc4c7e701" alt=""><figcaption></figcaption></figure>

### Ingest your Shaply values

Ingesting your Shaply values in Aporia can be done by adding a column with the following naming convention `<feature_name>_shap`.

For example, the SHAP column corresponding to a `featureX` would be `featureX_shap`.

Please note:

1. the SHAP column should not be mapped to the version schema but you must include it in your SQL query when integrating your training/serving dataset.
2. `_shap` must be lowercase and the `<feature_name>`  must be same case as the feature in Aporia. For those of you who use Snowflake we would recommend to pay attention that if the value is read directly from a table using `SELECT *`, the case-ness of the column name will be saved. Otherwise, your can force Snowflake to preserve case by using double quotes in the query. For example, `SELECT 1 AS a, 2 AS "b"` would return a table with 2 columns: `A` and `b`.

### Explain your predictions

Exploring SHAP values can be done via our Data Points cell as part of an Investigation Case.

When clicking on explain you’ll be able to view all the available SHAP values as well as getting a textual business explanation which you can share with stakeholders.

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FvFi1mpGcDnFEDPda6RRH%2Fimage.png?alt=media&#x26;token=f7e88bd4-0c3b-43fa-8b08-330baa3803f8" alt=""><figcaption><p>Click on Explain to view the SHAP values of the chosen prediction</p></figcaption></figure>

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FffMxVwqsXQs88avVaLuE%2Fimage.png?alt=media&#x26;token=955bbcc8-bf32-48bb-9e04-081c5470150a" alt=""><figcaption><p>Copy the business explanation to share with stakeholders</p></figcaption></figure>
