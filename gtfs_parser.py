# import pandas as pd

# # all gtfs txt files are in csv format

# # parse routes
# routes_df = pd.read_csv('gtfs_data\\routes.txt')

# # get MAX lines information and store in new list
# MAX_LINES = []
# for row in routes_df.itertuples():
#     if 'MAX' in row[4]:
#         tuple(row)
#         MAX_LINES.append(row)

# print(MAX_LINES[1][0])

import gtfs_kit as gk

path = "C:\\Users\\craygoza\\OneDrive - Intel Corporation\\Documents\\Python Scripts\\personal_MAXtrain_tracker\\gtfs.zip"

#Read the feed with gtfs-kit
feed = (gk.read_feed(path, dist_units='km'))

#Search for errors and warnings in the feed
print(feed.validate())