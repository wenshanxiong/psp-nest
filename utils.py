import requests
import logging
from scipy import stats
from datetime import date

PRICE_BY_DATE_URL = "http://wenshan.lol:6969/psp?date={date}"
PRICE_BY_DATE_RANGE_URL = "http://wenshan.lol:6969/psp?start={start_date}&end={end_date}"
DATE_FORMAT = "%Y-%m-%d"


def get_prices_by_date(date: date) -> list:
    date_str = date.strftime(DATE_FORMAT)
    response = requests.get(PRICE_BY_DATE_URL.format(date=date_str))
    if response.status_code != 200:
        logging.error("Failed to fetch price")
        exit()

    price_map = response.json()
    return price_map[date_str]


def get_peak_hours(prices: list, threshold: float = 1.5) -> list:
    z_scores = stats.zscore(prices)
    threshold = 1.5
    outlier_indices = [idx for idx, z_score in enumerate(z_scores) if z_score > threshold]
    return outlier_indices
