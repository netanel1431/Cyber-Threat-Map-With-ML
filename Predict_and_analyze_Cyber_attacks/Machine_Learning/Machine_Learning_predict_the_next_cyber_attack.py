#!/usr/bin/env python
# coding: utf-8
#Importing libraries

import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


"""
    The Machine Learning answer on the next QUES:
     1. predict the next attack target ,based on the 'Attack_Source' column (display/print the 5 most Chance to the next attack target for each unique country on the 'Attack_Source' column)
     2. predict the next attack target ,based on the 'Attack_Source' and 'Attack_Type' column (display/print the 5 most Chance to the next attack target)
     3. predict the next Source attack ,based on the 'Attack_Target' column (display/print the 5 most Chance to the next attack target)
     4. predict the next Source attack ,based on the 'Attack_Target' and 'Attack_Type' column (display/print the 5 most Chance to the next attack target)
     5. predict the next Source & Target attack for each uniquely value from the 'Attack_Type' column
"""
def Question_1(df_file_path):
    #1. predict the next attack target ,based on the 'Attack_Source' column (display/print the 5 most Chance to the next attack target for each unique country on the 'Attack_Source' column)
    print('###################################################################################################################')
    print('QUESTION 1')
    print('###################################################################################################################')
    # 1 --------------------------------------------------------------------------------------------------------
    """
    As we can observe from the header, the features are categorical strings. Thus, we need to convert those categories to numbers
    for example :
    For attack_source : 'unknown' will be 1 and 'united states' will be 2 and so on. 
    """
    data=pd.read_csv(df_file_path)
    encoder1 = LabelEncoder() # First encoder for attack source
    encoder2 = LabelEncoder() #second encoder for atatck target
    df1 = data[['Attack_Source','Attack_Target']].copy() # get the two columns from initial data set.
    df1['Attack_Source'] = encoder1.fit_transform(df1['Attack_Source']) # encode the attack source column
    df1['Attack_Target'] = encoder2.fit_transform(df1['Attack_Target']) # encode the attack target column
    X = df1['Attack_Source'].values # convert data to arrays
    y = df1['Attack_Target'].values # convert data to arrays
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42) #split the data to train/test
    model = RandomForestClassifier() #RandomForestClassifier model
    model.fit(X_train.reshape(-1, 1),y_train) #training of the model.
    pred = model.predict(X_test.reshape(-1,1)) #prediction on test set
    print('the accuracy is',accuracy_score(pred.reshape(-1,1),y_test.reshape(-1,1))) #the score

    for x in np.unique(X_test):
        input_test = X_test[x].reshape(-1,1) #a signle input test from test set.
        pred_test = model.predict_proba(input_test) # get the probability of each class.
        most_5_attacks =  list(encoder2.classes_[np.argsort(pred_test)[0][-5:]]) #get the most 5 chances to the next target
        """
        print of the result
        """
        print()
        print('Given the country {} as attack source, the 5 most Chance to the next attack target are: \n {}'.format(encoder1.inverse_transform(x.reshape(-1)),most_5_attacks))




def Question_2(df_file_path):
    #2. predict the next attack target ,based on the 'Attack_Source' and 'Attack_Type' column (display/print the 5 most Chance to the next attack target)
    print('###################################################################################################################')
    print('QUESTION 2')
    print('###################################################################################################################')
    """
    As we can observe from the header, the features are categorical strings. Thus, we need to convert those categories to numbers
    for example :
    For attack_source : 'unknown' will be 1 and 'united states' will be 2 and so on. 
    """
    data = pd.read_csv(df_file_path)
    encoder1 = LabelEncoder()  # Attack_Source encoder
    encoder2 = LabelEncoder()  # Attack_Target encoder
    encoder3 = LabelEncoder()  # Attack_Type encoder
    df2 = data[['Attack_Source', 'Attack_Type', 'Attack_Target']].copy()  # the new data to work with
    df2['Attack_Source'] = encoder1.fit_transform(df2['Attack_Source'])  # encode the attack source colmn
    df2['Attack_Target'] = encoder2.fit_transform(df2['Attack_Target'])  # encode the attack target colmn
    df2['Attack_Type'] = encoder3.fit_transform(df2['Attack_Type'])  # encode the attack type colmn
    """
    Series to arrays
    """
    X = df2[['Attack_Source', 'Attack_Type']].values
    y = df2['Attack_Target'].values
    """
    Data split (train/test)
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    # --------------------------------------
    """
    Naive bias model
    """
    model = RandomForestClassifier()
    model.fit(X_train, y_train)  # model training
    pred = model.predict(X_test)  # prediction on test set
    print('Accuracy score is', accuracy_score(pred.reshape(-1, 1), y_test.reshape(-1, 1)))  # model accuracy
    # -------------------------------------------
    pred_test = model.predict_proba(X_test[0].reshape(1, -1))  # proabilities prediction
    most_5_attacks = list(encoder2.classes_[np.argsort(pred_test)[0][-5:]])  # 5 most Chance to the next attack target
    input_attack_type = encoder3.inverse_transform(X_test[0][1].reshape(-1))
    input_attack_source = encoder1.inverse_transform(X_test[0][0].reshape(-1))
    print('5 most Chance to the next attack target for attack source {} and atatck type {} are: \n {}'.format(input_attack_source, input_attack_type,most_5_attacks))


def Question_3(df_file_path):
    #3. predict the next Source attack ,based on the 'Attack_Target' column (display/print the 5 most Chance to the next attack target)
    print('###################################################################################################################')
    print('QUESTION 3')
    print('###################################################################################################################')
    """
    As we can observe from the header, the features are categorical strings. Thus, we need to convert those categories to numbers
    for example :
    For attack_source : 'unknown' will be 1 and 'united states' will be 2 and so on. 
    """
    data = pd.read_csv(df_file_path)
    encoder1 = LabelEncoder()  # Attack_Source encoder
    encoder2 = LabelEncoder()  # Attack_Target encoder
    df1 = data[['Attack_Source', 'Attack_Target']].copy()  # new data
    df1['Attack_Source'] = encoder1.fit_transform(df1['Attack_Source'])  # Attack_Source encoding
    df1['Attack_Target'] = encoder2.fit_transform(df1['Attack_Target'])  # Attack_Target encoding
    """
    Series to arrays.
    """
    y = df1['Attack_Source'].values
    X = df1['Attack_Target'].values
    """
    Data split (train/test)
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    model = RandomForestClassifier()  # RandomForestClassifier model
    model.fit(X_train.reshape(-1, 1), y_train)  # model training
    pred = model.predict(X_test.reshape(-1, 1))  # prediction on test set
    print('accuracy score is', accuracy_score(pred.reshape(-1, 1), y_test.reshape(-1, 1)))
    pred_test = model.predict_proba(X_test[0].reshape(-1, 1))  # Probablities prediction
    most_5_attacks = list(encoder1.classes_[np.argsort(pred_test)[0][-5:]])  # 5 most Chance to the next attack target
    input_ = encoder2.inverse_transform(X_test[0].reshape(-1))[0]  # input from test set
    print('For the target [{}] the most 5 Attacks sources are \n {}'.format(input_, most_5_attacks))



