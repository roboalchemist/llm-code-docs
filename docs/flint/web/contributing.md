# Contributing to Flint

## Source: https://github.com/flint-fyi/flint

Flint is an open-source project that welcomes contributions from the community. This guide explains how to get involved.

## Code of Conduct

All contributors are expected to follow the [Contributor Covenant Code of Conduct](https://github.com/flint-fyi/flint/blob/main/.github/CODE_OF_CONDUCT.md). We are committed to providing a welcoming and inclusive environment for all contributors.

## How to Contribute

There are many ways to contribute to Flint:

### 1. Report Issues

Found a bug or have a feature request?

- Visit the [GitHub issue tracker](https://github.com/flint-fyi/flint/issues)
- Choose the most appropriate issue template
- Fill out all required fields completely
- Provide clear, detailed information about the issue

Issue templates help categorize contributions:
- **Bug Report**: Report issues you've discovered
- **Feature Request**: Suggest new features or improvements
- **Documentation**: Suggest documentation improvements
- **General Feedback**: Provide general feedback or ideas

### 2. Send Pull Requests

Contributing code is welcome! Here's the process:

#### Before You Start

Look for issues on the tracker that meet these criteria:
- Marked as `status: accepting prs` label
- Not marked as `ai assigned` label
- Have no open PRs already

If this is your first contribution, look for issues also marked with `good first issue`.

**Note**: Flint does not use an issue claiming system. Don't post comments asking permission - if an issue hasn't received a PR yet, you can send one.

#### Steps to Send a PR

1. **Fork the repository**
   ```bash
   gh repo fork flint-fyi/flint
   git clone https://github.com/YOUR_USERNAME/flint
   cd flint
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature-description
   # Use a descriptive branch name
   ```

3. **Make your changes**
   - Write clear, focused code
   - Follow the project's code style
   - Add tests for new functionality
   - Update documentation as needed

4. **Commit with conventional commits**
   ```bash
   git commit -m "feat: add new feature"
   git commit -m "fix: resolve bug issue"
   git commit -m "docs: update documentation"
   ```

   PR titles must follow [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation
   - `test:` for tests
   - `refactor:` for code refactoring
   - `chore:` for maintenance

5. **Push to your fork**
   ```bash
   git push origin feature-description
   ```

6. **Create a Pull Request**
   - Visit your fork on GitHub
   - Click "Create Pull Request"
   - Fill out the PR template completely
   - Include a clear description of changes

7. **Ensure checks pass**
   - GitHub status checks must pass
   - Ask questions in PR comments if unclear
   - Respond to review feedback

8. **Address review feedback**
   ```bash
   # Make requested changes
   git add .
   git commit -m "refactor: address review feedback"
   git push origin feature-description

   # Re-request review
   ```

9. **Merge approval**
   - Once approved, maintainers will merge your PR
   - You don't need to merge it yourself

#### Pull Request Guidelines

- **Keep PRs focused**: Solve one problem per PR
- **Reasonable size**: Smaller PRs are easier to review
- **Good titles**: Use conventional commits format
- **Clear description**: Explain the "why" not just the "what"
- **Tests included**: Add tests for new functionality
- **Passing checks**: Ensure CI passes before requesting review

#### Draft PRs

If your PR isn't ready for review:
1. Click the "Convert to draft" button
2. Draft PRs won't be reviewed
3. Convert back when ready

#### Changeset for User-Facing Changes

If your PR includes user-facing changes:

```bash
pnpm changeset
```

This creates a changeset file that helps with versioning and release notes.

### 3. Improve Documentation

Documentation improvements are always welcome!

- Grammar and clarity fixes
- Adding examples
- Clarifying complex concepts
- Adding missing sections
- Updating outdated information

### 4. Provide Feedback

Share your thoughts and ideas:
- Participate in discussions
- Join the Discord community
- Comment thoughtfully on issues
- Help other contributors

## Development Setup

### Prerequisites

- Node.js 18+ (recommended 20+)
- npm or pnpm
- Git
- A text editor or IDE

### Local Development

See [DEVELOPMENT.md](https://github.com/flint-fyi/flint/blob/main/.github/DEVELOPMENT.md) in the repository for detailed setup instructions.

Basic steps:

```bash
# Clone the repository
git clone https://github.com/flint-fyi/flint
cd flint

# Install dependencies
pnpm install

# Run tests
pnpm test

# Build the project
pnpm build

# Run Flint on itself
pnpm flint
```

## Community

### Join the Community

Connect with other Flint contributors and users:

- **Discord**: https://flint.fyi/discord - Real-time discussion and support
- **GitHub Discussions**: Threaded conversations about features and ideas
- **GitHub Issues**: Report bugs and request features
- **GitHub Releases**: Follow project updates

### Getting Help

If you need help:

1. **Check existing issues**: Your question might be answered there
2. **Ask on Discord**: Real-time help from community members
3. **Create a discussion**: For questions that aren't bug reports
4. **Comment on issues**: Ask for clarification from maintainers

## Contribution Ideas

### Good First Issues

Look for issues marked with these labels:
- `good first issue` - Perfect for newcomers
- `status: accepting prs` - Ready for contributions
- No `ai assigned` label - Not already assigned

### Areas for Contribution

- **Bug fixes**: Fix known issues
- **Rule additions**: Add new linting rules
- **Plugin development**: Create new plugins
- **Documentation**: Improve guides and examples
- **Testing**: Increase test coverage
- **Performance**: Optimize slow operations
- **Accessibility**: Improve IDE and tooling support

### Example Contributions

Examples of valuable contributions:

1. **Add a new rule** to an existing plugin
2. **Create a new focused plugin** for a popular framework
3. **Improve rule documentation** with more examples
4. **Add missing tests** for existing functionality
5. **Fix performance issues** identified in PRs
6. **Improve error messages** for clarity
7. **Add configuration examples** to documentation
8. **Create example projects** showing Flint usage

## Code Style and Standards

### TypeScript

Flint is written in strict TypeScript:
- Enable strict mode
- No `any` types without explicit justification
- Full type annotations
- Comprehensive type coverage

### Testing

- Write tests for new features
- Update tests for changed behavior
- Aim for high code coverage
- Use clear, descriptive test names

### Formatting

- Follow ESLint/Prettier conventions
- Run `pnpm format` to auto-format
- Keep line lengths reasonable
- Use meaningful variable names

### Commits

- Keep commits focused and atomic
- Write descriptive commit messages
- One logical change per commit
- Squash merge to main keeps history clean

## Review Process

### What to Expect

1. **Automated checks** run on every push
2. **Maintainer review** within reasonable time
3. **Requested changes** for improvements
4. **Approval** when changes are good
5. **Merge** by maintainer

### Providing Feedback

When reviewing others' code:
- Be respectful and constructive
- Ask questions rather than make demands
- Acknowledge good work
- Suggest improvements with reasoning
- Follow the Code of Conduct

## Emoji Appreciation

When submitting issues or PRs, include an emoji to show you've read the contribution guide. This helps us quickly identify engaged contributors!

The flaming heart emoji (❤️‍🔥) is the project's signature emoji, but any thoughtful emoji works.

## Frequently Asked Questions

### Can I work on an issue that's assigned?

No, assignment indicates an AI is currently working on it. Look for unassigned issues instead.

### Do I need permission to contribute?

No! If an issue is marked `status: accepting prs` and has no open PR, you can send one directly.

### What if I'm stuck?

Ask questions in PR comments or on Discord. Maintainers and community members are happy to help!

### How long does review take?

Review times vary based on maintainer availability and PR complexity. Be patient - all PRs will be reviewed.

### Can I contribute examples or tutorials?

Absolutely! Examples and tutorials are valuable contributions, whether in the repo or elsewhere.

## Recognition

Once your PR is merged:
- Check if you should be added to the contributors table
- Ping the merging maintainer if not added within 24 hours
- Your contribution is acknowledged in release notes

## Financial Support

If you'd like to support Flint financially:

- Visit [Open Collective](https://opencollective.com/flintfyi)
- One-time or recurring donations
- Your contribution helps fund development

## Additional Resources

- **GitHub Repository**: https://github.com/flint-fyi/flint
- **Issue Tracker**: https://github.com/flint-fyi/flint/issues
- **Pull Requests**: https://github.com/flint-fyi/flint/pulls
- **Code of Conduct**: https://github.com/flint-fyi/flint/blob/main/.github/CODE_OF_CONDUCT.md
- **Contributing Guidelines**: https://github.com/flint-fyi/flint/blob/main/.github/CONTRIBUTING.md
- **Development Guide**: https://github.com/flint-fyi/flint/blob/main/.github/DEVELOPMENT.md

## Support the Project

### Ways to Help Beyond Code

- Share Flint with others
- Write blog posts about using Flint
- Create example projects
- Improve documentation
- Test and report bugs
- Provide feedback and ideas
- Participate in discussions
- Help new contributors

## Final Thoughts

Thank you for considering contributing to Flint! Whether it's code, documentation, ideas, or community participation, every contribution helps move the project forward.

The community around Flint is just as important as the code itself. We look forward to collaborating with you!

---

**Remember**: The flaming heart (❤️‍🔥) is our favorite emoji!
