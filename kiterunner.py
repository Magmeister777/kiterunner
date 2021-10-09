import time

exit_message = """------------------------------------------ \n Thanks for using KiteRunner101 
             \n for you a thousand times over \n -----------------------------------------------------"""
characters_dict = {"amir": """
The central character of the story as well as its narrator, Amir has a privileged upbringing. His father, Baba, is rich by Afghan standards, and as a result, Amir grows up accustomed to having what he wants. The only thing he feels deprived of is a deep emotional connection with Baba, which he blames on himself. He thinks Baba wishes Amir were more like him, and that Baba holds him responsible for killing his mother, who died during his birth. Amir, consequently, behaves jealously toward anyone receiving Baba’s affection. His relationship with Hassan only exacerbates this. Though Hassan is Amir’s best friend, Amir feels that Hassan, a Hazara servant, is beneath him. When Hassan receives Baba’s attention, Amir tries to assert himself by passive-aggressively attacking Hassan. He mocks Hassan’s ignorance, for instance, or plays tricks on him. At the same time, Amir never learns to assert himself against anyone else because Hassan always defends him. All of these factors play into his cowardice in sacrificing Hassan, his only competition for Baba’s love, in order to get the blue kite, which he thinks will bring him Baba’s approval""", 
"hassan": "If Amir’s character arc is about growth, Hassan’s arc is about not changing at all. From the start and through his death, Hassan remains the same: loyal, forgiving, and good-natured. As a servant to Baba and Amir, Hassan grows up with a very particular role in life. While Amir prepares for school in the morning, Hassan readies Amir’s books and his breakfast. While Amir is at school getting an education, Hassan helps Ali with the chores and grocery shopping. As a result, Hassan learns that it is his duty to sacrifice himself for others. Furthermore, by nature he is not prone to envy, and he even tells Amir he is happy with what he has, though he sees all the time how much more Amir has. Hassan comes across as the personification of innocence as a result, and this innocence is crucial in creating the drama and symbolism of his rape by Assef. First, Hassan’s innocence gives Amir no justifiable reason to betray Hassan. Amir’s behavior cannot be rationalized, making it consummately selfish and reprehensible. Second, Hassan’s rape becomes the sacrifice of an innocent, a recurring motif in Islam, Christianity, and Judaism that carries a great deal of symbolic meaning.", 
"baba": """In his words and actions, Baba sets the moral bar in the novel. When Amir is a boy, Baba’s major concern about him is that he doesn’t have the courage to stand up for himself, demonstrating that Baba places great value on doing what is right. If Amir cannot take of himself as a boy, he worries, he will not have the strength to behave morally as an adult. Baba follows through on these beliefs in his own behavior. When he and Amir flee Kabul, he is willing to sacrifice his life to keep the Russian guard from raping the woman with them, and in doing so he sets the example that Amir will follow later when he must choose between saving himself or doing what he knows to be right.
What the reader sees of Baba from Amir’s narrative is not the full story, however. As Amir describes him, he is proud, independent, determined, but sometimes emotionally distant and impatient. We learn from a note Rahim Khan writes to Amir toward the end of the book that Baba was a man torn between two halves, specifically between Amir and Hassan. Amir never sees Baba’s inner conflict because Baba has very much separated his outward appearance from his internal emotions. For instance, Baba builds an orphanage, which appears to be a simple act of charity. But as Rahim Khan explains, Baba built the orphanage to make up for the guilt he felt for not being able to acknowledge Hassan as his son. Baba’s hesitation to reveal his emotions causes Amir to feel that he never knows Baba completely, alienating Amir from Baba while Amir is growing up.""",
"ali": """In many ways, Ali is a parallel character to Hassan. Both share the same social status as poor, ethnic Hazaras, both are devoted childhood friends to Baba and Amir respectively, and both have physical deformities. Most significantly, both characters deal with betrayal at the hands of their masters. Baba has sex with Ali’s wife, setting into motion all of the interpersonal betrayals that occur throughout the novel. Despite this infidelity, Ali remains a dedicated servant to Baba. Ali represents a particularly faithful, traditional Muslim perspective. None of the other characters in the novel overtly display this same level of faith, and Hosseini presents it as part of Ali’s admirable moral fortitude. Ali is also the first person to learn what happened between Hassan and Amir in the alley. Because of this knowledge, Ali allows Hassan to lie about stealing Amir’s watch and birthday money, causing Ali and Hassan’s departure from Baba’s household. In this heartbreaking and ultimately self-sacrificing act, Ali, despite his limited social power, does what he can to protect his son from Amir’s betrayal.""", 
"sohrab": """Throughout the end of The Kite Runner, Sohrab acts as an extension of Hassan. In addition to their “breathtaking” physical similarities, both characters are born and raised in the same hut, both are sexually abused by the same man, both kite-run with Amir, and both carry a slingshot. Hassan threatens to take out Assef’s eye with his slingshot, and nearly a quarter-century later, Sohrab makes good on the threat. In fact, the parallels between Hassan and Sohrab are so numerous that the reader could treat the two as one character, which is important and necessary for Amir’s narrative arc. Amir cannot make amends with Hassan because he is dead, but by rescuing Sohrab, Amir attempts to atone for his betrayal of Hassan. However, Sohrab diverges from his father in that the dark aftermath of his sexual abuse is described. Believing that he is “dirty and full of sin,” Sohrab flinches at Amir’s touch and retreats into himself, “fists buried in his armpits.” He attempts suicide when he believes Amir will abandon him, an act that ultimately acts as a catalyst for a renewal of Amir’s faith as he begs Allah to save Sohrab in the hospital.""",
"assef": """Assef encompasses all that is evil in Afghanistan. The reader first meets Assef as a violent, racist child who draws his social power from his economic and ethnic identity, and wants to rid his country of all Hazaras. Assef’s rape of Hassan is a dramatic and explicit example of those with social privilege violating those without. Adult Assef becomes a Taliban leader and continues embracing Afghanistan’s most vicious and bigoted beliefs, ultimately personifying racism and abuse.

Assef also shares many characteristics with Amir. Both children grow up with a measure of privilege, and both children hurt Hassan—a socially and economically disadvantaged Hazara—when they abuse this privilege. As Amir fights Assef to save Sohrab, he is ultimately fighting the darkest part of himself that betrayed Hassan. Assef is the most unambiguously evil character in the novel, emphasized by the fact that Assef’s hero as a child is Adolf Hitler. Significantly, Assef does not die in the novel, insinuating that the cruelest parts of Afghanistan cannot be easily or fully extinguished."""}


