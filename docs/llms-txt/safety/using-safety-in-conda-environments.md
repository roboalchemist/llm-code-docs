# Source: https://docs.safetycli.com/safety-docs/support/using-safety-in-conda-environments.md

# Using Safety in Conda Environments

## Using Safety CLI with Anaconda Environments

### Overview

Safety CLI is the only dependency scanner powered by Safety's industry-leading vulnerability database. Safety CLI can be used to scan and secure Anaconda projects and environments, with some additional steps required to help make implementation and rollout seamless across your team.\
\
This guide will show you how to use Safety CLI effectively with your Anaconda projects.

### Table of Contents

* [General Process](#general-process)
* [Scanning Unix-based Systems (Linux/macOS)](#unix-based-systems-linux-macos)
* [Scanning Windows-based Systems](#windows-based-systems)
* [Notes](#important-note-1)

### General Process

To scan Anaconda environments with Safety CLI, the following general steps are recommended:

1. Export the Anaconda manifest (list of packages in the Anaconda project):

   ```bash
   conda activate your_environment_name
   conda list -e > requirements.txt
   ```
2. Separate pip-installed packages and conda-installed packages into two separate temporary requirements.txt files (instructions and examples for this below)
3. Scan the separated requirements files using `safety scan`
4. Delete the temporary requirements.txt files that were created

### Unix-based Systems (Linux/macOS)

For a streamlined workflow on Unix-based systems, use the following bash script:

```bash
#!/bin/bash

# Function to clean up temporary files
cleanup() {
    rm -f requirements.txt conda_requirements.txt pip_requirements.txt
}

# Trap to ensure cleanup happens even if the script is interrupted
trap cleanup EXIT

# Generate requirements file
conda list -e > requirements.txt

# Function to separate conda and pip packages
separate_requirements() {
    local input_file=$1
    local conda_output=$2
    local pip_output=$3

    > "$conda_output"
    > "$pip_output"

    while IFS= read -r line
    do
        if [[ $line =~ ^#.*$ ]] || [[ -z $line ]]; then
            echo "$line" >> "$conda_output"
        elif [[ $line == *"=pypi_0"* ]]; then
            package_info=$(echo "$line" | sed 's/=/==/;s/=pypi_0//')
            echo "$package_info" >> "$pip_output"
        else
            package_info=$(echo "$line" | awk -F= '{print $1"=="$2" #"$3}')
            echo "$package_info" >> "$conda_output"
        fi
    done < "$input_file"
}

# Separate requirements
separate_requirements "requirements.txt" "conda_requirements.txt" "pip_requirements.txt"

# Run safety with all arguments passed to this script
safety "$@"

# Cleanup is handled by the trap
```

#### Usage

1. Save the script as `conda_safety.sh`
2. Make it executable: `chmod +x conda_safety.sh`
3. Run the script as a replacement for the `safety` command, using any Safety CLI arguments. For example:

```
conda activate <your_environment_name>
./conda_safety.sh scan
```

or

```
conda activate <your_environment_name>
./conda_safety.sh scan --output json
```

#### Setting Up as a Command using an alias

To use the script as a command:

1. Add an alias in your shell configuration file (`~/.bashrc` or `~/.zshrc`):

   ```
   alias conda-safety='/path/to/your/conda_safety.sh'
   ```
2. Reload your shell configuration:

   ```
   source ~/.bashrc  # or ~/.zshrc for Zsh
   ```

Now you can use `conda-safety` as a drop-in replacement for the `safety` command. Once you've activated your conda environment, use \`conda-safety\`. For example:

```
conda activate <your_environment_name>
conda-safety auth
conda-safety scan
```

### Windows-based Systems

For Windows users, use the following PowerShell script:

```powershell
# Function to clean up temporary files
function Cleanup {
    Remove-Item -ErrorAction SilentlyContinue requirements.txt, conda_requirements.txt, pip_requirements.txt
}

# Ensure cleanup happens even if the script is interrupted
trap { Cleanup; break }

# Generate requirements file
conda list -e > requirements.txt

# Function to separate conda and pip packages
function Separate-Requirements {
    param (
        [string]$InputFile,
        [string]$CondaOutput,
        [string]$PipOutput
    )

    $null > $CondaOutput
    $null > $PipOutput

    Get-Content $InputFile | ForEach-Object {
        if ($_ -match '^#' -or $_ -eq '') {
            $_ >> $CondaOutput
        }
        elseif ($_ -match '=pypi_0') {
            $packageInfo = $_ -replace '=', '==' -replace '=pypi_0', ''
            $packageInfo >> $PipOutput
        }
        else {
            $parts = $_ -split '='
            "$($parts[0])==$($parts[1]) #$($parts[2])" >> $CondaOutput
        }
    }
}

# Separate requirements
Separate-Requirements "requirements.txt" "conda_requirements.txt" "pip_requirements.txt"

# Run safety with all arguments passed to this script
safety $args

# Cleanup
Cleanup
```

#### Usage

1. Save the script as `Conda-Safety.ps1`
2. Open PowerShell and navigate to the script's directory
3. Run the script with Safety CLI arguments:

```
conda activate <your_environment_name>
.\Conda-Safety.ps1 scan
```

or

```
conda activate <your_environment_name>
.\Conda-Safety.ps1 scan --output json
```

#### Setting Up as a Command

To use the script as a command in Windows:

1. Create a directory for the script if it doesn't exist:

   ```
   mkdir C:\Users\YourUsername\Documents\WindowsPowerShell\Scripts
   ```
2. Move the script to this directory:

   ```
   Move-Item Conda-Safety.ps1 C:\Users\YourUsername\Documents\WindowsPowerShell\Scripts
   ```
3. Add the directory to your PATH:
   * Open System Properties
   * Click on Environment Variables
   * Under System Variables, find and edit the PATH variable
   * Add `C:\Users\YourUsername\Documents\WindowsPowerShell\Scripts`
4. Create a PowerShell profile if you don't have one:

   ```
   if (!(Test-Path -Path $PROFILE)) { New-Item -ItemType File -Path $PROFILE -Force }
   ```
5. Add this line to your PowerShell profile:

   ```
   Set-Alias conda-safety C:\Users\YourUsername\Documents\WindowsPowerShell\Scripts\Conda-Safety.ps1
   ```

Now you can use `conda-safety` as a command in PowerShell as a drop-in replacement for the `safety` command. This requires `safety` and `conda` to already be installed and available in Powershell.

### Important Note

Conda-installed packages may differ from standard PyPI packages. As a result, security findings for conda-installed packages may differ from PyPi equivalent packages. Always verify findings for conda-installed packages against the specific versions in your Anaconda environment.

### Help and Implementation Assistance

Anaconda environments and setups vary. If the instructions above do not work or you encouter any issues, please don't hesitate to reach out to our support team at <support@safetycli.com>. We're here to help you ensure the security of your Python projects, regardless of your environment setup.
