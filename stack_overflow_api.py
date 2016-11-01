from stackexchange import Site, StackOverflow
import json
import os
so = Site(StackOverflow, 'COq7tST2*12CYE9j8BA)CQ((')
questions_list = []
user_id = []
users = {}
rep_user_map = {}
badge_user_map = {}
badges = {'gold': 0, 'silver':0, 'bronze':0}
count = 0
questions = {}
tags = []
for question in so.questions(tagged=['python', 'pandas'], pagesize=10):
    response = question.json
    if not response['title'] in questions:
        questions[response['title']] = {}
    questions[response['title']]['tags'] = response['tags']
    tags.append(response['tags'])
    questions[response['title']]['answered'] = response['answer_count']
    if 'user_id' in response['owner']:
        questions_list.append(response['title'])
        user_id.append(response['owner']['user_id'])
        user_obj = so.user(response['owner']['user_id'])
        if not response['owner']['user_id'] in users:
            users[response['owner']['user_id']] = {}
        badge_user_map[user_obj.badge_total] = user_obj
        users[response['owner']['user_id']]['badge'] = user_obj.badge_total
        users[response['owner']['user_id']]['reputaion'] = user_obj.reputation
        users[response['owner']['user_id']]['url'] = user_obj.json['link']
        users[response['owner']['user_id']]['user_name'] = user_obj.json['display_name']
        users[response['owner']['user_id']]['user_id'] = response['owner']['user_id']
        rep_user_map[user_obj.reputation] = users[response['owner']['user_id']]
        if 'badge_counts' in user_obj.json:
            for badge_type in badges.keys():
                if badge_type in user_obj.json['badge_counts']:
                    badges[badge_type] = badges[badge_type] + 1
        tags_list= []
        for tag in user_obj.tags.fetch():
           tags_list.append(tag)
        users[response['owner']['user_id']]['tags'] = tags_list
        count+=1
    if count > 50:
        break

top_weight_user = badge_user_map.keys()
top_weight_user.sort()
top_weight_user = top_weight_user[-1]
top_weight_user_obj = badge_user_map[top_weight_user]
top_ques = []
for ques in top_weight_user_obj.top_questions_in_tag(['python','pandas']):
    top_ques.append(ques.title)

tags = [item for sublist in tags for item in sublist]
tags = list(set(tags))

ques4 = {}
for t in tags:
    obj = so.tag(t)
    ques4[t] = obj.count



print ("questions_list")
print (questions_list)
print ("\nuser ids")
print (user_id)
print ("top questions according to the weightage.\n")
print (top_ques)



rep_user = rep_user_map.keys()
rep_user.sort()
for item in ['pandas', 'python']:
    with open("/tmp/%s_topic.txt"%item, 'w') as f:
        for user in rep_user:
            f.write(str(rep_user_map[user]['user_id'])+",")
            f.write(rep_user_map[user]['user_name']+",")
            f.write(rep_user_map[user]['url']+"\n")
print ("Successfully written the results to the following files /tmp/pandas.txt /tmp/python.txt")


for key, value in badges.iteritems():
    print ("%s : %s"%(key,value))



for key, value in questions.iteritems():
    print ("Question  --->%s"%key)
    print ("Tags --->%s"%str(value['tags']))

for key, value in questions.iteritems():
    print ("Question --->%s"%key)
    print ("Number of answers --->%s"%value['answered'])


for key, value in ques4.iteritems():
    print ("Tag %s  Number of Questions %s"%(key, value))


