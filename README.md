[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/16Ytx_fz)

# W6 Summative
### Candidate Number: 37492

## Introduction
This report was commisioned by the Office of Quirky Inquiries (OQI) to answer the following research question:

### Research Question
Is London really as rainy as the movies make it out to be?

### Data and Variables
All data was obtained through the publicly available [world_cities.csv](https://simplemaps.com/data/world-cities) and the [OpenMeteo.com Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api). The main variable used on OpenMeteo is <b> daily rain_sum </b>

### Hypotheses
<b> H0: </b> London is no different than any other generally-rainy city, in terms of raininess

<b> H1: </b> London is as rainy as the movies make it out to be, defined by how it compares to other cities on raininess

## Getting Started
### Order of Notebooks
| NB | Name | Content |
| :--: | :--- | :--- |
| 00 | [Preprocessing](code/NB00-Preprocessing.ipynb) | x |
| 01 | [City Selection](code/NB01-City-Selection.ipynb) | x |
| 02 | [Raininess Index](code/NB02-Raininess-Index.ipynb) | How I decided on my variables and created my Raininess Index |
| 03 | [Rankings](code/NB03-Rankings.ipynb) | x |
| 04 | [Summary and Results]() | x |

### Key Information on Data Collection

##### 1) The time period 
My chosen time period is <b> between 2021-01-01 and 2024-01-01 </b>. I initially wanted to choose a start date that had significance for movies (e.g., the first movie screening in London). However, OpenMeteo's API does not go that far back, so I decided to adapt the time range and settled on 3 years.
##### 2) Number and selection of cities being compared to London
I decided to compare London's raininess with <b> 4 other cities </b>. This was due to 5 being a large enough sample size to see between-city variations in raininess while also allowing for a simple, neat way to draw conclusions and plotting the data. The cities I decided on and why (alongside some movie references) can be found in NB01 [here](code/NB01-City-Selection.ipynb).
##### 3) My Raininess Index
I used the <b> daily variable rain sum </b> from the OpenMeteo Historical Weather API to build my Raininess Index. You can find more details about why I picked rain sum and how I converted rain_sum into raininess in NB02 [here](code/NB02-Raininess-Index.ipynb).

## How to run the script


## Findings
I have gone into more detail in [NB04](), but to summarize:
- London ranked 4/5 rainiest city in my dataset meaning that;
- London is most likely <b> not </b> as rainy as the movies make it out to be!;
- Because there are at least 3 cities rainier than London, which also have considerable movie presences

## Use of AI Chatbot, ChatGPT
Although I did all of the coding and creative work for this assignment myself, I got help from ChatGPT when I needed help understanding my error codes and some chunks of code that we wrote in the labs/lectures. You can find a link to my conversation with the Chatbot [here]()!