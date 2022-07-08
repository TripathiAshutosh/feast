from feast import Entity, Feature,Field, FeatureView, FileSource, ValueType
from feast.types import Float64, Int64
from datetime import timedelta

# Declaring an entity for the dataset
patient = Entity(
    name="patient_id", 
    value_type=ValueType.INT64, 
    description="The ID of the patient")

# Declaring the source of the first set of features
f_source1 = FileSource(
    path=r"data/predictors_df.parquet",
    event_timestamp_column="event_timestamp",
)

# Defining the first set of features
df1_fv = FeatureView(
    name="predictors_df_feature_view",
    ttl=timedelta(seconds=86400 * 1),
    entities=["patient_id"],
    schema=[
        Field(name="Pregnancies", dtype=Int64),
        Field(name="Glucose", dtype=Int64),
        Field(name="BloodPressure", dtype=Int64),
        Field(name="SkinThickness", dtype=Int64),
        Field(name="Insulin", dtype=Int64),
        Field(name="BMI", dtype=Float64),
        Field(name="DiabetesPedigreeFunction", dtype=Float64),
        Field(name="Age", dtype=Int64),
        ],
    source=f_source1,
    online = True,
    tags={},
)

# Declaring the source of the targets
target_source = FileSource(
    path=r"data/target_df.parquet", 
    created_timestamp_column="event_timestamp",
    
)

# Defining the targets
target_fv = FeatureView(
    name="target_feature_view",
    entities=["patient_id"],
    ttl=timedelta(seconds=86400 * 1),
    schema=[
        Field(name="Outcome", dtype=Int64)        
        ],    
    source=target_source,
    online = True,
    tags={},
)