import pandas as pd
import datetime
import time

def List_Of_Dictionary_2_Dataframe_CSV(List_Of_Dictionary,File_Path,mode,header):
    df = pd.DataFrame(List_Of_Dictionary)
    df = df.drop_duplicates()
    df.to_csv(File_Path, mode=mode, index=False, header=header, na_rep='Unkown')

def Remove_Duplicates_Rows(File_Path):
    df = pd.read_csv(File_Path)
    df.drop_duplicates(keep='last', inplace=True)
    df.to_csv(File_Path,mode='w',index=False,header=True,na_rep='Unkown')


def Clean_Data_Timestamp_Column(File_Path):
    df = pd.read_csv(File_Path)
    df['Timestamp'] = ((df['Timestamp'].str.strip()))  # beautify the data
    df.to_csv(File_Path, mode='w', index=False, header=True, na_rep='Unkown')


def Clean_Data_Attack_Type_Column(File_Path):
    df = pd.read_csv(File_Path)
    # Convert all of the same Attack Type that get from the 4 vendors website to the same Attack_Type
    df['Attack_Type'] = df['Attack_Type'].replace(['exploit' ,'attack' ,'Access' ,'Entrapment' ,'Corruption','File' ,  'Escalation' ,'Execution','Deletion' , 'Inclusion' , 'Creation' , 'Bypass','Retrieval','Evasion','Breach','Csrf' ], "Exploit")
    df['Attack_Type'] = df['Attack_Type'].replace(['Bufferoverflow','Bufferoverflow'], "Buffer_Overflow")
    df['Attack_Type'] = df['Attack_Type'].replace(['Overflow' ,'String' , 'DoS' ,'Bufferoverflow', 'spam','Bufferoverflow','Bufferoverflow','Ping'], "Buffer_Overflow")
    df['Attack_Type'] = df['Attack_Type'].replace(['malware','A' ,'infection','Register','Bax','Overwrite','Bax'], "Malware")
    df['Attack_Type'] = df['Attack_Type'].replace(['Injection','XSS','Csrf','Long','Disclosure','Request' ], "Injection")

    #-----------------------------------------------------------------------------------------------
    df['Attack_Type'] = ((df['Attack_Type'].str.strip()).str.lower()).str.title()  # beautify the data
    time.sleep(0.5)
    df.to_csv(File_Path,mode='w',index=False,header=True,na_rep='Unkown')
    time.sleep(0.5)


def Clean_Data_Attack_Source_AND_Attack_Target_Column(File_Path):
    df = pd.read_csv(File_Path)
    # Convert all of the same Countries with different name that get from the 4 vendors website to the same ['Attack_Source','Attack_Target']
    Clean_Column=['Attack_Source','Attack_Target']
    for Column_name in Clean_Column :
        df[Column_name] = df[Column_name].replace(['Russian Federation'], "Russia")
        df[Column_name] = df[Column_name].replace(['Curaçao'], "Venezuela")
        df[Column_name] = df[Column_name].replace(['Bouvet Island'], "Norway")
        df[Column_name] = df[Column_name].replace(['Macedonia(Fyrom)','Macedonia (Fyrom)','Macedonia (Fyrom)'], "Macedonia")
        df[Column_name] = df[Column_name].replace(['French Polynesia','Martinique','New Caledonia','Réunion'], "France")
        df[Column_name] = df[Column_name].replace(['Republic Of Lithuania'], "Lithuania")
        df[Column_name] = df[Column_name].replace([' RUSSIAN FEDERATION ','RUSSIAN FEDERATION','Russian Federation','Russian Federation','Russian Federation'],"Russia")
        df[Column_name] = df[Column_name].replace(['  Ireland','Anguilla','Saint Kitts And Nevis','Isle Of Man','Faroe Islands','Bermuda','Saint Vincent And The Grenadines','Guernsey','Barbados','Barbados','Cayman Islands','Ireland','BRITISH','VIRGIN ISLANDS', " VIRGIN ISLANDS, BRITISH ",'Jersey','Virgin Islands, British','British Virgin Islands'],"United Kingdom")
        df[Column_name] = df[Column_name].replace(['Vietnam'], "Viet Nam")
        df[Column_name] = df[Column_name].replace(["Lao People'S Democratic Republic"], "Laos")
        df[Column_name] = df[Column_name].replace(['Guadeloupe'], "Dominican Republic")
        df[Column_name] = df[Column_name].replace(['Slovak Republic'], "Slovakia")
        df[Column_name] = df[Column_name].replace(['Vanuatu','Fiji'], "Australia")
        df[Column_name] = df[Column_name].replace(['Iran, Islamic Republic of','Iran, Islamic Republic Of'], "Iran")
        df[Column_name] = df[Column_name].replace(['Korea, Republic Of'], "Republic Of Korea")
        df[Column_name] = df[Column_name].replace(['Korea, Republic Of','Korea, Republic Of','South Korea'], "Republic Of Korea")
        df[Column_name] = df[Column_name].replace(['Hashemite Kingdom Of Jordan','Republic Of Jordan'], "Jordan")
        df[Column_name] = df[Column_name].replace(['Trinidad And Tobago'], "Asia-Pacific")
        df[Column_name] = df[Column_name].replace(['Cote D’Ivoire', "Côte D'Ivoire"], "Ivory Coast")
        df[Column_name] = df[Column_name].replace(['Samoa','Bahamas','Virgin Islands, U.S','Virgin Islands, U.S.'], "United States")
        df[Column_name] = df[Column_name].replace(['Czechia'], "Czech Republic")
        df[Column_name] = df[Column_name].replace(['Qatar'], "United Arab Emirates")
        df[Column_name] = df[Column_name].replace(["Palestine, State Of",'Palestinian Territory'], "Palestine")
        df[Column_name] = df[Column_name].replace(['Cote D’Ivoire'], "Ivory Coast")
        df[Column_name] = df[Column_name].replace(['Moldova, Republic Of','Moldova'], "Republic Of Moldova")
        df[Column_name] = df[Column_name].replace(['Syria'], "Syrian Arab Republic")
        # -----------------------------------------------------------------------------------------------
        df[Column_name] = ((df[Column_name].str.strip()).str.lower()).str.title()  # beautify the data
    time.sleep(0.5)
    df.to_csv(File_Path, mode='w', index=False, header=True, na_rep='Unkown')
    time.sleep(0.5)

def Change_Time_From_Ctime_2_Datatime(File_Path,Column_Time):
    df = pd.read_csv(File_Path)
    Timestamp_List = df[Column_Time].tolist()
    for i in range(0, len(Timestamp_List)):
        try:
            Timestamp_List[i] = datetime.datetime.strptime(Timestamp_List[i], "%a %b %d %H:%M:%S %Y")
        except:
            continue

    df[Column_Time] = Timestamp_List
    df.to_csv(File_Path, mode='w', index=False, header=True, na_rep='Unkown')








