# arXiv Identifier Information

## Current Scheme (Since April 1, 2007)

The modern format follows: `arXiv:YYMM.number` with an optional version suffix.

### Structure

- `YY` = Two-digit year (07-99, potentially up to 06 for 2106)
- `MM` = Two-digit month (01-12)
- `number` = Sequence number, zero-padded to 4 digits (0704-1412) or 5 digits (1501+)
- `vV` = Optional version marker (e.g., v1, v2)

### Examples

- `arXiv:1501.00001`
- `arXiv:0706.0001v2`

The canonical form references the most recent version when the version number is omitted.

## Legacy Scheme (1991-March 2007)

The older format included archive and subject class information: `archive/YYMMNNN` or `archive.subclass/YYMMNNN`

Examples:

- `astro-ph/0107001`
- `math.GT/0503100`

## Key Changes in 2007

The revision separated identification from classification, allowing articles to be reclassified without changing their identifiers. The old scheme limited submissions to 999 per month per archive.

## Five-Digit Update (January 2015)

As of 1501, sequence numbers expanded to 5 digits to accommodate "more than 9999 submissions per month."

## Identifier Use in API

When using the arXiv API, you can reference articles by:

- **Latest version**: Use ID without version suffix (e.g., `1501.00001`)
- **Specific version**: Append version marker (e.g., `1501.00001v1`)
- **Legacy identifiers**: Old format IDs still work (e.g., `astro-ph/0107001`)

### API Query Examples

```text
http://export.arxiv.org/api/query?id_list=1501.00001        (latest version)
http://export.arxiv.org/api/query?id_list=1501.00001v1      (version 1)
http://export.arxiv.org/api/query?id_list=astro-ph/0107001  (legacy format)
```
