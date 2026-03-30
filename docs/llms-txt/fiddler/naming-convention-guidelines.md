# Source: https://docs.fiddler.ai/developers/client-library-reference/naming-convention-guidelines.md

# Naming Convention Guidelines

## Core Fiddler Asset Naming Requirements

The following naming convention applies specifically to these core Fiddler platform assets: Projects, Models, Baselines, and Webhooks. Other elements in the platform may have different naming rules.

### Required Format

* Names must start with a lowercase letter (a-z)
* After the first character, names may contain:
  * Lowercase letters (a-z)
  * Numbers (0-9)
  * Underscores (\_)
* Names cannot contain uppercase letters, spaces, hyphens, or special characters
* Each asset type has specific length requirements:

| Fiddler Asset | Minimum Name Length | Maximum Name Length |
| ------------- | ------------------- | ------------------- |
| Baseline      | 3                   | 256                 |
| Model         | 2                   | 30                  |
| Project       | 2                   | 32                  |
| Webhook       | 2                   | 127                 |

### Examples

#### Valid Names

* `model_1`
* `test_project_2023`
* `prod_env`
* `my_baseline_123`

#### Invalid Names

* `Model1` (starts with uppercase)
* `1_model` (starts with a number)
* `test-project` (contains hyphen)
* `my feature` (contains space)
* `project#1` (contains special character)
* `m` (too short for any asset type)
* `_test` (starts with underscore)
* `extremely_long_name_that_exceeds_the_character_limit_for_models_and_projects` (exceeds length limits for Models, Projects, and Webhooks)

### Best Practices

While following the required format, we recommend these additional best practices:

* Use descriptive names that indicate the purpose or content
* Use underscores to separate words for better readability
* Keep names reasonably short while maintaining clarity
* Be consistent with naming patterns across similar items
* Consider using prefixes to group related assets (e.g., `prod_`, `dev_`, `test_`)

### Note on Other Platform Elements

This naming convention applies specifically to core Fiddler assets (Projects, Models, Baselines, and Webhooks). Other elements in the Fiddler platform may have different naming requirements or restrictions. Consult the specific documentation for those elements if needed.
