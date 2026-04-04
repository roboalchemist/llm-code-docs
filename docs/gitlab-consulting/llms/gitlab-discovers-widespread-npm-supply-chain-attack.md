# Source: https://gitlab.consulting/en-gb/blog/2025/11/24/gitlab-discovers-widespread-npm-supply-chain-attack.md


# GitLab Discovers Widespread npm Supply Chain Attack
<h2 id="gitlab-uncovers-major-npm-supply-chain-threat">GitLab Uncovers Major npm Supply Chain Threat</h2>
<p>In a recent development, the GitLab Threat Insights Team has identified a substantial and ongoing supply chain attack targeting the JavaScript and Node.js ecosystem via the npm package manager. This newly uncovered operation involves thousands of malicious packages that seem automated and are designed to exfiltrate sensitive environment data such as tokens, credentials, and configuration files.</p>
<p>This discovery underscores how open-source ecosystems continue to be high-value targets for attackers. Upon further investigation, the GitLab team discovered obfuscated scripts and base64-encoded payloads within package installation routines — potentially allowing attackers to harvest credentials from affected systems silently and persistently.</p>
<p>These malicious packages exploit the trust developers place in published open-source components. They rely heavily on mimicry of popular package names through typosquatting techniques. Once installed, the hostile code begins to extract confidential files such as .env, .bash_history, .ssh configurations, and IDE-specific settings.</p>
<p>GitLab has reported the issue to GitHub and npm maintainers, who have initiated package removals and takedown procedures. In addition, GitLab&rsquo;s secure software development practices, Threat Insights automation, and community partnerships were instrumental in identifying and counteracting this campaign.</p>
<p>This incident further validates GitLab’s commitment to DevSecOps and highlights the necessity for organisations to adopt an integrated and proactive approach to security, especially as software supply chains grow more complex and vulnerable to manipulation.</p>
<p><strong>Get Expert Support</strong><br>
If your organisation depends on npm packages for development, now is the time to evaluate your software supply chain security. <a href="https://gitlab.consulting/en-gb/?mtm_campaign=internal-blog-link&amp;mtm_kwd=en-gb:gitlab-discovers-widespread-npm-supply-chain-attack">IDEA GitLab Solutions</a> is a Select GitLab Partner offering professional services, licensing, and consultancy across the UK, Czech Republic, Slovakia, Serbia, Croatia, Slovenia, Macedonia, Israel, South Africa, and Paraguay. Our experienced experts can help you identify risks, implement security scanners, and adopt GitLab’s comprehensive DevSecOps capabilities for full lifecycle protection.</p>


