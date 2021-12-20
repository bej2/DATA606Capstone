# Cryptocurrency Market Analysis

### Overview
Cryptocurrency is a phenomenon in recent times, from currencies like Bitcoin to Ethereum, people nowadays are more fascinated with its power and growth over the last few years, specifically in the year 2021. Twitter was increasingly used as a news source influencing purchase decisions by informing users of the currency and its increasing popularity, especially the tweets of certain influencers. With the increasing polarity, popularity and expansion of both cryptocurrency and online platforms like Twitter, quickly understanding the impact of sentiments through areas like tweets on price direction can provide a purchasing and selling advantage to a cryptocurrency user or a trader. In this paper, we analyze the ever-fluctuating price of Bitcoin and Ethereum prices utilizing Twitter sentiment data and its polarity and subjectivity, and Bitcoin and Ethereum data over a time period. Bitcoin and Ethereum, the two largest cryptocurrencies in terms of market capitalization. Our goal for this analysis is to create a model to determine if twitter sentiment is enough to determine price fluctuations of Bitcoin and Ethereum.

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

## Process
1. Research other projects and their approach to similar projects
2. Use research to delop a plan of action
3. Gather data to be used in the project
4. EDA
5. Model Creation
6. Evaluation of models

## Data
The datasets we used ware acquired from different sources. 
The live data was acquired from Yahoo! Finance while the historical data was from CoinMetrics, Blockchain.com, and EtherScan.io. 
We also utilized the module named pygooglenews to extract the news headlines, URLs and dates of Google News for performing the sentiment analysis of the news articles headlines. 
For blockchain analysis on Bitcoin, we utilized a platform called Blockchain. We got the following metrics from the website.
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

For Twitter data, a python module named Twint was used to gather data. It would return the date, text, user, and other data about the tweet. The text was put into a sentiment analysis module called Textblob. It would return both the polarity and subjectivity of the text. Polarity is how positive or negative the text is and subjectivity is how much of an opinion it is. These numbers were then averaged for each day.

## Methodology and Analyses

### Exploratory Data Analysis of cryptocurrencies
EDA is an approach for analyzing data using a variety of techniques. The purpose of EDA is to summarize visualizations and statistics to better understand data, its quality and structure. The following is the line graph of all 7 cryptocurrency from 2016 to present day and the correlation between them. 

<img src="https://github.com/bej2/DATA606Capstone/blob/main/Images/4_Ethereum_Sentiment_Pie.png" class="img-responsive" alt="1_Scaled_Prices_of_Crypto.png"> </div>

![1_Scaled_Prices_of_Crypto.png](Images/1_Scaled_Prices_of_Crypto.pngs)
![2_Crypto_Comparison.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/2_Crypto_Comparison.png)

### Twitter Sentiment Analysis
Twitter is a popular social media platform where users can create short messages to send out for others to read. In fact, in 2021 it is the 16th most popular platform with around 400 million users. These users produce roughly 6,000 tweets per second, which is about 350,000 tweets per minute, or about 500 million tweets sent each day. That is an incredible amount of data. Due to the sheer amount of data produced by twitter users it has become a goldmine for analyzing opinionated data from large sample sizes of users. Natural Language Processing (NLP) is the process of using computers to analyze text and speech in a way like how humans can. There are many different NLP tools, but the ones used in this project for sentiment analysis of twitter data are both Lexicon-based tools. 

Twitter provides to its users a free API in order to make gathering this data easier for the people who want to do so. Getting the API key requires submitting a request through Twitter's API page and then to go through their validation process, which can take anywhere from 48 hours to 1 month if the user is not denied. Once an API key is obtain-ed, using the python library Tweepy, a person can gather tweets on different keywords between two periods of time as long as they have received an API key from twitter. Twitter's API will then send back data which can then be analyzed using NLP tools.
With Tweepy, Vader Sentiment was used in order to determine the sentiment of each tweet. After processing, Vader would return both the polarity and subjectivity of the tweet. Polarity is how positive or negative the text was with 1 being positive and -1 being negative. Subjectivity is how much of an opinion it is with 1 being a complete opinion and 0 being a fact. The data could then be graphed/charted in order for better visuali-zation. The following is the sentiment analysis of bitcoin and Ethereum related tweets from a single day.

![3_Bitcoin_Sentiment_Pie.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/3_Bitcoin_Sentiment_Pie.png)
![4_Ethereum_Sentiment_Pie.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/4_Ethereum_Sentiment_Pie.png)

