from download_data import read_harps_with_noaa
import pandas as pd

def add_label(row):
    if row['HARPNUM'] in harps_with_noaa_df['HARPNUM']:
        return 1
    else:
        return 0

if __name__=="__main__":

    url ="http://jsoc.stanford.edu/doc/data/hmi/harpnum_to_noaa/all_harps_with_noaa_ars.txt"
    harps_with_noaa_df = read_harps_with_noaa(url)

    sharp_df = pd.read_csv('combined_sharp_lorentz.csv')

    sharp_df['label'] = sharp_df.apply(add_label, axis=1)
    sharp_df.to_csv('combined_sharp_lorentz_labeled.csv', index=False)
