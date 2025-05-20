import os.path
import sys
import csv
import dateutil.parser
import math
from functools import lru_cache
import time

# Global variables
fibCount = 0        # Recursive Fib(n) call counter
cachedFibCount = 0  # Recursive (cached) Fib_Cached(n) call counter

# Main
def main():
    print("Fibonacci Retracement Stock Indicator")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

    print("|","------█------",sep='')
    print("|","---██--█----█","\tNathaniel Kren",sep='')
    print("|","--█--█--█--█-","\tPython: Sample Program",sep='')
    print("|","--█-----███--","\tCS 431 Principles of Programming Languages",sep='')
    print("|","-█-------█---","\tOctober 2020",sep='')
    print("|","█------------","\tVersion: 1.1",sep='')
    print("|","█------------\n",sep='')
    
    print("This program will calculate the Fibonacci sequence using many recursive calls.")
    print("The current system recursion limit is ",sys.getrecursionlimit(),".\n",sep='')

    input("Press the <Enter> key to begin.")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n")

    run = True  # Run program trigger
    found = False
    while(not found):
        ticker = input("Enter stock symbol with existing CSV data (press <Enter> to exit): ")
        # If user does not enter ticker, stop program run
        if ticker == '':
            run = False
            found = True
            continue
        # If user enters ticker, check for data file existence
        filename = str(ticker) + '.csv'
        print("\nAttempting to locate ",ticker,".csv...",sep='',end='')
        if os.path.isfile(filename):
            print ("found!\n")
            found = True
        else:
            print ("not found.\n")

    # If program not set to terminate (no ticker entered)
    if run:
        stockData = parseStockDataCSV(filename)             # Gather quote data
        print("✅ Stock data gathered.\n")

        print("Please enter the number of values in the Fibonacci Sequence to calculate (enter integer only).")
        fibN = int(input("Be cautious of the system's available memory (recursion limit): "))
        print("\nBuilding Fibonacci Sequence to",fibN,"indices...",end='')
        start = time.time()                                 # Begin timer
        Fibonacci = buildFibonacciSequence(fibN,Fib)        # Inefficiently define [fibN] numbers of the Fibonacci Sequence
        end = time.time()                                   # Stop timer
        print("took",fibCount,"recursive calls to Fib(n) and",(end-start),"time to complete.\n")
        print("Fibonacci Sequence:")
        print(Fibonacci)
        print("\n✅ Fibonacci Sequence generated (recursively).\n")

        print("\nBuilding Fibonacci Sequence to",fibN,"indices...",end='')
        start = time.time()                                 # Begin timer
        Fibonacci2 = buildFibonacciSequence(fibN,Fib_Cached)# Build Fibonacci Sequence using a cache
        end = time.time()                                   # Stop timer
        print("took",cachedFibCount,"recursive calls to Fib(n) and",(end-start),"time to complete.\n")
        print("Fibonacci Sequence:")
        print(Fibonacci)
        print("\n✅ Fibonacci Sequence generated (recursively).\n")


        print("Calculating Key Ratios from Fibonacci Sequence...\n")
        keyRatios = [0.0,0.5,1.0]                           # Key Fibonacci Ratios: 100.0%, 61.8%, 50.0%, 38.2%, 23.6%, 0.0%
                                                            # Set the standard ratios (0%, 5%, and 10%) here (theses are Fibonacci ratios,
                                                            # from the first four digits of the sequence: [0, 1, 1, 2])
        keyRatios = calcKeyFibRatios(Fibonacci,keyRatios)   # Calculate Fibonacci Ratios here
        print("Ratios:",keyRatios)
        print("\n✅ Fibonacci Ratios calculated.\n")

        print("Determining minimum and maximum stock prices in data period...\n")
        min, max = findExtremePrices(stockData)             # Find the highest and lowest prices in the data
        print("High:\t$",round(max,2),"\nLow:\t$",round(min,2),"\n",sep='')
        print("✅ Price extrema determined.\n")

        print("Performing Fibonacci Retracement on",ticker,"stock data...\n")
        levels = calcIndicatorLevels(max,min,keyRatios)     # Use high, low, and Fibonacci ratios to calculate indicator levels
        print("Indicator levels:",levels,"\n")
        print("✅ Indicator levels calculated.\n")

        input("Press <Enter> to draw price chart with Fibonacci Retracement.")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n")
        chartStockPrice(max,min,stockData,levels,ticker)    # Display price chart with indicator levels
        input("Complete.  Press <Enter> to terminate program.")
    else:
        print("Exiting...")

# Parse Stock Data CSV File
# Opens CSV stock data file and stores data as a list
def parseStockDataCSV(filename):
    with open(filename) as Stock_Data:
        stockData = list(csv.reader(Stock_Data))
    return stockData

# Returns the (n)th Number in Fibonnacci Sequence, recursively
def Fib(n):
    global fibCount
    fibCount += 1
    if((n == 0) or (n == 1)):
        return n
    else:
        return Fib(n - 1) + Fib(n - 2)

