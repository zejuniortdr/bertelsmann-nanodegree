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
    df['route'] = f"{df['Start Station']} - {df['End Station']}"

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
    df_most_common_month = df['month'].value_counts().to_frame()
    most_common_month = get_dict_key_name_from_value(
        MONTHS_NAMES, df_most_common_month.index.values[0]
    )
    count = df_most_common_month.values[0][0]
    print(f"The most common month is {most_common_month.title()}. Count: {count}")

    # display the most common day of week
    df_most_common_day_of_week = df['day_of_week'].value_counts().to_frame()
    most_common_day_of_week = df_most_common_day_of_week.index.values[0]
    count = df_most_common_day_of_week.values[0][0]
    print(f"The most common day of week is {most_common_day_of_week}. Count: {count}")

    # display the most common start hour
    df_most_common_hour = df['hour'].value_counts().to_frame()
    most_common_hour = df_most_common_hour.index.values[0]
    count = df_most_common_hour.values[0][0]
    print(f"The most common start hour is {most_common_hour}. Count: {count}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # display most commonly used start station
    df_most_common_station = df['Start Station'].value_counts().to_frame()
    most_common_station = df_most_common_station.index.values[0]
    count = df_most_common_station.values[0][0]
    print(f"The most commonly used start station is {most_common_station}. Count: {count}")

    # display most commonly used end station
    df_most_common_station = df['End Station'].value_counts().to_frame()
    most_common_station = df_most_common_station.index.values[0]
    count = df_most_common_station.values[0][0]
    print(f"The most commonly used end station is {most_common_station}. Count: {count}")

    # display most frequent combination of start station and end station trip
    # df_most_common_route = df['route'].value_counts().to_frame()
    # most_common_route = df_most_common_route.index.values[0]
    # count = df_most_common_route.values[0][0]
    # print(f"The most common start route is {most_common_route}. Count: {count}")
    # TODO: most frequent combination
    print("# TODO: most frequent combination of start station and end station trip")



    print("\nThis took %s seconds." % (time.time() - start_time))
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

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # Display counts of user types

    # Display counts of gender

    # Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def main():
    while True:
        # city, month, day = get_filters()
        city, month, day = "chicago", "january", "sunday"
        
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        # user_stats(df)

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
    main()
