# Read Me File

## Instructions:

0. Before running this code you must install xlwt, dropbox and pandas using the following commands:

xlwt:
`pip install xlwt`
dropbox:
`pip install dropbox`
pandas:
`pip install pandas`
psutil:
`pip install psutil`
xlrd:
`pip install xlrd`
plotly4.0:
`pip install plotly==4.0.0`
bs4:
`pip install bs4`
lxml:
`pip install lxml`

1. After all 3 are installed, open you web browser and go to cars.com.

2. At the home page, select what kind of car you are looking for and then click search.

3. Scroll down to the bottom of the page and change the "per page" option to display 100 per page.

4. Copy the url for this page.

5. run Cars_Scraper.py in terminal window using the command `python Cars_Scraper.py`

6. The program will ask you to enter a listing, paste the url that was copied previously then press enter.

7. The program will scrape the data from the website listing and export it to an xls file. This file will then
be sorted by price, condition, and model. This information will then be placed in corresponding xls files.

8. All of these files will be uploaded to the designated dropbox folder.

## Notes:

- After program is executed, choosen dropbox folder must be empty before program can be executed again, if the folder
is not cleared, and error will occur.

- Drop box token and path can be assigned in dropboxdriver function

- Output files can also be found locally in the "output" folder within the "code" folder.

- Dropbox no longer supports HTML preview so file must be downloaded from dropbox to view
