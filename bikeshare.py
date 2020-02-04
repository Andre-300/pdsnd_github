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



    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # this function is called at the bottom in the main function
def get_user_input_city(prompt):
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input(prompt).strip().lower()
        if city in cities:
            return city
        elif input('Please select any of the following: Chicago,New York and Washington'):
            if city in cities:
                return city


    # TO DO: get user input for month (all, january, february, ... , june)
def get_user_input_month(prompt):
    months = ['all', 'jan', 'feb', 'mar', 'apr', 'may', 'jun']
    while True:
        month = input(prompt).strip().lower()
        if month in months:
            return month
        elif input("Data can only be displayed for 'all', Jan', 'Feb', 'Mar', 'Apr', 'May', and 'Jun': "):
            if month in months:
                return month


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
def get_user_input_day(prompt):
    while True:
        day = str(input(prompt).strip().lower())
        if day in ('all','0','1', '2', '3', '4', '5', '6'):
            return day

# this will prit dashed lines after the execution of the function
print('-'*40)



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

    df['month'] = df['Start Time'].dt.month
    df['week_day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df['start_end_combo'] = "starting at" + df['Start Station'] + ' and ending at ' + df['End Station']

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The Most Common Month is ',common_month)


    # TO DO: display the most common day of week
    common_day = df['week_day'].mode()[0]
    print('The Most Common Day is ',common_day)


    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The Most Common Hour is ',common_hour)


# important point to check run time of a particular function
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The Most Popular Start Station is ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The Most Popular End Station is ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_combo = df['start_end_combo'].mode()[0]
    print('The Most Popular Start/End Combination is ', popular_start_end_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('Total Trip Duration is ', total_trip_duration)

    # TO DO: display mean travel time
    avg_trip_duration = df['Trip Duration'].mean()
    print('Average Trip Duration is ', avg_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    try:
        user_genders = df['Gender'].value_counts()
    except: user_genders = 'Washington does not have user gender data'
    print(user_genders)

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        oldest_rider_birth = 'The oldest rider was born in ' + str(df['Birth Year'].min())
    except: oldest_rider_birth = 'Washington does not have rider year of birth data'

    print(oldest_rider_birth)

    try:
        youngest_rider_birth = 'The youngest ride was born in ' + str(df['Birth Year'].max())
    except: youngest_rider_birth = 'Washington does not have rider year of birth data'

    print(youngest_rider_birth)

    try:
        most_common_rider_birth = 'The year in which the most riders were born in is ' + str(df['Birth Year'].mode()[0])
    except: most_common_rider_birth = 'Washington does not have rider year of birth data'

    print(most_common_rider_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
#function gives the user the ability to look at the first 5 rows and then gives them the option to iterate through 5 lines at a time if they'd like to inspect further.
#used a while loop to keep iterating as long as user continues to answer "yes" or exit and move on when they don't.
    i = 0
    data = input("\nwould you like to view the first 5 lines of raw bikeshare data?\n").lower()
    if data != 'yes':
        print("skipping raw data display.")
    else:
        while True:
            window = df[(i * 5):5 +(i * 5)]
            print(window)
            i += 1
            five_raw = input("\nWould you like to see the next 5 rows of raw data?\n")
            if five_raw.lower() != 'yes':
                break

def main():
    while True:
        city = get_user_input_city("Which city would you like to explore? Please select Chicago, New York City, or Washington: ")

        month = get_user_input_month("What months we could choose from? Please select 'all', Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun: ")

        day = get_user_input_day("Which day of the week would you like to look at? Please select 'all' days or a day using the corresponding day of the week, starting with Sunday=0 and ending with Saturday: ")
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
