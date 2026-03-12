# Source: https://clickhouse.ferndocs.com/reference/interfaces/formats/PrettyCompactNoEscapesMonoBlock.md

---
alias: []
description: Documentation for the PrettyCompactNoEscapesMonoBlock format
input_format: false
keywords:

- PrettyCompactNoEscapesMonoBlock
output_format: true
slug: /interfaces/formats/PrettyCompactNoEscapesMonoBlock
title: PrettyCompactNoEscapesMonoBlock <Badge intent="success">Output</Badge>
doc_type: reference

---

import PrettyFormatSettings from './_snippets/common-pretty-format-settings.md';

## Description [#description]

Differs from the [`PrettyCompactNoEscapes`](/reference/interfaces/formats/PrettyCompactNoEscapes) format in that up to `10,000` rows are buffered,
and then output as a single table, and not by [blocks](/development/architecture#block).

## Example usage [#example-usage]

## Format settings [#format-settings]

<PrettyFormatSettings/>
