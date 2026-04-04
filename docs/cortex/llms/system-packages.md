# Source: https://docs.cortexlabs.com/0.35/workloads/dependencies/system-packages.md

# Source: https://docs.cortexlabs.com/0.34/workloads/dependencies/system-packages.md

# Source: https://docs.cortexlabs.com/0.33/workloads/dependencies/system-packages.md

# Source: https://docs.cortexlabs.com/0.32/workloads/dependencies/system-packages.md

# Source: https://docs.cortexlabs.com/0.31/workloads/dependencies/system-packages.md

# Source: https://docs.cortexlabs.com/0.30/workloads/dependencies/system-packages.md

# Source: https://docs.cortexlabs.com/0.29/workloads/dependencies/system-packages.md

# Source: https://docs.cortexlabs.com/0.28/workloads/dependencies/system-packages.md

# System packages

Cortex looks for a file named `dependencies.sh` in the top level Cortex project directory (i.e. the directory which contains `cortex.yaml`). For example:

```
./my-classifier/
├── cortex.yaml
├── predictor.py
├── ...
└── dependencies.sh
```

`dependencies.sh` is executed with `bash` shell during the initialization of each replica (before installing Python packages in `requirements.txt` or `conda-packages.txt`). Typical use cases include installing required system packages to be used in your Predictor, building Python packages from source, etc.

Here is an example `dependencies.sh`, which installs the `tree` utility:

```bash
apt-get update && apt-get install -y tree
```

The `tree` utility can now be called inside your `predictor.py`:

```python
# predictor.py
import subprocess

class PythonPredictor:
    def __init__(self, config):
        subprocess.run(["tree"])
    ...
```