symbols_dict = {"kites": """The kite serves as a symbol of Amir’s happiness as well as his guilt. Flying kites is what he enjoys most as a child, not least because it is the only way that he connects fully with Baba, who was once a champion kite fighter. But the kite takes on a different significance when Amir allows Hassan to be raped because he wants to bring the blue kite back to Baba. His recollections after that portray the kite as a sign of his betrayal of Hassan. Amir does not fly a kite again until he does so with Sohrab at the end of the novel. Because Amir has already redeemed himself by that point, the kite is no longer a symbol of his guilt. Instead, it acts as a reminder of his childhood, and it also becomes the way that he is finally able to connect with Sohrab, mirroring the kite’s role in Amir’s relationship with Baba.""",
"cleft lip":"Hassan’s cleft lip is one of his most representative features as a child, and it is one of the features Amir refers to most in describing him. The split in Hassan’s lip acts as a mark of Hassan’s status in society. It signifies his poverty, which is one of the things that separates him from Amir, simply because a cleft lip indicates that he and his family do not have the money to fix the deformity. Baba, who is Hassan’s biological father, chooses to pay a surgeon to repair Hassan’s lip as a birthday gift, signifying his secret fatherly love for Hassan. Later, Assef splits Amir’s lip as he beats him, leaving Amir with a permanent scar much like Hassan’s. In a sense, Amir’s identity becomes merged with Hassan’s. He learns to stand up for those he cares about, as Hassan once did for him, and he becomes a father figure to Sohrab. Because of this, it also serves as a sign of Amir’s redemption",
"lamb":"""In Islam, as in Christianity, the lamb signifies the sacrifice of an innocent. Amir describes both Hassan and Sohrab as looking like lambs waiting to be slaughtered. Amir says this during Hassan’s rape, noting that Hassan resembled the lamb they kill during the Muslim celebration of Eid Al-Adha, which honors Abraham’s near sacrifice of his son for God. Similarly, he describes Sohrab as looking like a slaughter sheep when he first sees Sohrab with Assef. Assef and the others had put mascara on Sohrab’s eyes, just as Amir says the mullah used to do to the sheep before slitting its throat. Both Hassan and Sohrab are innocents who are figuratively sacrificed by being raped, but these sacrifices have very different meanings. In Hassan’s case, Amir sacrifices him for the blue kite. But in Sohrab’s case, Amir is the one who stops his sexual abuse. In this context, sacrifice is portrayed as the exploitation of an innocent.""",}

