import pandas as pd


class DataCleaner:
    """
    Takes only path: str
    """

    def __init__(self, path: str):
        self.path = path

    def clean_data(self):
        try:
            ignore_emails = self.get_ignore_emails()
            data = pd.read_csv(self.path)
            data['Email'] = data['Email'].str.lower()
            unique_emails = data.drop_duplicates(['Email'])
            drop_na = unique_emails[unique_emails['Email'].notna()]
            result = drop_na[['Email', 'First Name', 'Last Name']]
            result = result[~result['Email'].isin(ignore_emails)]
            self.save(result)
            return True

        except FileNotFoundError:
            raise FileNotFoundError('File Not Found')

    @staticmethod
    def get_ignore_emails():
        try:
            with open('_internal/ignore_emails.txt', 'r') as f:
                lines = f.readlines()
                if len(lines) > 0:
                    return [line[:-1] for line in lines]
                return []
        except FileNotFoundError:
            return []

    def save(self, result: pd.DataFrame):
        new_file_name = 'Cleaned Bookings.csv'
        new_file_path = self.path.split('/')
        new_file_path[-1] = new_file_name
        new_file_path = '/'.join(new_file_path)
        result.to_csv(new_file_path, index=False)
        return
