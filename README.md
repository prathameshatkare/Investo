# Investo



# Trading Strategy Implementation

This project implements a Moving Average Crossover trading strategy using historical stock data. The implementation includes database setup, data processing, strategy implementation, and testing.

## Prerequisites

- MySQL or PostgreSQL database
- Python 3.x
- Required Python packages:
  - pandas
  - mysql-connector-python
  - unittest

## Project Structure

```
├── sql/
│   └── create_table.sql       # Database table creation script
├── src/
│   ├── data_insertion.py      # Script to load data into database
│   ├── strategy.py            # Moving average crossover implementation
│   └── test_strategy.py       # Unit tests
└── data/
    └── HINDALCO_1D.xlsx      # Input data file
```

## Installation & Setup

1. Install required Python packages:
```bash
pip install pandas mysql-connector-python
```

2. Create the database table using the provided SQL script:
```sql
CREATE TABLE ticker_data (
    datetime DATETIME PRIMARY KEY,
    close DECIMAL(10, 2),
    high DECIMAL(10, 2),
    low DECIMAL(10, 2),
    open DECIMAL(10, 2),
    volume INT,
    instrument VARCHAR(50)
);
```

## Implementation Steps

### 1. Database Setup
- Choose between MySQL or PostgreSQL
- Create the database and table using the provided SQL script
- Test database connection using the Python connector

### 2. Data Insertion
- Load data from Excel file
- Insert records into the database
- Validate data insertion

### 3. Trading Strategy
The implementation uses a Moving Average Crossover strategy with:
- Short-term MA: 10 days
- Long-term MA: 50 days

Trading signals:
- Buy: Short-term MA crosses above Long-term MA
- Sell: Short-term MA crosses below Long-term MA

### 4. Testing
Unit tests cover:
- Data validation
  - Column existence
  - Data type verification
- Strategy validation
  - Signal generation
  - Return calculation

## Usage

1. Set up the database:
```python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)
```

2. Insert data:
```python
# Load and insert data
python src/data_insertion.py
```

3. Run the strategy:
```python
# Execute strategy and generate results
python src/strategy.py
```

4. Run tests:
```python
# Execute all unit tests
python -m unittest src/test_strategy.py
```

## Results

The strategy performance can be evaluated using:
- Cumulative returns
- Performance charts
- Trading signals generated

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/enhancement`)
3. Commit your changes (`git commit -m 'Add enhancement'`)
4. Push to the branch (`git push origin feature/enhancement`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
