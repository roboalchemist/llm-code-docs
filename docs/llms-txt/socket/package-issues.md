# Source: https://docs.socket.dev/docs/package-issues.md

# Alert Categories

How package issues are categorized by Socket

Socket detects [80+ dependency risks](https://socket.dev/alerts) divided over the following set of categories:

## Supply chain risk

| Severity | Description                                                                                                                                                                                                                                                                                                                                    |
| :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Critical | Package contains a critical supply chain risk that makes it unsuitable for use in most applications. This category is reserved for [known malware](https://socket.dev/npm/issue/malware), [typosquats](https://socket.dev/npm/issue/didYouMean), [HTTP dependencies](https://socket.dev/npm/issue/httpDependency), and other critical threats. |
| High     | Package contains a supply chain risk that makes it unsafe to use in most applications *until a manual inspection has been performed to confirm that the package is safe*.                                                                                                                                                                      |
| Medium   | Package contains a medium-risk supply chain security issue. Critical applications in areas such as finance, health, regulated industries, should manually inspect medium-risk issues.                                                                                                                                                          |
| Low      | Package contains a low-risk supply chain security issue.                                                                                                                                                                                                                                                                                       |

## Quality

| Severity | Description                                                                                                                                                                                                                                                                                                               |
| :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Critical | Package has critical quality issues that make it unsuitable for use in all applications. Examples include an [invalid package.json](https://socket.dev/npm/issue/invalidPackageJSON) which fails to parse, or [unresolved requires](https://socket.dev/npm/issue/unresolvedRequire) which import files that do not exist. |
| High     | Package contains a high-risk quality issue.                                                                                                                                                                                                                                                                               |
| Medium   | Package contains a medium-risk quality issue.                                                                                                                                                                                                                                                                             |
| Low      | Package contains a low-risk quality issue.                                                                                                                                                                                                                                                                                |

## Maintenance

| Severity | Description                                                                                  |
| :------- | :------------------------------------------------------------------------------------------- |
| Critical | Package has critical maintenance issues that make it unsuitable for use in all applications. |
| High     | Package contains a high-risk maintenance issue.                                              |
| Medium   | Package contains a medium-risk maintenance issue.                                            |
| Low      | Package contains a low-risk maintenance issue.                                               |

## Vulnerability

| Severity | Description                                                                                                                             |
| :------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| Critical | Package contains a critical CVE that makes it unsuitable for use in all applications. You should update to a fixed version immediately. |
| High     | Package contains a high-risk CVE. You should update to a fixed version as soon as reasonably possible.                                  |
| Medium   | Package contains a medium-risk CVE.                                                                                                     |
| Low      | Package contains a low-risk CVE.                                                                                                        |

## License

| Severity | Description                                                                                                                                                                                                          |
| :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Critical | Package has a critical license issue that makes it unsuitable for use in most applications. Package should immediately be replaced with a different one to avoid significant legal risk.                             |
| High     | Package has a license issue that makes it a risk for use in most commercial applications. Package should be examined by a legal expert, or additional license metadata added to the package to make it safe for use. |
| Medium   | Package contains a medium-risk license issue.                                                                                                                                                                        |
| Low      | Package contains a low-risk license issue.                                                                                                                                                                           |