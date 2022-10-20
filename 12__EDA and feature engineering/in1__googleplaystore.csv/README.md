# google-playstore-dataset-EDA

## About Dataset

### Context

While many public datasets (on Kaggle and the like) provide Apple App Store data, there are not many counterpart datasets available for Google Play Store apps anywhere on the web. On digging deeper, it was found out that iTunes App Store page deploys a nicely indexed appendix-like structure to allow for simple and easy web scraping. On the other hand, Google Play Store uses sophisticated modern-day techniques (like dynamic page load) using JQuery making scraping more challenging.

## Introduction

This project aims at performing Exploratory Data Analysis on the Google-Playstore-Dataset to draw meaningful inferences and what various typical feature engineeirng techniques can be performed that are ought to be performed before any kind of Machine Learning model-building. The idea behind this analysis was to gain a hands-on practice and experiment various pre-processing techniques by the virtue of this dataset.

## Data description (after data cleaning)


```python
playstore.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 10357 entries, 0 to 10356
    Data columns (total 13 columns):
     #   Column          Non-Null Count  Dtype  
    ---  ------          --------------  -----  
     0   App             10357 non-null  object 
     1   Category        10357 non-null  object 
     2   Rating          8892 non-null   float64
     3   Reviews         10357 non-null  float64
     4   Size (in MB)    8831 non-null   float64
     5   Installs        10357 non-null  int64  
     6   Type            10356 non-null  object 
     7   Price (in $)    10357 non-null  float64
     8   Content Rating  10357 non-null  object 
     9   Genres          10357 non-null  object 
     10  Last Updated    10357 non-null  object 
     11  Current Ver     10349 non-null  object 
     12  Android Ver     10355 non-null  object 
    dtypes: float64(4), int64(1), object(8)
    memory usage: 1.0+ MB
    


```python
playstore['App'].value_counts()
```




    ROBLOX                                           9
    8 Ball Pool                                      7
    Bubble Shooter                                   6
    Helix Jump                                       6
    Zombie Catchers                                  6
                                                    ..
    Popsicle Launcher for Android P 9.0 launcher     1
    PixelLab - Text on pictures                      1
    P Launcher for Android™ 9.0                      1
    Pacify (Android P theme) - Theme for Xperia™     1
    iHoroscope - 2018 Daily Horoscope & Astrology    1
    Name: App, Length: 9659, dtype: int64




```python
playstore['Category'].value_counts()
```




    FAMILY                 1943
    GAME                   1121
    TOOLS                   843
    BUSINESS                427
    MEDICAL                 408
    PRODUCTIVITY            407
    PERSONALIZATION         388
    LIFESTYLE               373
    COMMUNICATION           366
    FINANCE                 360
    SPORTS                  351
    PHOTOGRAPHY             322
    HEALTH_AND_FITNESS      306
    SOCIAL                  280
    NEWS_AND_MAGAZINES      264
    TRAVEL_AND_LOCAL        237
    BOOKS_AND_REFERENCE     230
    SHOPPING                224
    DATING                  196
    VIDEO_PLAYERS           175
    MAPS_AND_NAVIGATION     137
    EDUCATION               130
    FOOD_AND_DRINK          124
    ENTERTAINMENT           111
    AUTO_AND_VEHICLES        85
    LIBRARIES_AND_DEMO       85
    WEATHER                  82
    HOUSE_AND_HOME           80
    ART_AND_DESIGN           65
    EVENTS                   64
    PARENTING                60
    COMICS                   60
    BEAUTY                   53
    Name: Category, dtype: int64




```python
playstore.columns
```




    Index(['App', 'Category', 'Rating', 'Reviews', 'Size (in MB)', 'Installs',
           'Type', 'Price (in $)', 'Content Rating', 'Genres', 'Last Updated',
           'Current Ver', 'Android Ver'],
          dtype='object')




```python
playstore['Type'].value_counts()
```




    Free    9591
    Paid     765
    Name: Type, dtype: int64




```python
playstore['Content Rating'].value_counts()
```




    Everyone           8382
    Teen               1146
    Mature 17+          447
    Everyone 10+        377
    Adults only 18+       3
    Unrated               2
    Name: Content Rating, dtype: int64




```python
playstore['Genres'].value_counts()
```




    Tools                                842
    Entertainment                        588
    Education                            527
    Business                             427
    Medical                              408
                                        ... 
    Parenting;Brain Games                  1
    Travel & Local;Action & Adventure      1
    Lifestyle;Pretend Play                 1
    Tools;Education                        1
    Strategy;Creativity                    1
    Name: Genres, Length: 119, dtype: int64




```python
playstore.describe()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rating</th>
      <th>Reviews</th>
      <th>Size (in MB)</th>
      <th>Installs</th>
      <th>Price (in $)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>8892.000000</td>
      <td>1.035700e+04</td>
      <td>8831.000000</td>
      <td>1.035700e+04</td>
      <td>10357.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>4.187877</td>
      <td>4.059046e+05</td>
      <td>21.287413</td>
      <td>1.415776e+07</td>
      <td>1.030800</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.522377</td>
      <td>2.696778e+06</td>
      <td>22.540591</td>
      <td>8.023955e+07</td>
      <td>16.278625</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>0.000000e+00</td>
      <td>0.008301</td>
      <td>0.000000e+00</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>4.000000</td>
      <td>3.200000e+01</td>
      <td>4.700000</td>
      <td>1.000000e+03</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>4.300000</td>
      <td>1.680000e+03</td>
      <td>13.000000</td>
      <td>1.000000e+05</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>4.500000</td>
      <td>4.641600e+04</td>
      <td>29.000000</td>
      <td>1.000000e+06</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>5.000000</td>
      <td>7.815831e+07</td>
      <td>100.000000</td>
      <td>1.000000e+09</td>
      <td>400.000000</td>
    </tr>
  </tbody>
</table>
</div>


