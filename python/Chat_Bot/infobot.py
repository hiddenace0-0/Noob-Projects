import long_responses as long
import sql_data as sq
import API as api
import re




def message_probablity(user_message, recongnised_words, single_response=False, required_words=[], operation_response=False):
    message_certainty = 0
    has_required_words = True 
    if operation_response == True:
        for word in user_message:
            for letter in word:
                if letter in recongnised_words:
                    message_certainty+=1
    else:
        for word in user_message:
            if word in recongnised_words:
                message_certainty+=1
    
    percentage = float(message_certainty) / float(len(recongnised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break 
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0
        

def check_all_messages(message):
    highest_prob_list = {}
    
    
    def response(bot_response, list_of_words, single_response=False, required_words=[], operation_response=False):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probablity(message, list_of_words, single_response, required_words, operation_response)


    #Responses--------------------------------------------------------------------------------------------------------------
    
    response('I\'m doing fine and you?', long.hru, required_words=['how','are','doing'])
    response('Pretty good :)', long.hig, required_words=['it', 'going'])
    response('I am currently talking to you', long.wrud, required_words=['what', 'doing'])
    response('Thank you ', long.ilib, required_words=['i','love'])
    response(long.battery, long.bat_health, required_words=['what', 'battery'])
    response(long.time, long.w_time, required_words=['what', 'time'])
    response(long.birth, long.h_old, required_words=['how', 'old', 'you'])
    response(api.advice, long.c_advice, required_words=['can', 'advice'])
    response('Thats good :)', ['i\'m', 'doing', 'fine'], required_words=['fine'])

    #API Responses---------------------------------------------------------------------------------------------------------

    response('My calculations say '+ str(math_ans), ['-','+','/','*'], operation_response=True)
    response('No problem', 'thanks', required_words= ['thanks'])
    #response('Goodbye, programming ending....')
    response(a_weather(),long.w_weather, required_words=['weather'])
    response(a_weather(),long.w_temp, required_words=['temperature'])
    response(a_weather(messagez,custom=True),['@'],required_words=['@'])
    response('Not much dog',long.a1, required_words=['whats','up','dude'])
    response(a_weather(),long.a2, required_words=['weather'])
    response('Info Bot silly!', long.a3,required_words=['what','name'])
    response('I have never met a cat but I love all creatures of planet earth',long.a7,required_words=['do', 'like', 'cat'])
    response('I am from...I do know :(' , long.a8, required_words=['where','from'])
    response(a_weather(),long.a9, required_words=['what','weather'])
    #Single Response-------------------------------------------------------------------------------------------------------
    response('Thats good :)', long.poss_thats_good, single_response=True)
    response('Hello!', long.poss_hi, single_response=True)
    response('Oh, I\'m sorry to hear that I hope you feel better soon',long.poss_bad, single_response=True)
    response('No, I physically I do not i am a program but, I wish I could so bad', long.a4)
    response('My favorite color like the devils tail',long.a5, required_words=['what','favorite','colour'])
    response(spell(),long.a6,required_words=['spell'])
    #print(highest_prob_list)
    best_match = max(highest_prob_list, key=highest_prob_list.get)

    if highest_prob_list[best_match] < 1:
        sq.insert_response(messagez)
   
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(message):
    global math_ans, messagez
    messagez = message
    math_ans = operations(message)
    split_message = re.split(r'\s+|[,;?!.-]\s*', message.lower())
    response = check_all_messages(split_message)
    return response


def operations(user_input):
    numbers = [int(s) for s in re.findall(r'\b\d+\b', user_input)]
    operation = [s for s in re.findall(r'[-,+,/,*]', user_input)]
    if len(numbers) > 1:    
        result = numbers.pop(0)
        while numbers:
            for symbol in operation:
                if symbol == '*':
                    result = result * numbers.pop(0)
                elif symbol == '-':
                    result = result - numbers.pop(0)
                elif symbol == '+':
                    result = result + numbers.pop(0)
                elif symbol == '/':
                    result = result / numbers.pop(0)
            return result
    else:
        return False


def a_weather(location=None, custom=False):
    w = api.weather(long.c_location.lower())
    if custom == False:
        if w[0] == 'span':
            result = 'Unable to find the current temperature\n(Tip: If you would like to know the location that is else where, just type: @ Location)'
        else:
            result = 'My reports show - '+ w[0]+', '+ w[1]+'\n(Tip: If you would like to know the location that is else where, just type: @ Location)'
        return result
    elif custom == True:
        s = api.weather(location[1:len(location)])
        if s[0] == 'span':
            result = 'Unable to find the current temperature'
        else:
            result = 'My reports show - '+ s[0]+', '+ s[1]
    return result


def upload(): 
    count = 0
    sen = sq.get_response_by_num()
    length = (len(sen))
    #show_responses()
    print("Adding to long_responses.py...")
    set = input('What will you label this set ')
    for i in range(length):
        count+=1
        # print(("done"))
        # print(sen[i][1].split())
        with open('long_responses.py', 'a') as f:
            f.write(set+str(count)+'='+ str(sen[i][1].split())+"\n")
            f.write('#response('','')\n')
    for i in range(length):
        sq.remove_responses(sen[i][1])
        print(sen[i][1])
    #show_responses()

def show_responses():
    ans = sq.get_response_by_num()
    print(ans)

def spell():
    m =messagez
    s = m.find('spell')+6
    x = (m[s:len(m)])
    result = []
    for letter in x:
        result.append(letter)
    return str(result)
    


# upload()

# print(spell())