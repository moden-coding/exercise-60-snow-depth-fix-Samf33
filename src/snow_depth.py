#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    df = pd.read_csv("src/kumpula-weather-2017.csv", index_col=0)
    return df["Snow depth (cm)"].max()

def main():
    result = snow_depth()
    print(f"Max snow depth: {result}")

if __name__ == "__main__":
    main()
