# Source: https://electric-sql.com/demos/encryption.md

---
url: /demos/encryption.md
description: Example of how to implement encryption with Electric.
---

# {{ $frontmatter.title }}

{{ $frontmatter.description }}

## Encrypting local-first data with Electric

This is an example of encryption with Electric.

Electric syncs ciphertext as well as it syncs plaintext. You can encrypt data on and off the local client, i.e.:

* encrypting data before it leaves the client
* decrypting data after it syncs in to the client through Electric

It's a React app with a very simple Express API server. The Electric-specific code is in [`./src/Example.tsx`](https://github.com/electric-sql/electric/blob/main/examples/encryption/src/Example.tsx):

<<< @../../examples/encryption/src/Example.tsx{tsx}
