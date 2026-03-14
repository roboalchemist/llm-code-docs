# Source: https://docs.linkup.so/pages/documentation/tutorials/company-data-enrichment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Automating Lead Qualification

> Learn how to automatically research and score your leads using Linkup AI to prioritize high-value prospects

<Note>
  **Time-saving Automation:** This tutorial shows you how to build a system that
  can process hundreds of leads automatically, saving 5+ hours of manual
  research per week while ensuring you focus on the right opportunities.
</Note>

# The Challenge: From Manual Research to Automated Intelligence

Every day, new users sign up for Linkup. When they do, we capture two crucial pieces of information:

* Their company name
* Their email address

When we had a few signups every day, our team could spend time researching each company manually and identify the most important ones. But as we grow and the number of daily signups becomes too high to handle manually, we face a challenge: **How do we know which leads to focus on first?**

**Before automation:** Our sales team spent hours manually researching each company, often missing high-value opportunities because of the volume.

**After automation:** We instantly identify and prioritize the most promising leads based on AI-powered analysis of their company profile and website.

## The Solution: An Automated Enrichment Pipeline to Qualify Leads

By the end of this tutorial, you'll have a working system that:

1. **Finds Official Websites:** Cross-references company names with email domains
2. **Analyzes Company Websites:** Determines how well each company fits your ideal customer profile
3. **Prioritizes Leads:** Assigns a score from 1-5 so your team knows who to contact first

For this tutorial, we are going to use:

* **Attio CRM data pull:** to generate the input .json file with org names and company domains.
* **Linkup API:** to search the web and enrich the leads.

## The Complete Process: Visual Overview

Here's how the data transforms throughout this process:

```mermaid  theme={null}
graph LR
    A[User Signup] -->|Extract| B[Name + Email Domain]
    B -->|Linkup API Lookup| C[Verified Website]
    C -->|Linkup API Analysis| D[ICP Score]

    style A fill:#f9d4d4
    style D fill:#c9f7c9
```

## Project Setup: Getting Started

Let's start with our project structure and requirements:

```bash  theme={null}
your-project-directory/
├── .env                                 # API keys
├── organization_names_with_domains.json # Input file
├── company_analysis_results.json        # Output file
└── linkup_enrich.py                     # Enrichment script
```

<Steps>
  <Step title="Create Your Environment">
    First, let's set up our environment and install the required packages:

    ```bash  theme={null}
    # Create a virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    #### Install required packages
    pip install requests python-dotenv
    ```
  </Step>

  <Step title="Set Up Your API Keys">
    Create a `.env` file in your project directory with your API keys:

    ```env  theme={null}
    LINKUP_API_KEY=your_api_key_here
    ATTIO_API_KEY=your_attio_api_key_here
    ```

    <Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
      Create a Linkup account for free to get your API key.
    </Card>

    <Note type="warning">
      Never put your API KEYS directly in your code. Always include them in a `.env`
      file.
    </Note>
  </Step>

  <Step title="Add your input file">
    Our starting point is a JSON file containing user signup information:

    * Organizations
    * Email address (or rather: the domains of the email addresses)

    In our case, we extracted this file from our CRM (Attio) since this is where we send signup data (and want to send the enriched data back after the process). This file could be the output of a signup form or any lead generation document you're using.

    Let's look at the structure:

    ```json  theme={null}
    "034Q2K4NXVY6JIWZ": {
        "name": "test",
        "people_ids": "01HQ2K4NX123457",
        "domain": "anthropic.com"
    },
    "01HQ2K4NXVY6GPWZ": {
        "name": "Personal",
        "people_ids": "01HQ2K4NX123456",
        "domain": "live.fr"
    },
    "CHDY2K4NXVY6GJUE": {
        "name": "MistralAI",
        "people_ids": "01HQ2K4NX120987",
        "domain": "gmail.com"
    },
    ```

    <Note>
      As you can see, data quality might not be optimal:

      * Some users provide personal email addresses
      * Others do not put the name of their company

      This is why we're combining both information to try and get better results.

      We could add a Linkup search for LinkedIn profiles associated with the first part of the emails.
    </Note>
  </Step>
</Steps>

## The Enrichment Pipeline: Step-by-Step Implementation

Before we share the whole script (see the end of the tutorial), let's break down our enrichment pipeline into steps:

