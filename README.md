
# Simple Naive Bayes

Simple Naive Bayes is a Python library designed to provide a straightforward implementation of the Naive Bayes classifier for classification tasks. It includes functionalities for dividing datasets, handling missing values, and applying the Naive Bayes algorithm to single elements, columns, or entire tables.

## Installation

You can install Simple Naive Bayes using pip:

```
pip install simpleNaiveBayes
```

## Usage

### Importing Modules

```python
from simpleNaiveBayes import by_strategy
from simpleNaiveBayes.stat_helpers import stat_helpers
from simpleNaiveBayes.simpleNaiveBayes import snb
```

### Initializing the Filling Machine

```python
filling_machine = by_strategy(strategy_dict, table, empty_symbol)
```

- `strategy_dict`: A dictionary containing strategies for handling missing values.
- `table`: The input data table.
- `empty_symbol`: Symbol representing missing values.

### Running the Program

```python
filled_table = filling_machine()
```

This will execute the filling machine according to the specified strategies and return the filled table.

### Example Usage

```python
from simpleNaiveBayes import by_strategy

# Sample strategy dictionary
strategy_dict = {
    "strategy": "one",
    "replacement": "mean",
    "rows": 5,
    "columns": 2,
    "results": False
}

# Sample data table
data_table = [
    [1, 2, 3],
    [4, None, 6],
    [7, 8, 9]
]

# Initialize filling machine
filling_machine = by_strategy(strategy_dict, data_table, None)

# Execute filling machine
filled_table = filling_machine()

print(filled_table)
```

## Features

- **Flexible**: Supports various strategies for handling missing values.
- **Efficient**: Implements the Naive Bayes algorithm efficiently for classification tasks.
- **Customizable**: Allows customization of strategies and parameters for different use cases.

## Contribution

Contributions to Simple Naive Bayes are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request on the [GitHub repository](https://github.com/example/simpleNaiveBayes).

## License

Simple Naive Bayes is licensed under the MIT License. See the [LICENSE](https://github.com/example/simpleNaiveBayes/blob/main/LICENSE) file for details.

## Contact

For any inquiries or support, you can reach out to [author@example.com](mailto:author@example.com).
