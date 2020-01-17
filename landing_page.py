from urllib.parse import urlparse


def utm_parameters_string_to_hash(utm_parameters_string):
    """"""
    return dict(
        [tuple(parameter.split("=")) for parameter in utm_parameters_string.split("&")]
    )


def extract_utm_parameters(utm_parameters_hash):
    parameters = ["source", "medium", "campaign"]
    return {
        parameter: utm_parameters_hash.get(f"utm_{parameter}", None)
        for parameter in parameters
    }


class LandingPage:
    def __init__(self, full_url):
        parsed_full_url = urlparse(full_url)
        self.full_url = full_url
        self.path = parsed_full_url.path
        self.utm_parameters_string = parsed_full_url.query

    def get_utm_parameters_hash(self):
        utm_parameters_hash = utm_parameters_string_to_hash(self.utm_parameters_string)
        return extract_utm_parameters(utm_parameters_hash)
