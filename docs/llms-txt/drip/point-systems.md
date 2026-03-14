# Source: https://docs.drip.re/developer/point-systems.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Point Systems

> Master DRIP's point and currency systems 💰

Learn how to effectively manage points and currencies in your DRIP realm. This guide covers everything from basic point operations to advanced currency management strategies.

## Overview

DRIP's point system is highly flexible, allowing you to create multiple currencies, manage complex reward structures, and build engaging gamification experiences for your community.

<Info>
  Points in DRIP are called "Realm Points" and can be customized with names, emojis, and branding to match your community's theme.
</Info>

## Understanding Realm Points

### Point Types

<CardGroup cols={2}>
  <Card title="Primary Currency" icon="coins">
    Your main point system (e.g., XP, Coins, Tokens)

    * Usually the most visible to members
    * Used for major rewards and purchases
    * Often tied to overall member ranking
  </Card>

  <Card title="Secondary Currencies" icon="gem">
    Additional point types for specific purposes

    * Event-specific points (e.g., "Summer Points")
    * Category-specific rewards (e.g., "Art Coins")
    * Premium currencies (e.g., "Gems")
  </Card>
</CardGroup>

### Point Properties

Each Realm Point has these key properties:

```javascript  theme={"dark"}
const realmPoint = {
  id: "507f1f77bcf86cd799439015",
  name: "Community XP",
  emoji: "⭐",
  description: "Experience points for community participation",
  isDefault: true,
  isTransferable: true,
  minimumBalance: 0,
  maximumBalance: 1000000
};
```

## Basic Point Operations

### Awarding Points

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={"dark"}
    async function awardPoints(client, memberId, points, reason = '') {
      try {
        const result = await client.request('PATCH',
          `/realm/${client.realmId}/members/${memberId}/point-balance`,
          { tokens: points }
        );

        console.log(`✅ Awarded ${points} points to member ${memberId}`);
        if (reason) console.log(`Reason: ${reason}`);
        
        return result;
      } catch (error) {
        console.error(`❌ Failed to award points: ${error.message}`);
        throw error;
      }
    }

    // Examples
    await awardPoints(client, 'member123', 100, 'Completed daily quest');
    await awardPoints(client, 'member456', 50, 'Helpful community contribution');
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={"dark"}
    def award_points(client, member_id, points, reason=''):
        try:
            result = client.request('PATCH',
                f'/realm/{client.realm_id}/members/{member_id}/point-balance',
                {'tokens': points}
            )

            print(f"✅ Awarded {points} points to member {member_id}")
            if reason:
                print(f"Reason: {reason}")
            
            return result
        except Exception as e:
            print(f"❌ Failed to award points: {e}")
            raise

    # Examples
    award_points(client, 'member123', 100, 'Completed daily quest')
    award_points(client, 'member456', 50, 'Helpful community contribution')
    ```
  </Tab>
</Tabs>

### Deducting Points

```javascript  theme={"dark"}
// Deduct points (negative amount)
await awardPoints(client, 'member123', -25, 'Minor rule violation penalty');

// Or use a dedicated deduction function
async function deductPoints(client, memberId, points, reason = '') {
  return await awardPoints(client, memberId, -Math.abs(points), reason);
}
```

### Checking Balances

```javascript  theme={"dark"}
async function getPointBalance(client, memberId) {
  const members = await client.searchMembers('drip-id', memberId);
  
  if (members.data && members.data.length > 0) {
    const member = members.data[0];
    return member.pointBalances || [];
  }
  
  throw new Error('Member not found');
}

// Usage
const balances = await getPointBalance(client, 'member123');
balances.forEach(balance => {
  console.log(`${balance.realmPoint.name}: ${balance.balance} ${balance.realmPoint.emoji}`);
});
```

## Advanced Point Management

### Multiple Currency Systems

Manage different types of points for different purposes:

```javascript  theme={"dark"}
class MultiCurrencyManager {
  constructor(client) {
    this.client = client;
    this.currencies = new Map();
  }

  async loadCurrencies() {
    // Load available realm points
    const realmPoints = await this.client.getRealmPoints();
    
    for (const point of realmPoints.data) {
      this.currencies.set(point.name.toLowerCase(), {
        id: point.id,
        name: point.name,
        emoji: point.emoji,
        isDefault: point.isDefault
      });
    }
  }

