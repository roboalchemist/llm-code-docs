# Source: https://docs.api7.ai/apisix/enterprise-feature/custom-plugins-and-sandbox.md

# Custom Plugins and Sandbox

Custom plugins are essential in scenarios where existing plugins cannot fully meet specific requirements. On the one hand, they allow the API gateway to connect to proprietary systems, legacy infrastructure, or non-standard protocols that cannot be addressed with off-the-shelf solutions. On the other hand, using custom plugins, users can enable the customization and extension of the API gateway to address unique business needs accordingly.

However, custom plugins have inherent security risks, especially when executing user-written code. Sandbox is used to help mitigate the risks associated with granting full access to system resources. By providing isolated environments in which the plugin runs, sandboxing protects the underlying system and services from potential vulnerabilities or malicious behavior.

To use a custom plugin in API7 Enterprise, users simply upload the plugin file, select the appropriate catalog for the organization, provide details such as the plugin's usage description, and author information, and optionally upload a logo. Once configured, the plugin can be added and utilized in the system, and its name must remain unique to avoid conflicts. After the custom plugin is created, it can be easily referenced by all gateway groups and services, enhancing the overall flexibility and efficiency of API management.

![Add Custom Plugin in API7 Enterprise](https://static.api7.ai/uploads/2024/12/13/fXAqAfcq_custom-plugins.jpeg)

## Key Features[â](#key-features "Direct link to Key Features")

* Support Lua for custom plugin development exclusively to ensure consistency with the core of API7 Enterprise while maintaining lightweight and high-performance operation.
* Custom plugins can be used as other built-in plugins, which can be applied directly to routes or services, enabling flexible and targeted API traffic management.
* Custom plugins can be activated across all gateways or specifically assigned to particular gateway groups, offering granular control over where and when the plugins run.
* Sandboxing offers a secure and controlled environment that limits the execution scope of custom plugins, balancing between safety and the flexibility needed for custom plugin operations.

## Use Cases[â](#use-cases "Direct link to Use Cases")

### Integrate with Legacy or Non-Standard Protocols[â](#integrate-with-legacy-or-non-standard-protocols "Direct link to Integrate with Legacy or Non-Standard Protocols")

When enterprises need to integrate their API gateway with internal systems or legacy applications, they may need to tailor plugins suitable for their systems. In such cases, custom plugins are essential for organizations looking to maintain compatibility with their existing infrastructure while adopting modern API management practices.

Many legacy systems rely on proprietary protocols or data formats that are not natively supported by modern API management tools. Furthermore, standard plugins may not fully meet the requirements when dealing with non-standard protocols or data formats. To bridge this gap, custom plugins can be developed to handle unique business needs.

For instance, custom plugins can perform data transformations between proprietary formats and industry-standard formats. This ensures that the API gateway can effectively manage requests and responses between legacy or non-standard protocol services and new ones.

### Tailor Extensive Features[â](#tailor-extensive-features "Direct link to Tailor Extensive Features")

Custom plugins offer a way to tailor the API gateway to meet the specific needs of an organization, especially when dealing with complex use cases. Custom plugins allow businesses to enhance their API gateways with highly specific functionalities that go beyond the capabilities of built-in features.

By extending the API gateway with custom plugins, businesses can not only preserve their existing infrastructure but also modernize and future-proof their systems. This approach allows businesses to stay agile and adapt to evolving technological demands, ensuring long-term scalability and flexibility.

### Balance Flexibility and Security with Sandbox[â](#balance-flexibility-and-security-with-sandbox "Direct link to Balance Flexibility and Security with Sandbox")

In API7 Enterprise, custom plugins can be used in many ways. For example, they can be used as built-in plugins, enabling full access to all functions of the API gateway. While this offers maximum flexibility, it comes with increased security risks. Custom plugins can also be used in a sandbox, which helps mitigate risks by restricting the plugin's access to the system, allowing only safe and controlled interactions with the API gateway.

In the future, custom plugin security can be further enhanced by writing configuration files, rather than exposing them on the dashboard. Sandboxes offer an optimal solution for organizations looking to balance flexibility with security, ensuring that the API gateway remains safe and efficient.
