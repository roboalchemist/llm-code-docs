# Source: https://pkg.go.dev/golang.org/x/perf/cmd/benchstat

# Benchstat: Statistical Analysis for Go Benchmarks

Benchstat computes statistical summaries and A/B comparisons of Go benchmarks.

## Overview

Benchstat is a command-line tool from the golang.org/x/perf package that analyzes Go benchmark results. It provides statistical summaries with confidence intervals and performs A/B comparisons to determine if performance changes are statistically significant.

## Usage

```
benchstat [flags] inputs...
```

Each input file should be in the Go benchmark format (https://golang.org/design/14313-benchmark-format), such as the output of `go test -bench .`.

## Getting Started

### Installation

```bash
go install golang.org/x/perf/cmd/benchstat@latest
```

### Basic Example

Collect benchmark results before a change:
```bash
go test -run='^$' -bench=. -count=10 > old.txt
```

Collect benchmark results after the change:
```bash
go test -run='^$' -bench=. -count=10 > new.txt
```

Compare the results:
```bash
benchstat old.txt new.txt
```

### Benchmark File Format

Example benchmark file format:
```
goos: linux
goarch: amd64
pkg: golang.org/x/perf/cmd/benchstat/testdata
BenchmarkEncode/format=json-48         	  690848	      1726 ns/op
BenchmarkEncode/format=json-48         	  684861	      1723 ns/op
BenchmarkEncode/format=json-48         	  693285	      1707 ns/op
BenchmarkEncode/format=gob-48          	  372699	      3069 ns/op
BenchmarkEncode/format=gob-48          	  394740	      3075 ns/op
```

The order of lines in the file does not matter, except that the output lists benchmarks in order of appearance.

## Output Format

### Example Comparison Output

```
$ benchstat old.txt new.txt
goos: linux
goarch: amd64
pkg: golang.org/x/perf/cmd/benchstat/testdata
                      │   old.txt   │               new.txt               │
                      │   sec/op    │   sec/op     vs base                │
Encode/format=json-48   1.718µ ± 1%   1.423µ ± 1%  -17.20% (p=0.000 n=10)
Encode/format=gob-48    3.066µ ± 0%   3.070µ ± 2%        ~ (p=0.446 n=10)
geomean                 2.295µ        2.090µ        -8.94%
```

### Understanding the Output

- **Median**: Shows the median value with 95% confidence interval
- **vs base**: Percentage change compared to baseline
- **p-value**: Probability that differences are due to random chance (lower = more significant)
- **n**: Number of samples from each input file
- **~**: No statistically significant difference detected

### Geomean Row

The last row shows the geometric mean of each column, giving an overall picture of how benchmarks changed. Proportional changes in the geomean reflect proportional changes in the benchmarks.

For n benchmarks, if sec/op for one increases by a factor of 2, then the sec/op geomean will increase by a factor of ⁿ√2.

## Filtering

Benchstat has a flexible filtering system to configure which benchmarks are summarized and compared. Use the `-filter` flag to filter inputs.

### Filter Syntax

Basic filter terms:
```
key:value        - Match if key equals value
key:"value"      - Value is a double-quoted string (can contain spaces)
"key":value      - Keys may also be double-quoted
key:/regexp/     - Match if key matches a regular expression
key:(val1 OR val2 OR ...)  - Short-hand for key:val1 OR key:val2
*                - Match everything
```

Combining terms:
```
x y ...          - Match if x, y, etc. all match
x AND y          - Same as x y
x OR y           - Match if x or y match
-x               - Match if x does not match
(...)            - Subexpression
```

### Filter Keys

- `.name` - The base name of a benchmark
- `.fullname` - The full name of a benchmark (including configuration)
- `.file` - The name of the input file or user-provided file label
- `/{name-key}` - Per-benchmark sub-name configuration key
- `{file-key}` - File-level configuration key
- `.unit` - The name of a unit for a particular metric

### Filter Example

```bash
benchstat -filter "/format:json goos:linux .unit:(ns/op OR B/op)" old.txt new.txt
```

This matches benchmarks with "/format=json" in the sub-name keys, file-level configuration "goos" equal to "linux", and extracts "ns/op" and "B/op" measurements.

## Configuring Comparisons

Configure how benchstat groups and compares results using flags:

- `-table KEYS` - Group results into tables by KEYS (default: `.config`)
- `-row KEYS` - Group results into table rows by KEYS (default: `.fullname`)
- `-col KEYS` - Compare across columns with different values of KEYS (default: `.file`)
- `-ignore KEYS` - Keys to ignore when grouping results

Each KEYS argument is a comma- or space-separated list of keys.

### Comparison Keys

- `.name` - The base name of a benchmark
- `.fullname` - The full name of a benchmark (including configuration)
- `.file` - The name of the input file or user-provided file label
- `/{name-key}` - Per-benchmark sub-name configuration key
- `{file-key}` - File-level configuration key
- `.config` - All file-level configuration keys

### Projection Examples

#### Default Projection

```bash
benchstat -table .config -row .fullname -col .file old.txt new.txt
```

Groups all benchmarks into one table (when they have same config), rows by full name, columns by file.

#### Compare Encoding Formats

Compare json encoding to gob encoding from the same file:

```bash
benchstat -col /format new.txt
```

Output:
```
goos: linux
goarch: amd64
pkg: golang.org/x/perf/cmd/benchstat/testdata
          │    json     │                 gob                  │
          │   sec/op    │   sec/op     vs base                 │
Encode-48   1.423µ ± 1%   3.070µ ± 2%  +115.82% (p=0.000 n=10)
```

#### Simplify by Benchmark Name

```bash
benchstat -col /format -row .name new.txt
```

Groups rows by benchmark name rather than full name.

#### Warning on Information Loss

```bash
benchstat -row .name new.txt
```

Output:
```
goos: linux
goarch: amd64
pkg: golang.org/x/perf/cmd/benchstat/testdata
       │    new.txt     │
       │     sec/op     │
Encode   2.253µ ± 37% ¹
¹ benchmarks vary in .fullname
```

Benchstat warns when projections strip away information, indicating that results were grouped in a potentially meaningless way.

## Sorting

By default, benchstat sorts by order of first observation. Override using the following syntax:

- `{key}@{order}` - Specifies built-in sort order: "alpha" (alphabetic) or "num" (numeric, understands metric/IEC prefixes like "2k", "1Mi")
- `{key}@({value} {value} ...)` - Specifies a fixed value order

### Sorting Example

Compare json improvement over gob:

```bash
benchstat -col "/format@(gob json)" -row .name -ignore .file new.txt
```

Output:
```
goos: linux
goarch: amd64
pkg: golang.org/x/perf/cmd/benchstat/testdata
       │     gob     │                json                 │
       │   sec/op    │   sec/op     vs base                │
Encode   3.070µ ± 2%   1.423µ ± 1%  -53.66% (p=0.000 n=10)
```

## Custom File Labels

Override file name labels by specifying input as `label=path` instead of just `path`.

```bash
benchstat O=old.txt N=new.txt
```

Output:
```
goos: linux
goarch: amd64
pkg: golang.org/x/perf/cmd/benchstat/testdata
                      │      O      │                  N                  │
                      │   sec/op    │   sec/op     vs base                │
Encode/format=json-48   1.718µ ± 1%   1.423µ ± 1%  -17.20% (p=0.000 n=10)
Encode/format=gob-48    3.066µ ± 0%   3.070µ ± 2%        ~ (p=0.446 n=10)
geomean                 2.295µ        2.090µ        -8.94%
```

## Units

Benchstat normalizes units:
- "ns" → "sec"
- "MB" → "B"

This avoids creating nonsense units like "µns/op" that appear in Go's default metrics.

### Custom Unit Metadata

Benchstat supports custom unit metadata for controlling statistics (see https://golang.org/design/14313-benchmark-format).

The "assume" metadata is useful for controlling statistics:

- **assume=nothing** (default): Non-parametric statistics
  - Median for summaries
  - Mann-Whitney U-test for A/B comparisons

- **assume=exact**: For measurements with no noise (e.g., binary sizes)
  - Warns if there's any variation in measured values
  - Shows A/B comparisons even with single before/after measurement

## Best Practices for Benchmarking

### Run Count

- Typically run benchmarks **at least 10 times**
- More runs provide statistically significant results
- Ideally, use **20+ runs**
- Pick a number and stick to it

### Noise Reduction

To reduce noise and get more reliable results:

1. **Run on idle machine** - Stop unnecessary background processes
2. **Disable power management** - Avoid battery mode and thermal throttling
3. **Interleave runs** - Mix before and after runs rather than running all before, then all after
4. **Pre-compile benchmarks** - Use `go test -c` to compile benchmark binary first
5. **See https://llvm.org/docs/Benchmarking.html** - Many additional tips on reducing benchmark noise

### Statistical Considerations

1. **Avoid multiple testing** - Don't rerun benchmarks until you see a significant change
   - Default α threshold is 0.05 (5% expected false positive rate)
   - Rerunning creates statistical bias

2. **Expect false positives** - With large numbers of benchmarks, ~5% will show "significant" differences even without actual changes

3. **Distinguish between significance and magnitude** - Statistically significant ≠ large change
   - With low-noise data, even tiny changes can be statistically significant
   - Large changes are easier to distinguish from noise

### Benchmark File Order

The order of lines in a benchmark file does not matter, except that output lists benchmarks in order of appearance.

## Advanced Usage

### Multiple Comparisons

Compare multiple files at once:

```bash
benchstat old.txt new1.txt new2.txt
```

This creates separate columns for each comparison file.

### Filtering and Comparing

Combine filtering with comparison:

```bash
benchstat -filter "goos:linux" old.txt new.txt
```

### Complex Projections

For detailed statistics reference, see https://pkg.go.dev/golang.org/x/perf/benchproc/syntax

## Common Workflows

### Before/After Analysis

```bash
# Collect baseline
go test -run='^$' -bench=BenchmarkEncode -count=20 > baseline.txt

# Make changes
# ... edit code ...

# Collect new results
go test -run='^$' -bench=BenchmarkEncode -count=20 > current.txt

# Compare
benchstat baseline.txt current.txt
```

### Compare Implementations

```bash
# Collect results from different implementations
benchstat impl1.txt impl2.txt impl3.txt
```

### Filter by Platform

```bash
benchstat -table "goos,goarch" -col .file old.txt new.txt
```

Creates separate tables for each operating system and architecture combination.

## Related Tools

- **benchproc** - Processing and filtering benchmark results
- **benchmath** - Mathematical functions for benchmark statistics
- **See https://pkg.go.dev/golang.org/x/perf** - Full golang.org/x/perf documentation

## Source

- **Repository**: https://github.com/golang/perf
- **Package**: golang.org/x/perf/cmd/benchstat
- **Documentation**: https://pkg.go.dev/golang.org/x/perf/cmd/benchstat
- **Design Document**: https://golang.org/design/14313-benchmark-format
