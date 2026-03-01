# Source: https://visx.airbnb.tech/docs/bounds

Title: visx | @visx/bounds documentation

URL Source: https://visx.airbnb.tech/docs/bounds

Published Time: Tue, 11 Nov 2025 18:12:38 GMT

Markdown Content:
[![Image 1](https://img.shields.io/npm/dm/@visx/bounds.svg?style=flat-square)](https://www.npmjs.com/package/@visx/bounds "@visx/bounds npm downloads")

```
npm install --save @visx/bounds
```

### `withBoundingRects` HOC

It's often useful to determine whether elements (e.g., tooltips) overflow the bounds of their parent container and adjust positioning accordingly. The `withBoundingRects` higher-order component is meant to simplify this computation by passing in a component's bounding rect as well as its _parent's_ bounding rect.

### Example usage

Example usage with a `<Tooltip />` component

```
import React from 'react';
import { withBoundingRects, WithBoundingRectsProps } from '@visx/bounds';

type TooltipProps = WithBoundingRectsProps & {
  left: number;
  top: number;
  children?: React.ReactNode;
};

function Tooltip({ left: initialLeft, top: initialTop, rect, parentRect, children }: TooltipProps) {
  let left = initialLeft;
  let top = initialTop;

  if (rect && parentRect) {
    left = rect.right > parentRect.right ? left - rect.width : left;
    top = rect.bottom > parentRect.bottom ? top - rect.height : top;
  }

  return <div style={{ top, left, ...myTheme }}>{children}</div>;
}

export default withBoundingRects(Tooltip);
```
