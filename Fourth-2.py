class RoseDictionary:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def pop_item(self, raise_error=True, default=None, error_msg=None):
        if not self.data:
            if raise_error:
                if error_msg is not None:
                    raise KeyError(error_msg)
                else:
                    raise KeyError('error_msg')
            else:
                if default is not None:
                    return default
                else:
                    return 'Dictionary was empty and no default value/message was specified.'
        else:
            return self.data.popitem()

    def get_item(self, key, raise_error=True, default=None, error_msg=None):
        if key in self.data:
            return self.data[key]
        else:
            if raise_error:
                if error_msg is not None:
                    raise KeyError(error_msg)
                else:
                    raise KeyError('error_msg')
            else:
                if default is not None:
                    return default
                else:
                    return 'Value was not found and no default value/message was specified.'