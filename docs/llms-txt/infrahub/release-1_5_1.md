# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_5_1.md

# Release 1.5.1

| Release Number | 1.5.1                                                                               |
| -------------- | ----------------------------------------------------------------------------------- |
| Release Date   | November 13th, 2025                                                                 |
| Tag            | [infrahub-v1.5.1](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.5.1) |

### Security[​](#security "Direct link to Security")

* Updated FastAPI and vulnerable version of starlette

### Fixed[​](#fixed "Direct link to Fixed")

* Disabled scroll on number input fields to prevent accidental value changes. ([#7602](https://github.com/opsmill/infrahub/issues/7602))
* Backend database sessions are now handled consistently avoiding resource leakage.

### Housekeeping[​](#housekeeping "Direct link to Housekeeping")

* Bump SDK to fix issue with object file range expansion.
