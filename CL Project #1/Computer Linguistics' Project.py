from string import punctuation
from razdel import sentenize
from razdel import tokenize as razdel_tokenize
import numpy as np
from IPython.display import Image
from IPython.core.display import HTML

lenta = open('lenta.txt',encoding="utf-8").read()
rtt = open('russian_toxic_tweets.txt',encoding="utf-8").read()

#посчитаем длину корпусов
#print("Длина 1 -", len(lenta))
#print("Длина 2 -", len(rtt))

#примерно сравняем количество корпусов (сократим ленту)
lenta_shortened = (lenta[:2644296] + '..' if len(lenta) > 2644296 else lenta)
#print(len(lenta_shortened))

#функция нормализации текста
def normalize(text):
    normalized_text = [word.text.strip(punctuation) for word \
                                                            in razdel_tokenize(text)]
    normalized_text = [word.lower() for word in normalized_text if word and len(word) < 20 ]
    return normalized_text

#сравним по токенам
normalized_lenta = normalize(lenta_shortened)
normalized_rtt = normalize(rtt)
#print("Длина корпуса новостных текстов в токенах -", len(normalized_lenta))
#print("Длина корпуса твитов в токенах - ", len(normalized_rtt))

#и по уникальным токенам
#print("Уникальных токенов в корпусе новостных текстов -", len(set(normalized_lenta)))
#print("Уникальный токенов в корпусе твитов - ", len(set(normalized_rtt)))

#посчитаем самые частые слова
from collections import Counter
vocab_lenta = Counter(normalized_lenta)
vocab_rtt = Counter(normalized_rtt)
#print(vocab_lenta.most_common(10))
#print(vocab_rtt.most_common(10))

#посчитаем вероятности
probas_lenta = Counter({word:c/len(normalized_lenta) for word, c in vocab_lenta.items()})
#print(probas_lenta.most_common(20))
probas_rtt = Counter({word:c/len(normalized_rtt) for word, c in vocab_rtt.items()})
#print(probas_rtt.most_common(20))

#теперь с помощью этих вероятностей мы можем оценить, насколько рандомный
#текст соответствует публицистическому или разговорному стилю

#1 метод
#функция, которая рассчитает общую вероятность (перемножаем вероятности, т. к.
#нам нужно вероятность нескольких независимых событий (слов) возникающих одновременно

#def joint_probas(text, word_probas):
#    prob = 0
#    for word in normalize(text):
#        if word in word_probas:
#            prob += (np.log(word_probas[word]))
#        else:
#            prob += (np.log(1 / len(normalized_rtt)))
#        return np.exp(prob)

#посчитаем, какова вероятность встретить следующий новостной заголовок Яндекс.Дзена в обоих корпусах
phrase = 'В Twitter раскритиковали Зеленского за сравнение Путина с драконом'
#print(joint_probas(phrase, probas_rtt))
#print(joint_probas(phrase, probas_lenta))

#попробуем другой текст
phrase1 = 'Обидно, когда после свадьбы жена перестает следить за собой, а за тобой не перестает'
#print(joint_probas(phrase1, probas_rtt))
#print(joint_probas(phrase1, probas_lenta))

#2 метод
#посчитаем вероятности слов уже как зависимых событий (второе - от первого,
#третье - от второго и т.д.) с помощью подсчёта биграмм (Марковское предположение)

from nltk.tokenize import sent_tokenize
def ngrammer(tokens, n=2):
    ngrams = []
    for i in range(0,len(tokens)-n+1):
        ngrams.append(' '.join(tokens[i:i+n]))
    return ngrams

#добавим тэг начала предложения, чтобы мы могли также посчитать вероятность
#первого слова

sentences_lenta = [['<start>'] + normalize(text) for text in sent_tokenize(lenta_shortened[:2644296])]
sentences_rtt = [['<start>'] + normalize(text) for text in sent_tokenize(rtt[:2644296])]

#подсчёт биграмм
unigrams_lenta = Counter()
bigrams_lenta = Counter()

for sentence in sentences_lenta:
    unigrams_lenta.update(sentence)
    bigrams_lenta.update(ngrammer(sentence))

unigrams_rtt = Counter()
bigrams_rtt = Counter()

for sentence in sentences_rtt:
    unigrams_rtt.update(sentence)
    bigrams_rtt.update(ngrammer(sentence))

#посчитаем условную вероятность (количество всех вхождений / на
#количество вхождений первого слова)
def joint_probas_markov(text, word_counts, bigram_counts):
    prob = 0
    for ngram in ngrammer(['<start>'] + normalize(phrase)):
        word1, word2 = ngram.split()
        if word1 in word_counts and ngram in bigram_counts:
            prob += np.log(bigram_counts[ngram] / word_counts[word1])
        else:
            prob += np.log(2e-5)

    return np.exp(prob)

#проверим, что получилось
print(joint_probas_markov(phrase, unigrams_lenta, bigrams_lenta) > joint_probas_markov(phrase, unigrams_rtt, bigrams_rtt))
print(joint_probas_markov(phrase1, unigrams_lenta, bigrams_lenta) > joint_probas_markov(phrase1, unigrams_rtt, bigrams_rtt))

#print(joint_probas_markov(phrase, unigrams_lenta, bigrams_lenta))
#print(joint_probas_markov(phrase, unigrams_rtt, bigrams_rtt))
#print(joint_probas_markov(phrase1, unigrams_lenta, bigrams_lenta))
#print(joint_probas_markov(phrase1, unigrams_rtt, bigrams_rtt))


