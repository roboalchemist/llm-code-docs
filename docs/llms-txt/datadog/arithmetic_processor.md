# Source: https://docs.datadoghq.com/events/pipelines_and_processors/arithmetic_processor.md

---
title: Arithmetic Processor
description: >-
  Add a new attribute to an event with the result of a formula to remap time
  attributes or compute operations on event attributes
breadcrumbs: Docs > Event Management > Pipelines and Processors > Arithmetic Processor
---

# Arithmetic Processor

Use the arithmetic processor to add a new attribute (without spaces or special characters in the new attribute name) to an event with the result of the provided formula. This remaps different time attributes with different units into a single attribute, or compute operations on attributes within the same event.

A arithmetic processor formula can use parentheses and basic arithmetic operators: `-`, `+`, `*`, `/`.

By default, a calculation is skipped if an attribute is missing. Select *Replace missing attribute by 0* to automatically populate missing attribute values with 0 to ensure that the calculation is done.

**Notes**:

- An attribute may be listed as missing if it is not found in the event attributes, or if it cannot be converted to a number.
- The operator `-` needs to be space split in the formula as it can also be contained in attribute names.
- If the target attribute already exists, it is overwritten by the result of the formula.
- Results are rounded up to the 9th decimal. For example, if the result of the formula is `0.1234567891`, the actual value stored for the attribute is `0.123456789`.
- If you need to scale a unit of measure, use the scale filter.

**Example arithmetic processor**

{% image
   source="https://datadog-docs.imgix.net/images/logs/log_configuration/processor/arithmetic_processor.b866facee14ced43cb90f984d2136080.png?auto=format"
   alt="Arithmetic Processor" /%}
