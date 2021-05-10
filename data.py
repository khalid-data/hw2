import pandas


def load_data(path):
    """
    loads data into dictionary from csv file that contains the wanted info
    :param path: path of file
    :param features: features we want to keep in the dictionary
    :return: the dictionary
    """
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    return data


def filter_by_features(data, feature, values):
    """
    the function returns two dict filtered by feature and value
    :param data: a dictionary, its keys are features from the csv file
    :param feature: feature from csv file
    :param values: values that can represent the feature
    :return: tow dic one with the data we want (filtered) and the rest of the data
    """
    # create list of the colmn we filter by
    feature_l = list(data[feature])
    wanted = dict()
    others = dict()
    for i in data.keys():
        wanted[i] = list()
        others[i] = list()
    n = len(data[feature])
    for j in range(n):
        d = values
        if feature_l[j] in d:
            for k in data.keys():
                wanted[k] += [data[k][j]]
        else:
            for k in data.keys():
                others[k] += [data[k][j]]
    return wanted, others


def print_details(data, features, statistic_functions):
    """
    prints statistic data for the features
    :param data: a dictionary, its keys are features from the csv file
    :param features: features from csv file
    :param statistic_functions: functions in statistics file that calculates statics
    :return: none
    """
    for i in features:
        num_sum = (statistic_functions[0](data[i]))
        num_mean = (statistic_functions[1](data[i]))
        num_median = (statistic_functions[2](data[i]))
        print(i + ":", num_sum, num_mean, num_median)
