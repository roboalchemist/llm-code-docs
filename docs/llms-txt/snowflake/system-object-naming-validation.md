# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/getting-started/running-snowconvert/validation/system-object-naming-validation.md

# SnowConvert AI - System Object Naming Validation

## Description

This validation step verifies the files and folder names that contain reserved words. These files and folders are marked as invalid or out of scope because they can potentially be built-in systems definitions that must be removed from the migration scope. When this behavior happens, the following warning is displayed:

Also, in the ScopeValidation report, you will find information about the failed file(s).
