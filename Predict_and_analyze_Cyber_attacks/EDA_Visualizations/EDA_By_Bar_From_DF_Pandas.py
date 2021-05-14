import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
from datetime import datetime, timedelta


def Pandas_Data_between_Range_Time(df, Timestamp_Coulmn, From_This_Date, Until_This_Date):
    df[Timestamp_Coulmn] = pd.to_datetime(df[Timestamp_Coulmn])  # Convert the Timestamp coulmn to Datatime coulmn
    Delta_Time = (df[Timestamp_Coulmn] >= From_This_Date) & (df[Timestamp_Coulmn] < Until_This_Date)  # for each date value in the Timestamp coulmn check if he between the Delta_Time(From_This_Date<Timestamp_Vale_Per_Row<Until_This_Date)
    return df.loc[Delta_Time]
def Get_List_Of_Unique_Value_from_One_Specific_Coulmn(df, Column_Name):
        return df[Column_Name].unique()
def Create_Bar(Title,pdf,df,Coulmn_name):
    Column_Name_2_Dict = ((df[Coulmn_name].value_counts())).to_dict()  # Create dictionary from specifec coulmn
    key_list = list(Column_Name_2_Dict.keys())  # Create List of key from Column_Name_2_Dict
    val_list = list(Column_Name_2_Dict.values())  # Create List of value from Column_Name_2_Dict
    if len(key_list) <4000:
        annotation_to_bars_range_y=0.65
        annotation_to_bars_range_x = 0.65
        fontsize_=8
    else:
        annotation_to_bars_range_y=0.1
        annotation_to_bars_range_x = 111
        fontsize_=7
    # Figure Size
    fig, ax = plt.subplots(figsize=(15, 17), facecolor='w')

    # Horizontal Bar Plot
    ax.barh(key_list, val_list)

    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)

    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad=2)
    ax.yaxis.set_tick_params(pad=0, width=200, labelsize=fontsize_, length=10)

    # Add x, y gridlines
    ax.grid(b=True, color='grey',
            linestyle='-.', linewidth=0.5,
            alpha=0.5)

    # Show top values
    ax.invert_yaxis()

    # Add annotation to bars
    for i in ax.patches:
        plt.text(i.get_width() + annotation_to_bars_range_x, i.get_y() + annotation_to_bars_range_y,
                 str(round((i.get_width()), 2)),
                 fontsize=fontsize_, fontweight='bold',
                 color='green')

    # Add Plot Title
    ax.set_title(Title,
                 loc='left', )

    # Add Text watermark
    fig.text(0.9, 0.15, 'By Netanel Levi', fontsize=12,
             color='grey', ha='right', va='bottom',
             alpha=0.7)

    # Show Plot
    # plt.show()
    pdf.savefig(fig)
    plt.clf()
def Create_Bars_By_Pandas_Column_Main(df_File, From_This_Date='2021-04-01',Until_This_Date=datetime.today().strftime('%Y-%m-%d'),Timestamp_Coulmn='Timestamp',Coulmn_names_List=['Attack_Source', 'Attack_Target']):
    year, month, day = Until_This_Date.split("-")
    Until_This_Date_Include_This_Day = (datetime(int(year), int(month), int(day)) + timedelta(days=1)).strftime("%Y-%m-%d")
    pdf = PdfPages('EDA_Visualizations\\Summary_Graph_By_Bars.pdf')

    for Coulmn_Index in range(0, len(Coulmn_names_List)):  # List of columns for them a map is required , example :['Attack_Source','Attack_Target']
        Coulmn_name = Coulmn_names_List[Coulmn_Index]  # The name of the specific column from the Coulmn_names_List
        Title = Coulmn_name + ' Between ' + From_This_Date + " To " + Until_This_Date  # The Title of the svg file

        df = pd.read_csv(df_File)  # read the csv file
        #df = Pandas_Data_between_Range_Time(df, Timestamp_Coulmn, From_This_Date,Until_This_Date_Include_This_Day)  # Zoom in  to the csv file between the given date range
        Create_Bar(Title, pdf, df, Coulmn_name)

        temp_list = Get_List_Of_Unique_Value_from_One_Specific_Coulmn(df,'Attack_Type')  # Get all unique values of the Attack Type coulmn
        for Unique_Value_From_Attack_Type_Coulmn in temp_list:  # for each unique value in the Attack Type coulmn create World Map with the df that create by the Coulmn_names_List= Attack_Source or Attack_Target
             temp_df = df.loc[df['Attack_Type'] == Unique_Value_From_Attack_Type_Coulmn]
             Title = Coulmn_name + ' with the Attack_Type:' + Unique_Value_From_Attack_Type_Coulmn + ' .Between ' + From_This_Date + " To " + Until_This_Date
             Coulmn_name = Coulmn_names_List[Coulmn_Index]
             Create_Bar(Title, pdf, temp_df, Coulmn_name)

    pdf.close()


