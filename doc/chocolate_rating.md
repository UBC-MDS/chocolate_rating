---
title: "Chocolate Rating Predictor"
author: "Eyre Hong, Lisha Guo, Markus Nam, Robin Dhillon"
date: "2022/11/25"
output:
  html_document:
    toc: yes
    keep_md: yes
  pdf_document:
    toc: yes
always_allow_html: yes
bibliography: references.bib
---



# Summary

In this project, we tackle the regression problem of predicting chocolate ratings from a chocolate database containing information such as `Company Location`and `Company (manufacturer)` as well as ingredient specific features such as `Country of Bean Origin` and `Cocoa Percent`. We trained a number of different models on this problem (DummyRegressor, Ridge, and SVR) and determined that the best performing model was SVR which had a MAPE (Mean Absolute Percentage Error) of 0.08. This is a relatively reasonable result, we believe that we can continue this study to obtain lower MAPE before model deployment; and it will enable us to have more confidence in using these results in business settings (food recommendations, supermarkets/cafes that sell chocolates, etc.)

# Introduction

The ultimate goal of this project is to predict chocolate ratings from consumers given information about the manufacturing company, origins of ingredients and taste characteristics. This has important consequences for business use-cases; for example, there are many supermarkets, cafes, dessert shops, or confectionary stores which wish to optimise revenue obtained from chocolate sales. Having a scalable and powerful machine learning model can be immensely useful for such businesses. Such a model can be leveraged to better understand consumer behaviours which enables business owners to make appropriate adjustments to what type of chocolates they should put in their inventories or which ones to target their advertising to consumers.

# Data

