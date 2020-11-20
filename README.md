# surfs_up


# Overview of the statistical analysis

# Overview of the statistical analysis

I have done thorough work to analyse the Hawaii climate data. I have used SQLAlchemy, and a Flask API, climate_app.py to pull data from the Hawaii. SQLite weather station tables. 

I used python and notebook for data analysis. Now, the work which is require is to pull temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

# Results:

I have pulled June data from 2010 up to 2018. The total data for June was 1,700 presented in a list.

## June
The temperature pulled are as below in a dataframe, summarizing the results.
- June temperature
![image](Resources/June_Temperature.png)

The mean is 74.9 and the max is 85 with 75% of the data located in the 77 degree which is better for vacations.

I also plot the data to have an idea of temperature fluctuation.

- June plot
![image](Resources/Plot_temp_june.png)

We can see as per the plot , that the temperature are balanced throughout the data set. The split (drop or increase) is not significant. 

- December dataframe
![image](Resources/Dec_Temperature.png)

1,517 count with a mean of 71 and a max of 83 degree, which is in the range of June temperatures.
- Plot December
![image](Resources/Plot_temp_dec.png)

The plot also look similar to June with limited fluctuation from the data analayzed.
Somehow,  december is an appropriate month for ice cream and beach, in Hawaii.

# Summary

As captured above, the temperatures for June and December do not differ much and look similar. With the same statistical outcome, it is considered as better for the summer business. I encouraged Avy in the business.

December, in most of the regions, is a cold momth with some part reaching freezing. However, Hawaii is different. Climate is favourable throughout the year for vacation, beach and ice cream.

The outcome of the data analysis is that the surf and ice cream shop business are sustainable year-round.
