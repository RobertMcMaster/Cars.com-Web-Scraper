# This work is mine unless otherwise Cited -Robert McMaster
import dropbox
import bs4 as bs
import urllib.request
import json
from xlwt import Workbook
import pandas as pd
import plotly
import plotly.graph_objects as go

# **Packages necassary to have installed**
# pip install plotly==4.0.0
# pip install xlrd
# pip install bs4
# pip install dropbox
# pip install xlwt
# pip install lxml
# pip install pandas
# pip install psutil

def CarsScraper():
    print("Enter cars.com listing: ", end="" )
    wb = Workbook()
    ws = wb.add_sheet("Sheet 1")

    # formats width of each column so text does not get cut off
    first_col = ws.col(0)
    first_col.width = 256*20
    second_col = ws.col(1)
    second_col.width = 256*20
    third_col = ws.col(2)
    third_col.width = 256*20

    ws.write(0,0, "Price")
    ws.write(0,1, "Condition")
    ws.write(0,2, "Model")

    myUrl = input()
    sauce = urllib.request.urlopen(myUrl).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    specificSoup = soup.find_all('div', class_='listing-row__details')
    count = 2
    print("Scraping webpage please wait...")


    row = 1
    while(len(specificSoup)):
        for div in specificSoup:

            modelName = div.find("h2", class_ = "listing-row__title")
            condition = div.find(class_ = "listing-row__stocktype")
            price = div.find("span", class_ = "listing-row__price")

            if (condition != None and price != None):
                writeToWorkBook(ws, price.text, condition.text, modelName.text, row)
                row+=1
            else:
                print("NOT PRICED---------------------------------------------------------")



        firstpart = myUrl.split("&page")
        secondpart = firstpart[1].split("&perPage")
        myUrl = firstpart[0] + "&page=" + str(count) + "&perPage" + secondpart[1]
        count +=1

        sauce = urllib.request.urlopen(myUrl).read()
        soup = bs.BeautifulSoup(sauce, 'lxml')
        specificSoup = soup.find_all('div', class_='listing-row__details')

    wb.save("output/car_data.xls")
    print("Scraping complete...")

def writeToWorkBook(ws: Workbook, price: str, condition: str, modelName: str, row: int):
    #strip() is used to remove white spaces so it is formatted better when added to the spreadsheet
    ws.write(row, 0, price.strip())
    ws.write(row, 1, condition.strip())
    ws.write(row, 2, modelName.strip())


def DropboxDriver():
    #Connects to dropbox folder and uploads files to folder
    access_token = 'HrV9Z6WWop4AAAAAAAAAAXKD68405NX-jW2s-xzHzKanmL-_JPt_IWB1V4T3mopA'
    transferData = TransferData(access_token)

    file_from1 = 'output/car_data.xls' #name of the file to be uploaded
    file_to1 = '/Web-scraper/data/car-data.xls' #dropbox folder path

    file_from2 = 'output/sorted_by_price.xls' #name of the file to be uploaded
    file_to2 = '/Web-scraper/data/sorted_by_price.xls' #dropbox folder path

    file_from3 = 'output/sorted_by_model.xls' #name of the file to be uploaded
    file_to3 = '/Web-scraper/data/sorted_by_model.xls' #dropbox folder path

    file_from4 = 'output/sorted_by_condition.xls' #name of the file to be uploaded
    file_to4 = '/Web-scraper/data/sorted_by_condition.xls' #dropbox folder path

    #Dropbox no longer supports HTML preview so file must be downloaded from dropbox to view
    file_from5 = 'output/Car_Data_Graph.html' #name of the file to be uploaded
    file_to5 = '/Web-scraper/data/Car_Data_Graph.html' #dropbox folder path

    transferData.upload_file(file_from1, file_to1)
    transferData.upload_file(file_from2, file_to2)
    transferData.upload_file(file_from3, file_to3)
    transferData.upload_file(file_from4, file_to4)
    transferData.upload_file(file_from5, file_to5)
    print("Transfer complete, go check your dropbox folder!")

def SpreadsheetSorter():
    excel_file = "output/car_data.xls"
    car_table = pd.read_excel(excel_file)

    sort_by_price = car_table.sort_values(["Price"], ascending=True)
    sort_by_price.to_excel("output/sorted_by_price.xls")

    sort_by_model = car_table.sort_values(["Model"], ascending=False)
    sort_by_model.to_excel("output/sorted_by_model.xls")

    sort_by_condition = car_table.sort_values(["Condition"], ascending=False)
    sort_by_condition.to_excel("output/sorted_by_condition.xls")
    print("Sorting complete...")


def CarPlotter():
    excel_file = 'output/sorted_by_model.xls'
    df = pd.read_excel(excel_file)
    print(df)

    data = [go.Scatter( x=df['Model'], y=df['Price'])]
    fig = go.Figure(data)
    fig.update_layout(
        xaxis_title="Model Type",
        yaxis_title="Price",
        title={'text': "Model Type (age) vs Price",
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
    )

    fig.write_html("output/Car_Data_Graph.html")
    print("Plotting complete...")


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

if __name__ == '__main__':
    CarsScraper()
    SpreadsheetSorter()
    CarPlotter()
    DropboxDriver()

