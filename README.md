# Predict_and_analyze_Cyber_attacks with Machine Learning with naive_bayes GaussianNB model
Predict_and_analyze_Cyber_attacks run over  4 threat map websites, crawl and gather data over all the current real time attack


## Problem
Everyday tens of millions of cyber attacks take place around the world.
Each attack split to different type: Injection, Malware, Spam DDOS, Exploit Vulnerability and more…
Each attack can make a lot of damage for Industry company , government services and more…

## Project Goal 
- predict the next attack target ,based on the 'Attack_Source' column (display/print the 5 most Chance to the next attack target for each unique country on the    'Attack_Source' column)
- predict the next attack target ,based on the 'Attack_Source' and 'Attack_Type' column (display/print the 5 most Chance to the next attack target)
- predict the next Source attack ,based on the 'Attack_Target' column (display/print the 5 most Chance to the next attack target)
- predict the next Source attack ,based on the 'Attack_Target' and 'Attack_Type' column (display/print the 5 most Chance to the next attack target)
- predict the next Source & Target attack for each uniquely value from the 'Attack_Type' column

## Threat map website 

- Threat map FortiGuard - Fire eye Cyber Map -Threat map Bitdefender - Threat Map Checkpoint

## Features

- Crawl on a webpage.
- Save the data into .csv format (with Pandas)
- Gather the data :'Website_Source','Timestamp','Attack_Source','Attack_Target','Attack_Type','Attack_Name' from every website.
- Create a unique unique worldmap for all the "Attack_Source","Attack_Target" and for eavery unique value from the "Attack_Type" column.

## Pre-install API's

Soccer Match Calculator uses a number of api's to work properly:
- [Selenium]      - Helps me to get data from dynamic HTML websites
- [Beautifulsoup] - Helps me to navigate easier in HTML  
- [Matplotlib]    - Helps me to show data visually to the user
- [GaussianNB]    - Helps me to be able to predict the next cyber attack


## Installation

Soccer Match Calculator requires Python3 and up to run.
Also 

## Examples 

You can run my code like this:

sh
python Soccer.py 


This is an example of how to load and crawl inside every website and get the freshest data!
After its done, it will automatically generate any missing data that will be eventually availble in ti
