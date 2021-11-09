# web_scrapping_olx.pl

The aim of this project is to show an example of ETL (Extract - Transform - Load) using web scrapping, SQLite database, and dashboarding in google cloud data studio for final product visualisation.

## This project is divided in 3 stages.

Before starting, make sure you have downloaded the repository and installed the following packages in your python environment:
- beautifulsoup
- sqlite3
- requests

### Stage 1: Extract

Here we aim to create a script that searches for house offers for the largest populated cities in Poland on [olx.pl](https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz). Then the script saves the data on a SQLite database which is defined in the code.

### Stage 2: Transform

A python extension is created in order to retrieve this data from the SQLite database to a normal pandas dataframe and some string transformation is taking place to ensure clean data for visualisation purposes.

### Stage 3: Load (to be continued...)

We intend to create a dashboard to present some data analytics on the data stored in the SQLite database.

The final interactive report can be visualised by clicking [here](https://datastudio.google.com/reporting/1e2a72ec-2acb-4855-8028-e08f19c97a3e), or by opening the PDF file in this repository 

Final thoughts:

- It seems that the house market in Poland is very dynamic around the area of the Mazovian Voivodeship since most of the offers are concentrated in this area.
- Between of the rest of the cities, the distribution of houses is quite similar and the amount of house offered doesn't vary much.
- At the moment (09/11/2021) there are 8413 properties being sold in OLX.pl in 79 different locations