After using Tweepy for initial gathering of tweets, a limitation interfered with sufficient gathering of tweets. The limitation comes from Twitter’s api itself. Twitter’s api puts a limit of how many tweets can be gathered from a single user in a time frame. The current limit for tweets gathered in a single day is 2,400. This was problematic for us because we needed it for at least a single month, and it would take a month just to gather the data. To combat this, we switched over to the Twint library for python.

Twint is like Tweepy in the fact that it gathers tweets based on keywords, dates, as well as other factors. Where it differs is where it mattered. Twint gathers data not through the Twitter api, but through web scraping a Twitter page with search criteria put in. Because of this, there is no limit on the number of tweets that could be gathered.

Using Twint to our advantage we were able to gather tweets with the keyword’s bitcoin and Ethereum from November 1st, 2021, until December 12th, 2021. Using the Textblob library to perform sentiment analysis on the data and averaging the sentiment of each tweet per day resulted in the following charts.

![5_Bitcoin_Polarity.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/5_Bitcoin_Polarity.png)
![6_Ethereum_Polarity.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/6_Ethereum_Polarity.png)
 
### Google News Sentiment Analysis

The target of our project is to determine the factors influencing the cryptocurrency market prices. Upon performing the sentiment analysis done on tweets posted on social media platforms like Twitter, we realized that individual sentiment when combined with the volumes of tweets and retweets, led to fluctuations in the market values of some cryptocurrencies. We say ‘some’ because not all cryptocurrencies are discussed or tweeted about. It made sense to also look at other sources of sentiment i.e., news articles. 

We used Google News to carry out additional sentiment analysis on Bitcoin and Ethereum, since they were largely discussed and spoken about. Keeping up with the news constantly can be beneficial to everyday trading or investing opportunities in the crypto world. Therefore, we simply utilized the headlines to understand the overall sentiment for Bitcoin and Ethereum. We used a module named ‘pygooglenews’ for this purpose (Bugara, n.d.). We extracted the titles, URLs, and the respective dates of when they were published. We then applied the polarity to the titles, i.e., between -1 and 1. Here, -1 stood for negative, 0 for neutral, and 1 for positive polarity. It looked something like this.

![7_Google_News_Head.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/7_Google_News_Head.png)

We calculated the sentiment based on the polarity of the title. The sentiments were categorized as positive, negative or neutral.

![8_Google_News_Head.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/8_Google_News_Head.png) 

The sentiment count was plotted and visual-ized as follows. 

![9_Google_News_Bar.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/9_Google_News_Bar.png) 

We then plotted the total sentiment over time.

![10_Google_News_Chart.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/10_Google_News_Chart.png) 

We realized that for many titles, the polarity went further below -1 and further ahead of +1. This was because when multiple articles were published on the same day with either positive or negative sentiment, the polarity of the respective date fluctuated above or below the normal range of +1 and -1 respectively. So, we grouped the articles by date and found the polarity average using the following formulae. 
AveragePolarity = Polarity/ PolarityCount

Once again, we plotted the sentiment average over time.

![11_Google_News_Avg_Chart.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/11_Google_News_Avg_Chart.png)

### Blockchain Analysis

#### Bitcoin
We looked at the overall Bitcoin Blockchain and analyzed the contained data to underst-and the effects of different metrics on the price of the respective cryptocurrency. Below is the visualization of when the Bitcoin Blockchain observed an increase in its number of transactions. 

![12_Blockchain_Bitcoin.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/12_Blockchain_Bitcoin.png)

Visualize the increase of the processing power of the miners (hash_rate) of the respective cryptocurrency. We do this with respect to the entire network as a function of time.

![13_Blockchain_Bitcoin_Hash.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/13_Blockchain_Bitcoin_Hash.png)

It can be observed that the network got increased support of mining power from 2015 onwards. This gives us an understand-ing that our focus should ideally be on the dataset acquired from 2015 onwards. We also established the relationship between different variables that we used for further analysis. 

![14_Blockchain_Comparison.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/14_Blockchain_Comparison.png)

Median confirmation time for a transaction (btc_median_confirmation_time) and avg. transactions per block (btc_n_transactions_per_block) show an exponential relationship of sorts. A strong linear relationship can be observed between the Hash Rate and Difficulty level of the Bitcoin blockchain. Higher the hash rate, faster the block mining. Also, the difficulty level will be set in accordance with the same.
 
