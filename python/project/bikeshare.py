from datetime import timedelta
import time
import pandas as pd
import numpy as np


CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}

MONTHS_NAMES = {
    "january": 1, 
    "february": 2, 
    "march": 3, 
    "april": 4, 
    "may": 5, 
    "june": 6,
}

WEEKDAYS_NAMES = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]


def get_most_commum(df):
    df_most_common = df.value_counts().to_frame()
    most_common = df_most_common.index.values[0]
    count = df_most_common.values[0][0]
    return most_common, count

def get_route(row):
    return f"FROM: {row['Start Station']} TO: {row['End Station']}"


def get_dict_key_name_from_value(input_dict, value):
    """
    Function to get dict key name from a key value
    Args:
        (dict) input_dict - dict to search for the value
        (int) value - value used in search
    Returns:
        (str) key - key from dict with the value informed
        None - if it was not found
    """
    try:
        key = list(input_dict.keys())[list(input_dict.values()).index(value)]
        return key
    except ValueError:
        return None


def get_input_data(label, validation_data, enable_all=False):
    """
    Generic function to get data from input and validate until is correct

    Returns:
        (str) label - label for messages to user. Examples: city, month or day
        (list) validation_data - validation list to be compare against user input
        (boolean) enable_all - allow the user to type [all] for a filter
    """
    while True:
        enable_all_error_message = ""
        user_input = input(f"Enter the {label} name: ").lower()
        if user_input == "exit":
            exit()
        if user_input in validation_data or (user_input == "all" and enable_all):
            return user_input
        elif enable_all:
            enable_all_error_message = " or type 'all'"

        print(
            f"Invalid {label} name '{user_input}]'. Please choose one of the following: {validation_data}{enable_all_error_message}"
        )


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")
    print("If you want to quit, just type 'exit' anytime")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = get_input_data("city", list(CITY_DATA.keys()))

    # get user input for month (all, january, february, ... , june)
    month = get_input_data("month", list(MONTHS_NAMES.keys()), enable_all=True)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_input_data("day of week", WEEKDAYS_NAMES, enable_all=True)

    print("-" * 40)
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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month 
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    df['route'] = df.apply(lambda row: get_route(row), axis=1)

    if month != "all":
        df = df[df['month'] == MONTHS_NAMES[month]]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # display the most common month
    month, count = get_most_commum(df['month'])
    month = get_dict_key_name_from_value(MONTHS_NAMES, month)
    print(f"The most common month is {month.title()}. Count: {count}")

    # display the most common day of week
    day_of_week, count = get_most_commum(df['day_of_week'])
    print(f"The most common day of week is {day_of_week}. Count: {count}")

    # display the most common start hour
    hour, count = get_most_commum(df['hour'])
    print(f"The most common start hour is {hour}. Count: {count}")

    print(f"\nThis took {time.time() - start_time} seconds.")
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # display most commonly used start station
    start_station, count = get_most_commum(df['Start Station'])
    print(f"The most commonly used start station is {start_station}. Count: {count}")

    # display most commonly used end station
    end_station, count = get_most_commum(df['End Station'])
    print(f"The most commonly used end station is {end_station}. Count: {count}")

    # display most frequent combination of start station and end station trip
    # TODO: most frequent combination
    route, count = get_most_commum(df['route'])
    print(f"The most commonly route is {route}. Count: {count}")


    print(f"\nThis took {time.time() - start_time} seconds.")
    print("-" * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # display total travel time
    total_time_in_seconds = int(df['Trip Duration'].sum())
    print(f"Total travel time is {total_time_in_seconds} seconds ({timedelta(seconds=total_time_in_seconds)})")

    # display mean travel time
    mean_time_in_seconds = int(df['Trip Duration'].mean())
    print(f"Mean travel time is {mean_time_in_seconds} seconds ({timedelta(seconds=mean_time_in_seconds)})")

    # display max travel time
    max_time_in_seconds = int(df['Trip Duration'].max())
    print(f"Max travel time is {max_time_in_seconds} seconds ({timedelta(seconds=max_time_in_seconds)})")

    # display min travel time
    min_time_in_seconds = int(df['Trip Duration'].min())
    print(f"Min travel time is {min_time_in_seconds} seconds ({timedelta(seconds=min_time_in_seconds)})")
    
    print(f"\nThis took {time.time() - start_time} seconds.")
    print("-" * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # Display counts of user types
    df_users_types = df.groupby(['User Type'])['User Type'].count()
    print()
    print(df_users_types.to_string())

    # Display counts of gender
    df_gender = df.groupby(['Gender'])['Gender'].count()
    print()
    print(df_gender.to_string())
    empty = len(df) - sum(df_gender.values.tolist())
    print(f"Empty:     {empty}")

    # Display earliest, most recent, and most common year of birth
    df_erliest_year = int(df["Birth Year"].min())
    df_recent_year = int(df["Birth Year"].max())
    df_mode_year = int(df["Birth Year"].mode())

    print(f"\nThe most erliest year of birth: {df_erliest_year}")
    print(f"The most recent year of birth: {df_recent_year}")
    print(f"The most common year of birth: {df_mode_year}")

    print(f"\nThis took {time.time() - start_time} seconds.")
    print("-" * 40)


def main():
    # while True:
    i = 0
    for k, v in CITY_DATA.items():
        for k2, _ in MONTHS_NAMES.items():
            for d in WEEKDAYS_NAMES:
                start_time = time.time()
                # city, month, day = get_filters()
                # city, month, day = "chicago", "january", "monday"
                city, month, day = k, k2, d
                
                df = load_data(city, month, day)

                time_stats(df)
                station_stats(df)
                trip_duration_stats(df)
                user_stats(df)
                

                print(f"\nTotal time in seconds: {time.time() - start_time}")
                # restart = input("\nWould you like to restart? Enter yes or no.\n")
                # if restart.lower() != "yes":
                #     break
                
                i += 1
                print("#"*50)
                print(i, 126)
                print("#"*50)

if __name__ == "__main__":
    main()
