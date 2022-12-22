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

            m = len(pattern)
            n = len(tokens)

            if m > n:
                print(
                    "The given tokens are not enough to match pattern.")
                return

            B = {}
            for i in range(m):
                B[pattern[i]] = (B.get(pattern[i], 0) | (1 << i))

            D = 0
            for i in range(n):
                D = ((D << 1) | 1) & (B.get(tokens[i], 0))
                if D & (1 << (m - 1)):
                    matches += 1
                    print(f"Found match in position {i - m + 1}")

            print(f'Total matches for pattern "{pattern}" : {matches}')
        except Exception as e:
            logging.error(f"Something went wrong: {e}")
        finally:
            print(
                f'--- Total Time: {(time.time() - start_time) * 1000} miliseconds ---')
