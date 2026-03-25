# Source: https://docs.safetycli.com/safety-docs/safety-cli/safety-telemetry.md

# Safety Telemetry

By default, Safety receives non-sensitive, anonymized telemetry data when scans are performed. These data are captured solely for the purpose of delivering, maintaining and improving the Safety product.

The data captured include the following:&#x20;

| Name                                                            | Description                                                                                | Essential / Optional |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | -------------------- |
| **Safety Version** (safety\_version)                            | The version of Safety that was used, e.g. v3.0.1.                                          | Essential            |
| <p><strong>Safety Source</strong></p><p>(safety\_source)</p>    | The method by which Safety was used, e.g. via the CLI or via code.                         | Essential            |
| <p><strong>Safety Command</strong></p><p>(safety\_command)</p>  | Limited to the command used when running the scan (e.g. `safety scan`, `safety check`)     | Optional             |
| <p><strong>Safety Options</strong></p><p>(safety\_options)</p>  | Limited to the options used and how many times each is used, e.g. `-r`, `--output`, et al. | Optional             |
| <p><strong>Python Version</strong> </p><p>(python\_version)</p> | The version of Python installed.                                                           | Optional             |
| <p><strong>OS Type</strong></p><p>(os\_type)</p>                | The OS type used.                                                                          | Optional             |
| <p><strong>OS Release</strong></p><p>(os\_release)</p>          | The version of the OS used.                                                                | Optional             |
| **OS Description** (os\_description)                            | Description of the OS used.                                                                | Optional             |

## Disabling Non-Essential Telemetry Data

It is possible to disable the non-essential telemetry data by using the following option:

`--disable-optional-telemetry` e.g. `safety scan --disable-optional-telemetry`

When this option is employed, Safety will still collect the anonymized Safety Version and Safety Source. These data are required for us to be able to give our customers security protection, including security protection if Safety itself needs an update. We may also use the safety\_version to alert customers of any vulnerability or risk and recommend the user upgrade.

<br>
