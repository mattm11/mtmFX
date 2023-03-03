from api.oanda_api import OandaAPI
from infrastructure.instrument_collection import instrumentCollection
from stream_example.streamer import run_streamer


if __name__ == '__main__':
    api = OandaAPI()
    instrumentCollection.loadInstruments("./data")
    run_streamer()

