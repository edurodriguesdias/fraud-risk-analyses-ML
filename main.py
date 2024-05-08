import pandas
from ydata_profiling import ProfileReport

data_frame = pandas.read_csv('./data/fraud_dataset_example.csv')

data_frame = data_frame[
    [
        'isFraud',
        'isFlaggedFraud',
        'step',
        'type',
        'amount',
        'nameOrig',
        'oldbalanceOrg',
        'newbalanceOrig',
        'nameDest',
        'oldbalanceDest',
        'newbalanceDest'
    ]
]


def renameColumns(data_frame):
    columnsName = {
        'isFraud': 'fraud',
        'isFlaggedFraud': 'is_potential_fraud',
        'step': 'time',
        'type': 'payment_type',
        'amount': 'value',
        'nameOrig': 'payer',
        'oldbalanceOrg': 'payer_balance',
        'newbalanceOrig': 'payer_balance_updated',
        'nameDest': 'payee',
        'oldbalanceDest': 'payee_balance',
        'newbalanceDest': 'payee_balance_updated',
    }

    return data_frame.rename(columns=columnsName)


data_frame = renameColumns(data_frame)

print("Describe Data Frame", data_frame.describe().T)

print("Show Data Frame Size (Rows x Columns)", data_frame.shape)

print("Show Data Frame Info", data_frame.info())

data_frame.groupby('fraud').time.count()

print("Indicates if Data Frame has null values:", str(data_frame.isnull().values.any()))


profile = ProfileReport(data_frame, title="Fraud Analyses Report")

profile.to_file('./report/report.html')
