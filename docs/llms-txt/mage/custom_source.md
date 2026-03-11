# Source: https://docs.mage.ai/data-integrations/sources/custom_source.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom source

> Easily plug in your own data integration sources and destinations with Mage Pro.

export const ProOnly = ({button = 'Get started for free', description = 'Try our fully managed solution to access this advanced feature.', source = 'documentation', title = 'Only in Mage Pro.'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        <p className="normal">{description}</p>
      </div>

      <div> </div>

      <div>
        <ProButton label={button} href={`https://cloud.mage.ai/sign-up?source=${source}`} />
      </div>
    </div>
  </a>;

export const ProButton = ({href, label = 'Get started with Mage Pro for free', source = 'documentation'}) => <div style={{
  height: 32,
  position: 'relative'
}}>
    <a target="_blank" className="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium rounded-full" href={href ?? `https://cloud.mage.ai/sign-up?source=${source}`}>
      <span className="absolute inset-0 bg-primary-dark dark:bg-primary-light/10 border-primary-light/30 rounded-full dark:border group-hover:opacity-[0.9] dark:group-hover:border-primary-light/60">
      </span>

      <div className="mr-0.5 space-x-2.5 flex items-center">
        <span class="z-10 text-white dark:text-primary-light">
          {label}
        </span>

        <svg width="3" height="24" viewBox="0 -9 3 24" class="h-5 rotate-0 overflow-visible text-white/90 dark:text-primary-light">
          <path d="M0 0L3 3L0 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
      </div>
    </a>
  </div>;

<ProOnly source="data-integration" />

Mage Pro makes it easy to integrate your own custom data integration sources and destinations.

To get started, follow the [adapt an existing source](/contributing/data-integrations/adapt-existing-source) guide or the [add a new source](/contributing/data-integrations/add-new-source) guide to create your custom integration.

Once your custom source or destination is ready, simply include it in your Mage Pro project by adding it to the appropriate folder as shown below.

## Folder structure

To register custom sources and destinations in your Mage Pro project, organize your project directory as follows:

```
.
├── mage_data
└── project_name
    ├── charts
    ├── custom
    ├── data_exporters
    ├── data_loaders
    ├── dbt
    ├── extensions
    ├── pipelines
    ├── data_integrations              # ← important
    │   └── sources
    │   │   ├── custom_source_1
    │   │   │   └── templates
    │   │   │   │   └── config.json
    │   │   │   └── __init__.py
    │   │   │   └── README.md
    │   │   ├── custom_source_2
    │   │   └── metadata.yaml          # Register all source definitions here
    │   └── destinations
    │       ├── custom_destination_1
    │       ├── custom_destination_2
    │       └── metadata.yaml          # Register all destination definitions here
    ├── scratchpads
    ├── transformers
    ├── utils
    ├── __init__.py
    ├── io_config.yaml
    ├── metadata.yaml
    └── requirements.txt
```

**Instructions**

1. Create a `data_integrations` folder inside your project directory.
2. Inside data\_integrations, create two subfolders:
   * `sources`: for your custom data source integrations
   * `destinations`: for your custom data destination integrations
3. Each source/destination should have its own folder (e.g., `custom_source_1`) containing:
   * An `__init__.py` file with the integration class
   * A `README.md` for documentation
   * A `templates/` directory with a `config.json` file for default configuration
4. Define a `metadata.yaml` file in each of the sources/ and destinations/ folders to register the integrations with Mage Pro.

This structure allows Mage Pro to discover and load your custom integrations dynamically.

## Register custom sources and destinations

To register your custom sources or destinations, create or update the `metadata.yaml` file inside the
respective `sources/` or `destinations/` subfolders under `data_integrations`.

📘 Example: `sources/metadata.yaml`

```yaml  theme={"system"}
sources:
- name: Source Name
  module_name: SourceModuleName
  uuid: source_uuid
```

📘 Example: `destinations/metadata.yaml`

```yaml  theme={"system"}
destinations:
- name: Source Name
  module_name: SourceModuleName
  uuid: source_uuid
```

Field descriptions

* `name`: Display name shown in the Mage UI dropdown.
* `module_name` (optional): The class name defined in the source's `__init__.py` file. Defaults to the `name` field with spaces removed.
* `uuid` (optional): Folder name of the source. Defaults to the lowercased `name`, with spaces replaced by underscores.

## Code modification

Unlike the [add a new source guide](/contributing/data-integrations/add-new-source) (which adds sources to the Mage core),
using custom sources in your project requires updating import paths to point to your project-level modules.

Update any imports from `mage_integrations` to `data_integrations` like so:

```python  theme={"system"}
# Before
from mage_integrations.sources.custom_source.module import SomeClass

# After
from data_integrations.sources.custom_source.module import SomeClass
```

This change ensures that Mage loads and uses your custom integration from the project folder instead of the built-in Mage package.

## Testing Your Custom Source

To test your custom data source integration:

1. Create a new data integration pipeline.
2. **Select your custom source** from the source dropdown.
   * Custom sources appear at the **bottom** of the list in the UI.
3. **Enter your source configuration**.
4. Click "**Test connection**" if your custom source class implements the test\_connection method.
5. Click "**View and select stream**" to verify that the expected streams are returned.
6. **Add a destination** and run the pipeline using a trigger to test end-to-end data flow.

### Troubleshooting: Source Not Appearing in UI?

If your custom source isn't showing up in the Data Integration source dropdown, follow these steps to debug:

1. Create a pipeline and add a **scratchpad block**.
2. **Run the following code** in the block to inspect the custom sources:

```python  theme={"system"}
# Inspect custom source registration
from mage_ai.server.api.integration_sources import get_custom_collection

custom_sources = get_custom_collection('sources', debug=True)
print(f'Custom sources detected: {custom_sources}')
```

3. **Try importing your custom module manually** to ensure it's discoverable and error-free:

```python  theme={"system"}
from data_integrations.sources.source_uuid import SourceModuleName
```

Replace `source_uuid` and `SourceModuleName` with the actual folder name and class name of your custom source.

### Troubleshooting: "View and select stream" Not Working?

If clicking "**View and select stream**" in the UI doesn’t return any streams, you can manually debug the discovery step using a **scratchpad block** in your pipeline.

Run the following code to test your custom source's `discover_streams` method:

```python  theme={"system"}
from data_integrations.sources.source_uuid import SourceModuleName

# Replace with your actual config keys and values
config = dict(
    key1='value1',
    key2='value2',
)

# Initialize the source class with config
source = SourceModuleName(config=config)

# Run stream discovery
streams = source.discover_streams()

# Print discovered streams
print(f'Discovered streams: {streams}')
```

**What to check**

* Ensure the `config` you provide contains all required fields expected by your source class.
* If `discover_streams()` returns an empty list or raises an error, check your source implementation or credentials.


Built with [Mintlify](https://mintlify.com).