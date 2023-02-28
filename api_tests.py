from api.oanda_api import OandaAPI
from infrastructure.instrument_collection import instrumentCollection
import time

if __name__ == '__main__':
    api = OandaAPI()
    instrumentCollection.loadInstruments("./data")
    # trade_id = api.place_trade("EUR_USD", 100, 1)
    # print("Opened:", trade_id)
    # time.sleep(10)
    # print(f"Closing {trade_id}", api.close_trade(trade_id))
    [api.close_trade(x.id) for x in api.get_open_trades()]