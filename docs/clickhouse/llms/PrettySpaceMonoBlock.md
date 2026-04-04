# Source: https://clickhouse.ferndocs.com/reference/interfaces/formats/PrettySpaceMonoBlock.md

---
alias: []
description: Documentation for the PrettySpaceMonoBlock format
input_format: false
keywords:
  - PrettySpaceMonoBlock
output_format: true
slug: /interfaces/formats/PrettySpaceMonoBlock
title: PrettySpaceMonoBlock <Badge intent="success">Output</Badge>
doc_type: reference
---

import PrettyFormatSettings from './_snippets/common-pretty-format-settings.md';

## Description [#description]

Differs from the [`PrettySpace`](/reference/interfaces/formats/PrettySpace) format in that up to `10,000` rows are buffered, 
and then output as a single table, and not by [blocks](/development/architecture#block).

## Example usage [#example-usage]

## Format settings [#format-settings]

<PrettyFormatSettings/>
