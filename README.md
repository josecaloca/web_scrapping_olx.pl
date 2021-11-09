# web_scrapping_olx.pl

The aim of this project is to show an example of ETL (Extract - Transform - Load) using web scrapping, SQLite database, and dash for final product visualisation dashboarding.

## This project is divided in 3 stages.

Before starting, make sure you have downloaded the repository and installed the following packages in your python environment:
- beautifulsoup
- sqlite3
- requests

### Stage 1: Extract

Here we aim to create a script that searches for houses in the Masovian Voivodeship on [olx.pl](https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz) and saves the data on a SQLite database.

### Stage 2: Transform

A python extension is created in order to retrieve this data from the SQLite database to a normal pandas dataframe.

### Stage 3: Load (to be continued...)

We intend to create a dash webapp to present some data analytics on the data stored in the SQLite database
