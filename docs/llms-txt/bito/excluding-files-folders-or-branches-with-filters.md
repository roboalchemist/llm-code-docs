# Source: https://docs.bito.ai/ai-code-reviews-in-git/excluding-files-folders-or-branches-with-filters.md

# Excluding files, folders, or branches with filters

The [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) offers powerful filters to exclude specific files and folders from code reviews and gives you precise control over which Git branches are included in automated reviews.

These filters can be configured at the Agent instance level, overriding the default behavior.

## Exclude Files and Folders filter

A list of files/folders that the AI Code Review Agent will not review if they are present in the diff. You can specify the files/folders to exclude from the review by name or glob/regex pattern. The Agent will automatically skip any files or folders that match the exclusion list.

This filter applies to both manual reviews initiated through the `/review` command and automated reviews triggered via webhook.

By default, these files are excluded: `*.xml`, `*.json`, `*.properties`, `.gitignore`, `*.yml`, `*.md`

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F8qrlYfC2AhUXtfITPKks%2Fscrnli_67LP18Ctwr8Zli.png?alt=media&#x26;token=91709f9b-b295-412e-8595-af17eac6cf53" alt=""><figcaption></figcaption></figure>

### Examples

{% hint style="info" %}
**Note:**

* Patterns are case sensitive.
* Don’t use double quotes, single quotes or comma in the pattern.
* Users can pass both types of patterns - Unix files system based glob pattern or regex.
  {% endhint %}

| Exclusion Rule for Files & Folders                                                                      | Applicable Pattern                       | Matched Examples                                                                                                                                 | Not Matched Examples                                                          |
| ------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| Exclude all properties files in all folders and subfolders                                              | `*.properties`                           | `resource/config.properties`, `resource/server/server.properties`                                                                                | `resource/config.yaml`, `resource/config.json`                                |
| Exclude all files, folders and subfolders in folder starting with `resources`                           | `resources/`                             | `resources/application.properties`, `resources/config/config.yaml`                                                                               | `app/resources/file.txt`, `config/resources/service.properties`               |
| Exclude all files, folders and subfolders in folder `src/com/resources`                                 | `src/com/resources/`                     | `resources/application.properties`, `resources/config/config.yaml`                                                                               | `app/resources/file.txt`, `config/resources/service.properties`               |
| Exclude all files, folders and subfolders in subfolder `resource` and in parent folder `src`            | `src/*/resource/*`                       | <p><code>src/com/resource/main.html</code>,</p><p><code>src/com/resource/script/file.css</code>, <code>src/com/resource/app/script.js</code></p> | `src/resource/file.txt`, `src/com/config/file.txt`, `app/com/config/file.txt` |
| Exclude non-css files from folder `src/com/resource/` and subfolders                                    | `^src\/com\/resource\\/(?!.*\\.css$).*$` | <p><code>src/com/resource/main.html, src/com/resource/app/script.js</code>, </p><p><code>src/com/config/file.txt</code></p>                      | `src/com/resource/script/file.css`                                            |
| Exclude specific file `controller/webhook_controller.go`                                                | `controller/webhook_controller.go`       | `controller/webhook_controller.go`                                                                                                               | `controller/controller.go`, `controller/webhook_service.go`                   |
| Exclude non-css files from folder starting with `config` and its subfolders                             | `^config\\/(?!.*\\.css$).*$`             | `config/server.yml`, `config/util/conf.properties`                                                                                               | `config/profile.css`, `config/styles/main.css`                                |
| Exclude all files & folders                                                                             | `*`                                      | `resource/file.txt`, `config/file.properties`, `app/folder/`                                                                                     | `-`                                                                           |
| Exclude all files & folders starting with name `bito` in `module` folder                                | `module/bito*`                           | `module/bito123`, `module/bitofile.js`, `module/bito/file.js`                                                                                    | `module/filebito.js`, `module/file2.txt`, `module/util/file.txt`              |
| Exclude single-character folder names                                                                   | `*/?/*`                                  | `src/a/file.txt`, `app/b/folder/file.yaml`                                                                                                       | `folder/file.txt`, `ab/folder/file.txt`                                       |
| Exclude all folders, subfolders and files in those folders except folder starting with `service` folder | `^(?!service\\/).*$`                     | `config/file.txt`, `resources/file.yaml`                                                                                                         | `service/file.txt`, `service/config/file.yaml`                                |
| Exclude all files in all folders except `.py`, `.go`, and `.java` files                                 | `^(?!.*\\.(py\|go\|java)$).*$`           | `config/file.txt`, `app/main.js`                                                                                                                 | `main.py`, `module/service.go`, `test/Example.java`                           |
| Exclude non-css files from folder `src/com/config` and its subfolders                                   | `^config\\/(?!.*\\.css$).*$`             | `config/server.yml`, `config/util/conf.properties`                                                                                               | `config/profile.css`, `config/styles/main.css`                                |

## Include Source/Target Branches filter

This filter defines which pull requests trigger automated reviews based on their source or target branch, allowing you to focus on critical code and avoid unnecessary reviews or AI usage.

By default, pull requests merging into the repository’s default branch are subject to review. To extend review coverage, additional branches may be specified using explicit branch names or valid glob/regex patterns. When the source or target branch of a pull request matches one of the patterns on your inclusion list, Bito’s AI Code Review Agent will trigger an automated review.

