# Source: https://gitlab.consulting/en-gb/blog/2025/10/31/what-is-yaml.md


# What is YAML? A Beginner-Friendly Format for Configurations and Pipelines
<h2 id="understanding-yaml-a-human-friendly-data-format">Understanding YAML: A Human-Friendly Data Format</h2>
<p>YAML, short for &ldquo;YAML Ain’t Markup Language,&rdquo; is a concise, human-readable data serialisation standard commonly used for configuration files and data exchange between languages with different data structures. Designed to be simple and intuitive, YAML aligns closely with most modern programming languages, making it an ideal choice for managing configuration in DevOps workflows, including CI/CD pipelines in GitLab.</p>
<p>Unlike other data formats like JSON or XML, YAML prioritises readability without unnecessary syntax noise. It uses indentation to represent hierarchy, eliminating the need for brackets or commas. This makes YAML not only easier to read but also less prone to syntax errors, especially when manually edited.</p>
<p>GitLab, a leading DevSecOps platform, leverages YAML for defining CI/CD pipelines in a <code>.gitlab-ci.yml</code> file. This single configuration file allows teams to dictate the entire automation process of software development — from building and testing to deployment. By using YAML, GitLab empowers users to define stages, specify scripts, set job dependencies, and manage environments seamlessly.</p>
<p>Here’s a quick example of what a basic GitLab CI/CD pipeline might look like in YAML:</p>
<pre tabindex="0"><code>stages:
  - build
  - test

build_job:
  stage: build
  script:
    - make build

test_job:
  stage: test
  script:
    - make test
</code></pre><p>This minimal syntax belies the power and flexibility YAML allows. YAML also supports complex data types like sequences (arrays), mappings (hashtables), and scalars, making it robust enough to handle sophisticated configurations without becoming verbose.</p>
<p>YAML’s wide adoption is not limited to GitLab. Tools such as Kubernetes, Ansible, and Docker Compose also rely on YAML, making learning it a crucial skill for DevOps professionals and developers.</p>
<p>If your team is adopting GitLab or looking to refine your YAML-based CI/CD pipelines, our experienced consultants at <a href="https://gitlab.consulting/en-gb/?mtm_campaign=internal-blog-link&amp;mtm_kwd=en-gb:what-is-yaml">IDEA GitLab Solutions</a> can assist. As a GitLab Select Partner supporting regions such as the UK, Czech Republic, Slovakia, Croatia, Serbia, Slovenia, Macedonia, Israel, South Africa, and Paraguay, we offer professional services and licensing tailored to your needs.</p>
<p>To learn more or get assistance with your YAML configurations and GitLab setup, <a href="https://gitlab.consulting/en-gb/?mtm_campaign=internal-blog-link&amp;mtm_kwd=en-gb:what-is-yaml">contact us today</a>.</p>


