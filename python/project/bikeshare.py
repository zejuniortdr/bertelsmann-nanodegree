from __future__ import absolute_import, print_function

import time

import numpy as np
import pandas as pd
from six.moves import input

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}
MONTHS_NAMES = ["january", "february", "march", "april", "may", "june"]
WEEKDAYS_NAMES = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]


def get_input_data(label, validation_data, enable_all=False):
    """
    Generic function to get data from input and validate until is correct

    Returns:
        (str) label - label for messages to user like city, month and day
        (list) validation_data - validation list to be compare against user input
        (boolean) enable_all - allow the user to type [all] for a filter
    """
    while True:
        enable_all_error_message = ""
        user_input = eval(input(f"Enter the {label} name: ").lower())
        if user_input in validation_data or (user_input == "all" and enable_all):
            return user_input
        elif enable_all:
            enable_all_error_message = " or type [all]"

        print(
            f"Invalid {label} name [{user_input}]. Please choose one of the following: {validation_data}{enable_all_error_message}"
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = get_input_data("city", list(CITY_DATA.keys()))

    # get user input for month (all, january, february, ... , june)
    month = get_input_data("month", MONTHS_NAMES, enable_all=True)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_input_data("day of week", WEEKDAYS_NAMES, enable_all=True)

    print(("-" * 40))
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

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # display the most common month

    # display the most common day of week

    # display the most common start hour

    print(("\nThis took %s seconds." % (time.time() - start_time)))
    print(("-" * 40))


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # display most commonly used start station

    # display most commonly used end station

    # display most frequent combination of start station and end station trip

    print(("\nThis took %s seconds." % (time.time() - start_time)))
    print(("-" * 40))


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # display total travel time

    # display mean travel time

    print(("\nThis took %s seconds." % (time.time() - start_time)))
    print(("-" * 40))


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # Display counts of user types

    # Display counts of gender

    # Display earliest, most recent, and most common year of birth

    print(("\nThis took %s seconds." % (time.time() - start_time)))
    print(("-" * 40))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = eval(input("\nWould you like to restart? Enter yes or no.\n"))
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
    main()
