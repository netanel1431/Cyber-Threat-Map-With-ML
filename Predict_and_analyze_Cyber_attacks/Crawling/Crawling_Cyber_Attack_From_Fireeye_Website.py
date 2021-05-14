import time
from bs4 import BeautifulSoup
from selenium import webdriver
import  time

def Fireeye_Website_Details_and_Crawling(Count=30):
    #--------------Get information data--------------------------
    df_list=[]
    url = "https://www.fireeye.com/cyber-map/threat-map.html"
    driver = webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe") # Add your path
    driver.set_window_size(1360,768)
    driver.get(url)
    time.sleep(3)
    #--------------Start Crawling and get the attack rows------------------------
    for i in range(0,Count):
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        div_log=soup.find_all(id='log')
        time.sleep(1)
        for attack in div_log:
            attack_list = ((attack.text).split("[X] NEW ATTACK: FROM"))
            attack_list = list(filter(None, attack_list))  # filter/delete empty index
    #--------------Clean the Data before send to the Main program-----------------
        for attack in attack_list:

            Attack_dict={'Website_Source':"", 'Timestamp':"" , "Attack_Source":"" , "Attack_Target":"","Attack_Type":"","Attack_Name":""}
            temp_list = attack.split("TO")
            temp_list = list(filter(None, temp_list))  # filter/delete empty index

            #1
            Attack_dict["Website_Source"]="Fireeye"
            #2
            Attack_dict["Attack_Source"]=temp_list[0].replace("[", "").replace("]", "")
            #3
            Attack_dict["Attack_Target"]=(temp_list[1].replace("[", "").replace("]", ""))
            #4
            Attack_dict["Timestamp"] =time.ctime()


            df_list.append(Attack_dict)
    #-------------------------Close driver and return data-----------------
    driver.close()
    driver.quit()
    return df_list #Return the DF list from Fireeye_Website Crawling


