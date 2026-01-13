# Advanced Testing Implementation Checklist

Use this checklist to progressively implement advanced testing practices in your project.

## Phase 1: Foundation (Days 1-3)

### Setup Unit Testing with Snapshots

- [ ] **Python Projects**
  - [ ] Install pytest: `pip install pytest`
  - [ ] Install snapshot plugin: `pip install pytest-snapshot`
  - [ ] Create `tests/` directory
  - [ ] Write 10 unit tests with snapshots
  - [ ] Run: `pytest --snapshot-update`
  - [ ] Verify `.snapshot.json` files created
  - [ ] Commit snapshots to git

- [ ] **JavaScript/TypeScript Projects**
  - [ ] Install Jest or Vitest
  - [ ] Create `__tests__/` or `.test.ts` files
  - [ ] Write 10 unit tests with `toMatchSnapshot()`
  - [ ] Run: `npm test -- -u`
  - [ ] Verify `__snapshots__/` directories created
  - [ ] Commit snapshots to git
  - [ ] Update package.json test script

- [ ] **Rust Projects**
  - [ ] Create `tests/` directory
  - [ ] Install insta: `cargo add insta --dev`
  - [ ] Write 5 unit tests with snapshots
  - [ ] Run: `cargo test --test '*'`
  - [ ] Review snapshots: `cargo insta review`
  - [ ] Accept and commit snapshots

### Pre-commit Hooks

- [ ] **Install pre-commit framework**
  - [ ] `pip install pre-commit` or `npm install husky --save-dev`
  - [ ] Create `.pre-commit-config.yaml` or `.husky/pre-commit`

- [ ] **Configure pre-commit checks**
  - [ ] Lint check (eslint, pylint)
  - [ ] Format check (prettier, black)
  - [ ] Type check (TypeScript, mypy)
  - [ ] Unit tests run successfully
  - [ ] Snapshots committed
  - [ ] No large test files added

- [ ] **Test pre-commit hooks**
  - [ ] Modify file and commit
  - [ ] Verify hooks run
  - [ ] Verify failures block commits

### Code Coverage Baseline

- [ ] **Generate coverage report**
  - [ ] Python: `pip install coverage && coverage run -m pytest && coverage report`
  - [ ] JavaScript: `npm test -- --coverage`
  - [ ] Rust: `cargo tarpaulin`

- [ ] **Set coverage target**
  - [ ] Record baseline percentage (e.g., 65%)
  - [ ] Set team goal (e.g., >90%)
  - [ ] Create issue to improve coverage

- [ ] **Integrate with CI/CD**
  - [ ] Add coverage to GitHub Actions/GitLab CI
  - [ ] Generate coverage badge
  - [ ] Fail builds below threshold

---

## Phase 2: Property-Based Testing (Days 4-7)

### Choose Framework

- [ ] **Python**
  - [ ] Install Hypothesis: `pip install hypothesis`
  - [ ] Read quickstart: https://hypothesis.readthedocs.io/quickstart.html
  - [ ] Pick 3-5 critical functions

- [ ] **JavaScript/TypeScript**
  - [ ] Install fast-check: `npm install --save-dev fast-check`
  - [ ] Read documentation: https://fast-check.dev/
  - [ ] Pick 3-5 critical functions

- [ ] **Rust**
  - [ ] Install proptest: `cargo add proptest --dev`
  - [ ] Read documentation: https://docs.rs/proptest/
  - [ ] Pick 3-5 critical functions

### Write First Property Tests

For each critical function:

- [ ] **Understand the function**
  - [ ] What inputs are valid?
  - [ ] What properties should always hold?
  - [ ] What edge cases matter?

- [ ] **Define properties**
  - [ ] Identity properties: `f(x) == f(f(x))`?
  - [ ] Inverse properties: Does `g(f(x)) == x`?
  - [ ] Structural properties: Length, ordering, etc.
  - [ ] Invariant properties: Constraints that always hold

- [ ] **Write tests**
  - [ ] Use framework strategies for input generation
  - [ ] Write 3-5 properties per function
  - [ ] Add 3-5 edge case examples
  - [ ] Run locally: `pytest --hypothesis-profile=dev`
  - [ ] Verify all pass

- [ ] **Examples to write**
  - [ ] Sorting function: maintains length, sorted order, same elements
  - [ ] Parser: parses valid input, rejects invalid input
  - [ ] JSON roundtrip: `loads(dumps(x)) == x`
  - [ ] Database query: returns expected type

### Integrate into CI

- [ ] **Add to test suite**
  - [ ] Create separate test file or mark tests
  - [ ] Add to CI pipeline
  - [ ] Set reasonable timeout (30 minutes max)

- [ ] **Run property tests locally**
  - [ ] `pytest tests/test_properties.py`
  - [ ] Verify examples found and minimized
  - [ ] Record baseline run time

---

## Phase 3: Mutation Testing (Days 8-10)

### Setup Mutation Framework

