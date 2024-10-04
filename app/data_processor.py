import pandas as pd

def process_data(data):
    df = pd.DataFrame(data)
    return df.describe()

def main():
    data = {'age': [23, 29, 21, 18], 'height':[165, 170, 174, 168]}
    result = process_data(data)
    print(result)

if __name__=='__main__':
    main()