This filter applies only to automatically triggered reviews. Users should still be able to trigger reviews manually via the `/review` command.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F00UMeHuAITRMKGaBoZjO%2Fscrnli_P386e3Jr001VDd.png?alt=media&#x26;token=826ced85-028e-4317-852e-05ac8185a80b" alt=""><figcaption></figcaption></figure>

**Watch video tutorial:**

{% embed url="<https://youtu.be/31h8V-ip0J8>" %}

### Examples

{% hint style="info" %}
**Note:**

* Patterns are case sensitive.
* Don’t use double quotes, single quotes or comma in the pattern.
* Users can pass both types of patterns - Unix files system based glob pattern or regex.
  {% endhint %}

| Inclusion Rules for Branch                                                                                         | Pattern                                               | Matched Examples                                | Not Matched Examples                                |
| ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- | ----------------------------------------------- | --------------------------------------------------- |
| Include any branch that starts with name `BITO-`                                                                   | `BITO-*`                                              | `BITO-feature`, `BITO-123`                      | `feature-BITO`, `development`                       |
| Include any branch that does not start with `BITO-`                                                                | `^(?!BITO-).*`                                        | `feature-123`, `release-v1.0`                   | `BITO-feature`, `BITO-123`                          |
| Include any branch which is not `BITO`                                                                             | `^(?!BITO$).*`                                        | `feature-BITO`, `development`                   | `BITO`                                              |
| Include branches like `release/v1.0` and `release/v1.0.1`                                                          | `release/v\\d+\\.\\d+(\\.\\d+)?`                      | `release/v1.0`, `release/v1.0.1`                | `release/v1`, `release/v1.0.x`                      |
| Include any branch ending with `-test`                                                                             | `*-test`                                              | `feature-test`, `release-test`                  | `test-feature`, `release-testing`                   |
| Include the branch that has keyword `main`                                                                         | `main`                                                | `main`, `main-feature`, `mainline`              | `master`, `development`                             |
| Include the branch named `main`                                                                                    | `^main$`                                              | `main`                                          | `main-feature`, `mainline`, `master`, `development` |
| Include any branch name that does not start with `feature-` or `release-`                                          | `^(?!release-\|feature-).*$`                          | `hotfix-123`, `development`                     | `feature-123`, `release-v1.0`                       |
| Include branches with names containing digits                                                                      | `.*\\d+.*`                                            | `feature-123`, `release-v1.0`                   | `feature-abc`, `main`                               |
| Include branches with names ending with `test` or `testing`                                                        | `.*(test\|testing)$`                                  | `feature-test`, `bugfix-testing`                | `testing-feature`, `test-branch`                    |
| Include branches with names containing a specific substring `test`                                                 | `*test*`                                              | `feature-test`, `test-branch`, `testing`        | `feature`, `release`                                |
| Include branches with names containing exactly three characters                                                    | `^.{3}$`                                              | `abc`, `123`                                    | `abcd`, `ab`                                        |
| Include branch names starting with `release`, `hotfix`, or `development` but not starting with `Bito` or `feature` | `^(?!Bito\|feature)(release\|hotfix\|development).*$` | `release-v1.0`, `hotfix-123`, `development-xyz` | `Bito-release`, `feature-hotfix`, `main-release`    |
| Include all branches where name do not contains version like `1.0`, `1.0.1`, etc.                                  | `^(?!.\\b\\d+\\.\\d+(\\.\\d+)?\\b).*`                 | `feature-xyz`, `main`                           | `release-v1.0`, `hotfix-1.0.1`                      |
| Include all branches which are not alphanumeric                                                                    | `^.[^a-zA-Z0-9].$`                                    | `feature-!abc`, `release-@123`                  | `feature-123`, `release-v1.0`                       |
| Include all branches which contains space                                                                          | `.*\\s.*`                                             | `feature 123`, `release v1.0`                   | `feature-123`, `release-v1.0`                       |

## Draft pull requests filter

A binary setting that enables/disables automated review of pull requests (PR) based on the draft status. Enter `True` to disable automated review for draft pull requests, or `False` to enable it.

The default value is `True` which skips automated review of draft PR.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Feq4VAtW5pzAXmMb56Tkh%2Fscrnli_6lY6vx73F6U1U6.png?alt=media&#x26;token=34238de9-542e-490f-a9df-4d2daf762e21" alt=""><figcaption></figcaption></figure>

## How to configure the filters?

### Bito Cloud (Bito-hosted Agent)

You can configure filters using the Agent configuration page. For detailed instructions, please refer to the [**Install/run Using Bito Cloud**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud) documentation page.

### CLI or webhooks service (self-hosted Agent)

You can configure filters using the [**bito-cra.properties file**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/agent-configuration-bito-cra.properties-file). Check the options `exclude_branches`, `exclude_files`, and `exclude_draft_pr` for more details.

### GitHub Actions (self-hosted Agent)

You can configure filters using the GitHub Actions repository variables: `EXCLUDE_BRANCHES`, `EXCLUDE_FILES`, and `EXCLUDE_DRAFT_PR`. For detailed instructions, please refer to the [**Install/Run via GitHub Actions**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/install-run-via-github-actions) documentation page.
