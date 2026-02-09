# Source: https://docs.snyk.io/scan-with-snyk/import-project-repository/exclude-directories-and-files-from-project-import.md

# Exclude directories and files from Project import

Files are excluded from the retest and, therefore, are not tested by Snyk Code and do not appear in the Code Analysis results.If you import a Project through an SCM integration, add the exclusions, folders only, to the bottom of the import window.

<figure><img src="https://lh7-us.googleusercontent.com/stHVnzk1ZuP6oUm0zAImt0zROcajuZMm5iB4qX7vTbHkjPWklSgD9NxUdZ6UGgT1kV-dBjrcLyOp0SP1CqFzbNuq9S7qgl4cOD6T9UwuWlEk5SWVHUiHRlO-KfAyq_UppnGNvE67p7ZsSwuWok0_2RM" alt=""><figcaption><p>Exclude folders</p></figcaption></figure>

When you import a repository to be tested by Snyk Code, you can exclude certain directories and files from the import by using the `.snyk` file. The `.snyk` file is a YAML policy file that can contain shell matching patterns (regular expressions), which allow you to specify the directories and files you want to exclude from the import process. The `.snyk` file should be created in the repository you intend to import.

{% hint style="info" %}

* In Snyk Code, the `.snyk` file can only be used to exclude directories and files from import. It cannot be used to ignore vulnerabilities or for any other action, as in other Snyk products.
* Currently, the `exclude` option in the `.snyk` file applies only to the Snyk Web UI and CLI Environments. The `exclude` option cannot be used when working with Snyk Code in an IDE environment.
* In certain situations, your excluded files may not be excluded if there is an invalid `.snyk` file. In these situations, the scan continues without the `.snyk` file.
  {% endhint %}

{% hint style="info" %}
Consider excluding directories and files only if you do not publish or compile them into production. If a trace goes through an excluded file or directory with existing vulnerabilities, Snyk might miss potential issues.
{% endhint %}

You can also use the instructions in this section to exclude directories and files from the [Snyk Code CLI test](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-snyk-code/scan-source-code-with-snyk-code-using-the-cli), by creating the `.snyk` file in your tested repository.

## **Exclusion syntax of the .snyk file**

### Syntax to use to exclude files and directories from Snyk Code testing

Use the following syntax to exclude files and directories by using the `.snyk` file:

<pre class="language-yaml"><code class="lang-yaml"># Snyk (https://snyk.io) policy file
---
exclude:
    global:
<strong>        # Exclude a single file. For example, - test.spec.js
</strong>        - file_name.ext
<strong>        # Exclude a single directory. For example, - src/lib
</strong>        - source/directory_name
        # Exclude any file with a specific extension in the specific directory. For example, - tests/.js
<strong>        - directory_name/.ext
</strong>        # Exclude files with a specific ending in any directory. For example, - “*.spec.js”
        - "*.ending.ext"
        # Exclude files in directories that have the same name with a different ending, like “test” and “tests”. The last character before the question mark is optional. For example, - tests?/
        - directory_name?/
        # Exclude all files and directories located within any specified folder within your Project. For example, directory_name/** matches and excludes all contents under any directory named directory_name. It is not constrained to the root level or the location of the .snyk file.
