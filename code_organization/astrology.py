
import datetime

def birthday_to_sign(month, day):

    """
    Enter a doc string here
    :param month:
    :param day:
    :return:
    """

    # datetime objects require a year, month, and day
    # define a nominal year (a leap year) for date comparisons
    nominal_year = 2000

    # define a date corresponding to the month and day provided
    # as arguments in this function
    date = datetime.datetime(nominal_year,month,day)

    # Aries is between Mar 21 and Apr 20
    if date >= datetime.datetime(nominal_year, 3, 21) and date <= datetime.datetime(nominal_year, 4, 20):
        sign = 'Aries'

    # Taurus is between Apr 21 and May 20
    if date >= datetime.datetime(nominal_year, 4, 21) and date <= datetime.datetime(nominal_year, 5, 20):
        sign = 'Taurus'

    # Gemini is between May 21 and Jun 21
    if date >= datetime.datetime(nominal_year, 5, 21) and date <= datetime.datetime(nominal_year, 6, 21):
        sign = 'Gemini'

    # Cancer is between Jun 22 and Jul 22
    if date >= datetime.datetime(nominal_year, 6, 22) and date <= datetime.datetime(nominal_year, 7, 22):
        sign = 'Cancer'

    # Leo is between Jul 23 and Aug 23
    if date >= datetime.datetime(nominal_year, 7, 23) and date <= datetime.datetime(nominal_year, 8, 23):
        sign = 'Leo'

    # Virgo is between Aug 24 and Sep 23
    if date >= datetime.datetime(nominal_year, 8, 24) and date <= datetime.datetime(nominal_year, 9, 23):
        sign = 'Virgo'

    # Complete the following signs for this function

    # Libra is between Sept 24 and Oct 23


    # Scorpio is between Oct 24 and Nov 22


    # Sagittarius is between Nov 23 and Dec 21


    # Capricorn is between Dec 22 and Jan 20


    # Aquarius is between Jan 21 and Feb 18


    # Pisces is between Fwb 19 and Mar 20


    return(sign)

def sign_to_birthday_range(sign):

    """
        Enter a doc string here
        :param sign:
        :return:
    """

    # Aries is between Mar 21 and Apr 20
    if sign == 'Aries':
        start_month = 3
        start_day = 21
        end_month = 4
        end_day = 20

    # Taurus is between Apr 21 and May 20
    if sign == 'Taurus':
        start_month = 4
        start_day = 21
        end_month = 5
        end_day = 20

    # Gemini is between May 21 and Jun 21
    if sign == 'Gemini':
        start_month = 5
        start_day = 21
        end_month = 6
        end_day = 21

    # Cancer is between Jun 22 and Jul 22
    if sign == 'Cancer':
        start_month = 6
        start_day = 22
        end_month = 7
        end_day = 22

    # Leo is between Jul 23 and Aug 23
    if sign == 'Leo':
        start_month = 7
        start_day = 23
        end_month = 8
        end_day = 23

    # Virgo is between Aug 24 and Sep 23
    if sign == 'Virgo':
        start_month = 8
        start_day = 24
        end_month = 9
        end_day = 23

    # Complete the statements below for this function

    # Libra is between Sept 24 and Oct 23


    # Scorpio is between Oct 24 and Nov 22


    # Sagittarius is between Nov 23 and Dec 21


    # Capricorn is between Dec 22 and Jan 20


    # Aquarius is between Jan 21 and Feb 18


    # Pisces is between Fwb 19 and Mar 20


    return(start_month, start_day, end_month, end_day)