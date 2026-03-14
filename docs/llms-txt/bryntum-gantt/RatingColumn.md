# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/column/RatingColumn.md

# [RatingColumn](https://bryntum.com/docs/gantt/api/Grid/column/RatingColumn)

A column that displays a star rating. Click a start to set a value, shift+click to unset a single start from the end. Clicking the first and only star toggles it.

This column inherits from `NumberColumn` and uses a NumberField widget as its editor when the `CellEdit` feature is active.

```
new Grid({
    appendTo : document.body,

    columns : [
        { type: 'rating', max : 10, field: 'rating' }
    ]
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[emptyIcon](https://bryntum.com/docs/gantt/api/Grid/column/RatingColumn#config-emptyIcon)
The empty rating icon to show

[filledIcon](https://bryntum.com/docs/gantt/api/Grid/column/RatingColumn#config-filledIcon)
The filled rating icon to show

[editable](https://bryntum.com/docs/gantt/api/Grid/column/RatingColumn#config-editable)
Allow user to click a rating icon to change the value

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRatingColumn](https://bryntum.com/docs/gantt/api/Grid/column/RatingColumn#property-isRatingColumn)
Identifies an object as an instance of [RatingColumn](https://bryntum.com/docs/gantt/api/#Grid/column/RatingColumn) class, or subclass thereof.

[isRatingColumn](https://bryntum.com/docs/gantt/api/Grid/column/RatingColumn#property-isRatingColumn-static)
Identifies an object as an instance of [RatingColumn](https://bryntum.com/docs/gantt/api/#Grid/column/RatingColumn) class, or subclass thereof.

[emptyIcon](https://bryntum.com/docs/gantt/api/Grid/column/RatingColumn#property-emptyIcon)
The empty rating icon to show

[filledIcon](https://bryntum.com/docs/gantt/api/Grid/column/RatingColumn#property-filledIcon)
The filled rating icon to show

[editable](https://bryntum.com/docs/gantt/api/Grid/column/RatingColumn#property-editable)
Allow user to click a rating icon to change the value

## Functions

Functions are methods available for calling on the class

[defaultRenderer](https://bryntum.com/docs/gantt/api/Grid/column/RatingColumn#function-defaultRenderer)
Renderer that displays a number of stars in the cell. Also adds CSS class 'b-rating-cell' to the cell.
