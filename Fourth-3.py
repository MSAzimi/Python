#!pip install matplotlib
#import matplotlib.pyplot as plt
try:
    name_1, name_2 = map(str, input().split())
    health_1, health_2 = map(int, input().split())
    damage_A, damage_B, damage_C = map(int, input().split())
    damages = {'A': damage_A, 'B': damage_B, 'C': damage_C}
    cards_1 = list(map(str, input().split()))
    cards_2 = list(map(str, input().split()))
    cards_3 = list(map(str, input().split()))
    for i in range(2):
        if cards_1[i] == 'A':
            cards_1[i] = damages['A']
        elif cards_1[i] == 'B':
            cards_1[i] = damages['B']
        elif cards_1[i] == 'C':
            cards_1[i] = damages['C']

    for i in range(2):
        if cards_2[i] == 'A':
            cards_2[i] = damages['A']
        elif cards_2[i] == 'B':
            cards_2[i] = damages['B']
        elif cards_2[i] == 'C':
            cards_2[i] = damages['C']
    for i in range(2):
        if cards_3[i] == 'A':
            cards_3[i] = damages['A']
        elif cards_3[i] == 'B':
            cards_3[i] = damages['B']
        elif cards_3[i] == 'C':
            cards_3[i] = damages['C']
    score_1=0
    score_2=0
    if cards_1[0]>cards_1[1]:
        score_1+=1
    elif cards_1[0]<cards_1[1]:
        score_2+=1
    if cards_2[0]>cards_2[1]:
        score_1+=1
    elif cards_2[0]<cards_2[1]:
        score_2+=1
    if cards_3[0]>cards_3[1]:
        score_1+=1
    elif cards_3[0]<cards_3[1]:
        score_2+=1
    health_1-=cards_1[1]+cards_2[1]+cards_3[1]
    health_2-=cards_1[0]+cards_2[0]+cards_3[0]
    print(f"{name_1} -> Score: {score_1}, Health: {health_1}")
    print(f"{name_2} -> Score: {score_2}, Health: {health_2}")
    #f=open("result.txt","w")
    #f.write(f"{name_1} -> Score: {score_1}, Health: {health_1}")
    #f.write(f"\n{name_2} -> Score: {score_2}, Health: {health_2}")
    #f.close()
    #a = open("result.txt", "r")
    #print(a.read())
    #persons = [f"{name_1}",f"{name_2}"]
    #scores = [f"{score_1}",f"{score_2}"]

    #plt.bar(persons, scores, color='skyblue')
    #plt.xlabel('person')
    #plt.ylabel('score')
    #plt.title('Plot for carting game')
    #plt.show()
except:
    print('Invalid Command.')
    #f=open("result.txt","w")
    #f.write('Invalid Command.')
    #f.close()
    #a=open("result.txt","r")
    #print(a.read())