key_facts_dict = {"narrator": "The Kite Runner is narrated by Amir four days after the final events of his decades-long story.",
"point of view": "The narrator speaks in the first person, primarily describing events that occurred months and years ago. The narrator describes these events subjectively, explaining only how he experienced them. At one point, another character briefly narrates a chapter from his own point of view.",
"tone" :"The tone is confessional, expressing profound remorse throughout the story",
"tense": "Past tense with extended flashbacks",
"setting": "Time: 1975 through 2001 \n Place: Kabul, Afghanistan; California, United States",
"protagonist": "Amir",
"major conflict": "After failing to intervene in the rape of his friend Hassan, Amir wrestles with his guilt and tries to find a way to atone for his actions.",
"rising action": "Forced out of Afghanistan by the Soviet invasion, Amir flees to the United States, where he tries to rebuild his life until an old friend offers him a way to make amends for his past."
,"climax": "Amir returns to Kabul, where he finds Hassan’s son, Sohrab, and encounters Assef, the man that raped Hassan twenty-six years earlier.",
"themes": "The search for redemption; the love and tension between fathers and sons; the intersection of political events and private lives; the persistence of the past"

}
themes_dict = {
"redemption": """"Amir’s quest to redeem himself makes up the heart of the novel. Early on, Amir strives to redeem himself in Baba’s eyes, primarily because his mother died giving birth to him, and he feels responsible. To redeem himself to Baba, Amir thinks he must win the kite-tournament and bring Baba the losing kite, both of which are inciting incidents that set the rest of the novel in motion. The more substantial part of Amir’s search for redemption, however, stems from his guilt regarding Hassan. That guilt drives the climactic events of the story, including Amir’s journey to Kabul to find Sohrab and his confrontation with Assef. The moral standard Amir must meet to earn his redemption is set early in the book, when Baba says that a boy who doesn’t stand up for himself becomes a man who can’t stand up to anything. As a boy, Amir fails to stand up for himself. As an adult, he can only redeem himself by proving he has the courage to stand up for what is right."""
,"fathers and Sons": "Amir has a very complex relationship with Baba, and as much as Amir loves Baba, he rarely feels Baba fully loves him back. Amir’s desire to win Baba’s love consequently motivates him not to stop Hassan’s rape. Baba has his own difficulty connecting with Amir. He feels guilty treating Amir well when he can’t acknowledge Hassan as his son. As a result, he is hard on Amir, and he can only show his love for Hassan indirectly, by bringing Hassan along when he takes Amir out, for instance, or paying for Hassan’s lip surgery. In contrast with this, the most loving relationship between father and son we see is that of Hassan and Sohrab. Hassan, however, is killed, and toward the end of the novel we watch Amir trying to become a substitute father to Sohrab. Their relationship experiences its own strains as Sohrab, who is recovering from the loss of his parents and the abuse he suffered, has trouble opening up to Amir."
,"politics":"The major events of the novel, while framed in the context of Amir’s life, follow Afghanistan’s transitions as well. In Amir’s recollections of his childhood, we see the calm state of Kabul during the monarchy, the founding of the republic, and then watch as the Soviet invasion and infighting between rival Afghan groups ruin the country. These events have a hand in dictating the novel’s plot and have significant effects on the lives of the characters involved. The establishment of the republic gives Assef an opportunity to harass Amir, simply because Assef’s father knows the new president. Later, Kabul’s destruction forces Baba and Amir to flee to California. When the Taliban take over after that, they murder Hassan and even give Assef a position that lets him indulge his sadism and sexual urges without repercussions. Both of these events factor into Amir’s mission to save Sohrab and his redemption by confronting Assef, subtly implying that Afghanistan will similarly have its own redemption one day."
,"past":"All the characters in the novel feel the influence of the past, but none so much as Amir and Sohrab. In Sohrab’s case, his past has been so traumatizing that it affects all his behavior. The prolonged physical and sexual abuse he endured makes him flinch anytime Amir touches him. He also fears the abandonment he experienced when his parents died so much that he attempts suicide when Amir says he may have to go back to an orphanage. For Amir, the past is always with him, from the book’s first sentence, when he says he became what he is today at the age of twelve, to its final sentence. That’s because Amir defines himself by his past. His feelings of guilt for his past actions continue to motivate him. Amir even feels responsible for the Taliban murdering Hassan because he thinks he set in motion the events that led to Hassan’s death when when he pushed Hassan and Ali out of Baba’s house. As he says on the book’s first page, the past can never be buried."
,"male friendship": "The Kite Runner focuses nearly exclusively on male relationships. While the relationship between father and son is important to the novel, male friendship is central as well. Amir’s relationship with Hassan is the most obvious example. Though the two are constant companions, Amir’s superior social status causes a power difference between them, which is later complicated when Amir learns that Hassan is actually his half-brother. Amir realizes that the favor Baba showed Hassan was that of a father to a son, and he reflects on the way he let his jealousy corrupt his friendship with Hassan. Despite this problematic dynamic, Hassan is clearly a wonderful friend, as demonstrated by his willingness to support Amir even when it is difficult or dangerous to do so. This loyalty is evidenced most clearly by Hassan’s kite-running, and his refusal to give Assef the kite he runs for Amir, resulting in Assef raping Hassan as punishment. Rahim Khan is another important character for understanding male friendship in the novel. He is a friend to both Baba and Amir, and in those relationships, he takes the role of pushing back against the questionable choices both men make. Rahim Khan can take this role because he occupies the same social position as Baba and Amir. It is Rahim Khan who knows his friends’ innermost secrets—that Baba slept with Ali’s wife and Amir allowed Hassan’s rape—and yet he does not lord these secrets over them, instead choosing to be a voice of reason and call the other characters back to goodness. Rahim Khan’s morality is evident in his phone call to grown-up Amir, in which he states “there is a way to be good again.” As a friend, Rahim provides Amir with “a way to end the cycle” of betrayals and secrets."
, "racism": "Throughout The Kite Runner, racism is depicted both overtly and more subtly and systemically. Assef, the most overtly racist character in the novel, directly justifies his rape of Hassan by saying, “It’s just a Hazara.” Later, Assef compares Hazaras to garbage littering the “beautiful mansion” of Afghanistan, and he takes it upon himself to “take out the garbage” by murdering those he views as second-class citizens. Amir’s original failure to defend Hassan against Assef is surely motivated by cowardice and his desire to please Baba, but Amir is also able to justify his inaction because of the social distance he feels due to Hassan’s ethnic background. This racism becomes complicated when Amir later learns that he and Hassan were half-brothers. Amir finally publicly rejects his implicit racism when he instructs General Taheri that the General can never refer to Sohrab as “Hazara boy” again."
, "religion": "The Kite Runner illustrates the many ways characters practice Islam, and how a single religion can take on starkly different forms. Baba is not a religious man, and he openly mocks and questions the hypocrisy of Muslim leaders. Amir’s lack of religious upbringing later serves him well when it allows him to look past Soraya’s sexual history in a way that other Afghan men have been unwilling to do. On the other hand, Ali’s diligent recitation of daily prayers is depicted as honorable, and his devout faith marks him as one of the most admirably humble characters in the novel. When Amir feverishly, almost instinctively, starts praying after Sohrab’s suicide attempt, not only are the depths of Amir’s desperation revealed, but also the latent influence of Ali’s faith. Religious zealotry is used by other characters to justify horrific acts of cruelty. Assef, who becomes a Taliban leader, justifies his murder of Hazaras as “virtuous” and truly believes he is “doing God’s work.” Amir witnesses Assef stone two adulterers to death, then discovers how he has turned Sohrab into his own child prostitute, all in the name of Islam. Through this radicalized perversion of religion, Assef and the rest of the Taliban are able to carelessly justify anything, while Baba and Amir—who, for most of the novel, have little or no religious identity—are burdened by past mistakes that they must wrestle with."}
info_available = {"characters": characters_dict, "symbols": symbols_dict, "key facts": key_facts_dict, "themes": themes_dict}


