#1.9 at date of competetion

def calc_percents(ratio,total) -> float:
    percent = float(ratio)/total
    return percent



if(__name__ == "__main__"):
    min_per_song,num_of_song = [int(i) for i in input().split()]
    songTimes = [int(i) for i in input().split()]