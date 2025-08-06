'''Welcome to your Coderbyte assessment.
You are encouraged to use any resources at your disposal (google, chatgpt, stackoverflow, reddit, etc). An incomplete notebook will result in an automatic fail.
Use pandas or numpy vectorization and avoid for-loops to the best of your ability. Points will be docked wherever for-loops are used. In reality, python for-loops are impractical to use with big data. There are ways to circumvent this. Here is an article discussing the performance difference.
Try and solve the challenges and answer the questions within this assessment to the best of your ability. Good luck!'''

import numpy as np
import pandas as pd
import re

def StockPicker(arr):
    if len(arr) <= 1:
        return -1
    
    arr_np = np.array(arr)
    max_future_prices = np.maximum.accumulate(arr_np[::-1])[::-1]
    profits = max_future_prices - arr_np
    max_profit = np.max(profits)
    
    return max_profit if max_profit > 0 else -1


def evaluate_list(lst):
    result = 0
    current_number = ""
    operation = "+"

    for item in lst:
        if isinstance(item, (int, float)):
            current_number += str(item)
        elif item in ["+", "-"]:
            if current_number:
                if operation == "+":
                    result += int(current_number)
                else:
                    result -= int(current_number)
                current_number = ""
            operation = item

    # Handle the last number
    if current_number:
        if operation == "+":
            result += int(current_number)
        else:
            result -= int(current_number)

    return result

# Example usage
#input_list = [1, 2, 3, '+', 2]
#output = evaluate_list(input_list)
#print(f"Input: {input_list}")
#print(f"Output: {output}")


def num2words(strinput,reverse_hmap):
            series = pd.Series(list(strinput))
            is_negative = series.eq('-')
            series = series.where(~is_negative,'negative')
            result = series.map(reverse_hmap).fillna(series)
            return ''.join(result)


def StringExpression(strParam):


    strParam = "onezeropluseight"
  
    hmap = {"zero":"0","one":"1" , "two":"2", "three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    hmap_operator = {"plus":"+","minus":"-"}
    # reverse_hmap for efficient lookup for function num2words
    reverse_hmap = {v :k for k, v in hmap.items()}

    strOper = ""
    operation = []
    for i in strParam:
      strOper = strOper + str(i)
      if strOper in hmap:
        operation.append(int(hmap[strOper]))
        strOper = ""
      elif strOper in hmap_operator:
        operation.append(hmap_operator[strOper])
      strOper = ""

    print(operation)
    if len(operation)<=1:
      return strParam

    # Convert operation to a Pandas Series for vectorized operations
    operation_series = pd.Series(operation)

    # Identify numeric values and operators
    is_numeric = operation_series.apply(lambda x: isinstance(x, (int, float)))
    is_operator = operation_series.isin(["+", "-"])

    # Create a DataFrame to hold the numeric values and operators
    df = pd.DataFrame({
        'value': operation_series.where(is_numeric).ffill().fillna(0),
        'operator': operation_series.where(is_operator).ffill().fillna("")
    })

    # Calculate cumulative results based on operators
    df['result'] = np.where(df['operator'] == '+', df['value'], -df['value'])
    final_result = df['result'].cumsum().iloc[-1]

    print(final_result)

    print(num2words(str(finalResult),reverse_hmap))
    # code goes here
    return num2words(str(finalResult),reverse_hmap)

# keep this function call here 
print(StringExpression("onezeropluseight"))

operation = [1, "+", 2, "-", 3, 4, "+", 5]

# Convert to a Pandas Series
operation_series = pd.Series(operation)

# Identify numeric values and operators
is_numeric = operation_series.apply(lambda x: isinstance(x, (int, float)))

# Forward-fill numeric values for multi-digit numbers (e.g., "34" is treated as "3" and "4")
numeric_values = operation_series.where(is_numeric).ffill()

# Create a mask for operators
operators = operation_series.where(~is_numeric).fillna("")

# Group by numeric values and their associated operators
df = pd.DataFrame({"value": numeric_values, "operator": operators})

# Convert numeric values to integers
df["value"] = df["value"].astype(int)

# Apply operations based on operators
df["signed_value"] = np.where(
    (df["operator"] == "-"), -df["value"], df["value"]
)

# Sum up all signed values to get the final result
final_result = df["signed_value"].sum()

print(final_result)