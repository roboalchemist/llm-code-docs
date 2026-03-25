# Source: https://developers.make.com/custom-apps-documentation/debug-your-app/make-devtool/tools.md

# Tools

The Tools section of the Make DevTool has useful features that can help you build your scenario.

<figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-1f63409f9913cf0cc20d1e3d9807dcbb643103b8%2Fcustomapps_devtools_maketoolspanel.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

## Focus a module

Opens settings of the selected module.

The module ID is the number you see in the Scenario Builder next to the name of the module. The same apps used multiple times in one scenario will have different IDs for each module.

## Find module(s) by mapping

Searches module(s)' values for the specified term.

<table><thead><tr><th width="169.25927734375" valign="top">Field</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">Keyword</td><td valign="top">Enter the term you want to search for and click the <strong>Run</strong> button. The numbers in the output are IDs of modules tha contain the term you have entered.</td></tr><tr><td valign="top">Use only values</td><td valign="top">Enable this option to only search in module fields' values. Disable this option to also search in module fields' names.</td></tr></tbody></table>

## Get app metadata

Retrieves app metadata by the app's module name or ID. This is useful when you need to get the app version used in your scenario for technical support or development of the app.

## Copy mapping

Copies values from the source module to the target module. When the source and target modules are specified, click the **Run** button to copy the mapping.

<table><thead><tr><th width="165.5555419921875" valign="top">Field</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">Source module</td><td valign="top">Select the module or enter the module ID of the module from which you want to copy field values.</td></tr><tr><td valign="top">Target module</td><td valign="top">Select the module or enter the module ID of the module into which you want to insert the source module values. The values in the target module will be overwritten.</td></tr></tbody></table>

## Copy filter

Copies the filter settings from the source module to the target module. The copy action is performed on the filter placed on the left side of the selected module. When the source and target modules are specified, click the **Run** button to copy the filter.

<table><thead><tr><th width="192.22222900390625" valign="top">Field</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">Source module</td><td valign="top">Select the module or enter the ID of the module from which you want to copy filter values.</td></tr><tr><td valign="top">Target module</td><td valign="top">Select the module or enter the ID of the module into which you want to insert the filter values from the source module. The values in the target module will be overwritten.</td></tr><tr><td valign="top">Preserve fallback route setting</td><td valign="top">If enabled and the source filter is set as the fallback route, then the target filter is also set at the fallback route.</td></tr></tbody></table>

## Swap connection

Duplicates a connection from the source module to every module of the same app in the scenario.

<table><thead><tr><th width="147.0369873046875" valign="top">Field</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">Source module</td><td valign="top">Select the module or enter the ID of the module from which you want to duplicate the connection and set the same connection for every module of the same app in your scenario.</td></tr></tbody></table>

## Swap variable

Searches for specified variables in the scenario and replaces them with a new variable.

<table><thead><tr><th width="172.96295166015625" valign="top">Field</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">Variable to find</td><td valign="top">Select the variable you want to replace from the module in your scenario and copy it to this field. You can also drag and drop the variable into the field.</td></tr><tr><td valign="top">Replace with</td><td valign="top">Copy and paste, or drag and drop the variable you want to use instead of the variable specified in the field above.</td></tr><tr><td valign="top">Module</td><td valign="top">Select the module in which you want to replace the variable. If no module is selected, the variable will be replaced in the entire scenario.</td></tr></tbody></table>

## Swap app

Replaces the selected app version in your scenario with another app version.

Before swapping, make sure that the version you've selected supports all the modules and functions you might need for your scenario.

## Base 64

Encodes the entered data to Base64 or decodes Base64. This is useful when you you want to search for particular data in the encoded request. When the input is specified, click the **Run** button to perform the action.

<table><thead><tr><th width="145.5555419921875" valign="top">Field</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">Operation</td><td valign="top">Select whether you want to encode the data from the Raw Data field to Base64 or decode Base64 to raw data.</td></tr><tr><td valign="top">Raw Data</td><td valign="top">Enter the data you want to encode to Base64 or the Base64 you want to decode to raw data, depending on the option selected in the Operation field above.</td></tr></tbody></table>

## Copy module name

Copies the name of the selected module to your clipboard. When the module is selected, click the **Run** button to copy the module's name.

<table><thead><tr><th width="141.851806640625" valign="top">Field</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">Module</td><td valign="top">Select the module whose name you want to copy.</td></tr></tbody></table>

## Remap source

Changes the mapping source from one module to another. You can do this for an existing module in your scenario as well as a new one. Click the **Run** button to perform the action.

<table><thead><tr><th width="175.1851806640625" valign="top">Field</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">Source module</td><td valign="top">Select the module to be replaced as the mapping source for other modules in your scenario.</td></tr><tr><td valign="top">Target module</td><td valign="top">Select the module you want to use as the new mapping source.</td></tr><tr><td valign="top">Module to edit</td><td valign="top">If you don't want to change the mapping in the entire scenario, select the module you want to change the mapping for.</td></tr></tbody></table>

## Highlight app

Highlights modules of the specified app in your scenario.

<table><thead><tr><th width="212.22222900390625" valign="top">Field</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">App to be highlighted</td><td valign="top">Select the app you want to highlight in your scenario.</td></tr><tr><td valign="top">Version</td><td valign="top">Select the version of the app you want to highlight.</td></tr><tr><td valign="top">Highlight color</td><td valign="top">Enter the hex color you want to use to highlight modules in your scenario.</td></tr></tbody></table>

## Get blueprint size

Checks the size of modules in the scenario. This is useful when you are having trouble saving a blueprint that is too large.

## Showcase mode

Toggles the showcase mode of the scenario editor. This mode is useful when you are building a scenario and don't want to set up the full module.

To leave showcase mode, run this tool again or save the scenario and refresh the browser window.

## Mock labels

Changes the label and description of the given module. Changes made by this tool are not permanent and don't affect the real scenarios. This option is meant for presentation purposes only. To reset the text, refresh the browser window.

<table><thead><tr><th width="157.40740966796875" valign="top">Field</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">Module</td><td valign="top">Select the module to change the label and description.</td></tr><tr><td valign="top">Label</td><td valign="top">Enter the label of the module. An empty value equals no change. If you want a blank label, enter (space).</td></tr><tr><td valign="top">Description</td><td valign="top">Enter the description of the module. An empty value equals no change. If you want a blank label, enter (space).</td></tr></tbody></table>

## Change background

Temporarily changes the background color of the scenario. This is useful when you need a white background for screenshots and mockups. To reset the background, refresh the browser window.
