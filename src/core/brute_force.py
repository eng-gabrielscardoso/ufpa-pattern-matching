import time


class BruteForce:
    def __init__(self, tokens, pattern) -> None:
        start_time = time.time()
        index = 0
        matches = 0

        print("# Brute force algorithm")
        for word in tokens:
            if word == pattern:
                print(f"Found match in position: {index}")
                matches += 1
            index += 1

        print(f'Total matches for pattern "{pattern}" : {matches}')
        print(
            f'--- Total Time: {(time.time() - start_time) * 1000} miliseconds ---')
