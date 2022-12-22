import logging
import time


class BMH:
    def __init__(self, tokens, pattern) -> None:
        start_time = time.time()
        matches = 0
        logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            filename='logs/app.log', filemode='w',)

        try:
            print("# BMH algorithm")
            m = len(pattern)
            n = len(tokens)

            if m > n:
                print(
                    "The given tokens are not enough to match pattern.")
                return

            skip = []
            for k in range(256):
                skip.append(m)
            for k in range(m - 1):
                skip[ord(pattern[k])] = m - k - 1

            skip = tuple(skip)
            k = m - 1

            while k < n:
                j = m - 1
                i = k
                while j >= 0 and tokens[i] == pattern[j]:
                    j -= 1
                    i -= 1
                if j == -1:
                    matches += 1
                    print(f"Found match in position {i}")
                k += skip[ord(tokens[k])]

            print(f'Total matches for pattern "{pattern}" : {matches}')
        except Exception as e:
            logging.error(f"Something went wrong: {e}")
        finally:
            print(
                f'--- Total Time: {(time.time() - start_time) * 1000} miliseconds ---')
