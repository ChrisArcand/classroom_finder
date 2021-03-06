import re

def pad(date):
    '''take datetime object and pad zero on day/month if needed'''
    day = '0' + str(date.day) if (len(str(date.day)) < 2) else date.day
    month = '0' + str(date.month) if (len(str(date.month)) < 2) else date.month
    return str(date.year) + str(month) + str(day)


def constructURL(date, campus):
    ''' Construct Url for fetching html data.
        @param date - datetime object
        @param campus - string indicating which campus code (ex. "east" -> 947166
    '''
    eastCode=947166
    westCode=947169
    stpaulCode=947171
    if campus == "east":
        code = eastCode
    if campus == "west":
        code = westCode
    if campus == "stpaul":
        code = stpaulCode

    return "http://wvprd.ocm.umn.edu/gpcwv/wv3_servlet/urd/run/wv_space." + \
               "DayList?spfilter={},spdt={},lbdviewmode=list".format(code,pad(date))

def get_space_id(_string):
    ''' simple wrapper for 'javascript:spaceInfo(#)' pattern '''
    pattern = re.compile("\([^)]+\)")
    return re.search(pattern, _string).group()[1:-1]

# because, why not
def int_to_month(i):
    months = ["January", "February", "March", "April", "May", "June", "July",\
                "August", "September", "October", "November", "December"]
    return months[i-1]
