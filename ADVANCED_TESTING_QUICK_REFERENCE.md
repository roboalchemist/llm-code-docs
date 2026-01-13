# Advanced Testing Quick Reference Guide (2025)

## At a Glance

| Testing Type | Purpose | When to Use | Tools | Speed | Complexity |
|--------------|---------|------------|-------|-------|------------|
| **Property-Based** | Find edge cases | Algorithm logic | Hypothesis, fast-check | Medium | Medium |
| **Snapshot** | Detect regressions | UI/API output | Jest, Vitest, Playwright | Fast | Low |
| **Mutation** | Validate test quality | Improve tests | Stryker, mutmut, PIT | Slow | Low |
| **Fuzzing** | Discover crashes | Security/robustness | Atheris, libFuzzer, AFL++ | Very Slow | High |

---

## Quick Setup by Language

### Python
```bash
# Install testing tools
pip install pytest hypothesis atheris mutmut

# Property-based test
python -m pytest --hypothesis-profile=ci

# Mutation testing
mutmut run
mutmut browse

# Fuzzing
python fuzzer.py
```

### JavaScript/TypeScript
```bash
# Install
npm install --save-dev jest vitest fast-check @stryker-mutator/core

# Run tests with snapshots
npm test -- --updateSnapshot

# Mutation testing
npx stryker run

# Property-based tests
npx vitest --reporter=verbose
```

### Rust
```bash
# Add to Cargo.toml
[dev-dependencies]
proptest = "1.4"
criterion = "0.5"

[target.'cfg(fuzzing)'.dependencies]
libfuzzer-sys = "0.4"

# Fuzz testing
cargo fuzz run fuzz_target_1

# Property tests
cargo test --test '*' -- --nocapture
```

### Java
```bash
# Maven mutation testing
mvn org.pitest:pitest-maven:mutationCoverage

# Fuzzing with Jazzer
bazel run //target:fuzz_test
```

---

## Framework Decision Tree

```
START: "I need to improve testing"
│
├─→ "Catch regressions?"
│   ├─→ YES → Use SNAPSHOT TESTING (Jest, Playwright)
│   └─→ NO → Continue
│
├─→ "Test algorithm correctness?"
│   ├─→ YES → Use PROPERTY-BASED TESTING (Hypothesis, fast-check)
│   └─→ NO → Continue
│
├─→ "Evaluate test quality?"
│   ├─→ YES → Use MUTATION TESTING (Stryker, mutmut)
│   └─→ NO → Continue
│
└─→ "Find crashes/vulnerabilities?"
    ├─→ YES → Use FUZZING (libFuzzer, Atheris, cargo-fuzz)
    └─→ NO → Use STANDARD UNIT TESTS
```

---

## Setup Checklist

### Step 1: Unit + Snapshot Tests (Week 1)
```bash
# JavaScript
npm test

# Python
pytest

# Rust
cargo test

# Check snapshots are committed
git add **/*.snap
git commit -m "Add snapshot tests"
```

### Step 2: Property-Based Tests (Week 2)
```javascript
// JavaScript example
import fc from 'fast-check';

describe('Sorting', () => {
  it('should be sorted after sort()', () => {
    fc.assert(
      fc.property(fc.array(fc.integer()), arr => {
        const sorted = [...arr].sort((a, b) => a - b);
        return sorted.every((v, i, a) => !i || a[i - 1] <= v);
      })
    );
  });
});
```

```python
# Python example
from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_sort(arr):
    sorted_arr = sorted(arr)
    assert all(sorted_arr[i] <= sorted_arr[i+1]
               for i in range(len(sorted_arr)-1))
```

### Step 3: Mutation Testing (Week 3)
```bash
# JavaScript
npx stryker init
npx stryker run

# Python
mutmut run
mutmut browse

# Target: >80% mutation kill rate
```

### Step 4: Fuzzing (Week 4+)
```bash
# Python - High-value targets only (parsers, validators)
pip install atheris
python fuzzer.py

# Rust
cargo fuzz list
cargo fuzz run fuzz_target_1 -- -artifact_prefix=crash_
```