A relationship can be observed between the median confirmation time and the transaction fees (btc_transaction_fees). Below we observe the median transaction time and the number of transactions of 2015, 2016, 2017.

![15_Blockchain_Plot.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/15_Blockchain_Plot.png)
 
Below is the plotted graph of median transaction time and the average fee per transaction.
 
Time Series Analysis of average number of transactions per block over time.

![16_Blockchain_Chart.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/16_Blockchain_Chart.png)

A trend can be seen via the series plotted above. This can be because either this is time dependent, or the series values depend on the previous ones. For this purpose, we select the data before 2017. This is because the BTC network experienced a hard fork wherein BTC was split into BTC Bash and BTC. This can be observed in the fall in the graph during the same timeframe. We stay away from such extraneous events.

![17_Blockchain_Autocorrelation.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/17_Blockchain_Autocorrelation.png)
 
We regress Log (no. of transactions) = (m*t)+c. Here t->time. Aim is to understand if the residuals exhibit correlations. Significant figures for lags 1, 2 and periodically in 7, 14, 21 etc. can be noticed from the above plot. This indicates the presence of Seasonality in the series. Now, we model the regress against lag 1 & 8.

![18_Blockchain_Autocorrelation.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/18_Blockchain_Autocorrelation.png)

Overall, the model looks like a good fit. There seems to still exist some lag, but the guess is that increase in the number of variables will also increase the overfitting potential of the model. Selecting the right lags becomes fundamental.
The future of this analysis could focus on the function i.e., probability of orphan blocks, of other variables of the bitcoin network. Analysis of miners' incentives can be done by adding features to our data i.e., feature engineering.

#### Ethereum
The Ethereum Blockchain Analysis was fairly simple. We uploaded the selected features from EtherScan to our notebook and found the interrelationships between diffe-rent features and variables. The variables we used were as follows. 
	Ethereum Price History in USD from 2016 to 2021 (current day)
	Ethereum Block Size History from 2016 to 2021 (current day)
	Ethereum Unique Address Growth Rate from 2016 to 2021 (current day)
	Ethereum Hash Rate from 2016 to 2021 (current day)
	Ethereum Market Cap from 2016 to 2021 (current day)
	Ethereum Transaction History from 2016 to 2021 (current day) 

From the graph below, we can see that the block size of Ethereum overtime has increased significantly. Also, the blockchain seems to have been affected only after 2017. 

![19_Blocksize.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/19_Blocksize.png)

From the graph below, we can see the price of Ethereum in USD overtime. Also, the blockchain seems to have increased in price only after 2017.

![20_GrowthRate.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/20_GrowthRate.png)

Here, we see the Hashrate Growth Rate of the network over time. 

![21_Hashrate.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/21_Hashrate.png)

We look at the transaction history of the network. This transaction seems to have increased before the prices increased in the above graph. It can be observed that the number of transactions is proportional to the price of the cryptocurrency.  

![22_Trasaction.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/22_Trasaction.png)

From the below graph, we can see that the market capital of the network is 5 times what it was in 2018. Although the prices and transactions increased from 2017, the market price was significantly affected only by 2018.

![23_Marketcapital.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/23_Marketcapital.png)

We now look at the total number of transactions per year from 2015 onwards. Maximum number of transactions can be noticed in 2020 and 2021. 

![24_Total_Trasactions_Per_year.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/24_Total_Trasactions_Per_year.png)

## Models

### Decision Tree Regression Model Voting 
Decision Trees are flowcharts like tools where each node in the chart is a new decision that is used in order to make a final decision on what to do with the input. A Decision Tree Regression Model uses the same principle as a decision tree to correctly predict a value based on imputed features. 

![25_decisiontree.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/25_decisiontree.png)

After Decision Tree Regression Models make their predictions on the value of the price of BTC or ETH, they then “vote” on the correct value. This is simply done by averaging the values outputted by each model. The reason voting is useful is because the output relies on the prediction of multiple models. This is beneficial because if one model were to predict poorly, the others would help bring the value to a more precise one. The drawback would be that if one model is very accurate at predicting and the others are not, the one good model is held back by the others. Because the price of crypto can be very erratic and hard to predict, the use of model voting will hopefully eliminate some of the error of just using one model.