# Returns the (n)th Number in Fibonnacci Sequence, recursively but using a cache
@lru_cache(maxsize = None)
def Fib_Cached(n):
    global cachedFibCount
    cachedFibCount += 1
    if((n == 0) or (n == 1)):
        return n
    else:
        return Fib_Cached(n - 1) + Fib_Cached(n - 2)
    
# Makes inefficient calls to the recursive function Fib(n) to calculate (n) numbers of the Fibonacci Sequence
def buildFibonacciSequence(n,function):
    Fibonacci = []
    for f in range(n):
        Fibonacci.append(function(f))
    return Fibonacci

# Calculates key ratios (Fibonacci ratios)
def calcKeyFibRatios(Fibonacci,ratios):
    fibRatios = [[],[],[]]
    i,a = 0,0

    # Calculate each individual ratio
    while(i < (len(Fibonacci) - 3)):
        fibRatios[0].append(Fibonacci[i] / Fibonacci[i + 1])
        fibRatios[1].append(Fibonacci[i] / Fibonacci[i + 2])
        fibRatios[2].append(Fibonacci[i] / Fibonacci[i + 3])
        i += 1

    # Calculate average ratio
    while(a < len(fibRatios)):
        total = 0
        for r in range(4, len(fibRatios[a])):
            total += fibRatios[a][r]
        ratios.append(round((total / (len(fibRatios[a]) - 4)),3))
        a += 1

    # Sort ratios (ascending)
    ratios.sort()
    
    return ratios

# Find price extreme in quote data (high, low)
def findExtremePrices(quoteData):
    min, max = float(quoteData[1][3]),float(quoteData[1][2])
    low, high = None,None

    # Locate high and low prices in range, start at 2 to eliminate header row and first record (prices set already)
    for pr in range(2,len(quoteData)):
        low = float(quoteData[pr][3])
        high = float(quoteData[pr][2])
        
        if (high >= max):
            max = high
        if (low <= min):
            min = low

    return min,max

# Calculate Fibonnaci Retracement indicator levels
def calcIndicatorLevels(periodHigh,periodLow,ratios):
    diff = periodHigh - periodLow               # Calculate difference between high and low
    levels = []
    for r in ratios:
        levels.append((diff * r) + periodLow)   # Apply ratios and add to lowest price to get real level

    return levels

# Create and draw stock price chart with indicator levels
def chartStockPrice(max,min,quoteData,levels,ticker):
    chart = []                                      # Create chart
    rows = math.ceil(max) - math.floor(min) + 1     # Number of rows equal to price range + 1
    cols = len(quoteData)                           # Number of cols equal to number of record rows in data

    # Create emprt chart with appropriate number of rows and columns
    for r in range(rows):
        chart.append([])
        chart[r].append(math.ceil(max) - r)
        chart[r].append("|")
        for c in range(1,cols):
            chart[r].append(" ")

    # Create x axis
    chart.append(["--","|"])
    row = len(chart) - 1
    for c in range(1,cols):
        date = "[" + str(dateutil.parser.parse(quoteData[c][0]).month) + "-" + str(dateutil.parser.parse(quoteData[c][0]).day) + "]"
        chart[row].append("|")

    # Draw "candlesticks" at appropriate chart locations
    for p in range(1,cols):
        open = round(float(quoteData[p][1]))            # Get open price
        close = round(float(quoteData[p][4]))           # Get close price

        openRow =  math.floor(max) - open + 1           # Find corresponding grid row for open price
        closeRow = math.floor(max) - close + 1          # Find corresponding grid row for close price

        if(openRow > closeRow):                         # If open is greater than close, price moved down
            rng = openRow - closeRow                    # Open - Close to get positive range
            for c in range(rng):                        # Place "candlesticks" through range
                chart[c + closeRow][p+1] = "█"
        elif(closeRow > openRow):                       # If close is greater than open, price moved up
            rng = closeRow - openRow                    # Close - open to get positive range
            for c in range(rng):                        # Place "candelsticks" through range
                chart[c + openRow][p+1] = "█"
        else:                                           # If open and close match, price moved laterally
            chart[closeRow][p+1] = "█"                  # Place "candlestick" at row

    # Draw Fibonnaci Retracement (indicator) lines
    for r in range(len(levels)):
        lvl = round(levels[r])
        lvlRow = math.floor(max) - lvl + 1
        for c in range(len(chart[lvlRow])):             # For each chart cell in currenet indicator level's corresponding row
            if (chart[lvlRow][c] == " "):               # If cell is blank, add indicator line
                chart[lvlRow][c] = "-"
        else:
            chart[lvlRow].append(" " + str(levels[r]))  # Add indicator level at end of line

    print(ticker," [High: ",max,", Low: ",min,"]",sep='')
    print("FibRT: ",levels,"\n",sep='')

    # Draw chart (output to console)
    for r in range(len(chart)):
        for c in range(len(chart[r])):
            print(chart[r][c],end='',sep='')
        print()

# Run program
if __name__ == "__main__":
    main()

