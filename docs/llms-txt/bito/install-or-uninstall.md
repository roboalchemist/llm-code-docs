# Source: https://docs.bito.ai/other-bito-ai-tools/bito-cli/install-or-uninstall.md

# Install or uninstall

## Installing Bito CLI (Recommended)&#x20;

We recommend you use the following methods to install Bito CLI.&#x20;

### Mac and Linux&#x20;

`sudo curl https://alpha.bito.ai/downloads/cli/install.sh -fsSL | bash`

**Note:** curl will always download the latest version.

#### Archlinux&#x20;

Arch and Arch based distro users can install it from [AUR](https://aur.archlinux.org/packages/bito-cli)&#x20;

`yay -S bito-cli`

or

`paru -S bito-cli`

**Note for the Mac Users:** You might face issues related to verification for which you will have to manually do the steps from [here](https://support.apple.com/en-in/guide/mac-help/mh40616/mac) (we are working on fixing it as soon as possible).&#x20;

### Windows&#x20;

* In the [Bito CLI GitHub repo](https://github.com/gitbito/CLI), open the folder that has the latest version number.&#x20;
* From here, download the MSI file called `Bito CLI.exe` and then install Bito CLI using this installer.
* On Windows 11, you might get notification related to publisher verification. Click on "Show more" or "More info" and click on "Run anyway" (we are working on fixing this as soon as possible).&#x20;

{% hint style="info" %}
Once the installation is complete, start a new command prompt and run `bito` command to get started.&#x20;
{% endhint %}

## Installing with Manual Binary Download (Not Recommended)&#x20;

While it's not recommended, you can download the Bito CLI binary from our repository, and install it manually. The binary is available for Windows, Linux, and Mac OS (x86 and ARM architecture).&#x20;

### Mac and Linux&#x20;

1. In the [Bito CLI GitHub repo](https://github.com/gitbito/CLI), open the folder that has the latest version number.&#x20;
2. From here, download the Bito CLI binary specific to your OS platform.
3. Start the terminal, go to the location where you downloaded the binary, move the downloaded file (in the command below use bito-\* filename you have downloaded) to filename bito.

   `mv bito-<os>-<arch> bito`
4. Make the file executable using following command `chmod +x ./bito`
5. Copy the binary to `/usr/local/bin` using following command `sudo cp ./bito /usr/local/bin`&#x20;
6. Set PATH variable so that Bito CLI is always accessible. `PATH=$PATH:/usr/local/bin`&#x20;
7. Run Bito CLI with `bito` command. If PATH variable is not set, you will need to run command with the complete or relative path to the Bito executable binary.

### Windows&#x20;

1. In the [Bito CLI GitHub repo](https://github.com/gitbito/CLI), open the folder that has the latest version number.&#x20;
2. From here, download the Bito CLI binary for Windows called `bito.exe`.&#x20;
3. For using Bito CLI, always move to the directory containing Bito CLI prior to running it.
4. Set PATH variable so that Bito CLI is always accessible.&#x20;
   1. Follow the instructions as per this [link](https://share.bito.co/static/share?aid=02f4506f-1208-4d97-bb1d-96f3b4a1a017)&#x20;
   2. Edit the "Path" variable and add a new path of the location where Bito CLI is installed on your machine. &#x20;

## Uninstalling Bito CLI&#x20;

### Mac and Linux&#x20;

`sudo curl https://alpha.bito.ai/downloads/cli/uninstall.sh -fsSL | bash`

**Note:** This will completely uninstall Bito CLI and all of its components.

### Windows&#x20;

For Windows, you can uninstall Bito CLI just like you uninstall any other software from the control panel. You can follow these steps:&#x20;

1. Click on the Windows Start button and type "control panel" in the search box, and then open the Control Panel app.&#x20;
2. Under the "Programs" option, click on "Uninstall a program".&#x20;
3. Find "Bito CLI" in the list of installed programs and click on it.&#x20;
4. Click on the "Uninstall" button (given at the top) to start the uninstallation process.&#x20;
5. Follow the instructions provided by the uninstall wizard to complete the uninstallation process.

After completing these steps, Bito CLI should be completely removed from your Windows machine.&#x20;