- [ ] **Python (mutmut)**
  - [ ] Install: `pip install mutmut`
  - [ ] Run on one module: `mutmut run --tests-dir tests -p src/one_module.py`
  - [ ] Browse results: `mutmut browse`

- [ ] **JavaScript (Stryker)**
  - [ ] Install: `npm install --save-dev @stryker-mutator/core`
  - [ ] Run setup: `npx stryker init`
  - [ ] Review stryker.conf.js
  - [ ] Run on one directory: `npx stryker run`

- [ ] **Java (PIT)**
  - [ ] Add Maven plugin: `mvn org.pitest:pitest-maven:mutationCoverage`
  - [ ] Review target-mut.xml output

### Analyze Results

- [ ] **Run mutation testing**
  - [ ] Get baseline mutation score
  - [ ] Identify surviving mutants
  - [ ] Read mutation report

- [ ] **Understand results**
  - [ ] What mutants survived?
  - [ ] Do they indicate missing tests?
  - [ ] Are some survivals acceptable?

- [ ] **Improve tests**
  - [ ] Pick top 3 surviving mutants
  - [ ] Write tests to kill each
  - [ ] Re-run mutation testing
  - [ ] Verify kill rate improved

### Set Targets

- [ ] **Establish mutation kill rate goal**
  - [ ] Current baseline: ____%
  - [ ] Team target: >80%
  - [ ] Target modules: (list)

- [ ] **Document acceptable mutations**
  - [ ] Some mutants may be acceptable (version strings, etc.)
  - [ ] Document why each is acceptable
  - [ ] Whitelist in tool configuration

---

## Phase 4: Fuzzing (Days 11-14)

### Identify Fuzzing Targets

- [ ] **Security-critical code**
  - [ ] Parsers (JSON, XML, protobuf)
  - [ ] Validators (email, phone, URLs)
  - [ ] Protocol handlers
  - [ ] File format handlers

- [ ] **Complex input handling**
  - [ ] Regular expression engines
  - [ ] String manipulation
  - [ ] Serialization/deserialization
  - [ ] Image/media processing

- [ ] **Pick top 3 targets**
  - [ ] Target 1: ___________
  - [ ] Target 2: ___________
  - [ ] Target 3: ___________

### Setup Fuzzing

- [ ] **Python (Atheris)**
  - [ ] Install: `pip install atheris`
  - [ ] Read intro: https://seeinglogic.com/posts/intro-to-atheris/
  - [ ] Write fuzz target
  - [ ] Create corpus/  directory with seed inputs
  - [ ] Run: `python fuzz_target.py`

- [ ] **Rust (cargo-fuzz)**
  - [ ] Install: `cargo install cargo-fuzz`
  - [ ] Initialize: `cargo fuzz init`
  - [ ] Write fuzz target in fuzz/fuzz_targets/
  - [ ] Create corpus/fuzz_target_1/ with seeds
  - [ ] Run: `cargo fuzz run fuzz_target_1`

- [ ] **C/C++ (libFuzzer)**
  - [ ] Install LLVM/Clang
  - [ ] Write LLVMFuzzerTestOneInput function
  - [ ] Compile with -fsanitize=fuzzer
  - [ ] Create corpus directory
  - [ ] Run fuzzer binary

### Run Fuzzing Campaigns

- [ ] **Initial run (1 hour)**
  - [ ] Run fuzzer on target
  - [ ] Document baseline coverage
  - [ ] Note any crashes/hangs

- [ ] **Extended run (overnight)**
  - [ ] Schedule 8-12 hour campaign
  - [ ] Monitor for crashes
  - [ ] Triage any findings

- [ ] **Production run (continuous)**
  - [ ] Set up continuous fuzzing in CI
  - [ ] Use OSS-Fuzz or equivalent
  - [ ] Review crashes weekly

### Triage Findings

- [ ] **For each crash found**
  - [ ] [ ] Understand root cause
  - [ ] [ ] Create test case
  - [ ] [ ] Fix bug or document known issue
  - [ ] [ ] Add to regression tests

- [ ] **Document process**
  - [ ] Create FUZZING.md with:
    - [ ] How to run each target
    - [ ] Known crashes and status
    - [ ] Corpus organization

---

## Phase 5: CI/CD Integration (Days 15-17)

### Setup CI Pipeline

- [ ] **GitHub Actions**
  - [ ] Create `.github/workflows/test.yml`
  - [ ] Add job: unit tests + snapshots
  - [ ] Add job: property-based tests (timeout 30m)
  - [ ] Add job: mutation tests (PR only, timeout 20m)
  - [ ] Add job: fuzz (scheduled, timeout 2h)

- [ ] **GitLab CI**
  - [ ] Create `.gitlab-ci.yml`
  - [ ] Add unit test stage
  - [ ] Add property test stage
  - [ ] Add mutation test stage
  - [ ] Add fuzz stage

- [ ] **Jenkins/Other**
  - [ ] Create pipeline stages
  - [ ] Set appropriate timeouts
  - [ ] Configure artifacts and reports

