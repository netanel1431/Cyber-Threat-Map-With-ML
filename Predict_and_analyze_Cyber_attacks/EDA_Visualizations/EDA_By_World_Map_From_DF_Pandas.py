# import pygal library
import pandas as pd
import pygal
from pygal.style import Style
import os
from datetime import datetime, timedelta



def Dictionary_Of_Countries_Code():
    Dictionary_Of_Countries_Code = {
            'ad': 'Andorra',
            'ae': 'United Arab Emirates',
            'af': 'Afghanistan',
            'al': 'Albania',
            'am': 'Armenia',
            'ao': 'Angola',
            'aq': 'Antarctica',
            'ar': 'Argentina',
            'at': 'Austria',
            'au': 'Australia',
            'az': 'Azerbaijan',
            'ba': 'Bosnia And Herzegovina',
            'bd': 'Bangladesh',
            'be': 'Belgium',
            'bf': 'Burkina Faso',
            'bg': 'Bulgaria',
            'bh': 'Bahrain',
            'bi': 'Burundi',
            'bj': 'Benin',
            'bn': 'Brunei Darussalam',
            'bo': 'Bolivia',
            'br': 'Brazil',
            'bt': 'Bhutan',
            'bw': 'Botswana',
            'by': 'Belarus',
            'bz': 'Belize',
            'ca': 'Canada',
            'cd': 'Congo, the Democratic Republic of the',
            'cf': 'Central African Republic',
            'cg': 'Congo',
            'ch': 'Switzerland',
            'ci': 'Ivory Coast',
            'cl': 'Chile',
            'cm': 'Cameroon',
            'cn': 'China',
            'co': 'Colombia',
            'cr': 'Costa Rica',
            'cu': 'Cuba',
            'cv': 'Cape Verde',
            'cy': 'Cyprus',
            'cz': 'Czech Republic',
            'de': 'Germany',
            'dj': 'Djibouti',
            'dk': 'Denmark',
            'do': 'Dominican Republic',
            'dz': 'Algeria',
            'ec': 'Ecuador',
            'ee': 'Estonia',
            'eg': 'Egypt',
            'eh': 'Western Sahara',
            'er': 'Eritrea',
            'es': 'Spain',
            'et': 'Ethiopia',
            'fi': 'Finland',
            'fr': 'France',
            'ga': 'Gabon',
            'gb': 'United Kingdom',
            'ge': 'Georgia',
            'gf': 'French Guiana',
            'gh': 'Ghana',
            'gl': 'Greenland',
            'gm': 'Gambia',
            'gn': 'Guinea',
            'gq': 'Equatorial Guinea',
            'gr': 'Greece',
            'gt': 'Guatemala',
            'gu': 'Guam',
            'gw': 'Guinea-Bissau',
            'gy': 'Guyana',
            'hk': 'Hong Kong',
            'hn': 'Honduras',
            'hr': 'Croatia',
            'ht': 'Haiti',
            'hu': 'Hungary',
            'id': 'Indonesia',
            'ie': 'Ireland',
            'il': 'Israel',
            'in': 'India',
            'iq': 'Iraq',
            'ir': 'Iran',
            'is': 'Iceland',
            'it': 'Italy',
            'jm': 'Jamaica',
            'jo': 'Jordan',
            'jp': 'Japan',
            'ke': 'Kenya',
            'kg': 'Kyrgyzstan',
            'kh': 'Cambodia',
            'kp': 'Korea, Democratic People’s Republic of',
            'kr': 'Republic Of Korea',
            'kw': 'Kuwait',
            'kz': 'Kazakhstan',
            'la': 'Laos',
            'lb': 'Lebanon',
            'li': 'Liechtenstein',
            'lk': 'Sri Lanka',
            'lr': 'Liberia',
            'ls': 'Lesotho',
            'lt': 'Lithuania',
            'lu': 'Luxembourg',
            'lv': 'Latvia',
            'ly': 'Libyan Arab Jamahiriya',
            'ma': 'Morocco',
            'mc': 'Monaco',
            'md': 'Republic Of Moldova',
            'me': 'Montenegro',
            'mg': 'Madagascar',
            'mk': 'Macedonia',
            'ml': 'Mali',
            'mm': 'Myanmar',
            'mn': 'Mongolia',
            'mo': 'Macao',
            'mr': 'Mauritania',
            'mt': 'Malta',
            'mu': 'Mauritius',
            'mv': 'Maldives',
            'mw': 'Malawi',
            'mx': 'Mexico',
            'my': 'Malaysia',
            'mz': 'Mozambique',
            'na': 'Namibia',
            'ne': 'Niger',
            'ng': 'Nigeria',
            'ni': 'Nicaragua',
            'nl': 'Netherlands',
            'no': 'Norway',
            'np': 'Nepal',
            'nz': 'New Zealand',
            'om': 'Oman',
            'pa': 'Panama',
            'pe': 'Peru',
            'pg': 'Papua New Guinea',
            'ph': 'Philippines',
            'pk': 'Pakistan',
            'pl': 'Poland',
            'pr': 'Puerto Rico',
            'ps': 'Palestine',
            'pt': 'Portugal',
            'py': 'Paraguay',
            're': 'Reunion',
            'ro': 'Romania',
            'rs': 'Serbia',
            'ru': 'Russia',
            'rw': 'Rwanda',
            'sa': 'Saudi Arabia',
            'sc': 'Seychelles',
            'sd': 'Sudan',
            'se': 'Sweden',
            'sg': 'Singapore',
            'sh': 'Saint Lucia',
            'si': 'Slovenia',
            'sk': 'Slovakia',
            'sl': 'Sierra Leone',
            'sm': 'San Marino',
            'sn': 'Senegal',
            'so': 'Somalia',
            'sr': 'Suriname',
            'st': 'Sao Tome and Principe',
            'sv': 'El Salvador',
            'sy': 'Syrian Arab Republic',
            'sz': 'Swaziland',
            'td': 'Chad',
            'tg': 'Togo',
            'th': 'Thailand',
            'tj': 'Tajikistan',
            'tl': 'East Timor',
            'tm': 'Turkmenistan',
            'tn': 'Tunisia',
            'tr': 'Turkey',
            'tw': 'Taiwan',
            'tz': 'Tanzania',
            'ua': 'Ukraine',
            'ug': 'Uganda',
            'us': 'United States',
            'uy': 'Uruguay',
            'uz': 'Uzbekistan',
            'va': 'Holy See (Vatican City State)',
            've': 'Venezuela',
            'vn': 'Viet Nam',
            'ye': 'Yemen',
            'yt': 'Mayotte',
            'za': 'South Africa',
            'zm': 'Zambia',
            'zw': 'Zimbabwe'

}
    return Dictionary_Of_Countries_Code

