# Source: https://docs.perplexity.ai/cookbook/showcase/briefo

# 
[​](https://docs.perplexity.ai/cookbook/showcase/briefo#briefo-%7C-perplexity-powered-news-%26-finance-social-app)
Briefo | Perplexity Powered News & Finance Social App
**Briefo** delivers a personalized, AI generated newsfeed and company deep dives. Readers can follow breaking stories, request on demand financial analyses, and discuss insights with friends, all in one mobile experience powered by Perplexity’s Sonar API.
## 
[​](https://docs.perplexity.ai/cookbook/showcase/briefo#features)
Features
  * Personalized newsfeed across 17 categories with AI summaries and source links
  * Private and public threads for article discussion and sharing
  * Watch list with real time market snapshots and optional AI analyses
  * Deep research reports generated on 12 selectable criteria such as management, competitors, and valuation
  * General purpose chat assistant that remembers each user’s preferred topics


## 
[​](https://docs.perplexity.ai/cookbook/showcase/briefo#prerequisites)
Prerequisites
  * Node 18 LTS or newer
  * npm, Yarn, or pnpm
  * Expo CLI (`npm i -g expo-cli`)
  * Supabase CLI 1.0 or newer for local emulation and Edge Function deploys


## 
[​](https://docs.perplexity.ai/cookbook/showcase/briefo#installation)
Installation
Copy
Ask AI
```
git clone https://github.com/adamblackman/briefo-public.git
cd briefo-public
npm install

```

### 
[​](https://docs.perplexity.ai/cookbook/showcase/briefo#environment-variables)
Environment variables
Copy
Ask AI
```
# .env              (project root)
MY_SUPABASE_URL=https://<project>.supabase.co
MY_SUPABASE_SERVICE_ROLE_KEY=...
PERPLEXITY_API_KEY=...
LINKPREVIEW_API_KEY=...
ALPACA_API_KEY=...
ALPACA_SECRET_KEY=...
# .env.local        (inside supabase/)
# duplicate or override any secrets needed by Edge Functions

```

## 
[​](https://docs.perplexity.ai/cookbook/showcase/briefo#usage)
Usage
Run the Expo development server:
Copy
Ask AI
```
npx expo start

```

Deploy Edge Functions when you are ready:
Copy
Ask AI
```
supabase functions deploy perplexity-news perplexity-chat perplexity-research portfolio-tab-data

```

## 
[​](https://docs.perplexity.ai/cookbook/showcase/briefo#code-explanation)
Code Explanation
  * Frontend: React Native with Expo Router (TypeScript) targeting iOS, Android, and Web
  * Backend: Supabase (PostgreSQL, Row Level Security, Realtime) for data and authentication
  * Edge Functions: TypeScript on Deno calling Perplexity, Alpaca, Alpha Vantage, and LinkPreview APIs
  * Hooks: Reusable React Query style data hooks live in lib/ and hooks/
  * Testing and Linting: ESLint, Prettier, and Expo Lint maintain code quality


## 
[​](https://docs.perplexity.ai/cookbook/showcase/briefo#links)
Links
[GitHub Repository](https://github.com/adamblackman/briefo-public) [Live Demo](https://www.briefo.fun/)