For this approach we used three different Decision Tree Regression models which are Random Forest, Gradient Boosting, and ExtraTrees. Random Forest works by creating multiple decision trees and using the outcome of each tree to average the output. The “random” in its name comes from randomly selecting a subset of features for decision making. ExtraTrees is similar to Random Forest, the difference being that in ExtraTrees, the top-down splitting in the tree learner is randomized. Finally, Gradient Boosting works by creating multiple decision tree models. Before each decision tree is created after the first, the Gradient Boosting model uses a gradient descent procedure to minimize the error in the next tree by removing features that cause errors.

The results of the voting-based Decision Tree Regression Models did not perform as well as was hoped. The models for Bitcoin had a R Squared value of around 0.9 and an Explained Variance Score of again around 0.9. On the other hand, for Ethereum, the models only scored around a 0.23 for R Squared and 0.5 for Explained Variance. What these values mean is important. R Squared describes how well a model fits its data, a high R Square a better fit. If too high, a model can be over-fitted, if too low a straight line could do better at predicting. The Explained Variance Score describes how well the model can handle variation. Even though the models scored high for Bitcoin, they still were not able to predict the fall in price, the same goes for Ethereum.

![26_dt_bitcoin_accuracy.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/26_dt_bitcoin_accuracy.png)
![27_dt_ethereum_accuracy.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/27_dt_ethereum_accuracy.png)
![28_dt_bitcoin_chart.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/28_dt_bitcoin_chart.png)
![29_dt_ethereum_chart.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/29_dt_ethereum_chart.png)

In order to increase the accuracy of the model, the best approach would be to gather a larger set of data. Due to limitations of twitter gathering tools, the data was constrained to only one and half months of data. If data was gathered for around a year, the amount would help better train the models. Another thing to consider would be adding more features and possibly removing some that hinder the models. The feature selection for these models were done by hand and an aided feature selector could possibly increase the accuracy. Also, to add features, more data should be considered besides just twitter sentiment, google news sentiment, and on chain data. A great feature to include could be the average price of graphics cards as they are used by crypto miners to mine different crypto currencies.

### GARCH Model: Forecasting Volatility of BTC/ETH.
When using traditional approaches to model time series, a change in variance or volatility over the time might cause problems. Autoregressive models may be created for univariate time-series data that are stationary (AR), trend (ARIMA or AutoRegressive Integrated Moving Average), and seasonal (SARIMA). A change in variance over time is one characteristic of a univariate time series that these autoregressive models do not model. In our time series data, the variance changes consistently over time, this would be called increasing and decreasing volatility.

