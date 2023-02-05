import pandas as pd
from home_bot.help_files.help_usefull_func import pairs_found

# df = pd.DataFrame({'name': ['Earth', 'Moon', 'Mars', 'Sun'], 'mass_to_earth': [1, 0.606, 0.107, 12]})
# df.index = ['Row_1', 'Row_2', 'Row_3', 'Row_4']
# print(df)

def table_maker(f1: str, length_of_pair: int, f2: list):
    dict_for_df = {}
    pairs = pairs_found(f1, length_of_pair)
    start = 0
    stop = len(pairs)
    for i in pairs:
        dict_for_df[i] = f2[start:stop]
        start += len(pairs) - 1
        stop += len(pairs) - 1

    data_frame = pd.DataFrame(dict_for_df)
    data_frame.index = pairs

    return data_frame


