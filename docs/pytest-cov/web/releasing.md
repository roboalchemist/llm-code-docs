# Releasing

The process for releasing should follow these steps:

-

Test that docs build and render properly by running `tox -e docs`.

If there are bogus spelling issues add the words in `spelling_wordlist.txt`.

-

Update `CHANGELOG.rst` and `AUTHORS.rst` to be up to date.

-

Bump the version by running `bumpversion [ major | minor | patch ]`. This will automatically add a tag.

-

Push changes and tags with:

```
git push
git push --tags

```
