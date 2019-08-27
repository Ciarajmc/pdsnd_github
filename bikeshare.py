import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chicago, New York City or Washington?\n').lower()
    while True:
        if city not in ('chicago', 'new york city', 'washington'):
            city = input('Sorry I don\'t understand your input, plese try again\n').lower()
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\nWhich month? January, February, March, April, May, June or all?\n').lower().lower()
    while True:
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            month = input('Sorry I don\'t understand your input, plese try again\n').lower()
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nWhich day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all?\n').lower().lower()
    while True:
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            day = input('Sorry I don\'t understand your input, plese try again\n').lower()
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['Month'] == month]

    if day != 'all':
        df = df[df['Day of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    popular_month = df['Month'].mode()[0]
    print('Most Common Month is {}'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['Day of Week'].mode()[0]
    print('Most Common Day is {}'.format(popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['hour'].mode()[0]
    print('Most Common Start Hour is {}'.format(popular_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station is {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Common End Station is {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    popular_combination = 'From ' + df['Start Station'] + ' to ' + df['End Station']
    print('Most Popular Trip is {}'.format(popular_combination.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total Travel Time is {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time is {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('What is the breakdown of users?\n{}'.format(user_types_count))

    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print('\nNo gender data available for this location')
    else:
        gender_count = df['Gender'].value_counts()
        print('\nWhat is the breakdown of gender?\n{}'.format(gender_count))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print ('\nNo birth year data available for this location')
    else:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year of Birth is {}'.format(earliest_year))

        most_recent_year = df['Birth Year'].max()
        print ('Most Recent Year of Birth is {}'.format(most_recent_year))

        most_common_year = df['Birth Year'].mode()[0]
        print ('Most Common Year of Birth is {}'.format(most_common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    start_line = 0
    end_line = 5

    raw_data = input('Would you like to see individual trip data? Type \'yes\' or \'no\'\n').lower()
    while True:
        if raw_data == 'no':
            return
        if raw_data == 'yes':
            for i in range(start_line, end_line):
                print(df.iloc[i])
                print('\n')
            start_line += 5
            end_line += 5
        raw_data = input('Would you like to see more individual trip data? Type \'yes\' or \'no\'\n').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
