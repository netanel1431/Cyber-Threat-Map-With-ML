import time
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def Bitdefender_Details_and_Crawling(Count):
    #--------------Get information data--------------------------
    df_list=[]
    url = "https://threatmap.bitdefender.com/"
    driver = webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe") # Add your path
    driver.set_window_size(1360,768)
    driver.get(url)
    time.sleep(3)
    #--------------Start Crawling and get the attack rows------------------------
    for i in range(0,Count):
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        div_log=soup.find(class_='table_data').find_all('tr')[1:]
        time.sleep(1)
        for attack in div_log:
            Attack_dict={'Website_Source':"", 'Timestamp':"" , "Attack_Source":"" , "Attack_Target":"","Attack_Type":"","Attack_Name":""}
            #1
            Attack_dict["Website_Source"] = "bitdefender"
            #2
            Attack_dict["Timestamp"] =time.ctime()

            temp = attack.find_all("td")
            #3
            Attack_dict["Attack_Name"]   =temp[1].text
            #4
            Attack_dict["Attack_Type"]   =temp[2].text
            #5
            Attack_dict["Attack_Source"] =temp[3].text
            #6
            Attack_dict["Attack_Target"] =temp[4].text


            df_list.append(Attack_dict)
    #-------------------------Close driver and return data-----------------
    driver.close()
    driver.quit()
    return df_list #Return the DF list from Bitdefender_Website Crawling

