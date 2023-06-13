import os
os.environ["OPENAI_API_KEY"] = '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'
from friendliness_detector import FriendlinessDetector
from colloquialism_detector import ColloquialismDector
from topic_transition_detector import TopicTransitionDetector

if __name__ == '__main__':
    query_list = ['Sort of . I played golf on my computer !', 'What ? ! You did that ? ? ! ! !']
    context_list = [('"Hi , Nicole . Did you have a good weekend ? ", " Yes , I did . But I feel tired today . ", " Really ? Why ? ", " Well , on Saturday I cleaned the house and played tennis . Then on Sunday I hiked in the country . ", " And I bet you studied , too . ", " Yeah . I studied on Sunday evening . What about you ? ", " Well , I didn\'t clean the house and I didn\'t study . I stayed in bed and watched TV . ", " That sounds like fun , but did you exercise ? "', '" Sort of . I played golf on my computer ! "'),('"Congratulations , Vivian . You won the grand prize , again . ", " Isn\'t it just great ! I just knew I\'d win ! ", " You did ? How ? Did you wear red underwear again this year ? ", " Not only that ! ", " Tell me ! Tell me ! What\'s your secret ? ! ", " OK , OK . I\'ll whisper it to you , but you have to promise not to tell anyone ! "','" What ? ! You did that ? ? ! ! ! "')]
    friendliness_num = 0
    colloquialism_num = 0
    topic_transition_num = 0
    for query in query_list:
        friendliness_detector = FriendlinessDetector()
        friendliness = friendliness_detector.generate_response(query)
        print("friendliness:", friendliness)
        if friendliness == 'friendly':
            friendliness_num += 1

        colloquialism_detector = ColloquialismDector()
        colloquialism = colloquialism_detector.generate_response(query)
        print("colloquialism:", colloquialism)
        if colloquialism == 'oral':
            colloquialism_num += 1

    friendliness_ratio = friendliness_num / len(query_list)
    colloquialism_ratio = colloquialism_num / len(query_list)

    for context_query in context_list:
        context, query = context_query
        topic_transition_detector = TopicTransitionDetector()
        topic_transition = topic_transition_detector.generate_response(query, context)
        print("topic_transition", topic_transition)
        if topic_transition == 'yes':
            topic_transition_num += 1

    topic_transition_ratio = topic_transition_num / len(query_list)

    print("friendliness_ratio: ", friendliness_ratio)
    print("colloquialism_ratio: ", colloquialism_ratio)
    print("topic_transition_ratio: ", topic_transition_ratio)
