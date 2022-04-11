
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)
##
##
##
##

movie_table = soup.find('table')
#print(movie_table)

movie_rows = movie_table.findAll('tr') #tag for rows is tr
print(movie_rows[1])

#for x in range(1,6): #start at 1, not 0 bc of header
    #td = movie_rows[x].findAll('td')
    #ranking = td[0].text
    #title = td[1].text
    #gross = td[5].text
    #total_gross = td[7].text

    #print(gross)
    #input()



#create a new excel doc
wb = xl.Workbook()

#assign the current sheet to the MySheet worksheet object variable (he used ws instead of MySheet)
MySheet = wb.active

MySheet.title = 'Box Office Report'

#write headings
MySheet['A1'] = 'No.'
MySheet['B1'] = 'Movie Title'
MySheet['C1'] = 'Release Date'
MySheet['D1'] = 'Gross'
MySheet['E1'] = 'Total Gross'
MySheet['F1'] = '% of Total Gross'

for x in range(1,6): #start at 1, not 0 bc of header
    td = movie_rows[x].findAll('td')
    ranking = td[0].text
    title = td[1].text
    gross = int(td[5].text.replace(",","").replace("$","")) #replace commas and dollar signs with nothing ""
    total_gross = int(td[7].text.replace(",","").replace("$",""))
    release_date = td[8].text

    percent_gross = round((gross/total_gross)*100,2)

    MySheet['A' + str(x+1)] = ranking
    MySheet['B' + str(x+1)] = title
    MySheet['C' + str(x+1)] = release_date
    MySheet['D' + str(x+1)] = gross
    MySheet['E' + str(x+1)] = total_gross
    MySheet['F' + str(x+1)] = str(percent_gross) + '%'

#adjust column sizes
MySheet.column_dimensions['A'].width = 5
MySheet.column_dimensions['B'].width = 30
MySheet.column_dimensions['C'].width = 25
MySheet.column_dimensions['D'].width = 16
MySheet.column_dimensions['E'].width = 20
MySheet.column_dimensions['F'].width = 26

#apply formatting to header row
header_font = Font(size=16, bold = True)

for cell in MySheet[1:1]:
    cell.font = header_font


wb.save('BoxOfficeReport.xlsx')