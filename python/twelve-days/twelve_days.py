def recite(start_verse, end_verse):
    '''
    Assume: start_verse is less than end_verse
    '''
    days = {
                1: ("first", "a Partridge in a Pear Tree"),
                2: ("second", "two Turtle Doves"),
                3: ("third", "three French Hens"),
                4: ("fourth", "four Calling Birds"),
                5: ("fifth", "five Gold Rings"),
                6: ("sixth", "six Geese-a-Laying"),
                7: ("seventh", "seven Swans-a-Swimming"),
                8: ("eighth", "eight Maids-a-Milking"),
                9: ("ninth", "nine Ladies Dancing"),
                10: ("tenth", "ten Lords-a-Leaping"),
                11: ("eleventh", "eleven Pipers Piping"),
                12: ("twelfth", "twelve Drummers Drumming")
            }

    def msg_day(day, coll=None):
        '''
        day is a digit
        '''
        if coll is None:
            coll = []
        coll.append(days[day][1])
        if day == 1:
            return coll
        else:
            return msg_day(day-1, coll)

    def get_answer(day, msgs):
        '''
        day is a digit
        '''
        english_day = days[day][0]
        prefix = f"On the {english_day} day of Christmas my true love gave to me: "
        last = msgs[-1] + "."
        if day > 1:
            day_msg = prefix + ", ".join(msgs[-day:-1]) + ", and " + last
        else:
            day_msg = prefix + last
        return day_msg
        
    ans = []      
    msgs = msg_day(end_verse)
    for day in range(start_verse, end_verse + 1):
        day_msg = get_answer(day, msgs)
        ans.append(day_msg)
    return ans
