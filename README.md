## UMN classroom schedule listing

Warning: __RETIRED__
Note: Astra scheduler has replaced the backend that this was consuming and won't be updated to accommodate it.

This project seeks to create an easy interface to UMN classroom schedules by providing a 
lookup for gaps in classroom usage along with classroom info.  

### The Scrapers
To get fresh html source data, run the main scraper (`scraper.py`). Or for 
a marginally faster scrape, `DEBUG=true python scraper.py`  which will use 
the EastBank.html dump for testing.  

This supplies you with the sqlite database

### Starting the app
To get started:
- make sure you have pip, virtualenv, and sqlite3 installed
- `virtualenv venv`
- `. venv/bin/activate`
- `pip install -r requirements.pip`
- `python app.py`
