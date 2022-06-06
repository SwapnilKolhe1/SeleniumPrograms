import pytest

@pytest.mark.parametrize("username , password" ,
                             [
                                ("user", "pass"),
                                ("abc", "abc@pass"),
                                ("xyz", "xyz@pass"),
                                ("pqr", "pqr@pass"),
                             ]

                         )

def test_login(username , password):
    print(username + " " + password)
    #logic to test login functionality
