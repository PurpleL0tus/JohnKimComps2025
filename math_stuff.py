import random
import scipy.stats as stats

def normal_distribution(mean, std_dev, lower_bound=0, upper_bound=10):
    while 0 == 0:
        random_value = stats.norm.rvs(loc=mean, scale=std_dev)
        if lower_bound <= random_value <= upper_bound:
            return round(random_value)



random_val = normal_distribution(3, 1)
print(f"result: {random_val}")