### Reports and Metrics

- [ ] **Add coverage reporting**
  - [ ] Generate coverage XML
  - [ ] Upload to Codecov/Coveralls
  - [ ] Add coverage badge to README

- [ ] **Add mutation reports**
  - [ ] Generate HTML mutation report
  - [ ] Store as CI artifact
  - [ ] Link in PR comments

- [ ] **Create metrics dashboard**
  - [ ] Track coverage over time
  - [ ] Track mutation kill rate
  - [ ] Track fuzzing status

---

## Phase 6: Team Adoption (Days 18-21)

### Documentation

- [ ] **Create TESTING.md guide**
  - [ ] How to run tests locally
  - [ ] How to write each test type
  - [ ] Examples for each type
  - [ ] Troubleshooting tips

- [ ] **Update project README**
  - [ ] Add "Testing" section
  - [ ] Link to TESTING.md
  - [ ] Show test commands

- [ ] **Document best practices**
  - [ ] Property test guidelines
  - [ ] Snapshot review process
  - [ ] Mutation test interpretation
  - [ ] Fuzzing target selection

### Training

- [ ] **Team training session**
  - [ ] 15 min: Overview of all approaches
  - [ ] 20 min: Writing property tests (demo)
  - [ ] 15 min: Understanding mutation results (demo)
  - [ ] 10 min: Q&A and concerns

- [ ] **Pair programming**
  - [ ] Write first property test together
  - [ ] Review mutation results together
  - [ ] Debug fuzzing crash together

- [ ] **Create code examples**
  - [ ] Example property tests in repo
  - [ ] Example mutation improvements
  - [ ] Example fuzz target

### Governance

- [ ] **Establish team standards**
  - [ ] Minimum code coverage: ____%
  - [ ] Minimum mutation kill rate: ____%
  - [ ] Required snapshot review
  - [ ] Fuzz target policy

- [ ] **Setup PR checks**
  - [ ] Block PRs below coverage threshold
  - [ ] Require snapshot review
  - [ ] Optional mutation report in PR

- [ ] **Plan ongoing efforts**
  - [ ] Monthly mutation testing run
  - [ ] Quarterly fuzzing sprint
  - [ ] Continuous property test addition

---

## Validation Checklist

After completing all phases, verify:

- [ ] **Unit tests pass locally and in CI**
- [ ] **Snapshots are reviewed and committed**
- [ ] **Property tests run on 5+ critical functions**
- [ ] **Mutation kill rate is >75%**
- [ ] **At least 3 fuzzing targets exist**
- [ ] **CI/CD pipeline runs all test types**
- [ ] **Team has received training**
- [ ] **Documentation exists for all approaches**
- [ ] **Coverage reports visible in CI**
- [ ] **No test failures in main branch**

---

## Troubleshooting

### Property Tests Are Slow
- [ ] Reduce example count in settings
- [ ] Use smaller strategies (bounded integers)
- [ ] Only run on CI, not locally
- [ ] Mark some as "integration" tests

### Mutation Testing Takes Too Long
- [ ] Run only on changed files
- [ ] Run only on main branch, not every PR
- [ ] Focus on critical modules only
- [ ] Increase parallel workers

### Snapshots Failing Often
- [ ] Check if output is deterministic
- [ ] Exclude timestamps/UUIDs from snapshots
- [ ] Review all changes carefully in UI
- [ ] Use interactive update mode

### Fuzzing Finds Nothing
- [ ] Increase fuzzing time (8+ hours)
- [ ] Improve seed corpus quality
- [ ] Add assertions for invariants
- [ ] Use sanitizers (ASAN, UBSAN)

### Team Adoption Issues
- [ ] Start with snapshots (easiest)
- [ ] Show value with examples
- [ ] Make tests fast (critical!)
- [ ] Provide clear documentation

---

## Success Metrics

Track these metrics after implementation:

| Metric | Target | Timeline |
|--------|--------|----------|
| Code Coverage | >90% | Week 2 |
| Snapshot Tests | 50+ | Week 3 |
| Property Tests | 10+ | Week 4 |
| Mutation Kill Rate | >80% | Week 6 |
| Fuzzing Targets | 3+ | Week 7 |
| CI Test Time | <10 min (unit+snapshot) | Ongoing |
| Team Adoption | 80%+ writing tests | Week 8 |

---

## Completion Certificate

When you've completed all phases:

```
This project has implemented:

✓ Unit Testing with Snapshots
✓ Property-Based Testing
✓ Mutation Testing
✓ Fuzzing
✓ CI/CD Integration
✓ Team Training
✓ Documentation

Date Completed: _____________
Team Lead: _________________
```

---

**Total Implementation Time**: 2-3 weeks
**Maintenance Effort**: 1-2 hours/week
**Long-term ROI**: Very High (catches bugs before production)

Good luck! Questions? See the ADVANCED_TESTING_METHODOLOGIES.md guide.
