# Source: https://docs.enate.net/enate-help/enateai/enateai/enateai-ai-analyst/ai-prompts/credit-card-statement-reconciliation.md

# Credit Card Statement Reconciliation

### Scenario Description

Perform data reconciliation between two input excel documents, one an expenses report and the other a credit card statement. Create a new file as output with a summary of data from each of the input files.

### Sample Files

* Expense Report File

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FRaUe6RJ9EXmjLafbtXWe%2Fexpense%20report.xlsx?alt=media&token=53a8bd8c-d53e-49a1-a130-c7d69664da6c>" %}

* Credit Card Statement

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F8zYrUzsRaMeEErTyzaUk%2Fcredit%20card%20statement.xlsx?alt=media&token=e6f23d78-d5d2-4c1f-8826-ef72a4482631>" %}

### Input File Tags:

* Expense Report
* Credit Card Statement

### Output File Tags:

* Expense Report AI Output

### AI Persona Title:

* Data Analyst

### AI Persona Description:

* You are a experienced data analyst working in a company finance department. You help handle expense reports filed by company employees.

### Prompt Text

{% code overflow="wrap" fullWidth="false" %}

```
Objective:
Match transactions between the expense report and credit card statement using Expense category and category.

1. Open and read both the Expense Report file {{FileTag:Expense Report}} and the Credit Card Statement file {{FileTag:Credit card statement}}.

2. Create a new file and call it "Travel Expenses". Now copy and paste all the data from the Expense Category column and expenses amount column in the expense report file into the new file, but only for rows that have the value travel in the expense category column.

3. Now copy and paste all data for the description column and the credit card amount column from the credit card statement file into the new file, but only for rows that have the value travel in the description column.

4. Now create a new column in the Travel Expenses file and call it ‘Total Travel Expenses’. Now calculate the total amount by adding the values in the expenses amount column and the credit card amount column and place the value in the first row of the travel expenses column.

Do not duplicate any columns.

If the input file provided does not match data for reconciliation and so is not useful for analysis, give me the error output file in .txt. 

Do not wait for confirmation from us again please go ahead with Reconciliation. Do not wait for confirmation again from us - Any question you have for me should be asked in output file format that is defined in step 4.


```

{% endcode %}

### AI Creativity Level:

* Balanced
