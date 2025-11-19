# Source: https://dev.writer.com/home/prompt_injections.md

# Secure prompts against attacks

Security measures against prompt injections, jailbreak attacks, and secrets leakage

## Introduction

As AI systems like Writer models become increasingly integrated into a wide range of applications, the importance of securing them against various types of attacks becomes paramount. In this article, we delve into the technical details of how Writer safeguards its AI models against prompt injections, jailbreak attempts, and the leakage of sensitive information.

## Measures against prompt injections

<Tabs>
  <Tab title="Input sanitization">
    One of the first lines of defense is input sanitization, where incoming prompts are screened for potentially malicious code or harmful strings. Sophisticated Natural Language Processing (NLP) techniques, combined with standard cybersecurity measures, are used to detect and remove or neutralize suspicious inputs.
  </Tab>

  <Tab title="Rate limiting">
    To prevent brute-force attacks and other malicious activities, Writer often implements <a href="/api-reference/rate-limits">rate limiting</a> on the API requests. This ensures that a user can't overload the system with a large number of potentially harmful prompts in a short amount of time.
  </Tab>

  <Tab title="RBAC">
    Role-cased access control (RBAC) to more advanced or potentially risky functionalities is restricted based on roles. This prevents unauthorized users from injecting malicious prompts that could potentially exploit these functionalities.
  </Tab>
</Tabs>

## Safeguards against jailbreak attacks

<Tabs>
  <Tab title="Runtime environment isolation">
    The runtime environment in which the AI models operate is isolated from the rest of the system. This isolation is often achieved using containerization technologies like Docker, which limit the resources and system calls available to the running model.
  </Tab>

  <Tab title="Anomaly detection systems">
    Advanced anomaly detection systems are put in place to monitor the behavior of the AI models in real-time. Any unusual patterns or inconsistencies could trigger alerts, initiating immediate investigation and potential shutdown of the affected instance.
  </Tab>

  <Tab title="Code review and static analysis">
    Before deployment, the codebase undergoes rigorous reviews and static analysis to ensure that there are no vulnerabilities that could be exploited to "jailbreak" the AI system.
  </Tab>
</Tabs>

## Measures against secrets leakage

<Tabs>
  <Tab title="Encryption and secure storage">
    All sensitive information, including security keys and credentials, is encrypted using state-of-the-art encryption algorithms. These encrypted secrets are stored in secure vaults that are accessible only to authorized personnel.
  </Tab>

  <Tab title="Zero trust architecture">
    A Zero trust architecture is employed, which means that every request or interaction with the AI system is treated as potentially malicious until proven otherwise. This adds an extra layer of security against unauthorized access and data leakage.
  </Tab>
</Tabs>

## Conclusion

Security is a multi-faceted challenge that requires a holistic approach. Writer employs a combination of advanced technologies and best practices to safeguard its AI models against prompt injections, jailbreak attacks, and the leakage of sensitive information. While no system can be 100% secure, these measures provide a robust framework for identifying, mitigating, and responding to various security threats.
