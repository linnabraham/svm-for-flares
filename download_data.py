import drms
import pandas as pd

def read_harps_with_noaa(url):
    df = pd.read_csv(url, delim_whitespace=True)
    df = df.assign(NOAA_ARS=df['NOAA_ARS'].str.split(',')).explode('NOAA_ARS').reset_index(drop=True)
    df['NOAA_ARS'] = df['NOAA_ARS'].astype(int)
    return df

def show_keywords_hmi_sharp():
    c = drms.Client()
    si = c.info("hmi.sharp_720s")

    print("Keywords in SHARP 720s")
    for keyword in si.keywords.index:
        print(keyword)
    sharp_cea_720 = c.info("hmi.sharp_cea_720s")
    print("Keywords in SHARP CEA 720s")
    for keyword in sharp_cea_720.keywords.index:
        print(keyword)

if __name__=="__main__":

    url ="http://jsoc.stanford.edu/doc/data/hmi/harpnum_to_noaa/all_harps_with_noaa_ars.txt"
    harps_with_noaa_df = read_harps_with_noaa(url)

    c = drms.Client()
    keys = c.query('hmi.sharp_cea_720s[][2019.01.01 - 2019.05.01]', key='T_REC,HARPNUM, TOTPOT, MEANPOT, R_VALUE,TOTUSJH')
    print(keys)