def Create_Map_By_Column(Title,df,Svg_File_Name,Column_Name,Open_Browser):

    sty = Style(legend_font_size=7,tooltip_font_size=7,value_font_size=7,major_label_font_size=6,value_label_font_size=7) # set style font of  the worldmap
    worldmap = pygal.maps.world.World(style=sty, legend_at_bottom=True, width=800, height=400)# create a world map
    worldmap.title=Title                                                # set the title of the map


    Countries_Code = Dictionary_Of_Countries_Code()                     # get the Mapping of Code_ID to Countries  from the dictionary on the Dictionary_Of_Countries_Code function

    Column_Name_2_Dict = ((df[Column_Name].value_counts())).to_dict()   # Create dictionary from specifec coulmn
    key_list = list(Countries_Code.keys())                              # Create List of key from Column_Name_2_Dict
    val_list = list(Countries_Code.values())                            # Create List of value from Column_Name_2_Dict


    # Take the value from the Countries_Code dict and change it with the value of Column_Name_2_Dict
    for i in range(0, len(val_list)):
        if val_list[i] in Column_Name_2_Dict.keys():
            temp=val_list[i]
            val_list[i] = (Column_Name_2_Dict.get(val_list[i]))
            Column_Name_2_Dict.pop(temp, None)

    Dic_Of_Code_and_Counter = dict(zip(key_list, val_list))
    for key, value in dict(Dic_Of_Code_and_Counter).items():
        if type(value) == str:
            del Dic_Of_Code_and_Counter[key]
    #------------------------------------------------------------------------------------------------

    worldmap.add(Column_Name, Dic_Of_Code_and_Counter)                     # set worldmap with the new  Mapping of Code_ID to Countries count


    #All key&Values that Stayed in Column_Name_2_Dict and not get assosciate to the Dictionary_Of_Countries_Code
    key_list = list(Column_Name_2_Dict.keys())
    val_list = list(Column_Name_2_Dict.values())

    for index in range(0,len(key_list)):
            print(str(key_list[index])+':'+str(val_list[index]))
            temp_string='Not Enable Mapping --> '+str(key_list[index])+':'+str(val_list[index])
            worldmap.add(temp_string, [{'label': 'This is Value that dont display at the Map'}])
    # ------------------------------------------------------------------------------------------------

    worldmap.render_to_file(Svg_File_Name)      # Save the SVG File
    if Open_Browser:
        worldmap.render_in_browser()           # Open the SVG File on my browser

