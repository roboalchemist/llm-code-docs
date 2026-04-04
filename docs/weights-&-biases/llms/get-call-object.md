# Source: https://docs.wandb.ai/weave/guides/tracking/get-call-object.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a handle to the Call object during execution

> Access the W&B Weave Call object at runtime for feedback, display names, and other metadata

In Weave, when you use an Op, you can call the functions directly as you would any function:

<CodeGroup>
  ```python Python lines theme={null}
  @weave.op
  def my_op():
      ...

  my_op()
  ```

  ```typescript Typescript lines theme={null}
  function myFunction() {
      ...
  }

  const myFunctionOp = weave.op(myFunction)
  ```
</CodeGroup>

However, you can instead get access to the Call object directly by invoking the `op.call` method, which returns both the result and the `Call` object.

<Tabs>
  <Tab title="Python">
    ```python lines theme={null}
    @weave.op
    def my_op():
    ...

    output, call = my_op.call()
    ```

    From here, the `call` object contains all the information about the Call, including the inputs, outputs, and other metadata. You can use `call` to set, update, fetch additional properties, or add feedback.

    If your Op is a method on a class, you need to pass the instance of the class as the first argument to `call`. The following example shows getting a handle to a Call object that is a method on a class:

    ```python lines theme={null}
    import weave

    # Initialize Weave Tracing
    weave.init("intro-example")

    class MyClass:
        # Decorate your method
        @weave.op
        def my_method(self, name: str):
            return f"Hello, {name}!"

    instance = MyClass()

    # Pass `instance` as the first argument to `call`.
    result, call = instance.my_method.call(instance, "World")
    ```
  </Tab>

  <Tab title="TypeScript">
    ```plaintext  theme={null}
    This feature is not available in the TypeScript SDK yet.
    ```
  </Tab>
</Tabs>
