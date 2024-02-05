"""
Новогодние свечки
Программист Василий любит романтику — поэтому на этот Новый Год он решил освещать свою комнату свечами.

У Василия есть a свечей. Когда Василий зажигает новую свечу, сначала она горит ровно один час, а затем тухнет. Василий — сообразительный малый, поэтому из b потухших свечей он умеет получать одну новую свечу. В последствии эту новую свечу (так же как и другие новые свечи) можно зажечь.

Теперь Василию интересно, на сколько часов освещения хватит его свечек, если он будет действовать оптимальным образом. Помогите ему найти это число.
"""
a, b = map(int, input().split())
time = 0
while a > 0:
    a -= 1
    time += 1
    if time % b == 0:
        a += 1
print(time)
