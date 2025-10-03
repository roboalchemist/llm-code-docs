# Source: https://docs.perplexity.ai/cookbook/examples/README

# 
[​](https://docs.perplexity.ai/cookbook/examples/README#examples-overview)
Examples Overview
Welcome to the **Perplexity Sonar API Examples** collection! These are production-ready applications that demonstrate real-world use cases of the Sonar API.
## 
[​](https://docs.perplexity.ai/cookbook/examples/README#%F0%9F%9A%80-quick-start)
🚀 Quick Start
Navigate to any example directory and follow the instructions in the README.md file.
## 
[​](https://docs.perplexity.ai/cookbook/examples/README#%F0%9F%93%8B-available-examples)
📋 Available Examples
### 
[​](https://docs.perplexity.ai/cookbook/examples/README#%F0%9F%94%8D-fact-checker-cli)
🔍 [Fact Checker CLI](https://docs.perplexity.ai/cookbook/examples/fact-checker-cli/)
**Purpose** : Verify claims and articles for factual accuracy  
**Type** : Command-line tool  
**Use Cases** : Journalism, research, content verification **Key Features** :
  * Structured claim analysis with ratings
  * Source citation and evidence tracking
  * JSON output for automation
  * Professional fact-checking workflow

**Quick Start** :
Copy
Ask AI
```
cd fact-checker-cli/
python fact_checker.py --text "The Earth is flat"

```

* * *
### 
[​](https://docs.perplexity.ai/cookbook/examples/README#%F0%9F%A4%96-daily-knowledge-bot)
🤖 [Daily Knowledge Bot](https://docs.perplexity.ai/cookbook/examples/daily-knowledge-bot/)
**Purpose** : Automated daily fact delivery system  
**Type** : Scheduled Python application  
**Use Cases** : Education, newsletters, personal learning **Key Features** :
  * Topic rotation based on calendar
  * Persistent storage of facts
  * Configurable scheduling
  * Educational content generation

**Quick Start** :
Copy
Ask AI
```
cd daily-knowledge-bot/
python daily_knowledge_bot.py

```

* * *
### 
[​](https://docs.perplexity.ai/cookbook/examples/README#%F0%9F%8F%A5-disease-information-app)
🏥 [Disease Information App](https://docs.perplexity.ai/cookbook/examples/disease-qa/)
**Purpose** : Interactive medical information lookup  
**Type** : Web application (HTML/JavaScript)  
**Use Cases** : Health education, medical reference, patient information **Key Features** :
  * Interactive browser interface
  * Structured medical knowledge cards
  * Citation tracking for medical sources
  * Standalone deployment ready

**Quick Start** :
Copy
Ask AI
```
cd disease-qa/
jupyter notebook disease_qa_tutorial.ipynb

```

* * *
### 
[​](https://docs.perplexity.ai/cookbook/examples/README#%F0%9F%93%8A-financial-news-tracker)
📊 [Financial News Tracker](https://docs.perplexity.ai/cookbook/examples/financial-news-tracker/)
**Purpose** : Real-time financial news monitoring and market analysis  
**Type** : Command-line tool  
**Use Cases** : Investment research, market monitoring, financial journalism **Key Features** :
  * Real-time financial news aggregation
  * Market sentiment analysis (Bullish/Bearish/Neutral)
  * Impact assessment and sector analysis
  * Investment insights and recommendations

**Quick Start** :
Copy
Ask AI
```
cd financial-news-tracker/
python financial_news_tracker.py "tech stocks"

```

* * *
### 
[​](https://docs.perplexity.ai/cookbook/examples/README#%F0%9F%93%9A-academic-research-finder)
📚 [Academic Research Finder](https://docs.perplexity.ai/cookbook/examples/research-finder/)
**Purpose** : Academic literature discovery and summarization  
**Type** : Command-line research tool  
**Use Cases** : Academic research, literature reviews, scholarly work **Key Features** :
  * Academic source prioritization
  * Paper citation extraction with DOI links
  * Research-focused prompting
  * Scholarly workflow integration

**Quick Start** :
Copy
Ask AI
```
cd research-finder/
python research_finder.py "quantum computing advances"

```

## 
[​](https://docs.perplexity.ai/cookbook/examples/README#%F0%9F%94%91-api-key-setup)
🔑 API Key Setup
All examples require a Perplexity API key. You can set it up in several ways:
### 
[​](https://docs.perplexity.ai/cookbook/examples/README#environment-variable-recommended)
Environment Variable (Recommended)
Copy
Ask AI
```
export PPLX_API_KEY="your-api-key-here"

```

### 
[​](https://docs.perplexity.ai/cookbook/examples/README#env-file)
.env File
Create a `.env` file in the example directory:
Copy
Ask AI
```
PERPLEXITY_API_KEY=your-api-key-here

```

### 
[​](https://docs.perplexity.ai/cookbook/examples/README#command-line-argument)
Command Line Argument
Copy
Ask AI
```
python script.py --api-key your-api-key-here

```

## 
[​](https://docs.perplexity.ai/cookbook/examples/README#%F0%9F%9B%A0%EF%B8%8F-common-requirements)
🛠️ Common Requirements
All examples require:
  * **Python 3.7+**
  * **Perplexity API Key** ([Get one here](https://docs.perplexity.ai/guides/getting-started))
  * **Internet connection** for API calls

Additional requirements vary by example and are listed in each `requirements.txt` file.
## 
[​](https://docs.perplexity.ai/cookbook/examples/README#%F0%9F%8E%AF-choosing-the-right-example)
🎯 Choosing the Right Example
**If you want to…** | **Use this example**  
---|---  
Verify information accuracy | **Fact Checker CLI**  
Learn something new daily | **Daily Knowledge Bot**  
Look up medical information | **Disease Information App**  
Track financial markets | **Financial News Tracker**  
Research academic topics | **Academic Research Finder**  
## 
[​](https://docs.perplexity.ai/cookbook/examples/README#%F0%9F%A4%9D-contributing)
🤝 Contributing
Found a bug or want to improve an example? We welcome contributions!
  1. **Report Issues** : Open an issue describing the problem
  2. **Suggest Features** : Propose new functionality or improvements
  3. **Submit Code** : Fork, implement, and submit a pull request

See our [Contributing Guidelines](https://github.com/ppl-ai/api-cookbook/blob/main/CONTRIBUTING.md) for details.
## 
[​](https://docs.perplexity.ai/cookbook/examples/README#%F0%9F%93%84-license)
📄 License
All examples are licensed under the [MIT License](https://github.com/ppl-ai/api-cookbook/blob/main/LICENSE).
* * *
**Ready to explore?** Pick an example above and start building with Perplexity’s Sonar API! 🚀
