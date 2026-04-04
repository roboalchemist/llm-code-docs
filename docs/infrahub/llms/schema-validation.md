# Source: https://docs.infrahub.app/reference/schema-validation.md

# Source: https://docs.infrahub.app/vscode/topics/schema-validation.md

# Schema Validation and YAML Intelligence

This document explores how the Infrahub VSCode extension provides intelligent YAML editing capabilities, real-time schema validation, and navigation features that enhance the developer experience when working with infrastructure schemas.

## Overview[​](#overview "Direct link to Overview")

Schema validation and YAML intelligence are fundamental features that transform VSCode into a powerful Infrahub development environment. These capabilities help catch errors early, provide contextual assistance, and accelerate schema development through intelligent code completion and navigation.

## The Role of Schemas in Infrahub[​](#the-role-of-schemas-in-infrahub "Direct link to The Role of Schemas in Infrahub")

### Infrastructure as Schema[​](#infrastructure-as-schema "Direct link to Infrastructure as Schema")

In Infrahub, schemas define the structure of your infrastructure data:

```
version: '1.0'
nodes:
  - name: Device
    namespace: Network
    attributes:
      - name: hostname
        kind: Text
        unique: true
```

This schema-first approach means:

* **Type Safety**: Data must conform to defined structures
* **Consistency**: All infrastructure follows the same patterns
* **Validation**: Invalid data is rejected before it causes issues
* **Documentation**: Schemas serve as living documentation

### Why Validation Matters[​](#why-validation-matters "Direct link to Why Validation Matters")

Schema validation prevents several categories of errors:

1. **Syntax Errors**: Malformed YAML that won't parse
2. **Type Mismatches**: Wrong data types for attributes
3. **Constraint Violations**: Breaking uniqueness or required fields
4. **Relationship Errors**: Invalid references between objects
5. **Version Conflicts**: Incompatible schema versions

## How Schema Validation Works[​](#how-schema-validation-works "Direct link to How Schema Validation Works")

### Validation Pipeline[​](#validation-pipeline "Direct link to Validation Pipeline")

The extension implements a multi-stage validation pipeline:

```
File Change → YAML Parse → Schema Load → Validation → Diagnostics
     ↓            ↓            ↓            ↓            ↓
  Detected    Structure    Reference    Rules      Display
             Checking     Resolution   Applied     Errors
```

### Real-Time Validation[​](#real-time-validation "Direct link to Real-Time Validation")

Validation occurs at multiple points:

1. **On Type**: Incremental validation as you type (debounced)
2. **On Save**: Full validation when file is saved
3. **On Open**: Initial validation when file is opened
4. **On Focus**: Re-validation when switching between files

### Validation Scope[​](#validation-scope "Direct link to Validation Scope")

The extension validates files based on location:

```
# Automatically validated directories
models/        # Infrastructure models
schemas/       # Schema definitions
```

These directories are configured through:

```
{
  "infrahub-vscode.schemaDirectory": "schemas"
}
```

## YAML Intelligence Features[​](#yaml-intelligence-features "Direct link to YAML Intelligence Features")

### Syntax Highlighting[​](#syntax-highlighting "Direct link to Syntax Highlighting")

The extension provides enhanced syntax highlighting for Infrahub-specific constructs:

* **Keywords**: `version`, `nodes`, `attributes`, `relationships`
* **Types**: `Text`, `Number`, `Boolean`, `IPHost`, `IPNetwork`
* **Modifiers**: `unique`, `optional`, `default_value`

### Auto-Completion[​](#auto-completion "Direct link to Auto-Completion")

Context-aware suggestions appear as you type:

```
nodes:
  - name: Router
    attributes:
      - name: hostname
        kind: |  # Cursor here triggers type suggestions
              # Text, Number, Boolean, IPHost, etc.
```

### Go-to-Definition[​](#go-to-definition "Direct link to Go-to-Definition")

Navigate between related schemas with `F12` or `Ctrl+Click`:

```
relationships:
  - name: interfaces
    peer: NetworkInterface  # Ctrl+Click jumps to NetworkInterface definition
    kind: Component
```

