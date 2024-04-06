from typing import Union


class one_element:

    def __init__(self, coordinates: Union[list[int, int], bool] = False, test_percent_existing: int = 0, replacement_type: str = "mean"):
        """
        Choose proper strategy parameters.

        test_percent_existing:  give int in range 0-100.
        replacement_type:       give one of following:    "mean", "median" , "zero", "ones", "maximal", "minimal", "dynamic_mean"
        """

        # default attributes (false if not given)
        self.__properties_dict = {
                "strategy":     "one",
                "percent":      False,
                "replacement":  False,
                "columns":      False,
                "rows":         False,
                "results":      False
            }

        # using public functions to save attributes
        self.change_test_percent_existing(test_percent_existing)
        self.change_test_replace_type(replacement_type)
        if coordinates: self.change_coordinates(coordinates)


    def change_coordinates(self, x: int, y: int):
        "Change coordinates."
        self.__properties_dict["columns"] = [x]
        self.__properties_dict["rows"]    = [y]


    def change_test_percent_existing(self, test_percent_existing: int):
        "Changing class parameter, give int in range 0-100."

        # if given input is corresponding
        if test_percent_existing >= 0 and test_percent_existing <= 100:
            self.__properties_dict["percent"] = test_percent_existing
            return [True]

        # if given value is not considerable
        else:
            message = "Wrong percent ranage (not in [0-100])."
            print(message)
            return [False, message]


    def change_test_replace_type(self, replacement_type: str):
        """
        Changing replacement type, give one of below:
        "mean", "median" , "zero", "ones", "maximal", "minimal"
        "dynamic_mean"
        """

        # if given input is corresponding
        if replacement_type in ["mean", "median" , "zero", "ones", "maximal", "minimal", "dynamic_mean"]:
            self.__properties_dict["replacement"] = replacement_type
            return [True]

        # if given value is not considerable
        else:
            message = "Wrong attribute given, choose one of mentioned. [one_elemenet, change_test_replace_type, not] "+str(replacement_type)
            print(message)
            return [False, message]


    def give_dict(self):
        "Gives dictionary ready to use by a filling machine."
        # output dictionary:
        return self.__properties_dict




class series_column(one_element):

    def __init__(self, which_column: Union[int, bool] = False, test_percent_existing: int = 0, replacement_type: str = "mean", row_order: Union[str, list[int]] = "up_to_down"):
        """
        Choose proper strategy parameters.

        test_percent_existing:  give int in range 0-100.
        replacement_type:       give one of following:    "mean", "median" , "zero", "ones", "maximal", "minimal", "dynamic_mean"
        row_order:              give one of following: "up_to_down", "down_to_up"
                                or list of int where every given number means column to be considered
        """

        # executing init function from parent class
        super().__init__(False, test_percent_existing=test_percent_existing, replacement_type=replacement_type)
        #super().__init__(test_percent_existing, replacement_type)

        # default attributes (false if not given)
        self.__row_order       = False
        self.__column             = False

        # using public functions to save attributes
        self.change_row_order(row_order)
        if which_column: self.change_column(which_column)


    def change_column(self, which_column: int):
        "Change column."
        self.__properties_dict["columns"] = [which_column]


    def change_row_order(self, row_order: Union[str, list[int]]):
        """
        Changing execute order, type, give one of below:
        "up_to_down", "down_to_up"
        or list of int where every given number means column to be considered
        """

        # if given input is str
        if isinstance(row_order, str):

            # if given input is corresponding
            if row_order in ["up_to_down", "down_to_up"]:
                self.__properties_dict["rows"] = row_order
                return [True]

            # if given input is not considerable
            else:
                message = "Wrong attribute given, choose one of mentioned. [series_column, change_row_order, str] " + str(row_order)
                print(message)
                return [False, message]

        # if given input is list
        elif isinstance(row_order, list):

            # if given elements are unique
            if len(row_order) > len(set(row_order)):
                self.__properties_dict["rows"] = row_order
                return [True]

            # if given values are not unique
            else:
                message = "Elements in list are not unique."
                print(message)
                return [False, message]

        # if given value is not considerable
        else:
            message = "Wrong attribute given, choose one of mentioned. [series_column, change_row_order, not] " + str(row_order)
            print(message)
            return [False, message]


class series_table(series_column):

    def __init__(self, test_percent_existing: int = 0, replacement_type: str = "mean", include_results: bool = False, in_row_order: Union[str, list[int]] = "up_to_down", in_column_order: Union[str, list[int]] = "left_to_right"):#in_row_order: Union[str, list[int]] = "left_to_right", in_column_order: Union[str, list[int]] = "up_to_down")
        """
        Choose proper strategy parameters.

        test_percent_existing:  give int in range 0-100.
        replacement_type:       give one of following:    "mean", "median" , "zero", "ones", "maximal", "minimal", "dynamic_mean"
        in_column_order:        give one of following: "up_to_down", "down_to_up"
                                or list of int where every given number means column to be considered
        in_row_order:           give one of following: "left_to_right", "right_to_left"
                                or list of int where every given number means column to be considered
        """

        # executing init function from parent class
        super().__init__(False, test_percent_existing=test_percent_existing, replacement_type=replacement_type, row_order=in_row_order)

        # default attributes (false if not given)
        self.__in_row_order         = False
        self.__include_results      = False

        # using public functions to save attributes
        self.change_row_order(in_row_order)
        self.change_include_results(include_results)


    def change_column_order(self, column_order: Union[str, list[int]]):
        """
        Changing execute order, type, give one of below:
        "up_to_down", "down_to_up"
        or list of int where every given number means column to be considered
        """

        # if given input is str
        if isinstance(column_order, str):

            # if given input is corresponding
            if column_order in ["up_to_down", "down_to_up"]:
                self.__properties_dict["columns"] = column_order
                return [True]

            # if given input is not considerable
            else:
                message = "Wrong attribute given, choose one of mentioned. [series_table, change_row_order, str] " + str(in_row_order)
                print(message)
                return [False, message]

        # if given input is list
        elif isinstance(column_order, list):

            # if given elements are unique
            if len(column_order) > len(set(column_order)):
                self.__properties_dict["columns"] = column_order
                return [True]

            # if given values are not unique
            else:
                message = "Elements in list are not unique."
                print(message)
                return [False, message]

        # if given value is not considerable
        else:
            message = "Wrong attribute given, choose one of mentioned. [series_table, change_row_order, not] " + str(in_row_order)
            print(message)
            return [False, message]


    def change_include_results(self, include_results: bool):
        "Changing class parameter, give int in range 0-100."

        self.__properties_dict["results"] = include_results
        return [True]
