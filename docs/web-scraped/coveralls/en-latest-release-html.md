# Source: https://coveralls-python.readthedocs.io/en/latest/release.html

Title: Release — coveralls-python 4.1.0 documentation

URL Source: https://coveralls-python.readthedocs.io/en/latest/release.html

Markdown Content:
This project is released on PyPI as [coveralls](https://pypi.org/project/coveralls/), as well as on [quay](https://quay.io/repository/thekevjames/coveralls) and [dockerhub](https://hub.docker.com/r/thekevjames/coveralls). To cut a new release, ensure the latest master passes all tests. Then, create a release commit:

git cliff -u | pbcopy # prepend to CHANGELOG.md
poetry version (major|minor|patch)
poetry lock --regenerate
poetry sync
poetry run pytest
git commit -am 'chore(release): bump version'
git push
git tag $(poetry version | cut -f2 -d' ')
git push origin $(poetry version | cut -f2 -d' ')

Then:

1.   Create a new [GitHub release](https://github.com/TheKevJames/coveralls-python/releases/new).

2.   Verify the [docs build succeeded](https://readthedocs.org/projects/coveralls-python/builds/) then [mark it active](https://readthedocs.org/projects/coveralls-python/versions/).

Conda should automatically create a PR on their [coveralls-feedstock](https://github.com/conda-forge/coveralls-feedstock) shortly with the updated version – if something goes wrong, the manual process would be to:

1.   Fork [coveralls-feedstock](https://github.com/conda-forge/coveralls-feedstock).

2.   Update `recipe/meta.yaml` with the new version number and [sha](https://pypi.org/project/coveralls/#files).

3.   Create a PR.

4.   Comment on your own PR with: “@conda-forge-admin, please rerender”.

5.   Merge along with the automated commit from Conda.
