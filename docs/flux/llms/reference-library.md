# Source: https://docs.flux.ai/reference/reference-library.md

# The Library

Find components to use in your project.

## Overview

The library is one of the core aspects of the editor. It's home to 1M components, and it's where you'll find every component that's available to you:

- **Publicly available** – Components that were made public for everyone on Flux to use.
- **Shared with you** – Components that were shared with you.
- **Owned by an organization** – Components that belong to an organization of which you're a member.
- **Owned by you** – Components that you've created yourself and [published to the library](https://docs.flux.ai/flux/tutorials/publishing-a-part-to-the-library).

![Use filters to refine your search, and expand the width of the library to see more info.](https://uploads.developerhub.io/prod/86Yw/dgcqurzqzzy3wsdx4mhy1tn1ptsann03s6qxq0sy13nwv6tiykt4oa5ybzlvd2nb.png)

## Search

Searching the library is as easy as typing the part number you're looking for. You can also search by keywords if you don't have a specific part number in mind.

![](https://uploads.developerhub.io/prod/86Yw/44r7j9z5u2ua3byfcxjy71zlpnqsy8cz6arkk8orbcxvm0i3lwins9rpbm25loxg.png)

The search bar is located at the top of the Library tab in the left drawer, which sits along on the left side of the editor.

### Operators

The search bar supports a few basic search operators to narrow down results:

- **Phrase query `""`**
    - A specific sequence of terms that must be matched next to one another. A phrase query needs to be surrounded by double quotes. For example, the query `"Arduino Compatible"` only returns a record if it contains `“Arduino Compatible”` exactly in at least one attribute.
    - _Note:_ _Typo tolerance is disabled inside the phrase_ _(i.e. within the quotes)._

- **Prohibit operator `-`** 
    - Excludes records that contain a specific term. To exclude a term, you need to prefix it with a minus `-`. The engine only interprets the minus `-` as a prohibit operator when you place it at the start of a word. A minus `-` within double quotes `""` is not treated as a prohibit operator. 
    - Some examples:
        - `"-arduino"` matches records containing “-arduino” (no exclusion performed because of the inclusion of the double quotes `""`)
        - `-arduino compatible` matches records containing “compatible”, but not “arduino”
        - `-compatible` matches every record except those containing “compatible”
        - `arduino-compatible` matches records containing “arduino-compatible” (there’s no exclusion because the minus `-` is in the middle of a word)
        - `Arduino -Compatible` only matches records containing “Arduino”, but not “compatible”

### Filtering

You can use the filters section to find your desired part quickly. When a filter is selected, only parts that have such characteristic(s) will be shown.

![From left to right: **Person**: items you own - **Star:** items you've starred - **Chip:** contains a footprint (is a part) - **Blocks:** contains a sub-layout - **&lt;&gt;:** contains simulator code - **3D Cube:** contains a 3D model. **PDF:** contains datasheet link. **Cart:** contains part number](https://uploads.developerhub.io/prod/86Yw/tg86icok2jao18anxcagwjhy55elvf0jskrwr6u948srqpjrrel8awax1vhtxcuz.png)

## Expanding the library

The library can be expanded to show more information about each component. To do so, hover your mouse over the edge of the panel, then click and drag to the right.

![](https://uploads.developerhub.io/prod/86Yw/7g8lha7k9rno7tqfnvop506qdcrd1woe4ut8k1v8cqin35dwmpvnz25fx0py5anw.gif)

The library can also be hidden to create extra space for the canvas. To hide the library, hover your mouse over the edge of the panel, then click and drag to the left.