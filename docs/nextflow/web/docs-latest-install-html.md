# Source: https://www.nextflow.io/docs/latest/install.html

Title: Installation — Nextflow documentation

URL Source: https://www.nextflow.io/docs/latest/install.html

Markdown Content:
Nextflow can be used on any POSIX-compatible system (Linux, macOS, etc), and on Windows through [WSL](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux). This page describes how to install Nextflow.

Note

New versions of Nextflow are released regularly. See [Updating Nextflow](https://www.nextflow.io/docs/latest/updating-nextflow.html#updating-nextflow-page) for more information about Nextflow release cadence, how to update Nextflow, and how select your version of Nextflow.

Requirements[](https://www.nextflow.io/docs/latest/install.html#requirements "Permalink to this heading")
----------------------------------------------------------------------------------------------------------

Nextflow requires Bash 3.2 (or later) and [Java 17 (or later, up to 25)](http://www.oracle.com/technetwork/java/javase/downloads/index.html) to be installed. To see which version of Java you have, run the following command:

java -version

Changed in version 24.11.0-edge: Support for Java versions prior to 17 was dropped.

If you don’t have a compatible version of Java installed, it is recommended that you install it through [SDKMAN!](https://sdkman.io/), and that you use the latest Long-Term-Support (LTS) version of Temurin. See [Which version of JDK should I use?](https://whichjdk.com/) for more information about different versions of Java.

To install Java with SDKMAN:

1. [Install SDKMAN](https://sdkman.io/install):

curl -s https://get.sdkman.io | bash
2.   Open a new terminal.

1. Install Java:

sdk install java 17.0.10-tem
4.   Confirm that Java is installed correctly:

java -version

Install Nextflow[](https://www.nextflow.io/docs/latest/install.html#install-nextflow "Permalink to this heading")
------------------------------------------------------------------------------------------------------------------

Nextflow is distributed as an easy to use self-installing package. It is also distributed via Conda and as a standalone distribution.

### Self-install[](https://www.nextflow.io/docs/latest/install.html#self-install "Permalink to this heading")

In order to make the installation process as simple as possible, Nextflow is distributed as a self-installing package.

To install Nextflow with the self-installing package:

1. Download Nextflow:

curl -s https://get.nextflow.io | bash Tip

Set `export CAPSULE_LOG=none` to make the installation logs less verbose.
2.   Make Nextflow executable:

chmod +x nextflow
3.   Move Nextflow into an executable path. For example:

mkdir -p $HOME/.local/bin/
mv nextflow $HOME/.local/bin/ Tip

Ensure the directory `$HOME/.local/bin/` is included in your `PATH` variable. Temporarily add this directory to `PATH` by setting `export PATH="$PATH:$HOME/.local/bin"`. Add the directory to `PATH` permanently by adding the export command to your shell configuration file, such as `~/.bashrc` or `~/.zshrc`. Alternatively, move the `nextflow` executable to a directory already in your `PATH`. Warning

Nextflow updates its executable during the self-install process, therefore the update can fail if the executable is placed in a directory with restricted permissions.
4.   Confirm Nextflow is installed correctly:

nextflow info

### Conda[](https://www.nextflow.io/docs/latest/install.html#conda "Permalink to this heading")

To install Nextflow with Conda:

1. Create an environment with Nextflow:

conda create --name nf-env bioconda::nextflow
2.   Activate the environment:

source activate nf-env
3.   Confirm Nextflow is installed correctly:

nextflow info

Warning

Installing Nextflow via Conda may lead to outdated versions, dependency conflicts, and Java compatibility issues. Using the self-installing package is recommended for a more reliable and up-to-date installation.

### Standalone distribution[](https://www.nextflow.io/docs/latest/install.html#standalone-distribution "Permalink to this heading")

The Nextflow standalone distribution (i.e., the `dist` release) is a self-contained `nextflow` executable that can run without needing to download core dependencies at runtime. This distribution is useful for offline environments as well as building and testing Nextflow locally.

To use the standalone distribution:

1. Download the standalone distribution from Assets section of the [GitHub releases page](https://github.com/nextflow-io/nextflow/releases).

2. Grant execution permissions to the downloaded file. For example:

chmod +x nextflow-24.10.1-dist
3.   Use it as a drop-in replacement for `nextflow` command. For example:

./nextflow-24.10.1-dist run info

Note

The standalone distribution will still download core and third-party plugins as needed at runtime.

Seqera Platform[](https://www.nextflow.io/docs/latest/install.html#seqera-platform "Permalink to this heading")
----------------------------------------------------------------------------------------------------------------

You can launch workflows directly from [Seqera Platform](https://seqera.io/platform/) without installing Nextflow locally.

Launching from Seqera provides you with:

* User-friendly launch interfaces.

* Automated cloud infrastructure creation.

* Organizational user management.

* Advanced analytics with resource optimization.

Seqera Cloud Basic is free for small teams. Researchers at qualifying academic institutions can apply for free access to Seqera Cloud Pro. See [Seqera Platform Cloud](https://docs.seqera.io/platform) to get started.

If you have installed Nextflow locally, you can use the [nextflow auth](https://www.nextflow.io/docs/latest/reference/cli.html#cli-auth) command to authenticate with Seqera and automatically configure workflow monitoring.