def Pandas_Data_between_Range_Time(df,Timestamp_Coulmn,From_This_Date,Until_This_Date):
        df[Timestamp_Coulmn] = pd.to_datetime(df[Timestamp_Coulmn])  # Convert the Timestamp coulmn to Datatime coulmn
        Delta_Time = (df[Timestamp_Coulmn] >= From_This_Date) & (df[Timestamp_Coulmn] <= Until_This_Date)   #for each date value in the Timestamp coulmn check if he between the Delta_Time(From_This_Date<Timestamp_Vale_Per_Row<Until_This_Date)
        return df.loc[Delta_Time]

def Get_List_Of_Unique_Value_from_One_Specific_Coulmn(df,Column_Name):
        return df[Column_Name].unique()

def Create_World_Map_By_Pandas_Column_Main (df_File,From_This_Date='2021-04-01',Until_This_Date=datetime.today().strftime('%Y-%m-%d'),Timestamp_Coulmn='Timestamp',Coulmn_names_List=['Attack_Source','Attack_Target'],Svg_path_List=['EDA_Visualizations\\World_Map_Visualizations Of Attack Source','EDA_Visualizations\\World_Map_Visualizations Of Attack Target']):
        year, month, day = Until_This_Date.split("-")
        Until_This_Date_Include_This_Day = (datetime(int(year), int(month), int(day)) + timedelta(days=1)).strftime("%Y-%m-%d")
        for Coulmn_Index in range(0,len(Coulmn_names_List)):                                             # List of columns for them a map is required , example :['Attack_Source','Attack_Target']
                 Coulmn_name=Coulmn_names_List[Coulmn_Index]                                             # The name of the specific column from the Coulmn_names_List
                 Svg_path = Svg_path_List[Coulmn_Index]                                                  # The Svg_path(the folder) for the svg file

                 Title=Coulmn_name+' Between '+From_This_Date+" To "+Until_This_Date                     # The Title of the svg file
                 Svg_File_Name = os.path.join(Svg_path, Title+'.svg')                                    # The File name of the svg file
                 Open_Browser=True                                                                       # Open_Broweres =TRUE --> save&open the svg file to my browser   |||||    Open_Broweres =FALSE  --> Only savethe svg file to on my folder
                 df = pd.read_csv(df_File)                                                               # read the csv file


                 #df =Pandas_Data_between_Range_Time(df,Timestamp_Coulmn,From_This_Date,Until_This_Date_Include_This_Day)  # Zoom in  to the csv file between the given date range
                 Create_Map_By_Column(Title,df,Svg_File_Name,Coulmn_name,Open_Browser)                   # Create Map for all the value in the Coulmn_name (Usually Attack_Source or Attack_Target)  the map display the value and the count that the value appear in the coulmn


                 temp_list=Get_List_Of_Unique_Value_from_One_Specific_Coulmn(df,'Attack_Type')           # Get all unique values of the Attack Type coulmn
                 for Unique_Value_From_Attack_Type_Coulmn in temp_list:                                  # for each unique value in the Attack Type coulmn create World Map with the df that create by the Coulmn_names_List= Attack_Source or Attack_Target
                        temp_df =df.loc[df['Attack_Type'] ==Unique_Value_From_Attack_Type_Coulmn]
                        Title = Coulmn_name+' with the '+Unique_Value_From_Attack_Type_Coulmn+' Attack Type Between ' + From_This_Date + " To " + Until_This_Date
                        Svg_File_Name = os.path.join(Svg_path, Title + '.svg')
                        Coulmn_name = Coulmn_names_List[Coulmn_Index]
                        Open_Browser = False                                                            # Not need to open the browser for each unique values of the Attack Type coulmn , the file will be save at the Svg_path
                        Create_Map_By_Column(Title, temp_df, Svg_File_Name, Coulmn_name,Open_Browser)


