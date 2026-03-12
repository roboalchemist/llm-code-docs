# Source: https://kubescape.io/docs/install-cli/

Title: Installing the client - Kubescape

URL Source: https://kubescape.io/docs/install-cli/

Markdown Content:
The Kubescape command-line client is a single binary. Because the software is updated frequently, we recommend you install Kubescape with the package manager appropriate for your system.

When Kubescape runs, it will check for a more recent version.

Cross-platform
--------------

### Script install

Supported platforms

This script is supported on Linux (x86_64 and arm64), macOS (Intel or Apple Silicon) and `bash` on Windows (x86_64).

You can automatically download and install Kubescape using our installer script. We encourage you to read it before executing it.

If run as root, the script will install the `kubescape` binary in `/usr/local/bin`. If run as a user, it will put the binary in `/.kubescape/bin`.

```
curl -s https://raw.githubusercontent.com/kubescape/kubescape/master/install.sh | /bin/bash
```

### krew

[Krew](https://krew.sigs.k8s.io/) is the plugin manager for the `kubectl` command-line tool. Kubescape can be installed as a `kubectl` plugin.

First, [install Krew](https://krew.sigs.k8s.io/docs/user-guide/setup/install/) using the appropriate method for your platform. Then, install Kubescape:

```
kubectl krew update
kubectl krew install kubescape
```

To invoke Kubescape when installed with krew, use `kubectl kubescape` instead of `kubescape`.

Windows
-------

Supported platforms

Kubescape is supported on Windows x64.

### PowerShell

Similar to the [bash installation script](https://kubescape.io/docs/install-cli/#manual-install), you can install Kubescape using PowerShell on Windows:

```
iwr -useb https://raw.githubusercontent.com/kubescape/kubescape/master/install.ps1 | iex
```

If you get an error message, you may need to change the [execution policy](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.3):

```
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
```

Note

The installation script requires PowerShell v5.0 or higher.

### Chocolatey

[Chocolatey](https://chocolatey.org/) is a package manager for Windows. To install Kubescape using Chocolatey, open a PowerShell terminal and run:

```
choco install kubescape
```

### Scoop

[Scoop](https://scoop.sh/) is a command-line installer for Windows. To install Kubescape using Scoop, open a PowerShell terminal and run:

```
scoop install kubescape
```

macOS
-----

### Homebrew

Kubescape is available in the [official Homebrew repository](https://formulae.brew.sh/formula/kubescape#default) or through a [Kubescape tap](https://github.com/kubescape/homebrew-tap). The version from the official repository does not include support for scanning Git repositories, due to [an upstream packaging issue](https://github.com/kubescape/kubescape/issues/1014).

To install Kubescape from the official repository:

```
brew install kubescape
```

To get Git support, install the Kubescape tap and the `kubescape-cli` package:

```
brew tap kubescape/tap
brew install kubescape-cli
```

Linux
-----

### Ubuntu

The Kubescape maintainers build each release and upload the packages to a [personal package archive (PPA)](https://help.launchpad.net/Packaging/PPA).

To install Kubescape with `apt`:

```
sudo add-apt-repository ppa:kubescape/kubescape
sudo apt update
sudo apt install kubescape
```

Kubescape can also be installed from [the Snap Store](https://snapcraft.io/kubescape).

### Red Hat, CentOS, Fedora and other RPM-based distributions, and Debian

The Kubescape maintainers build each release and upload the packages to the openSUSE Build Service (OBS), which builds packages in `RPM` and `deb` format for many different distributions and platforms.

[Installation instructions for each distribution are available on the OBS page](https://software.opensuse.org/download.html?project=home%3Akubescape&package=kubescape).

### openSUSE

Kubescape is packaged for the Zypper package manager.

```
sudo zypper refresh
sudo zypper install kubescape
```

Note

Packaging for openSUSE is supported by the openSUSE community and may not always be up-to-date with the [latest Kubescape release](https://github.com/kubescape/kubescape/tags).

### Arch

Kubescape is available in the [Arch Linux User Repository (AUR)](https://aur.archlinux.org/). To download and compile Kubescape on Arch Linux:

```
yay -S kubescape
```

If you would like to save some time and do not want to compile, you can install `kubescape-bin` instead:

```
yay -S kubescape-bin
```

### NixOS, or using nix on Windows or Linux

You can use `nix` on Linux or macOS.

To try it out in an ephemeral shell, run `nix-shell -p kubescape`.

To install Kubescape on NixOS, add the following configuration to your [`/etc/nixos/configuration.nix`](https://nixos.org/manual/nixos/stable/#ch-configuration) file:

```
# your other config ...
  environment.systemPackages = with pkgs; [
    # your other packages ...
    kubescape
  ];
```

Alternatively, if using [Home Manager](https://nixos.wiki/wiki/Home_Manager):

```
# your other config ...
  home.packages = with pkgs; [
    # your other packages ...
    kubescape
  ];
```

Or, to install your profile (not recommended):

```
nix-env --install -A nixpkgs.kubescape
```

Offline/air-gapped environment support
--------------------------------------

When it runs, Kubescape downloads _artifacts_ (frameworks, controls and configurations) from the [control library](https://kubescape.io/docs/frameworks-and-controls/) or from a configured [provider](https://kubescape.io/docs/providers/).

You can download these files manually, so that Kubescape can run offline, or in an "air-gapped" environment.

### Download all artifacts

1.   Download the controls and save them in the local directory. If no path is specified, they will be saved in `~/.kubescape`.

```
kubescape download artifacts --output path/to/local/dir
``` 
2.   Copy the downloaded artifacts to the offline system.

3.   Scan using the downloaded artifacts:

```
kubescape scan --use-artifacts-from path/to/local/dir
``` 

### Download a single artifact

You can also download a single artifact, and scan with the `--use-from` flag:

1.   Download and save in a file. If no file name is specified, the artifact will be saved as `~/.kubescape/<framework name>.json`.

```
kubescape download framework nsa --output /path/nsa.json
``` 
2.   Copy the downloaded artifacts to the offline system.

3.   Scan using the downloaded framework:

```
kubescape scan framework nsa --use-from /path/nsa.json
``` 

Next steps
----------

*   [Learn how to install the Kubescape Operator in your Kubernetes cluster](https://kubescape.io/docs/install-operator/)
*   [Check out the GitHub repository for Kubescape packaging](https://github.com/kubescape/packaging)
