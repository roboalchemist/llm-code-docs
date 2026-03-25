# Source: https://plivo.com/docs/aiagent/aistudio/nodereference/customcode.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Code

> The Custom Code Node allows you to write and integrate custom code into your agent flow

The **Custom Code Node** allows users to integrate custom code directly into their workflows. This feature enables you to write Python code to perform specific tasks or calculations that are beyond the built-in capabilities of other nodes. Whether you want to process data, call external services, or create complex logic, the **Custom Code Node** provides flexibility and power.

### How to Use the Custom Code Node

1. **Adding the Node**:
   * Select the **Custom Code Node** from the list of available nodes.
   * The node opens with a Python editor where you can either generate the code automatically via **Plivo's code generator** or manually write the code.
2. **Writing the Code**:
   * Your code must contain a `main()` function with typed parameters and primitive return values.
   * The function signature should look like this:

     ```python  theme={null}
     def main(arg1: str, arg2: str) -> dict:
     ```
3. **Using Environment Variables**:
   * The code can make use of **secret variables** stored as environment variables. This is useful for integrating sensitive data without exposing them directly in the code.
4. **Generating the Schema**:
   * After writing the code, click on the **Generate Schema** button. This will generate the schema based on the function’s input and output types.
5. **Verifying the Schema**:
   * Review and verify the generated schema. Ensure that the arguments and return values are correctly configured.
6. **Setting Argument Values**:
   * Once the schema is generated, the input arguments will be auto-filled with a default value set to **“Autofill with AI”**.
   * You can manually modify the argument values if needed.
7. **Using the Result**:
   * The result of the custom code will be passed as **agent variables**. These variables can be used in subsequent nodes to influence the flow or provide context for further actions.

### Example Use Case

Let’s say you want to combine two pieces of customer data, such as the **customer name** and **purchase history**, into a personalized message. You can write a simple Python function like this:

```python  theme={null}
def main(customer_name: str, purchase_history: list) -> dict:
    result = f"Hello {customer_name}, thank you for your recent purchase: {purchase_history[-1]}"
    return {"personalized_message": result}
```

This function takes the **customer name** and their **purchase history**, and returns a **personalized message**.

Once this is set up, the **personalized\_message** variable will be available for use in the next nodes in the flow, such as displaying it to the user or sending it via SMS.

### Best Practices

* **Write Concise Code**: Keep the code modular and easy to understand. This helps with debugging and future updates.
* **Test Thoroughly**: Always test the code in the **Playground** to ensure it behaves as expected and handles all edge cases.
* **Avoid Overcomplicating**: Use built-in nodes for simpler tasks. Use the Custom Code Node only when more advanced logic is needed.
* **Use AI to Autofill**: Take advantage of the "Autofill with AI" functionality for dynamic inputs whenever possible.

### Troubleshooting

* **Schema Not Generating**: Ensure the **main()** function is correctly defined and that the code returns a primitive data type (e.g., string, integer, or dict).
* **Incorrect Result**: Verify the argument values and make sure they are properly passed into the function. Ensure the return type matches the expected output.
