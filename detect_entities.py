import spacy
nlp = spacy.load('xx_ent_wiki_sm')

def entites(text, lang=None):
    return [{"text":str(x), "type":x.label_, "start_pos":x.start_char, "end_pos":x.end_char} for x in nlp(str(text)).ents]
