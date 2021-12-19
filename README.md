# Cryptocurrency Market Analysis

## Team and Their Contributions
### Benjamin Jeremenko:
Research, Project Report, Literature Review, Twitter Sentiment Analysis, Prediction Analysis (Decision Tree Model using voting), GitHub

### Bhavika Bhupatrai Chavda:
Research, Slide Deck, Project Report, Literature Review, EDA, News Headlines Sentiment Analysis, Prediction Analysis (Sequential Model using LSTM layers), Blockchain Analysis (BTC, ETH), GitHub

### Dhruvil Dalwadi:
Research, Slide Deck, Project Report, Literature Review, EDA, Prediction Analysis (Sequential Model using LSTM layers)

### Parth Soni:
Research, Slide Deck, Project Report, Garch Model

### Temi Moses:
Research, Slide Deck, Project Report, Literature Review


## Goal

The goal of this project was to explore crypto currency and create a model using Block-Chain analysis along with Sentiment Analysis of Twitter data to accurately predict future prices of different crypto.

## Process
1. Research other projects and their approach to similar projects
2. Use research to delop a plan of action
3. Gather data to be used in the project
4. EDA
5. Model Creation
6. Evaluation of models

## Data
The datasets we used ware acquired from different sources. The live data was acquired from Yahoo! Finance while the historical data was from CoinMetrics, Blockchain.com, and EtherScan.io. We also utilized the module named pygooglenews to extract the news headlines, URLs and dates of Google News for performing the sentiment analysis of the news articles headlines. For Twitter data, a python module named Twint was used to gather data. It would return the date, text, user, and other data about the tweet. For blockchain analysis on Bitcoin, we utilized a platform called Blockchain. We got the following metrics from the website.
- Date
- Year
- Month
- Avg_Txn_Fee
- btc_market_price
- btc_total_bitcoins
- btc_market_cap
- btc_trade_volume
- btc_blocks_size
- btc_avg_block_size
- btc_n_orphaned_blocks
- btc_n_transactions_per_block
- btc_median_confirmation_time
- btc_hash_rate
- btc_difficulty
- btc_miners_revenue
- btc_transaction_fees
- btc_cost_per_transaction_percent
- btc_cost_per_transaction
- btc_n_unique_addresses
- btc_n_transactions
- btc_n_transactions_total
- btc_n_transactions_excluding_popular
- btc_n_transactions_excluding_chains_longer_than_100
- btc_output_volume
- btc_estimated_transaction_volume
- btc_estimated_transaction_volume_usd
 
For performing blockchain analysis for Ethereum, we utilized the data extracted from EtherScan.
We got the following metrics from the platform. 
-	Ethereum Price History in USD from 2016 to 2021 (current day)
-	Ethereum Block Size History from 2016 to 2021 (current day)
-	Ethereum Unique Address Growth Rate from 2016 to 2021 (current day)
-	Ethereum Hash Rate from 2016 to 2021 (current day)
-	Ethereum Market Cap from 2016 to 2021 (current day)
-	Ethereum Transaction History from 2016 to 2021 (current day)

## References
