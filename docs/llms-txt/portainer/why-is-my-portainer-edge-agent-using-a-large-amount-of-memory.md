# Source: https://docs.portainer.io/2.33-lts/faqs/troubleshooting/agents-and-environment-management/why-is-my-portainer-edge-agent-using-a-large-amount-of-memory.md

# Source: https://docs.portainer.io/sts/faqs/troubleshooting/agents-and-environment-management/why-is-my-portainer-edge-agent-using-a-large-amount-of-memory.md

# Source: https://docs.portainer.io/faqs/troubleshooting/agents-and-environment-management/why-is-my-portainer-edge-agent-using-a-large-amount-of-memory.md

# Why is my Portainer Edge Agent using a large amount of memory?

#### **Problem**

Some users have experienced excessive memory usage from the Portainer Edge Agent running on their devices. After restarting the container, memory usage typically drops back but gradually climbs again over time.

#### **Cause**

This issue is caused by a memory leak affecting **Edge Agent versions from 2.21.3 up until the fix introduced in version 2.26**. These versions are known to exhibit abnormal memory growth during runtime.

#### **Resolution**

The memory leak was **resolved in version 2.26**. Updating the Edge Agent to **2.26 or higher** will resolve the issue.
