# Source: https://novita.ai/docs/guides/owl.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# OWL

> Optimize Your Workflow with Novita AI and OWL.

OWL is an open-source framework for multi-agent collaboration that specializes in real-world task automation, built on the CAMEL-AI Foundation. By integrating with various AI models, OWL combines dynamic agent interactions with powerful toolkits for online search, browser automation, document processing, and code execution. This framework enables more natural, efficient, and robust task automation across diverse domains, delivering actionable insights tailored to your specific needs.

This guide will enable you to seamlessly integrate Novita AI with OWL and elevate your AI-driven processes for faster, smarter outcomes.

## **How to Integrate Novita AI with RAGFlow**

### **Step 1: Pre-Configuration Setup**

1. **Access the API Endpoint**

* Use the official API endpoint: [https://api.novita.ai/openai](https://api.novita.ai/openai).

2. **Create an API Key**

* Visit the [key management page](https://novita.ai/settings/key-management) and select `Add New Key` to generate your API key.

  <img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/images/-VisitthekeymanagementpageandselectAddNewKeytogenerateyourAPIkey..png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=ba76fbe63ca9f6246b5b7254ced54252" alt="Visitthekeymanagementpageandselect Add New Keytogenerateyour AP Ikey Pn" width="1280" height="689" data-path="images/-VisitthekeymanagementpageandselectAddNewKeytogenerateyourAPIkey..png" />
* Keep your API key safe.
  * **Note:** API keys are securely encrypted on the server. If you lose it, you’ll need to delete the old key and create a new one.

    <img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/images/-KeepyourAPIkeysafe-1.png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=aee9e2e9c06051a02c71cf7979265596" alt="Keepyour AP Ikeysafe 1 Pn" width="1280" height="692" data-path="images/-KeepyourAPIkeysafe-1.png" />

    <img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/images/-KeepyourAPIkeysafe-2.png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=7a06cefa2a3860de9db5ff52a2f95e91" alt="Keepyour AP Ikeysafe 2 Pn" width="1280" height="692" data-path="images/-KeepyourAPIkeysafe-2.png" />

3. **Identify the Model ID**

* meta-llama/llama-4-scout-17b-16e-instruct

### **Step 2: Install OWL**

* To begin, download and install OWL by following the step-by-step instructions on the Github: [https://github.com/camel-ai/owl](https://github.com/camel-ai/owl).

### **Step 3: Configure OWL**

* Prepare OWL for use by setting up environment variables and adding your API key. Run the following commands in your terminal:

```bash  theme={"system"}
cd owl
cp .env_template .env
```

* Start OWL and specify your task by executing:

```bash  theme={"system"}
python examples/run_novita_ai.py
```

<img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step3-ConfigureOWL.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=d54fb187a6aaf37bf22c7d8a03374c1c" alt="Step3 Configure OWL Pn" width="1280" height="545" data-path="images/Step3-ConfigureOWL.png" />

### **Step 4: View Results**

1. **Terminal Output**

* Once launched, OWL will display the execution results directly in the terminal window.

  <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/TerminalOutput-1.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=c93696ac4dfe47b305d465243b57e024" alt="Terminal Output 1 Pn" width="1280" height="529" data-path="images/TerminalOutput-1.png" />

  <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/TerminalOutput-2.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=eea7a48cd8070d65c177707fd2027457" alt="Terminal Output 2 Pn" width="1280" height="459" data-path="images/TerminalOutput-2.png" />

2. **Web Interface**

* For a more intuitive experience, use OWL’s web-based interface. Launch it by running:

```bash  theme={"system"}
cd owl
python webapp.py
```

<img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/WebInterface-1.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=89aa59be53d17f128496533510564add" alt="Web Interface 1 Pn" width="1280" height="281" data-path="images/WebInterface-1.png" />

<img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/WebInterface-2.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=0b268cbf677b9846ac4a6f535b6f7958" alt="Web Interface 2 Pn" width="1280" height="834" data-path="images/WebInterface-2.png" />

* Steps to use the Web UI:
  * Select `run_novita_ai` from the left-hand menu and go to the `Environment Variable Management` tab on the right and input your `NOVITA_API_KEY`.

    <img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/images/-StepstousetheWebUI-1.png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=74c433bed70e116dcfda4124e619b39e" alt="Stepstousethe Web UI 1 Pn" width="1280" height="864" data-path="images/-StepstousetheWebUI-1.png" />
  * Click `Run` to execute your task.

    <img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/images/-StepstousetheWebUI-2.png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=ff4ce3d506aba0093547fc06e0368794" alt="Stepstousethe Web UI 2 Pn" width="1280" height="827" data-path="images/-StepstousetheWebUI-2.png" />
  * To perform a new task, update the input field and click `Run` again.

    <img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/images/-StepstousetheWebUI-3.png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=dafac36d880a75665bb026867f982540" alt="Stepstousethe Web UI 3 Pn" width="1280" height="841" data-path="images/-StepstousetheWebUI-3.png" />

    <img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/images/-StepstousetheWebUI-4.png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=7601da5147281374c130d7145652e280" alt="Stepstousethe Web UI 4 Pn" width="1280" height="772" data-path="images/-StepstousetheWebUI-4.png" />
  * Results will be displayed in the terminal, or a new file will be generated in the root directory, depending on the task.

    <img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/images/-StepstousetheWebUI-5.png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=b89fc1b455ff6aa18c9d98a69ddc381f" alt="Stepstousethe Web UI 5 Pn" width="1280" height="1057" data-path="images/-StepstousetheWebUI-5.png" />
  * Alternatively, you can directly input your desired task into the content box and click the `Run` button to execute it.

    <img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/images/-StepstousetheWebUI-6.png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=a7a423e4fd0cc8c4995fb50503a972e8" alt="Stepstousethe Web UI 6 Pn" width="1280" height="777" data-path="images/-StepstousetheWebUI-6.png" />


Built with [Mintlify](https://mintlify.com).