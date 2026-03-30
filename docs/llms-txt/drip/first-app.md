# Source: https://docs.drip.re/developer/first-app.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Build Your First DRIP App

> Create a Discord Balance Manager to search by Discord ID and manage point balances 💰

Let's build a practical tool! We'll create a Discord Balance Manager that lets you search members by Discord ID and manage their point balances. Perfect first project to get familiar with DRIP. 🚀

## Prerequisites (2 minutes)

<Steps>
  <Step title="Get Your API Key">
    Follow the [quickstart guide](/developer/quickstart) to get your API key and realm ID (found in the dashboard header when your project is selected)
  </Step>

  <Step title="Choose Your Weapon">
    Pick your favorite:

    * **HTML + JavaScript** (runs anywhere, no setup)
    * **Node.js** (if you like npm and stuff)
    * **Python** (if you're into that)
  </Step>
</Steps>

## Discord Balance Manager

Let's build another useful app! This time we'll create a balance management tool that lets you search for users by their Discord ID and manage their point balances.

### What We're Building

A balance management app that:

* 🔍 Search users by Discord ID
* 💰 View current point balances
* ➕ Award or deduct points
* 📝 Add reasons for balance changes
* 🎯 Simple, clean interface

<Info>
  **Perfect for community managers** who need to quickly adjust member balances for events, contests, or corrections!
</Info>

<Warning>
  **🔒 SECURITY WARNING: This example is for learning purposes only!**

  The HTML version below exposes your API key in client-side JavaScript, which is **NOT SAFE for production use**. Anyone can view your API key by inspecting the page source.

  **For production applications:**

* Use server-side code (Node.js, Python, etc.) to keep API keys secure
* Store API keys in environment variables, never in source code
* Implement proper authentication and authorization
* Consider using the [App Client flow](/developer/app-development) for multi-realm applications

  **This tutorial is safe for:**

* Local development and testing
* Learning DRIP API concepts
* Prototyping (with test API keys only)
</Warning>

### HTML + JavaScript Version

<CodeGroup>
  ```html balance-manager.html theme={"dark"}
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>DRIP Balance Manager 💰</title>
      <style>
          * {
              margin: 0;
              padding: 0;
              box-sizing: border-box;
          }

          body {
              font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
              background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
              min-height: 100vh;
              padding: 20px;
          }
          
          .container {
              max-width: 800px;
              margin: 0 auto;
              background: white;
              border-radius: 20px;
              box-shadow: 0 20px 40px rgba(0,0,0,0.1);
              overflow: hidden;
          }
          
          .header {
              background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
              color: white;
              padding: 30px;
              text-align: center;
          }
          
          .header h1 {
              font-size: 2.5em;
              margin-bottom: 10px;
          }
          
          .content {
              padding: 30px;
          }
          
          .search-section {
              background: #f8f9ff;
              padding: 25px;
              border-radius: 15px;
              margin-bottom: 30px;
          }
          
          .form-group {
              margin-bottom: 20px;
          }
          
          .form-group label {
              display: block;
              margin-bottom: 8px;
              font-weight: 600;
              color: #333;
          }
          
          .form-group input, .form-group textarea, .form-group select {
              width: 100%;
              padding: 12px 15px;
              border: 2px solid #e1e5e9;
              border-radius: 10px;
              font-size: 16px;
              transition: border-color 0.3s;
          }
          
          .form-group input:focus, .form-group textarea:focus, .form-group select:focus {
              outline: none;
              border-color: #667eea;
          }
          
          .btn {
              background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
              color: white;
              border: none;
              padding: 12px 25px;
              border-radius: 10px;
              font-size: 16px;
              font-weight: 600;
              cursor: pointer;
              transition: transform 0.2s;
              margin-right: 10px;
              margin-bottom: 10px;
          }
          
          .btn:hover {
              transform: translateY(-2px);
          }
          
          .btn.success {
              background: #28a745;
          }
          
          .btn.danger {
              background: #dc3545;
          }
          
          .user-card {
              background: #f8f9ff;
              padding: 25px;
              border-radius: 15px;
              margin-bottom: 20px;
              border-left: 5px solid #667eea;
          }
          
          .user-info {
              display: flex;
              justify-content: space-between;
              align-items: center;
              margin-bottom: 20px;
          }
          
          .user-details h3 {
              color: #333;
              margin-bottom: 5px;
          }
          
          .user-details p {
              color: #666;
              margin: 2px 0;
          }
          
          .balance-list {
              display: grid;
              grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
              gap: 15px;
              margin-bottom: 20px;
          }
          
          .balance-item {
              background: white;
              padding: 15px;
              border-radius: 10px;
              text-align: center;
              border: 2px solid #e1e5e9;
          }
          
          .balance-amount {
              font-size: 1.5em;
              font-weight: bold;
              color: #667eea;
          }
          
          .balance-name {
              font-size: 0.9em;
              color: #666;
              margin-top: 5px;
          }
          
          .balance-actions {
              display: grid;
              grid-template-columns: 1fr 1fr;
              gap: 15px;
              margin-top: 20px;
          }
          
          .loading {
              text-align: center;
              padding: 40px;
              color: #666;
          }
          
          .error {
              background: #f8d7da;
              color: #721c24;
              padding: 15px;
              border-radius: 10px;
              margin-bottom: 20px;
              border-left: 5px solid #dc3545;
          }
          
          .success {
              background: #d4edda;
              color: #155724;
              padding: 15px;
              border-radius: 10px;
              margin-bottom: 20px;
              border-left: 5px solid #28a745;
          }
          
          .hidden {
              display: none;
          }
          
          @media (max-width: 768px) {
              .user-info {
                  flex-direction: column;
                  align-items: flex-start;
              }
              
              .balance-actions {
                  grid-template-columns: 1fr;
              }
          }
      </style>
  </head>
  <body>
      <div class="container">
          <div class="header">
              <h1>💰 Balance Manager</h1>
              <p>Search and manage member point balances</p>
          </div>

          <div class="content">
              <!-- Search Section -->
              <div class="search-section">
                  <h2>🔍 Find Member by Discord ID</h2>
                  <div class="form-group">
                      <label for="discordId">Discord User ID</label>
                      <input type="text" id="discordId" placeholder="e.g., 123456789012345678">
                      <small style="color: #666; font-size: 0.9em;">Right-click a user in Discord → Copy User ID</small>
                  </div>
                  <button class="btn" onclick="searchUser()">Search Member</button>
              </div>
              
              <!-- Loading State -->
              <div id="loading" class="loading hidden">
                  <h3>🔍 Searching for member...</h3>
              </div>
              
              <!-- Error Message -->
              <div id="error" class="error hidden">
                  <h4>❌ Error</h4>
                  <p id="error-message"></p>
              </div>
              
              <!-- Success Message -->
              <div id="success" class="success hidden">
                  <h4>✅ Success</h4>
                  <p id="success-message"></p>
              </div>
              
              <!-- User Details -->
              <div id="user-section" class="hidden">
                  <div class="user-card">
                      <div class="user-info">
                          <div class="user-details">
                              <h3 id="user-name">Loading...</h3>
                              <p><strong>Discord ID:</strong> <span id="user-discord-id"></span></p>
                              <p><strong>Member Since:</strong> <span id="user-joined"></span></p>
                          </div>
                      </div>
                      
                      <h4>💰 Current Balances</h4>
                      <div id="balance-list" class="balance-list">
                          <!-- Balances will be populated here -->
                      </div>
                      
                      <div class="balance-actions">
                          <div>
                              <h4>➕ Award Points</h4>
                              <div class="form-group">
                                  <select id="award-currency">
                                      <!-- Options populated dynamically -->
                                  </select>
                              </div>
                              <div class="form-group">
                                  <input type="number" id="award-amount" placeholder="Amount to award" min="1">
                              </div>
                              <div class="form-group">
                                  <input type="text" id="award-reason" placeholder="Reason (optional)">
                              </div>
                              <button class="btn success" onclick="awardPoints()">Award Points</button>
                          </div>
                          
                          <div>
                              <h4>➖ Deduct Points</h4>
                              <div class="form-group">
                                  <select id="deduct-currency">
                                      <!-- Options populated dynamically -->
                                  </select>
                              </div>
                              <div class="form-group">
                                  <input type="number" id="deduct-amount" placeholder="Amount to deduct" min="1">
                              </div>
                              <div class="form-group">
                                  <input type="text" id="deduct-reason" placeholder="Reason (optional)">
                              </div>
                              <button class="btn danger" onclick="deductPoints()">Deduct Points</button>
                          </div>
                      </div>
                  </div>
              </div>
          </div>
      </div>

           <script>
           // 🔥 CONFIGURE THESE WITH YOUR ACTUAL VALUES
           // ⚠️  WARNING: Never expose API keys in client-side code in production!
           // This is only safe for local development and learning.
           const DRIP_API_KEY = 'your_client_secret_here';
           const REALM_ID = 'your_realm_id_here';
           const API_BASE = 'https://api.drip.re/api/v1';
          
          let currentUser = null;
          let realmCurrencies = [];

          // Search for user by Discord ID
          async function searchUser() {
              const discordId = document.getElementById('discordId').value.trim();
              
              if (!discordId) {
                  showError('Please enter a Discord ID');
                  return;
              }
              
              showLoading(true);
              hideMessages();
              hideUserSection();
              
              try {
                  // Search for member by Discord ID
                  const response = await fetch(`${API_BASE}/realm/${REALM_ID}/members/search?type=discord&value=${discordId}`, {
                      headers: {
                          'Authorization': `Bearer ${DRIP_API_KEY}`,
                          'Content-Type': 'application/json'
                      }
                  });
                  
                  if (!response.ok) {
                      const error = await response.json();
                      throw new Error(error.message || 'Failed to search for member');
                  }
                  
                  const data = await response.json();
                  
                  if (!data.data || data.data.length === 0) {
                      throw new Error('No member found with that Discord ID');
                  }
                  
                  currentUser = data.data[0];
                  await loadRealmCurrencies();
                  displayUser(currentUser);
                  
              } catch (error) {
                  console.error('Search error:', error);
                  showError(error.message);
              } finally {
                  showLoading(false);
              }
          }
          
          // Load realm currencies for dropdowns
          async function loadRealmCurrencies() {
              try {
                  const response = await fetch(`${API_BASE}/realm/${REALM_ID}/points`, {
                      headers: {
                          'Authorization': `Bearer ${DRIP_API_KEY}`,
                          'Content-Type': 'application/json'
                      }
                  });
                  
                  if (!response.ok) {
                      throw new Error('Failed to load currencies');
                  }
                  
                  const data = await response.json();
                  realmCurrencies = data.data || [];
                  
                  populateCurrencyDropdowns();
                  
              } catch (error) {
                  console.error('Failed to load currencies:', error);
                  // Use fallback if available from user balance
                  if (currentUser && currentUser.pointBalances) {
                      realmCurrencies = currentUser.pointBalances.map(balance => balance.realmPoint);
                      populateCurrencyDropdowns();
                  }
              }
          }
          
          // Populate currency dropdown options
          function populateCurrencyDropdowns() {
              const awardSelect = document.getElementById('award-currency');
              const deductSelect = document.getElementById('deduct-currency');
              
              // Clear existing options
              awardSelect.innerHTML = '';
              deductSelect.innerHTML = '';
              
              // Add currency options
              realmCurrencies.forEach(currency => {
                  const option1 = document.createElement('option');
                  option1.value = currency.id;
                  option1.textContent = `${currency.emoji || '💰'} ${currency.name}`;
                  awardSelect.appendChild(option1);
                  
                  const option2 = document.createElement('option');
                  option2.value = currency.id;
                  option2.textContent = `${currency.emoji || '💰'} ${currency.name}`;
                  deductSelect.appendChild(option2);
              });
          }
          
          // Display user information
          function displayUser(user) {
              document.getElementById('user-name').textContent = user.displayName || user.username || 'Unknown User';
              document.getElementById('user-discord-id').textContent = user.credentials?.find(c => c.type === 'discord')?.platformId || 'N/A';
              document.getElementById('user-joined').textContent = user.joinedAt ? new Date(user.joinedAt).toLocaleDateString() : 'Unknown';
              
              // Display balances
              const balanceList = document.getElementById('balance-list');
              balanceList.innerHTML = '';
              
              if (user.pointBalances && user.pointBalances.length > 0) {
                  user.pointBalances.forEach(balance => {
                      const balanceItem = document.createElement('div');
                      balanceItem.className = 'balance-item';
                      balanceItem.innerHTML = `
                          <div class="balance-amount">${balance.balance.toLocaleString()}</div>
                          <div class="balance-name">${balance.realmPoint.emoji || '💰'} ${balance.realmPoint.name}</div>
                      `;
                      balanceList.appendChild(balanceItem);
                  });
              } else {
                  balanceList.innerHTML = '<div class="balance-item"><div class="balance-amount">0</div><div class="balance-name">No balances found</div></div>';
              }
              
              showUserSection();
          }
          
          // Award points to user
          async function awardPoints() {
              if (!currentUser) return;
              
              const currencyId = document.getElementById('award-currency').value;
              const amount = parseInt(document.getElementById('award-amount').value);
              const reason = document.getElementById('award-reason').value.trim();
              
              if (!currencyId || !amount || amount <= 0) {
                  showError('Please select a currency and enter a valid amount');
                  return;
              }
              
              try {
                  const requestBody = {
                      tokens: amount
                  };
                  
                  if (currencyId) {
                      requestBody.realmPointId = currencyId;
                  }
                  
                  const response = await fetch(`${API_BASE}/realm/${REALM_ID}/members/${currentUser.id}/point-balance`, {
                      method: 'PATCH',
                      headers: {
                          'Authorization': `Bearer ${DRIP_API_KEY}`,
                          'Content-Type': 'application/json'
                      },
                      body: JSON.stringify(requestBody)
                  });
                  
                  if (!response.ok) {
                      const error = await response.json();
                      throw new Error(error.message || 'Failed to award points');
                  }
                  
                  const currency = realmCurrencies.find(c => c.id === currencyId);
                  const currencyName = currency ? `${currency.emoji || '💰'} ${currency.name}` : 'points';
                  
                  showSuccess(`Successfully awarded ${amount} ${currencyName}${reason ? ` for: ${reason}` : ''}!`);
                  
                  // Clear form
                  document.getElementById('award-amount').value = '';
                  document.getElementById('award-reason').value = '';
                  
                  // Refresh user data
                  setTimeout(() => {
                      searchUser();
                  }, 1000);
                  
              } catch (error) {
                  console.error('Award error:', error);
                  showError(error.message);
              }
          }
          
          // Deduct points from user
          async function deductPoints() {
              if (!currentUser) return;
              
              const currencyId = document.getElementById('deduct-currency').value;
              const amount = parseInt(document.getElementById('deduct-amount').value);
              const reason = document.getElementById('deduct-reason').value.trim();
              
              if (!currencyId || !amount || amount <= 0) {
                  showError('Please select a currency and enter a valid amount');
                  return;
              }
              
              try {
                  const requestBody = {
                      tokens: -amount // Negative amount for deduction
                  };
                  
                  if (currencyId) {
                      requestBody.realmPointId = currencyId;
                  }
                  
                  const response = await fetch(`${API_BASE}/realm/${REALM_ID}/members/${currentUser.id}/point-balance`, {
                      method: 'PATCH',
                      headers: {
                          'Authorization': `Bearer ${DRIP_API_KEY}`,
                          'Content-Type': 'application/json'
                      },
                      body: JSON.stringify(requestBody)
                  });
                  
                  if (!response.ok) {
                      const error = await response.json();
                      throw new Error(error.message || 'Failed to deduct points');
                  }
                  
                  const currency = realmCurrencies.find(c => c.id === currencyId);
                  const currencyName = currency ? `${currency.emoji || '💰'} ${currency.name}` : 'points';
                  
                  showSuccess(`Successfully deducted ${amount} ${currencyName}${reason ? ` for: ${reason}` : ''}!`);
                  
                  // Clear form
                  document.getElementById('deduct-amount').value = '';
                  document.getElementById('deduct-reason').value = '';
                  
                  // Refresh user data
                  setTimeout(() => {
                      searchUser();
                  }, 1000);
                  
              } catch (error) {
                  console.error('Deduct error:', error);
                  showError(error.message);
              }
          }
          
          // UI Helper Functions
          function showLoading(show) {
              document.getElementById('loading').classList.toggle('hidden', !show);
          }
          
          function showError(message) {
              document.getElementById('error-message').textContent = message;
              document.getElementById('error').classList.remove('hidden');
              setTimeout(() => {
                  document.getElementById('error').classList.add('hidden');
              }, 5000);
          }
          
          function showSuccess(message) {
              document.getElementById('success-message').textContent = message;
              document.getElementById('success').classList.remove('hidden');
              setTimeout(() => {
                  document.getElementById('success').classList.add('hidden');
              }, 5000);
          }
          
          function hideMessages() {
              document.getElementById('error').classList.add('hidden');
              document.getElementById('success').classList.add('hidden');
          }
          
          function showUserSection() {
              document.getElementById('user-section').classList.remove('hidden');
          }
          
          function hideUserSection() {
              document.getElementById('user-section').classList.add('hidden');
          }
          
          // Allow Enter key to trigger search
          document.getElementById('discordId').addEventListener('keypress', function(e) {
              if (e.key === 'Enter') {
                  searchUser();
              }
          });
      </script>
  </body>
  </html>
  ```
</CodeGroup>

### Key Features Explained

<AccordionGroup>
  <Accordion title="Discord ID Search">
    The app searches for members using their Discord user ID:

    * Uses the `/realm/{realmId}/members/search` endpoint
    * Searches by `type=discord` and the provided Discord ID
    * Returns member details including current point balances
  </Accordion>

  <Accordion title="Multi-Currency Support">
    Handles multiple point currencies in your realm:

    * Fetches available currencies from `/realm/{realmId}/points`
    * Populates dropdown menus for currency selection
    * Displays all current balances with currency names and emojis
  </Accordion>

  <Accordion title="Balance Management">
    Award or deduct points with full control:

    * Uses `/realm/{realmId}/members/{memberId}/point-balance` endpoint
    * Positive values for awards, negative for deductions
    * Optional reason tracking for audit purposes
    * Real-time balance updates after each operation
  </Accordion>
</AccordionGroup>

### How to Get Discord IDs

<Steps>
  <Step title="Enable Developer Mode">
    In Discord: Settings → Advanced → Enable "Developer Mode"
  </Step>

  <Step title="Copy User ID">
    Right-click any user → "Copy User ID"
  </Step>

  <Step title="Use in App">
    Paste the ID into the search field and click "Search Member"
  </Step>
</Steps>

## What's Next? 🚀

Congratulations! You just built your first DRIP app! 🎉

Here are some ideas for your next projects:

<CardGroup cols={2}>
  <Card title="Points Dashboard" icon="chart-bar">
    Show detailed analytics: points over time, top earners, activity trends
  </Card>

  <Card title="Member Directory" icon="users">
    Searchable member list with profiles, badges, and achievements
  </Card>

  <Card title="Quest Tracker" icon="map">
    Show active quests, completion rates, and member progress
  </Card>

  <Card title="Store Integration" icon="coins">
    Let members spend points on rewards directly from your app
  </Card>
</CardGroup>

### Ready for More Advanced Stuff?

<CardGroup cols={2}>
  <Card title="Multi-Realm Apps" icon="globe" href="/developer/multi-realm-apps">
    Build apps that work across multiple communities
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference">
    Explore all available endpoints and advanced features
  </Card>
</CardGroup>

<Info>
  **Share your creation!** Built something cool? Show it off in our [Discord community](https://discord.gg/dripchain) and get feedback from other developers! 🚀
</Info>

Built with [Mintlify](https://mintlify.com).
