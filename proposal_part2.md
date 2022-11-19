Have you ever wondered what makes chocolates taste good? Why do some people prefer dark chocolates and others like white chocolates? When you say you like certain kinds of chocolate, what are the factors that made you think so? Are there any ingredients in the chocolates that you want to avoid? To answer these questions, we decided to perform an analysis based on a dataset of 2,588 chocolate ratings compiled by Brady Brelinsk from Manhattan Chocolate Society. The dataset is available to the public [here](http://flavorsofcacao.com/chocolate_database.html).



We want to create a model using different features provided related to the taste and flavors of the chocolate to predict the ratings. These features include `Manufacturer`, `Country of Bean Origin`, `Cocoa Percent`. Through data wrangling and tuning machine learning models, our end goal is to optimize the model in order to give a relatively accurate prediction of the rating.



We will first obtain a high-level data summary table to examine the number of missing values, and distribution statistics such as frequency, mean for all the features. We need to make sure the number of missing values is within a reasonable range so that it will not affect the EDA. At this stage, we will only replace the missing values with NaN, we may transform these data using `SimpleImputer` to replace them with the most frequent value or the mean based on the results of EDA. To make our dataset concise but also effective for model tuning, we will also create correlation plots in order to explore the correlation between different features. 