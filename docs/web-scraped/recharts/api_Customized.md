# Source: https://recharts.github.io/en-US/api/Customized/

### Customized 

**Deprecated:** Just render your components directly. Will be removed in 4.0

Customized component used to be necessary to render custom elements in Recharts 2.x. Starting from Recharts 3.x, all charts are able to render arbitrary elements anywhere, and Customized is no longer needed.

#### Properties 

- ::::: 
  [[component](#component)][C]*\@deprecated*

  ::: section
  Render your components directly, without Customized wrapper. Will be removed in 4.0
  :::

  ::: format
  FORMAT:

  ``` format-code
  Before: `<Customized component= />`
  After: `<MyCustomComponent />`
  ```
  :::
  :::::