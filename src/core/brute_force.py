import logging
import time


class BruteForce:
    def __init__(self, tokens, pattern) -> None:
        start_time = time.time()
        index = 0
        matches = 0
        logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            filename='logs/app.log', filemode='w',)

        try:
            print("# Brute force algorithm")
            for word in tokens:
                if word == pattern:
                    print(f"Found match in position: {index}")
                    matches += 1
                index += 1

            print(f'Total matches for pattern "{pattern}" : {matches}')
        except Exception as e:
            logging.error(f"Something went wrong: {e}")
        finally:
            print(
                f'--- Total Time: {(time.time() - start_time) * 1000} miliseconds ---')
