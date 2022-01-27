# Backorder Prediction
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Problem Statement
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To build a model which will be able to predict whether an order for a given product can go on backorder or not. A backorder is the order which could not be fulfilled by the company. Due to high demand of a product, the company was not able to keep up with the delivery of the order.

# Data Description
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* In the Train dataset we are provided with 23 columns(Features) of data.

* sku : unique id for a product

* national_inv: present national level of inventory of the product

* lead_time : the amount of time between when a purchase order is placed to replenish products and when the order is received in the warehouse.

* in_transit_qty : qty of goods in transit

* forecast_3_month : Forecasted sales of the product for the next 3 months.

* forecast_6_month : Forecasted sales of the product for the next 6 months.

* forecast_9_month : Forecasted sales of the product for the next 9 months.

* sales_1_month : Actual Sales of the product in the last 1 month.

* sales_3_month : Actual Sales of the product in the last 3 months.

* sales_6_month : Actual Sales of the product in the last 6 months.

* sales_9_month : Actual Sales of the product in the last 9 months.

* min_bank: Minimum amount of stock recommended to have.

* potential_issue: Any problem identified with the product or part.

* pieces_past_due : product kept for long time, past their expiry date.

* perf_6_month_avg : Average performance of product over last 6 months.

* perf_12_month_avg: Average performance of product over last 12 months.

* local_bo_qty : ( undeliverable orders / total number of orders )*100.

* deck_risk : risk associated with keeping the items in stock

* ppap_risk : used to determine whether a production will produce parts with consistency and repeatability

* stop_auto_buy : Has the auto buy for the product, which was back ordered, cancelled.

* TARGET FEATURE : went_on_backorder - Whether an items was backordered or not

Total 23 features , 15  numerical & 8 categorical features.

# Approach
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The main goal is to predict the whether a product comes in backorder or not based on different factors available in the dataset.

* Business Knowledge - Gaining knowledge of the E-commerce domain.

* Data Wrangling - Understanding the data and it's behaviour.

* Data Cleaning -  Making sure the data used in later stage is garbage free.

* EDA - Performing Univariate , Bivariate , Multivariate analysis & understanding the relationship of features.

* Data Preparation - Splitting data into train and test samples and performing missing value treatment, outlier treatment through appropriate means, encoding of categorical features, undersampling of majority class as per observation of ratio of majority to minority classes seen in EDA.

* Feature Selection - Using top features for model building.

* Model Building - Create Several baseline models like Logistic regression, Random Forest, Decision tree, Gradient boosted tree algorithms.

* Hyperparameter tuning - Using Grid Search/Random Search to find optimum parameter.
# Tools & Skills Used
-------------------------------------------------------------------------------------------------------------------------------------------------------------

 * Pycharm - IDE
 * Visualization - Matplotlib , Seaborn
 * Database - Cassandra
 * Front End - HTML , CSS , JS
 * Framework - Flask
 * VCS - GIT
 * Deployment - Heroku
 * Data Wrangling - Numpy,Pandas
 * Scikit-learn - Ml Models
 * Python

# User Inter Face 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* Home 


<p align="center">
  <img src="https://github.com/007G/BackOrder_Prediction/blob/main/gitreadme_files/home.png" width='600px'>
</p>


* About


<p align="center">
  <img src="https://github.com/007G/BackOrder_Prediction/blob/df6911440f97319bd5c35b8389e26406cda57211/gitreadme_files/About.png" width='600px'>
</p>


* Why Backorder


<p align="center">
  <img src="https://github.com/007G/BackOrder_Prediction/blob/df6911440f97319bd5c35b8389e26406cda57211/gitreadme_files/why_backorder.png" width='600px'>
</p>


* Model Performance


<p align="center">
  <img src="https://github.com/007G/BackOrder_Prediction/blob/df6911440f97319bd5c35b8389e26406cda57211/gitreadme_files/model%20per.png" width='600px'>
</p>


* Predict


<p align="center">
  <img src="https://github.com/007G/BackOrder_Prediction/blob/df6911440f97319bd5c35b8389e26406cda57211/gitreadme_files/form.png" width='600px'>
</p>


* BackOrder or Not


<p align="center">
  <img src="https://github.com/007G/BackOrder_Prediction/blob/df6911440f97319bd5c35b8389e26406cda57211/gitreadme_files/not_backorder.png" width='600px'>
</p>


<p align="center">
  <img src="https://github.com/007G/BackOrder_Prediction/blob/df6911440f97319bd5c35b8389e26406cda57211/gitreadme_files/yes_backorder.png" width='600px'>
</p>



# Back Order Prediction Project Video 

https://github.com/007G/BackOrder_Prediction/blob/561646ec92b92fefb61cf69385e018e9106b5a26/gitreadme_files/Project_video.mp4



# Deployment Links
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
 Heroku Link : https://check-backorder.herokuapp.com/

 # Run 
 ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* Clone the project
```bash
  git clone https://github.com/007G/BackOrder_Prediction
```
* Go to the project directory
```bash
  cd BackOrder_Prediction
 ```
* Install dependencies
```bash
  pip install -r requirements.txt
```
* Setting up the Controllers files
```bash
    Change the values inside the Controllers folder
```
* Run the app.py
```bash
  python app.py
```

# Contribute
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 If You Wish to contribute, follow the below steps:

* Fork the repo

* Create a new branch
```bash
   git checkout -b feature_name
```

* Commit your work
```bash
     git commit -m "Comment"
```
* Push to the branch
```bash
      git push origin feature_name
```
* Create a pull request


# Help
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you find any bug , please raise an issue 
# Documentation
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[High Level Documentation](https://github.com/007G/BackOrder_Prediction/blob/561646ec92b92fefb61cf69385e018e9106b5a26/Docs/HLD.pdf)

[Low Level Documentation](https://github.com/007G/BackOrder_Prediction/blob/561646ec92b92fefb61cf69385e018e9106b5a26/Docs/LLD.pdf)

[WireFrame](https://github.com/007G/BackOrder_Prediction/blob/561646ec92b92fefb61cf69385e018e9106b5a26/Docs/Wireframe.pdf)

[Detail Project Report](https://github.com/007G/BackOrder_Prediction/blob/561646ec92b92fefb61cf69385e018e9106b5a26/Docs/DPR.pdf)

[Architecture Documentation](https://github.com/007G/BackOrder_Prediction/blob/561646ec92b92fefb61cf69385e018e9106b5a26/Docs/Architecture.pdf)

