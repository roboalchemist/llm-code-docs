# Source: https://docs.bito.ai/ai-code-reviews-in-git/supported-programming-languages-and-tools.md

# Supported programming languages and tools

## Supported Programming Languages

### AI Code Review

The [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) understands code changes in pull requests by analyzing relevant context from your entire repository, resulting in more accurate and helpful code reviews. The agent provides either **Basic Code Understanding** or **Advanced Code Understanding** based on the programming languages used in the code diff. Learn more about all the supported languages in the table below.

**Basic Code Understanding** is providing the surrounding code for the diff to help AI better understand the context of the diff.

**Advanced Code Understanding** is providing detailed information holistically to the LLM about the changes the diff is making—from things such as global variables, libraries, and frameworks (e.g., Lombok in Java, React for JS/TS, or Angular for TS) being used, the specific functions/methods and classes the diff is part of, to the upstream and downstream impact of a change being made. Using advanced code traversal and understanding techniques, such as symbol indexes, embeddings, and abstract syntax trees, Bito deeply tries to understand what your changes are about and the impact and relevance to the greater codebase, like a senior engineer does when doing code review. [**Read more here about our approach**](https://bito.ai/blog/how-does-bitos-ai-that-understands-your-code-work/).

{% hint style="info" %}
For requests to add support for specific programming languages, please reach out to us at <support@bito.ai>
{% endhint %}

|         Languages        | AI Code Review | Basic Code Understanding | Advanced Code Understanding |
| :----------------------: | :------------: | :----------------------: | :-------------------------: |
|       **Assembly**       |       YES      |            YES           |             YES             |
|      **Bash/Shell**      |       YES      |            YES           |             YES             |
|           **C**          |       YES      |            YES           |             YES             |
|          **C++**         |       YES      |            YES           |             YES             |
|          **C#**          |       YES      |            YES           |             YES             |
|         **Dart**         |       YES      |            YES           |             YES             |
|        **Delphi**        |       YES      |            YES           |             YES             |
|          **Go**          |       YES      |            YES           |             YES             |
|        **Groovy**        |       YES      |            YES           |             YES             |
|       **HTML/CSS**       |       YES      |            YES           |             YES             |
|         **Java**         |       YES      |            YES           |             YES             |
|      **JavaScript**      |       YES      |            YES           |             YES             |
| **JavaScript Framework** |       YES      |            YES           |             YES             |
|        **Kotlin**        |       YES      |            YES           |             YES             |
|          **Lua**         |       YES      |            YES           |             YES             |
|      **Objective-C**     |       YES      |            YES           |             YES             |
|          **PHP**         |       YES      |            YES           |             YES             |
|      **PowerShell**      |       YES      |            YES           |             YES             |
|        **Python**        |       YES      |            YES           |             YES             |
|           **R**          |       YES      |            YES           |             YES             |
|         **Ruby**         |       YES      |            YES           |             YES             |
|         **Rust**         |       YES      |            YES           |             YES             |
|         **Scala**        |       YES      |            YES           |             YES             |
|         **SCSS**         |       YES      |            YES           |             YES             |
|          **SQL**         |       YES      |            YES           |             YES             |
|         **Swift**        |       YES      |            YES           |             YES             |
|       **Terraform**      |       YES      |            YES           |             YES             |
|      **TypeScript**      |       YES      |            YES           |             YES             |
| **TypeScript Framework** |       YES      |            YES           |             YES             |
|        **Vue.js**        |       YES      |            YES           |             YES             |
|   **Visual Basic .NET**  |       YES      |            YES           |             YES             |
|        **Others**        |       YES      |            YES           |             YES             |

***

### Static Code Analysis and Open Source Vulnerabilities Check

For custom SAST tools configuration to support specific languages in the [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview), please reach out to us at <support@bito.ai>

|       Languages       |                        Static Code Analysis / Linters                        | Open Source Vulnerabilities Check |
| :-------------------: | :--------------------------------------------------------------------------: | :-------------------------------: |
|      **Assembly**     |                                      NO                                      |                 NO                |
|     **Bash/Shell**    |                                      NO                                      |                 NO                |
|         **C**         |             <p>YES<br>(using <strong>Facebook Infer</strong>)</p>            |                 NO                |
|        **C++**        |             <p>YES<br>(using <strong>Facebook Infer</strong>)</p>            |                 NO                |
|         **C#**        |                                      NO                                      |                 NO                |
|        **Dart**       |                                      NO                                      |                 NO                |
|       **Delphi**      |                                      NO                                      |                 NO                |
|         **Go**        |             <p>YES<br>(using <strong>golangci-lint</strong>)</p>             |                YES                |
|       **Groovy**      |                                      NO                                      |                 NO                |
|      **HTML/CSS**     |                                      NO                                      |                 NO                |
|        **Java**       |             <p>YES<br>(using <strong>Facebook Infer</strong>)</p>            |                 NO                |
|     **JavaScript**    |                 <p>YES<br>(using <strong>ESLint</strong>)</p>                |                YES                |
|       **Kotlin**      |                                      NO                                      |                 NO                |
|        **Lua**        |                                      NO                                      |                 NO                |
|    **Objective-C**    |             <p>YES<br>(using <strong>Facebook Infer</strong>)</p>            |                 NO                |
|        **PHP**        |                                      NO                                      |                 NO                |
|     **PowerShell**    |                                      NO                                      |                 NO                |
|       **Python**      | <p>YES<br>(using <strong>Astral Ruff</strong> and <strong>Mypy</strong>)</p> |                 NO                |
|         **R**         |                                      NO                                      |                 NO                |
|        **Ruby**       |                                      NO                                      |                 NO                |
|        **Rust**       |                                      NO                                      |                 NO                |
|       **Scala**       |                                      NO                                      |                 NO                |
|        **SCSS**       |                                      NO                                      |                 NO                |
|        **SQL**        |                                      NO                                      |                 NO                |
|       **Swift**       |                                      NO                                      |                 NO                |
|     **Terraform**     |                                      NO                                      |                 NO                |
|     **TypeScript**    |                 <p>YES<br>(using <strong>ESLint</strong>)</p>                |                YES                |
|       **Vue.js**      |                                      NO                                      |                 NO                |
| **Visual Basic .NET** |                                      NO                                      |                 NO                |
|       **Others**      |                                      NO                                      |                 NO                |

***

## Supported Tools and Platforms

|            Tool            |                                Type                                |          Supported/Integrated         |
| :------------------------: | :----------------------------------------------------------------: | :-----------------------------------: |
|       **Astral Ruff**      |                          Linter for Python                         |                  YES                  |
|      **Azure DevOps**      |                           Code Repository                          |              Coming soon              |
|        **Bitbucket**       |                           Code Repository                          |                  YES                  |
|     **detect-secrets**     | Secrets scanner (e.g., passwords, API keys, sensitive information) |                  YES                  |
|         **ESLint**         |                Linter for JavaScript and TypeScript                |                  YES                  |
|     **Facebook Infer**     |       Static Code Analysis for Java, C, C++, and Objective-C       |                  YES                  |
|      **GitHub cloud**      |                           Code Repository                          |                  YES                  |
|  **GitHub (Self-Managed)** |                           Code Repository                          |  YES, supports version 3.0 and above. |
|      **GitLab cloud**      |                           Code Repository                          |                  YES                  |
|  **GitLab (Self-Managed)** |                           Code Repository                          | YES, supports version 15.5 and above. |
|      **golangci-lint**     |                            Linter for Go                           |                  YES                  |
|          **Mypy**          |                   Static Type Checker for Python                   |                  YES                  |
| **OWASP dependency Check** |                              Security                              |                  YES                  |
|          **Snyk**          |                              Security                              |                  YES                  |
|        **Whispers**        | Secrets scanner (e.g., passwords, API keys, sensitive information) |                  YES                  |

***

## Supported output languages for code review feedback

Bito supports posting code review feedback in over 20 languages. You can choose your preferred language in the [agent settings](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance). Supported languages include the following:

1. Arabic (عربي)
2. Bulgarian (български)
3. Chinese (Simplified) (简体中文)
4. Chinese (Traditional) (繁體中文)
5. Czech (čeština)
6. Dutch (Nederlands)
7. English (English)
8. French (français)
9. German (Deutsch)
10. Hebrew (עִברִית)
11. Hindi (हिंदी)
12. Hungarian (magyar)
13. Italian (italiano)
14. Japanese (日本語)
15. Korean (한국어)
16. Malay (Melayu)
17. Polish (polski)
18. Portuguese (português)
19. Russian (русский)
20. Spanish (español)
21. Turkish (Türkçe)
22. Vietnamese (Tiếng Việt)
