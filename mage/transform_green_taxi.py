if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


def camel_to_snake(df):
    column_mapping = {
    'VendorID': 'vendor_id',
    'store_and_fwd_flag': 'store_and_fwd_flag',
    'RatecodeID': 'ratecode_id',
    'PULocationID': 'pu_location_id',
    'DOLocationID': 'do_location_id',
    'passenger_count': 'passenger_count',
    'trip_distance': 'trip_distance',
    'fare_amount': 'fare_amount',
    'extra': 'extra',
    'mta_tax': 'mta_tax',
    'tip_amount': 'tip_amount',
    'tolls_amount': 'tolls_amount',
    'ehail_fee': 'ehail_fee',
    'improvement_surcharge': 'improvement_surcharge',
    'total_amount': 'total_amount',
    'payment_type': 'payment_type',
    'trip_type': 'trip_type',
    'congestion_surcharge': 'congestion_surcharge',
    'lpep_pickup_datetime':'lpep_pickup_datetime',
    'lpep_dropoff_datetime':'lpep_dropoff_datetime'
}
    df.columns=[column_mapping[col] for col in df.columns]
    return df

@transformer
def transform(data, *args, **kwargs):

    # Specify your transformation logic here
    print("Rows with pcount is 0: ",data['passenger_count'].isin([0]).sum())
    print("Rows with trip_dis is 0: ",data['trip_distance'].isin([0]).sum())
    clean_df=data[(data['passenger_count']>0) & (data['trip_distance']>0)]
    clean_df= camel_to_snake(clean_df)
    clean_df['lpep_pickup_date']=clean_df['lpep_pickup_datetime'].dt.date
    
    print(clean_df.columns)
    return  clean_df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert 'vendor_id' in output.columns, 'Vendor ID is not snake case'
    assert output['passenger_count'].isin([0]).sum() == 0, 'The output has 0 pcounts'
    assert output['trip_distance'].isin([0]).sum() == 0, 'The output has 0 valued trip'