### Document Symbols[​](#document-symbols "Direct link to Document Symbols")

The outline view shows schema structure:

```
📄 network.yml
  └─ nodes
      └─ Device
          ├─ attributes
          │   ├─ hostname
          │   └─ model
          └─ relationships
              └─ interfaces
```

## Schema Validation Rules[​](#schema-validation-rules "Direct link to Schema Validation Rules")

### Structural Validation[​](#structural-validation "Direct link to Structural Validation")

The extension enforces schema structure:

```
# Valid structure
version: '1.0'
nodes:
  - name: Device
    namespace: Network

# Invalid - missing version
nodes:  # ❌ Error: Schema must include version
  - name: Device
```

### Attribute Validation[​](#attribute-validation "Direct link to Attribute Validation")

Attributes must follow specific rules:

```
attributes:
  - name: hostname
    kind: Text        # ✅ Valid kind
    unique: true      # ✅ Valid modifier
    
  - name: port
    kind: String      # ❌ Error: Invalid kind 'String', use 'Text'
    
  - name: ip_address
    kind: IPHost
    mandatory: true   # ❌ Error: Use 'optional: false' instead
```

### Relationship Validation[​](#relationship-validation "Direct link to Relationship Validation")

Relationships are validated for consistency:

```
relationships:
  - name: location
    peer: LocationSite    # Must reference existing node
    kind: Parent         # Must be valid relationship kind
    cardinality: one     # Must be valid cardinality
    
  - name: interfaces
    peer: NonExistent    # ❌ Error: Node 'NonExistent' not found
    kind: Invalid        # ❌ Error: Invalid relationship kind
```

## Understanding Validation Messages[​](#understanding-validation-messages "Direct link to Understanding Validation Messages")

### Error Categories[​](#error-categories "Direct link to Error Categories")

Validation produces different message types:

1. **Errors** (Red): Must be fixed before schema works

   * Missing required fields
   * Invalid types
   * Syntax errors

2. **Warnings** (Yellow): Should be addressed but won't break functionality

   * Deprecated patterns
   * Performance concerns
   * Best practice violations

3. **Information** (Blue): Helpful suggestions

   * Optimization opportunities
   * Alternative approaches
   * Documentation hints

### Message Structure[​](#message-structure "Direct link to Message Structure")

Each validation message contains:

```
[Severity] [Location] Message
Example: Error at line 15: Attribute kind 'String' is not valid
```

### Common Validation Errors[​](#common-validation-errors "Direct link to Common Validation Errors")

#### Missing Required Fields[​](#missing-required-fields "Direct link to Missing Required Fields")

```
nodes:
  - namespace: Network  # ❌ Error: Missing required field 'name'
```

**Solution**: Add the missing field:

```
nodes:
  - name: Device
    namespace: Network
```

#### Invalid Attribute Kind[​](#invalid-attribute-kind "Direct link to Invalid Attribute Kind")

```
attributes:
  - name: count
    kind: Integer  # ❌ Error: Use 'Number' instead of 'Integer'
```

**Solution**: Use correct type:

```
attributes:
  - name: count
    kind: Number
```

#### Circular Dependencies[​](#circular-dependencies "Direct link to Circular Dependencies")

```
nodes:
  - name: A
    relationships:
      - peer: B
        kind: Parent
  - name: B
    relationships:
      - peer: A
        kind: Parent  # ❌ Error: Circular dependency detected
```

**Solution**: Redesign relationship hierarchy

## Advanced Validation Concepts[​](#advanced-validation-concepts "Direct link to Advanced Validation Concepts")

### Schema Inheritance[​](#schema-inheritance "Direct link to Schema Inheritance")

Understanding how schemas inherit from base definitions:

```
nodes:
  - name: Device
    namespace: Network
    inherit_from:
      - BuiltinDevice  # Inherits attributes and relationships
    attributes:
      - name: custom_field  # Adds to inherited attributes
        kind: Text
```

The validator checks:

* Base schema exists
* No attribute conflicts
* Relationship compatibility

### Cross-File Validation[​](#cross-file-validation "Direct link to Cross-File Validation")

