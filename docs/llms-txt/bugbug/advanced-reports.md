# Source: https://docs.bugbug.io/organizing-tests/reporting/advanced-reports.md

# Advanced reports

BugBug provides **compliance-ready test reports** that include detailed **PDFs with step-by-step screenshots**. You can easily export your test run and suite run data in multiple formats, including JSON, CSV, and more.

{% hint style="success" %}
Advance reports are available only in the [BUSINESS](https://bugbug.io/pricing/) plan.
{% endhint %}

### Available report types

* **Detailed PDF report with screenshots** - Comprehensive, compliance-friendly report including each step and screenshot. Perfect for audits and documentation.
* **CSV** - Spreadsheet format containing all tests, steps, and selectors. Ideal for data analysis or importing into BI tools.
* **JSON** - Structured data format designed for sending results to other apps or integrating with external systems.
* **ZIP with screenshots** - A packaged folder containing separate CSV and JSON files for each test, along with all related screenshots.

{% @arcade/embed flowId="L6kL6B3udaDyLJBCe1it" url="<https://app.arcade.software/share/L6kL6B3udaDyLJBCe1it>" %}

###

### How to download an Advanced report for a suite run

1. Go to the specific suite run in Runs history.
2. Click `Download report` in the top-right corner.<br>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Ff6fEgsergwpcccsM1ZF0%2Fimage.png?alt=media&#x26;token=d3ecca04-83f1-4ef9-bf6d-dd41240ab081" alt=""><figcaption></figcaption></figure>

3. Select your preferred format and click `Continue`.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FSIY6sWd3MlIXP3Hl6pUM%2Fimage.png?alt=media&#x26;token=b2d2d2fe-711e-4e6a-9a79-00482ce05d6f" alt=""><figcaption></figcaption></figure>

5. If you want to include additional context, you can add a custom note to the report before downloading. Once ready, click  `Download` to start the report generation process.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FxfS5TmPXDGiFwelJhAGf%2Fimage.png?alt=media&#x26;token=ffdfd268-87e3-4686-9bce-6f5b6e4cbf42" alt=""><figcaption></figcaption></figure>

6. Report generation will begin, and you’ll receive a download link via email once it’s ready.\
   The process runs asynchronously, as generating detailed reports with screenshots may take a few minutes.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fu7eOaiIqyJ18cJSFmVRi%2Fimage.png?alt=media&#x26;token=27c9ec1b-c232-49af-9939-57daf8aa305c" alt=""><figcaption></figcaption></figure>

7. Click the `Download PDF report`  button in your email. You’ll be redirected to the BugBug app, where the report download will start automatically.

{% hint style="warning" %}
All advanced reports are available for **24 hours** after generation.\
After that, the download links will expire, and you’ll need to generate a new report if needed.
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FMqom4oNN6AY5OPp08hcI%2Fimage.png?alt=media&#x26;token=f82c3f5e-6d62-4f01-8695-ba56f0ed89aa" alt=""><figcaption></figcaption></figure>

> Advanced reports that include screenshots — such as **detailed PDF** or **ZIP with screenshots** — can be quite large, sometimes exceeding **hundreds of megabytes**, since each test step includes its own screenshot. Keep this in mind when downloading or sharing reports.

###

### Examples of advanced reports

Below, you can find an example of how advanced reports look like for a single suite run with multiple tests inside.&#x20;

{% file src="<https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FoQwEGiHQ63JuKss9j96H%2FStaging_-_E2E_Regression_tests_2025-11-03_90490.pdf?alt=media&token=de5fb8cb-d7e9-40de-a53e-f6c25dceeba0>" %}

{% file src="<https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Ftt71oA9YGH3CmNIshHex%2FStaging_-_E2E_Regression_tests_2025-11-03_90490.csv?alt=media&token=ec8b4ffd-e63c-4ccc-9d32-ea94b0af21c3>" %}

{% file src="<https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FQ0ELyHi9OY3J2BkmS9N3%2FStaging_-_E2E_Regression_tests_2025-11-03_90490.json?alt=media&token=48776641-b1a1-401b-9023-018f1f9f0246>" %}

{% file src="<https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fmg2UfLrMhTsww450Dbqd%2FStaging_-_E2E_Regression_tests_2025-11-03_90490.zip?alt=media&token=d7b3bc37-c425-4b6b-ae6b-7fb241b43fe4>" %}
