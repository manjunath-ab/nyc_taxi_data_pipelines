
import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data(*args, **kwargs):
    df_list=[]
    taxi_dtypes = {
    'VendorID': pd.Int64Dtype(),
    'store_and_fwd_flag': str,
    'RatecodeID': pd.Int64Dtype(),
    'PULocationID': pd.Int64Dtype(),
    'DOLocationID': pd.Int64Dtype(),
    'passenger_count': pd.Int64Dtype(),
    'trip_distance': float,
    'fare_amount': float,
    'extra': float,
    'mta_tax': float,
    'tip_amount': float,
    'tolls_amount': float,
    'ehail_fee': float,
    'improvement_surcharge': float,
    'total_amount': float,
    'payment_type': pd.Int64Dtype(),
    'trip_type': float,
    'congestion_surcharge': float
     }
    parse_dates=['lpep_pickup_datetime','lpep_dropoff_datetime']
    base_url='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020'
    for i in range(10,13):
        #print(i)
        df=pd.read_csv(f'{base_url}-{i}.csv.gz', sep=',',compression='gzip',dtype=taxi_dtypes,parse_dates=parse_dates)
        df_list.append(df)
    complete_df=pd.concat(df_list,ignore_index=True)
    return complete_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
