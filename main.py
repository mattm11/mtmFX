from api.oanda_api import OandaAPI
from infrastructure.instrument_collection import instrumentCollection

if __name__ == '__main__':
    api = OandaAPI()

    instrumentCollection.createFile(api.get_account_instruments(), "./data")
    instrumentCollection.loadInstruments("./data")
    instrumentCollection.printInstruments()
