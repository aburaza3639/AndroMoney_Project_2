
import yfinance as yfin


def get_exchange_rate(pair, start, end):
    selected = f'{pair}=X'
    df3 = yfin.download(selected, start, end)
    print(f'{selected} : Complete Getting Data')
    return df3


def return_fx(start, end):
    pairs = ['SGDJPY', 'SGDHKD', 'SGDTHB']
    dat_jpy = get_exchange_rate(pairs[0], start, end)
    dat_hkd = get_exchange_rate(pairs[1], start, end)
    dat_thb = get_exchange_rate(pairs[2], start, end)
    fx = (dat_jpy.iloc[0,3], dat_hkd.iloc[0,3],dat_thb.iloc[0,3])
    return fx
