# Source: https://docs.safetycli.com/safety-docs/output/output-options-and-recommendations.md

# Output Options and Recommendations

Safety can output the result of a vulnerability scan to a variety of different output formats.&#x20;

The default output is `screen` output, which prints the scan to the command line screen.

Use the `--output` argument to configure which output format Safety generates. The `--output` command line argument can be set to the following values: `screen`, `json`, `html`, `spdx`, `spdx@2.2`, `spdx@2.3`, `none`.

## Screen and text output

`--output screen` (default) will print the results to the screen

Results can be easily saved to a text file. For example:&#x20;

```
safety scan --output screen > results.txt
```

{% hint style="info" %}
For more detailed output, add the **`--detailed-output`** flag
{% endhint %}

If `--detailed-output`  is specified along with `--output json`  then CVE details will be included in the output. In order to filter the json output to only 1 top-level key, the `--filter`  option can be specified. For example:

`safety scan --detailed-output --output json --filter cve_details`

Other options that can be chosen to filter are: `meta`, `scan_results`

## Additional Output Options

Full details on each output option can be found here:

* [JSON](https://docs.safetycli.com/safety-docs/output/json-output)
* [SBOM](https://docs.safetycli.com/safety-docs/output/sbom-output) (SPDX, SPDX\@2.2, SPDX\@2.3)
* [HTML5](https://docs.safetycli.com/safety-docs/output/html-output)
