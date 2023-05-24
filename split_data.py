import pandas as pd 
import functionSQL as f
from sklearn.model_selection import train_test_split

conn, cursor = f.init()
data = f.extract_all_data(conn, cursor, 'REVIEWS_CLEANED')

train, test = train_test_split(data, test_size=0.1, random_state=32)

f.save_to_csv(train, 'train', 'cleaned', conn, cursor)
f.save_to_csv(test, 'test', 'cleaned', conn, cursor)