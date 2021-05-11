import time
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def Checkpoint_Details_and_Crawling(Count=30):
    #--------------Get information data--------------------------
    df_list=[]
    url ="https://threatmap.checkpoint.com/"
    driver = webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe") # Add your path
    driver.set_window_size(1360,768)
    driver.get(url)
    time.sleep(3)
    #--------------Start Crawling and get the attack rows------------------------
    for i in range(0,Count):
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        div_log=soup.find_all(class_='attack-feed-entry')
        time.sleep(1)
        for attack in div_log:
            Attack_dict={'Website_Source':"", 'Timestamp':"" , "Attack_Source":"" , "Attack_Target":"","Attack_Type":"","Attack_Name":""}
            #1
            Attack_dict["Website_Source"] = "Checkpoint"
            #2
            Attack_dict["Timestamp"] =time.ctime()
            temp = ((((attack.find(class_='attack-feed-entry-details overflow-ellipsis'))).text).replace(u'\xa0',u' ')).split("  ")
            #3-4
            Attack_dict["Attack_Target"] = temp[1]
            Attack_dict["Attack_Source"] = " ".join((temp[0].split(" "))[1:])
            if "United States" in Attack_dict["Attack_Source"]:
                Attack_dict["Attack_Source"]="United States"
            if "United States" in Attack_dict["Attack_Target"]:
                Attack_dict["Attack_Target"]="United States"
            #5
            Attack_dict["Attack_Type"]=attack.find('img')['alt'] # attack type
            #6
            Attack_dict["Attack_Name"] =attack.find(class_='overflow-ellipsis').text # attack name
            df_list.append(Attack_dict)
    #-------------------------Close driver and return data-----------------
    driver.close()
    driver.quit()
    return df_list #Return the DF list from Checkpoint_Website Crawling