<strong>        - directory_name/**
</strong></code></pre>

{% hint style="info" %}
You can use `global` or `code`. Either will exclude the specified directories and files from Snyk code tests. `code` applies only to Snyk Code analysis. `global` currently applies only to analysis using Snyk Code but may apply to other products in the future.
{% endhint %}

### **Considerations in creating the `.snyk` file**

* The path in the rule should be relative to the `.snyk` file location.
* Do not use paths starting with `./`.
* All rules must have a preceding dash to be valid: `- <exclusion_rule>`
* For rules beginning with special characters and patterns, such as an asterisk character `*`, you must wrap them in double quotes (`" "`). This ensures they are treated as a single entity, avoiding potential misinterpretation or unintended behavior. For example, `"*/src"`
* The following are considerations in using indentations:
  * When using the syntax in the `.snyk` YAML file, pay careful attention to new lines and their indentation. Using the wrong indentation will prevent the execution of your excluding specification.
  * Do NOT use tabs for indentation. Use only spaces for indentation.
  * To verify that you are using the syntax correctly, you can use a YAML Validator, like [YAML Lint](http://www.yamllint.com/). Be aware that some YAML Validators do not differentiate between the use of tabs and spaces for indentation. If you use tabs, a Validator may approve the syntax, but the exclude specifications will not be executed.
* For more information on the syntax of shell matching patterns, see, for example. the following:
  * GNU Org - [Shell Pattern Matching](https://www.gnu.org/software/findutils/manual/html_node/find_html/Shell-Pattern-Matching.html)
  * Docstore - [Pattern Matching Quick Reference with Examples](https://docstore.mik.ua/orelly/unix/upt/ch26_10.htm)

## **Use the `.snyk` file to exclude directories and files from import**

Follow these steps to exclude directories and files from the import process using the .`snyk` file:

1\. In the repository you want to import, create a YAML file called `.snyk`, for example:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-e26510d1618d3ac1d64aeab05e0c55dcd5530a75%2FSnyk%20Code%20-%20Exlude%20from%20Import%20-%20.snyk%20file%20creation%20-%202.png?alt=media" alt=".snyk file in a repository"><figcaption><p><code>.snyk</code> file in a repository.</p></figcaption></figure>

2\. In the `.snyk` file, specify the directories or files or both that you want to exclude from import according to the following syntax:

```yaml
# Snyk (https://snyk.io) policy file
exclude:
 global:
   - <Exclusion_rule>
   - <Exclusion_rule>
```

For example:

```yaml
# Snyk (https://snyk.io) policy file
exclude:
 global:
   - todolist-goof/** 
```

3\. From the Snyk Web UI, import your repository in one of the following ways:

* If the repository was already imported to Snyk, retest the repository as follows:

  On the **Projects** page, click the **Code analysis** Project of the repository. Then, on the **Code Analysis** page, click **Retest now.**

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-6941359ecbbcbb64add59e10c24db092bb59942c%2Fcode_analysis_retest_now.png?alt=media" alt="Clicking the retest now option"><figcaption><p>Retest now option</p></figcaption></figure>

* If the repository was not imported yet to Snyk, [import the repository](https://docs.snyk.io/scan-with-snyk/snyk-code/import-project-with-snyk-code).

Your repository is imported to Snyk, without the directories and/or files you selected to exclude.

## **Example**: **Excluding two files from Snyk Code analysis**

You have a repository called `snyk-goof`, which you want to test for vulnerabilities using Snyk Code. After you import his repository to Snyk, you get a list of ten detected vulnerability issues, which were found in three files:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-51266574d2ff89e60074286dbf08e5c34ce9a8b9%2FSnyk%20Code%20-%20Exlude%20from%20Import%20-%20Example%20-%20Before%20Exclude.png?alt=media" alt=""><figcaption><p>Vulnerabilities detected found in three files</p></figcaption></figure>

Now you want to exclude the `app.js` and `db.js` files from the Snyk Code analysis. To achieve that, you do the following:

1\. You create a `.snyk` file in the **snyk-goof** repository in GitHub:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-adf681657ea8b2036acda7b0e5d27e5bed6ba2d7%2FSnyk%20Code%20-%20Exlude%20from%20Import%20-%20Example%20-%20.snyk%20file%20creation.png?alt=media" alt=".snyk file in snyk-goof repository"><figcaption><p><code>.snyk</code> file in snyk-goof repository</p></figcaption></figure>

2\. In the `.snyk` file, you enter the following commands to exclude the `app.js` and `db.js` files from the import:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-fab2cc3ad0f7f113f4a28bf79a1055bdaad14121%2FSnyk%20Code%20-%20Exlude%20from%20Import%20-%20Example%20-%20Command.png?alt=media" alt=".snyk file commands"><figcaption><p><code>.snyk</code> file commands</p></figcaption></figure>

3\. You retest the "snyk-goof" repository by clicking **Retest now** on the **Code Analysis** page for the repository.

The `app.js` and `db.js` files are excluded from the retest and, therefore, are not tested by Snyk Code and do not appear in the Code Analysis results. Now, only five vulnerability issues are detected:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-cc2400e19cbea5e09333cfebcf4fd44c679da7b0%2Fimage%20(545).png?alt=media&#x26;token=5dcc200b-24ec-47cb-93d9-f70bf37f67b7" alt="Example of issues detected in files after excluding"><figcaption><p>Detected issues after files have been excluded</p></figcaption></figure>
