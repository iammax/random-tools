import numpy as np


def load(filename):

    try:
        data = np.loadtxt(filename)
        return data
    except Exception as not_plaintext:
        pass
    
    try:
        data = np.loadtxt(filename, delimiter=',')
        return data
    except Exception as not_csv:
        pass
    
    try:
        data = np.load(filename)
        return data
    except Exception as not_binary:
        pass
    
    print "Error: {0} is not recognized as a plain text data, csv, or numpy binary file, or it doesn't exist".format(filename)