![30_Volatility.png](https://github.com/bej2/DATA606Capstone/blob/main/Images/30_Volatility.png)

The property of a time series in which the variance increases in a systematic way, such as an increasing trend, is known as heteroskedasticity. It's a statistical term that means varying or unequal variance across the series. If the change in variance can be correlated over time, then it can be modeled using an autoregressive process, such as ARCH or GARCH. After testing different autoregressive models like ARMA, ARIMA, and SARIMA to forecast the daily returns and price, we decided to use the GARCH model to forecast the volatility in the market using the daily returns (stationary). The autoregressive models failed to predict the future movements of the market.
GARCH, or Generalized Autoregressive Conditional Heteroskedasticity, is an expansion of the ARCH model that includes a moving average component in addition to the autoregressive component. The model incorporates lag variance factors, as well as lag residual errors from a mean process. It aims to reduce forecasting errors by accounting for prior forecasting errors and improving the accuracy of ongoing predictions. With the addition of a moving average component, the model can now model both conditional changes in variance across time and changes in time-dependent variance. Conditional increases and decreases in variance are two examples.
The model has two parameters: 
	p: The number of lag variances.
	q: The number of lag residual errors.
After analyzing different model parameters, the GARCH model with the number of lag variances and lag residual errors equal to one gave us the best results. 

### Sequential Model and LSTM
We used LSTM network sequential models and LSTM Sequential models are the machine learning models that input or output sequences of data. We applied sequential model to set layers of dense, dropout, and LSTM. The neural network comprises a LSTM layer followed by 20% of dropout layer and dense layer with linear activation function. We compiled the model using Adam as the optimizer and Mean Squared Error as the loss function. The parameters are random number seed, length of the window, test set size, number of neurons in LSTM layer, epochs, batch size, loss, dropouts, and optimizer. We took live data and acquired it from Yahoo! Finance. 
We took live data from January 01, 2021, to the present day for testing to predict the prices. After that, we predicted the prices for the next day, after one month, after three months and after six months prices for all seven cryptocurrencies. All the predictions are done considering the date December 15, 2021. The line graph below shows the actual prices and predicted prices of every cryptocurrency. There are four-line graphs for every cryptocurrency which is on the next day, after 1 month, after 3 months and after 6 months which depicts actual price and predicted price.

![31_Bitcoin_Cryptocurrency_line_graph.jpg](https://github.com/bej2/DATA606Capstone/blob/main/Images/31_Bitcoin_Cryptocurrency_line_graph.jpg)
Figure: Bitcoin Cryptocurrency line graph

![32_Ethereum_Cryptocurrency_line_graph.jpg](https://github.com/bej2/DATA606Capstone/blob/main/Images/32_Ethereum_Cryptocurrency_line_graph.jpg)
Figure : Ethereum Cryptocurrency line graph

![33_Litecoin_Cryptocurrency_line_graph.jpg](https://github.com/bej2/DATA606Capstone/blob/main/Images/33_Litecoin_Cryptocurrency_line_graph.jpg)
Figure: Litecoin Cryptocurrency line graph

![34_Ripple_Cryptocurrency_line_graph.jpg](https://github.com/bej2/DATA606Capstone/blob/main/Images/34_Ripple_Cryptocurrency_line_graph.jpg)
Figure : Ripple Cryptocurrency line graph

![35_Dogecoin_Cryptocurrency_line_graph.jpg](https://github.com/bej2/DATA606Capstone/blob/main/Images/35_Dogecoin_Cryptocurrency_line_graph.jpg)
Figure : Dogecoin Cryptocurrency line graph

![36_Decentraland_Cryptocurrency_line_graph.jpg](https://github.com/bej2/DATA606Capstone/blob/main/Images/36_Decentraland_Cryptocurrency_line_graph.jpg)
Figure: Decentraland Cryptocurrency line graph

![37_Polygon_Cryptocurrency_line_graph.jpg](https://github.com/bej2/DATA606Capstone/blob/main/Images/37_Polygon_Cryptocurrency_line_graph.jpg)
Figure: Polygon Cryptocurrency line graph

We used LSTM and sequential model layers on all 7 cryptocurrencies separately. The results we acquired were as per the date December 15, 2021. The results are as follows.

![38_Crypto_Result_Chart.PNG](https://github.com/bej2/DATA606Capstone/blob/main/Images/38_Crypto_Result_Chart.PNG)
![39_Crypto_Result_Chart.PNG](https://github.com/bej2/DATA606Capstone/blob/main/Images/39_Crypto_Result_Chart.PNG)

## Conclusions
In conclusion, our models show that the price of crypto is difficult to predict. Even when sentiment from different platforms is incorporated into the feature selection and the models have a good fit, the models still struggle to predict future prices. In our Decision Tree model, we had both a R Squared value and an Explained Variance score of 0.9 for Bitcoin. This means that the model fit our data well in the test and could handle variance. Even with this, the model failed to accurately predict price 1 week out. 
The volatility model is used by financial institutions to estimate the return volatility of stocks, bonds, and other investment vehicles which helps them manage risk vs reward. In order to achieve an accurate forecast, we decided to use the GARCH model to forecast the volatility in the market. In our GARCH model, it accurately determined the periods of high volatility and low volatility.  
The LSTM model has a negative R Squared value for every version of the model which is completely unexpected. Even looking at the graph of the predicted price versus the actual price, we can see that the model is able to roughly predict prices and follow the trends of Bitcoin, Ethereum, and Litecoin.
Each one of these approaches to solve our problem worked in some aspects, but all ultimately failed to reach the level of accuracy we would have hoped for. Most of our data came from crypto markets. It turns out that this data, by itself, fails to accurately predict the price of crypto. The inclusion of sentiment analysis and blockchain analysis was in the hope of adding something to supplement this failure. Even with this inclusion, the models still failed. 
In the future, in order to expand on this topic and better solve our issue, we would diversify our data more. Market data, sentiment analysis, and blockchain analysis, was not enough for our models to reach the accuracy we desire. On top of this, we would use a computer aided feature selection algorithm in order to help narrow down the features  to ones that would more accurately predict the price of cryptocurrencies. 

## References
