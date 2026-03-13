# Source: https://docs.safetycli.com/safety-docs/output/json-output.md

# JSON Output

Safety can generate JSON output, useful for parsing and analyzing the results of a scan. To do so, run the following command.

```
safety scan --output json
```

The JSON output is displayed in the terminal, as shown below. To save the JSON output to a file, use the following command, replacint `test.json` with your desired file name.

```
safety scan --output json >test.json
```

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FNZswLatSEzLQwd9qmEn9%2Fimage.png?alt=media&#x26;token=bab4b723-418a-4d9a-9ced-a92e3d1c7d9a" alt=""><figcaption></figcaption></figure>

### JSON structure

The resulting output is a JSON with the following sections:

`meta` contains meta information about the scan, such as timestamps, what was scanned, packages found and vulnerabilities found

`scanned_packages` is an array of packages (and versions) that were found during the scan

`affected_packages` is an array of packages that were found to have relevant vulnerabilities

`vulnerabilities` is an array of vulnerabilities that were found relating to the packages in the scan

`ignored_vulnerabilities` is an array of vulnerabilities that were found but were ignored via a command line argument or the safety policy file.

`remediations` an array of remediation (fix) recommendations for each package with relevant vulnerabilities.

`announcements` an array of announcements (messages) from the Safety team. These are not generally related to the packages of vulnerabilities found, but rather are more general announcements, such as announcing a new version of the Safety scanner.
