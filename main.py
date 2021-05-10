import sys
from data import load_data, filter_by_features, print_details
from statistics import sum1, mean, median

def main(argv):
    """

    :param argv:
    :return:
    """
    # load data from csv file
    all_data = load_data(sys.argv[0])
    # q1
    # print statistic info for D regions (ones that their names starts with L or S) for requested values
    # requested values are hospitalized_with_symptoms, Intensive_care, total_hospitalized, home_insulation
    # filter data and get a dict that has only data from region D
    wanted_data, unwanted_data = filter_by_features(all_data, 'hospitalized_with_symptoms', {'L', 'S'})
    statistic_functions = [sum1, mean, median]
    features_for_printing = ['hospitalized_with_symptoms', 'Intensive_care', 'total_hospitalized', 'home_insulation']
    print_details(wanted_data, features_for_printing, statistic_functions)

if __name__ == '__main__':
    main(sys.argv)


