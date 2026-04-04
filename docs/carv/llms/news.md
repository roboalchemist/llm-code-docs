# Source: https://docs.carv.io/d.a.t.a.-ai-framework/api-documentation/news.md

# News

### GET News

#### Endpoint

GET /ai-agent-backend/news

#### Params

| Name          | Location | Type   | Required | Description          |
| ------------- | -------- | ------ | -------- | -------------------- |
| Authorization | header   | string | yes      | login token in redis |

#### Example Request (HTTP)

```http
curl -X GET "https://interface.carv.io/ai-agent-backend/news" \
      -H "Content-Type: application/json" \
      -H "Authorization: <YOUR_AUTH_TOKEN>"
```

> Response Examples

```json
{
  "code": 0,
  "msg": "Success",
  "data": {
    "infos": [
      {
        "title": "Why is XRP price up today?",
        "url": "https://cointelegraph.com/why-is-xrp-price-up-today",
        "card_text": "XRP price is up 3% on Feb. 11, responding to Ripple’s partnership with Unicâmbio and increasing chances of XRP ETF approval."
      },
      {
        "title": "New Bitcoin miner ‘capitulation’ hints at sub-$100K BTC price bottom",
        "url": "https://cointelegraph.com/new-bitcoin-miner-capitulation-sub-100k-btc-price-bottom",
        "card_text": "Bitcoin miners may be pointing the way to a major long-term BTC price rebound."
      },
      {
        "title": "How a simple browser extension prevented an $80K transfer to a malicious wallet",
        "url": "https://cointelegraph.com/how-a-simple-browser-extension-prevented-an-80k-transfer-to-a-malicious-wallet",
        "card_text": "A last-minute alert stops an $80,000 transfer to a terrorist-linked wallet, underscoring the growing need for onchain security."
      },
      {
        "title": "SEC and Binance seek 60-day pause in crypto case",
        "url": "https://cointelegraph.com/binance-sec-case-halt-60-days-crypto-task-force",
        "card_text": "The SEC and Binance filed a joint motion to pause their legal case for 60 days, citing the newly formed SEC Crypto Task Force’s potential impact on regulations."
      },
      {
        "title": "2024 crypto VC deals fell 46% from Q1 to Q4 as investment volume rebounded",
        "url": "https://cointelegraph.com/crypto-vc-deal-count-dropped-46-percent-2024",
        "card_text": "Crypto VC deals dropped 46% from Q1 to Q4, but investment value rebounded in Q4, signaling a shift toward selective, high-value projects, according to PitchBook."
      },
      {
        "title": "Why is Cardano (ADA) price up today?",
        "url": "https://cointelegraph.com/why-is-cardano-ada-price-up-today",
        "card_text": "ADA price is up 15% on Feb. 11, responding to Grayscale’s application for a spot Cardano ETF in the United States."
      },
      {
        "title": "What is a Phantom wallet? How to set up and use it",
        "url": "https://cointelegraph.com/what-is-a-phantom-wallet-how-to-set-up-and-use-it",
        "card_text": "Learn how to set up and use a Phantom wallet, including downloading the extension, creating an account, securing your keys and more."
      },
      {
        "title": "Crypto advocates call for post-Biden clarity on digital asset regulations",
        "url": "https://cointelegraph.com/us-congress-crypto-regulation-hearing-2025",
        "card_text": "Industry leaders at a US congressional subcommittee hearing are set to call for clear digital asset regulations to maintain global competitiveness and attract crypto firms."
      },
      {
        "title": "BNB Chain memecoin platform Four.Meme hit by $183K exploit",
        "url": "https://cointelegraph.com/bnb-chain-memecoin-fourmeme-hacked-183k",
        "card_text": "The memecoin launch platform has temporarily stopped the creation of new liquidity pools while it addresses the exploit."
      },
      {
        "title": "Solo miner snags Bitcoin block reward worth $300K",
        "url": "https://cointelegraph.com/solo-miner-snags-bitcoin-block-reward-worth-300-k",
        "card_text": "Bitcoin rose back above $98,000 after dipping slightly when US President Donald Trump announced tariffs on aluminum and steel as part of an escalating US trade war."
      },
      {
        "title": "Story Protocol confirms public mainnet to launch on Feb. 13",
        "url": "https://cointelegraph.com/story-protocol-public-mainnet-launches-february-13",
        "card_text": "The Web3 IP protocol aims to provide an open market for programmable intellectual property, enabling creators and rights holders to protect their IP."
      },
      {
        "title": "ETF issuer Osprey wants judge to review its failed suit against Grayscale",
        "url": "https://cointelegraph.com/osprey-wants-judge-review-failed-suit-against-grayscale-bitcoin-etf",
        "card_text": "A Connecticut judge handed a win to Grayscale in Osprey Funds’ unfair trade practice suit but now Osprey is asking for that to be reviewed."
      },
      {
        "title": "Crypto’s onboarding tipping point – can verification keep up?",
        "url": "https://cointelegraph.com/crypto-s-onboarding-tipping-point",
        "card_text": "Crypto’s rapid growth brings new risks. As fraud escalates, can verification technology keep pace? AI, biometrics and regulatory shifts shape the future of secure crypto onboarding."
      },
      {
        "title": "Bitcoin, top altcoins are ripping attention from memecoins: Santiment",
        "url": "https://cointelegraph.com/bitcoin-top-altcoins-regaining-attention-heathier-market-cycle-santiment",
        "card_text": "Santiment’s social tracker shows top layer-1 blockchains are dominating 44% of the discussion on social media, while the top six memecoins are at 4%."
      },
      {
        "title": "Swedish fintech giant Klarna will ‘embrace crypto,’ CEO says",
        "url": "https://cointelegraph.com/swedish-fintech-firm-klarna-embrace-crypto",
        "card_text": "Klarna, a Swedish payments firm with 85 million users, is reportedly eyeing a US initial public offering — and its CEO is looking for ideas on how it can integrate digital assets."
      },
      {
        "title": "North Carolina House speaker files bill for state to invest in Bitcoin ETPs",
        "url": "https://cointelegraph.com/north-carolina-files-bill-allow-state-treasurer-to-invest-bitcoin",
        "card_text": "The bill limits investments to Bitcoin exchange-traded products only but includes various state funds such as pensions and insurance."
      },
      {
        "title": "Crypto broker breaks ankles while fleeing kidnappers in Spain",
        "url": "https://cointelegraph.com/crypto-broker-escapes-kidnappers-breaks-ankles-while-fleeing-spain-report",
        "card_text": "A search of the apartment in the Spanish town of Estepona where the broker was held by the kidnappers uncovered two firearms, knives, drugs and over $10,000 in cash."
      },
      {
        "title": "Grayscale, NYSE Arca file to launch US-based spot Cardano ETF",
        "url": "https://cointelegraph.com/grayscale-files-cardano-trust-spot-etf",
        "card_text": "NYSE Arca has filed on behalf of Grayscale to launch the firm’s first-ever standalone Cardano ETF product."
      },
      {
        "title": "Litecoin ETF has 90% chance to get SEC approval in 2025: Analysts",
        "url": "https://cointelegraph.com/litecoin-etf-90-percent-chance-sec-approval-2025",
        "card_text": "Bloomberg ETF analysts say Litecoin regulatory filings have been acknowledged and the SEC likely views it as a commodity."
      },
      {
        "title": "OpenAI’s Altman appears to reject Musk’s $97.4B bid for control",
        "url": "https://cointelegraph.com/openai-sam-altman-rejects-elon-musk-takeover-offer",
        "card_text": "OpenAI’s Sam Altman declined Elon Musk’s reported $100 million offer to buy the AI firm, responding with a simple “no thank you” on X."
      },
      {
        "title": "Here’s what happened in crypto today",
        "url": "https://cointelegraph.com/what-happened-in-crypto-today",
        "card_text": "Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, NFTs, Web3 and crypto regulation."
      },
      {
        "title": "Rep. Waters calls for support on bipartisan stablecoin legislation",
        "url": "https://cointelegraph.com/maxine-waters-bipartisan-stablecoin-legislation",
        "card_text": "US House Financial Services Committee ranking member Maxine Waters suggested lawmakers look to bipartisan stablecoin legislation drafted in the 118th session of Congress."
      },
      {
        "title": "Solana revenues outpace Ethereum, L2s despite market dip",
        "url": "https://cointelegraph.com/solana-outpaces-ethereum-l2s-despite-trading-dip",
        "card_text": "Solana-based app revenues beat Ethereum apps by 10x, according to crypto researcher Aylo."
      },
      {
        "title": "Post-election trading surge bullish for Coinbase earnings: Kaiko",
        "url": "https://cointelegraph.com/election-trading-bullish-coinbase-stock-earnings-kaiko",
        "card_text": "Coinbase is among several top US crypto firms scheduled to report earnings this week."
      },
      {
        "title": "Bitcoin price rallies above $97K as institutional and retail traders’ appetites shrink",
        "url": "https://cointelegraph.com/bitcoin-price-rallies-above-97-k-as-institutional-and-retail-traders-appetites-shrink",
        "card_text": "Bitcoin traders are not slamming the buy button, but most of their concerns are connected to macroeconomic conditions."
      },
      {
        "title": "CFTC announces crypto fraud action after enforcement priorities shift",
        "url": "https://cointelegraph.com/cftc-crypto-fraud-enforcement-priorities",
        "card_text": "Acting CFTC Chair Caroline Pham announced on Feb. 4 that the commission would essentially end its practice of regulation by enforcement."
      },
      {
        "title": "Metaplanet share price rises 4,800% as company stacks BTC",
        "url": "https://cointelegraph.com/metaplanet-shares-rise-btc-reserve-strategy",
        "card_text": "Metaplanet shares have risen 4,800% as the company, known as “Asia’s MicroStrategy,” has stacked Bitcoin."
      },
      {
        "title": "US Treasury sued over DOGE access, lawmakers propose stablecoin bill: Law Decoded",
        "url": "https://cointelegraph.com/us-treasury-sued-over-doge-access-lawmakers-propose-stablecoin-bill-law-decoded",
        "card_text": "The United States’ largest union group sued the Treasury Department, accusing it of unlawfully providing sensitive information to Elon Musk’s DOGE."
      },
      {
        "title": "Web3-focused campaign aims to catapult DePIN into mainstream",
        "url": "https://cointelegraph.com/web3-focused-campaign-aims-to-catapult-depin-into-mainstream",
        "card_text": "A token-backed campaign encouraging users to interact with decentralized infrastructure through real-world tasks is accelerating DePIN’s mainstream adoption."
      },
      {
        "title": "Bitcoin's booming 'permanent holder demand' positions BTC price for $116K",
        "url": "https://cointelegraph.com/bitcoin-booming-permanent-holder-demand-btc-price-116k",
        "card_text": "Bitcoin holders with no record of selling their holdings have increased their BTC reserves during the Trump-led market rally."
      },
      {
        "title": "Crypto betting markets’ huge growth fuels calls for billion-dollar volumes in 2025",
        "url": "https://cointelegraph.com/crypto-betting-markets-huge-growth-fuels-calls-for-billion-dollar-volumes-in-2025",
        "card_text": "Crypto-based prediction markets, casinos and sports betting are reshaping the iGaming sector while generating billions of dollars in trading volume."
      },
      {
        "title": "Tesla Q4 Bitcoin profit highlights BTC collateral opportunity — Crypto execs",
        "url": "https://cointelegraph.com/tesla-q4-bitcoin-profit-btc-collateral-opportunity-execs",
        "card_text": "“Mark-to-market gains, Tesla could use its Bitcoin as collateral to unlock liquidity and hedge against market downturns,” said Gadi Chait, an investment manager at Xapo Bank."
      },
      {
        "title": "USDC hits $56.3B market cap, regains losses from bear market",
        "url": "https://cointelegraph.com/usdc-56bn-market-cap-regains-losses-bear-market",
        "card_text": "Circle’s USDC stablecoin has reached a $56.3 billion market capitalization, erasing losses sustained during the bear market."
      },
      {
        "title": "Alleged hacker behind fake SEC post could forfeit $50K in plea deal",
        "url": "https://cointelegraph.com/sec-hacker-fake-bitcoin-etf-post-plea-agreement",
        "card_text": "The individual who allegedly helped compromise the SEC’s X account to post a fake Bitcoin ETF approval message earned roughly $50,000 that he could now be forced to forfeit."
      },
      {
        "title": "Ethereum short positions surge 500% as hedge funds bet on decline",
        "url": "https://cointelegraph.com/ethereum-hedge-funds-short-bets-price-struggles",
        "card_text": "Ethereum may also lack fundamental blockchain activity for an Ether price recovery, analysts told Cointelegraph."
      },
      {
        "title": "ZK identity project Holonym acquires Gitcoin Passport for $10M",
        "url": "https://cointelegraph.com/zk-identity-holonym-acquire-gitcoin-passport-10-million",
        "card_text": "Following the acquisition, Holonym plans to offer its rebranded Human Passport to users worldwide."
      },
      {
        "title": "Web3 growth will be synonymous with Ethereum growth",
        "url": "https://cointelegraph.com/web3-growth-and-ethereum-growth",
        "card_text": "Ethereum is the key to driving Web3 growth, thanks to its robust ecosystem, the rise of layer 2 rollups, and the Superchain’s potential."
      },
      {
        "title": "Bitcoin teases gains as traders say $100K now key support reclaim",
        "url": "https://cointelegraph.com/bitcoin-teases-upside-traders-100k-essential-support-reclaim",
        "card_text": "BTC price momentum is still lacking as the active Bitcoin trading range gets ever narrower."
      },
      {
        "title": "Michael Saylor’s Strategy bags first Bitcoin purchase under new name",
        "url": "https://cointelegraph.com/michael-saylor-s-strategy-makes-first-bitcoin-acquisition-under-new-name",
        "card_text": "Strategy’s fresh 7,633-BTC purchase came days after the firm rebranded from “MicroStrategy” last week."
      },
      {
        "title": "Central African Republic ‘CAR’ memecoin info pages plagued with phishing links",
        "url": "https://cointelegraph.com/car-memecoin-crypto-scam-phishing-links",
        "card_text": "Investors may find themselves clicking on malicious links while researching the controversial Central African Republic memecoin."
      }
    ]
  }
}
```

> 400 Response

```json
{
  "error": "string"
}
```

#### Responses

| HTTP Status Code | Meaning                                                          | Description | Data schema |
| ---------------- | ---------------------------------------------------------------- | ----------- | ----------- |
| 200              | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)          | none        | Inline      |
| 400              | [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1) | none        | Inline      |

#### Responses Data Schema

HTTP Status Code **200**

| Name           | Type      | Required | Restrictions | Title | description |
| -------------- | --------- | -------- | ------------ | ----- | ----------- |
| » code         | integer   | true     | none         |       | none        |
| » msg          | string    | true     | none         |       | none        |
| » data         | object    | true     | none         |       | none        |
| »» infos       | \[object] | true     | none         |       | none        |
| »»» title      | string    | true     | none         |       | none        |
| »»» url        | string    | true     | none         |       | none        |
| »»» card\_text | string    | true     | none         |       | none        |

HTTP Status Code **400**

| Name    | Type   | Required | Restrictions | Title | description |
| ------- | ------ | -------- | ------------ | ----- | ----------- |
| » error | string | true     | none         |       | none        |

## Data Schema
