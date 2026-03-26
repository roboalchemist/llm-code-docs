# Source: https://www.lucide.dev/contribute/affinity-designer-guide.md

---
url: /contribute/affinity-designer-guide.md
---

# Affinity Designer Template Guide

This guide describes how to use the Affinity Designer template for Lucide.

## General Workflow

> Attention: By default, Affinity Designer sets the unit for stroke to points. Make sure that it is set to pixel. To do this, open `Preferences > User Interface`. Under `Decimal Places for Unit Types`, uncheck `Show Lines in points`.

1. Download and open the [Affinity Designer template](https://github.com/lucide-icons/lucide/blob/main/docs/public/templates/affinity_designer.aftemplate).
2. Follow the [Icon Design Principles](icon-design-guide.md) while you use the template (to ensure integrity with the Lucide icon pack).
3. Export the file as SVG (`File > Export`). Make sure that *Rastering* is set to *Nothing*, *Export text as curves* is checked (hopefully, you won't need this), *Use hex colors* is checked, and *Flatten transforms* is checked.

   ![SVG export options in Affinity Designer](../images/affinity-designer-export-options.png?raw=true)
4. Optimize the exported SVG file further with [SVGOMG](https://jakearchibald.github.io/svgomg/) or [`svgo`](https://github.com/svg/svgo) (using `svgo --multipass exported_icon.svg`).
