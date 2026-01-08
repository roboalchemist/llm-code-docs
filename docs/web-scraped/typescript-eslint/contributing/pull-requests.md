# Source: https://typescript-eslint.io/contributing/pull-requests

On this page# Pull Requests
See [Local Development](/contributing/local-development) for details on how to get started developing locally.
So you&#x27;ve got changes locally that address an issue?
Fantastic!
Please do:
- Only send pull requests that resolve [open, unassigned issues marked as `accepting prs`](https://github.com/typescript-eslint/typescript-eslint/issues?q=is%3Aissue+is%3Aopen+label%3A%22accepting+prs%22+no%3Aassignee)
One exception: extremely minor documentation typos
- Fill out the pull request template in full
- Validate your changes per [Development > Validating Changes](/contributing/local-development#validating-changes) before un-[drafting your PR](https://github.blog/2019-02-14-introducing-draft-pull-requests)
Please don&#x27;t:
- Force push after opening a PR
Reasoning: GitHub is not able to track changes across force pushes, which makes it take longer for us to perform incremental reviews
- Comment on an existing PR asking for updates
Reasoning: Your PR hasn&#x27;t been forgotten! The volunteer maintainers have limited time to work on the project, and they will get to it as soon as they are able.
One exception: if a PR has been blocked on a question to a maintainer for 3 or more months, please ping us - we probably lost track of it.
- Comment on a closed PR
Reasoning: It is much easier for maintainers to not lose track of things if they are posted as issues. If you think there&#x27;s a bug in typescript-eslint, the right way to ask is to [file a new issue](https://github.com/typescript-eslint/typescript-eslint/issues/new/choose). The issue templates include helpful & necessary practices such as making sure you&#x27;re on the latest version of all our packages. You can provide the link to the relevant PR to add more context.
## Testing Changes[​](#testing-changes)
### Code Coverage[​](#code-coverage)
We aim for 100% code coverage in all PRs when possible, except in the `website/` package.
Coverage reports are generated locally whenever `yarn test` is run.
The `codecov` bot also comments on each PR with its percentage, as well as links to the line-by-line coverage of each file touched by the PR.
### Granular Unit Tests[​](#granular-unit-tests)
Most tests in most packages are set up as small, self-contained unit tests.
We generally prefer that to keep tests and their failure reports granular.
For rule tests we recommend, when reasonable:
- Including both `valid` and `invalid` code changes in most PRs that affect rule behavior
- Limiting to one error per `invalid` case
### AST Testing[​](#ast-testing)
AST tests belong in the `ast-spec` package, within `fixtures/` subfolders alongside the AST declarations. Each test has its own `<test-name>/` folder, containing a `fixture.ts` file defining the test, and a `snapshots/` subfolder. Happy-path test folders are stored directly under `fixtures/`; error-path test folders go under `fixtures/_errors/`. You can check out the [`ClassDeclaration` fixtures folder](https://github.com/typescript-eslint/typescript-eslint/tree/main/packages/ast-spec/src/declaration/ClassDeclaration/fixtures) for an example of both happy-path and unhappy-path test folders.
## Raising the PR[​](#raising-the-pr)
Once your changes are ready, you can raise a PR! 🙌
The title of your PR should match the following format:
```
<type>(<package>): <short description>
```
You can find more samples of good past PR titles in [recent commits to `main`](https://github.com/typescript-eslint/typescript-eslint/commits/main):
- `fix(scope-manager): correct handling for class static blocks`
- `docs: fix links to getting started in README.md`
Within the body of your PR, make sure you reference the issue that you have worked on, as well as pointing out anything of note you wish us to look at during our review.
We do not care about the number, or style of commits in your history, because we squash merge every PR into `main`.
Feel free to commit in whatever style you feel comfortable with.
Tip: Send the PR from a branch other than `main`.
See GitHub&#x27;s [Proposing Changes docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests) for more information.
### type[​](#type)
Must be one of the following:
- `docs` - if you only change documentation, and not shipped code
- `feat` - for any new functionality additions
- `fix` - for any bug fixes that don&#x27;t add new functionality
- `test` - if you only change tests, and not shipped code
- `chore` - anything else
### package[​](#package)
The name of the package you have made changes within, (e.g. `eslint-plugin`, `parser`, `typescript-estree`).
If you make significant changes across multiple packages, you can omit this (e.g.
`feat: foo bar`).
### short description[​](#short-description)
A succinct title for the PR.
## Addressing Feedback and Beyond[​](#addressing-feedback-and-beyond)
With your PR raised and the CI passing, your PR will [wait in the queue to be reviewed](https://github.com/typescript-eslint/typescript-eslint/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc+-label%3A%22breaking+change%22+-label%3A%22awaiting+response%22+-label%3A%221+approval%22+-label%3A%22DO+NOT+MERGE%22+status%3Asuccess).
We generally review PRs oldest to newest, unless we consider a newer PR higher priority (e.g. if it&#x27;s a bug fix).
Once we have reviewed your PR, we will provide any feedback that needs addressing.
If you feel a requested change is wrong, don&#x27;t be afraid to discuss with us in the comments.
Please post comments as [line comments](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request#adding-line-comments-to-a-pull-request) when possible, so that they can be threaded.
You can [resolve conversations](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request#resolving-conversations) on your own when you feel they&#x27;re resolved - no need to comment explicitly and/or wait for a maintainer.
Once you&#x27;ve addressed all our feedback by making code changes and/or started a followup discussion, [re-request review](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews#re-requesting-a-review) from each maintainer whose feedback you addressed.
Once the feedback is addressed, and the PR is approved, we&#x27;ll ensure the branch is up to date with `main`, and merge it for you.
### Updating Over Time[​](#updating-over-time)
You generally don&#x27;t need to keep merging commits from `main` into your PR branch.
If you see merge conflicts or other intersections that worry you, then you can preemptively - but that&#x27;s optional.
If we think merge conflicts need to be resolved in order to merge and/or review a PR, we might do that for you as a courtesy *if* we have time.
If not, we may ask you to.
## Asking Questions[​](#asking-questions)
If you need help and/or have a question, posting a comment in the PR is a great way to do so.
There&#x27;s no need to tag anybody individually.
One of us will drop by and help when we can.
Appreciation NoteThanks for reading through this file in full!
Please include your favorite emoji at the bottom of your pull request to hint to us that you did in fact read this file.
💖 is a good starter if you&#x27;re not sure which to use.
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../../docs/contributing/Pull_Requests.mdx)- [Testing Changes](#testing-changes)[Code Coverage](#code-coverage)- [Granular Unit Tests](#granular-unit-tests)- [AST Testing](#ast-testing)- [Raising the PR](#raising-the-pr)[type](#type)- [package](#package)- [short description](#short-description)- [Addressing Feedback and Beyond](#addressing-feedback-and-beyond)[Updating Over Time](#updating-over-time)- [Asking Questions](#asking-questions)