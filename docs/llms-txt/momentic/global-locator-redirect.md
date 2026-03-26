# Source: https://momentic.ai/docs/global-locator-redirect.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Global locator redirect

> Global locator redirect is a feature that Momentic uses to link accessible elements to their visible, actionable counterparts.

## Why we built global locator redirect

Many sites use a combination of semantically correct html tags (e.g.
`<input type=”checkbox”>`) combined with other elements to create components
that both look good and are accessible. Usually, what this looks like in
practice is an invisible input element covered by elements that are styled to
look like something (for example, a checkbox).

This can cause problems when using Momentic because the AI chooses elements from
the accessibility tree (i.e. the input), but we interact with the page as a
regular user would (i.e. clicking on the button). Often, the outcome is that the
element that the AI chose fails stability checks (is not visible, has no
bounding box, or is covered by another element), causing test failures. Because
of this, we need a way to get from the accessible element that the AI chose to
an element on the page that playwright can actually interact with.

## How global locator redirect works

Global locator redirect works by hit testing points where the original element
is located. At each point, we determine the topmost element that is visible and
can be interacted with. If the original element is ever visible, we continue to
target that element. If the original element is never visible, we choose the
most common overlapping element that is also similar to the original. We
determine similarity by verifying that the elements are nearby in the DOM and
their bounding boxes are similar. This prevents us from redirecting to
overlapping elements that are obviously completely unrelated to the original.

## Configuration options

Currently, global locator redirect has three configuration options:

1. Always: global locator redirect is used for all interactive steps that target
   elements (click, type, etc.). For CLI users, this is the same as setting
   `globalLocatorRedirect` to `always` in `momentic.config.yaml`.

2. Click only: this option exists for backwards-compatibility reasons. When
   enabled, global locator redirect applies only to click steps. For CLI users,
   this is the same as setting `globalLocatorRedirect` to `true` in
   `momentic.config.yaml`.

3. Never: global locator redirect is never used. For CLI users, this is the same
   as setting `globalLocatorRedirect` to `false` in `momentic.config.yaml`.

By default, global locator redirect is always enabled.


Built with [Mintlify](https://mintlify.com).