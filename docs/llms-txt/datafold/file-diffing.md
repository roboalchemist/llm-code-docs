# Source: https://docs.datafold.com/data-diff/file-diffing.md

# File Diffing

> Datafold allows you to diff files (e.g. CSV, Excel, Parquet, etc.) in a similar way to how you diff tables.

<Note>
  If you'd like to enable file diffing for your organization, please contact [support@datafold.com](mailto:support@datafold.com).
</Note>

In addition to diffing data in tables, views, and SQL queries, Datafold allows you to diff data in files hosted in cloud storage. For example, you can diff between an Excel file and a Snowflake table, or between a CSV file and an Excel file.

## Supported cloud storage providers

Datafold supports diffing files in the following cloud storage providers, with plans to support more in the future:

* Amazon S3
* Azure Blob Storage
* Azure Data Lake Storage (ADLS)
* Google Cloud Storage

## Supported file types

Datafold supports diffing the following file types:

* Tabular text files (e.g. `.csv`, `.tsv`, `.txt`, `.dat`)
* Excel (`.xlsx`, `.xls`)
* Parquet (`.parquet`)

## Type-specific options

Depending on the type of file you're diffing, you'll have a few options to specify how you'd like to parse the file.

For example, when diffing a tabular text file, you can specify the delimiter and skip header/footer rows.

<img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/file-diffing/adls-file-diff-options.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=bfbe8fbf183c9bf80bdedd39a5f8e110" alt="File diffing options" data-og-width="1440" width="1440" data-og-height="732" height="732" data-path="images/data_diff/file-diffing/adls-file-diff-options.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/file-diffing/adls-file-diff-options.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=5607d6a653192d345ede77ab89f7ff25 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/file-diffing/adls-file-diff-options.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=7f0bbf12eecac1b5c0ac76468c72daa7 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/file-diffing/adls-file-diff-options.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c2f297820dd0c454d8c563a1c31982f7 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/file-diffing/adls-file-diff-options.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=f5721a09b770a556877b6859c45d4539 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/file-diffing/adls-file-diff-options.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=54d0ef8b5cfb2b49492cdaba2158361b 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff/file-diffing/adls-file-diff-options.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=61a426a8f98cb76c65b487577fd486bb 2500w" />
