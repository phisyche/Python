def manipulate_data(data_type=None, data=None):
    if data_type is 'list':
        return data[-1:: -1]
    if data_type == 'set':
        return set.union(data, ["ANDELA", "TIA", "AFRICA"])
    if data_type == 'dictionary':
        return [keys for keys, item in data.items()]