<Steps>
  <Step title="Finding Official Websites">
    Our first challenge is to reliably find the official website for each company. We'll use Linkup's API with a carefully crafted prompt:

    ```python {8-13} theme={null}
    url = "https://api.linkup.so/v1/search"
    headers = {
        "Authorization": f"Bearer {LINKUP_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
      "q": f"Based on the name {company_name} and the email domain {domain_info}, " +
          f"find the most likely company website URL. Only return a result if you are 90% sure " +
          f"this is the correct website. If {company_name} seems like a generic company name " +
          f"(e.g. personal, perso, n/a), return nothing. If the domain is a generic domain " +
          f"(e.g. gmail.com, yahoo.com, hotmail.com, icloud.com), do not consider it. " +
          f"Only consider professional email domains. Only return the company domain URL.",
      "depth": "standard",
      "outputType": "sourcedAnswer",
      "includeImages": "false"
    }
    ```

    <Tip>
      **Understanding key parameters**:

      * **depth: "standard"**: For website finding,
        "standard" depth provides a good balance between speed and accuracy
      * **outputType: "sourcedAnswer"**: Returns a natural language answer with just
        the URL
      * **includeImages: "false"**: We don't need images, which speeds up
        the response
    </Tip>

    <Accordion title="Prompt Design Strategy">
      Notice how the prompt includes specific instructions:

      * Only return results with 90% confidence
      * Ignore generic company names
      * Skip generic email domains
      * Focus on professional email domains
        These constraints help ensure we get high-quality, reliable results.
    </Accordion>
  </Step>

  <Step title="Analyzing Company Fit">
    Once we have the website, we need to determine how well each company fits our ideal customer profile. For this, we're using a second prompt to Linkup that gives the domain URL as input and asks for an ICP score as output.

    ```python {7-13} theme={null}
    url = "https://api.linkup.so/v1/search"
    headers = {
      "Authorization": f"Bearer {LINKUP_API_KEY}",
      "Content-Type": "application/json"
    }
    payload = {
      "q": f"Analyze the website {website_url}. Determine if this company could be an Ideal Customer Profile (ICP) " +
            f"for my company https://www.linkup.so/. For context, we are selling a search API. We target AI companies, " +
            f"Tech Companies, and corporates, as well as consulting and financial firms. " +
            f"Our search API allows companies to enrich applications with real-time web knowledge and business intelligence, " +
            f"at scale. Consider factors like industry and whether they're likely to need API services, and if they " +
            f"might be building software products. Return a rating from 1 to 5, 1 being lowest ICP, 5 being highest ICP. " +
            f"Universities and schools should get a 3. Only return the rating, nothing else.",
      "depth": "deep",
      "outputType": "sourcedAnswer",
      "includeImages": "false"
    }
    ```

    <Tip>
      **We use 'deep' depth** for ICP analysis because:

      * It provides more thorough analysis of the company website
      * It considers more pages and context when making its assessment
      * The accuracy of ICP scoring is worth the slightly longer processing time
    </Tip>

    **The output will be an ICP (Ideal Customer Profile) score ranging from 1-5:**

    * **1** - Perfect match - AI companies, Tech Companies with clear API needs
    * **2** - Strong potential - Corporates, Financial Firms, Consulting companies
    * **3** - Moderate fit - Universities, Educational Institutions, Research Organizations
    * **4** - Might need education - Companies with potential but unclear use cases
    * **5** - Probably not a good fit - Consumer businesses, local services, etc.

    Notice how we don't have to explicitly explain our rating system - AIs understand it intuitively.
  </Step>

  <Step title="Checking the results">
    After we run the script with these two API calls, a new file will be created with two new fields for each company:

    * Website domain
    * ICP Analysis

    ```json {5-6,12-13,19-20} theme={null}
    "034Q2K4NXVY6JIWZ": {
      "name": "test",
      "people_ids": "01HQ2K4NX123457",
      "domain": "anthropic.com"
      "website": "https://www.anthropic.com/"
      "icp_analysis": "5"
    },
    "01HQ2K4NXVY6GPWZ": {
      "name": "Personal",
      "people_ids": "01HQ2K4NX123456",
      "domain": "live.fr"
      "website": ""
      "icp_analysis": "1"
    },
    "CHDY2K4NXVY6GJUE": {
      "name": "MistralAI",
      "people_ids": "01HQ2K4NX120987",
      "domain": "gmail.com"
      "website": "https://mistral.ai/"
      "icp_analysis": "5"
    }
    ```

    Great! As you can see, combining company name and email domain allows us to identify ICPs we would have missed if we had only considered one of the two factors.

    <Note>
      The complete script below includes additional functionality beyond the two
      Linkup API calls shown above. For example:

      * We implement logic to skip the ICP analysis call when no website is found, automatically assigning a rating of "1" (as seen in the second example output)
      * We include an incremental processing system that only analyzes companies without existing ratings, preventing redundant API calls and allowing you to resume processing after interruptions
      * The code handles file operations safely, maintains a processing counter, and includes appropriate rate limiting between API calls
    </Note>
  </Step>
