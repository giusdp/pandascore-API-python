from rest_api.apimediator import PandaRestAPI


class GenericCallsSet(object):

    def __init__(self, query_prefix=None):
        self.rest_api = PandaRestAPI()
        self.query_prefix = query_prefix

    def build_base_query(self, query, some_id=None, follow_up_query=None):
        s = ''
        if self.query_prefix is not None:
            s += self.query_prefix
        s += query
        if some_id is not None:
            s += '/' + str(some_id)
        if follow_up_query is not None:
            s += '/' + follow_up_query
        return s

    def get_things(self, query, some_id=None, follow_up_query=None, query_sort=None, query_filter=None, query_range=None):
        base_query = self.build_base_query(query, some_id, follow_up_query)
        return self.rest_api.send_query(base_query, query_sort, query_filter, query_range)

