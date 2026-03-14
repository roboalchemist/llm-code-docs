# Source: https://virustotal.readme.io/docs/vtdiff-filetype-exclusion.md

# Error - "Need to give exclusion list for filetype"

When using [VTDiff](https://virustotal.readme.io/docs/vtdiff-automatic-yara-rules) the system will ask you for a set of hashes to be included and a set of hashes to be excluded. The error you are getting means that the system is missing the exclusion set.

Why does this error not always show, even when you do not exclude any hashes? In order to ease the hunting task we are constantly improving how VTDiff works by predefining some lists of exclusion hashes for specific filetypes.

In this case, the specific filetype mentioned in the error does not have predefined exclusion lists, which is why you need to input them manually on the exclusion column.

You can start by inputting only one hash on the exclusion list, and then once you get the results of your first VTDiff session, if they include any goodware hashes, you can use this to iterate and start a new VTDiff session where you add these goodware hashes to the exclude column to get more interesting patterns.