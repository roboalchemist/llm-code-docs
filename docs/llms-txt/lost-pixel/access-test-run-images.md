# Source: https://docs.lost-pixel.com/docs/recipes/lost-pixel-oss/access-test-run-images.md

# Access test run images

When using the `open source edition` of Lost Pixel, you might want to look at your failed tests that were [happening on CI](https://docs.lost-pixel.com/docs/guides/getting-started/getting-started). While Lost Pixel provides extensive logging, you would not be able to see the images in the output of the action by default.\
\
To access the generated images you would need to use [GitHub Actions Artefacts](https://docs.github.com/en/rest/actions/artifacts). Presuming you [did not change the relative paths to the images](https://docs.lost-pixel.com/docs/setup/project-configuration/baseline-images) extend [GitHub action](https://docs.lost-pixel.com/docs/setup/integrating-with-github-actions) with the following step that takes place after `lost-pixel`:

```
...

  - uses: actions/upload-artifact@v3
    with:
      name: lost-pixel-artefacts
      path: .lostpixel
```

This step will ensure that everything that will be generated during the Lost Pixel action run on CI will be accessible for the download later after the workflow is finished:

![](https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-438dde13d5cd054a14f345e100554840ff4c579b%2FSCR-20220527-evp.png?alt=media)
