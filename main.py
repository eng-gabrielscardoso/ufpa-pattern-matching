#!/usr/bin/env python3

import logging
from src.app import App


def main():
    logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filename='logs/app.log', filemode='w',)

    try:
        app = App()
    except Exception as e:
        logging.error(f'Something went wrog: {e}', exc_info=True)


if __name__ == "__main__":
    for i in range(10):
        print(f"\n ######## Execution {i + 1} ########\n")
        main()
