# Source: https://docs.warp.dev/terminal/more-features/text-selection.md

# Text Selection

## Smart Selection

**Smart selection** goes beyond the typical double-click selection, which only highlights a single word. Instead, it uses semantic rules to treat common patterns (like URLs or file paths) as one unit, even when separated by punctuation or whitespace.

<figure><img src="https://4009768362-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPsjNxoJ0NFCXW6rRdHH3%2Fuploads%2Fgit-blob-193352c4cee174eebbcff3d530b604da8c917e52%2Fsmart-selection.png?alt=media" alt=""><figcaption><p>Using smart selection to select a file path by double clicking.</p></figcaption></figure>

Double-click on text in the input or blocklist. The following patterns are recognized:

1. URLs
2. File paths
3. Email addresses
4. IP addresses
5. Floating point numbers, including scientific notation.

You can toggle smart selection on the `Settings > Features > Terminal > Double-click smart selection`. If disabled, you can instead manually select specific punctuation characters to be included within word boundaries.

## Rectangular Selection

**Rectangular selection** lets you highlight text in a clean vertical block (also called *column* or *box* selection). This is especially useful for copying command output, logs, or prefixed text without grabbing unwanted characters.

<figure><img src="https://4009768362-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPsjNxoJ0NFCXW6rRdHH3%2Fuploads%2Fgit-blob-98d2d2b41c2b0e0cc6cd62bf31087c63f1643a0a%2Frectangular-selection.png?alt=media" alt=""><figcaption><p>Using rectangular selection to select by columns in the block output.</p></figcaption></figure>

Hold the modifier keys while dragging your mouse:

* macOS: `CMD-OPT`
* Windows and Linux: `CTRL-ALT`
