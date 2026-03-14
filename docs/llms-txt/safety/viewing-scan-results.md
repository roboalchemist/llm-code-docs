# Source: https://docs.safetycli.com/safety-docs/safety-cli/scanning-for-vulnerable-and-malicious-packages/viewing-scan-results.md

# Viewing Scan Results

## CLI Screen Output

When a **`safety scan`** is run, output will be displayed in the Terminal window. This output is split into the following sections:

1. **Scan Details:**&#x20;
   * Version of Safety installed
   * Project repository being scanned
   * Account details of the user performing the scan
   * Confirmation that Python has been detected and the number of requirements files detected in the current location.
2. **Dependency Vulnerabilities Detected**
   * Safety provides details on all dependencies detected during the scan, the number of vulnerabilities present in each, and detailed data about those vulnerabilities, including the Vulnerability ID and relevant CVE IDs.

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2F3PyTmxMV1nmp7jPLrHOO%2Fimage.png?alt=media&#x26;token=a6291f64-05de-4e8f-a623-d34eec10daeb" alt=""><figcaption><p>Safety CLI output showing vulnerabiities detected in a requirements file.</p></figcaption></figure>

3. **Recommendations**
   * For each vulnerability that has been detected, Safety will recommend that each be updated to a version in which the vulnerabilities have been fixed.&#x20;
   * A URL is provided, which can be copied and pasted into your browser to review additional information on each dependency, the vulnerabilities detected, and versions with the fix applied.

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FzDbDECfzfUyCQoMoIgGg%2Fimage.png?alt=media&#x26;token=3aa882ee-2080-4d46-909f-aa9e75215a63" alt=""><figcaption><p>Recommendations provided for each vulnerability detected in the previous step.</p></figcaption></figure>

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2Fj5ni2fIdNU1tdCwF7VVe%2Fimage.png?alt=media&#x26;token=ef51de11-2924-426a-b8b9-04b18aa1049e" alt=""><figcaption><p>Example of detailed changelogs for a package detected in the original scan using the URL provided.</p></figcaption></figure>

## Safety Platform

In addition to viewing output in the Terminal, all scan results are pushed to Safety Platform. Full details on how to view, interpret, and act upon Safety Platform information will be published as part of the Safety Platform documentation.&#x20;

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FSmDv4c6ZAfiISf45x1GH%2Fimage.png?alt=media&#x26;token=c37b4f40-ba1f-41dc-ad7e-7945399fb2f4" alt=""><figcaption></figcaption></figure>