The extension validates references across files:

```
# File: schemas/network.yml
nodes:
  - name: Device
    namespace: Network

# File: schemas/interface.yml
nodes:
  - name: Interface
    namespace: Network
    relationships:
      - name: device
        peer: NetworkDevice  # Validated across files
```

### Version Compatibility[​](#version-compatibility "Direct link to Version Compatibility")

Schema versions affect validation rules:

```
version: '1.0'  # Original schema format

version: '1.1'  # Supports additional features
generics:       # New in 1.1
  - name: GenericDevice
```

## Performance Considerations[​](#performance-considerations "Direct link to Performance Considerations")

### Incremental Validation[​](#incremental-validation "Direct link to Incremental Validation")

The extension uses incremental validation for performance:

1. **Parse Caching**: YAML AST cached between edits
2. **Partial Updates**: Only changed sections re-validated
3. **Debouncing**: Validation delayed during rapid typing
4. **Background Processing**: Validation doesn't block UI

### Large File Handling[​](#large-file-handling "Direct link to Large File Handling")

For large schema files:

* **Lazy Loading**: Schemas loaded on-demand
* **Chunked Processing**: Large files processed in segments
* **Priority Validation**: Visible content validated first
* **Throttling**: Rate-limited validation for huge files

## Customizing Validation[​](#customizing-validation "Direct link to Customizing Validation")

### Validation Settings[​](#validation-settings "Direct link to Validation Settings")

Configure validation behavior:

```
{
  "yaml.schemas": {
    "https://schema.infrahub.app/infrahub/schema/latest.json": [
      "schemas/**/*.yml",
      "models/**/*.yaml"
    ]
  },
  "yaml.validate": true,
  "yaml.customTags": [
    "!include",
    "!secret"
  ]
}
```

### Disabling Validation[​](#disabling-validation "Direct link to Disabling Validation")

To temporarily disable validation:

1. **Per File**: Add comment at top

   ```
   # yaml-language-server: $schema=none
   ```

2. **Per Workspace**: Modify settings

   ```
   {
     "yaml.validate": false
   }
   ```

## Integration with Other Tools[​](#integration-with-other-tools "Direct link to Integration with Other Tools")

### YAML Language Server[​](#yaml-language-server "Direct link to YAML Language Server")

The extension leverages the Red Hat YAML extension:

* **Schema Association**: Links files to Infrahub schemas
* **JSON Schema**: Uses JSON Schema for validation
* **Custom Tags**: Supports Infrahub-specific tags

### Linting Integration[​](#linting-integration "Direct link to Linting Integration")

Works alongside linting tools:

* **yamllint**: Style and formatting checks
* **Prettier**: Code formatting
* **Vale**: Documentation linting

## Troubleshooting Validation Issues[​](#troubleshooting-validation-issues "Direct link to Troubleshooting Validation Issues")

### Validation Not Working[​](#validation-not-working "Direct link to Validation Not Working")

If validation isn't functioning:

1. **Check File Location**: Ensure file is in configured directory
2. **Verify Extension**: Confirm YAML extension is installed
3. **Schema Association**: Check schema URL is correct
4. **Reload Window**: Try reloading VSCode

### False Positives[​](#false-positives "Direct link to False Positives")

If seeing incorrect errors:

1. **Update Extension**: Ensure latest version
2. **Check Schema Version**: Verify schema compatibility
3. **Clear Cache**: Reload VSCode window
4. **Report Issue**: File bug report if persistent

### Performance Issues[​](#performance-issues "Direct link to Performance Issues")

If validation is slow:

1. **File Size**: Consider splitting large files
2. **Disable Real-time**: Turn off on-type validation
3. **Increase Debounce**: Adjust validation delay
4. **Check Extensions**: Disable conflicting extensions

## Further Reading[​](#further-reading "Direct link to Further Reading")

* [Understanding the Extension Architecture](/vscode/topics/extension-architecture.md)
* [How to Execute GraphQL Queries](/vscode/guides/execute-graphql-queries.md)
* [Extension Commands Reference](/vscode/reference/commands-settings.md)
