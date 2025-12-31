# Source: https://docs.bito.ai/other-bito-ai-tools/bito-cli/available-commands.md

# Source: https://docs.bito.ai/ai-architect/available-commands.md

# Source: https://docs.bito.ai/ai-code-reviews-in-git/available-commands.md

# Source: https://docs.bito.ai/other-bito-ai-tools/bito-cli/available-commands.md

# Source: https://docs.bito.ai/ai-architect/available-commands.md

# Source: https://docs.bito.ai/ai-code-reviews-in-git/available-commands.md

# Available commands

The [**AI Code Review Agent**](https://docs.bito.ai/ai-code-reviews-in-git/overview) offers a suite of commands tailored to developers' needs. You can manually trigger a code review by entering any of these commands in the comment box below a pull/merge request on GitHub, GitLab, or Bitbucket and submitting the comment. Alternatively, if you are using the self-hosted version, you can configure these commands in the [**bito-cra.properties file**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/agent-configuration-bito-cra.properties-file) for automated code reviews.

{% hint style="info" %}
It may take a few minutes to get the code review posted as a comment, depending on the size of the pull/merge request.
{% endhint %}

## /review

This command provides a broad overview of your code changes, offering suggestions for improvement across various aspects but without diving deep for secure coding or performance optimizations or scalability improvements etc. This makes it ideal for catching general code quality issues that might not necessarily be critical blockers but can enhance readability, maintainability, and overall code health.

Think of it as a first-pass review to identify potential areas for improvement before delving into more specialized analyses.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FxlP180wDIuX69YbFO92n%2Fimage%20(9).png?alt=media&#x26;token=567f8c72-51aa-4682-8946-b540dc3258ec" alt=""><figcaption></figcaption></figure>

## Review Scope

Five specialized commands are available to perform detailed analyses on specific aspects of your code. Details for each command are given below.

1. `/review security`
2. `/review performance`
3. `/review scalability`
4. `/review codeorg`
5. `/review codeoptimize`

{% hint style="info" %}
You can provide comma-separated values to perform multiple types of code analysis simultaneously.

**Example:** `/review performance,security,codeoptimize`
{% endhint %}

### Combining general feedback with specialized review scopes

If you'd like to receive general code quality feedback alongside specialized analyses, include the `general` keyword in your review command.

For example, to receive feedback on general code quality, performance, and security, use:

* **Example:** `/review general,performance,security`

This ensures a holistic review encompassing both general code quality and specific areas of concern.

## /review security

This command performs an in-depth analysis of your code to identify vulnerabilities that could allow attackers to steal data, gain unauthorized access, or disrupt your application. This includes checking for weaknesses in input validation, output encoding, authentication, authorization, and session management. It also looks for proper encryption of sensitive data, secure coding practices, and potential misconfigurations that could expose your system.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fp7zoap8rRgTdWt8kqGxN%2Fscrnli_3_28_2024_2-59-52%20AM_1.png?alt=media&#x26;token=a4e78f8a-f0e6-4dcc-ba64-1e40a1cbea9b" alt=""><figcaption><p>Highlighting the security vulnerability detected and the proposed solution.</p></figcaption></figure>

## /review performance

This command evaluates the current performance of the code by pinpointing slow or resource-intensive areas and identifying potential bottlenecks. It helps developers understand where the code may be underperforming against expected benchmarks or standards. It is particularly useful for identifying slow processes that could benefit from further investigation and refinement.

This includes checking how well your code accesses data and manages tasks like database interactions and memory usage.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FoUbz3zRLYdIafoSro9AH%2Fscrnli_3_28_2024_3-05-21%20AM_2_1.png?alt=media&#x26;token=27535222-fdb7-4ce8-9d58-8ec4c2eede7d" alt=""><figcaption><p>Highlighting the performance issue detected and the proposed solution.</p></figcaption></figure>

## /review scalability

This command analyzes your code to identify potential roadblocks to handling increased usage or data. It checks how well the codebase supports horizontal scaling and whether it is compatible with load balancing strategies. It also ensures the code can handle concurrent requests efficiently and avoids bottlenecks from single points of failure. The command further examines error handling and retry mechanisms to promote system resilience under pressure.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FvDYzSi6S0qB9IymAJtji%2Fscrnli_3_28_2024_3-05-21%20AM_1_1.png?alt=media&#x26;token=d0668429-845b-44a8-868d-8addaff3da15" alt=""><figcaption><p>Highlighting the scalability issue detected and the proposed solution.</p></figcaption></figure>

## /review codeorg

This command scans your code for readability, maintainability, and overall clarity. This includes checking for consistent formatting, clear comments, well-defined functions, and efficient use of data structures. It also looks for opportunities to reduce code duplication, improve error handling, and ensure the code is written for future growth and maintainability.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FZXYio6wPTj0DsUxW8Uz0%2Fscrnli_3_28_2024_2-53-13%20AM_1.png?alt=media&#x26;token=ea6cdeb2-8b20-4c11-b48b-c049e7d9fd26" alt=""><figcaption><p>Highlighting the code structure issue detected and the proposed solution.</p></figcaption></figure>

## /review codeoptimize

This command helps identify specific parts of the code that can be made more efficient through optimization techniques. It suggests refactoring opportunities, algorithmic improvements, and areas where resource usage can be minimized. This command is essential for enhancing the overall efficiency of the code, making it faster and less resource-heavy.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FTKHJZ5xZ5ueLqlAVi7u8%2Fscrnli_3_28_2024_2-01-01%20AM_1.png?alt=media&#x26;token=27a7e6c0-77d7-4611-aabf-8eae284e635f" alt=""><figcaption><p>Precise code optimization advice pinpointing exact lines in a file.</p></figcaption></figure>

## Control code review workflow

These commands allow you to manage the AI Code Review Agent's behavior directly within your pull requests across GitHub, GitLab, and Bitbucket.

### /pause

Pauses automatic AI reviews on the current pull request.

**Use case:** Useful when significant changes are underway, and you want to prevent the AI from reviewing incomplete code.

**Example:** Add a comment with `/pause` to the pull request.

### /resume

Resumes the automatic AI reviews that were previously paused on the pull request.

**Use case:** Once your code changes are ready for review, use this command to re-enable the AI's automatic analysis.

**Example:** Add a comment with `/resume` to the pull request.

### /resolve

Marks all Bito-posted review comments as resolved.

**Use case:** After addressing the issues highlighted by the AI, use this command to clean up the comment threads.

**Example:** Add a comment with `/resolve` to the pull request.

{% hint style="info" %}
**Note:** The `/resolve` command is currently supported in GitLab and Bitbucket.
{% endhint %}

### /abort

Cancels all in-progress AI code reviews on the current pull request.

**Use case:** If an AI review is no longer needed or was initiated by mistake, this command stops the process.

**Example:** Add a comment with `/abort` to the pull request.

## Display Code Review in a Single Post

By default, the `/review` command generates inline comments, placing code suggestions directly beneath the corresponding lines in each file for clearer guidance on improvements. If you prefer a single consolidated code review instead of separate inline comments, use the `#inline_comment` parameter and set its value to `False`.

**Example:** `/review #inline_comment=False`

**Example:** `/review scalability #inline_comment=False`

{% hint style="info" %}
**Note:** The `/review` command defaults to `#inline_comment=True`, so you can omit this parameter when its value is `True`.
{% endhint %}
