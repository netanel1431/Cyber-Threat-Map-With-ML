from Crawling.Crawling_Cyber_Attack_from_Bitdefender_Web import *
from Crawling.Crawling_Cyber_Attack_From_Checkpoint_Web import *
from Crawling.Crawling_Cyber_Attack_From_Fireeye_Website import *
from Crawling.Crawling_Cyber_Attack_From_Fortiguard_Web import *
from Clean_Pandas_DB.Preliminary_analysis_and_data_optimization_by_Pandas import *
from EDA_Visualizations.EDA_By_Bar_From_DF_Pandas import  *
from EDA_Visualizations.EDA_By_World_Map_From_DF_Pandas import *
from Machine_Learning.Machine_Learning_predict_the_next_cyber_attack import *

if __name__ == '__main__':

     path = os.getcwd()
     df_file_path = os.path.join(path, 'Cyber_Attack_DB.csv')
     Crawling_Amount=5           #If not config the default is 30
     mode='a'                    #'a'-edit the current CSV file , 'w' -delete existing CSV file and create new with the same name
     header=False                #False - Not add header to the CSV file , True - add header to the CSV file

     #Remove_Duplicates_Rows(df_file_path)
     time.sleep(0.5)
     Change_Time_From_Ctime_2_Datatime(df_file_path, "Timestamp")
     Clean_Data_Timestamp_Column(df_file_path)
     Clean_Data_Attack_Type_Column(df_file_path)
     Clean_Data_Attack_Source_AND_Attack_Target_Column(df_file_path)
     Remove_Duplicates_Rows(df_file_path)

     #Crawling
     #--------------------------Bitdefender------------------------------
     temp_df=Bitdefender_Details_and_Crawling(Crawling_Amount)                #Crawling from Bitdefender Website
     List_Of_Dictionary_2_Dataframe_CSV(temp_df, df_file_path,mode,header)    #Add the df that get from the Bitdefender crawling to our DB CSV file
     #--------------------------Checkpoint------------------------------
     temp_df=Checkpoint_Details_and_Crawling(Crawling_Amount)                 #Crawling from Checkpoint Website
     List_Of_Dictionary_2_Dataframe_CSV(temp_df, df_file_path, mode, header)  # Add the df that get from the Checkpoint crawling to our DB CSV file

     #---------------------------Fortiguard------------------------------
     temp_df =Fortiguard_Website_Details_and_Crawling(Crawling_Amount)        #Crawling from Fortiguard Website
     List_Of_Dictionary_2_Dataframe_CSV(temp_df, df_file_path, mode,header)   # Add the df that get from the Fortiguard crawling to our DB CSV file

     # --------------------------Fireeye----------------------------------
     temp_df = Fireeye_Website_Details_and_Crawling(Crawling_Amount)          #Crawling from Fireeye Website
     List_Of_Dictionary_2_Dataframe_CSV(temp_df, df_file_path, mode,header)   # Add the df that get from the Fireeye crawling to our DB CSV file

     #Clean_Pandas_DB
     #clean the df after add new data
     Remove_Duplicates_Rows(df_file_path)
     time.sleep(0.5)
     Change_Time_From_Ctime_2_Datatime(df_file_path,"Timestamp")
     Clean_Data_Timestamp_Column(df_file_path)
     Clean_Data_Attack_Type_Column(df_file_path)
     Clean_Data_Attack_Source_AND_Attack_Target_Column(df_file_path)
     Remove_Duplicates_Rows(df_file_path)
     #--------------------------------

     #EDA&Visualizations
     Create_Bars_By_Pandas_Column_Main(df_file_path)                        #Create PDF (of BARS) that Showing the coulms 'Attack_Source' , 'Attack_Target' ,'Attack_Type'
     Create_World_Map_By_Pandas_Column_Main(df_file_path)                    #Create WorldMap and Showing on map all that attack Source&Target for all the Countries at the Cyber_Attack_DB.csv file

     #Machine_Learning
     """
     The Machine Learning answer on the next QUES:
      1. predict the next attack target ,based on the 'Attack_Source' column (display/print the 5 most Chance to the next attack target for each unique country on the 'Attack_Source' column)
      2. predict the next attack target ,based on the 'Attack_Source' and 'Attack_Type' column (display/print the 5 most Chance to the next attack target)
      3. predict the next Source attack ,based on the 'Attack_Target' column (display/print the 5 most Chance to the next attack target)
      4. predict the next Source attack ,based on the 'Attack_Target' and 'Attack_Type' column (display/print the 5 most Chance to the next attack target)
      5. predict the next Source & Target attack for each uniquely value from the 'Attack_Type' column
     """
     Question_1(df_file_path)
     Question_2(df_file_path)
     Question_3(df_file_path)
     Question_4(df_file_path)
     Question_5(df_file_path)









