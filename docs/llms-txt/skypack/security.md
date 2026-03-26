# Source: https://docs.skypack.dev/skypack-cdn/security.md

# Security

## Zero Package System Access

When you install your npm packages locally, most package managers will grant every package permission to run unknown, third-party scripts on your machine. With Skypack, this potential security vector is removed because packages are never installed directly on your machine. Instead, every package is installed and built inside of our very own sandboxed builder function.

## Lack of Subresource Integrity (SRI)

SRI is a security concept that exists for consumers of Skypack to implement. When you load JavaScript from a third-party source like npm or Skypack, you can check that the response matches a known hash (known as the integrity hash) to guarantee that the response has not been changed/interfered with.

&#x20;**Browsers don't yet support SRI for ESM imports.** This opens Skypack imports up to a man-in-the-middle attack if Skypack's origin were ever compromised. Because SRI is a browser feature, there is nothing that we can do to add this without browser support. Support is planned, but does not yet exist in any major browsers.

Non-browser applications like Deno and Snowpack are open and encouraged to implement SRI & integrity hash checks themselves by maintaining their own integrity hash as a part of installation.
