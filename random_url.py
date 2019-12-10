import string
import random

def url_gen(candidate_id,job_id):
    KEY_LEN = random.randint(8,16)
    urllist = [random.choice((string.ascii_letters+string.digits)) for i in range(KEY_LEN)]
    return (f'{candidate_id}/{job_id}/{"".join(urllist)}')
for i in range(20):
    print(url_gen(1,1))