  async awardCurrency(memberId, currencyName, amount, reason = '') {
    const currency = this.currencies.get(currencyName.toLowerCase());
    if (!currency) {
      throw new Error(`Currency '${currencyName}' not found`);
    }

    return await this.client.request('PATCH',
      `/realm/${this.client.realmId}/members/${memberId}/point-balance`,
      { 
        tokens: amount,
        realmPointId: currency.id
      }
    );
  }

  async transferBetweenCurrencies(memberId, fromCurrency, toCurrency, amount) {
    // Convert points between different currencies
    // This would need custom business logic for exchange rates
    
    const exchangeRate = this.getExchangeRate(fromCurrency, toCurrency);
    const convertedAmount = Math.floor(amount * exchangeRate);

    // Deduct from source currency
    await this.awardCurrency(memberId, fromCurrency, -amount, 'Currency conversion');
    
    // Add to target currency
    await this.awardCurrency(memberId, toCurrency, convertedAmount, 'Currency conversion');
    
    return { originalAmount: amount, convertedAmount, exchangeRate };
  }

  getExchangeRate(fromCurrency, toCurrency) {
    // Define your exchange rates
    const rates = {
      'xp_to_coins': 0.1,      // 10 XP = 1 Coin
      'coins_to_gems': 0.01,   // 100 Coins = 1 Gem
      'gems_to_coins': 100,    // 1 Gem = 100 Coins
    };

    const rateKey = `${fromCurrency}_to_${toCurrency}`;
    return rates[rateKey] || 1;
  }
}
```

### Batch Point Operations

Efficiently update multiple members at once:

```javascript  theme={"dark"}
async function batchPointAward(client, awards) {
  // awards = [{ memberId, points, reason }, ...]
  
  const updates = awards.map(award => ({
    memberId: award.memberId,
    tokens: award.points
  }));

  try {
    const result = await client.request('PATCH',
      `/realm/${client.realmId}/members/transaction`,
      { updates }
    );

    console.log(`✅ Batch awarded points to ${awards.length} members`);
    return result;
  } catch (error) {
    console.error('❌ Batch point award failed:', error.message);
    throw error;
  }
}

// Usage examples
await batchPointAward(client, [
  { memberId: 'member1', points: 100, reason: 'Event participation' },
  { memberId: 'member2', points: 150, reason: 'Contest winner' },
  { memberId: 'member3', points: 75, reason: 'Helpful member' }
]);
```

### Point Transfer Between Members

Enable peer-to-peer point transfers:

```javascript  theme={"dark"}
async function transferPoints(client, senderId, recipientId, amount, currency = null) {
  try {
    const transferData = {
      tokens: amount,
      recipientId: recipientId
    };

    if (currency) {
      transferData.realmPointId = currency;
    }

    const result = await client.request('PATCH',
      `/realm/${client.realmId}/members/${senderId}/transfer`,
      transferData
    );

    console.log(`✅ Transferred ${amount} points from ${senderId} to ${recipientId}`);
    return result;
  } catch (error) {
    console.error(`❌ Transfer failed: ${error.message}`);
    throw error;
  }
}

// Usage
await transferPoints(client, 'sender123', 'recipient456', 50);
```

## Gamification Strategies

### Point Earning Systems

<AccordionGroup>
  <Accordion title="Activity-Based Rewards">
    Reward different types of community engagement:

    ```javascript  theme={"dark"}
    const activityRewards = {
      'message_sent': 5,
      'reaction_added': 2,
      'voice_joined': 10,
      'helpful_reaction': 15,
      'first_message_daily': 25,
      'streak_7_days': 100
    };

    async function rewardActivity(client, memberId, activity) {
      const points = activityRewards[activity];
      if (points) {
        await awardPoints(client, memberId, points, `Activity: ${activity}`);
      }
    }
    ```
  </Accordion>

  <Accordion title="Milestone Rewards">
    Reward members for reaching specific milestones:

    ```javascript  theme={"dark"}
    const milestones = [
      { threshold: 100, reward: 50, title: 'Newcomer' },
      { threshold: 500, reward: 100, title: 'Regular' },
      { threshold: 1000, reward: 200, title: 'Veteran' },
      { threshold: 5000, reward: 500, title: 'Legend' }
    ];

    async function checkMilestones(client, memberId, currentPoints) {
      for (const milestone of milestones) {
        if (currentPoints >= milestone.threshold) {
          // Check if already awarded (you'd track this in your database)
          const alreadyAwarded = await hasAwardedMilestone(memberId, milestone.threshold);
          
          if (!alreadyAwarded) {
            await awardPoints(client, memberId, milestone.reward, 
              `Milestone achieved: ${milestone.title}`);
            await recordMilestoneAwarded(memberId, milestone.threshold);
          }
        }
      }
    }
    ```
  </Accordion>

  <Accordion title="Time-Based Bonuses">
    Implement daily, weekly, or seasonal bonuses:

    ```javascript  theme={"dark"}
    class TimeBonusManager {
      async getDailyBonus(client, memberId) {
        const today = new Date().toDateString();
        const lastClaim = await getLastBonusClaim(memberId);
        
        if (lastClaim !== today) {
          const bonusAmount = 25;
          await awardPoints(client, memberId, bonusAmount, 'Daily bonus');
          await recordBonusClaim(memberId, today);
          return bonusAmount;
        }
        
        return 0;
      }

      async getWeeklyBonus(client, memberId) {
        const streak = await getLoginStreak(memberId);
        if (streak >= 7) {
          const bonusAmount = 100 + (streak * 5); // Escalating bonus
          await awardPoints(client, memberId, bonusAmount, 'Weekly streak bonus');
          return bonusAmount;
        }
        
        return 0;
      }
    }
    ```
  </Accordion>
</AccordionGroup>

### Leaderboards and Rankings

Create competitive elements with point-based rankings:

```javascript  theme={"dark"}
class LeaderboardManager {
  constructor(client) {
    this.client = client;
  }

