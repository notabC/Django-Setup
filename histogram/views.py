# histogram/views.py
from django.shortcuts import render
from django.http import HttpResponse

def generate_histogram(filename):
    bins = {i: 0 for i in range(0, 101, 10)}
    try:
        with open(filename, 'r') as file:
            numbers = [int(line.strip()) for line in file if line.strip()]
        
        for num in numbers:
            if 1 <= num <= 100:
                bin_index = ((num - 1) // 10) * 10
                bins[bin_index] += 1
        
        histogram = []
        for i in range(0, 91, 10):
            start = i + 1
            end = i + 10
            count = bins[i]
            stars = '*' * count
            histogram.append(f"{start:>2} - {end:>3} | {stars}")
        
        stars = '*' * bins[90]
        histogram.append(f"91 - 100 | {stars}")
        
        return '\n'.join(histogram)
    
    except FileNotFoundError:
        return "Error: File not found"
    except ValueError:
        return "Error: File contains invalid data"

def get_histogram(request):

    histogram_text = generate_histogram('grades.txt')
    
    histogram_html = f"<pre>{histogram_text}</pre>"
    
    return HttpResponse(histogram_html)