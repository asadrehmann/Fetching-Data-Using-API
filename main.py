from tmdb_api import fetch_and_save_raw


def main():
    endpoint = "popular"

    df = fetch_and_save_raw(endpoint, 1, 200)

    print(df.shape)
    print(df.head())


if __name__ == "__main__":
    main()