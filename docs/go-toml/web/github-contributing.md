# go-toml Contributing Guide

Source: https://github.com/pelletier/go-toml/blob/v2/CONTRIBUTING.md

## Ways to Contribute

### Ask Questions

Use the discussion board to ask questions. As the maintainer notes, "somebody else might have it too," and these inquiries help identify documentation gaps.

### Documentation Improvements

Contributors can fix typos, clarify interfaces, or add examples through pull requests to the README or source code comments.

### Bug Reports

File issues with detailed information on the issues tracker using the provided template to minimize back-and-forth communication.

### Code Changes

The project welcomes patches with these requirements:

- Proof-of-concept code beats lengthy proposals
- Backward compatibility must be maintained
- New features require documentation
- Bug fixes need regression tests
- All new code must be tested

## Development Workflow

1. Fork the repository
2. Make changes on any branch
3. Open a pull request
4. Respond to review feedback
5. Merge via squash-and-merge

## Testing Requirements

- Run tests locally: `go test -race ./...`
- Test across Go versions using provided Docker scripts
- Maintain or improve code coverage using `go tool cover`
- Verify no performance regressions with benchmarks using `benchstat`
- Follow `go fmt` style conventions

## Code Style

- Code must pass `go fmt`
- Code must pass linting with the same golangci-lint version as CI (see version in `.github/workflows/lint.yml`):

```bash
# Install specific version (check lint.yml for current version)
curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/HEAD/install.sh | sh -s -- -b $(go env GOPATH)/bin <version>
# Run linter
golangci-lint run ./...
```

## Performance Requirements

- go-toml aims to stay efficient; avoid performance regressions
- Run benchmarks to verify: `go test ./... -bench=. -count=10`
- Compare results using [benchstat](https://pkg.go.dev/golang.org/x/perf/cmd/benchstat)

## Commit Messages

- Commit messages must explain **why** the change is needed
- Keep messages clear and informative even if details are in the PR description
