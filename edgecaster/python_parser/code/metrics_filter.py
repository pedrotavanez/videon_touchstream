from pprint import pprint


def metrics_filtering(data, metric_filter):
    new_dict = {}
    for filter in metric_filter:
        ##print(f"{filter}")
        for index, item in enumerate(data):
            # print(item)
            # print(index,item)
            if filter == item:
                pass
            elif "*" in filter:
                if item.startswith(filter.replace("*", "")):
                    pass
                else:
                    r = dict(data)
                    del r[item]
            else:
                r = dict(data)
                del r[item]
    # pprint(r)
    return r
