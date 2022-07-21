from string import Template
import json
template_first = Template("""Dear $place, and $person1, and $person2, $person3, $person4, $person5 and $person6: I thank you for your friendly letters. You sure know how to cheer up a really old geezer ($ages) in his sunset years. I don’t make public appearances any more because I now resemble nothing so much as an iguana.
What I had to say to you, moreover, would not take long, to wit: Practice any art, music, singing, dancing, acting, drawing, painting, sculpting, poetry, fiction, essays, reportage, no matter how well or badly, not to get money and fame, but to experience becoming, to find out what’s inside you, to make your soul grow.
Seriously! I mean starting right now, do art and do it for the rest of your lives. Draw a funny or nice picture of Ms. Lockwood, and give it to her. Dance home after school, and sing in the shower and on and on. Make a face in your mashed potatoes. Pretend you’re Count Dracula.
Here’s an assignment for tonight, and I hope Ms. Lockwood will flunk you if you don’t do it: Write a six line poem, about anything, but rhymed. No fair tennis without a net. Make it as good as you possibly can. But don’t tell anybody what you’re doing. Don’t show it or recite it to anybody, not even your girlfriend or parents or whatever, or Ms. Lockwood. OK?
Tear it up into teeny-weeny pieces, and discard them into widely separated trash recepticals. You will find that you have already been gloriously rewarded for your poem. You have experienced becoming, learned a lot more about what’s inside you, and you have made your soul grow.
God bless you all!
$writer""")
place, person1, person2, person3, person4, person5, person6, ages, writer = "place", "1", "2", "3", "44", "55", "66", 700, "me"
print(template_first.substitute(place=place, person1=person1, person2=person2, person3=person3, person4=person4, person5=person5, person6=person6, ages=ages, writer=writer))

text = open("txthomework.txt", "r")
template_second = Template(text.read())
print(template_second.substitute(place=place, person1=person1, person2=person2, person3=person3, person4=person4, person5=person5, person6=person6, ages=ages, writer=writer))

jsonfile = open("jsonfolder/jsonforhomework.json")
jsontext = json.load(jsonfile)
print(template_second.substitute(
    place=jsontext["place"],
    person1=jsontext["person1"],
    person2=jsontext["person2"],
    person3=jsontext["person3"],
    person4=jsontext["person4"],
    person5=jsontext["person5"],
    person6=jsontext["person6"],
    ages=jsontext["ages"],
    writer=jsontext["writer"]))
