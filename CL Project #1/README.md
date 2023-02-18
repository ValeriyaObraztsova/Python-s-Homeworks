                                        Контролируемый язык на этапе предобработки текста для осуществления машинного перевода

1) *Keywords*: controlled language, text pre-processing, length of the sentence, pronouns, style, stylistic errors, stylistic dictionaries, collocations, anaphoras/cataphoras, antecedent, smart search, errors marker, 10 rules of controlled language by U.Muegge, single-meaning words, homonyms

2) *Ссылки на источники* 

|                            reference_link                                         | reference_name | comments         |
| -------------                                                                     | -------------  | ---------------  |
| http://www.muegge.cc/controlled-language.htm#A_controlled_language_with_ten_rules | Uwe Muegge     | Здесь чётко и вкратце о том, что такое КЯ словами самого основоположника + сами 10 правил  | 
| https://www.rush-analytics.ru/blog/programmy-dlya-ispravleniya-v-tekste-razbor-primerov-i-osnovnye-osobennosti | Дмитрий Цытрош | Здесь можно посмотреть примерный функкционал похожих программ по исправлению ошибок в русском тексте и определиться с собственным диапазоном функций поиска нашей программы |
| https://www.lexilogos.com/english/dictionary.htm | без автора | В ссылке полный набор гиперссылок на словари, которые понадобятся для возможной проверки и исправления самых примитивный ошибок |

3) *Abstract.* 
Первая версия программы будет направлена только на поиск мест в любом тексте, в котором онлайн-переводчик может совершить ошибку или не совсем корректно перевести без предварительной обработки. Правило будет выделять в тексте места, на которые специалисту, занимающимся предобработкой текста, будет необходимо обратить особое внимание и по возможности "поддаться" машине и притивизировать то или иной место, выделенное программой. Прежде, чем осуществлять поиск ошибочный мест, правило будет определять стиль загруженного текста по процентному соотношению (например, официально-деловой - 78 %, публицистический - 8 %, научный - 5 %, научно-популярный - 3 %, разговорный - 3%, художественный - 3 %), чтобы на следующем этапе придерживаться данного словаря для поиска неточностей на лексическом и стилистическом уровнях. После подборя нужного стиля, использования загруженного словаря и поиска "потенциально опасных" мест в тексте, программа может предложить свой вариант исправления на необязательной основе (если у неё есть "идеи", она может предложить человеку свой "вариант", если же нет, то программа пишет 0 вариантов исправления. Сам этап исправления уже является необязательным, поэтому на него можно будет выделить время (если таковое будет оставаться перед финальной защитой проекта) только после того как будут чётко соблюдаться все предыдущие этапы предобработки текста.

4) *Данные:* Наше правило должно работать при загрузке любого вида текста. Для примера можно взять три разных типа текста, например, отрывок из художественного произведения, инструкцию по эксплуатации и новость с какого-либо информационного источника. Для интереса можно попробовать загрузить туда чей-то твит или другой текст с менее очевидной структурой.

5) *Актуальность:* Я плотно занималась этой темой при написании бакалаврской работы. Всё оказалось намного интереснее, чем я ожидала. Очень хотела бы попробовать такой принцип совершенствования работы онлайн переводчика. Можно по-разному реализовывать эту идею: можно вынести её в отдельный этап (ступеньку) загрузки текста в онлайн-переводчик и предварительной обработки (но здесь мы заходим в тупик, так как пока у меня нет идей того, как программа сама может заниматься исправлением выделенных ею "опасных мест", поэтому на этом этапе, наверное, вмешательство человека неизбежно), а можно вообще создать отдельное программное обеспечение, которое будет заниматься только машинной предварительной обработкой текста. 

6) *Пайплайн работы:*
    -) Выбрать перечень словарей всех стилей английского языка, которые будут использоваться программой для определения стиля загружаемого текста (напр. официально-деловой, научный, художественный, разговорный, сленг и т.п.);
    -) "Загрузить" их в программу и "попросить" её при загрузке и анализе текстов пользовться этими словарями;
    -) Написать правило в питоне, согласно которому программа будет определять стиль загруженного текста в процентном соотношении того перечня стилей текста, который мы зададим) / произвести лемматизацию загруженного текста;
    -) Выбрать несколько правил У. Мюгге и попробовать "научить" программу выделять эти критерии в загруженном тексте
    
7) *Сложности:* могут возникнуть на этапе "загрузки" словарей (не совсем пока понимаю, как это осуществлять. Вижу это как загрузку памяти переводов, но плохо представляю, как это реализовать в питоне и какими методами пользоваться), а также на этапе "выделения" в тексте "опасных" мест.

8) *Что хотели бы делать после:* реализовать все 10 правил Мюгге! (но пока это выглядит крайне невыполнимо для меня =D)
9) *Что угодно, что хотели бы добавить:* спасибо, что дочитали до конца! Будет здорово, если получу обратную связь по поводу всей этой писанины.

    