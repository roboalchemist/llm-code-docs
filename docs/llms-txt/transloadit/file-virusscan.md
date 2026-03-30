# Source: https://transloadit.com/docs/robots/file-virusscan.md

![](/_next/static/media/copy.8f7d2926.svg?dpl=dpl_GAEaNRfbaNgVy6q3c3ke5o1s9Xtk)

```
  This <dfn>Robot</dfn> is built on top of [ClamAV](https://www.clamav.net/), the best open source antivirus engine available. We update its signatures on a daily basis.

```

By default, this Robot excludes all malicious files from further processing without any additional notification. This behavior can be changed by setting `error_on_decline` to `true`, which will stop Assemblies as soon as malicious files are found. Such Assemblies will then be marked with an error.

We allow the use of industry standard [EICAR files](https://www.eicar.org/download-anti-malware-testfile/) for integration testing without needing to use potentially dangerous live virus samples.
