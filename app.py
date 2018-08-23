import io

import hug
from pandas import read_csv


@hug.post('/csv/sort')
def csv_sort(content: hug.types.text):
    """Sorts data from content attribute and returns JSON to user."""

    data_frame = read_csv(io.StringIO(content), sep='\t', header=None)
    data_frame = data_frame.sort_values(by=list(data_frame.columns.values))
    csv_data = data_frame.to_csv(sep='\t', header=None, index=False)
    return {'result': csv_data}
