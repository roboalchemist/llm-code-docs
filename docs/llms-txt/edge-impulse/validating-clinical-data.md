# Source: https://docs.edgeimpulse.com/knowledge/guides/reference-designs/health-reference-design/validating-clinical-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Validating clinical data

<Info>
  **Only available on the Enterprise plan**

  This feature is only available on the Enterprise plan. Review our [plans and pricing](https://edgeimpulse.com/pricing) or sign up for our free [expert-led trial](https://edgeimpulse.com/expert-led-trial) today.
</Info>

## Using Checklists

You can optionally show a check mark in the list of data items, and show a check list for data items. This can be used to quickly view which data items are complete (if you need to capture data from multiple sources) or whether items are in the right format.

<Frame caption="Checklists in the your Data overview">
  <img src="https://mintcdn.com/edgeimpulse/rTWxVUHegAMX0AbN/.assets/images/research-data-ei-checks.png?fit=max&auto=format&n=rTWxVUHegAMX0AbN&q=85&s=766d96666d0d6242e8ee2ee6b2076e83" width="1588" height="1000" data-path=".assets/images/research-data-ei-checks.png" />
</Frame>

Checklists look trivial, but are actually very powerful as they give quick insights in dataset issues. Missing these issues until after the study is done can be very expensive.

Checklists are written to `ei-metadata.json` and are automatically being picked up by the UI.

Checklists are driven by the metadata for a data item. Set the `ei_check` metadata item to `0` or `1` to show a check mark in the list. To show an item in the checklist, set an `ei_check_KEYNAME` metadata item to `0` or `1`.

To query for items with or without a check mark, use a filter in the form of:

```
metadata->ei_check = 1
```

To make it easy to create these lists on the fly you can set these metadata items directly from a [transformation block](/studio/organizations/custom-blocks/custom-transformation-blocks)

## Example

For the reference design described and used in the previous pages, the combiner takes in a data item, and writes out:

1. A checklist, e.g.:
   * ✔ - PPG file present
   * ✔ - Accelerometer file present
   * ✘ - Correlation between HR/PPG HR is at least 0.5
2. If the checklist is OK, a `combined.parquet` file.
3. A `hr.png` file with the correlation between HR found from PPG, and HR from the reference device. This is useful for two reasons:
   * If the correlation is too low we're looking at the wrong file, or data is missing.
   * Verify if the PPG => HR algorithm actually works.

<Frame caption="AMS_010 hr.png">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/AMS_010-hr.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=a65855cc0c407359a202e578592e9cc9" width="640" height="480" data-path=".assets/images/AMS_010-hr.png" />
</Frame>

This makes it easy to quickly see if the data is in the right format, and if the data is complete. If the checklist is not OK, the data item is not used in the training set.


Built with [Mintlify](https://mintlify.com).