  async getTopMembers(limit = 10, currencyId = null) {
    const members = await this.client.searchMembers('drip-id', 'all');
    
    return members.data
      .filter(member => member.pointBalances && member.pointBalances.length > 0)
      .map(member => {
        const balance = currencyId 
          ? member.pointBalances.find(b => b.realmPoint.id === currencyId)
          : member.pointBalances[0];
          
        return {
          id: member.id,
          name: member.displayName || member.username,
          points: balance?.balance || 0,
          currency: balance?.realmPoint.name || 'Unknown'
        };
      })
      .sort((a, b) => b.points - a.points)
      .slice(0, limit)
      .map((member, index) => ({ ...member, rank: index + 1 }));
  }

  async getMemberRank(memberId, currencyId = null) {
    const leaderboard = await this.getTopMembers(1000, currencyId);
    const memberRank = leaderboard.find(entry => entry.id === memberId);
    
    return memberRank ? memberRank.rank : null;
  }

  async getSeasonalLeaderboard(season, currencyId = null) {
    // This would require tracking seasonal points separately
    // Implementation depends on your seasonal point tracking system
    
    const seasonalPoints = await this.getSeasonalPoints(season, currencyId);
    return seasonalPoints
      .sort((a, b) => b.points - a.points)
      .map((entry, index) => ({ ...entry, rank: index + 1 }));
  }
}
```

## Point Economy Design

### Balancing Your Economy

<CardGroup cols={2}>
  <Card title="Inflation Control" icon="trending-down">
    Prevent point inflation by:

    * Setting reasonable earning rates
    * Creating point sinks (ways to spend points)
    * Implementing diminishing returns
    * Regular economy reviews
  </Card>

  <Card title="Engagement Optimization" icon="target">
    Optimize for engagement by:

    * Rewarding diverse activities
    * Providing clear progression paths
    * Balancing effort vs. reward
    * Regular feedback and adjustments
  </Card>
</CardGroup>

### Point Sink Strategies

Create ways for members to spend their points:

```javascript  theme={"dark"}
const pointSinks = {
  store_items: {
    'premium_role': { cost: 1000, duration: '30 days' },
    'custom_emoji': { cost: 500, permanent: true },
    'channel_access': { cost: 250, duration: '7 days' }
  },
  
  services: {
    'priority_support': { cost: 100, duration: '24 hours' },
    'custom_title': { cost: 300, permanent: true },
    'event_priority': { cost: 150, duration: 'next event' }
  },
  
  gambling: {
    'daily_lottery': { cost: 10, chance_to_win: 0.1, payout: 200 },
    'point_doubler': { cost: 50, chance_to_win: 0.3, payout: 100 }
  }
};
```

## Analytics and Monitoring

### Point Flow Tracking

Monitor how points move through your economy:

```javascript  theme={"dark"}
class PointAnalytics {
  constructor(client) {
    this.client = client;
    this.transactions = [];
  }

