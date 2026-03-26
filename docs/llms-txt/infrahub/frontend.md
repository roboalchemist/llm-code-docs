# Source: https://docs.infrahub.app/development/frontend.md

# Frontend guide

Welcome to the Infrahub frontend guide! This guide details the technologies and steps required to contribute effectively to the Infrahub frontend.

## Infrahub stack[​](#infrahub-stack "Direct link to Infrahub stack")

Infrahub frontend is developed with:

* **UI Framework**: [React](https://react.dev/)
* **Typing**: [TypeScript](https://www.typescriptlang.org/)
* **Component Library**: [Headless UI](https://headlessui.com/)
* **CSS Framework**: [Tailwind CSS](https://tailwindcss.com/)
* **GraphQL Client**: [Apollo Client](https://www.apollographql.com/docs/react/)
* **State Management**: [Jotai](https://jotai.org/)

For testing, we rely on:

* **Unit testing**: [Vitest](https://vitest.dev/)
* **Integration testing**: [Vitest browser react](https://github.com/vitest-dev/vitest-browser-react)
* **end-to-end testing**: [Playwright](https://playwright.dev/)

## Accessing the frontend code[​](#accessing-the-frontend-code "Direct link to Accessing the frontend code")

To access Infrahub's codebase, use Git and switch to the `develop` branch to access the latest changes. All frontend code resides in `/frontend`.

```
git clone --recursive git@github.com:opsmill/infrahub.git
cd infrahub/frontend
```

Before contributing, we recommended starting with [Getting set up with frontend](/development/frontend/getting-set-up.md).
