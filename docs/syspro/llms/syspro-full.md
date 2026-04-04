# llms.txt â Syspro (www.syspro.com)
# Purpose: Guidance for AI/LLM systems that retrieve, summarize, or cite Syspro web content.
# Last updated: 2026-03-02

site: https://www.syspro.com

contact: https://www.syspro.com/contact-us/
policies:
  privacy: https://www.syspro.com/privacy-policy/
  terms: https://www.syspro.com/terms-of-service/
  cookies: https://www.syspro.com/cookie-policy/

# =========================
# Allowed usage
# =========================
allow:
  - Retrieval for answering user questions about Syspro ERP and public-facing information
  - Summarization and quoting short excerpts with attribution (link back to the canonical URL)
  - Indexing of publicly accessible pages that return HTTP 200 and are self-canonical

# =========================
# Disallowed / restricted
# =========================
disallow:
  - Any authenticated, customer-only, paywalled, or gated areas
  - Form submissions, demo-request automation, scraping of contact details or lead forms
  - Accessing or storing personal data, user sessions, or credentials
  - Any attempt to bypass access controls, rate limits, or robots directives

# =========================
# Crawl scope (public site)
# =========================
# Prefer canonical HTTPS + www + trailing slash URLs.
preferred_host: https://www.syspro.com

# High-value hubs (recommended for understanding site structure)
key_pages:
  - https://www.syspro.com/
  - https://www.syspro.com/product/
  - https://www.syspro.com/industries/
  - https://www.syspro.com/about-syspro/
  - https://www.syspro.com/blog/
  - https://www.syspro.com/press_release/
  - https://www.syspro.com/erp-product-tour/
  - https://www.syspro.com/solutions/

# =========================
# Exclusions (paths to avoid)
# =========================
# These are commonly non-content, admin, transactional, or duplicate surfaces.
exclude_paths:
  - /wp-admin/
  - /wp-login.php
  - /wp-json/
  - /xmlrpc.php
  - /?s=
  - /search/
  - /thank-you
  - /thank-you/
  - /partnerup-thank-you/
  - /thank-you-for-your-request/
  - /cart/
  - /checkout/
  - /my-account/

# =========================
# External / subdomain guidance
# =========================
# These may have separate policies; treat as out-of-scope unless their own llms.txt allows.
out_of_scope_domains:
  - https://customers.syspro.com
  - https://help.syspro.com
  - https://developer.syspro.com
  - https://trust.syspro.com
  - https://careers.syspro.com
  - https://videos.syspro.com

# =========================
# Attribution & freshness
# =========================
attribution:
  - Always cite the canonical URL when referencing Syspro content
  - Prefer the most recently updated official pages and hub pages above

# End of file