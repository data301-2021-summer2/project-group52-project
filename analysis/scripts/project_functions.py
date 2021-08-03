#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
## Task 2. Method Chaining and writing Python programs (10%)¶






import pandas as pd
import numpy as np


def load_and_process(url_or_path_to_csv_file):
    
    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          [['host_id', 'host_acceptance_rate', 'host_response_rate', 'host_is_superhost',
                     'host_identity_verified', 'latitude', 'longitude', 'property_type', 'room_type',
                      'accommodates', 'bathrooms', 'bathrooms_text', 'bedrooms', 'beds', 'price',
                      'review_scores_rating', 'reviews_per_month']]
                 .dropna(subset=['host_acceptance_rate', 'host_response_rate', 'host_is_superhost',
                            'host_identity_verified', 'review_scores_rating', 'reviews_per_month'])

      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
          .assign(superhost_flag = lambda x: np.where(x.host_is_superhost == 't', 1, 0))
                 .assign(host_identity_verified_flag = lambda x: np.where(x.host_identity_verified == 't', 1, 0))
                 .assign(bathrooms = lambda x: x.bathrooms_text.str.split(' ').str[0])
                 .assign(price = lambda x: x.price.str.split('$').str[1])
                 .drop(columns=['bathrooms_text','host_is_superhost', 'host_identity_verified'])
      )

    # Make sure to return the latest dataframe

    return df2 
    
    
