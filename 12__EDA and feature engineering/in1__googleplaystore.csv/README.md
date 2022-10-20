{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3fa6b098",
   "metadata": {},
   "source": [
    "# google-playstore-dataset-EDA"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "738f9621",
   "metadata": {},
   "source": [
    "## About Dataset"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "59a105f9",
   "metadata": {},
   "source": [
    "### Context\n",
    "\n",
    "While many public datasets (on Kaggle and the like) provide Apple App Store data, there are not many counterpart datasets available for Google Play Store apps anywhere on the web. On digging deeper, it was found out that iTunes App Store page deploys a nicely indexed appendix-like structure to allow for simple and easy web scraping. On the other hand, Google Play Store uses sophisticated modern-day techniques (like dynamic page load) using JQuery making scraping more challenging."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4b4da664",
   "metadata": {},
   "source": [
    "## Introduction\n",
    "\n",
    "This project aims at performing Exploratory Data Analysis on the Google-Playstore-Dataset to draw meaningful inferences and what various typical feature engineeirng techniques can be performed that are ought to be performed before any kind of Machine Learning model-building. The idea behind this analysis was to gain a hands-on practice and experiment various pre-processing techniques by the virtue of this dataset."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e2a7923b",
   "metadata": {},
   "source": [
    "## Data description (after data cleaning)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9ef9b82c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 10357 entries, 0 to 10356\n",
      "Data columns (total 13 columns):\n",
      " #   Column          Non-Null Count  Dtype  \n",
      "---  ------          --------------  -----  \n",
      " 0   App             10357 non-null  object \n",
      " 1   Category        10357 non-null  object \n",
      " 2   Rating          8892 non-null   float64\n",
      " 3   Reviews         10357 non-null  float64\n",
      " 4   Size (in MB)    8831 non-null   float64\n",
      " 5   Installs        10357 non-null  int64  \n",
      " 6   Type            10356 non-null  object \n",
      " 7   Price (in $)    10357 non-null  float64\n",
      " 8   Content Rating  10357 non-null  object \n",
      " 9   Genres          10357 non-null  object \n",
      " 10  Last Updated    10357 non-null  object \n",
      " 11  Current Ver     10349 non-null  object \n",
      " 12  Android Ver     10355 non-null  object \n",
      "dtypes: float64(4), int64(1), object(8)\n",
      "memory usage: 1.0+ MB\n"
     ]
    }
   ],
   "source": [
    "playstore.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6ae71922",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "ROBLOX                                           9\n",
       "8 Ball Pool                                      7\n",
       "Bubble Shooter                                   6\n",
       "Helix Jump                                       6\n",
       "Zombie Catchers                                  6\n",
       "                                                ..\n",
       "Popsicle Launcher for Android P 9.0 launcher     1\n",
       "PixelLab - Text on pictures                      1\n",
       "P Launcher for Android™ 9.0                      1\n",
       "Pacify (Android P theme) - Theme for Xperia™     1\n",
       "iHoroscope - 2018 Daily Horoscope & Astrology    1\n",
       "Name: App, Length: 9659, dtype: int64"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "playstore['App'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e8ccf954",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "FAMILY                 1943\n",
       "GAME                   1121\n",
       "TOOLS                   843\n",
       "BUSINESS                427\n",
       "MEDICAL                 408\n",
       "PRODUCTIVITY            407\n",
       "PERSONALIZATION         388\n",
       "LIFESTYLE               373\n",
       "COMMUNICATION           366\n",
       "FINANCE                 360\n",
       "SPORTS                  351\n",
       "PHOTOGRAPHY             322\n",
       "HEALTH_AND_FITNESS      306\n",
       "SOCIAL                  280\n",
       "NEWS_AND_MAGAZINES      264\n",
       "TRAVEL_AND_LOCAL        237\n",
       "BOOKS_AND_REFERENCE     230\n",
       "SHOPPING                224\n",
       "DATING                  196\n",
       "VIDEO_PLAYERS           175\n",
       "MAPS_AND_NAVIGATION     137\n",
       "EDUCATION               130\n",
       "FOOD_AND_DRINK          124\n",
       "ENTERTAINMENT           111\n",
       "AUTO_AND_VEHICLES        85\n",
       "LIBRARIES_AND_DEMO       85\n",
       "WEATHER                  82\n",
       "HOUSE_AND_HOME           80\n",
       "ART_AND_DESIGN           65\n",
       "EVENTS                   64\n",
       "PARENTING                60\n",
       "COMICS                   60\n",
       "BEAUTY                   53\n",
       "Name: Category, dtype: int64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "playstore['Category'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3796d1a8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['App', 'Category', 'Rating', 'Reviews', 'Size (in MB)', 'Installs',\n",
       "       'Type', 'Price (in $)', 'Content Rating', 'Genres', 'Last Updated',\n",
       "       'Current Ver', 'Android Ver'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "playstore.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "e5612e12",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Free    9591\n",
       "Paid     765\n",
       "Name: Type, dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "playstore['Type'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "57075223",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Everyone           8382\n",
       "Teen               1146\n",
       "Mature 17+          447\n",
       "Everyone 10+        377\n",
       "Adults only 18+       3\n",
       "Unrated               2\n",
       "Name: Content Rating, dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "playstore['Content Rating'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ccb9469a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Tools                                842\n",
       "Entertainment                        588\n",
       "Education                            527\n",
       "Business                             427\n",
       "Medical                              408\n",
       "                                    ... \n",
       "Parenting;Brain Games                  1\n",
       "Travel & Local;Action & Adventure      1\n",
       "Lifestyle;Pretend Play                 1\n",
       "Tools;Education                        1\n",
       "Strategy;Creativity                    1\n",
       "Name: Genres, Length: 119, dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "playstore['Genres'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "00e36e70",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Rating</th>\n",
       "      <th>Reviews</th>\n",
       "      <th>Size (in MB)</th>\n",
       "      <th>Installs</th>\n",
       "      <th>Price (in $)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>8892.000000</td>\n",
       "      <td>1.035700e+04</td>\n",
       "      <td>8831.000000</td>\n",
       "      <td>1.035700e+04</td>\n",
       "      <td>10357.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>4.187877</td>\n",
       "      <td>4.059046e+05</td>\n",
       "      <td>21.287413</td>\n",
       "      <td>1.415776e+07</td>\n",
       "      <td>1.030800</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.522377</td>\n",
       "      <td>2.696778e+06</td>\n",
       "      <td>22.540591</td>\n",
       "      <td>8.023955e+07</td>\n",
       "      <td>16.278625</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>0.008301</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>4.000000</td>\n",
       "      <td>3.200000e+01</td>\n",
       "      <td>4.700000</td>\n",
       "      <td>1.000000e+03</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>4.300000</td>\n",
       "      <td>1.680000e+03</td>\n",
       "      <td>13.000000</td>\n",
       "      <td>1.000000e+05</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>4.500000</td>\n",
       "      <td>4.641600e+04</td>\n",
       "      <td>29.000000</td>\n",
       "      <td>1.000000e+06</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>5.000000</td>\n",
       "      <td>7.815831e+07</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>1.000000e+09</td>\n",
       "      <td>400.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Rating       Reviews  Size (in MB)      Installs  Price (in $)\n",
       "count  8892.000000  1.035700e+04   8831.000000  1.035700e+04  10357.000000\n",
       "mean      4.187877  4.059046e+05     21.287413  1.415776e+07      1.030800\n",
       "std       0.522377  2.696778e+06     22.540591  8.023955e+07     16.278625\n",
       "min       1.000000  0.000000e+00      0.008301  0.000000e+00      0.000000\n",
       "25%       4.000000  3.200000e+01      4.700000  1.000000e+03      0.000000\n",
       "50%       4.300000  1.680000e+03     13.000000  1.000000e+05      0.000000\n",
       "75%       4.500000  4.641600e+04     29.000000  1.000000e+06      0.000000\n",
       "max       5.000000  7.815831e+07    100.000000  1.000000e+09    400.000000"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "playstore.describe()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
