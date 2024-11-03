[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/16Ytx_fz)

# W6 Summative
### Candidate Number: 37492

## Introduction
This report was commisioned by the Office of Quirky Inquiries (OQI) to answer the following research question:

## Research Question
Is London really as rainy as the movies make it out to be?

## Data and Variables
All data was obtained through the publicly available world_cities.csv and the OpenMeteo.com Historical Weather website. The main variable used on OpenMeteo is <b> daily rain_sum </b>

## Hypotheses
<b> H0: </b> London is no different than any other generally-rainy city, in terms of raininess

<b> H1: </b> London is as rainy as the movies make it out to be, defined by how it compares to other cities on raininess

## Getting Started
### Order of Notebooks
| No | Name | Content |
| :--: | :--- | :--- |
| 1 | [City Selection](https://github.com/lse-ds105/ds105a-2024-w06-summative-deyavuz/blob/main/code/NB02-City-Selection.ipynb) | x |
| 2 | [Raininess Index](https://github.com/lse-ds105/ds105a-2024-w06-summative-deyavuz/blob/main/code/NB01-Raininess-Index.ipynb) | How I decided on my variables and created my Raininess Index |
| 3 | [Rankings]() | x |
| 4 | [Summary and Results]() | x |

### Key Information on Data Collection

##### 1) The time period I have chosen is between 2021-01-01 and 2024-01-01
I initially wanted to choose a start date that had significance for movies (e.g., the first movie screening in London). However, OpenMeteo's API does not go that far back, so I decided to adapt the time range and settled on 3 years.
##### 2) Number and selection of cities being compared to London
I decided to compare London's raininess with 4 other cities. This was due to 5 being a large enough sample size to see between-city variations in raininess while also allowing for a simple, neat way to draw conclusions and plotting the data. The cities I decided on and why (alongside some movie references) can be found in NB01 [here]().
##### 3) My Raininess Index (and the variables used from OpenMeteo's API to create it)
I have used the daily variable rain sum to build my Raininess Index. You can find more details about why I picked rain sum and how I converted rain_sum into raininess in NB02 [here]().

## How to run the script


## Findings
I have gone into more detail in [NB04](), but to summarize:
- London ranked 4/5 rainiest city in my dataset meaning that;
- London is most likely <b> not </b> as rainy as the movies make it out to be!;
- Because there are at least 3 cities rainier than London, which also have considerable movie presences

## Use of AI Chatbot, ChatGPT
Although I did all of the coding and creative work for this assignment myself, I got help from ChatGPT when I needed help understanding my error codes and some chunks of code that we wrote in the labs/lectures. You can find a link to my conversation with the Chatbot [here]()!