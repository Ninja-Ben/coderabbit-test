# simple_utils.py - A tiny utility library

def reverse_string(text):
    """
    Return the string with characters in reverse order.
    
    Parameters:
    	text (str): The string to reverse
    
    Returns:
    	str: The reversed string
    """
    return text[::-1]

def count_words(sentence):
    """
    Count the number of words in a sentence.
    
    Parameters:
    	sentence (str): A string containing words separated by whitespace
    
    Returns:
    	int: The number of words in the sentence
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature value from Celsius to Fahrenheit.
    
    Parameters:
        celsius: The temperature in Celsius.
    
    Returns:
        The equivalent temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32
