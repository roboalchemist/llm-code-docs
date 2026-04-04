# Source: https://electric-sql.com/demos/notes.md

---
url: /demos/notes.md
description: Collaborative note-taking app with sync powered by Electric and Yjs.
---

# Notes

This is a collaborative note-taking app with real-time sync powered by Electric and [Yjs](/docs/integrations/yjs).

## Electric <> Yjs demo

Notes demonstrates our [Yjs integration](/docs/integrations/yjs). By combining Yjs's powerful collaborative editing capabilities with Postgres and Electric, you get the best of both worlds:

* Postgres provides rock-solid storage that can handle millions of documents with powerful querying capabilities
* Electric provides real-time sync that scales to millions of concurrent users while keeping your data consistent
* Yjs handles the collaborative editing with battle-tested conflict resolution

[`y-electric.ts`](https://github.com/KyleAMathews/electric-notes/blob/main/src/y-electric/index.ts) provides a standard Yjs provider similar to y-websocket. Internally it syncs Yjs operations using the standard [`ShapeStream`](/docs/api/clients/typescript#shapestream) class from the Electric [Typescript client](/docs/api/clients/typescript).
