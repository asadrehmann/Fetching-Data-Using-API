from data_utils import to_dataframe, save_csv


def fetch_and_save_raw(endpoint, start=1, end=200):
    all_data = fetch_all_pages(endpoint, start, end)

    df = to_dataframe(all_data)

    file_path = f"data/raw/{endpoint}_movies.csv"
    save_csv(df, file_path)

    return df