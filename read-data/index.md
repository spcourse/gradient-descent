# Read Data

We have a CSV file `yearly_avg_temp.csv` containing yearly average minimum and maximum temperatures measured at De Bilt, the Netherlands, from 1901 to 2025. The file looks like this:

    year,avg_TN,avg_TX
    1901,4.58,12.85
    1902,4.14,12.21
    ...

Each row contains a year, the average minimum temperature for that year (`avg_TN`), and the average maximum temperature (`avg_TX`), all separated by commas. Temperatures are in degrees Celsius.

Download the data file here: [yearly_avg_temp.csv](yearly_avg_temp.csv)

## Assignment

Create a file called `read_data.py` that reads `yearly_avg_temp.csv` and stores the data in three lists:

- `years` — the year as an integer
- `avg_tns` — the average minimum temperature as a float
- `avg_txs` — the average maximum temperature as a float

Then find and print the coldest and warmest year for both temperature columns. Use a `for` loop to find the extremes — do not use Python's built-in `min()` or `max()` functions.

### Expected Output

    Coldest year (avg min temp): 1929 (3.63°C)
    Warmest year (avg min temp): 2024 (7.71°C)
    Coldest year (avg max temp): 1963 (11.70°C)
    Warmest year (avg max temp): 2022 (15.96°C)

## Hints

- To read a file in Python, use a `with` block:
- 
        with open("yearly_avg_temp.csv") as f:
            ...

- The first line of the file is a header, you need to skip this line. 
- Split each line on `","` to get the individual values:

        parts = line.split(",")


## Run

    python read_data.py

## Checkpy

    checkpy read_data
