# ts-morph Documentation
# Source: https://raw.githubusercontent.com/dsherret/ts-morph/latest/docs/navigation/language-service.md
# Path: docs/navigation/language-service.md

---
title: Language Service
---

## Language Service

Get the language service by calling:

```ts
const languageService = project.getLanguageService();
```

### Underlying compiler object

The underlying `ts.LanguageService` can be retrieved as follows:

```ts
const tsLanguageService = languageService.compilerObject;
```

### Use

Generally you won't need to use the language service because most of the functionality is exposed as methods on other objects.
