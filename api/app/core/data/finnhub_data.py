import json, requests, datetime, pytz
from core.data.api_urls import FINNHUB_CANDLE_URL
from core.data.api_keys import FINNHUB_KEY

def datetime_to_unix(date_time):
	"""Convert datetime object to unix timestamp"""
	start_time = pytz.utc.localize(datetime.datetime(1970,1,1))
	return int((date_time-start_time).total_seconds())

def unix_to_datetime(unix_time):
	"""Convert unix timestamp to datetime object"""
	return pytz.utc.localize(datetime.datetime.fromtimestamp(unix_time))

def get_data_fh(ticker, time_from, time_to, resolution):
    """Get historical daily data from world trading data api"""
    params = {
    	'symbol': ticker,
    	'to': datetime_to_unix(time_to),
    	'from': datetime_to_unix(time_from),
    	'resolution': resolution,
    	'token': FINNHUB_KEY
    }
    try:
        res = requests.get(url=f"""{FINNHUB_CANDLE_URL}""", params=params)
    except:
        return None

    if res.status_code == 200:
        return json.loads(res.text)
    else:
        return None


def format_data(data):
	"""Change the format of the candle data to timestamped list of dicts"""
	formatted_data = []
	for index in range(len(data['t'])):
		formatted_data.append({
			'time_stamp': unix_to_datetime(data['t'][index]),
			'close_price': data['c'][index],
			'open_price': data['o'][index] ,
			'high_price': data['h'][index],
			'low_price': data['l'][index],
			'volume': data['v'][index]
		})	
		index+=1
	return formatted_data


def get_data(ticker, *args):
	"""get data from finnhub api and return"""
	data = get_data_fh(ticker, *args)
	return format_data(data)