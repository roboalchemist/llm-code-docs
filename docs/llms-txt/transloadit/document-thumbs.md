# Source: https://transloadit.com/docs/robots/document-thumbs.md

## Things to keep in mind

* If you convert a multi-page PDF file into several images, all result images will be sorted with the first image being the thumbnail of the first document page, etc.
* You can also check the `meta.thumb_index` key of each result image to find out which page it corresponds to. Keep in mind that these thumb indices **start at 0,** not at 1.
