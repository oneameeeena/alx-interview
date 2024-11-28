def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.
    
    Args:
        coins (list): List of coin denominations available
        total (int): Target total amount
    
    Returns:
        int: Fewest number of coins needed to meet total,
             or -1 if total cannot be met
    """
    # Handle base cases
    if total <= 0:
        return 0
    
    # Initialize dynamic programming array 
    # dp[i] will store minimum coins needed to make amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Compute minimum coins for each amount from 1 to total
    for amount in range(1, total + 1):
        # Try each coin denomination
        for coin in coins:
            if coin <= amount:
                # Update minimum coins if current coin provides a better solution
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # Return result, converting infinite to -1 if total cannot be met
    return dp[total] if dp[total] != float('inf') else -1
