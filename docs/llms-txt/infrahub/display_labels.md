# Source: https://docs.infrahub.app/release-notes/deprecation-guides/display_labels.md

# How to migrate from display\_labels to display\_label

With Infrahub version 1.5, the `display_labels` configuration was deprecated in favor of a Jinja2-based `display_label` configuration that provides more flexibility and consistency.

This guide shows you how to update your schema files to use the new `display_label` syntax and remove the deprecated `display_labels` field.

Learn more about this change in the [release notes](https://github.com/opsmill/infrahub/releases).

info

This guide applies only to Infrahub instances that were migrated from a version prior to 1.5. If you're starting with Infrahub 1.5 or later, your schemas already use the new format.

## Step 1: Update display\_labels in schema files[​](#step-1-update-display_labels-in-schema-files "Direct link to Step 1: Update display_labels in schema files")

Find all `display_labels` occurrences in your schema files and replace them with the appropriate `display_label` (singular) configuration using Jinja2 syntax.

**Prompt for AI assisted refactoring**

Feel free to use this prompt with your preferred coding agent to handle the heavy lifting for the code refactoring.

```
# Task: Refactor display_labels to display_label in Schema YAML Files

## Context

We are migrating from the deprecated `display_labels` (list format) to the new `display_label` (Jinja2 template string format) across all Infrahub schema YAML files.

## Migration Rules

### 1. Basic Conversion

Convert list-based `display_labels` to a single Jinja2 template string:

**Before:**

display_labels:
  - name__value
  - tenant_id__value

**After:**

display_label: "{{ name__value }} ({{ tenant_id__value }})"

### 2. Relationship Support

The new format now supports relationships. If applicable you can add relationships in display label:

**Before:**

display_labels:
  - identifier__value

**After:**

display_label: "{{ identifier__value }} (Provider: {{ provider__name__value }})"

## Instructions

1. **Find all occurrences** of `display_labels` in infrahub schema YAML files
2. **Analyze the context** of each field list to determine appropriate formatting
3. **Convert to Jinja2 template** using these guidelines:
   - First field should be the primary identifier
   - Additional fields should be wrapped in parentheses with descriptive labels
   - Use human-readable labels (i.e., "Tenant ID:", "Provider:")
   - Maintain semantic meaning from the original field names
4. **Handle edge cases:**
   - Single-field `display_labels` → `display_label: "{{ field_name }}"`
   - Check for TODO comments indicating desired relationships
   - Preserve any important inline comments as separate comment lines
5. **Format consistently** across all files

## Notes

- The examples above are for illustration only - adapt the format to fit the semantic meaning of each schema
- Choose appropriate descriptive labels based on field names and context
- Ensure all Jinja2 templates are properly quoted
```

info

Here is for reference the PR that implements this migration in [schema-library](https://github.com/opsmill/schema-library): [PR #62](https://github.com/opsmill/schema-library/pull/62)

### Migration patterns[​](#migration-patterns "Direct link to Migration patterns")

#### Single attribute reference[​](#single-attribute-reference "Direct link to Single attribute reference")

**Before:**

```
display_labels:
  - name__value
```

**After:**

```
display_label: "{{ name__value }}"
```

#### Multiple attribute references[​](#multiple-attribute-references "Direct link to Multiple attribute references")

**Before:**

```
display_labels:
  - form_factor__value
  - sfp_type__value
```

**After:**

```
display_label: "{{ form_factor__value }} {{ sfp_type__value }}"
```

#### Using relationships[​](#using-relationships "Direct link to Using relationships")

The new format supports relationship traversal, enabling more descriptive display labels:

```
display_label: "{{ device__name__value }}>{{ name__value }}"
```

This example creates a display label that shows both the device name and interface name, separated by a `>` character.

## Step 2: Apply schema changes[​](#step-2-apply-schema-changes "Direct link to Step 2: Apply schema changes")

After updating your schema files, apply the changes to your Infrahub instance using one of the following methods:

If you're using Git integration to manage your schemas:

1. Commit your changes to a new branch
2. Push the branch to your Git repository
3. Infrahub will automatically detect and apply the schema updates

If you're managing schemas locally with `infrahubctl`:

1. Validate your schema changes:

   ```
   infrahubctl schema check path/to/your/schema/files
   ```

2. Load the updated schema:

   ```
   infrahubctl schema load path/to/your/schema/files
   ```

success

If the schema loads without errors and your objects display correctly, the migration is complete!

## Related resources[​](#related-resources "Direct link to Related resources")

* [Release notes for Infrahub 1.5](https://github.com/opsmill/infrahub/releases)
* [Schema topic](/topics/schema.md)
