# Source: https://docs.safetycli.com/safety-docs/safety-cli/scanning-for-vulnerable-and-malicious-packages/exit-codes.md

# Exit Codes

Safety natively supports improved exit codes. It will return a zero (success) exit code for scans that find no vulnerabilities and non-zero exit codes for scans that find vulnerabilities or have other issues.

If you want to suppress non-zero exit codes for scans that find vulnerabilities, you can set this in your Safety policy file. To read more, please refer to the Safety Policy File documentation.
