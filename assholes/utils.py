def read_excel(file_path):
    """
    Load data from an Excel file into a pandas DataFrame.
    
    Parameters:
    - file_path: str, path to the Excel file.
    
    Returns:
    - DataFrame containing the loaded data.
    """
    import pandas as pd
    return pd.read_excel(file_path)

def create_pie(file_path, categories_column, values_column, title=''):
    """
    Create and display a pie chart from Excel data.
    
    Parameters:
    - file_path: str, path to the Excel file.
    - categories_column: str, name of the column containing category labels.
    - values_column: str, name of the column containing the values for each category.
    - title: str, title of the pie chart.
    """
    import pandas as pd
    import matplotlib.pyplot as plt

    # Use the existing function to read data from Excel
    data = read_excel(file_path)

    # Extract categories and values based on provided column names
    categories = data[categories_column]
    values = data[values_column]

    # Create the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=categories, autopct='%1.1f%%')
    plt.title(title)
    plt.show()
    
    #BARCHART

def create_bar(file_path, category_column, value_column, title=''):
    """
    Create and display a bar chart from Excel data.
    """
    import pandas as pd
    import matplotlib.pyplot as plt
    """""
    Parameters:
    - file_path: str, path to the Excel file.
    - category_column: str, name of the column containing category labels.
    - value_column: str, name of the column containing the values for each category.
    - title: str, title of the bar chart.
    """
    # Load the dataset
    data = pd.read_excel(file_path)
    
    # Plotting the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(data[category_column], data[value_column], color='skyblue')
    plt.xlabel(category_column)
    plt.ylabel(value_column)
    plt.title(title)
    plt.xticks(rotation=45)  # Rotate category labels for better readability
    plt.tight_layout()  # Adjust layout to not cut off labels
    plt.show()

    #HISTOGRAM

def create_histogram(file_path, column, bins=10, title=''):
    import pandas as pd
    import matplotlib.pyplot as plt
    """
    Create and display a histogram from a specified column in an Excel file.

    Parameters:
    - file_path: str, path to the Excel file.
    - column: str, name of the column to create the histogram for.
    - bins: int, number of bins for the histogram.
    - title: str, optional title for the histogram.
    """
    # Load the dataset
    data = pd.read_excel(file_path)
    
    
    # Plotting the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(data[column].dropna(), bins=bins, color='skyblue', edgecolor='black')
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()


   #CURVEDIAGRAM
def create_curvediagram(file_path, x_column, y_column, title='', xlabel='', ylabel=''):
    import pandas as pd
    import matplotlib.pyplot as plt
    """
    Create and display a curve diagram (line plot) from Excel data.

    Parameters:
    - file_path: str, path to the Excel file.
    - x_column: str, name of the column to use for x-axis values.
    - y_column: str, name of the column to use for y-axis values.
    - title: str, title of the curve diagram.
    - xlabel: str, label for the x-axis.
    - ylabel: str, label for the y-axis.
    """
    # Load the dataset
    data = pd.read_excel(file_path)
    
    # Plotting the curve diagram
    plt.figure(figsize=(10, 6))
    plt.plot(data[x_column], data[y_column], marker='o', linestyle='-', color='b')
    plt.title(title)
    plt.xlabel(xlabel if xlabel else x_column)
    plt.ylabel(ylabel if ylabel else y_column)
    plt.grid(True)
    plt.tight_layout()  # Adjust layout to not cut off labels
    plt.show()

    #SCATTERPLOT
def create_scatterplot(file_path, x_column, y_column, title='', xlabel='', ylabel=''):
    import pandas as pd
    import matplotlib.pyplot as plt
    """
    Create and display a scatter plot from Excel data.

    Parameters:
    - file_path: str, path to the Excel file.
    - x_column: str, name of the column to use for x-axis values.
    - y_column: str, name of the column to use for y-axis values.
    - title: str, title of the scatter plot.
    - xlabel: str, label for the x-axis.
    - ylabel: str, label for the y-axis.
    """
    # Load the dataset
    data = pd.read_excel(file_path)
    
    # Create the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data[x_column], data[y_column], alpha=0.5)
    plt.title(title)
    plt.xlabel(xlabel if xlabel else x_column)
    plt.ylabel(ylabel if ylabel else y_column)
    plt.grid(True)
    plt.show()


    #Statistics CALCLULATION

