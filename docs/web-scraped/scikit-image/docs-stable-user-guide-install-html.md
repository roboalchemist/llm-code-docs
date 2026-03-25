# Source: https://scikit-image.org/docs/stable/user_guide/install.html

Title: 1. Installing scikit-image — skimage 0.26.0 documentation

URL Source: https://scikit-image.org/docs/stable/user_guide/install.html

Markdown Content:
*   First, you need to have the Python language installed. Two popular routes are the pip-based [Python.org installers](https://www.python.org/downloads/) and the conda-based [miniforge](https://github.com/conda-forge/miniforge).

*   Install `scikit-image` via [pip](https://scikit-image.org/docs/stable/user_guide/install.html#install-via-pip) or [conda](https://scikit-image.org/docs/stable/user_guide/install.html#install-via-conda), as appropriate.

*   Or, [build the package from source](https://scikit-image.org/docs/stable/user_guide/install.html#installing-scikit-image-for-contributors). Do this if you’d like to contribute to development.

1.1. Supported platforms[#](https://scikit-image.org/docs/stable/user_guide/install.html#supported-platforms "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

*   Windows 64-bit on x86 processors

*   macOS on x86 and ARM (M1, etc.) processors

*   Linux 64-bit on x86 and ARM processors

While we do not officially support other platforms, you could still try [building from source](https://scikit-image.org/docs/stable/user_guide/install.html#building-from-source).

1.2. Version check[#](https://scikit-image.org/docs/stable/user_guide/install.html#version-check "Link to this heading")
------------------------------------------------------------------------------------------------------------------------

To see whether `scikit-image` is already installed or to check if an install has worked, run the following in a Python shell or Jupyter notebook:

import skimage as ski
print(ski. __version__ )

or, from the command line:

python -c "import skimage; print(skimage.__version__)"

(Try `python3` if `python` is unsuccessful.)

You’ll see the version number if `scikit-image` is installed and an error message otherwise.

1.3. Installation via pip and conda[#](https://scikit-image.org/docs/stable/user_guide/install.html#installation-via-pip-and-conda "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------

### 1.3.1. pip[#](https://scikit-image.org/docs/stable/user_guide/install.html#install-via-pip "Link to this heading")

Prerequisites to a pip install: you must be able to use `pip` on your command line to install packages.

We strongly recommend the use of a [virtual environment](https://towardsdatascience.com/virtual-environments-104c62d48c54?gi=2532aa12906#ee81). A virtual environment creates a clean Python environment that does not interfere with the existing system installation, can be easily removed, and contains only the package versions your application needs.

To install the current `scikit-image` you’ll need at least Python 3.11. If your Python is older, pip will find the most recent compatible version.

# Update pip
python -m pip install -U pip

# Install scikit-image
python -m pip install -U scikit-image

Some additional dependencies are required to access all example datasets in `skimage.data`. Install them using:

python -m pip install -U scikit-image[data]

To install optional scientific Python packages that expand `scikit-image`’s capabilities to include, e.g., parallel processing, use:

python -m pip install -U scikit-image[optional]

Warning

Do not use the command `sudo` and `pip` together as `pip` may overwrite critical system libraries.

### 1.3.2. conda[#](https://scikit-image.org/docs/stable/user_guide/install.html#install-via-conda "Link to this heading")

We recommend [miniforge](https://github.com/conda-forge/miniforge), a minimal distribution that makes use of [conda-forge](https://conda-forge.org/). It installs Python and provides virtual environments.

Once you have your conda environment set up, install `scikit-image` with:

conda install scikit-image

1.4. System package managers[#](https://scikit-image.org/docs/stable/user_guide/install.html#system-package-managers "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

Using a package manager (`apt`, `dnf`, etc.) to install `scikit-image` or other Python packages is not your best option, since you’re likely to get an older version. It also becomes harder to install other Python packages not provided by the package manager.

1.5. Downloading all demo datasets[#](https://scikit-image.org/docs/stable/user_guide/install.html#downloading-all-demo-datasets "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

Some of our example images (in `skimage.data`) are hosted online and are not installed by default. These images are downloaded upon first access. If you prefer to download all demo datasets, so they can be accessed offline, ensure that `pooch` is installed, then run:

python -c 'import skimage as ski; ski.data.download_all()'

1.6. Additional help[#](https://scikit-image.org/docs/stable/user_guide/install.html#additional-help "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------

If you still have questions, reach out through

*   our [user forum](https://forum.image.sc/tags/scikit-image)

*   our [developer forum](https://discuss.scientific-python.org/c/contributor/skimage)

*   our [chat channel](https://skimage.zulipchat.com/)

To suggest a change in these instructions, [please open an issue on GitHub](https://github.com/scikit-image/scikit-image/issues/new).

2. Installing scikit-image for contributors[#](https://scikit-image.org/docs/stable/user_guide/install.html#installing-scikit-image-for-contributors "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Your system needs a:

*   C compiler,

*   C++ compiler, and

*   a version of Python supported by `scikit-image` (see [pyproject.toml](https://github.com/scikit-image/scikit-image/blob/main/pyproject.toml#L14)).

First, [fork the scikit-image repository on GitHub](https://github.com/scikit-image/scikit-image/fork). Then clone your fork locally and set an `upstream` remote to point to the original scikit-image repository:

Note

We use `git@github.com` below; if you don’t have SSH keys setup, use `https://github.com` instead.

git clone git@github.com:YOURUSERNAME/scikit-image
cd scikit-image
git remote add upstream git@github.com:scikit-image/scikit-image

All commands below are run from within the cloned `scikit-image` directory.

2.1. Build environment setup[#](https://scikit-image.org/docs/stable/user_guide/install.html#build-environment-setup "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

Set up a Python development environment tailored for scikit-image. Here we provide instructions for two popular environment managers: `venv` (pip) and `conda` (miniforge).

### 2.1.1. venv[#](https://scikit-image.org/docs/stable/user_guide/install.html#venv "Link to this heading")

# Create a virtualenv named ``skimage-dev`` that lives outside of the repository.
# One common convention is to place it inside an ``envs`` directory under your home directory:
mkdir ~/envs
python -m venv ~/envs/skimage-dev

# Activate it
# (On Windows, use ``skimage-dev\Scripts\activate``)
source ~/envs/skimage-dev/bin/activate

# Install development dependencies
pip install -r requirements.txt
pip install -r requirements/build.txt

# Install scikit-image in editable mode. In editable mode,
# scikit-image will be recompiled, as necessary, on import.
spin install -v

Tip

The above installs scikit-image into your environment, which makes it accessible to IDEs, IPython, etc. This is not strictly necessary; you can also build with:

spin build

In that case, the library is not installed, but is accessible via `spin` commands, such as `spin test`, `spin ipython`, `spin run`, etc.

### 2.1.2. conda[#](https://scikit-image.org/docs/stable/user_guide/install.html#id5 "Link to this heading")

We recommend installing conda using [miniforge](https://github.com/conda-forge/miniforge), an alternative to Anaconda without licensing costs.

After installing miniforge:

# Create a conda environment with required dependencies
conda env create -f environment.yml

# Activate it
conda activate skimage-dev

# Install scikit-image in editable mode. In editable mode,
# scikit-image will be recompiled, as necessary, on import.
spin install -v

Tip

The above installs scikit-image into your environment, which makes it accessible to IDEs, IPython, etc. This is not strictly necessary; you can also build with:

spin build

In that case, the library is not installed, but is accessible via `spin` commands, such as `spin test`, `spin ipython`, `spin run`, etc.

2.2. Testing[#](https://scikit-image.org/docs/stable/user_guide/install.html#testing "Link to this heading")
------------------------------------------------------------------------------------------------------------

Run the complete test suite:

spin test

Or run a subset of tests:

# Run tests in a given file
spin test skimage/morphology/tests/test_gray.py

# Run tests in a given directory
spin test skimage/morphology

# Run tests matching a given expression
spin test -- -k local_maxima

2.3. Adding a feature branch[#](https://scikit-image.org/docs/stable/user_guide/install.html#adding-a-feature-branch "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

When contributing a new feature, do so via a feature branch.

First, fetch the latest source:

git switch main
git pull upstream main

Create your feature branch:

git switch --create my-feature-name

Using an editable install, `scikit-image` will rebuild itself as necessary. If you are building manually, rebuild with:

.. code-block:: sh

> spin build

Repeated, incremental builds usually work just fine, but if you notice build problems, rebuild from scratch using:

spin build --clean

2.4. Platform-specific notes[#](https://scikit-image.org/docs/stable/user_guide/install.html#platform-specific-notes "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

**Windows**

Building `scikit-image` on Windows is done as part of our continuous integration testing; the steps are shown in this [Azure Pipeline](https://github.com/scikit-image/scikit-image/blob/main/azure-pipelines.yml).

**Debian and Ubuntu**

Install suitable compilers prior to library compilation:

sudo apt-get install build-essential

2.5. Full requirements list[#](https://scikit-image.org/docs/stable/user_guide/install.html#full-requirements-list "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------

**Build Requirements**

# Generated via tools/generate_requirements.py and pre-commit hook.
# Do not edit this file; modify pyproject.toml instead.
meson-python>=0.16
ninja>=1.11.1.1
Cython>=3.0.8,!=3.2.0b1
pythran>=0.16
numpy>=2.0
spin==0.13
build>=1.2.1

**Runtime Requirements**

# Generated via tools/generate_requirements.py and pre-commit hook.
# Do not edit this file; modify pyproject.toml instead.
numpy>=1.24
scipy>=1.11.4
networkx>=3.0
pillow>=10.1
imageio>=2.33,!=2.35.0
tifffile>=2022.8.12
packaging>=21
lazy-loader>=0.4

**Test Requirements**

# Generated via tools/generate_requirements.py and pre-commit hook.
# Do not edit this file; modify pyproject.toml instead.
numpydoc>=1.7
pooch>=1.6.0; sys_platform != "emscripten"
pytest>=8.3
pytest-cov>=2.11.0
pytest-pretty
pytest-localserver
pytest-faulthandler
pytest-doctestplus>=1.6.0

**Documentation Requirements**

# Generated via tools/generate_requirements.py and pre-commit hook.
# Do not edit this file; modify pyproject.toml instead.
sphinx>=8.0
sphinx-gallery[parallel]>=0.18
numpydoc>=1.7
sphinx-copybutton
matplotlib>=3.7
dask[array]>=2023.2.0
pandas>=2.0
seaborn>=0.11
pooch>=1.6
tifffile>=2022.8.12
myst-parser
intersphinx-registry>=0.2411.14
ipywidgets
ipykernel
plotly>=5.20
kaleido==0.2.1
scikit-learn>=1.2
sphinx_design>=0.5
pydata-sphinx-theme>=0.16
PyWavelets>=1.6
pytest-doctestplus>=1.6.0

**Developer Requirements**

# Generated via tools/generate_requirements.py and pre-commit hook.
# Do not edit this file; modify pyproject.toml instead.
pre-commit
ipython
docstub==0.3.0.post0
asv; sys_platform != "emscripten"

**Data Requirements**

The full selection of demo datasets is only available with the following installed:

# Generated via tools/generate_requirements.py and pre-commit hook.
# Do not edit this file; modify pyproject.toml instead.
pooch>=1.6.0

**Optional Requirements**

You can use `scikit-image` with the basic requirements listed above, but some functionality is only available with the following installed:

*   [Matplotlib](https://matplotlib.org/) Used in various functions, e.g., for drawing, segmenting, reading images.

*   [Dask](https://dask.org/) The `dask` module is used to parallelize certain functions.

More rarely, you may also need:

*   [PyAMG](https://pyamg.org/) The `pyamg` module is used for the fast `cg_mg` mode of random walker segmentation.

*   [Astropy](https://www.astropy.org/) Provides FITS I/O capability.

*   [SimpleITK](http://www.simpleitk.org/) Optional I/O plugin providing a wide variety of [formats](https://itk.org/Wiki/ITK_File_Formats). including specialized formats used in biomedical imaging.

# Generated via tools/generate_requirements.py and pre-commit hook.
# Do not edit this file; modify pyproject.toml instead.
SimpleITK; sys_platform != "emscripten"
scikit-learn>=1.2
pyamg>=5.2; sys_platform != "emscripten" and python_version < "3.14"
astropy>=6.0
dask[array]>=2023.2.0
matplotlib>=3.7
pooch>=1.6.0; sys_platform != "emscripten"
PyWavelets>=1.6

2.6. Help with contributor installation[#](https://scikit-image.org/docs/stable/user_guide/install.html#help-with-contributor-installation "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

See [Additional help](https://scikit-image.org/docs/stable/user_guide/install.html#additional-help) above.
