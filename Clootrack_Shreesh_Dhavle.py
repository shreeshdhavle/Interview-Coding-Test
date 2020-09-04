from collections import Counter

num_test_cases = int(input("Enter the number of tweet test case/cases:"))
num_test_count = 0
tweet_names = []

while num_test_count < num_test_cases:
	num = int(input("Enter the number of Tweet Test Case:"))
	counts = 0
    
	while counts < num:
		name = str(input("Enter the twitter name followed by the ID: "))
		tweet_names.append(name)
		counts += 1

	num_test_count += 1

tweet_names = [names.split()[0] for names in tweet_names]
count_tweet = Counter(tweet_names)

repeat = count_tweet.values()

for element in set(repeat):
	duplicate = ([(name, count) for name, count in sorted(count_tweet.items()) if count == element])

	if len(duplicate) > 1:
		for (name, count) in duplicate:
			print (name,'',count)

	max_count = max(count_tweet.values())
	max_result = [(name, count) for name, count in sorted(count_tweet.items()) if count == max_count]

	if max_result != duplicate:
		for (name, count) in max_result:
			print (name,'',count)