The data set used in this project is a chocolate rating with the tasting effectiveness features created by Brady Brelinski and Andrea Brelinski, the directors of Manhattan Chocolate Society posted on the [Flavors of Cacao](http://flavorsofcacao.com/), specifically on this [page](http://flavorsofcacao.com/chocolate_database.html). Each row in the data set represents summary statistics of the chocolate rating(1.0 to 5.0) and the features related to the taste of the chocolate(including the bean origin information, the manufacturer company information and location, the cocoa percentage, ingredients and flavor etc.). The total observations of this data set are 2588, and 9 features with our target column "Rating". There are 87 observations with missing values in the "Ingredients" feature and all other features do not have missing values.

# Model

We trained three different models on the dataset: DummyRegressor, Ridge and SVR. All of these models came from sklearn's [@scikit-learn] default models libraries. The training for all models were done with the same train-test split of 75-25. For both the Ridge and SVR models, we used sklearn's RandomizedSearchCV to find the best model hyperparameters. Throughout this project, we used Python and R programming languages [@Python; @R]. The following Python and R packages also were used to perform the analysis: docopt [@docoptpython], pickle [@van1995python], pandas [@reback2020pandas], numpy [@harris2020array], knitr [@knitr], kableExtra[@kableExtra], and tidyverse[@tidyverse].

Our entire implementation can be found here: <https://github.com/UBC-MDS/chocolate_rating>

# Results & Analysis

We performed a series of EDA on the dataset and found that the memorable characteristics and manufacturer company features were particularly strong predictive power. Below is a histogram of the most memorable characteristics:

<div class="figure" style="text-align: center">
<img src="../results/characteristcs_bar.png" alt="Figure 1.Count of memorable characteristics." width="50%" />
<p class="caption">Figure 1.Count of memorable characteristics.</p>
</div>

This was derived by first splitting the comma-delimited "most memorable characteristics". Cocoa comes out as top flavour while nutty and sweet are the other top two flavours. Note that different reviewers might taste chocolates differently, hence a certain amount of subjectivity must be noted here.

Here is a boxplot of the manufacturing company vs. chocolate rating:

<div class="figure" style="text-align: center">
<img src="../results/company_boxplot.png" alt="Figure 2. Manufaturer vs.chocolate rating." width="50%" />
<p class="caption">Figure 2. Manufaturer vs.chocolate rating.</p>
</div>

From the above graph, we can see although "Soma" has the highest rating mean and the highest rating median, its error bar is wide, which means that its chocolate rating is various. On the contrary, "Smooth Chocolator" are doing better with a slightly lower mean than "Soma", a narrower error bar than Soma, and the same median as 3.75. Therefore, "Smooth Chocolatro" has stable and high chocolate rating.

Our model performance is given in the below table. The evaluation metric we picked for this project is MAPE (Mean Absolute Percentage Error, the smaller the better). The best performing model is the SVR model with a MAPE score of 0.07. Ridge comes next with the MAPE score 0.08:



<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>Table 1. MAPE Scores of 3 Models</caption>
 <thead>
  <tr>
   <th style="text-align:left;"> Model </th>
   <th style="text-align:right;"> MAPE Score </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> DummyRegressor </td>
   <td style="text-align:right;"> 0.1098208 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> SVR </td>
   <td style="text-align:right;"> 0.0798650 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Ridge </td>
   <td style="text-align:right;"> 0.0822302 </td>
  </tr>
</tbody>
</table>

For comparison, we also plot the comparison of the predicted and the true values for both Ridge and SVR models. We can tell that the predication error is smaller for SVR. This corresponds to the numeric results of the MAPE scores.

<div class="figure" style="text-align: center">
<img src="../results/ridge_predict_vs_true.png" alt="Figure 3. Predicted vs.true value (Ridge and SVR)." width="50%" /><img src="../results/svr_predict_vs_true.png" alt="Figure 3. Predicted vs.true value (Ridge and SVR)." width="50%" />
<p class="caption">Figure 3. Predicted vs.true value (Ridge and SVR).</p>
</div>

It is interesting to note the relationships between the models and the informative features we mentioned above. Here is a table of the coefficient importance for the Ridge model. We can see that `raspberry` and `Company_(Manufacturer)_Fruition` have the biggest positive coefficients, meaning adding these two factors will lead to the largest increase in the chocolate rating. This is consistent with what we found in the EDA as the company Fruition has a large median as well as a wide error bar, which indicates that it might produce some extremely good products. At the bottom, `chemical` and `medicinal` have the most negative coefficients. Having these two features will result in a large decrease in the rating score. This is not surprising as the majority do not like chocolates with these two characteristics:

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>Table 2. Ridge Coefficients</caption>
 <thead>
  <tr>
   <th style="text-align:left;"> features </th>
   <th style="text-align:right;"> coefficients </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> raspberry </td>
   <td style="text-align:right;"> 0.2702992 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Company_(Manufacturer)_Fruition </td>
   <td style="text-align:right;"> 0.2533775 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> complex </td>
   <td style="text-align:right;"> 0.2221797 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> long </td>
   <td style="text-align:right;"> 0.2137749 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> balanced </td>
   <td style="text-align:right;"> 0.2088994 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> distinct </td>
   <td style="text-align:right;"> 0.2067235 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Company_(Manufacturer)_Benoit Nihant </td>
   <td style="text-align:right;"> 0.2043493 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> fig </td>
   <td style="text-align:right;"> 0.2010037 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Company_(Manufacturer)_Idilio (Felchlin) </td>
   <td style="text-align:right;"> 0.2007200 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Company_(Manufacturer)_Soma </td>
   <td style="text-align:right;"> 0.2002486 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> pungent </td>
   <td style="text-align:right;"> -0.2459583 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> pastey </td>
   <td style="text-align:right;"> -0.2597173 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> burnt </td>
   <td style="text-align:right;"> -0.2606715 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> this </td>
   <td style="text-align:right;"> -0.2837441 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Company_(Manufacturer)_Cote d' Or (Kraft) </td>
   <td style="text-align:right;"> -0.2837441 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> bitter </td>
   <td style="text-align:right;"> -0.2922230 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> off </td>
   <td style="text-align:right;"> -0.2973282 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> very </td>
   <td style="text-align:right;"> -0.3649972 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> chemical </td>
   <td style="text-align:right;"> -0.3692680 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> medicinal </td>
   <td style="text-align:right;"> -0.3755048 </td>
  </tr>
</tbody>
</table>

# Future Improvements

There are a number of improvements we can make towards this machine learning problem. From the data side of things, the current label distribution is skewed and it may be worthwhile to apply a log-transform to rescale the distribution. In addition, we can examine if the dataset can be improved; for example, could we get more detailed user feedback on chocolates, venue where it was sold, more informative Ingredients column (instead of the current one which we had to drop). 

\
From a features standpoint, we can also explore approaches whether we can employ further feature engineering techniques (for example, feature crosses and feature selection). Another fruitful approach might be to use more sophisticated text embedding techniques such as deep learning ones. On the model's side, we can experiment with more exhaustive hyperparameter tuning and perhaps other model architectures as well (Decision Tree, Neural Networks, etc). Lastly, it may be worthwhile to try out other evaluation metrics in future studies (R2, Mean Squared Error, Root Mean Squared Error) instead of just MAPE; this will give us a more clear picture of how the model performs overall and more guarantees prior to production deployment.

# References
