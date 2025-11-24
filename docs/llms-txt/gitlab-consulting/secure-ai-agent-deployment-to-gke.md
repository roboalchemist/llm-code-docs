# Source: https://gitlab.consulting/en-gb/blog/2025/11/10/secure-ai-agent-deployment-to-gke.md


# Secure AI Agent Deployment to GKE Using GitLab CI/CD
<h2 id="securely-deploying-ai-agents-to-gke-with-gitlab">Securely Deploying AI Agents to GKE with GitLab</h2>
<p>As AI-driven applications continue to soar, deploying intelligent agents efficiently and securely becomes paramount. GitLab provides a complete DevSecOps approach to streamline deployment pipelines for AI agents across Kubernetes environments, particularly with Google Kubernetes Engine (GKE).</p>
<p>In a recent technical showcase, GitLab demonstrated how to securely deploy a Retrieval-Augmented Generation (RAG) chatbot agent on GKE. This use case not only highlighted GitLab&rsquo;s powerful CI/CD capabilities, but also reinforced key security practices, such as secret management and infrastructure-as-code (IaC) for resource automation.</p>
<p>The process begins with an Open Source chatbot agent powered by LangChain and FastAPI. It uses the RetrievalQA framework, which taps into external knowledge sources to enhance accuracy. The AI agent connects to Fireworks.ai&rsquo;s Mistral-7B LLM, a smart language model tailored for context-driven interactions. Source documents are ingested into a Postgres database enhanced with pgvector for similarity search indexing. This provides faster, more relevant answers based on stored content.</p>
<p>The infrastructure setup leans on Terraform for replicable and trackable deployment. Terraform modules for GKE clusters, CloudSQL for Postgres, and secret rotation integrate seamlessly into version control, enabling consistent infrastructure across all environments.</p>
<p>In GitLab, CI/CD pipelines manage the provisioning of both infrastructure and application. The use of custom runners allows isolated execution — ideal for enterprise-grade security. GitLab’s dynamic secrets handling prevents sensitive data from being stored in plaintext, reducing vulnerability risks across the software supply chain.</p>
<p>This setup enables streamlined iteration, auditable deployment processes, and scalable infrastructure that&rsquo;s ideal for production-level AI workloads.</p>
<p>For organisations across <strong>the Czech Republic, Slovakia, Croatia, Serbia, Slovenia, Macedonia, the United Kingdom</strong>, and beyond — including our remote consultants in Israel, South Africa, and Paraguay — <a href="https://gitlab.consulting/en-gb/?mtm_campaign=internal-blog-link&amp;mtm_kwd=en-gb:secure-ai-agent-deployment-to-gke">IDEA GitLab Solutions</a> offers expert consulting, GitLab licensing, and tailored solutions to support AI innovation in a secure and compliant manner.</p>
<p>Start transforming your deployment strategy for AI agents today with GitLab.</p>


