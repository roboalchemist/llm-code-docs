# Source: https://docs.aws.amazon.com/dcv/latest/extsdkguide/llms.txt

# Amazon DCV Extension SDK Developer Guide

> Further information on how to use the Amazon DCV Extension SDK and provides links to code samples.

- [What is Amazon DCV Extension SDK?](https://docs.aws.amazon.com/dcv/latest/extsdkguide/what-is.html)
- [Release Notes and Document History](https://docs.aws.amazon.com/dcv/latest/extsdkguide/doc-history-release-notes.html)

## [Getting started](https://docs.aws.amazon.com/dcv/latest/extsdkguide/getting-started.html)

### [Extension architecture](https://docs.aws.amazon.com/dcv/latest/extsdkguide/extension-architecture.html)

There are two parts to the Amazon DCV Extension SDK: a manifest file that describes extension metadata and an executable that runs when the extension is activated.

- [Extension manifest](https://docs.aws.amazon.com/dcv/latest/extsdkguide/extension-manifest.html): Manifest files are JSON files in the format described below.
- [Extension executable](https://docs.aws.amazon.com/dcv/latest/extsdkguide/extension.executable.html): Extension manifest files define the executable file spawned by Amazon DCV.
- [Digital signature](https://docs.aws.amazon.com/dcv/latest/extsdkguide/digital.signature.html): On Windows, Amazon DCV starts only digitally signed extension executables.
- [Installing and registering the extension](https://docs.aws.amazon.com/dcv/latest/extsdkguide/install-register-extension.html): Amazon DCV does not determine where extension executables should be located.
- [Permissions](https://docs.aws.amazon.com/dcv/latest/extsdkguide/permissions.html): Amazon DCV has two new permissions to enable the execution of the extensions:
- [Protocol and framing](https://docs.aws.amazon.com/dcv/latest/extsdkguide/protocol-framing.html): When Amazon DCV components start the extension on either server or client side, DCV uses standard input (stdin) and standard output (stdout), also known as anonymous pipes, to communicate with the extension.


## [API Reference](https://docs.aws.amazon.com/dcv/latest/extsdkguide/api-reference.html)

- [General API](https://docs.aws.amazon.com/dcv/latest/extsdkguide/general-api.html)
- [Virtual Channel API](https://docs.aws.amazon.com/dcv/latest/extsdkguide/virtual-channel-api.html)
- [Geometry API](https://docs.aws.amazon.com/dcv/latest/extsdkguide/geometry-api.html)
