import json, requests

with open('wl.json', encoding='utf-8') as f:
    words = json.load(f)

word_count = len(words)
url = 'https://www.random.org/integers/?num=3&min=1&max={wc}&col=1&base=10&format=plain&rnd=new'.format(wc=word_count)
r = requests.get(url)
nums = r.text.strip().split('\n')
sel_words = [words[int(num) - 1] for num in nums]
print('-'.join(sel_words))