#!/bin/python3
import copy


def _adjacent(word1, word2):
    if len(word1) == len(word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
        if count <= 1:
            print("1st word =", word1)
            print("2nd word=", word2)
            return True
        return False
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.
    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    '''


def verify_word_ladder(ladder):
    if not ladder:
        return False
    if len(ladder) == 1:
        return True
    for word in range(0, len(ladder) - 1):
        if not _adjacent(ladder[word], ladder[word + 1]):
            return False
            print("ladder=", ladder)
    return True
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    from collections import deque
    with open(dictionary_file, 'r') as f:
        text = f.read()
        words = text.split()
    if start_word == end_word:
        return [start_word]
    if len(start_word) != len(end_word):
        return None
    stack = []
    stack.append(start_word)
    queue = deque()
    queue.append(stack)

    while len(queue) != 0:
        current_stack = queue.popleft()
        for word in list(words):
            if _adjacent(current_stack[-1], word):
                words.remove(word)
                if word == end_word:
                    current_stack.append(word)
                    return current_stack
                copied_stack = copy.copy(current_stack)
                copied_stack.append(word)
                queue.append(copied_stack)
    else:
        return None

    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny',
    'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots',
    'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.

    '''
