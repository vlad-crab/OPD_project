define d = Character('Добросплав', color="#c8ffc8", image='dobrosplav')
define f = Character('Имя2', color='#ef3038', image="friend")

init:
    $ left2 = Position(xalign=0.2)
    $ right2 = Position(xalign=0.8)
    $ dwithf = Position(yalign=1.5, xalign=0.8)

label start:

    scene bg bedroom
    with fade

    d "«Доброе утро» никогда не бывало для меня добрым.{w} Привыкнуть просыпаться так рано невозможно!"

    show dobrosplav sad
    with dissolve

    d "Сегодня в расписании нет ни одного предмета, который я буду сдавать на ЕГЭ, так что идти необязательно."

    d "Правда, если останусь, то всё равно не буду ничего делать."

    d "Так что оправдать перед самим собой прогул не выйдет… {w}Придётся идти."

    scene bg bathroom
    with fade

    show dobrosplav normal
    with easeinleft

    "Умывается"

    scene bg kitchen
    with fade

    show dobrosplav normal
    with easeinleft

    "Ест"
    "Включает компьютер"

    d surprise "Чёрт! Я ж уже решил пойти сегодня!"

    "Выключает компьютер"

    d smile "СИЛА ВОЛИ! Надо уже выходить."

    scene bg street
    with fade

    show dobrosplav normal
    with moveinright

    hide dobrosplav
    with moveoutleft

    scene bg school
    with fade

    show dobrosplav surprise
    with moveinright

    d "Как-то мало людей"

    hide dobrosplav
    with moveoutleft

    scene bg classroom
    with fade

    show friend at left2
    with moveinleft

    show dobrosplav smile at dwithf
    with moveinright

    d "Привет! Где все?"

    f "Сообщение в чате не видел?{w} Первый урок отменили."

    d @ surprise "Ясно. А ты тогда чего тут?"

    f '''
    Учитель по общаге с ноутом просил помочь.
    Тот у него работает только от сети.
    Аккум не родной, вот он и решил, что проблема в этом.
    '''

    d "А на самом деле, хах?"

    f "Контакт отвалился. Тут я бессилен…"

    d "Ахахахахахаха!"

    d "У тебя ещё что-то есть сегодня?"

    f "Сам знаешь – последнее время у меня одна забота."

    d @ sad "Да ну… Пусть лучше... Как его там?"

    f "Сергей Дмитриевич"

    d @ sad"Вот! Пусть этот Сергей Димыч сервер и настраивает{w}, а ты – просто школьник! {w}Даже ведь не платят!"

    f "Зато интересно!"

    d @ normal "Ну да, ну да… {w}Дай ка сюда домашку, хоть спишу"

    f "Сегодня ж одна гуманитарщина!{w} Сам ничего не делал, больно надо"

    d "Справедливо. Я тогда до библиотеки прогуляюсь. {w}Серверная по дороге, ты со мной?"

    f "Пошли"

    hide dobrosplav
    with moveoutright

    hide friend
    with moveoutright

    scene bg school corridor
    with fade

    show friend at left2
    with moveinright

    show dobrosplav smile at dwithf
    with moveinright

    f "Блин, свой то ноут я забыл взять!"

    d "Ладно, пошевеливайся. Второй то урок у нас не отменяли"

    hide friend
    with moveoutright

    d "Это что серверная?"

    scene bg server room
    with fade

    show dobrosplav surprise
    with moveinleft

    d "Вау, отдельная комнутушка, шикарно. Что тут вообще есть?"

    d "Придумал! Имя2 же думает, что я в библиотеку пошёл, а я тут его подкараулю!"

    d "Надо спрятаться"

    show dobrosplav smile at right:

    d "..."

    d "Ну же! Что-то я его даже не слышу"

    d "..."

    d @ surprise "Слышу только странное гудение{w}, которого, по идее, здесь быть не должно, ведь ничего не работает!"

    d "О! Слышу, идёт!"

    d "Да блин, что гудит то, не могу понять. Он мне на нервы действует!"

    d "И вообще, такое странное чувство…"

    hide dobrosplav
    with dissolve


    return
