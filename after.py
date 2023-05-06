import httpx
import re
import time
import asyncio


async def count_https_in_web_pages():
    with open('15-urls.txt', 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f.readlines()]

    async with httpx.AsyncClient() as client:
        tasks = (client.get(url) for url in urls)
        reqs = await asyncio.gather(*tasks)

    htmls = [req.text for req in reqs]

    counter_https = 0
    counter_http = 0
    for html in htmls:
        counter_https += len(re.findall("https://", html))
        counter_http += len(re.findall("http://:", html))

    print("finished parsing")
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
        asyncio.run(count_https_in_web_pages())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    stats.dump_stats(filename='better-stats.prof')


if __name__ == "__main__":
    main()
