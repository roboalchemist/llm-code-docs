# Source: https://docs.baseten.co/reference/cli/truss/run-python.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# truss run-python

> Run a Python script in the Truss environment.

```sh  theme={"system"}
truss run-python [OPTIONS] SCRIPT [TARGET_DIRECTORY]
```

Runs a Python script in the same environment as your Truss. This builds a Docker
image matching your Truss environment, mounts the script, and executes it. Use
this to test scripts with the same dependencies your model uses.

### Arguments

<ParamField body="SCRIPT" type="PATH" required>
  Path to the Python script to run.
</ParamField>

<ParamField body="TARGET_DIRECTORY" type="TEXT">
  A Truss directory. Defaults to current directory.
</ParamField>

**Example:**

To run a script in the Truss environment, use the following:

```sh  theme={"system"}
truss run-python test_script.py
```

To run a script with a specific Truss directory, use the following:

```sh  theme={"system"}
truss run-python test_script.py /path/to/my-truss
```
