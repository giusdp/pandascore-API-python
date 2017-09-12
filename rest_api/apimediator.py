import requests
import json

# Useful constants ?
LOL = 1  # I think it's 1?
DOTA2 = 2
CSGO = 3

status = {200: 'Ok',
          400: 'The request is malformed',
          401: 'Unauthorized',
          403: 'Forbidden',
          404: 'Page or resource is not found',
          422: 'Unprocessable entity',
          500: 'We have a problem with our server. Please try again later.',
          'Connection refused': 'Most likely cause is not using HTTPS.'}


def get_status_message(status_code):
        return status[status_code]


class PandaRestAPI(object):
    """Class used to build the url queries and make the api calls. GeneralPanda, Dota2, LoL etc offer the bindings 
    to their relative api calls. Each one of those class use PandaRestAPI as a mediator to the Pandascore."""

    def __init__(self):
        """Sets the endpoint and gets the access token in order to perfom the api calls."""
        self.endpoint = 'https://api.pandascore.co'
        import os.path  # all of this to go get the access token in secrets.json
        f = open(os.path.join(os.path.dirname(__file__), os.pardir, 'SECRETS.json'), 'r')
        js = json.load(f)
        self.access_token = js['API_Token']
        f.close()

    def send_query(self, query, query_sort=None, query_filter=None, query_range=None):
        """Method to make an api call. It receives a string to specify what to call and options like sort or filter 
        and builds a complete query url for the Pandascore API. It returns a tuple with the status code
        and the JSON of the response. The status message can be retrieved with: get_status_message giving it the status code.
        XML to be done. 
        :param query: A string to specify what to call. (e.g. /leagues )
        :type query: str
        :param query_sort: optional parameter, it defines the sorting method to apply on the response by Pandascore. 
        It must be a list of the fields to use for sorting. 
        :type query_sort: list
        :param query_filter: optional parameter. It defines the filter method to apply on the response by Pandascore.
        It must be a dict having as keys the fields to use and the values a list of what to get.
        :type query_filter: dict
        :return: the tuple containing status code and json response.
        :rtype: tuple"""

        opts = {}
        if query_sort is not None and not isinstance(query_sort, list):
            raise TypeError('query_sort must be a list')
        if query_filter is not None and not isinstance(query_filter, dict):
            raise TypeError('query_filter must be a dict')
        if not isinstance(query, str):
            raise TypeError('query must be a str')

        opts.update({'sort': query_sort})
        opts.update({'filter': query_filter})

        request_url = self.encode_options(self.endpoint + query, opts)
        auth_token = {'Authorization': 'Bearer ' + self.access_token}
        r = requests.get(request_url, headers=auth_token)
        return self.build_answer_tuple(r)

    def build_answer_tuple(self, req_response):
        """ Method used to create the return object after making an api call. It creates a tuple containing 
        the status code of the response and a json object if the api call succeded (status code == 200), 
        the status message if the call failed.
        For now it's assumed always JSON if success. XML to be done.
        :param req_response: response from a GET query to the Pandascore API.
        :type req_response: Response
        :return: A tuple containing the status code of the response and a json object
        (or status message if there was an error).
        """
        # req_response.headers[content-type] can be used to see if it's JSON or XML. For now it's assumed always JSON.
        if req_response.status_code == 200:
            return req_response.status_code, req_response.json()
        else:
            return req_response.status_code, get_status_message(req_response.status_code)

    def encode_options(self, base_query, options=None):
        """Method used to build a query url starting from the base query and adding the options one at a time.
        options must be a dict where the key defines the method (e.g. sort, filter) and the values are the options to 
        apply.
        :param base_query: A string which is the base query url.
        :type base_query: str
        :param options: A dict to specify the options to add to the base query
        :type options: dict
        :return: The query url to send to Pandascore.
        :rtype: str"""
        if options is None:
            return base_query
        base_query += '?'
        for key in options.keys():
            opt = options[key]  # can be list to sort, dict to filter etc.
            if opt is None or len(opt) == 0:
                continue
            elif key == 'sort':
                base_query += self.encode_sort(opt) + '&'
            elif key == 'filter':
                base_query += self.encode_filter(opt) + '&'
        return base_query[:len(base_query) - 1]  # to get rid of the last '&' (or '?')

    def encode_sort(self, to_sort_list):
        """:param to_sort_list: A list with strings.
        :type to_sort_list: list"""
        return 'sort=' + ','.join(str(item) for item in to_sort_list)

    def encode_filter(self, filters):
        """:param filters: A dict having as keys the attributes to filter and values lists with the words to use.
        :type filters: dict"""
        s = ''
        for key in filters:
            s += 'filter[' + key + ']=' + ','.join(str(item) for item in filters[key])
        return s

    def encode_range(self):
        pass

    def encode_pagination(self):
        pass


