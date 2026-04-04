# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_3_2.md

# Release 1.3.2

| Release Number   | 1.3.2                                                                               |
| ---------------- | ----------------------------------------------------------------------------------- |
| Release Date     | June 30th, 2025                                                                     |
| Release Codename | Amsterdam                                                                           |
| Tag              | [infrahub-v1.3.2](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.3.2) |

### Fixed[​](#fixed "Direct link to Fixed")

* Improve performance of uniqueness constraint checks during create/update/upsert mutations by allowing ordering elements from more specific to less specific within a constraint group ([#6377](https://github.com/opsmill/infrahub/issues/6377))

* Fixed: min/max constraints no longer trigger on empty values when the field is optional. ([#6671](https://github.com/opsmill/infrahub/issues/6671))

* Object template ([#6724](https://github.com/opsmill/infrahub/issues/6724))

  <!-- -->

  * Fixed "Kind" filter in object template list view.
  * Fixed search in object template selector during creation form

* Improve performance when calculating a large diff with many added and/or deleted node (>2,000) ([#6751](https://github.com/opsmill/infrahub/issues/6751))
