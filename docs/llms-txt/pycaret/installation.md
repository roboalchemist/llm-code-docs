# Source: https://pycaret.gitbook.io/docs/get-started/installation.md

# Installation

## Option 1: Install via PyPi

PyCaret is tested and supported on 64-bit systems with:

* Python 3.8, 3.9, 3.10, and 3.11
* Ubuntu 16.04 or later
* Windows 7 or later

You can install PyCaret with Python's pip package manager:

{% code lineNumbers="true" %}

```bash
pip install pycaret
```

{% endcode %}

PyCaret's default installation will not install all the optional dependencies automatically. Depending on the use case, you may be interested in one or more extras:

```bash
# install analysis extras
pip install pycaret[analysis]

# models extras
pip install pycaret[models]

# install tuner extras
pip install pycaret[tuner]

# install mlops extras
pip install pycaret[mlops]

# install parallel extras
pip install pycaret[parallel]

# install test extras
pip install pycaret[test]

## 

# install multiple extras together
pip install pycaret[analysis,models]

```

Check out all [optional dependencies](https://github.com/pycaret/pycaret/blob/master/requirements-optional.txt). If you want to install everything including all the optional dependencies:

{% code lineNumbers="true" %}

```bash
# install full version
pip install pycaret[full]
```

{% endcode %}

## Option 2: Source

Install the development version of the library directly from the source. The API may be unstable. It is not recommended for production use.&#x20;

{% code lineNumbers="true" %}

```bash
pip install git+https://github.com/pycaret/pycaret.git@master --upgrade
```

{% endcode %}

## Option 3: Docker

Docker creates virtual environments with containers that keep a PyCaret installation separate from the rest of the system. PyCaret docker comes pre-installed with a Jupyter notebook. It can share resources with its host machine (access directories, use the GPU, connect to the Internet, etc.). The PyCaret Docker images are always tested for the latest major releases.

{% code lineNumbers="true" %}

```bash
# default version
docker run -p 8888:8888 pycaret/slim

# full version
docker run -p 8888:8888 pycaret/full
```

{% endcode %}

To learn more, check out the Docker page for [pycaret/slim](https://hub.docker.com/r/pycaret/slim) or [pycaret/full](https://hub.docker.com/r/pycaret/full).

## Environment

In order to avoid potential conflicts with other packages, it is strongly recommended to use a virtual environment, e.g. python3 virtualenv (see [python3 virtualenv documentation](https://docs.python.org/3/tutorial/venv.html)) or [conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). Using an isolated environment makes it possible to install a specific version of pycaret and its dependencies independently of any previously installed Python packages.&#x20;

{% code lineNumbers="true" %}

```bash
# create a conda environment
conda create --name yourenvname python=3.8

# activate conda environment
conda activate yourenvname

# install pycaret
pip install pycaret

# create notebook kernel
python -m ipykernel install --user --name yourenvname --display-name "display-name"
```

{% endcode %}

## Training on GPU

To train models on the GPU, simply pass `use_gpu = True` in the `setup` function. There is no change in the use of the API; however, in some cases, additional libraries have to be installed. The following models can be trained on GPUs:

* Extreme Gradient Boosting&#x20;
* Catboost
* Light Gradient Boosting Machine requires [GPU specific installation](https://lightgbm.readthedocs.io/en/latest/GPU-Tutorial.html)
* Logistic Regression, Ridge Classifier, Random Forest, K Neighbors Classifier, K Neighbors Regressor, Support Vector Machine, Linear Regression, Ridge Regression, Lasso Regression requires [cuML >= 0.15](https://github.com/rapidsai/cuml)

## PyCaret Intel sklearnex support

You can apply [Intel optimizations](https://github.com/intel/scikit-learn-intelex) for machine learning algorithms and speed up your workflows. To train models with Intel optimizations use `sklearnex` engine. There is no change in the use of the API, however, installation of Intel sklearnex is required:

{% code lineNumbers="true" %}

```bash
pip install scikit-learn-intelex
```

{% endcode %}
