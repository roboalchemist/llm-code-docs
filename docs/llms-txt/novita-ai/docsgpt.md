# Source: https://novita.ai/docs/guides/docsgpt.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# DocsGPT

> Seamlessly integrate Novita AI with DocsGPT to unlock powerful AI models for enhanced workflows.

DocsGPT simplifies documentation with AI-powered assistance. Integrating it with Novita AI enhances its performance, offering faster processing, scalable resources, and advanced model support for improved productivity.

This guide walks you through how to use DocsGPT with Novita AI based on the OpenAl APl, offering a way to query your content and get served customized answers.

## **How to use DocsGPT**

### **Prerequisites:**

**Docker:** Ensure you have [Docker ](https://docs.docker.com/engine/install/)installed and running on your system.

### **Launching DocsGPT (macOS and Linux)**

For macOS and Linux users, the easiest way to launch DocsGPT is using the provided `setup.sh` script. This script automates the configuration process and offers several setup options.

Step 1: Download the DocsGPT repository

* First, you need to download the DocsGPT repository to your local machine. You can do this using Git:

```bash  theme={"system"}
git clone https://github.com/arc53/DocsGPT.git
cd DocsGPT
```

Step 2: Run the `setup.sh` script

* Navigate to the DocsGPT directory in your terminal and execute the `setup.sh` script:

```bash  theme={"system"}
./setup.sh
```

This interactive script will guide you through setting up DocsGPT. It offers four options: using the public API, running locally, connecting to a local inference engine, or using a cloud API provider. The script will automatically configure your `.env` file and handle necessary downloads and installations based on your chosen option.

### **Launching DocsGPT (Windows)**

For Windows users, please refer to the [Docker Deployment documentation](https://docs.docsgpt.cloud/Deploying/Docker-Deploying) for detailed step-by-step instructions on setting up DocsGPT using Docker.

## **How to Integrate Novita AI API with DocsGPT**

Step 1: Log in to[ Novita AI ](https://novita.ai)and create an [API Key](https://novita.ai/settings/key-management)

<Frame>
    <img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/images/3-1LogintoNovitaAI.png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=b5c90a73cd15f73f327bb9c3be6ad701" alt="images/3-1LogintoNovitaAI.png" width="974" height="785" data-path="images/3-1LogintoNovitaAI.png" />
</Frame>

<Frame>
    <img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/images/3-2CreateanAPIKey.png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=48e2bd4c6e3642b24b12bff15417b13b" alt="images/3-2CreateanAPIKey.png" width="801" height="484" data-path="images/3-2CreateanAPIKey.png" />
</Frame>

Step 2: Select option4 and connect cloud API provider in your terminal

<Frame>
    <img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/images/2SelectOption4andConnectCloudAPIProvider.png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=bb8ddd2e4bdebda1e2d69e839823de97" alt="images/2SelectOption4andConnectCloudAPIProvider.png" width="1280" height="592" data-path="images/2SelectOption4andConnectCloudAPIProvider.png" />
</Frame>

Step 3: Choose option7 Novita and enter the API key you just created

<Frame>
    <img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/images/4ChooseOption7NovitaandEntertheAPIKeyYouJustCreated.png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=cfb5b58e584472599f3e9b3c14d4aa8d" alt="images/4ChooseOption7NovitaandEntertheAPIKeyYouJustCreated.png" width="1280" height="660" data-path="images/4ChooseOption7NovitaandEntertheAPIKeyYouJustCreated.png" />
</Frame>

Step 4: Wait for the startup process to complete

<Frame>
    <img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/images/5WaitfortheStartupProcesstoComplete.png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=332ea094376d7e01ee8419b7918b821e" alt="images/5WaitfortheStartupProcesstoComplete.png" width="1280" height="577" data-path="images/5WaitfortheStartupProcesstoComplete.png" />
</Frame>

Step 5: Access DocsGPT in your browser

* Once the setup is complete and Docker containers are running, navigate to [http://localhost:5173/](http://localhost:5173) in your web browser to access the DocsGPT web application.

<Frame>
    <img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/images/6AccesstheApplicationathttp-localhost-5173.jpeg?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=27b16380d04d4b5b39f6082b7b18b252" alt="images/6AccesstheApplicationathttp-localhost-5173.jpeg" width="3173" height="1749" data-path="images/6AccesstheApplicationathttp-localhost-5173.jpeg" />
</Frame>

Step 6: Stopping DocsGPT

* To stop DocsGPT, simply open a new terminal in the `DocsGPT` directory and run:

```bash  theme={"system"}
docker compose -f deployment/docker-compose.yaml down
```

* (or the specific `docker compose` command shown at the end of the `setup.sh` execution, which may include optional compose files depending on your choices).


Built with [Mintlify](https://mintlify.com).