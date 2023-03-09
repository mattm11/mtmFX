from scraping.dailyfx_com import dailyfx_com
from scraping.investing_com import get_pair, investing_com
from scraping.bloomberg_com import bloomberg_com
from scraping.fx_calendar import fx_calendar, get_fx_calendar

from dateutil import parser

if __name__ == "__main__":
    print("\ndailyfx_com()")
    print(dailyfx_com())

    print("\ninvesting_com()")
    print(get_pair("EUR_USD", "H1"))

    print("\nbloomberg_com")
    print(bloomberg_com())

    print("\nfx_calendar")
    print(get_fx_calendar(parser.parse("2023-02-28 00:00:00")))