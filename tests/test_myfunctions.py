from learning_conf import myfunctions
def test_get_confidence(monkeypatch, capsys):
    # Test case 1: Valid input
    user_input = "75"
    monkeypatch.setattr('builtins.input', lambda _: user_input)

    # Call the function and capture the output
    myfunctions.get_confidence()
    captured1 = capsys.readouterr()

    # Assert that the captured output contains the expected prompt
    assert "The integer you entered is: 75" in captured1.out

    # Test case 2: Valid input after invalid input
    user_inputs = ["abc", "90"]

    # First call with invalid input
    def mock_input(_):
        return user_inputs.pop(0)

    # Keep asking for input until valid value is provided
    monkeypatch.setattr('builtins.input', mock_input)
    while True:
        try:
            myfunctions.get_confidence()
        except ValueError:
            continue
        break

    # Capture the output after the valid input is provided
    captured2 = capsys.readouterr()

    # Assert that the captured output contains the expected prompt for the valid input
    assert "The integer you entered is: 90" in captured2.out


def test_plot_confidence(capsys):
    # Set up test data
    conf_records = [30, 60, 78, 50, 25, 90, 65]
    # Call the plot_confidence function with test data
    myfunctions.conf_records = conf_records

    # The function should run without raising any errors
    myfunctions.plot_confidence()