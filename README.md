README FILE 

-------------------------
This project was a collaborative effort between;
    Jonathan Wu
    Yichen Jiang
    Di Wu
    Gordon (Yang) Jin


# Introduction of intended use for code
    This program intakes data of a city's weather attributions, including 
    temperature, wind, rain, pressure etc. It trains a model which outputs
    a prediction of the energy demand of a day, given a set of comprehensive
    weather attributes on that day. Both a linear regression model and a PCA
    model were created and tested against our data to see which model performed
    better based on r squared and MSE values.


# File structure and use of each file
    plots.py 
        - plots feature data across time

    fill_missing_data.py
        - Fills the missing values for train and validation datasets using the
          mean of the corresponding attributes from the corresponding season.
        
    price_demand_average.py
        - Computes the daily average energy demand from the data
    
    split.py
        - Unused features are removed from the data
        - Daily average price demand is added to the data
        - Splits the weather data into train and validate sets.
    
    feature_scaling.py
        - Feature standardised for PCA

    feature_selection.py
        - Takes in the filled train datasets, calculates and prints the mutual
          information score between attributes and average demand, enabling selection
          of feature with highest correlation to predictor variable.

    Regression.py
        - Trains a linear regression model using the filled training dataset
          based on the attributes selected based on the MI score.
        - The model is assessed against the original unfilled validation dataset,
          outputting R Square and MSE values.

    PCA.py
        - Each of the attributes are normalised by the MinMaxScaler.
        - PCA dimension reduction is performed on the dataset.
        - The dataset is split into training and validation data.
        - Linear regression model is used and assessed against the validation data.
        - The linear regression model is assessed on the test data. 


# Instructions on how to run your code.

    Order of running files:
        plots.py
        price_demand_average.py
        split.py
        fill_missing_data.py
        feature_scaling.py
        feature_selection.py
        Regression.py
        PCA.py
        












