# Source: https://github.com/volarjs/docs/blob/main/src/content/docs/guides/first-server.mdx

---
title: Your First Volar Language Server
description: A simple guide to creating your first Volar language server.
---

> This page is a work in progress. Interested in contributing some documentation to it, or want to improve it? [Edit this page on GitHub](https://github.com/volarjs/docs/blob/main/src/content/docs/guides/first-server.mdx)


In this guide, you will learn create a simple Volar language server and VS Code client. To keep things simple, the language it'll support will look suspiciously like HTML, albeit with one twist: Only one `<style>` tag will be allowed. The language will be called HTML1.

This guide assumes that you have a basic understanding of TypeScript and Node.js, and also of what a language server is. If you're not familiar with language servers, you might want to read the "What is the Language Server Protocol?" section of the [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) homepage before continuing.

> 💡 Interested in seeing the final product? Check out the [starter project](https://github.com/volarjs/starter) on GitHub.

## Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/) version 1.55 or higher.
- [Node.js](https://nodejs.org/en/) version 14 or higher.
- Basic knowledge of JavaScript and Node.
- (Optional) Install the [Volar Labs](https://volarjs.dev/core-concepts/volar-labs/) extension for VS Code.

## Getting Started

First create a new project directory and initialize a new Node.js project: