# Source: https://doc.replicache.dev/examples/todo

Title: Todo, Three Ways | Replicache Docs

URL Source: https://doc.replicache.dev/examples/todo

Markdown Content:
This page contains several different implementations of the same simple todo app, demonstrating different ways to build a Replicache app.

You can study them as an example of how to use a particular technique, or just clone them to play with a complete working app, before diving into building your own server.

![Image 1](https://doc.replicache.dev/img/setup/todo.webp)

### todo-nextjs

**Frontend:** Next.js

**Backend:** Next.js/Vercel

**Mutators:** Shared

**Database:** Supabase

**Strategy:** Global Versioning

**Pokes:** Supabase Realtime

### todo-wc

**Frontend:** Web Components / Vanilla JS

**Backend:** Node.js/Express

**Mutators:** Shared

**Database:** Postgres

**Strategy:** Per-Space Versioning

**Pokes:** Server-Sent Events

### todo-row-versioning

**Frontend:** React

**Backend:** Node.js/Express

**Mutators:** Unshared

**Database:** Postgres

**Strategy:** Row Versioning

**Pokes:** Server-Sent Events
