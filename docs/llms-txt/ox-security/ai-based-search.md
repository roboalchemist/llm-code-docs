# Source: https://docs.ox.security/scan-and-analyze-with-ox/analyzing-scan-results/ai-based-search.md

# AI Based Search

AI Search lets you describe what you are searching for in natural language without learning every filter or field.

AI Search does not add data. It interprets your request and applies existing filters on the page. If a concept is not represented in your data or filters, results can be empty.

Best practices:

* Be specific when a term is broad. If the exploit is too general, name the exploit type or context.
* Combine conditions in one sentence. For example, critical and high, or reachable and exploitable.
* If you get no results, start simple and add one condition at a time.
* After AI applies filters, review them, adjust as needed, and search again.

## What You Can Do With AI Search

| Task                      | How it works                                                                             |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| Find by severity          | “Show all critical and high issues” applies Severity = Critical, High.                   |
| Find by security concept  | “Show all issues with improper authorization” or “Show all cross-site scripting issues.” |
| Find by multiple concepts | “Show all issues with overprivileged access and cross-site scripting.”                   |
| Find by time pressure     | “Show all issues with SLA due in the next 7 days.”                                       |
| Find by severity factors  | “Show issues that are reachable, exploitable, and high damage.”                          |

## Using the AI search

1. Go to a supported page, such as Active Issues, and select **Search with AI**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0bd7a2eb2587489db07873d3ceef02a2dd3fabdf%2FAI%20search.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Enter a request in natural language, for example, show all critical and high issues for juice-shop.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-cb577327e0d6b00469d671865602fbb6b71c8a70%2FAI%20search_filters.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Review the filters the system applied for you, and adjust any filter if needed.
2. Run the search again.

## Example requests you can try

| Example request                                                     | What OX will look for                                                                 |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Show all critical and high issues                                   | Severity = Critical, High                                                             |
| Show all issues with improper authorization                         | Access control issues that match improper authorization                               |
| Show all issues with overprivileged access and cross-site scripting | Combined match for overprivileged access and XSS                                      |
| Show all issues with SLA due in the next 7 days                     | SLA due date within 7 days                                                            |
| Show issues that are reachable, exploitable, and high damage        | Severity factor combinations indicating reachability, exploitability, and high impact |
