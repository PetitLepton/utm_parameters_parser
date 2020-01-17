from landing_page import (
    utm_parameters_string_to_hash,
    extract_utm_parameters,
    LandingPage,
)


simple_url = "www.example.com"
simple_url_with_trailing_slash = "www.example.com/"
url_with_parameters = (
    "www.example.com?utm_source=my_source&utm_medium=my_medium&utm_campaign=my_campaign"
)


def test_parameters_string_to_hash():
    bare = "a=1&b=2&c=3"
    expected = {"a": "1", "b": "2", "c": "3"}
    assert expected == utm_parameters_string_to_hash(bare)


def test_extract_utm_parameters():
    bare = {
        "utm_source": "my_source",
        "utm_medium": "my_medium",
        "utm_campaign": "my_campaign",
        "search": "useless",
    }
    expected = {
        "source": "my_source",
        "medium": "my_medium",
        "campaign": "my_campaign",
    }
    assert expected == extract_utm_parameters(bare)


def test_init():
    landing_page = LandingPage(
        full_url="www.example.com?utm_source=my_source&utm_medium=my_medium&utm_campaign=my_campaign"
    )

    assert landing_page.path == "www.example.com"
    assert (
        landing_page.utm_parameters_string
        == "utm_source=my_source&utm_medium=my_medium&utm_campaign=my_campaign"
    )

