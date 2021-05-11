import time
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def Fortiguard_Website_Details_and_Crawling(Count=30):
    #--------------Get information data--------------------------
    df_list=[]
    url = "https://threatmap.fortiguard.com/"
    driver = webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe") # Add your path
    driver.set_window_size(1360,768)
    driver.get(url)
    time.sleep(3)

    #--------------Start Crawling and get the attack rows------------------------
    for i in range(0,Count):
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        div_log = soup.find_all(lambda tag: tag.name == 'tr' and tag.get('class') == ['log_entry'])  #for lambda soultion --> https://stackoverflow.com/questions/22726860/beautifulsoup-webscraping-find-all-finding-exact-match
        time.sleep(1)
    #--------------Clean the Data before send to the Main program-----------------
        for attack in div_log:
            Attack_dict = {'Website_Source': "", 'Timestamp': "", "Attack_Source": "", "Attack_Target": "",
                           "Attack_Type": "", "Attack_Name": ""}
            #1
            Attack_dict["Website_Source"] ="Fortiguard"
            #2

            Attack_dict["Timestamp"] =time.ctime()
            temp = attack.find_all("td")
            #3
            temp2 = temp[0].text.split(".")
            Attack_dict["Attack_Type"] = temp2[-1]

            #4
            temp2 = temp2[:-1]
            " ".join(temp2)
            Attack_dict["Attack_Name"] = " ".join(temp2)

            try:
                if attack.attrs['style']=="color:rgb(239,152,74);": #orange
                     Attack_dict["Attack_Source"]=temp[2].text
                elif attack.attrs['style']=="color:rgb(104,172,229);": #blue/azure
                    Attack_dict["Attack_Target"] = temp[2].text
                else:
                    continue
            except:
                continue

            df_list.append(Attack_dict)

    #-------------------------Close driver and return data-----------------
    driver.close()
    driver.quit()
    return df_list #Return the DF list from Fortiguard_Website Crawling

