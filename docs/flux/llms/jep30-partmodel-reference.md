# Source: https://docs.flux.ai/reference/jep30-partmodel-reference.md

# JEP30 PartModel Import/Export

Import and export parts in JEP30 PartModel Format. This feature is only available on the [Enterprise Plan](https://www.flux.ai/p/contact-sales?utm_source=docs).

![](https://uploads.developerhub.io/prod/86Yw/x6sxeevjwzn4k79dbb65li7uxu7cplcw9znauwhbeke1onx8iel7hs60hclvygji.png)

## Overview

JEP30 PartModel is a set of guidelines established by JEDEC, which is designed to facilitate the exchange of part data between manufacturers and their customers within the electrical and electronics industries. [Read more about JEP30](https://www.jedec.org/category/technology-focus-area/jep30).

Flux's JEP30 import converts any PartModel XML files into Flux-native components that can be used in any design or modified at will. Flux's JEP30 export converts any Flux component into a PartModel XML file to be downloaded. Flux can also generate JEP30 files from a datasheet using AI, [learn more.](https://docs.flux.ai/flux/tutorials/ai-generated-jep30-partmodel)

## Getting Started

## JEP30 PartModel Import

To import a JEP30 XML file:

1. Open the Flux menu on the top left.
2. Select "Import"-&gt;"JEP30 PartModel"
3. Select a JEP30 PartModel XML
4. Click on "Import"

![](https://uploads.developerhub.io/prod/86Yw/9w59hjqhpuadzu7opwxkyas86az6rk4m8tfe5pjflnv5uhuifla97e9gjf4pe0w8.gif)

## JEP30 PartModel Export

To export a JEP30 XML file:

1. Open the target component
2. Click on the Flux menu on the top left.
3. Select "Export"-&gt;"JEP30 PartModel"

![](https://uploads.developerhub.io/prod/86Yw/56db26z7u9ttq1btm28og2gzrzvwehwr2a82dsoiw2185vruv1eynlsv8314dnz7.gif)

### Requirements

For JEP30 PartModel export to work, the target component needs meet the following requirements

- Contains a `Manufacturer Part Number` [property](https://docs.flux.ai/flux/reference/reference-inspector-properties).
- Contains a `Manufacturer Name` [property](https://docs.flux.ai/flux/reference/reference-inspector-properties).
- The project can only contain terminals.

JEP30 PartModel XML Example

```xml

```



## FAQs

[Limited to specific part types? What happens if it's outside?]