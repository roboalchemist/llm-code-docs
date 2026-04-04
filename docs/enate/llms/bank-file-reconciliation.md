# Source: https://docs.enate.net/enate-help/enateai/enateai/enateai-ai-analyst/ai-prompts/bank-file-reconciliation.md

# Bank File Reconciliation

### Scenario Description

Matching entries from two different excel documents, matching bank statement transactions from one system with entries in a Master file from another system. Output should be a list of the transactions (rows in the excels) which do not match.

### Sample Input Files:

* Bank Transaction File

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FYVobybJQ5TXYxnbWmOht%2FBank%20Transactions.csv?alt=media&token=f5b73f38-7152-424d-ab78-b1ce0567d10f>" %}

* Master File

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FNGt1k7pL8TKOgoRABJYK%2FMaster%20File.csv?alt=media&token=2451291e-43ff-440b-bc75-679007e43dd1>" %}

### Input File Tags:&#x20;

* Transactions&#x20;
* Masterfile

### Output File Tags:

* AI Output Bank File

### AI Persona Title:

* Bank Clerk

### AI Persona Description:

* You are a bank clerk who works on file reconciliation queries.

### Prompt Text

{% code overflow="wrap" %}

```
**Objective:**   
To efficiently match bank statement transactions in the file {{FileTag:Transactions}} with entries in a master file called {{FileTag:masterfile}} ,   

ensuring all transactions are correctly reconciled, and to identify any discrepancies that require further investigation.  

**Scope:**  
This policy applies to the reconciliation process involving bank statement transactions and a master transaction file.  

**Procedure:**  
1. **Preparation of Data Files:**  

   - Confirm that the following key fields are present and correctly labeled in both files:  

     - **Transaction ID:** Unique identifier for each transaction.  

     - **Date:** Transaction date.  

     - **Amount:** Transaction amount.  

     - **Description:** Brief description of the transaction.  

2. **Defining Matching Criteria:**  
   - Transactions will be matched based on the following fields:  

     - **Transaction ID**  

     - **Amount**  

   - Ensure exact matches for both fields to confirm a transaction as reconciled.  

3. **Comparison Process:**  
   - Open both the bank statement file and the master file in a spreadsheet program such as Microsoft Excel or Google Sheets.  

   - Use conditional formatting or formulas to highlight transactions where the Transaction ID and Amount match in both files.  

   - Manually identify and mark any discrepancies in other fields like Date or Description for transactions that have matched IDs and Amounts.  

   - Identify transactions that are present in one file but not in the other, marking these as unmatched.  

4. **Creation of Reconciliation Report:**  
   - Create a new detailed report covering all transactions as an .xlsx. Divide the spreadsheet into three sections:  

     - **Matched Transactions:** List all transactions where the Transaction ID and Amount align in both files.  

     - **Mismatched Transactions:** Document transactions with the same Transaction ID but discrepancies in other details.  

     - **Unmatched Transactions:** List all entries that do not find a match in the opposite file.  

5. If the input files provided do not match data for reconciliation and it's not useful for analysis give me the error output file in .txt do not wait for confirmation from us again.  

```

{% endcode %}

### AI Creativity Level:&#x20;

* Balanced
