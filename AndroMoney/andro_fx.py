
import yfinance as yfin




def get_exchange_rate(pair, start, end):
    selected = f'{pair}=X'
    df3 = yfin.download(selected, start, end)
    print(f'{selected} : Complete Getting Data')
    return df3


def return_fx(start, end):
    pairs = ['SGDJPY', 'SGDHKD', 'SGDTHB']
    dat_JPY = get_exchange_rate(pairs[0], start, end)
    dat_HKD = get_exchange_rate(pairs[1], start, end)
    dat_THB = get_exchange_rate(pairs[2], start, end)
    FX = (dat_JPY.iloc[0,3], dat_HKD.iloc[0,3],dat_THB.iloc[0,3])
    return FX
