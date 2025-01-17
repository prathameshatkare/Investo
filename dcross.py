from sqlalchemy import create_engine
import pandas as pd

# Database connection details
user = "root"
password = "ben123"
host = "localhost"
database = "ap"

# Create SQLAlchemy engine
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")

# Load data using SQLAlchemy engine
data = pd.read_sql("SELECT * FROM ticker_data ORDER BY datetime ASC", engine)

# Parse datetime and set it as an index
data['datetime'] = pd.to_datetime(data['datetime'])
data.set_index('datetime', inplace=True)

# Calculate moving averages
data['short_ma'] = data['close'].rolling(window=10).mean()
data['long_ma'] = data['close'].rolling(window=50).mean()

# Generate signals
data['signal'] = 0
data.loc[data['short_ma'] > data['long_ma'], 'signal'] = 1  # Buy signal
data.loc[data['short_ma'] <= data['long_ma'], 'signal'] = -1  # Sell signal

# Evaluate strategy performance
data['daily_return'] = data['close'].pct_change()
data['strategy_return'] = data['signal'].shift(1) * data['daily_return']

# Fill missing strategy returns and calculate cumulative return
data['strategy_return'].fillna(0, inplace=True)
cumulative_return = (1 + data['strategy_return']).cumprod() - 1

# Print results
if not cumulative_return.empty:
    print("Cumulative Return of Strategy:", cumulative_return.iloc[-1])
else:
    print("No valid data for calculating returns.")
