lightningcss

# Module bundler

Source Available on **crate feature `bundler`** only.

## Structs§

BundlerA Bundler combines a CSS file and all imported dependencies together into
a single merged style sheet.FileProviderProvides an implementation of SourceProvider
that reads files from the file system.

## Enums§

BundleErrorKindAn error that could occur during bundling.ResolveResultThe result of SourceProvider::resolve.

## Traits§

SourceProviderA trait to provide the contents of files to a Bundler.
