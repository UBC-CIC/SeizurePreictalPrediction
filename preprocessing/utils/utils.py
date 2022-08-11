import datetime
from typing import Union
from exceptions import StringTimestampFormat


def calculate_duration(
        start_timestamp: Union[str, datetime.datetime],
        end_timestamp: Union[str, datetime.datetime]
) -> (datetime.datetime, datetime.datetime, float):
    """
    :param start_timestamp: Timestamp to begin the duration calculation from.
    Acceptable format[s]:
    (1) String literal, for example: str("01.03.01")
    (2) Datetime object, for example: datetime.datetime(2021, 12, 11, 1, 3, 1)

    :param end_timestamp: Timestamp to begin the duration calculation from.
    Acceptable format[s]:
    (1) String literal, for example: str("01.03.01")
    (2) Datetime object, for example: datetime.datetime(2021, 12, 11, 1, 3, 1)

    :returns:
    (1) start_timestamp as a datetime.datetime object
    (2) end_timestamp as a datetime.datetime object
    (3) float value indicating the duration of time between the start and end
    timestamps in seconds (for example: 12585.0) 
    """

    start_time = None
    end_time = None

    try:
        if isinstance(start_timestamp, datetime.datetime) and isinstance(end_timestamp, datetime.datetime):
            """ 
            If both variables are already datetime.datetime objects, 
            no further processing is required. Hence, directly compute 
            the elapsed time (in seconds) and return it.
            """

            start_time = start_timestamp
            end_time = end_timestamp

            time_elapsed = end_time - start_time
            return time_elapsed.total_seconds()

        elif isinstance(start_timestamp, str) and isinstance(end_timestamp, str):

            """
            If both variables are string objects, check if they follow the hh.mm.ss format.
            When such a string is split based on the '.' character, it leads to a list with 
            3 components, ["hh", "mm", "ss"].
            """
            if len(start_timestamp.split('.')) != 3:
                raise StringTimestampFormat(entered_timestamp=start_timestamp)
            elif len(end_timestamp.split('.')) != 3:
                raise StringTimestampFormat(entered_timestamp=end_timestamp)

            else:
                try:
                    if int(start_timestamp.split('.')[0]) > int(end_timestamp.split('.')[0]):
                        """
                        This is checked to see if the end_timestamp is from the next day. If the end_timestamp 
                        is from the next day, it has an earlier timestamp than the first, hence the "hour"
                        corresponding to the end_timestamp will be less than that of the start_timestamp. 
                        In such a case, assign the end_timestamp to the next date.
                        
                        For example, if the start_timestamp is "22.01.01" and the end_timestamp is "06.01.01",
                        the function should return 28800.0 and not -57600.0
                        """
                        start_time = datetime.datetime(
                            year=2021,
                            month=12,
                            day=11,
                            hour=int(start_timestamp.split('.')[0]),
                            minute=int(start_timestamp.split('.')[1]),
                            second=int(start_timestamp.split('.')[2])
                        )

                        end_time = datetime.datetime(
                            year=2021,
                            month=12,
                            day=12,
                            hour=int(end_timestamp.split('.')[0]),
                            minute=int(end_timestamp.split('.')[1]),
                            second=int(end_timestamp.split('.')[2])
                        )
                    else:
                        """
                        If the start_timestamp is earlier than the end_timestamp, it means 
                        that they belong to the same day. In such a case, assign the same date to both 
                        to calculate the duration.
                        """
                        start_time = datetime.datetime(
                            year=2021,
                            month=12,
                            day=11,
                            hour=int(start_timestamp.split('.')[0]),
                            minute=int(start_timestamp.split('.')[1]),
                            second=int(start_timestamp.split('.')[2])
                        )

                        end_time = datetime.datetime(
                            year=2021,
                            month=12,
                            day=11,
                            hour=int(end_timestamp.split('.')[0]),
                            minute=int(end_timestamp.split('.')[1]),
                            second=int(end_timestamp.split('.')[2])
                        )
                except Exception as e:

                    """
                    If there happens to be any other error in processing these timestamp string literals, 
                    return the exception that has occurred.
                    """
                    print("\n An {} exception occurred when computing the duration of time between {} and {}.".format(
                        e.__class__.__name__, start_timestamp, end_timestamp))

        time_elapsed = end_time - start_time
        return start_time, end_time, time_elapsed.total_seconds()

    except TypeError:
        print("\n Please ensure that both timestamps are the same objects, either strings or datetime.datetime. "
              "Returning \"None\".")

    return None


if __name__ == "__main__":

    this_result = calculate_duration(
        start_timestamp=datetime.datetime(2021, 12, 11, 1, 3, 1),
        end_timestamp=datetime.datetime(2021, 12, 11, 5, 23, 26)
    )

    print(this_result)
