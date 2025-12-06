
import yfinance as yfin
import time


def get_exchange_rate(pair, start, end):
    selected = f'{pair}=X'
    df3 = yfin.download(selected, start, end)
    print(f'{selected} : Complete Getting Data')
    return df3


def return_fx(start, end):

    try:
        pairs = ['SGDJPY', 'SGDHKD', 'SGDTHB']
        dat_jpy = get_exchange_rate(pairs[0], start, end)
        time.sleep(2)
        dat_hkd = get_exchange_rate(pairs[1], start, end)
        time.sleep(2)
        dat_thb = get_exchange_rate(pairs[2], start, end)
        fx = (dat_jpy.iloc[0,3], dat_hkd.iloc[0,3],dat_thb.iloc[0,3])
        return fx
    except Exception as e:
        print(e)

