import pandas as pd


class DataCleaner:
    """
    If split, then splits by 200 and outputs several files, otherwise outputs one file

    path: str
    split: bool
    """

    def __init__(self, path: str, split: bool):
        self.path = path
        self.split = split
        self.ignore_zonal = '@zonal.co.uk'
        self.ignore_test = 'test'

    def clean_data(self):
        """
        Reads the .csv file from the path given, and cleans the data.
            1 - Converts Email to lowercase
            2 - Removes duplicate Emails and notna values
            3 - Ignores emails that are in the ignore_emails list

        :return: bool or raises
        """
        try:
            ignore_emails = self.get_ignore_emails()
            data = pd.read_csv(self.path)

            # Remove Empty Values
            data['Email'] = data['Email'].str.lower()
            unique_emails = data.drop_duplicates(['Email'])
            drop_na = unique_emails[unique_emails['Email'].notna()]
            result = drop_na[['Email', 'First Name', 'Last Name']]
            result.loc[:, 'Email'] = result['Email'].astype(str)

            # Capitalize First and Last name
            result['First Name'] = result['First Name'].str.capitalize()
            result['Last Name'] = result['Last Name'].str.capitalize()

            # Remove zonal support emails and tests
            result = result[(~result.Email.str.endswith(self.ignore_zonal) & ~result.Email.str.contains(self.ignore_test))]

            # Remove emails that are in the ignore list
            result = result[~result['Email'].isin(ignore_emails)]
            self.save(result)
            return True

        except FileNotFoundError:
            raise FileNotFoundError('File Not Found')

    @staticmethod
    def get_ignore_emails():
        """
        Checks whether you have selected emails to ignore, and returns them formated without the /n at the end.

        :return: list
        """
        try:
            with open('_internal/ignore_emails.txt', 'r') as f:
                lines = f.readlines()
                if len(lines) > 0:
                    return [line.replace('\n', '') for line in lines] # takes off the new line
                return []
        except Exception:
            return []

    def save(self, result: pd.DataFrame):
        """
        Creates an output file in the same dir as the .csv input file or several files depending on self.split value

        :param result: pd.DataFrame
        :return: None
        """
        output_list = self.split_two_hundred(result) if self.split else [result]
        name = ' 200' if len(output_list) > 1 else ''

        for index in range(len(output_list)):
            new_file_name = f'Cleaned Bookings{name}-{index + 1}.csv'
            new_file_path = self.path.split('/')
            new_file_path[-1] = new_file_name
            new_file_path = '/'.join(new_file_path)
            output_list[index].to_csv(new_file_path, index=False)
        return

    @staticmethod
    def split_two_hundred(entry_df: pd.DataFrame):
        """
        Takes the DataFrame and splits the results by 200 entries, if self.split

        :param entry_df: pd.DataFrame
        :return: list
        """
        max_rows = 200
        num_splits = (len(entry_df) // max_rows) + 1

        output_list = []

        for i in range(num_splits):
            start_index = i * max_rows
            end_index = min(start_index + max_rows, len(entry_df))
            output_list.append(entry_df.iloc[start_index:end_index])

        return output_list
