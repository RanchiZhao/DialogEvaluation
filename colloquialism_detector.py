from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
class ColloquialismDector:
    def __init__(self):
        self.chat = ChatOpenAI(temperature=0.0)
        self.template_string = """There's now a sentence from daily conversations generated by a language model.\n
        Your task is: Judge whether this sentence conforms to the habitual expressions of daily spoken language. 
        Specifically, is the sentence structure simple and the words basic? You need to answer with oral/formal.\n
        ---------------\n
        example1\n
        sentence: I'm intending to depart shortly; do you require anything from the marketplace?
        judgement: formal
        example2\n
        sentence: I'm just about to initiate the preparation of dinner, would you prefer pasta or salad?
        judgement: oral
        example3\n
        sentence: I was immensely gratified by the cinematic experience last evening.
        judgement: formal
        example4\n
        sentence: Hey, that new song you shared? It's dope!
        judgement: oral
        example5\n
        sentence: Greetings, I have observed your absence recently; is everything in order?
        judgement: formal
        example6\n
        sentence: Bummer! The game's cancelled due to rain.
        judgement: oral
        example7\n
        sentence: I find myself in a state of considerable fatigue; may we postpone our conversation until the morrow?
        judgement: formal
        example8\n
        sentence: So, ready for the weekend road trip?
        judgement: oral
        ---------------\n
        sentence: {query_str}
        judgement: 
        """
        self.prompt_template = ChatPromptTemplate.from_template(self.template_string)

    def generate_response(self, query_str):
        messages = self.prompt_template.format_messages(query_str=query_str)
        response = self.chat(messages)
        return response.content

