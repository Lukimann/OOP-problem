class Scores:
 def all_scores(participants):
    scores = []

    for participant in participants:
        name = participant['name']
        score = participant['chickenwings'] * 5 + participant['hamburgers'] * 3 + participant['hotdogs'] * 2
        scores.append({'name': name, 'score': score})
    
    scores.sort(key=lambda x: (-x['score'], x['name']))
    return scores