---

## Common Patterns

### Pattern: Sort Function
```python
# Test with all 3 methods
from hypothesis import given, strategies as st

# Unit test
def test_sort_basic():
    assert sort([3, 1, 2]) == [1, 2, 3]

# Property test
@given(st.lists(st.integers()))
def test_sort_properties(arr):
    result = sort(arr)
    assert len(result) == len(arr)  # Same length
    assert set(result) == set(arr)  # Same elements
    assert all(result[i] <= result[i+1] for i in range(len(result)-1))  # Sorted

# Snapshot test (for output format)
def test_sort_output_format():
    assert snapshot(sort([3, 1, 2])) == [1, 2, 3]
```

### Pattern: JSON Parser
```python
# Fuzzing target (highest value - finds crashes)
import atheris
import json

@atheris.instrument_func
def test_json_fuzzing(data):
    try:
        json.loads(data)
    except (ValueError, json.JSONDecodeError):
        pass  # Expected

atheris.Setup(sys.argv, test_json_fuzzing)

# Property-based (catches logic errors)
@given(st.dictionaries(st.text(), st.integers()))
def test_json_roundtrip(data):
    json_str = json.dumps(data)
    result = json.loads(json_str)
    assert result == data

# Unit + snapshot (regression detection)
def test_json_parsing():
    assert snapshot(parse_json('{"a": 1}')) == {'a': 1}
```

### Pattern: API Validation
```javascript
// Property-based for valid inputs
it('valid email returns true', () => {
  fc.assert(
    fc.property(fc.emailAddress(), email => {
      return validateEmail(email) === true;
    })
  );
});

// Fuzzing for invalid inputs
it('should not crash on malicious input', () => {
  fc.assert(
    fc.property(fc.string(), input => {
      try {
        validateEmail(input);
        return true; // No crash
      } catch {
        return false;
      }
    })
  );
});

// Snapshot for expected outputs
it('validation messages match expected', () => {
  expect(validateEmail('invalid')).toMatchSnapshot();
});
```

---

## Performance Expectations

| Framework | Test Type | 100 Tests | 1000 Tests | Notes |
|-----------|-----------|-----------|-----------|-------|
| Jest/Vitest | Unit + Snapshot | < 5s | 10-30s | Fast, parallelizable |
| fast-check | Property-based | 10-30s | 60-120s | Generates many inputs |
| Hypothesis | Property-based | 5-15s | 30-90s | Python, good shrinking |
| Stryker | Mutation | 2-5 min | 10-30 min | Per mutation run |
| mutmut | Mutation (Python) | 1-3 min | 5-15 min | Faster than Stryker |
| libFuzzer | Fuzzing | 10 min+ | Hours | Improves with time |
| Atheris | Fuzzing (Python) | 10 min+ | Hours | Explores input space |

---

## CI/CD Pipeline Example

### GitHub Actions (All Languages)
```yaml
name: Complete Testing

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [18.x, 20.x]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'

      # Unit tests with snapshots (fast)
      - name: Unit tests
        run: npm test -- --coverage
        timeout-minutes: 10

      # Lint commit
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/coverage-final.json

      # Property-based tests (medium time)
      - name: Property tests
        run: npm run test:property
        timeout-minutes: 30

      # Mutation tests (only on PRs, slower)
      - name: Mutation tests
        if: github.event_name == 'pull_request'
        run: npm run test:mutation:changed-only
        timeout-minutes: 20

  fuzz:
    # Only on specific labels or nightly
    if: contains(github.event.pull_request.labels.*.name, 'security') || github.event_name == 'schedule'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Fuzz test
        run: |
          pip install atheris
          python fuzz_test.py
        timeout-minutes: 60
```

---

## Common Issues & Solutions

### Issue: Snapshots always failing
```bash
# Solution 1: Check if output is deterministic
# Some outputs include timestamps, UUIDs, etc.

# Solution 2: Update snapshots intentionally
npm test -- -u  # Jest
pytest --snapshot-update  # pytest

# Solution 3: Check git - snapshots must be committed
git add **/*.snap
git commit -m "Update snapshots"
```

