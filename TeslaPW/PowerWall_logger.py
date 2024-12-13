"""" This is a simple script to periodically query the Bioproton Pty Ltd Powerwall and
output the data into an excel spreadsheet. By AWANG""""

import requests, os, b4, openpyxl, time

url= "https:\\192.168.1.1\\"

urlaggregates= "https:\\192.168.1.1\\api\\meters\\aggregates\\"

def getTime():
    now=datetime.now()
    today=now.strftime("%m/%d/%Y, %H:%M:%S")
    return today

def getPWstatus:
    res=requests.get(url+"api\\sitemaster\\")
    PWstatus=res[0;1]
    return PWstatus

def getUptime:
    res=requests.get(url+"api\\sitemaster\\")
    Uptime=res[2]
    return uptime

def getGridstatus:
    res=requests.get(url+"api\\system_status\\status"
    Gridstatus=res
    return gridstatus

def getState:
    res=requests.get((url+"api\\system_status\\soe"
    state=res
    return state

def getCharge:
    res=requests.get(urlaggregates +"charge")
    charge=res
    return charge

def getGrid:
    res=requests.get(urlaggregates +"site")
    grid=res
    return grid
  
def getLoad():
    # Positive no. indicates the powerdraw from system to home/factory
    res=requests.get(urlaggregates +"load")
    load=res
    return load

def getSolar():
    # Positive no. indicates the power generated from solar and sent to the system
    # Negative no. indicates the power generated from solar and sent to grid
    res=requests.get(urlaggregates+"solar")
    solar=res
    return solar

                      
                     
wb=openpyxl.load_workbook('C://Users//wanga22//Bioproton Dropbox//alexander.wang@bioproton.com//Alex stuff//Work//Python scripts//PowerWall//PowerwallDatalog.xlsx')
sh1=wb['Data']
sh2=wb['Graphs']

                      
def getData():
    a=0
    #Run loop every minutes for the day  6:30am to 6:30pm
                      while a<49:
                      #Max rows and max columns
                      row=sh1.max_row
                      column=sh1.max_column
                      #Edit relevant cells in excel worksheet (Data)
                      sh1.cell(row+1,1).value=getTime()
                      sh1.cell(row+1,2).value=getStatus()
                      sh1.cell(row+1,3).value=getUptime()
                      sh1.cell(row+1,4).value=getStatus()
                      sh1.cell(row+1,5).value=getLoad()
                      getSolar()
                      if solar<0:
                          sh1.cell(row+1,8).value=getSolar()
                          sh1.cell(row+1,7).value=0
                      else:
                          sh1.cell(row+1,7).value=getSolar()
                          sh1.cell(row+1,8).value=0

                      totalSolar=getSolar()
                      sh1.cell(row+1,9).value=getSolar()
                      a+=1
                      time.sleep(900)


schedule.every().day.at("6:30").do(job,'PW Datalogging has started')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
                     

print("PW Data logging for the working day has been complete, the excel sheet has been generated")

wb.save('C://Users//wanga22//Bioproton Dropbox//alexander.wang@bioproton.com//Alex stuff//Work//Python scripts//PowerWall//PowerwallDatalog.xlsx')
    
    