#functions
#formats dictionary items into string
def make_dict_string(dictionary):
    item_string = ""
    for key in dictionary.keys():
       item_string += f"-{key}; \n"
    return item_string

def select_category():
    current_input= input(f"""\n Select a category to revise:
{make_dict_string(info_available)}
""").lower()

    return current_input


#print information, if input is 'enter' or 'next' print next item
#if back, select category if exit, print goodbye message
def print_info(item, dict, word):
    item_index = list(dict).index(item)
    item_number = item_index + 1
    #prints information
    print(f"""
    \n {item.upper()} ({word} {item_number} of {len(dict)}): \n    {dict[item]}""")
    current_input = input(f"\n Press ENTER for next {word} or type BACK/EXIT: ").lower()
    if current_input == "next" or current_input == "":
        if item_number == len(dict):
            item_index = 0
        else: item_index += 1
        next_item = list(dict)[item_index]
        print_info(next_item, dict, word)
    if current_input == "back":
        new_input = select_category()
        check_input(new_input)
    if current_input == "exit":
        print(exit_message)
    
#select specific item in dictionary, calls print info
#if not in dictionary sends error message and calls itself
def select_item(dict, word, string):
    category_input = input(f"\n \nPick a {word}:\n{string} or press ENTER for first \n" ).lower()
    if category_input in dict:
        print_info(category_input, dict, word)
    elif category_input == "":
        print_info(list(dict)[0], dict, word)
    elif category_input not in dict: 
            print(f"Sorry couldn't find info on {category_input}")
            time.sleep(1.3)
            select_item(dict, word, string)
    
#finds dictionary input refers to
#if not recognised, prompts for new input
def check_input(current_input):
    if current_input == "exit":
        print(exit_message)
        return
    for key in info_available.keys():
        if current_input == key:
            dictionary = info_available[key]
            select_item(dictionary, current_input[:-1], make_dict_string(dictionary))
        elif current_input == "":
            new_input = input(f"Please enter an option from the list above. \n").lower()
            check_input(new_input)
        elif current_input not in info_available.keys(): 
            new_input = input(f"Sorry couldn't find info on {current_input}.  Please enter an option from the list above. \n").lower()
            check_input(new_input)
   
        
    



#START of interface
print(f"\n \n Hello! Welcome to KiteRunner101, a simple study guide to Khaled Hosseini's bestselling novel.")
print("----------------------------------------------------------------------------------------------")

#prompts input from list of categories, checks that these are recognised
current_input = select_category()
check_input(current_input)