  recordTransaction(type, memberId, amount, reason) {
    this.transactions.push({
      timestamp: Date.now(),
      type, // 'award', 'deduct', 'transfer'
      memberId,
      amount,
      reason
    });
  }

  getEconomyStats(timeframe = '7d') {
    const cutoff = Date.now() - this.getTimeframeMs(timeframe);
    const recentTransactions = this.transactions.filter(t => t.timestamp > cutoff);

    return {
      totalAwarded: recentTransactions
        .filter(t => t.type === 'award')
        .reduce((sum, t) => sum + t.amount, 0),
      
      totalDeducted: recentTransactions
        .filter(t => t.type === 'deduct')
        .reduce((sum, t) => sum + Math.abs(t.amount), 0),
      
      totalTransfers: recentTransactions
        .filter(t => t.type === 'transfer')
        .reduce((sum, t) => sum + t.amount, 0),
      
      netPointsCreated: recentTransactions
        .reduce((sum, t) => {
          if (t.type === 'award') return sum + t.amount;
          if (t.type === 'deduct') return sum - Math.abs(t.amount);
          return sum; // transfers don't create/destroy points
        }, 0)
    };
  }

  getTimeframeMs(timeframe) {
    const units = {
      'd': 24 * 60 * 60 * 1000,
      'h': 60 * 60 * 1000,
      'm': 60 * 1000
    };
    
    const value = parseInt(timeframe);
    const unit = timeframe.slice(-1);
    
    return value * (units[unit] || units.d);
  }
}
```

## Best Practices

<AccordionGroup>
  <Accordion title="Point Value Consistency">
    Keep point values meaningful and consistent:

    ```javascript  theme={"dark"}
    // ✅ Good: Consistent scaling
    const rewards = {
      simple_task: 10,
      medium_task: 25,
      complex_task: 50,
      major_contribution: 100
    };

    // ❌ Bad: Inconsistent scaling
    const badRewards = {
      simple_task: 5,
      medium_task: 100,
      complex_task: 15,
      major_contribution: 1000
    };
    ```
  </Accordion>

  <Accordion title="Error Handling">
    Always handle point operations gracefully:

    ```javascript  theme={"dark"}
    async function safePointAward(client, memberId, points, reason) {
      try {
        // Validate inputs
        if (!memberId || typeof points !== 'number' || points === 0) {
          throw new Error('Invalid award parameters');
        }

        // Check if member exists
        const members = await client.searchMembers('drip-id', memberId);
        if (!members.data || members.data.length === 0) {
          throw new Error('Member not found');
        }

        // Award points
        const result = await awardPoints(client, memberId, points, reason);
        
        // Log successful transaction
        console.log(`✅ ${points} points awarded to ${memberId}: ${reason}`);
        
        return result;
      } catch (error) {
        // Log error
        console.error(`❌ Failed to award points: ${error.message}`);
        
        // Don't throw for non-critical errors
        return null;
      }
    }
    ```
  </Accordion>

  <Accordion title="Performance Optimization">
    Optimize point operations for scale:

    ```javascript  theme={"dark"}
    // Use batch operations for multiple updates
    const batchUpdates = members.map(member => ({
      memberId: member.id,
      tokens: calculateReward(member.activity)
    }));

    await client.batchUpdatePoints(batchUpdates);

    // Cache frequently accessed data
    const memberBalances = new Map();

    async function getCachedBalance(memberId) {
      if (memberBalances.has(memberId)) {
        return memberBalances.get(memberId);
      }
      
      const balance = await getPointBalance(client, memberId);
      memberBalances.set(memberId, balance);
      
      // Clear cache after 5 minutes
      setTimeout(() => memberBalances.delete(memberId), 5 * 60 * 1000);
      
      return balance;
    }
    ```
  </Accordion>
</AccordionGroup>

## Next Steps

<CardGroup cols={2}>
  <Card title="Member Management" icon="users" href="/developer/managing-members">
    Learn to search and manage community members effectively
  </Card>

  <Card title="Ghost Credentials" icon="ghost" href="/developer/credentials">
    Pre-credit points to users before they join your realm
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference">
    Explore point-related API endpoints and advanced features
  </Card>

  <Card title="Best Practices" icon="shield" href="/developer/best-practices">
    Follow production-ready patterns for point systems
  </Card>
</CardGroup>

<Info>
  **Building a point economy?** Join our [Discord community](https://discord.gg/dripchain) to discuss strategies and get feedback from other developers! 💰
</Info>

Built with [Mintlify](https://mintlify.com).
