# 0G Testnet (Galileo)

Test your applications on 0G's infrastructure without real costs or risks.

:::tip Testnet Explorer
🔍 **[Explore Testnet Activity](https://explorer.0g.ai/testnet/home)**
:::

## Network Details

| Parameters | Network Details |
|----------------|---|
| **Network Name** | 0G-Galileo-Testnet |
| **Chain ID** | 16602 |
| **Token Symbol** | 0G |
| **Block Explorer** | ```https://chainscan-galileo.0g.ai``` |
| **Faucet** | https://faucet.0g.ai |

#### ✅ 3rd Party RPCs (Recommended for production)
- [QuickNode](https://www.quicknode.com/chains/0g)
- [ThirdWeb](https://thirdweb.com/0g-galileo-testnet-16601)
- [Ankr](https://www.ankr.com/rpc/0g/)
- [dRPC NodeCloud](https://drpc.org/chainlist/0g-galileo-testnet-rpc)

## Getting Started

### Step 1: Add Network to Wallet

export const AddNetworkSection = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  return (
    <>
      
        
          
            Remove any old 0G testnet configurations before adding Galileo. 
             { e.preventDefault(); setIsModalOpen(true); }} style={{marginLeft: '5px'}}>
              Need help?
            
          
        
      

      
        <MetaMaskButton label="Add to MetaMask" />
        <OKXButton label="Add to OKX Wallet" />
      

      <RemoveNewtonModal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} />
    </>
  );
};

<AddNetworkSection />

<style>
  {`
    .wallet-buttons {
      display: flex;
      gap: 16px;
      margin: 16px 0;
    }
    
    @media (max-width: 768px) {
      .wallet-buttons {
        flex-direction: column;
      }
    }
  `}
</style>

### Step 2: Get Test Tokens

Visit the [0G Faucet](https://faucet.0g.ai) to receive free testnet tokens. **Daily Limit**: 0.1 0G per wallet.

### Step 3: Start Building

Choose your integration:
- [Deploy Smart Contracts](/developer-hub/building-on-0g/contracts-on-0g/deploy-contracts)
- [Use Storage SDK](/developer-hub/building-on-0g/storage/sdk)
- [Access Compute Network](/developer-hub/building-on-0g/compute-network/inference)
- [Integrate DA Layer](/developer-hub/building-on-0g/da-integration)

### Contract Addresses

:::caution
Addresses may change during testnet.
:::

**0G Storage**
- Flow: `0x22E03a6A89B950F1c82ec5e74F8eCa321a105296`
- Mine: `0x00A9E9604b0538e06b268Fb297Df333337f9593b`
- Reward: `0xA97B57b4BdFEA2D0a25e535bd849ad4e6C440A69`

**0G DA**
- DAEntrance: `0xE75A073dA5bb7b0eC622170Fd268f35E675a957B`

<!-- **Deployment Block**: `326165` -->

## Developer Tools

### Block Explorers
- **[Chain Explorer](https://chainscan-galileo.0g.ai)**: View transactions, blocks, and smart contracts
- **[Storage Explorer](https://storagescan-galileo.0g.ai)**: Track storage operations and metrics
- **[Validator Dashboard](https://testnet.0g.explorers.guru)**: Monitor network validators

<details>
<summary>Development RPC</summary>

:::warning Development Only
This endpoint is for development purposes and should not be used in production applications.
:::

`https://evmrpc-testnet.0g.ai`

</details>

## Faucet
- Use the [official Faucet](https://faucet.0g.ai) to request tokens. Each user can receive up to 0.1 0G token per day, which is sufficient for most testing needs.

- If you require more than 0.1 0G token per day, please reach out in our vibrant [discord](https://discord.com/invite/0glabs) community to request additional tokens.

---

## 0G Documentation

import Link from '@docusaurus/Link';
import SocialProofSection from '@site/src/components/SocialProofSection';

  
    Build the Future of Decentralized AI
    
      <Link className="button button--primary button--lg hero-primary-btn" to="/developer-hub/getting-started">
        Quick Start
      </Link>
      <Link className="button button--outline button--primary button--lg hero-secondary-btn" to="/concepts/chain">
        Learn Concepts
      </Link>
    
  

  
    
    <Link to="/developer-hub/testnet/testnet-overview" className="resource-card">
      
      
        
          Join Testnet
        
        Connect to Galileo testnet and start building your first dApp on 0G
        
          Connect to Testnet →
        
      
    </Link>

    <Link to="/node-sale/ai-alignment-node-user-guide" className="resource-card">
      
      
        
          AI Alignment Node
        
        Learn more about the AI Alignment Node operation
        
          Learn More →
        
      
    </Link>
    
    <Link to="/developer-hub/building-on-0g/compute-network/inference" className="resource-card">
      
      
        
          Inference
        
        Integrate AI inference into your applications with SDKs
        
          View Docs →
        
      
    </Link>
    
    <Link to="/developer-hub/building-on-0g/storage/sdk" className="resource-card">
      
      
        
          Storage SDK
        
        Store and retrieve massive datasets with Go and TypeScript client libraries
        
          View Docs →
        
      
    </Link>
    
    <Link to="/developer-hub/building-on-0g/compute-network/fine-tuning" className="resource-card">
      
      
        
          Fine-tuning
        
        Customize AI models for your specific use case with our command-line tools
        
          View Docs →
        
      
    </Link>
    
    <Link to="/run-a-node/validator-node" className="resource-card">
      
      
        
          Run a Validator
        
        Secure the network and earn rewards by running a validator node
        
          Setup Guide →
        
      
    </Link>
  

<SocialProofSection />

  
  Ready to Build?
  Join thousands of developers building the future of decentralized AI
  
    <Link className="button button--primary button--lg cta-primary-btn" to="/developer-hub/getting-started">
      View Full Documentation
    </Link>
  

<style>{`
  /* Hide sidebar toggle on mobile for landing page */
  @media screen and (max-width: 996px) {
    .navbar__toggle {
      display: none !important;
      visibility: hidden !important;
    }
  }

  /* Global font family for landing page */
  .landing-page-custom,
  .landing-page-custom * {
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  /* Global button styling for consistency */
  .landing-page-custom .button {
    border-radius: 12px;
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  /* Hide sidebar on landing page */
  .new-landing {
    --doc-sidebar-width: 0 !important;
  }
  
  /* Hide page title */
  .landing-page-custom h1:first-child,
  .landing-page-custom .theme-doc-markdown > h1:first-child,
  .landing-page-custom header h1,
  article > h1:first-child,
  main h1:first-child:not(.hero-title),
  .hide-title-wrapper ~ h1,
  h1:has(+ .hide-title-wrapper),
  .markdown > h1:first-child {
    display: none !important;
  }
  
  /* More aggressive title hiding */
  .landing-page-custom .markdown > *:first-child:is(h1) {
    display: none !important;
  }
  
  /* Hero Section */
  .landing-hero {
    text-align: center;
    padding: 6rem 2rem 4rem;
    margin-left: calc(-50vw + 50%);
    margin-right: calc(-50vw + 50%);
    margin-top: -2rem;
    margin-bottom: 3rem;
    width: 100vw;
    position: relative;
    overflow: hidden;
    background: linear-gradient(180deg, 
      rgba(146, 0, 225, 0.08) 0%, 
      rgba(183, 95, 255, 0.05) 50%, 
      transparent 100%);
  }
  
  .landing-hero::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(ellipse at 20% 50%, rgba(146, 0, 225, 0.25) 0%, transparent 40%),
                radial-gradient(ellipse at 80% 50%, rgba(227, 193, 255, 0.2) 0%, transparent 40%);
    animation: float 20s ease-in-out infinite;
  }
  
  @keyframes float {
    0%, 100% { transform: translate(0, 0) rotate(0deg); }
    33% { transform: translate(30px, -30px) rotate(120deg); }
    66% { transform: translate(-20px, 20px) rotate(240deg); }
  }
  
  .hero-content {
    position: relative;
    z-index: 1;
  }
  
  .hero-title {
    font-size: 4rem;
    font-weight: 400; /* Book weight */
    margin-bottom: 1.5rem;
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
    letter-spacing: -0.02em;
    line-height: 1.1;
  }
  
  /* Light mode hero title */
  [data-theme='light'] .hero-title {
    color: #1A1A1F;
  }
  
  /* Dark mode hero title */
  [data-theme='dark'] .hero-title {
    color: #F5F5F7;
  }
  
  .gradient-text {
    background: linear-gradient(135deg, #9200E1 0%, #B75FFF 50%, #CB8AFF 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .text-purple{
    color: #B75FFF;
  }
  
  .hero-subtitle {
    font-size: 1.25rem;
    color: var(--ifm-color-secondary-darkest);
    max-width: 800px;
    margin: 0 auto 2.5rem;
    line-height: 1.6;
    opacity: 0.9;
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  .hero-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
  }
  
  .hero-primary-btn,
  .hero-secondary-btn,
  .cta-primary-btn,
  .cta-secondary-btn {
    line-height: 1.2;
    display: inline-flex;
    align-items: center;
  }
  
  .hero-primary-btn p,
  .hero-secondary-btn p,
  .cta-primary-btn p,
  .cta-secondary-btn p,
  .button p {
    margin: 0 !important;
  }
  
  /* Primary Button - Black with rounded corners */
  .hero-primary-btn {
    background: #1A1A1F;
    border: none;
    font-weight: 400; /* Book weight */
    padding: 0.875rem 2rem;
    border-radius: 12px;
    transition: all 0.3s ease;
    color: #FFFFFF !important;
    box-shadow: 0 4px 14px rgba(26, 26, 31, 0.25);
  }
  
  .hero-primary-btn:hover {
    background: #2A2A2F;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(26, 26, 31, 0.35);
    text-decoration: none;
    color: #FFFFFF !important;
  }
  
  /* Secondary Button Base - Soft purple/gray with rounded corners */
  .hero-secondary-btn {
    font-weight: 400; /* Book weight */
    padding: 0.875rem 2rem;
    border-radius: 12px;
    transition: all 0.3s ease;
    border: 2px solid transparent;
  }
  
  .hero-secondary-btn:hover {
    transform: translateY(-2px);
    text-decoration: none;
  }
  
  /* Light mode secondary button - Gray */
  [data-theme='light'] .hero-secondary-btn {
    background: #F5F5F7;
    color: #5A5A6E !important;
    border-color: #E8E8F0;
  }
  
  [data-theme='light'] .hero-secondary-btn:hover {
    background: #EAEAEC;
    color: #3A3A4A !important;
    border-color: #D0D0D5;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
  }
  
  /* Dark mode secondary button - Soft purple */
  [data-theme='dark'] .hero-secondary-btn {
    background: rgba(183, 95, 255, 0.12);
    color: #E3C1FF !important;
    border-color: rgba(183, 95, 255, 0.3);
  }
  
  [data-theme='dark'] .hero-secondary-btn:hover {
    background: rgba(183, 95, 255, 0.2);
    color: #FFFFFF !important;
    border-color: rgba(183, 95, 255, 0.5);
    box-shadow: 0 4px 14px rgba(183, 95, 255, 0.25);
  }
  
  /* Container adjustments */
  .landing-page-custom .theme-doc-markdown {
    max-width: 100%;
  }
  
  .landing-page-custom .container {
    max-width: 100%;
    padding: 0;
  }
  
  .landing-page-custom article {
    padding: 0;
  }
  
  /* Developer Section */
  .landing-section {
    margin: 2rem auto 4rem;
    max-width: 1200px;
    padding: 0 2rem;
  }
  
  .section-title {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    font-weight: 400; /* Book weight */
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  .section-subtitle {
    text-align: center;
    color: var(--ifm-color-secondary-darkest);
    margin-bottom: 3rem;
    font-size: 1.1rem;
    opacity: 0.9;
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  .resource-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
    gap: 1.5rem;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .resource-card {
    position: relative;
    border-radius: 16px;
    overflow: hidden;
    transition: transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), 
                box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1);
    text-decoration: none;
    color: inherit;
    display: block;
    will-change: transform;
    transform: translateZ(0); /* Force GPU acceleration */
    backface-visibility: hidden; /* Prevent flickering */
  }
  
  .card-glow {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at 50% 0%, rgba(183, 95, 255, 0.15) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.2s ease;
    pointer-events: none;
    will-change: opacity;
  }
  
  .resource-card:hover .card-glow {
    opacity: 1;
  }
  
  .resource-card:hover {
    transform: translate3d(0, -4px, 0); /* Use 3D transform for GPU */
    text-decoration: none;
  }
  
  .resource-card * {
    text-decoration: none !important;
  }
  
  .card-content {
    position: relative;
    padding: 2rem;
    z-index: 1;
  }
  
  .card-header {
    margin-bottom: 1rem;
  }
  
  .card-header h3 {
    margin: 0;
    font-size: 1.5rem;
    font-weight: 400; /* Book weight */
    color: var(--ifm-heading-color);
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  .resource-card p {
    color: var(--ifm-color-secondary-darkest);
    margin-bottom: 1.5rem;
    line-height: 1.6;
    opacity: 0.9;
    min-height: 3.2em;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  .card-footer {
    margin-top: auto;
  }
  
  .card-link {
    color: #B75FFF;
    font-weight: 600;
    font-size: 0.875rem;
    text-transform: uppercase;
    letter-spacing: 0.75px;
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    transition: gap 0.3s ease;
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  .resource-card:hover .card-link {
    gap: 0.5rem;
  }
  
  /* Social Proof Section */
  .social-proof-section {
    padding: 6rem 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
  }
  
  .social-proof-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, 
      transparent 0%, 
      rgba(183, 95, 255, 0.3) 50%, 
      transparent 100%);
  }
  
  .stats-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 4rem;
    max-width: 800px;
    margin: 0 auto;
  }
  
  .stat-item {
    flex: 1;
    text-align: center;
  }
  
  .stat-number {
    font-size: 3.5rem;
    font-weight: 400; /* Book weight */
    background: linear-gradient(135deg, #9200E1 0%, #B75FFF 50%, #CB8AFF 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.2;
    margin-bottom: 0.5rem;
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  /* Fade in animation for stats */
  @keyframes fadeInUp {
    from {
      opacity: 0;
      transform: translateY(30px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  /* Initial state - hidden */
  .stat-item {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.8s ease-out, transform 0.8s ease-out;
  }
  
  /* Visible state - animated in */
  .stat-item.animate {
    opacity: 1;
    transform: translateY(0);
  }
  
  /* Stagger the animations */
  .stat-item:nth-child(1) {
    transition-delay: 0.2s;
  }
  
  .stat-item:nth-child(3) {
    transition-delay: 0.4s;
  }
  
  .stat-item:nth-child(5) {
    transition-delay: 0.6s;
  }
  
  .stat-label {
    font-size: 1.125rem;
    color: var(--ifm-color-secondary-darkest);
    opacity: 0.8;
    font-weight: 400; /* Book weight */
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  .stat-divider {
    width: 1px;
    height: 60px;
    background: linear-gradient(180deg, 
      transparent 0%, 
      rgba(183, 95, 255, 0.3) 50%, 
      transparent 100%);
  }
  
  /* Light mode adjustments */
  [data-theme='light'] .stat-label {
    color: #5A5A6E;
  }
  
  /* Dark mode adjustments */
  [data-theme='dark'] .stat-label {
    color: #C0B8D0;
  }
  
  /* Responsive stats */
  @media (max-width: 768px) {
    .stats-container {
      flex-direction: column;
      gap: 2rem;
    }
    
    .stat-divider {
      width: 60px;
      height: 1px;
    }
    
    .stat-number {
      font-size: 2.5rem;
    }
  }
  
  /* CTA Section */
  .landing-cta {
    text-align: center;
    padding: 4rem 3rem;
    margin: 6rem auto 2rem;
    max-width: 1200px;
    position: relative;
    border-radius: 16px;
    transition: transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), 
                box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1);
  }
  
  .cta-glow {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at 50% 0%, rgba(183, 95, 255, 0.15) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.2s ease;
    pointer-events: none;
    border-radius: 16px;
  }
  
  .landing-cta:hover .cta-glow {
    opacity: 1;
  }
  
  .landing-cta:hover {
    transform: translate3d(0, -4px, 0);
  }
  
  .landing-cta h2 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    position: relative;
    z-index: 2;
    color: var(--ifm-heading-color);
    font-weight: 400; /* Book weight */
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  .landing-cta > p {
    font-size: 1.25rem;
    margin-bottom: 2rem;
    position: relative;
    z-index: 2;
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  /* CTA text colors for purple background */
  [data-theme='light'] .landing-cta > p,
  [data-theme='dark'] .landing-cta > p {
    color: #4A4A5A;
    opacity: 0.95;
  }
  
  /* CTA heading colors for purple background */
  [data-theme='light'] .landing-cta h2,
  [data-theme='dark'] .landing-cta h2 {
    color: #2A2A3A;
  }
  
  /* Ensure button text is not affected */
  .landing-cta .button p {
    color: inherit !important;
    opacity: 1 !important;
  }
  
  .cta-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
    position: relative;
    z-index: 2;
  }
  
  /* CTA Primary Button - Black with rounded corners */
  .cta-primary-btn {
    background: #1A1A1F;
    border: none;
    font-weight: 400; /* Book weight */
    padding: 0.875rem 2.5rem;
    border-radius: 12px;
    color: #FFFFFF !important;
    transition: all 0.3s ease;
    box-shadow: 0 4px 14px rgba(26, 26, 31, 0.25);
  }
  
  .cta-primary-btn:hover {
    background: #2A2A2F;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(26, 26, 31, 0.35);
    text-decoration: none;
    color: #FFFFFF !important;
  }
  
  /* CTA Secondary Button Base - Matching hero secondary */
  .cta-secondary-btn {
    font-weight: 400; /* Book weight */
    padding: 0.875rem 2.5rem;
    border-radius: 12px;
    transition: all 0.3s ease;
    border: 2px solid transparent;
  }
  
  .cta-secondary-btn:hover {
    transform: translateY(-2px);
    text-decoration: none;
  }
  
  /* CTA Secondary Button - Light Mode (Gray) */
  [data-theme='light'] .cta-secondary-btn {
    background: #F5F5F7;
    color: #5A5A6E !important;
    border-color: #E8E8F0;
  }
  
  [data-theme='light'] .cta-secondary-btn:hover {
    background: #EAEAEC;
    color: #3A3A4A !important;
    border-color: #D0D0D5;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
  }
  
  /* CTA Secondary Button - Dark Mode (Soft purple) */
  [data-theme='dark'] .cta-secondary-btn {
    background: rgba(183, 95, 255, 0.12);
    color: #E3C1FF !important;
    border-color: rgba(183, 95, 255, 0.3);
  }
  
  [data-theme='dark'] .cta-secondary-btn:hover {
    background: rgba(183, 95, 255, 0.2);
    color: #FFFFFF !important;
    border-color: rgba(183, 95, 255, 0.5);
    box-shadow: 0 4px 14px rgba(183, 95, 255, 0.25);
  }
  
  /* Override any inherited styles - Force button colors */
  .landing-page-custom .button {
    --ifm-link-color: currentColor !important;
    --ifm-link-hover-color: currentColor !important;
  }
  
  /* Force primary button colors (black) */
  .hero-primary-btn,
  .hero-primary-btn:visited,
  .hero-primary-btn:active,
  .hero-primary-btn:focus,
  .cta-primary-btn,
  .cta-primary-btn:visited,
  .cta-primary-btn:active,
  .cta-primary-btn:focus {
    color: #FFFFFF !important;
    background:rgb(46, 46, 47) !important;
  }
  
  .hero-primary-btn:hover,
  .cta-primary-btn:hover {
    color: #FFFFFF !important;
    background: #2A2A2F !important;
  }
  
  /* Force secondary button colors */
  [data-theme='light'] .hero-secondary-btn,
  [data-theme='light'] .hero-secondary-btn:visited,
  [data-theme='light'] .hero-secondary-btn:active,
  [data-theme='light'] .hero-secondary-btn:focus,
  [data-theme='light'] .cta-secondary-btn,
  [data-theme='light'] .cta-secondary-btn:visited,
  [data-theme='light'] .cta-secondary-btn:active,
  [data-theme='light'] .cta-secondary-btn:focus {
    color: #5A5A6E !important;
  }
  
  [data-theme='light'] .hero-secondary-btn:hover,
  [data-theme='light'] .cta-secondary-btn:hover {
    color: #3A3A4A !important;
  }
  
  [data-theme='dark'] .hero-secondary-btn,
  [data-theme='dark'] .hero-secondary-btn:visited,
  [data-theme='dark'] .hero-secondary-btn:active,
  [data-theme='dark'] .hero-secondary-btn:focus,
  [data-theme='dark'] .cta-secondary-btn,
  [data-theme='dark'] .cta-secondary-btn:visited,
  [data-theme='dark'] .cta-secondary-btn:active,
  [data-theme='dark'] .cta-secondary-btn:focus {
    color: #E3C1FF !important;
  }
  
  [data-theme='dark'] .hero-secondary-btn:hover,
  [data-theme='dark'] .cta-secondary-btn:hover {
    color: #FFFFFF !important;
  }
  
  /* Light mode card styles - optimized without glassmorphism */
  [data-theme='light'] .resource-card {
    background: #FFFFFF;
    border: 1px solid #E8E8F0;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  }
  
  [data-theme='light'] .resource-card:hover {
    border-color: #B75FFF;
    box-shadow: 0 8px 24px rgba(146, 0, 225, 0.12);
  }
  
  [data-theme='light'] .card-glow {
    display: none; /* Disable glow in light mode for performance */
  }
  
  /* Dark mode - optimized without backdrop-filter */
  [data-theme='dark'] .resource-card {
    background: rgba(30, 30, 35, 0.6);
    border: 1px solid rgba(183, 95, 255, 0.15);
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.3);
    transition: transform 0.15s cubic-bezier(0.4, 0, 0.2, 1),
                box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1),
                background-color 0.15s ease,
                border-color 0.15s ease;
  }
  
  [data-theme='dark'] .resource-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, 
      rgba(183, 95, 255, 0.08) 0%, 
      transparent 60%);
    opacity: 0;
    transition: opacity 0.15s ease;
    pointer-events: none;
  }
  
  [data-theme='dark'] .resource-card:hover {
    background: rgba(40, 40, 45, 0.7);
    border-color: rgba(183, 95, 255, 0.4);
    box-shadow: 0 8px 24px rgba(146, 0, 225, 0.2);
  }
  
  [data-theme='dark'] .resource-card:hover::before {
    opacity: 1;
  }
  
  /* Light mode CTA styling with solid purple background */
  [data-theme='light'] .landing-cta {
    background: #DDC2FB;
    border: 1px solid rgba(183, 95, 255, 0.3);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  }
  

  
  [data-theme='light'] .landing-cta .cta-glow {
    display: none; /* Disable glow in light mode for consistency */
  }
  
  /* Dark mode CTA styling with solid purple background */
  [data-theme='dark'] .landing-cta {
    background: #DDC2FB;
    border: 1px solid rgba(183, 95, 255, 0.3);
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.3);
  }
  
  /* Hover effects for both themes with purple background */
  [data-theme='light'] .landing-cta:hover,
  [data-theme='dark'] .landing-cta:hover {
    background: #D4B8F8; /* Slightly darker purple on hover */
    border-color: rgba(183, 95, 255, 0.5);
    box-shadow: 0 8px 24px rgba(146, 0, 225, 0.15);
  }
  
  /* Responsive design */
  @media (max-width: 996px) {
    .landing-hero {
      padding: 4rem 1.5rem;
      margin: -1.5rem -1.5rem 3rem -1.5rem;
    }
    
    .hero-title {
      font-size: 3rem;
    }
    
    .resource-grid {
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    }
  }
  
  @media (max-width: 768px) {
    .hero-title {
      font-size: 2.5rem;
    }
    
    .hero-subtitle {
      font-size: 1.1rem;
      padding: 0 1rem;
    }
    
    .section-title {
      font-size: 2rem;
      font-weight: 400; /* Book weight */
    }
    
    .resource-grid {
      grid-template-columns: 1fr;
      gap: 1rem;
      padding: 0 1rem;
    }
    
    .card-content {
      padding: 1.5rem;
    }
    
    .landing-cta {
      margin: 4rem 1rem 2rem;
      padding: 3rem 1.5rem;
      border-radius: 16px;
    }
    
    .hero-buttons {
      flex-direction: column;
      align-items: stretch;
      width: 100%;
      max-width: 280px;
      margin: 0 auto;
    }
    
    .hero-buttons .button {
      width: 100%;
      text-align: center;
      justify-content: center;
      min-height: 48px;
      display: flex;
      align-items: center;
    }
  }
  
  /* Monospace for technical elements */
  .resource-card code {
    font-family: 'Geist Mono', 'Consolas', monospace;
  }
`}</style>

---

## How to Get 0G Token


:::info Network Details
- **Token**: Native gas token (EVM-compatible)
- **Chain ID**: 16661
- **Explorer**: [https://chainscan.0g.ai](https://chainscan.0g.ai)
- **Mainnet Launch**: September 2025
:::

## Centralized Exchanges

The most straightforward way to acquire $0G is through centralized exchanges. After purchasing, withdraw directly to the **0G Mainnet** (select "0G Chain" or "0G Mainnet" as the withdrawal network).

### Spot Trading

| Exchange | Trading Pairs |
|----------|---------------|
| **[HTX](https://www.htx.com/trade/0g_usdt)** | 0G/USDT |
| **[Binance](https://www.binance.com/en/trade/0G_USDT)** | 0G/USDT, 0G/USDC, 0G/BNB, 0G/FDUSD, 0G/TRY |
| **[Bybit](https://www.bybit.com/en/trade/spot/0G/USDT)** | 0G/USDT |
| **[MEXC](https://www.mexc.com/exchange/0G_USDT)** | 0G/USDT, 0G/USDC |
| **[KuCoin](https://www.kucoin.com/trade/0G-USDT)** | 0G/USDT |
| **[Gate.io](https://www.gate.io/trade/0G_USDT)** | 0G/USDT |
| **[Bitget](https://www.bitget.com/spot/0GUSDT)** | 0G/USDT |
| **[HashKey Exchange](https://global.hashkey.com/en-US/spot/0G_USDT)** | 0G/USDT |
| **[LBank](https://www.lbank.com/trade/0g_usdt)** | 0G/USDT |
| **[Upbit](https://upbit.com/exchange?code=CRIX.UPBIT.USDT-0G)** | 0G/USDT |
| **[Kraken](https://www.kraken.com/prices/0g)** | 0G/USDT |

## Bridge to 0G Chain

Use **[XSwap](https://xswap.link/)**, the official bridge for the 0G network, powered by [Chainlink CCIP](https://docs.chain.link/ccip/directory/mainnet/chain/0g-mainnet).

### XSwap Bridge

- **URL**: [https://xswap.link/bridge?toChain=16661](https://xswap.link/bridge?toChain=16661)
- **Supported Assets**: USDC and other tokens
- **Networks**: Ethereum ↔ 0G (with more chains coming)
- **Security**: Powered by [Chainlink CCIP](https://docs.chain.link/ccip/directory/mainnet/chain/0g-mainnet) with enterprise-grade security

**How to Bridge:**

1. Visit [xswap.link/bridge?toChain=16661](https://xswap.link/bridge?toChain=16661)
2. Connect your wallet (MetaMask, SafePal, etc.)
3. Select source chain (e.g., Ethereum) and 0G as destination
4. Choose asset to bridge (e.g., USDC)
5. Confirm transaction and wait for bridging to complete
6. Once bridged, swap your assets to $0G on the 0G Hub

## Swap on 0G Chain

Once you have assets on the 0G network, swap them for native $0G tokens.

### 0G Hub (Recommended)

- **URL**: [https://hub.0g.ai/swap](https://hub.0g.ai/swap)
- **Features**: Official swap interface for the 0G ecosystem
- **Powered by**: [Jaine](https://jaine.app/)
- **Available Pairs**: Multiple trading pairs including ETH, USDT, USDC

The 0G Hub provides seamless token swapping, portfolio tracking, and access to the entire 0G ecosystem.

## Wallet Setup

To receive and hold $0G, you need a wallet that supports the 0G network.

### Supported Wallets

- **[MetaMask](https://metamask.io/)** - Add 0G network manually via [Mainnet Overview](/developer-hub/mainnet/mainnet-overview)
- **[SafePal](https://www.safepal.com/)** - Native support for 0G chain
- **[OKX Wallet](https://www.okx.com/web3)** - Native support for 0G network
- **[Rabby](https://rabby.io/)** - Add 0G network manually

### Adding 0G Network

For detailed instructions on adding the 0G network to your wallet, including RPC endpoints and network configuration, visit the [Mainnet Overview](/developer-hub/mainnet/mainnet-overview) page.

---

For more information about the 0G network and its features, see [Understanding 0G](/introduction/understanding-0g).

---

## New Landing

import Link from '@docusaurus/Link';
import SocialProofSection from '@site/src/components/SocialProofSection';

  
    Build the Future of Decentralized AI
    
      <Link className="button button--primary button--lg hero-primary-btn" to="/developer-hub/getting-started">
        Quick Start
      </Link>
      <Link className="button button--outline button--primary button--lg hero-secondary-btn" to="/introduction/understanding-0g">
        Learn Concepts
      </Link>
    
  

  
    
    <Link to="/developer-hub/testnet/testnet-overview" className="resource-card">
      
      
        
          Join Testnet
        
        Connect to Galileo testnet and start building your first dApp on 0G
        
          Connect to Testnet →
        
      
    </Link>

    <Link to="/concepts/chain" className="resource-card">
      
      
        
          New to 0G? Start Here
        
        Learn the basics of 0G's AI infrastructure and get oriented quickly
        
          Get Started →
        
      
    </Link>
    
    <Link to="/developer-hub/building-on-0g/compute-network/inference" className="resource-card">
      
      
        
          Inference
        
        Integrate AI inference into your applications with SDKs
        
          View Docs →
        
      
    </Link>
    
    <Link to="/developer-hub/building-on-0g/storage/sdk" className="resource-card">
      
      
        
          Storage SDK
        
        Store and retrieve massive datasets with Go and TypeScript client libraries
        
          View Docs →
        
      
    </Link>
    
    <Link to="/developer-hub/building-on-0g/compute-network/fine-tuning" className="resource-card">
      
      
        
          Fine-tuning
        
        Customize AI models for your specific use case with our command-line tools
        
          View Docs →
        
      
    </Link>
    
    <Link to="/run-a-node/validator-node" className="resource-card">
      
      
        
          Run a Validator
        
        Secure the network and earn rewards by running a validator node
        
          Setup Guide →
        
      
    </Link>
  

<SocialProofSection />

  
  Ready to Build?
  Join thousands of developers building the future of decentralized AI
  
    <Link className="button button--primary button--lg cta-primary-btn" to="/developer-hub/getting-started">
      View Full Documentation
    </Link>
  

<style>{`
  /* Global font family for landing page */
  .landing-page-custom,
  .landing-page-custom * {
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  /* Global button styling for consistency */
  .landing-page-custom .button {
    border-radius: 12px;
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  /* Hide sidebar on landing page */
  .new-landing {
    --doc-sidebar-width: 0 !important;
  }
  
  /* Hide page title */
  .landing-page-custom h1:first-child,
  .landing-page-custom .theme-doc-markdown > h1:first-child,
  .landing-page-custom header h1,
  article > h1:first-child,
  main h1:first-child:not(.hero-title),
  .hide-title-wrapper ~ h1,
  h1:has(+ .hide-title-wrapper),
  .markdown > h1:first-child {
    display: none !important;
  }
  
  /* More aggressive title hiding */
  .landing-page-custom .markdown > *:first-child:is(h1) {
    display: none !important;
  }
  
  /* Hero Section */
  .landing-hero {
    text-align: center;
    padding: 6rem 2rem 4rem;
    margin-left: calc(-50vw + 50%);
    margin-right: calc(-50vw + 50%);
    margin-top: -2rem;
    margin-bottom: 3rem;
    width: 100vw;
    position: relative;
    overflow: hidden;
    background: linear-gradient(180deg, 
      rgba(146, 0, 225, 0.08) 0%, 
      rgba(183, 95, 255, 0.05) 50%, 
      transparent 100%);
  }
  
  .landing-hero::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(ellipse at 20% 50%, rgba(146, 0, 225, 0.25) 0%, transparent 40%),
                radial-gradient(ellipse at 80% 50%, rgba(227, 193, 255, 0.2) 0%, transparent 40%);
    animation: float 20s ease-in-out infinite;
  }
  
  @keyframes float {
    0%, 100% { transform: translate(0, 0) rotate(0deg); }
    33% { transform: translate(30px, -30px) rotate(120deg); }
    66% { transform: translate(-20px, 20px) rotate(240deg); }
  }
  
  .hero-content {
    position: relative;
    z-index: 1;
  }
  
  .hero-title {
    font-size: 4rem;
    font-weight: 400; /* Book weight */
    margin-bottom: 1.5rem;
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
    letter-spacing: -0.02em;
    line-height: 1.1;
  }
  
  /* Light mode hero title */
  [data-theme='light'] .hero-title {
    color: #1A1A1F;
  }
  
  /* Dark mode hero title */
  [data-theme='dark'] .hero-title {
    color: #F5F5F7;
  }
  
  .gradient-text {
    background: linear-gradient(135deg, #9200E1 0%, #B75FFF 50%, #CB8AFF 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .text-purple{
    color: #B75FFF;
  }
  
  .hero-subtitle {
    font-size: 1.25rem;
    color: var(--ifm-color-secondary-darkest);
    max-width: 800px;
    margin: 0 auto 2.5rem;
    line-height: 1.6;
    opacity: 0.9;
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  .hero-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
  }
  
  .hero-primary-btn,
  .hero-secondary-btn,
  .cta-primary-btn,
  .cta-secondary-btn {
    line-height: 1.2;
    display: inline-flex;
    align-items: center;
  }
  
  .hero-primary-btn p,
  .hero-secondary-btn p,
  .cta-primary-btn p,
  .cta-secondary-btn p,
  .button p {
    margin: 0 !important;
  }
  
  /* Primary Button - Black with rounded corners */
  .hero-primary-btn {
    background: #1A1A1F;
    border: none;
    font-weight: 400; /* Book weight */
    padding: 0.875rem 2rem;
    border-radius: 12px;
    transition: all 0.3s ease;
    color: #FFFFFF !important;
    box-shadow: 0 4px 14px rgba(26, 26, 31, 0.25);
  }
  
  .hero-primary-btn:hover {
    background: #2A2A2F;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(26, 26, 31, 0.35);
    text-decoration: none;
    color: #FFFFFF !important;
  }
  
  /* Secondary Button Base - Soft purple/gray with rounded corners */
  .hero-secondary-btn {
    font-weight: 400; /* Book weight */
    padding: 0.875rem 2rem;
    border-radius: 12px;
    transition: all 0.3s ease;
    border: 2px solid transparent;
  }
  
  .hero-secondary-btn:hover {
    transform: translateY(-2px);
    text-decoration: none;
  }
  
  /* Light mode secondary button - Gray */
  [data-theme='light'] .hero-secondary-btn {
    background: #F5F5F7;
    color: #5A5A6E !important;
    border-color: #E8E8F0;
  }
  
  [data-theme='light'] .hero-secondary-btn:hover {
    background: #EAEAEC;
    color: #3A3A4A !important;
    border-color: #D0D0D5;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
  }
  
  /* Dark mode secondary button - Soft purple */
  [data-theme='dark'] .hero-secondary-btn {
    background: rgba(183, 95, 255, 0.12);
    color: #E3C1FF !important;
    border-color: rgba(183, 95, 255, 0.3);
  }
  
  [data-theme='dark'] .hero-secondary-btn:hover {
    background: rgba(183, 95, 255, 0.2);
    color: #FFFFFF !important;
    border-color: rgba(183, 95, 255, 0.5);
    box-shadow: 0 4px 14px rgba(183, 95, 255, 0.25);
  }
  
  /* Container adjustments */
  .landing-page-custom .theme-doc-markdown {
    max-width: 100%;
  }
  
  .landing-page-custom .container {
    max-width: 100%;
    padding: 0;
  }
  
  .landing-page-custom article {
    padding: 0;
  }
  
  /* Developer Section */
  .landing-section {
    margin: 2rem auto 4rem;
    max-width: 1200px;
    padding: 0 2rem;
  }
  
  .section-title {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    font-weight: 400; /* Book weight */
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  .section-subtitle {
    text-align: center;
    color: var(--ifm-color-secondary-darkest);
    margin-bottom: 3rem;
    font-size: 1.1rem;
    opacity: 0.9;
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  .resource-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
    gap: 1.5rem;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .resource-card {
    position: relative;
    border-radius: 16px;
    overflow: hidden;
    transition: transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), 
                box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1);
    text-decoration: none;
    color: inherit;
    display: block;
    will-change: transform;
    transform: translateZ(0); /* Force GPU acceleration */
    backface-visibility: hidden; /* Prevent flickering */
  }
  
  .card-glow {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at 50% 0%, rgba(183, 95, 255, 0.15) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.2s ease;
    pointer-events: none;
    will-change: opacity;
  }
  
  .resource-card:hover .card-glow {
    opacity: 1;
  }
  
  .resource-card:hover {
    transform: translate3d(0, -4px, 0); /* Use 3D transform for GPU */
    text-decoration: none;
  }
  
  .resource-card * {
    text-decoration: none !important;
  }
  
  .card-content {
    position: relative;
    padding: 2rem;
    z-index: 1;
  }
  
  .card-header {
    margin-bottom: 1rem;
  }
  
  .card-header h3 {
    margin: 0;
    font-size: 1.5rem;
    font-weight: 400; /* Book weight */
    color: var(--ifm-heading-color);
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  .resource-card p {
    color: var(--ifm-color-secondary-darkest);
    margin-bottom: 1.5rem;
    line-height: 1.6;
    opacity: 0.9;
    min-height: 3.2em;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  .card-footer {
    margin-top: auto;
  }
  
  .card-link {
    color: #B75FFF;
    font-weight: 600;
    font-size: 0.875rem;
    text-transform: uppercase;
    letter-spacing: 0.75px;
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    transition: gap 0.3s ease;
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  .resource-card:hover .card-link {
    gap: 0.5rem;
  }
  
  /* Social Proof Section */
  .social-proof-section {
    padding: 6rem 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
  }
  
  .social-proof-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, 
      transparent 0%, 
      rgba(183, 95, 255, 0.3) 50%, 
      transparent 100%);
  }
  
  .stats-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 4rem;
    max-width: 800px;
    margin: 0 auto;
  }
  
  .stat-item {
    flex: 1;
    text-align: center;
  }
  
  .stat-number {
    font-size: 3.5rem;
    font-weight: 400; /* Book weight */
    background: linear-gradient(135deg, #9200E1 0%, #B75FFF 50%, #CB8AFF 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.2;
    margin-bottom: 0.5rem;
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  /* Fade in animation for stats */
  @keyframes fadeInUp {
    from {
      opacity: 0;
      transform: translateY(30px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  /* Initial state - hidden */
  .stat-item {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.8s ease-out, transform 0.8s ease-out;
  }
  
  /* Visible state - animated in */
  .stat-item.animate {
    opacity: 1;
    transform: translateY(0);
  }
  
  /* Stagger the animations */
  .stat-item:nth-child(1) {
    transition-delay: 0.2s;
  }
  
  .stat-item:nth-child(3) {
    transition-delay: 0.4s;
  }
  
  .stat-item:nth-child(5) {
    transition-delay: 0.6s;
  }
  
  .stat-label {
    font-size: 1.125rem;
    color: var(--ifm-color-secondary-darkest);
    opacity: 0.8;
    font-weight: 400; /* Book weight */
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  .stat-divider {
    width: 1px;
    height: 60px;
    background: linear-gradient(180deg, 
      transparent 0%, 
      rgba(183, 95, 255, 0.3) 50%, 
      transparent 100%);
  }
  
  /* Light mode adjustments */
  [data-theme='light'] .stat-label {
    color: #5A5A6E;
  }
  
  /* Dark mode adjustments */
  [data-theme='dark'] .stat-label {
    color: #C0B8D0;
  }
  
  /* Responsive stats */
  @media (max-width: 768px) {
    .stats-container {
      flex-direction: column;
      gap: 2rem;
    }
    
    .stat-divider {
      width: 60px;
      height: 1px;
    }
    
    .stat-number {
      font-size: 2.5rem;
    }
  }
  
  /* CTA Section */
  .landing-cta {
    text-align: center;
    padding: 4rem 3rem;
    margin: 6rem auto 2rem;
    max-width: 1200px;
    position: relative;
    border-radius: 16px;
    transition: transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), 
                box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1);
  }
  
  .cta-glow {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at 50% 0%, rgba(183, 95, 255, 0.15) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.2s ease;
    pointer-events: none;
    border-radius: 16px;
  }
  
  .landing-cta:hover .cta-glow {
    opacity: 1;
  }
  
  .landing-cta:hover {
    transform: translate3d(0, -4px, 0);
  }
  
  .landing-cta h2 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    position: relative;
    z-index: 2;
    color: var(--ifm-heading-color);
    font-weight: 400; /* Book weight */
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  .landing-cta > p {
    font-size: 1.25rem;
    margin-bottom: 2rem;
    position: relative;
    z-index: 2;
    font-family: 'Regola Pro', system-ui, -apple-system, sans-serif;
  }
  
  /* CTA text colors for purple background */
  [data-theme='light'] .landing-cta > p,
  [data-theme='dark'] .landing-cta > p {
    color: #4A4A5A;
    opacity: 0.95;
  }
  
  /* CTA heading colors for purple background */
  [data-theme='light'] .landing-cta h2,
  [data-theme='dark'] .landing-cta h2 {
    color: #2A2A3A;
  }
  
  /* Ensure button text is not affected */
  .landing-cta .button p {
    color: inherit !important;
    opacity: 1 !important;
  }
  
  .cta-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
    position: relative;
    z-index: 2;
  }
  
  /* CTA Primary Button - Black with rounded corners */
  .cta-primary-btn {
    background: #1A1A1F;
    border: none;
    font-weight: 400; /* Book weight */
    padding: 0.875rem 2.5rem;
    border-radius: 12px;
    color: #FFFFFF !important;
    transition: all 0.3s ease;
    box-shadow: 0 4px 14px rgba(26, 26, 31, 0.25);
  }
  
  .cta-primary-btn:hover {
    background: #2A2A2F;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(26, 26, 31, 0.35);
    text-decoration: none;
    color: #FFFFFF !important;
  }
  
  /* CTA Secondary Button Base - Matching hero secondary */
  .cta-secondary-btn {
    font-weight: 400; /* Book weight */
    padding: 0.875rem 2.5rem;
    border-radius: 12px;
    transition: all 0.3s ease;
    border: 2px solid transparent;
  }
  
  .cta-secondary-btn:hover {
    transform: translateY(-2px);
    text-decoration: none;
  }
  
  /* CTA Secondary Button - Light Mode (Gray) */
  [data-theme='light'] .cta-secondary-btn {
    background: #F5F5F7;
    color: #5A5A6E !important;
    border-color: #E8E8F0;
  }
  
  [data-theme='light'] .cta-secondary-btn:hover {
    background: #EAEAEC;
    color: #3A3A4A !important;
    border-color: #D0D0D5;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
  }
  
  /* CTA Secondary Button - Dark Mode (Soft purple) */
  [data-theme='dark'] .cta-secondary-btn {
    background: rgba(183, 95, 255, 0.12);
    color: #E3C1FF !important;
    border-color: rgba(183, 95, 255, 0.3);
  }
  
  [data-theme='dark'] .cta-secondary-btn:hover {
    background: rgba(183, 95, 255, 0.2);
    color: #FFFFFF !important;
    border-color: rgba(183, 95, 255, 0.5);
    box-shadow: 0 4px 14px rgba(183, 95, 255, 0.25);
  }
  
  /* Override any inherited styles - Force button colors */
  .landing-page-custom .button {
    --ifm-link-color: currentColor !important;
    --ifm-link-hover-color: currentColor !important;
  }
  
  /* Force primary button colors (black) */
  .hero-primary-btn,
  .hero-primary-btn:visited,
  .hero-primary-btn:active,
  .hero-primary-btn:focus,
  .cta-primary-btn,
  .cta-primary-btn:visited,
  .cta-primary-btn:active,
  .cta-primary-btn:focus {
    color: #FFFFFF !important;
    background:rgb(46, 46, 47) !important;
  }
  
  .hero-primary-btn:hover,
  .cta-primary-btn:hover {
    color: #FFFFFF !important;
    background: #2A2A2F !important;
  }
  
  /* Force secondary button colors */
  [data-theme='light'] .hero-secondary-btn,
  [data-theme='light'] .hero-secondary-btn:visited,
  [data-theme='light'] .hero-secondary-btn:active,
  [data-theme='light'] .hero-secondary-btn:focus,
  [data-theme='light'] .cta-secondary-btn,
  [data-theme='light'] .cta-secondary-btn:visited,
  [data-theme='light'] .cta-secondary-btn:active,
  [data-theme='light'] .cta-secondary-btn:focus {
    color: #5A5A6E !important;
  }
  
  [data-theme='light'] .hero-secondary-btn:hover,
  [data-theme='light'] .cta-secondary-btn:hover {
    color: #3A3A4A !important;
  }
  
  [data-theme='dark'] .hero-secondary-btn,
  [data-theme='dark'] .hero-secondary-btn:visited,
  [data-theme='dark'] .hero-secondary-btn:active,
  [data-theme='dark'] .hero-secondary-btn:focus,
  [data-theme='dark'] .cta-secondary-btn,
  [data-theme='dark'] .cta-secondary-btn:visited,
  [data-theme='dark'] .cta-secondary-btn:active,
  [data-theme='dark'] .cta-secondary-btn:focus {
    color: #E3C1FF !important;
  }
  
  [data-theme='dark'] .hero-secondary-btn:hover,
  [data-theme='dark'] .cta-secondary-btn:hover {
    color: #FFFFFF !important;
  }
  
  /* Light mode card styles - optimized without glassmorphism */
  [data-theme='light'] .resource-card {
    background: #FFFFFF;
    border: 1px solid #E8E8F0;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  }
  
  [data-theme='light'] .resource-card:hover {
    border-color: #B75FFF;
    box-shadow: 0 8px 24px rgba(146, 0, 225, 0.12);
  }
  
  [data-theme='light'] .card-glow {
    display: none; /* Disable glow in light mode for performance */
  }
  
  /* Dark mode - optimized without backdrop-filter */
  [data-theme='dark'] .resource-card {
    background: rgba(30, 30, 35, 0.6);
    border: 1px solid rgba(183, 95, 255, 0.15);
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.3);
    transition: transform 0.15s cubic-bezier(0.4, 0, 0.2, 1),
                box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1),
                background-color 0.15s ease,
                border-color 0.15s ease;
  }
  
  [data-theme='dark'] .resource-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, 
      rgba(183, 95, 255, 0.08) 0%, 
      transparent 60%);
    opacity: 0;
    transition: opacity 0.15s ease;
    pointer-events: none;
  }
  
  [data-theme='dark'] .resource-card:hover {
    background: rgba(40, 40, 45, 0.7);
    border-color: rgba(183, 95, 255, 0.4);
    box-shadow: 0 8px 24px rgba(146, 0, 225, 0.2);
  }
  
  [data-theme='dark'] .resource-card:hover::before {
    opacity: 1;
  }
  
  /* Light mode CTA styling with solid purple background */
  [data-theme='light'] .landing-cta {
    background: #DDC2FB;
    border: 1px solid rgba(183, 95, 255, 0.3);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  }
  

  
  [data-theme='light'] .landing-cta .cta-glow {
    display: none; /* Disable glow in light mode for consistency */
  }
  
  /* Dark mode CTA styling with solid purple background */
  [data-theme='dark'] .landing-cta {
    background: #DDC2FB;
    border: 1px solid rgba(183, 95, 255, 0.3);
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.3);
  }
  
  /* Hover effects for both themes with purple background */
  [data-theme='light'] .landing-cta:hover,
  [data-theme='dark'] .landing-cta:hover {
    background: #D4B8F8; /* Slightly darker purple on hover */
    border-color: rgba(183, 95, 255, 0.5);
    box-shadow: 0 8px 24px rgba(146, 0, 225, 0.15);
  }
  
  /* Responsive design */
  @media (max-width: 996px) {
    .landing-hero {
      padding: 4rem 1.5rem;
      margin: -1.5rem -1.5rem 3rem -1.5rem;
    }
    
    .hero-title {
      font-size: 3rem;
    }
    
    .resource-grid {
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    }
  }
  
  @media (max-width: 768px) {
    .hero-title {
      font-size: 2.5rem;
    }
    
    .hero-subtitle {
      font-size: 1.1rem;
      padding: 0 1rem;
    }
    
    .section-title {
      font-size: 2rem;
      font-weight: 400; /* Book weight */
    }
    
    .resource-grid {
      grid-template-columns: 1fr;
      gap: 1rem;
      padding: 0 1rem;
    }
    
    .card-content {
      padding: 1.5rem;
    }
    
    .landing-cta {
      margin: 4rem 1rem 2rem;
      padding: 3rem 1.5rem;
      border-radius: 16px;
    }
    
    .hero-buttons {
      flex-direction: column;
      align-items: stretch;
      width: 100%;
      max-width: 280px;
      margin: 0 auto;
    }
    
    .hero-buttons .button {
      width: 100%;
      text-align: center;
      justify-content: center;
      min-height: 48px;
      display: flex;
      align-items: center;
    }
  }
  
  /* Monospace for technical elements */
  .resource-card code {
    font-family: 'Geist Mono', 'Consolas', monospace;
  }
`}</style>

---

## Understanding 0G


import LottieAnimation from '@site/src/components/lottieAnimation';

## Why 0G Exists

AI (Artificial Intelligence) is rapidly advancing, but its powerful capabilities are largely confined to centralized systems & limited to a few large companies. Bringing AI onto the blockchain unlocks transformative potential: truly verifiable AI, user-owned data powering AI applications, and open, censorship-resistant AI development.

However, a fundamental challenge has held back this vision:
- **AI's Data Hunger:** AI models and datasets are massive. Existing blockchains make storing and accessing this data impossibly expensive and slow.
- **Intense Compute Demands:** AI requires significant processing power, far beyond what traditional blockchains can offer efficiently.
- **Need for Speed:** Real-time AI applications demand high throughput and low latency

Without overcoming these hurdles, the dream of decentralized AI remains out of reach.

**0G is built to break these barriers.** We provide the foundational infrastructure like high-performance storage, scalable compute, and a fast, modular blockchain—designed from the ground up to power the future of on-chain AI.

## What is 0G?

0G (Zero Gravity) is the first decentralized AI L1 chain that orchestrates hardware resources (storage, compute) and software assets (data, models) to handle AI workloads at scale. It bridges the gap between Web2 AI capabilities and Web3 decentralization.

:::info 0G is building the global foundation for a better, fairer, and more open AI ecosystem, where power is distributed and innovation thrives
:::

**How it works**: 0G provides four independent services that solve different pieces of the AI + blockchain puzzle:
- **Storage** → Where to keep massive AI datasets
- **Compute** → How to run AI models economically  
- **Chain** → Where to execute AI transactions quickly
- **Data Availability** → How to ensure data is always accessible

  

## Modular Architecture

:::tip Key Benefit of Modular Architecture: You DON'T need to use all of 0G!
**Pick only what you need:**
- **Already on Ethereum, Polygon, or any EVM chain?** Use 0G Storage and Compute directly from your existing smart contracts, no need to migrate.
- **Building on Solana or other non-EVM chains?** Our SDKs support cross-chain integration
- **Just need one service?** Use only 0G Storage or only 0G Compute
:::

## The 4 Components of 0G

| Component             | Works Independently?                                   | Key Features & Use Cases                                                          | Cost Highlight                        |
|-----------------------|--------------------------------------------------------|-----------------------------------------------------------------------------------|---------------------------------------|
| **0G Chain**        | ✅ Yes (Optional for other services)             | Fastest modular EVM L1 for AI agents, DeFi with AI logic        | Low gas fees in 0G token              |
| **0G Storage**     | ✅ Yes (Any app/chain can access)                       | Store AI models (GBs-TBs), training datasets, user files, game assets            | 10-100x cheaper than alternatives     |
| **0G Compute**     | ✅ Yes (Any app/chain can access)                     | Run AI inference, model training, verifiable compute, ML pipelines               | Pay-only-for-what-you-use             |
| **0G DA**          | ✅ Yes (Works with any rollup/L1/L2)                  | Power gaming chains, AI rollups, high-frequency trading chains                   | Economical for high-volume DA         |

*\*0G Storage can be used completely standalone without any blockchain integration - perfect for traditional apps needing decentralized storage.*

## Key Concepts Explained Simply

<details>
<summary>**What is decentralized storage?**</summary>

Instead of storing your files on one company's computer (like Google Drive), they're split and stored across hundreds of computers worldwide.

**Why it matters**: If Google's servers crash, you lose access. With decentralized storage, even if 50 computers fail, your data is still safe and accessible.
</details>

<details>
<summary>**What is data availability?**</summary>

It's a guarantee that your data can always be accessed when needed, like having multiple backup generators for your house.

**Why it matters**: In blockchain, if data isn't available, the whole system can freeze. 0G ensures this never happens.
</details>

<details>
<summary>**What is an AI compute network?**</summary>

It's like Uber for computing power - connect to available GPUs when you need to run AI models, pay only for what you use.

**Why it matters**: Instead of buying expensive GPUs or relying on big tech companies, access computing power on-demand from a global network.
</details>

<details>
<summary>**What is a modular blockchain?**</summary>

Like LEGO blocks, each part of the blockchain (storing data, processing transactions, reaching agreement) is separate and can be upgraded independently.

**Why it matters**: Traditional blockchains are like old phones where you can't upgrade just the camera. Modular blockchains let you improve each part without rebuilding everything.
</details>

## Why "Zero Gravity"?

"0G" represents "Zero Gravity" - the state where everything flows effortlessly. Just as astronauts move freely in zero gravity, data and AI computations flow seamlessly through our network without the heavy "gravity" of:
- High costs
- Slow speeds  
- Technical barriers
- Platform lock-in

## What Can You Build?

With 0G's technology, previously impossible use cases are now within reach:

- **On-chain AI agents** that learn and evolve
- **Decentralized ChatGPT** alternatives
- **AI-powered DeFi** trading systems
- **Medical AI** with patient-owned data
- **Large-scale ML training** without AWS bills

And this is just the beginning.

## Where to Go Next

Now that you understand what 0G is and why it exists, here's how to dive deeper:

**For Learners** → Read more about [Concepts](/concepts/chain) to understand how each component works  
**For Builders** → Jump into the [Developer Hub](/developer-hub/getting-started) to start building  
**For Operators** → Learn how to [Run a Node](/run-a-node/overview) and earn rewards

## Join the 0G Community

- [Discord](https://discord.gg/0gLabs) - Get help and chat with builders
- [X(Twitter)](https://x.com/0g_Labs) - Latest updates and announcements
- [GitHub](https://github.com/0gfoundation/0g-doc) - Contribute to the project

We're excited to have you on board as we build the future of Web3 × AI together!

<LottieAnimation />

---

## Vision & Mission


## Our Mission: Make AI a Public Good

At 0G, our mission is clear: **To Make AI a Public Good**.

We believe that AI technology should be accessible, transparent, and beneficial to everyone, not just a select few. By building a decentralized AI operating system, we're creating the infrastructure that will enable this vision.

## Our Vision

We envision a world where:

- **AI is democratized**: Anyone can access and contribute to AI development without gatekeepers
- **AI is transparent**: The models, data, and processes are open and verifiable
- **AI is fair**: Resources and benefits are distributed equitably across the network
- **AI is secure**: Decentralization ensures no single point of failure or control

## How We Achieve This

Every component of our ecosystem contributes toward this goal:

1. **Open Infrastructure**: By providing decentralized storage, compute, and data availability, we remove the barriers to AI development
2. **Community Ownership**: Through our node network and governance model, the community owns and operates the infrastructure
3. **Economic Alignment**: Our tokenomics ensure that contributors are fairly rewarded for their participation
4. **Technical Excellence**: We build the fastest, most efficient infrastructure to make decentralized AI competitive with centralized alternatives

## Join Our Mission

We invite you to join us in building the foundation for a decentralized AI future. Whether you're a developer, node operator, or community member, there's a place for you in the 0G ecosystem.

Together, we're not just building technology – we're shaping the future of AI for the benefit of all humanity.

## Join the 0G Community

- [Discord](https://discord.gg/0gLabs)
- [X(Twitter)](https://x.com/0g_Labs)
- [GitHub](https://github.com/0gfoundation/0g-doc)

---

## 0G AI Alignment Node - Guide

---

::::info **Who this is for & what you'll learn**
- Run your own Alignment Node or delegate to a NAAS provider
- Understand system requirements, setup steps, and monitoring
- Learn NAAS models (commission vs prepaid) and how to delegate/undelegate
::::

## Overview

The 0G AI Alignment Node system allows license holders to participate in the network either by running their own nodes or delegating to Node as a Service (NAAS) providers. This guide covers both options to help you choose the best approach for your needs.

## Choose Your Path

### Quick decision summary

| Option | Best for | Setup time | Rewards | Maintenance |
|-------|----------|-----------|---------|-------------|
| **Option 1: [Delegate to NAAS](#option-1-delegating-to-naas-providers)** | Non-technical users | 2-3 Minutes | 100% (prepaid) or minus commission | Provider handles |
| **Option 2: [Run your own](#option-2-running-your-own-node)** | Technical users | 1-2 Hours | 100% | You handle |

---

## Option 1: Delegating to NAAS Providers

### Understanding NAAS Models

NAAS providers offer two delegation models:

#### Commission-Based Model
- **How it works:** NAAS provider takes a percentage of your rewards as commission
- **Payment:** No upfront payment required
- **Status:** Nodes start as "Active" immediately
- **Best for:** Users who prefer sharing rewards over upfront payments

#### Prepaid Model
- **How it works:** Pay a fixed fee upfront for node operation
- **Payment:** One-time or recurring prepaid fee
- **Status:** Nodes start as "Expired" until payment is confirmed
- **Best for:** Users who want predictable costs

### How to Delegate

#### Step 1: Choose a NAAS Provider

1. Access the [0G Claim Portal](https://claim.0gfoundation.ai)
2. Navigate to the NAAS Providers section
3. Review available providers:
   - **Name & Description**: Provider details
   - **Commission Rate**: Percentage for commission-based model
   - **Prepaid Price**: Cost for prepaid nodes
   - **Reputation**: Community ratings and uptime statistics

   ![NAAS Providers](../../static/img/naas.png)

#### Step 2: Complete Provider Onboarding

1. Visit the selected NAAS provider's platform (URL provided in portal)
2. Complete their onboarding process:
   - Create an account
   - Choose delegation model (commission or prepaid)
   - If prepaid, complete payment
3. Receive your **Target NAAS Node Address** from the provider

**Important:** Save this address - you'll need it for delegation.

#### Step 3: Delegate Your Licenses

1. Return to the 0G Portal
2. Login with your wallet containing licenses
3. Navigate to "My Licenses"
4. Select license(s) to delegate
5. Choose "Delegate" action
6. Enter the **Target NAAS Node Address** provided by your NAAS provider
7. Confirm the transaction

![Delegate Licenses](../../static/img/delegate.png)

#### Step 4: Monitor Delegation Status

Your delegation will show different statuses:

| Status | Description |
|--------|------------|
| **Inactive** | License not delegated |
| **Pending** | Delegation submitted, awaiting NAAS approval |
| **Delegated** | Active and earning rewards |
| **Expired** | Prepaid period ended or payment issue |

### Managing Your Delegation

#### Checking Status
1. Access the 0G Portal
2. Navigate to "My Licenses"
3. View delegation status for each license

#### Undelegating
To reclaim your licenses:

1. Select delegated license(s)
2. Choose "Undelegate"
3. Confirm the transaction
4. Licenses immediately return to "Inactive" status

**Note:** Undelegation is immediate and doesn't require NAAS approval.

#### Switching Providers
1. First undelegate from current provider
2. Wait for transaction confirmation
3. Follow delegation steps with new provider

### NAAS Payment Management

#### For Commission-Based:
- Rewards automatically distributed after commission deduction
- No action required from you
- Monitor earnings in the portal

#### For Prepaid:
- Track expiration dates
- Renew before expiration to avoid downtime
- Provider will update status upon payment
- Node shows "Expired" if payment lapses

---

## Option 2: Running Your Own Node

### System Requirements

Before setting up your node, ensure your system meets these minimum specifications:

| Component | Minimum Requirement |
|-----------|-------------------|
| **RAM** | 64 MB |
| **CPU** | 1 x86 Core @ 2.1GHz |
| **Disk Space** | 10 GB |
| **Internet** | 10 Mbps connection |
| **Network** | Port must be externally accessible (configure in firewall) |

### Installation & Setup

#### Step 1: Download the Node Binary

Download the latest 0G alignment node binary from the official repository:

```bash