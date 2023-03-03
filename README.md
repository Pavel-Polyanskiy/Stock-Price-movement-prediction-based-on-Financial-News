# Stock Dynamics Forecasting based on Financial News
This project is aimed at forecasting stock dynamics by analyzing financial news and financial indicators. The project involves collecting financial news data from various sources, preprocessing and analyzing the data using natural language processing techniques, and then building predictive models integrated into Flask App to forecast stock dynamics based on the sentiment analysis of the news.

#### -- Project Status: Completed

### Table of Contents  
1. [Intro](#intro)  
   - [Techniques Used](#techniques-used) 
   - [Technologies](#technologies)
2. [Methodology](#methodology)  
   - [Dictionary-based Sentiment Analysis](#1-dictionary-based-sentiment-analysis)
   - [Topic Modelling](#2-topic-modelling)
   - [Neural Network](#3-neural-network)
3. [Installation](#installation) 
4. [Demo](#demonstation)
5. [Contact](#contact)

## Intro

The main goal of the project is to create a model that parses the news of the given company, transforms them into machine-readable format, extracts feauters and then returns prediction on the movement direction (up or down) for today using Deep Learning.


### Techniques Used
* Parsing
* Deep Learning
* Data Visualization
* Sentiment analysis
* Topic Modelling
* Financial analysis

### Technologies
* Python
* Flask

## Methodology

The research framework is depicted below:


<img width="1087" alt="Screenshot 2023-03-03 at 12 20 54" src="https://user-images.githubusercontent.com/84684422/222718797-e3d13828-e4ef-4431-a813-8afb1cd29218.png">

The ***first stage*** is to scrape for the financial news that are being published on the daily basis. The parser based on [Finnhub](https://finnhub.io/) API extracts all news for the particular day. Then, the algo sends the textual data into the preprocessing step where the news are cleaned, lemmatized and stop words are removed (just basic cleaning stuff). 

While textual data are being incorporated, the historical and current quates from the NYSE are received. Then, the next indicators are computed:

1. 10-, 20-, 30-day **Moving Average**

2. 12- and 26-day **Exponential Moving Average**

3. 6-, 12-, 24-day** Relative Strength Index (RSI)**

4. **Previous trend for stock** - it measures how many consequent days the stock demostrates the same pattern (either going up or down).

The ***second stage*** is feature extraction of the cleaned news text. There 2 feature extraction algorithms applied:

### 1. Dictionary-based Sentiment Analysis: 

   - Loughran-McDonald Sentiment Lexicon
   - Oliveira’s Stock Market Lexicon
   - SenticNet dictionary

The sentiment scores are assigned separately for each news and dictionary based on the dictionary's correspondent value. Then, the compound sentiment is computed by weighted average of 3 sentiment scores. Thus, each ticker receices the combined sentiment for each news for each day of observation.

### 2. Topic Modelling

Non-Negative Matrix Factorization model is applied for deriving the topics hidden in the news. Then, topics probability distributions are grouped by day, then the top-5 most probable topics among i-th day news are selected and transmitted to the final dataset. Finally, each ticker gets top-5 most relevant topics and their respective probabilities of being assigned for each day.


### 3. Neural Network
The ***third step*** is constructing the Neural Network using tensorflow and keras. Below you may find the architecture of the model fitted:

<p align="center">
<img width="329" alt="Screenshot 2023-03-03 at 12 36 02" src="https://user-images.githubusercontent.com/84684422/222721818-7c1e48c3-0d15-4269-8f74-dbffe11a6953.png">
</p>

The model is built with 3 ***Dense layers*** and 3 respective ***Batch Normalization*** layers. Neural Network should be given a **ticker** and the **company name** in order to give the predictions: **up-** or **down-trend** for today with the confidence probability.


## Installation

1. Clone this repo: 

`git clone https://github.com/Pavel-Polyanskiy/Stock-Price-movement-prediction-based-on-Financial-News`

2. Install the requirements:

`pip install requirements.txt`

3. Run the Flask app in your browser:

`python3 index.py`


## Demonstation

<video src=https://user-images.githubusercontent.com/84684422/221692818-4a984c2b-b957-4534-b7ff-a6938cd94047.mov width=180 ></video>

## Contact
✉️ pavelpolyanskiyhse@gmail.com



