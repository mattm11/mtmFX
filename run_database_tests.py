from api.oanda_api import OandaAPI
from infrastructure.instrument_collection import instrumentCollection
from stream_example.streamer import run_streamer
from db.db import DataDB

def db_tests():
    d = DataDB()

    # d.add_one(DataDB.SAMPLE_COLL, dict(age=12, name='gandalf', street='shire'))
    # print(d.query_single(DataDB.SAMPLE_COLL, age=12))
    print(d.query_distinct(DataDB.SAMPLE_COLL, 'age'))

        

if __name__ == '__main__':
    api = OandaAPI()
    # instrumentCollection.loadInstruments("./data")
    # instrumentCollection.createDB(api.get_account_instruments())

    instrumentCollection.loadInstrumentsDB()
    print(instrumentCollection.instruments_dict)

    # run_streamer()
    # d = DataDB()
    # d.test_connection()
    # db_tests()