### Issue: Property tests are slow
```bash
# Solution 1: Reduce example count
@settings(max_examples=100)  # Hypothesis
fc.settings({ numRuns: 100 })  # fast-check

# Solution 2: Use simpler strategies
st.integers(min_value=0, max_value=1000)  # Bounded
fc.integer({min: 0, max: 1000})  # fast-check

# Solution 3: Run on CI only, locally use --hypothesis-profile=dev
```

### Issue: Mutation tests killing too many mutants
```bash
# Solution 1: Your tests are too strict (actually good!)
# But some mutations may be trivial

# Solution 2: Whitelist certain mutants
@pytest.mark.skip_mutants(['RemoveConditionals'])
def test_something(): ...

# Solution 3: Accept >80% is "good enough"
# Don't aim for 100%
```

### Issue: Fuzzing finds no crashes
```bash
# Solution 1: Increase fuzzing time
cargo fuzz run fuzz_target_1 -- -max_total_time=3600

# Solution 2: Provide good seed corpus
ls fuzz/corpus/fuzz_target_1/ | wc -l  # Check corpus size

# Solution 3: Add assertions for invariants
assert len(output) >= len(input)  # Example invariant
```

---

## Testing Metrics to Track

```javascript
// Create dashboard
const metrics = {
  // Unit tests
  coverage: 92,                    // Target: >90%
  unitTestCount: 350,              // Growing over time

  // Snapshots
  snapshotTests: 45,               // Growing with features
  snapshotFailures: 0,             // Should be 0 or require investigation

  // Property-based
  propertyTestCount: 12,           // At least 1-2 per critical module
  propertyFailures: 0,             // Any failure is critical

  // Mutation testing
  mutationKillRate: 87,            // Target: >80%
  mutantsSurvived: 15,             // Identify gaps

  // Fuzzing
  fuzzingHoursCampaigned: 256,     // Total fuzzing time
  crashesFound: 2,                 // Security issues
  uniqueCoverageAchieved: 4200     // Unique code paths
};

// Report
console.table(metrics);
```

---

## Tool Comparison Matrix

### By Ease of Setup
1. **Snapshot** (Jest) - One liner
2. **Unit Tests** - Immediate
3. **Property-Based** - Few minutes
4. **Mutation** - 5-10 minutes
5. **Fuzzing** - 15-30 minutes

### By Effectiveness
1. **Fuzzing** - Finds unknown bugs
2. **Mutation** - Validates test quality
3. **Property-Based** - Finds edge cases
4. **Snapshot** - Catches regressions
5. **Unit** - Baseline coverage

### By Time Investment
1. **Snapshot** - Seconds per snapshot
2. **Unit** - Minutes to write
3. **Property** - Hours to define properties
4. **Mutation** - Hours to improve tests
5. **Fuzzing** - Days/weeks of campaigns

---

## Resources

### Documentation
- Hypothesis: https://hypothesis.readthedocs.io/quickstart.html
- fast-check: https://fast-check.dev/api/interfaces/IAsyncProperty.html
- Stryker: https://stryker-mutator.io/docs/stryker-js/getting-started/
- mutmut: https://mutmut.readthedocs.io/
- Atheris: https://github.com/google/atheris#getting-started

### Tutorials
- "Property-based Testing Explained": https://unzip.dev/0x009-property-based-testing/
- "Getting Started with Mutation Testing": https://about.codecov.io/blog/getting-started-with-mutation-testing-in-python-with-mutmut/
- "Fuzzing with Atheris": https://seeinglogic.com/posts/intro-to-atheris/

### Tools
- Compare frameworks: https://github.com/jmid/pbt-frameworks
- Stryker Playground: https://stryker-mutator.io/stryker-playground/

---

## One-Minute Summary

Start with **unit tests + snapshots** (your baseline). Add **property-based tests** for algorithms. Use **mutation testing** to validate your tests are effective. Finally, apply **fuzzing** to security-critical code. Integrate all into CI/CD and track metrics.

---

**Last Updated**: January 2026
