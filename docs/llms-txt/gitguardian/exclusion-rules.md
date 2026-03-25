# Source: https://docs.gitguardian.com/secrets-detection/customize-detection/exclusion-rules.md

# Exclusion rules

> Configure filepath exclusions and secret pattern exclusions to reduce noise and focus secrets detection on relevant incidents.

## Filepath exclusions

By scanning your entire git history, or simply due to your software development activity, you could have many incidents on your GitGuardian dashboard. **Decreasing the number of incidents and focusing only on those that matter** most is therefore key. This feature only applies to secrets incidents.

### Description

In [your workspace settings, under the Secrets detection section](https://dashboard.gitguardian.com/settings/secrets/filepath-exclusions), you can **configure the filepaths you want to exclude from secrets detection**. You can link specific repositories to these excluded filepaths, ensuring that the exclusion only applies to those repositories.

When a secret is leaked on an excluded filepath:

- you will not receive any notification,
- no incident will be created in your dashboard.

Note that **newly created filepath exclusions will also apply to existing secret incidents** and these would therefore be removed from your secret incidents table.

![Filepath exclusion](/img/secrets-detection/customize-detection/filepath_exclusion.png)

You have the ability to test a filepath against your exclusion list to verify your configuration.

### Filepath format

The filepath format is a **subset of the glob-style pattern**. It uses the **â/â character to separate each element of the path (POSIX norm)**, and allows the **special â\*â character as a wildcard**. Additionally, the â\*\*â sequence can be used to recursively match any number of directories.

| PATTERN                  | CORRESPONDING REGEX       | MATCHES                                                         | NON-MATCHES                             |
| :----------------------- | :------------------------ | :-------------------------------------------------------------- | :-------------------------------------- |
| test.py           | `test\.py$`               | src/tests/test.py                                               | src/test/file.pysrc/test.py/README |
| tests/\*.py       | `tests/([^/]+)\.py$`      | src/tests/test.pysrc/tests/file.py                         | src/test.pysrc/test.txt            |
| /tests/\*.py      | `^tests/([^/]+)\.py$`     | tests/test.py                                                   | src/tests/test.py                       |
| /\*/test.py       | `^([^/]+)/test\.py$`      | src/test.py                                                     | test.pysrc/tests/test.py           |
| src/\*\*/test.py  | `src/([^/]+/)*test\.py$`  | src/test.pysrc/dir1/dir2/dir3/test.pydir1/src/test.py | dir1/dir2/dir3/test.py                  |
| /src/\*\*/test.py | `^src/([^/]+/)*test\.py$` | src/test.pysrc/dir1/dir2/dir3/test.py                      | dir1/src/test.py                        |
| \*\*/templates/   | `templates/`              | templates/file.htmlsrc/templates/file.html                 | src/file.html                           |

> If you misuse the glob-style pattern, GitGuardian will automatically correct your input. For instance:

- ``src/**/**/**/tests/`` will be corrected to ``src/**/test``
- ``**/src/**`` will be corrected to ``src/``

## Filepath suggestions

To focus on the most relevant secrets, here are some **suggested filepath exclusions**:

### Documentation and static content

Documentation files rarely contain secrets:

- `**/docs/**` - Documentation directories
- `**/README*` - README files
- `**/*.md` - Markdown files
- `**/*.rst` - reStructuredText files
- `**/CHANGELOG*` - Changelog files
- `**/LICENSE*` - License files

### Test and mock data

Test files may contain fake secrets that shouldn't trigger alerts:

- `**/test/**` - Test directories
- `**/tests/**` - Test directories alternative
- `**/*test*` - Files with 'test' in the name
- `**/mock/**` - Mock data directories
- `**/*.test.*` - Test files
- `**/*.spec.*` - Specification/test files

### Package manager files

Dependency files typically don't contain secrets:

- `**/package-lock.json` - npm lock file
- `**/yarn.lock` - Yarn lock file
- `**/Pipfile.lock` - Python Pipfile lock
- `**/poetry.lock` - Python Poetry lock file
- `**/Gemfile.lock` - Ruby Gemfile lock
- `**/go.sum` - Go modules checksum file

:::warning Review your exclusions
Always review your exclusions periodically to ensure they still align with your project structure and security requirements.
:::

## Secret pattern exclusion

### Description

In [your workspace settings, under the Secrets detection section](https://dashboard.gitguardian.com/settings/secrets/secret-pattern-exclusions), you can **configure the secret pattern you want to exclude from secrets detection**. You can link specific repositories to these excluded secret pattern, ensuring that the exclusion only applies to those repositories. The secret pattern you define must use the regular expression pattern.

When a secret pattern is triggered:

- you will not receive any notification,
- no incident will be created in your dashboard.

Note that **newly created secret pattern exclusions will also apply to existing secret incidents** and these would therefore be removed from your incidents table.

![Secret Pattern Exclusion](/img/secrets-detection/customize-detection/secret_pattern_exclusion.png)

You have the ability to test a secret pattern coverage.
