from collections import namedtuple
from enum import Enum


class PredictMethod(Enum):
    """
    The predict method for all of the stan template. Often used are mean and median.
    """
    MAP = 'map'
    MEAN = 'mean'
    MEDIAN = 'median'
    FULL_SAMPLING = 'full'


class PredictionKeys(Enum):
    """
    column names for the data frame of predicted result with decomposed components
    """
    TREND = 'trend'
    SEASONALITY = 'seasonality'
    REGRESSION = 'regression'
    REGRESSOR = 'regressor'
    PREDICTION = 'prediction'


class EstimatorsKeys(Enum):
    """
    alias for all available estimator types when they are called under model wrapper functions
    """
    PyroSVI = 'pyro-svi'
    StanMAP = 'stan-map'
    StanMCMC = 'stan-mcmc'


class TrainingMetaKeys(Enum):
    """
    training meta data dictionary processed under `Forecaster.fit()`
    """
    RESPONSE = 'response'
    DATE_ARRAY = 'date_array'
    DATE_UNIQUE_ARRAY = 'date_unique_array'
    NUM_OF_OBS = 'num_of_obs'
    NUM_OF_STEPS = 'num_of_steps'
    RESPONSE_SD = 'response_sd'
    START = 'training_start'
    END = 'training_end'
    RESPONSE_COL = 'response_col'
    DATE_COL = 'date_col'
    INFER_FREQ = 'infer_freq'
    TIME_DELTA = 'time_delta'


class PredictionMetaKeys(Enum):
    """
    prediction input meta data dictionary processed under `Forecaster.predict()`
    """
    DATE_ARRAY = 'date_array'
    # number of forward steps needed in the forecast region after the end of train period
    # this is purely based on shape of dataframes; not from calculation of date array distances
    FUTURE_STEPS = 'n_forecast_steps'
    START = 'prediction_start'
    END = 'prediction_end'
    START_INDEX = 'start'
    PREDICTION_DF_LEN = 'prediction_length'


class PlotLabels(Enum):
    """
    used in multiple prediction plots
    """
    # Also used in training_actual_response column name.
    TRAINING_ACTUAL_RESPONSE = 'training_actual_response'
    PREDICTED_RESPONSE = 'predicted_response'
    ACTUAL_RESPONSE = 'actual_response'


class TimeSeriesSplitSchemeKeys(Enum):
    """ hash table keys for the dictionary of back-test meta data
    """
    MODEL = 'model'
    TRAIN_START_DATE = 'train_start_date'
    TRAIN_END_DATE = 'train_end_date'
    TRAIN_IDX = 'train_idx'
    TEST_IDX = 'test_idx'
    # split scheme type
    SPLIT_TYPE_EXPANDING = 'expanding'
    SPLIT_TYPE_ROLLING = 'rolling'


class BacktestFitKeys(Enum):
    """ column names of the dataframe used in the output from the backtest.BackTester.fit_predict() or any labels of
    the intermediate variables to generate such outcome dataframe
    """
    # labels for fitting process
    # note that the convention "_prediction" cannot be changed since it is also assumed in
    # all metric functions signature
    ACTUAL = 'actual'
    PREDICTED = 'prediction'
    DATE = 'date'
    SPLIT_KEY = 'split_key'
    TRAIN_FLAG = 'training_data'
    TRAIN_ACTUAL = 'train_actual'
    TRAIN_PREDICTED = 'train_prediction'
    TEST_ACTUAL = 'test_actual'
    TEST_PREDICTED = 'test_prediction'
    # labels for scoring process
    METRIC_VALUES = 'metric_values'
    METRIC_NAME = 'metric_name'
    TRAIN_METRIC_FLAG = 'is_training_metric'


class KTRTimePointPriorKeys(Enum):
    """ hash table keys for the dictionary of back-test aggregation analysis result
    """
    NAME = 'name'
    PRIOR_START_TP_IDX = 'prior_start_tp_idx'
    PRIOR_END_TP_IDX = 'prior_end_tp_idx'
    PRIOR_MEAN = 'prior_mean'
    PRIOR_SD = 'prior_sd'
    PRIOR_REGRESSOR_COL = 'prior_regressor_col'


# Defaults Values
DEFAULT_REGRESSOR_SIGN = '='
DEFAULT_REGRESSOR_BETA = 0
DEFAULT_REGRESSOR_SIGMA = 1.0

# beta coef columns
COEFFICIENT_DF_COLS = namedtuple(
    'coefficients_df_cols',
    ['REGRESSOR', 'REGRESSOR_SIGN', 'COEFFICIENT']
)('regressor', 'regressor_sign', 'coefficient')
