class RoseDictionary:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def pop_item(self, raise_error=False, default=None, error_msg=None):
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
            key, value = list(self.data.items())[-1]
            del self.data[key]
            return key, value

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
d = RoseDictionary()
#d["key1"] = "value1"
#d["key2"] = "value2"
#print(d["key1"])
#print(d.get_item("key1"))
#print(d.get_item("key3", default = "Default Value"))
#d.get_item("key3")
print(d.pop_item())
print(d.get_item("key1", error_msg = "error message"))
print(d.get_item("key2", error_msg = "error message2"))
d.pop_item()
d.get_item("key3", default = "Default Value", raise_error = True, error_msg = "Hi")