def cal_statistics(file_path, column):
    import pandas as pd

    # Load the dataset
    data = pd.read_excel(file_path)
    
    # Ensure the column exists
    if column not in data.columns:
        raise ValueError(f"Column '{column}' not found in the Excel file.")
    
    # Calculating the mean of the specified column
    mean = data[column].mean()
    
    # Calculating the median of the specified column
    median = data[column].median()
    
    # Calculating the mode of the specified column
    # The mode() method returns a Series, so we use .iloc[0] to get the first mode value if exists
    mode_series = data[column].mode()
    mode = mode_series.iloc[0] if not mode_series.empty else None
    
    # Return the results in a dictionary
    return {
        "mean": mean,
        "median": median,
        "mode": mode
    }

    

   #VARIANCE AND STANDARD DEVIATION
def cal_variance_std(file_path, column):
    import pandas as pd
    """
    Calculate and return the variance and standard deviation for a specified column in an Excel file.

    Parameters:
    - file_path: str, path to the Excel file.
    - column: str, name of the column to calculate statistics for.

    Returns:
    - A dictionary containing the variance and standard deviation of the specified column.
    """
    # Load the dataset
    data = pd.read_excel(file_path)
    
    # Ensure the column exists
    if column not in data.columns:
        raise ValueError(f"Column '{column}' not found in the Excel file.")
    
    # Calculate variance and standard deviation
    variance_result = data[column].var()
    std_dev_result = data[column].std()
    
    # Return the results in a dictionary
    return {
        "variance": variance_result,
        "standard deviation": std_dev_result
    }
    print("Variance",variance_result)
    print("Standard Deviation", std_dev_result )

    #QUATERTIELS

def cal_quartiles(file_path, column):
    import pandas as pd
    """
    Calculate and return the quartiles for a specified column in an Excel file.

    Parameters:
    - file_path: str, path to the Excel file.
    - column: str, name of the column to calculate quartiles for.

    Returns:
    - A dictionary containing the first, second (median), and third quartiles of the specified column.
    """
    # Load the dataset
    data = pd.read_excel(file_path)
    
    # Ensure the column exists
    if column not in data.columns:
        raise ValueError(f"Column '{column}' not found in the Excel file.")
    
    # Calculate quartiles
    first_quartile = data[column].quantile(0.25)
    second_quartile = data[column].quantile(0.5)  # This is also the median
    third_quartile = data[column].quantile(0.75)
    
    # Return the results in a dictionary
    return {
        "first quartile (Q1)": first_quartile,
        "second quartile (Q2) / median": second_quartile,
        "third quartile (Q3)": third_quartile
    }

    # Covariance + r + r2 + Trend Line

def cal_statistics_relationship(file_path, column_x, column_y):
    import pandas as pd
    import numpy as np
    import scipy.stats
    """
    Calculate covariance, correlation coefficient, coefficient of determination,
    and regression line equation for two variables in an Excel file.

    Parameters:
    - file_path: str, path to the Excel file.
    - column_x: str, name of the first variable/column.
    - column_y: str, name of the second variable/column.

    Returns:
    - A dictionary containing the calculated statistics and regression line equation.
    """
    # Load the dataset
    data = pd.read_excel(file_path)
    
    # Ensure both columns exist
    if column_x not in data.columns or column_y not in data.columns:
        raise ValueError(f"One or both specified columns ('{column_x}', '{column_y}') not found in the Excel file.")
    
    # Extract columns
    x = data[column_x]
    y = data[column_y]
    
    # Calculate covariance
    covariance = np.cov(x, y)[0][1]
    
    # Calculate correlation coefficient
    correlation_coefficient, _ = scipy.stats.pearsonr(x, y)
    
    # Coefficient of determination (r²)
    coefficient_of_determination = correlation_coefficient ** 2
    
    # Calculate regression (trend line)
    slope, intercept = np.polyfit(x, y, 1)
    trend_line_eq = f"y = {slope}x + {intercept}"
    
    return {
        "covariance": covariance,
        "correlation_coefficient (r)": correlation_coefficient,
        "coefficient_of_determination (r²)": coefficient_of_determination,
        "trend_line_equation": trend_line_eq
    }

def create_binomial_distribution(n, p, title=''):
    import numpy as np
    import matplotlib.pyplot as plt
    """
    Calculate and visualize a binomial distribution.

    Parameters:
    - n: int, number of trials.
    - p: float, probability of success in each trial.
    - title: str, title of the plot.
    """
    # Calculate binomial distribution
    x = np.arange(0, n+1)
    y = np.random.binomial(n, p, size=10000)
    
    # Plotting the histogram of the sample
    plt.figure(figsize=(10, 6))
    plt.hist(y, bins=x, density=True, alpha=0.7, color='skyblue', edgecolor='black')
    
    # Plot details
    plt.title(title if title else f'Binomial Distribution n={n}, p={p}')
    plt.xlabel('Number of Successes')
    plt.ylabel('Probability')
    plt.xticks(x)
    plt.grid(axis='y', alpha=0.75)
    
    plt.show()

