[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/16Ytx_fz)

# W6 Summative
### Candidate Number: 37492

## Introduction
This report was commisioned by the Office of Quirky Inquiries (OQI) to answer the following research question:

### Research Question (RQ)
I will be adapting the original RQ "Is London really as rainy as the movies make it out to be?" and instead exploring "Is London more rainy than other rainy cities portrayed in movies?"

This adaptation was done due to constraints with resources (i.e., time and publicly available APIs), aiming to conduct research that will have mostly concise findings regarding the RQ and hypotheses. So, I decided to adapt the RQ and focus it on comparing London with other rainy movie-cities.

### Data and Variables
All data was obtained through the publicly available [world_cities.csv](https://simplemaps.com/data/world-cities) and the [OpenMeteo.com Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api). The main variable used on OpenMeteo is <b> daily rain_sum </b>, used to create an index called <b> the Raininess Index </b>. Based on OpenMeteo's description of daily variables, daily rain_sum is, as the name suggest, sum of daily rain in units mm.

### Hypotheses
<b> H0: </b> London's raininess is no different than any other generally-rainy city

<b> H1: </b> London is rainier than the other selected cities

### Methodology


## Getting Started
### Order of Notebooks
| NB | Name | Content |
| :--: | :--- | :--- |
| 00 | [Preprocessing](code/NB00-Preprocessing.ipynb) | Testing imported functions and the sample London dataframe |
| 01 | [City Selection](code/NB01-City-Selection.ipynb) | Choosing 5 cities and saving their data as a CSV |
| 02 | [Raininess Index](code/NB02-Raininess-Index.ipynb) | Creating the Raininess Index and plotting mean raininess |
| 03 | [Rankings](code/NB03-Rankings.ipynb) | Ranking cities daily and overall on how rainy they are |
| 04 | [Summary, Results, and Next Steps](code/NB04-Summary-Results-NS.ipynb) | Discussing results, limitations, and how the research could be expanded upon in the future |

### Key Information on Data Collection

##### 1) The time period 
My chosen time period is <b> between 2021-01-01 and 2024-01-01 </b>. I initially wanted to choose a start date that had significance for movies (e.g., the first movie screening in London). However, OpenMeteo's API does not go that far back, so I decided to adapt the time range and settled on 3 years.
##### 2) Number and selection of cities being compared to London
I decided to compare London's raininess with <b> 4 other cities </b>. This was due to 5 being a large enough sample size to see between-city variations in raininess while also allowing for a simple, neat way to draw conclusions and plotting the data. The cities I decided on and why (alongside some movie references) can be found in NB01 [here](code/NB01-City-Selection.ipynb).
##### 3) The Raininess Index
I used the <b> daily variable rain sum </b> from the OpenMeteo Historical Weather API to build my Raininess Index. You can find more details about why I picked rain sum and how I converted rain_sum into raininess in NB02 [here](code/NB02-Raininess-Index.ipynb).

## How to run the script
The dataframes used in this research have already been saved under the <b> data </b> folder; however, if you would like to collect the data yourself, you should run NB00-Preprocessing on your own machine.

Otherwise, proceed with running NB01-City-Selection, and then NB02 and NB03 respectively. 

NB04 is a markdown-only notebook explaining the results, limitations, and further research possibilities and thus has no other instructions.

## Findings
I have gone into more detail in [NB04](code/NB04-Summary-Results-NS.ipynb), but to summarize:
- London ranked 4/5 rainiest city in my dataset meaning that;
- London is most likely <b> not </b> as rainy as the movies make it out to be...
- ...Because there are at least 3 cities rainier than London, which also have considerable movie presences

## Use of AI Chatbot, ChatGPT
Although I did all of the coding and creative work for this assignment myself, I got help from ChatGPT when I needed help understanding my error codes and some chunks of code that we wrote in the labs/lectures. You can find a link to my conversation with the Chatbot [here]()!