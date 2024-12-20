# Import necessary libraries
import pandas as pd
import numpy as np
from gymnasium import Env
from gymnasium.spaces import Discrete, Box

class TradingEnvironment(Env):
    def __init__(self, data, initial_balance=10000, trade_fraction=0.5):
        self.data = data
        self.initial_balance = initial_balance
        self.trade_fraction = trade_fraction  # Fraction to trade

        # Action and observation space
        self.action_space = Discrete(3)  # 0 = hold, 1 = buy, 2 = sell
        self.observation_space = Box(low=-np.inf, high=np.inf, shape=(len(features),), dtype=np.float32)

        # Internal state
        self.reset()

    def reset(self, seed=None, options=None):
        # Seed the environment
        if seed is not None:
            self._np_random, seed = seeding.np_random(seed)

        self.current_step = 0
        self.balance = self.initial_balance
        self.crypto_owned = 0
        self.crypto_price = self.data.iloc[self.current_step]['close']
        self.net_worth = self.initial_balance
        self.trades = []

        obs = self._next_observation()
        return obs, {}

    def _next_observation(self):
        obs = self.data.iloc[self.current_step][features].values
        return np.array(obs, dtype=np.float32)

    def step(self, action):
        self.current_step += 1
        terminated = self.current_step >= len(self.data) - 1
        truncated = False  # No truncation logic

        reward = 0

        # Market indicators
        rsi = self.data.iloc[self.current_step]['RSI']
        macd = self.data.iloc[self.current_step]['MACD']
        macd_signal = self.data.iloc[self.current_step]['MACD_signal']

        # Execute action
        if action == 1:  # Buy
            if self.balance > 0:
                # Valid buy action
                trade_amount = self.balance * self.trade_fraction
                self.crypto_owned += trade_amount / self.crypto_price
                self.balance -= trade_amount

                # Rewards for buying at the right time
                if rsi < 30:
                    reward += 0.04
                    if macd > macd_signal:
                        reward += 0.2  # Positive market condition
                else: 
                    reward -= 0.04

        elif action == 2:  # Sell
            if self.crypto_owned > 0:
                # Valid sell action
                trade_amount = self.crypto_owned * self.trade_fraction
                self.balance += trade_amount * self.crypto_price
                self.crypto_owned -= trade_amount

                # Rewards for selling at the right time
                if rsi > 70:
                    reward += 0.04
                    if macd < macd_signal:
                        reward += 0.2  # Positive market condition
                else: 
                    reward -= 0.04


        elif action == 0:  # Hold
            # Reward for holding in neutral market conditions
            if 30 <= rsi <= 70:
                reward += 0.04  # Neutral market condition
            else:
                # Small penalty for holding when action is expected
                reward -= 0.03


        # Update net worth
        self.crypto_price = self.data.iloc[self.current_step]['close']
        self.net_worth = self.balance + self.crypto_owned * self.crypto_price



        # Log the step details
        print(f"Step: {self.current_step}, Action: {action}, Net Worth: {self.net_worth}, Reward: {reward}")
                
        return self._next_observation(), reward, terminated, truncated, {}
    