def create_histogram_with_statistics(file_path, data_column, bins=10, title='', show_stats=True):
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    """
    Create and display a histogram from Excel data and optionally plot mode, mean, and median.

    Parameters:
    - file_path: str, path to the Excel file.
    - data_column: str, name of the column containing the numeric data for the histogram.
    - bins: int, number of bins for the histogram.
    - title: str, title of the histogram.
    - show_stats: bool, whether to show mode, mean, and median on the histogram.
    """
    # Load the dataset
    data = pd.read_excel(file_path)
    
    # Plotting the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(data[data_column].dropna(), bins=bins, color='skyblue', edgecolor='black', alpha=0.7)
    
    if show_stats:
        # Calculate statistics
        stats_results = cal_statistics(file_path, data_column)
        mean = stats_results['mean']
        median = stats_results['median']
        mode = stats_results['mode']
        
        # Plotting the mean, median, mode
        plt.axvline(mean, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean:.2f}')
        plt.axvline(median, color='green', linestyle='dashed', linewidth=1, label=f'Median: {median:.2f}')
        if mode is not None and not np.isnan(mode):  # Check if mode is valid
            plt.axvline(mode, color='blue', linestyle='dashed', linewidth=1, label=f'Mode: {mode:.2f}')
    
    plt.title(title)
    plt.xlabel(data_column)
    plt.ylabel('Frequency')
    plt.legend()
    plt.tight_layout()
    plt.show()



def cal_probabilities(file_path, column, k):
    import pandas as pd
    """
    Calculate probabilities for a given column in an Excel file.

    Parameters:
    - file_path: str, path to the Excel file.
    - column: str, name of the column to calculate probabilities for.
    - k: int, the value to calculate probabilities for P(X ≤ k), P(X > k), and P(X ≥ k).

    Returns:
    - A dictionary containing the calculated probabilities.
    """
    # Load the dataset
    data = pd.read_excel(file_path, k )
    
    # Ensure the column exists
    if column not in data.columns:
        raise ValueError(f"Column '{column}' not found in the Excel file.")
    
    # Calculate frequencies of each unique value
    frequencies = data[column].value_counts().to_dict()
    total_frequency = sum(frequencies.values())
    
    # Calculating probabilities
    p_x_leq_k = sum(freq for outcome, freq in frequencies.items() if outcome <= k) / total_frequency
    p_x_gt_k = sum(freq for outcome, freq in frequencies.items() if outcome > k) / total_frequency
    p_x_geq_k = sum(freq for outcome, freq in frequencies.items() if outcome >= k) / total_frequency
    
    return {
        "P(X ≤ k)": p_x_leq_k,
        "P(X > k)": p_x_gt_k,
        "P(X ≥ k)": p_x_geq_k
    }


def cal_and_create_poisson(lam, max_k, title='Poisson Distribution'):
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import poisson
    """
    Calculate probabilities and cumulative probabilities for a Poisson distribution
    and visualize the PMF and CDF.

    Parameters:
    - lam: float, the average rate (lambda) of successes in a given time interval.
    - max_k: int, the maximum value of k to calculate the PMF and CDF for.
    - title: str, title of the plot.
    """
    # k values for which we will calculate the PMF and CDF
    k_values = np.arange(0, max_k + 1)
    
    # Calculate PMF and CDF for each k value
    pmf_values = poisson.pmf(k_values, lam)
    cdf_values = poisson.cdf(k_values, lam)
    
    # Visualizing the Poisson PMF and CDF
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # PMF
    color = 'tab:blue'
    ax1.set_xlabel('Number of Events (k)')
    ax1.set_ylabel('PMF (Probability)', color=color)
    ax1.stem(k_values, pmf_values, linefmt='b-', markerfmt='bo', basefmt='r-', label='PMF')
    ax1.tick_params(axis='y', labelcolor=color)
    
    # CDF
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:red'
    ax2.set_ylabel('CDF (Cumulative Probability)', color=color)
    ax2.plot(k_values, cdf_values, color=color, marker='o', linestyle='-', label='CDF')
    ax2.tick_params(axis='y', labelcolor=color)
    
    # Final plot adjustments
    fig.suptitle(title)
    fig.tight_layout()  # Adjust layout to not cut off labels
    plt.grid(True, which='both', axis='x', linestyle='--', linewidth=0.5)
    plt.show()

    # Optionally, return the calculated PMF and CDF values
    return pmf_values, cdf_values
