# Source: https://docs.jit.io/docs/sbom.md

# Software Bill of Materials (SBOM)

## Key things to know about Jit SBOM

* **Brief description:** Jit scans your codebase to maintain a continuously updated inventory of the OSS software components and dependencies used in your application, as well as their open source licenses.
* **Scanning process:** Jit automatically scans your codebase daily and scans individual repositories whenever there is a change made to each repository. The SBOM report is updated after every scan.
* **How to get started:** Go to **My Environment** in the left menu and click **SBOM**. Then click **Activate**. This will automatically scan your codebase (or selected repositories), while implementing daily scanning to continuously update your SBOM.
* **Based on OSV Scanner:** Jit unifies and enhances the leading open source scanners for all product security scanning technologies. For SBOM, Jit leverages OSV Scanner to scan your codebase and identify OSS components.

> 📘 Premium Feature
>
> Software Bill of Materials (SBOM) is only available for paying Jit customers.

## Generating an SBOM report

1. In the left menu, hover over **My Environment** and select **SBOM**.

   ![](https://files.readme.io/88081c1-image.png)

2. Optional: If you have not activated SBOM, click **Activate** and wait for the process to run. This may take some time. Data is displayed in the SBOM interface throughout the Activation process. For more information about SBOM activation, see [Security Plan Page](https://dash.readme.com/project/jitsecurity/v4.5.0/docs/security-plans-1).

   ![](https://files.readme.io/6a38ae7-image.png)

3. Click an entry to display where the component appears in the project.

<br />

### CSV export for SBOM

Currently, SBOM reports are available for the product standard Cyclone DX format.\
For users requiring a CSV script the below Python file can be run locally:

* Download the Python file on a machine that has python3 installed and name it cyclonedx-to-csv.py
* Download the JSON SBOM from the Jit UI
* Open a terminal and issue the OS command to change the directory to the location of the Python file
* Use the following command to convert the file:
* python3 cyclonedx-to-csv.py <path to input json sbom> <output csv name>

```python
#!/usr/bin/env python3
import json
import csv
import argparse
from typing import Dict, List, Any, Optional
from pathlib import Path

def safe_get_licenses(license_data: Optional[List[Any]]) -> str:
    """
    Safely extract license information from various possible formats.
    """
    if not license_data:
        return ''
    
    licenses = []
    for license_info in license_data:
        if isinstance(license_info, dict):
            # Handle license dictionary format
            if 'license' in license_info:
                license_content = license_info['license']
                if isinstance(license_content, dict):
                    licenses.append(license_content.get('id', ''))
                else:
                    licenses.append(str(license_content))
            # Handle expression format
            elif 'expression' in license_info:
                licenses.append(license_info['expression'])
        else:
            # Handle direct license string
            licenses.append(str(license_info))
    
    return '; '.join(filter(None, licenses))

def get_location_path(properties: Optional[List[Dict[str, Any]]]) -> str:
    """
    Extract the location path from properties with name 'syft:location:0:path'.
    """
    if not properties:
        return ''
    
    for prop in properties:
        if isinstance(prop, dict) and prop.get('name') == 'syft:location:0:path':
            return prop.get('value', '')
    
    return ''

def extract_repo_name(location_path: str) -> str:
    """
    Extract repository name from the location path.
    The repository name is considered to be the first part of the path after initial slash.
    """
    if not location_path or not location_path.startswith('/'):
        return ''
    
    # Split by '/' and take the first non-empty part
    parts = location_path.split('/')
    for part in parts:
        if part:
            return part
    
    return ''

def extract_component_data(component: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract relevant data from a component in the SBOM, handling missing fields gracefully.
    """
    if not isinstance(component, dict):
        return {
            'name': '',
            'version': '',
            'purl': '',
            'type': '',
            'publisher': '',
            'group': '',
            'description': '',
            'licenses': '',
            'cpe': '',
            'author': '',
            'location_path': '',
            'repository': ''
        }

    # Extract publisher information
    publisher = component.get('publisher', '')
    if isinstance(publisher, dict):
        publisher = publisher.get('name', '')

    # Extract author information
    author = component.get('author', '')
    if isinstance(author, dict):
        author = author.get('name', '')
    
    # Extract location path from properties
    location_path = get_location_path(component.get('properties', []))
    
    # Extract repository name from location path
    repository = extract_repo_name(location_path)

    return {
        'name': str(component.get('name', '')),
        'version': str(component.get('version', '')),
        'purl': str(component.get('purl', '')),
        'type': str(component.get('type', '')),
        'publisher': str(publisher),
        'group': str(component.get('group', '')),
        'description': str(component.get('description', '')),
        'licenses': safe_get_licenses(component.get('licenses', [])),
        'cpe': str(component.get('cpe', '')),
        'author': str(author),
        'location_path': location_path,
        'repository': repository
    }

def process_sbom(sbom_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Process the SBOM data and extract component information, handling missing sections gracefully.
    """
    components = []
    
    # Process metadata components if they exist
    metadata = sbom_data.get('metadata', {})
    if isinstance(metadata, dict):
        metadata_components = metadata.get('components', [])
        if isinstance(metadata_components, list):
            for component in metadata_components:
                if component:
                    components.append(extract_component_data(component))
    
    # Process main components list
    main_components = sbom_data.get('components', [])
    if isinstance(main_components, list):
        for component in main_components:
            if component:
                components.append(extract_component_data(component))
    
    return components

def write_csv(components: List[Dict[str, Any]], output_file: Path) -> None:
    """
    Write the component data to a CSV file.
    """
    if not components:
        print("No components found to write to CSV.")
        return
    
    fieldnames = [
        'name', 'version', 'purl', 'type', 'publisher',
        'group', 'description', 'licenses', 'cpe', 'author',
        'location_path', 'repository'
    ]
    
    with output_file.open('w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(components)

def main():
    parser = argparse.ArgumentParser(description='Convert CycloneDX SBOM JSON to CSV')
    parser.add_argument('input_file', type=str, help='Input CycloneDX JSON file path')
    parser.add_argument('output_file', type=str, help='Output CSV file path')
    
    args = parser.parse_args()
    input_path = Path(args.input_file)
    output_path = Path(args.output_file)
    
    if not input_path.exists():
        print(f"Error: Input file {input_path} does not exist.")
        return
    
    try:
        with input_path.open('r', encoding='utf-8') as f:
            sbom_data = json.load(f)
        
        if not isinstance(sbom_data, dict):
            print("Error: Invalid SBOM format - root element must be an object")
            return
            
        components = process_sbom(sbom_data)
        write_csv(components, output_path)
        print(f"Successfully converted {input_path} to {output_path}")
        print(f"Processed {len(components)} components")
        
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON file - {e}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```

<br />

### Supported Ecosystems

Jit will scan and include components from the following ecosystems in the SBOM report:

* Alpine (apk)
* C (conan)
* C++ (conan)
* Dart (pubs)
* Debian (dpkg)
* Dotnet (deps.json)
* Objective-C (cocoapods)
* Elixir (mix)
* Erlang (rebar3)
* Go (go.mod, Go binaries)
* Haskell (cabal, stack)
* Java (jar, ear, war, par, sar, nar, native-image)
* JavaScript (npm, yarn)
* Jenkins Plugins (jpi, hpi)
* Linux kernel archives (vmlinz)
* Linux kernel modules (ko)
* Nix (outputs in /nix/store)
* PHP (composer)
* Python (wheel, egg, poetry, requirements.txt)
* Red Hat (rpm)
* Ruby (gem)
* Rust (cargo.lock)
* Swift (cocoapods, swift-package-manager)
* Wordpress plugins

### Licenses Detection - Language support

Software licenses are included for every component for the following languages:

* NodeJS
* Go
* Python
* PHP

\*In some cases, licenses will be included for languages not specified above.