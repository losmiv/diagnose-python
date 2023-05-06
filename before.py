import requests
import re
import time


def count_https_in_web_pages():
    with open('15-urls.txt', 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f.readlines()]

    htmls = []
    for url in urls:
        htmls = htmls + [requests.get(url).text]

    counter_https = 0
    counter_http = 0
    for html in htmls:
        counter_https += len(re.findall("https://", html))
        counter_http += len(re.findall("http://:", html))

    print("finished parsing")
    time.sleep(2.0)
    print(f'{counter_https=}')
    print(f'{counter_http=}')
    # print(f'{counter_https/counter_http=}')


def main():
    """
    start = time.perf_counter()
    count_https_in_web_pages()
    elapsed = time.perf_counter() - start
    print(f'done in {elapsed:.2f}s')
    """
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        count_https_in_web_pages()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    stats.dump_stats(filename='stats.prof')


if __name__ == "__main__":
    main()
