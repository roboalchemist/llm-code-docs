# Source: https://docs.snowflake.com/en/sql-reference/functions/system_resolve_python_packages.md

Categories:
:   [System functions](../functions-system.md) (System functions)

# SYSTEM$RESOLVE_PYTHON_PACKAGES

Returns a list of the resolved dependencies and their versions for the Python packages that were specified.
This function works with packages from both Anaconda and Artifact Repository (PyPI).

## Syntax

```sqlsyntax
SYSTEM$RESOLVE_PYTHON_PACKAGES( '<python_version>', '<package_spec_string>', ['<artifact_repository_name>'] )
```

## Arguments

`python_version`
:   String specifying the version of the Python runtime (e.g., ‘3.12’).

`package_spec_string`
:   Package specifications in PACKAGES clause format (e.g., `$$('numpy>=1.20.0', 'pandas==1.3.0')$$`).
    Use `$$()$$` to return only base packages (Python runtime and its dependencies).

`artifact_repository_name`
:   Optional. String specifying the artifact repository name (e.g., ‘snowflake.snowpark.pypi_shared_repository’).
    If not provided or empty, uses the default Anaconda repository.

## Returns

Returns a JSON array that contains the resolved packages and their dependencies.
Each element in the array is a string in the following format: `<package_name>==<version_name>`.
The result always includes base packages (e.g., Python runtime and system libraries).

## Access control requirements

This function can be called by any user. No special privileges are required.

## Usage notes

* Unlike [SHOW_PYTHON_PACKAGES_DEPENDENCIES](show_python_packages_dependencies.md), which only works with Anaconda packages,
  `SYSTEM$RESOLVE_PYTHON_PACKAGES` works with packages from both Anaconda and Artifact Repository (PyPI).
* The function creates a temporary UDF internally to resolve package dependencies and automatically cleans it up.
* Use this function when you need to determine all dependencies for packages that will be included in a packages policy.

## Examples

**Example 1: Resolve packages from Anaconda**

The following example returns a list of the dependencies of the `numpy` and `pandas` Python packages
with the Python 3.12 runtime from the default Anaconda repository:

```sqlexample
SELECT SYSTEM$RESOLVE_PYTHON_PACKAGES('3.12', $$('numpy>=1.20.0', 'pandas==1.3.0')$$);
```

The result is a list of the dependencies and their versions:

```output
["_libgcc_mutex==0.1", "_openmp_mutex==5.1", "blas==1.0", "ca-certificates==2024.9.24",
"intel-openmp==2023.1.0", "libffi==3.4.4", "libgcc-ng==11.2.0", "numpy==1.24.3",
"pandas==1.5.3", "python==3.12.20", "readline==8.2", "sqlite==3.45.3", ...]
```

**Example 2: Resolve packages from Artifact Repository (PyPI)**

The following example resolves the `scikit-learn` package from a PyPI artifact repository:

```sqlexample
SELECT SYSTEM$RESOLVE_PYTHON_PACKAGES('3.12', $$('scikit-learn')$$, 'snowflake.snowpark.pypi_shared_repository');
```

**Example 3: Get base packages only**

The following example returns only the base packages for Python 3.12:

```sqlexample
SELECT SYSTEM$RESOLVE_PYTHON_PACKAGES('3.12', $$()$$);
```

The result contains the Python runtime and system dependencies:

```output
["_libgcc_mutex==0.1", "ca-certificates==2024.9.24", "libffi==3.4.4",
"openssl==3.0.15", "python==3.12.20", "readline==8.2", ...]
```

## See also

* [SHOW_PYTHON_PACKAGES_DEPENDENCIES](show_python_packages_dependencies.md) - Returns dependencies for Anaconda packages only (requires ACCOUNTADMIN role)
* [Packages policies](../../developer-guide/udf/python/packages-policy.md) - Packages policies for Python
* [Using third-party packages](../../developer-guide/udf/python/udf-python-packages.md) - Using Python packages in UDFs
