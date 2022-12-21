import logging
import time


class ExactShiftAnd:
    def __init__(self, tokens, pattern) -> None:
        start_time = time.time()
        m = len(pattern)
        n = len(tokens)
        logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            filename='logs/app.log', filemode='w',)

        try:
            print("# Exact Shift-And algorithm")
            matches = 0

            

            print(f'Total matches for pattern "{pattern}" : {matches}')
        except Exception as e:
            logging.error(f"Something went wrong: {e}")
        finally:
            print(
                f'--- Total Time: {(time.time() - start_time) * 1000} miliseconds ---')
