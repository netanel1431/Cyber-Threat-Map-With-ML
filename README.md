# Predict and analyze Cyber Attacks With Machine Learning Random-Forest-Classifier model
Predict_and_analyze_Cyber_attacks run over 4 threat map websites, crawl and gather data over all the current real time attack

## Problem
Everyday tens of millions of cyber attacks take place around the world.
Each attack split to different type: Injection, Malware, Spam DDOS, Exploit Vulnerability and more…
Each attack can make a lot of damage for Industry company , government services and more…

## 5 Project Goals
- 1.predict the next attack target ,based on the 'Attack_Source' column (display/print the 5 most Chance to the next attack target for each unique country on the    'Attack_Source' column)
- 2.predict the next attack target ,based on the 'Attack_Source' and 'Attack_Type' column (display/print the 5 most Chance to the next attack target)
- 3.predict the next Source attack ,based on the 'Attack_Target' column (display/print the 5 most Chance to the next attack target)
- 4.predict the next Source attack ,based on the 'Attack_Target' and 'Attack_Type' column (display/print the 5 most Chance to the next attack target)
- 5.predict the next Source & Target attack for each uniquely value from the 'Attack_Type' column

## Threat map website 

- Threat map FortiGuard Website
- Fire eye Cyber Map Website
- Threat map Bitdefender Website 
- Threat Map Checkpoint Website 

## Features

- Crawl on a webpage.
- Save the data into .csv format (with Pandas)
- Gather the data :'Website_Source','Timestamp','Attack_Source','Attack_Target','Attack_Type','Attack_Name' from every website.
- Create a unique worldmap for all the "Attack_Source","Attack_Target" and for eavery unique value from the "Attack_Type" column.

## Pre-install API's

Predict_and_analyze_Cyber_attacks of api's to work properly:
- [Selenium]      - Helps me to get data from dynamic HTML websites (need install chromedriver.exe)
- [Beautifulsoup] - Helps me to navigate easier in HTML  
- [Matplotlib]    - Helps me to show data visually to the user
- [sklearn.ensemble]    - Helps me to be able to predict the next cyber attack


## Installation

Predict_and_analyze_Cyber_attacks requires Python3 and up to run.


## Examples 

You can run my code like this:
main.py 

This is an example of how to load and crawl inside every website and get the real time data!
After its done, it will automatically generate worldmap and pdf with bar graphs , while the machine learning will be answer to our five project goals

## How to improve the project ?
- Collect more data , with wider date range.
- Save data with real DB , like SQL...
- Upgrade/Change the machine learning model , maybe there is a better model.
- Handle with unknown values.
- Add more code map for the world map view
