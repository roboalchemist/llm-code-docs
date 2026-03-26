# Source: https://docs.tabnine.com/main/getting-started/tabnine-agent/agents-in-action.md

# Agents in Action

## Creating a Wiki in Notion from the IDE

{% embed url="<https://www.youtube.com/watch?v=tFhhAgmihVo>" %}

## Adding Nullness Annotations to a Java Project

{% embed url="<https://www.youtube.com/watch?v=uwUg1QPfXqY>" %}

In this example, there may be a null pointer exception when the Customer returned from the service is null. However, the built-in static analysis in vscode (and similar tools) is not able to track the data flow in the program and flag that.

```java
public class App {
    public static void main(String[] args) {
        CustomerService customerService = new CustomerService();
        NotificationService notificationService = new NotificationService();

        Customer customer = customerService.getCustomerById("999"); // This is null
        String email = customer.getEmail(); // NPE here!

        notificationService.sendEmail(email, "Welcome!");
    }
}
```

One way to assist the static analysis is to add so called *nullness annotations*. These annotations make tracking dataflow easier by tagging parameters, fields, and return value of functions as `Nullable` or `NotNull`.

After adding the annotations, the agent is able to fix the code to deal with these potential null values. It modifies the code, and the tests to match the new corrected code.
