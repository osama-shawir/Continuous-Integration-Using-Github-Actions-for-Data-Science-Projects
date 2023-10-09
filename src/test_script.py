import pytest
from Polars_Descriptive_Stats_Script import AircraftAnalytics

def test_AircraftAnalytics():
    """
    Test the AircraftAnalytics function for basic functionality.

    This test case checks if the AircraftAnalytics function
    
     can be run without raising exceptions.
    """
    try:
        # Attempt to run the AircraftAnalytics function
        AircraftAnalytics()
    except Exception as e:
        # If an exception occurs, fail the test and provide an error message
        pytest.fail(f"AircraftAnalytics raised an exception: {str(e)}")


if __name__ == "__main__":
    test_AircraftAnalytics()