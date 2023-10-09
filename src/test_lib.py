from lib import (
    read_aircraft_data_from_google_drive,
    calculate_strikes_max_damage,
    return_25th_quantile,
    return_mean,
    return_std_dev,
    return_median
)


def test_descriptive_stats():
    """
    Test the descriptive statistics functions.

    This test case checks if the descriptive statistics functions can be run
    without raising exceptions and if they return numerical results.
    """
    # Load aircraft data (replace with your specific file_id)
    target_column = 'Speed'
    file_id = '1TAD7Uyc9PjByt_q13uvGXGeubXnujnUi'
    data = read_aircraft_data_from_google_drive(file_id)

    # Test calculate_strikes_max_damage function
    strikes, most_risky_part = calculate_strikes_max_damage(data)
    assert isinstance(strikes, dict)
    assert isinstance(most_risky_part, str)

    # Test return_25th_quantile function
    quantile_25 = return_25th_quantile(data, target_column)
    assert isinstance(quantile_25, float)

    # Test return_mean function
    mean_value = return_mean(data, target_column)
    assert isinstance(mean_value, float)

    # Test return_std_dev function
    std_deviation = return_std_dev(data, target_column)
    assert isinstance(std_deviation, float)

    # Test return_median function
    median_value = return_median(data, target_column)
    assert isinstance(median_value, float)

if __name__ == "__main__":
    test_descriptive_stats()