</Steps>

## Next Steps and Customization Opportunities

This script is just the beginning! Here are ways you can extend it:

1. **Additional Enrichment**: Add other API calls to find additional information (company industry, value chain positioning, pricing strategy...)
2. **CRM Integration**: Add code to push results back to your CRM automatically (what we're doing at Linkup)
3. **Multi-threaded Processing**: Speed up processing by handling multiple companies simultaneously

In our case, we're actually sending the data back to our CRM so that new signups get automatically rated. We then have live alerts that tell us when important customers sign up to our products.

## The Complete Code

Below is the complete Python script that implements our lead qualification system. The file is more complex than the two functions to allow for observability, troubleshooting, batch processing, etc. Do not hesitate to reach out if you have any questions.

```python [expandable] theme={null}
import os
import json
import time
import re
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

# API keys from environment variables
ATTIO_API_KEY = os.getenv('ATTIO_API_KEY')
LINKUP_API_KEY = os.getenv('LINKUP_API_KEY')

if not ATTIO_API_KEY or not LINKUP_API_KEY:
    print("Error: Missing API keys in .env file")
    exit(1)

# File paths and settings
FILE = 'new_companies.json'
MAX_COMPANIES = 50

def load_existing_data():
    """Load file with new companies to enrich"""
    try:
        with open(FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Error: Could not load {FILE}")
        exit(1)

def find_website_url(company_name, company_domain=None):
    if not company_name or not company_name.strip():
        return ""

    url = "https://api.linkup.so/v1/search"
    headers = {
        "Authorization": f"Bearer {LINKUP_API_KEY}",
        "Content-Type": "application/json"
    }

    domain_info = company_domain if company_domain else ""
    payload = {
        "q": f"Based on the name {company_name} and the email domain {domain_info}, find the most likely company website URL. Only return a result if you are 90% sure this is the correct website. If {company_name} seems like a generic company name (e.g. personal, perso, n/a), return nothing. If the domain is a generic domain (e.g. gmail.com, yahoo.com, hotmail.com, icloud.com), do not consider it. Only consider professional email domains. Only return the company domain URL.",
        "depth": "standard",
        "outputType": "sourcedAnswer",
        "includeImages": "false"
    }

    print(f"Sending API request to Linkup for: {company_name}")
    try:
        response = requests.post(url, headers=headers, json=payload)
        print(f"API response status: {response.status_code}")
        response.raise_for_status()

        result = response.json()
        if 'answer' in result:
            url_text = result['answer']
            url_pattern = re.compile(r'https?://\S+')
            url_match = url_pattern.search(url_text)

            if url_match:
                website_url = url_match.group(0)
                return re.sub(r'[.,;:"\')]\s*$', '', website_url)
        return ""

    except Exception as e:
        print(f"Error in API call: {e}")
        return ""

def analyze_icp_fit(company_name, website_url):
    if not website_url:
        return "1"

    url = "https://api.linkup.so/v1/search"
    headers = {
        "Authorization": f"Bearer {LINKUP_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "q": f"Analyze the website {website_url}. Determine if this company could be an Ideal Customer Profile (ICP) for my company https://www.linkup.so/. For context, we are selling a search API. We target AI companies, Tech Companies, and corporates, as well as consulting and financial firms. Our search API allows companies to enrich applications with real-time web knowledge and business intelligence, at scale. Consider factors like industry and whether they're likely to need API services, and if they might be building software products. Return a rating from 1 to 5, 1 being lowest ICP, 5 being highest ICP. Universities and schools should get a 3.  Only return the rating, nothing else.",
        "depth": "deep",
        "outputType": "sourcedAnswer",
        "includeImages": "false"
    }

    print(f"Sending ICP analysis request to Linkup for: {company_name}")
    try:
        response = requests.post(url, headers=headers, json=payload)
        print(f"ICP API response status: {response.status_code}")
        response.raise_for_status()

        result = response.json()
        if 'answer' in result:
            return result['answer']
        return "1"

    except Exception as e:
        print(f"Error in ICP API call: {e}")
        return "1"

def save_results(results):
    print(f"\nSaving results to {FILE}...")
    try:
        # First try to save to a temporary file
        temp_file = f"{FILE}.tmp"
        with open(temp_file, 'w') as f:
            json.dump(results, f, indent=2)

        # If successful, rename the temp file to the actual file
        if os.path.exists(FILE):
            os.replace(temp_file, FILE)
        else:
            os.rename(temp_file, FILE)

        print(f"Successfully saved {len(results)} results")

        # Verify the save
        with open(FILE, 'r') as f:
            saved_data = json.load(f)
            print(f"Verified save: {len(saved_data)} results in file")

    except Exception as e:
        print(f"Error saving results: {e}")
        # Try to clean up temp file if it exists
        if os.path.exists(temp_file):
            try:
                os.remove(temp_file)
            except:
                pass

def main():
    results = load_existing_data()
    print(f"\nLoaded {len(results)} existing results")

    # Find organizations to process
    to_process = {record_id: (results[record_id]["name"], results[record_id].get("domain"))
                  for record_id in results
                  if not results[record_id].get("website") and
                     results[record_id].get("name") and
                     (not results[record_id].get("icp_analysis") or results[record_id].get("icp_analysis") == "")}

    companies_to_process = dict(list(to_process.items())[:MAX_COMPANIES])

    print(f"\nFound {len(to_process)} organizations to process")
    print(f"Will process {len(companies_to_process)} organizations...")

    processed_count = 0
    websites_found = 0

    for record_id, (org_name, org_domain) in companies_to_process.items():
        print(f"\nProcessing: {org_name}")

        company_result = results[record_id]
        website_url = find_website_url(org_name, org_domain)

        if website_url:
            company_result["website"] = website_url
            websites_found += 1
            print(f"Found: {website_url}")

            time.sleep(2)
            icp_analysis = analyze_icp_fit(org_name, website_url)
            company_result["icp_analysis"] = icp_analysis
            print(f"Updated {org_name} with website: {website_url} and ICP: {icp_analysis}")
        else:
            # Set default ICP analysis to "1" when no website is found
            company_result["icp_analysis"] = "1"
            print(f"Updated {org_name} with default ICP: 1")

        results[record_id] = company_result
        processed_count += 1

        # Save after each company
        save_results(results)
        print(f"Saved results after processing {org_name}")

        if processed_count < len(companies_to_process):
            time.sleep(3)

    websites_with_analysis = sum(1 for r in results.values() if r.get("website") and r.get("icp_analysis"))

    print(f"\nFinal Results:")
    print(f"Processed {processed_count} organizations")
    print(f"Found {websites_found} websites")
    print(f"Total organizations with websites: {sum(1 for r in results.values() if r.get('website'))}")
    print(f"Total organizations with analysis: {websites_with_analysis}")

    # Final save with verification
    save_results(results)

if __name__ == "__main__":
    main()
```

# Try It Yourself

<AccordionGroup>
  <Accordion title="Customize Your ICP Definition">
    Try modifying the ICP analysis prompt to match your specific business needs:

    1. Update the description of your company
    2. List your target industries
    3. Define what makes an ideal customer for you
    4. Run the script and see how the results change
  </Accordion>

  <Accordion title="Add Company Size Estimation">
    Extend the script to also estimate company size:

    1. Create a new function similar to `analyze_icp_fit`
    2. Craft a prompt asking Linkup to estimate employee count
    3. Add this data to your results structure
    4. Use it as an additional factor in prioritization
  </Accordion>
</AccordionGroup>

# Conclusion

You've now built an automated system that transforms basic CRM information into actionable intelligence. By leveraging the Linkup API, you can:

1. **Save Time**: Eliminate manual research
2. **Improve Targeting**: Focus on the most promising leads
3. **Scale Your Process**: Handle hundreds of leads with ease

This approach combines the best of both worlds: AI-powered analysis with your business expertise to define what makes an ideal customer.

For more sophisticated implementations, check out our other tutorials or reach out to our support team!

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).