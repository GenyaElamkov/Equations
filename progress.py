from time import sleep

from tqdm import tqdm


def progress_bar(counter: int) -> None:
    for _ in tqdm(range(counter), ncols=80, ascii=True, desc='Total'):
        sleep(0.1)
