# Source: https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule-DL3059.html

Title: Hadolint.Rule.DL3059

URL Source: https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule-DL3059.html

Markdown Content:
| Safe Haskell | None |
| --- |
| Language | GHC2021 |

Hadolint.Rule.DL3059

Documentation
-------------

[rule](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule-DL3059.html) :: [Rule](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:Rule "Hadolint.Rule")[ParsedShell](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Shell.html#t:ParsedShell "Hadolint.Shell")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.DL3059.html#rule)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule-DL3059.html#v:rule)

This Rule catches multiple consecutive `RUN` instructions. It ignores the case where multiple commands are chained together (e.g. with `&&`) because in that case the programmer most likely has deliberately chosen to use multiple `RUN` instructions. Cases where --mount=xxx flags differ are excluded as well.
