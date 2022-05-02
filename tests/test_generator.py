import unittest

from buzz import generator


def test_sample_single_word():
    my_list = ('foo', 'bar', 'foobar')
    word = generator.sample(my_list)
    assert word in my_list


def test_sample_multiple_words():
    my_list = ('foo', 'bar', 'foobar')
    words = generator.sample(my_list, 2)
    assert len(words) == 2
    assert words[0] in my_list
    assert words[1] in my_list
    assert words[0] is not words[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