def Question_4(df_file_path) :
    #4. predict the next Source attack ,based on the 'Attack_Target' and 'Attack_Type' column (display/print the 5 most Chance to the next attack target)
    print('###################################################################################################################')
    print('QUESTION 4')
    print('###################################################################################################################')

    """
    Features encoding
    """
    data = pd.read_csv(df_file_path)
    encoder1 = LabelEncoder()
    encoder2 = LabelEncoder()
    encoder3 = LabelEncoder()
    df2 = data[['Attack_Source', 'Attack_Type', 'Attack_Target']].copy()
    df2['Attack_Source'] = encoder1.fit_transform(df2['Attack_Source'])
    df2['Attack_Target'] = encoder2.fit_transform(df2['Attack_Target'])
    df2['Attack_Type'] = encoder3.fit_transform(df2['Attack_Type'])
    """
    Fetaures to arrays format
    """
    X = df2[['Attack_Type', 'Attack_Target']].values
    y = df2['Attack_Source'].values
    """
    Data split
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    # --------------------------------------
    model = RandomForestClassifier()
    model.fit(X_train, y_train)  # model training
    pred = model.predict(X_test)  # predict on test set
    print('the accuracy score is', accuracy_score(pred.reshape(-1, 1), y_test.reshape(-1, 1)))
    pred_test = model.predict_proba(X_test[0].reshape(1, -1))
    most_5_attacks = list(encoder1.classes_[np.argsort(pred_test)[0][-5:]])
    input_attack_type = encoder3.inverse_transform(X_test[0][0].reshape(-1))
    input_attack_target = encoder2.inverse_transform(X_test[0][1].reshape(-1))
    print('The most 5 attack sources for attack type {} and attack target {} are: \n {}'.format(input_attack_type,
                                                                                                input_attack_target,
                                                                                                most_5_attacks))
def Question_5(df_file_path):
    print('###################################################################################################################')
    print('QUESTION 5')
    print('###################################################################################################################')

    # features encoding
    data = pd.read_csv(df_file_path)
    # features encoding
    encoder1 = LabelEncoder()
    encoder2 = LabelEncoder()
    encoder3 = LabelEncoder()
    df2 = data[['Attack_Source', 'Attack_Type', 'Attack_Target']].copy()
    df2['Attack_Source'] = encoder1.fit_transform(df2['Attack_Source'])
    df2['Attack_Target'] = encoder2.fit_transform(df2['Attack_Target'])
    df2['Attack_Type'] = encoder3.fit_transform(df2['Attack_Type'])
    # Features into arrays
    X = df2['Attack_Type'].values
    y = df2[['Attack_Source', 'Attack_Target']].values
    # Data split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    # --------------------------------------
    model = RandomForestClassifier()  # RANDOM FOREST MODEL
    model.fit(X_train.reshape(-1, 1), y_train)  # model trainig
    pred = model.predict(X_test.reshape(-1, 1))  # prediction on tests set
    print('accuracy score is', accuracy_score(pred.reshape(-1, 1), y_test.reshape(-1, 1)))
    for x in np.unique(X_test):
        pred_test = model.predict_proba(x.reshape(1, -1))  # probabilities prediction
        most_5_attacks_source = list(encoder1.classes_[np.argsort(pred_test[0])[0][-5:]])  # most_5_attacks_source
        most_5_attacks_target = list(encoder2.classes_[np.argsort(pred_test[1])[0][-5:]])  # most_5_attacks_target
        attack_type_input = encoder3.inverse_transform(x.reshape(-1))  # singl input test
        print("########################### ATTACK TYPE {} #################################################".format(
            attack_type_input))
        print('The most 5 attack sources are \n {}'.format(most_5_attacks_source))
        print('The most 5 attack targets are \n {}'.format(most_5_attacks_target))


